 
function sel = tournament_selection(pop)
N = numel(pop);
i = randi(N); j = randi(N);
a = pop(i); b = pop(j);
if a.Rank < b.Rank, sel = a;
elseif b.Rank < a.Rank, sel = b;
else
    if a.CrowdingDistance > b.CrowdingDistance, sel = a; else sel = b; end
end
end
