
function [nVar, VarMin, VarMax] = get_problem_details(problem_name)
switch lower(problem_name)
    case 'zdt1', nVar=30; VarMin=zeros(1,nVar); VarMax=ones(1,nVar);
    case 'zdt3', nVar=30; VarMin=zeros(1,nVar); VarMax=ones(1,nVar);
    case 'kursawe', nVar=3; VarMin=-5*ones(1,nVar); VarMax=5*ones(1,nVar);
    case 'fonseca', nVar=3; VarMin=-4*ones(1,nVar); VarMax=4*ones(1,nVar);
    case 'schaffer1', nVar=1; VarMin=-100; VarMax=100;
    case 'schaffer2',  nVar = 1; VarMin = -5; VarMax = 10;
    case 'binhkorn', nVar=2; VarMin=[0,0]; VarMax=[5,3];
    case 'chankonghaimes', nVar=2; VarMin=[-20,-20]; VarMax=[20,20];
    otherwise, error('Unknown problem'); 
end
end
