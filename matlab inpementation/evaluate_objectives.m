
function [F, constraints] = evaluate_objectives(x, problem_name)
switch lower(problem_name)
    case 'zdt1'
        f1 = x(1); g = 1 + 9/(numel(x)-1)*sum(x(2:end)); h = 1 - sqrt(f1/g); f2 = g*h; F=[f1,f2]; constraints=[];
    case 'zdt3'
        f1 = x(1); g = 1 + 9/(numel(x)-1)*sum(x(2:end)); h = 1 - sqrt(f1/g) - (f1/g).*sin(10*pi*f1); f2 = g*h; F=[f1,f2]; constraints=[];
    case 'kursawe'
        f1 = -10*(exp(-0.2*sqrt(x(1)^2+x(2)^2)) + exp(-0.2*sqrt(x(2)^2+x(3)^2)));
        f2 = sum(abs(x).^0.8 + 5*sin(x.^3));
        F=[f1,f2]; constraints=[];
    case 'fonseca'
        n = numel(x); f1 = 1 - exp(-sum((x - 1/sqrt(n)).^2)); f2 = 1 - exp(-sum((x + 1/sqrt(n)).^2));
        F=[f1,f2]; constraints=[];
    case 'schaffer1'
        f1 = x(1)^2; f2 = (x(1)-2)^2; F=[f1,f2]; constraints=[];
    case 'schaffer2'
        x1 = x(1);
        % piecewise f1 as in the paper:
        if x1 <= 1
            f1 = -x1;
        elseif x1 <= 3
            f1 = x1 - 2;
        elseif x1 <= 4
            f1 = 4 - x1;
        else
            f1 = x1 - 4;
        end
        f2 = (x1 - 5)^2; F = [f1, f2]; constraints = [];

    case 'binhkorn'
        x1=x(1); x2=x(2); f1=4*x1^2+4*x2^2; f2=(x1-5)^2+(x2-5)^2;
        g1 = (x1 - 5)^2 + x2^2 - 25;
        g2 = 7.7 - ((x1 - 8)^2 + (x2 + 3)^2);
        F=[f1,f2]; constraints=[g1,g2];
    case 'chankonghaimes'
        x1=x(1); x2=x(2); f1=2+(x1-2)^2+(x2-1)^2; f2=9*x1 - (x2-1)^2;
        g1 = x1^2 + x2^2 - 225; g2 = x1 - 3*x2 + 10;
        F=[f1,f2]; constraints=[g1,g2];
    otherwise, error('Unknown problem'); end
end
