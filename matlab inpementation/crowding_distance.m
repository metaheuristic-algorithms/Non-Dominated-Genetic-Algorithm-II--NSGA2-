
function pop = crowding_distance(pop, fronts)
N = numel(pop);
for i=1:N, pop(i).CrowdingDistance = 0; end
for f=1:numel(fronts)
    F = fronts{f};
    if isempty(F), continue; end
    M = numel(pop(1).Objectives);
    Obj = zeros(numel(F), M);
    for ii=1:numel(F), Obj(ii,:) = pop(F(ii)).Objectives; end
    for m=1:M
        [vals, order] = sort(Obj(:,m));
        fmax = max(vals); fmin = min(vals);
        pop(F(order(1))).CrowdingDistance = inf;
        pop(F(order(end))).CrowdingDistance = inf;
        for k=2:(numel(F)-1)
            if fmax - fmin == 0, cont = 0; else cont = (vals(k+1)-vals(k-1)) / (fmax - fmin); end
            if isfinite(pop(F(order(k))).CrowdingDistance)
                pop(F(order(k))).CrowdingDistance = pop(F(order(k))).CrowdingDistance + cont;
            end
        end
    end
end
end
