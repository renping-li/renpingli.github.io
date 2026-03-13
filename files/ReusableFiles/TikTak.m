% TikTak Global Optimizer
% =======================
%
% MATLAB implementation of the TikTak algorithm for global optimization,
% following Arnoud, Guvenen, & Kleineberg (2019).
%
% TikTak is designed for objective functions that are expensive to evaluate
% (e.g., simulated method of moments in structural estimation). It combines:
%
%   Global stage  -- Evaluate the objective at N quasi-random Sobol points
%                    spread across the parameter space.
%   Local stage   -- Select the N* best starting points. For each, form a
%                    weighted average with the current best estimate, then
%                    run Nelder-Mead (fminsearchbnd) from that point.
%                    The weight on the prior best increases over iterations,
%                    so early starts explore broadly and later starts
%                    refine near the optimum.
%
% Reference:  https://www.fatihguvenen.com/tiktak
%
% Usage:
%   1. Define your objective function:
%        function err = Objective(params, <your args>)
%   2. Set LowerBound and UpperBound vectors for each parameter.
%   3. Adjust N (Sobol draws) and N_star (local starts) below.
%   4. Run this script.
%
% Requirements: Optimization Toolbox (fminsearch), fminsearchbnd (free,
%               by John D'Errico on MATLAB File Exchange).


%% ========================================================================
%  USER SETTINGS -- edit this section
%  ========================================================================

% Number of Sobol points for the global stage
N = 10000;

% Number of best starting points for the local stage
N_star = 100;

% Maximum function evaluations per Nelder-Mead run
MaxFunEvals_global = 0;      % set > 0 to also run N-M in the global stage
MaxFunEvals_local  = 500;
MaxFunEvals_final  = 2000;   % final refinement from the best local result

% Parameter bounds (example with 3 parameters -- replace with your own)
%                     Lower       Upper       Description
LowerBound(1) = 0;   UpperBound(1) = 100;   % parameter 1
LowerBound(2) = 0;   UpperBound(2) = 10;    % parameter 2
LowerBound(3) = 0;   UpperBound(3) = 1;     % parameter 3

nParams = length(LowerBound);

% Output file paths
global_output = 'TikTak_global_results.mat';
local_output  = 'TikTak_local_results.mat';
final_output  = 'TikTak_final_estimate.mat';


%% ========================================================================
%  GLOBAL STAGE -- evaluate objective at Sobol quasi-random points
%  ========================================================================

% Generate Sobol sequence spanning the parameter space
rng(314);
pset       = sobolset(nParams, 'Skip', 1e6);
pset       = scramble(pset, 'MatousekAffineOwen');
SobolDraws = net(pset, N);
SobolParams = LowerBound + (UpperBound - LowerBound) .* SobolDraws;

% Evaluate objective at each Sobol point
guess_all = nan(N, nParams + 1);   % col 1 = error, cols 2:end = params

for n = 1:N
    params = SobolParams(n, :);
    err = Objective(params);       % <-- replace with your objective call
    guess_all(n, 1)          = err;
    guess_all(n, 2:end)      = params;

    if mod(n, 500) == 0
        fprintf('Global stage: %d / %d points evaluated\n', n, N);
        save(global_output, 'guess_all');
    end
end

save(global_output, 'guess_all');

% Sort by objective value and pick the N* best starting points
guess_all  = sortrows(guess_all, 1);
guess_best = guess_all(1:N_star, :);
fprintf('Global stage complete. Best objective = %.6f\n', guess_best(1,1));


%% ========================================================================
%  LOCAL STAGE -- Nelder-Mead from weighted starting points
%  ========================================================================

fmoption = optimset('MaxFunEvals', MaxFunEvals_local, 'Display', 'iter');
wisdom   = inf(N_star, nParams + 1);   % col 1 = error, cols 2:end = params

for i = 1:N_star

    % ----- Form the starting point -----
    s_i = guess_best(i, 2:end);        % i-th Sobol candidate

    if i == 1
        % First iteration: start directly from the best Sobol point
        x0 = s_i;
    else
        % Weighted average: prior best <--> current Sobol candidate
        % Weight on prior best grows from ~0.1 toward ~1 as i increases,
        % so early iterations explore and later iterations refine.
        weight_prior = min(max(0.1, (i / N_star)^0.7), 0.995);
        [~, best_idx] = min(wisdom(1:i-1, 1));
        x_best = wisdom(best_idx, 2:end);
        x0 = weight_prior * x_best + (1 - weight_prior) * s_i;
    end

    % ----- Check feasibility of starting point -----
    err0 = Objective(x0);             % <-- replace with your objective call
    if ~isfinite(err0)
        fprintf('Local %d/%d: infeasible start, skipping.\n', i, N_star);
        wisdom(i, 1) = inf;
        continue
    end

    % ----- Run Nelder-Mead -----
    [best_params, best_err] = fminsearchbnd( ...
        @(p) Objective(p), ...         % <-- replace with your objective call
        x0, LowerBound, UpperBound, fmoption);

    wisdom(i, 1)     = best_err;
    wisdom(i, 2:end) = best_params;
    fprintf('Local %d/%d: objective = %.6f\n', i, N_star, best_err);
    save(local_output, 'wisdom');
end

wisdom = sortrows(wisdom, 1);
save(local_output, 'wisdom');
fprintf('Local stage complete. Best objective = %.6f\n', wisdom(1,1));


%% ========================================================================
%  FINAL REFINEMENT -- one last Nelder-Mead run with more evaluations
%  ========================================================================

fmoption_final = optimset('MaxFunEvals', MaxFunEvals_final, 'Display', 'iter');

[StructParams, FinalError] = fminsearchbnd( ...
    @(p) Objective(p), ...             % <-- replace with your objective call
    wisdom(1, 2:end), LowerBound, UpperBound, fmoption_final);

fprintf('\n=== Final estimate ===\n');
fprintf('Objective = %.6f\n', FinalError);
fprintf('Parameters:\n'); disp(StructParams);
save(final_output, 'StructParams', 'FinalError');
