n = 50;
x = y = linspace(-8, 8, n);
[xx, yy] = meshgrid(x, y);
r = sqrt(xx .^2 + yy .^2) + eps;
c = 5 * sin(r) ./ r;
h = surf(xx, yy, c, c);
shading interp