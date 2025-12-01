
function [child1, child2] = genetic_operators(p1, p2, VarMin, VarMax, pc, eta_c, pm, eta_m)
nVar = numel(p1); child1 = p1; child2 = p2;
if rand <= pc
    for j=1:nVar
        u = rand;
        if u <= 0.5, beta = (2*u)^(1/(eta_c+1));
        else, beta = (1/(2*(1-u)))^(1/(eta_c+1)); end
        child1(j) = 0.5*((1+beta)*p1(j) + (1-beta)*p2(j));
        child2(j) = 0.5*((1-beta)*p1(j) + (1+beta)*p2(j));
    end
end
for j=1:nVar
    if rand <= pm
        u = rand;
        if u < 0.5, delta = (2*u)^(1/(eta_m+1)) - 1;
        else, delta = 1 - (2*(1-u))^(1/(eta_m+1)); end
        child1(j) = child1(j) + delta*(VarMax(j) - VarMin(j));
        u2 = rand;
        if u2 < 0.5, delta2 = (2*u2)^(1/(eta_m+1)) - 1;
        else, delta2 = 1 - (2*(1-u2))^(1/(eta_m+1)); end
        child2(j) = child2(j) + delta2*(VarMax(j) - VarMin(j));
    end
end
child1 = max(child1, VarMin); child1 = min(child1, VarMax);
child2 = max(child2, VarMin); child2 = min(child2, VarMax);
end
