function [pop, fronts] = non_dominated_sort(pop)
% Performs non-dominated sorting and assigns Rank to each individual.
N = numel(pop);
fronts = {};           % cell array of fronts
S = cell(N,1);         % S{p}: set of solutions dominated by p
n = zeros(N,1);        % n(p): number of solutions that dominate p
rank = zeros(N,1);

% Precompute constraint violations if Constraints field exists
for i = 1:N
    if isempty(pop(i).Constraints)
        pop(i).Constraints = [];
    end
end

% Main pairwise dominance computations
for p = 1:N
    S{p} = [];
    n(p) = 0;
    for q = 1:N
        if p == q, continue; end
        dom = dominates(pop(p), pop(q));
        if dom == 1
            S{p} = [S{p}, q];
        elseif dom == -1
            n(p) = n(p) + 1;
        end
    end
    if n(p) == 0
        rank(p) = 1;
        % initialize fronts{1} if needed, then append p
        if isempty(fronts)
            fronts{1} = p;
        else
            fronts{1} = [fronts{1}, p];
        end
    end
end

% Build subsequent fronts
i = 1;
while true
    if i > numel(fronts) || isempty(fronts{i})
        break;
    end
    Q = [];
    for idx = fronts{i}
        for q = S{idx}
            n(q) = n(q) - 1;
            if n(q) == 0
                rank(q) = i + 1;
                Q = [Q, q];
            end
        end
    end
    if isempty(Q)
        break;
    end
    i = i + 1;
    fronts{i} = Q;
end

% Assign ranks to population
for i = 1:N
    pop(i).Rank = rank(i);
end

end

% --------------------
% Local helper: dominance test using Deb's constraint-domination principle
function d = dominates(a,b)
% Returns 1 if a dominates b, -1 if b dominates a, 0 otherwise

% Ensure Objectives and Constraints exist
fa = a.Objectives; fb = b.Objectives;
if isempty(a.Constraints), ca = 0; else ca = sum(max(0, a.Constraints)); end
if isempty(b.Constraints), cb = 0; else cb = sum(max(0, b.Constraints)); end

% Constraint-domination
if ca == 0 && cb > 0
    d = 1; return;
elseif cb == 0 && ca > 0
    d = -1; return;
elseif ca > 0 && cb > 0
    if ca < cb
        d = 1;
    elseif cb < ca
        d = -1;
    else
        d = 0;
    end
    return;
else
    % both feasible: Pareto dominance
    le = all(fa <= fb);
    lt = any(fa < fb);
    if le && lt
        d = 1;
    elseif all(fb <= fa) && any(fb < fa)
        d = -1;
    else
        d = 0;
    end
    return;
end
end
