function [T, Y] = runge_kutta(f, cond, start, stop, step)
    N = floor((stop - start)/step);
    s = size(cond);
    Y = zeros(N+1, s(1));
    Y(1,:) = cond;
    T = zeros(N+1, 1);
    T(1) = start;
    for i = 2:N+1
       T(i) = T(i-1) + step;
       k_1 = f(T(i-1), Y(i-1,:));
       k_2 = f(T(i-1)+step/2, Y(i-1,:)+k_1*step/2);
       k_3 = f(T(i-1)+step/2, Y(i-1,:)+k_2*step/2);
       k_4 = f(T(i-1)+step, Y(i-1,:)+k_3*step);
       Y(i,:) = Y(i-1,:) + step/6*(k_1+2*k_2+2*k_3+k_4);
    end
end