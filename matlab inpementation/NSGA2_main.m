
% NSGA2_main.m - Main script for NSGA-II (educational implementation)
clear; clc; close all;
% Choose problem: 'ZDT1','ZDT3','Kursawe','Fonseca','Schaffer1','Schaffer2','BinhKorn','ChankongHaimes'
problem_name = 'ZDT3';

% Algorithm parameters
N = 50; MaxIt = 100;
pc = 0.9; eta_c = 15;
% get problem details
[nVar, VarMin, VarMax] = get_problem_details(problem_name);
pm = 1/nVar; eta_m = 20;

% initialize population
empty.Position=[]; empty.Objectives=[]; empty.Constraints=[];
empty.ConstraintViolation=0; empty.Rank=0; empty.CrowdingDistance=0;
pop = repmat(empty, N, 1);
for i=1:N
    pop(i).Position = unifrnd(VarMin, VarMax, [1,nVar]);
    [pop(i).Objectives, pop(i).Constraints] = evaluate_objectives(pop(i).Position, problem_name);
    pop(i).ConstraintViolation = sum(max(0, pop(i).Constraints));
end
[pop, F] = non_dominated_sort(pop);
pop = crowding_distance(pop, F);

% main loop
for it=1:MaxIt
    fprintf('Iter %d/%d\n', it, MaxIt);
    offspring = repmat(empty, N, 1);
    idx=1;
    while idx<=N
        p1 = tournament_selection(pop);
        p2 = tournament_selection(pop);
        [c1,c2] = genetic_operators(p1.Position, p2.Position, VarMin, VarMax, pc, eta_c, pm, eta_m);
        offspring(idx).Position = c1;
        if idx+1<=N, offspring(idx+1).Position = c2; end
        idx = idx + 2;
    end
    % evaluate offspring
    for i=1:N
        [offspring(i).Objectives, offspring(i).Constraints] = evaluate_objectives(offspring(i).Position, problem_name);
        offspring(i).ConstraintViolation = sum(max(0, offspring(i).Constraints));
    end
    % combine and select
    combined = [pop; offspring];
    [combined, F] = non_dominated_sort(combined);
    combined = crowding_distance(combined, F);
    % build new population
    newpop = repmat(empty, N, 1); count=0; fidx=1;
    while count < N
        front = F{fidx};
        if count + numel(front) <= N
            for j=1:numel(front), count=count+1; newpop(count)=combined(front(j)); end
        else
            cds = arrayfun(@(x) combined(x).CrowdingDistance, front);
            [~, order] = sort(cds, 'descend');
            need = N - count;
            for j=1:need, idx_sel = front(order(j)); count = count+1; newpop(count)=combined(idx_sel); end
        end
        fidx = fidx + 1;
    end
    pop = newpop;
    [pop, F] = non_dominated_sort(pop);
    pop = crowding_distance(pop, F);
end

% plot final Pareto (front 1)
FinalPareto = pop([pop.Rank]==1);
Obj = vertcat(FinalPareto.Objectives);
figure; plot(Obj(:,1), Obj(:,2),'r*'); grid on; xlabel('f_1'); ylabel('f_2');
title(['Pareto Front - ' problem_name]);
