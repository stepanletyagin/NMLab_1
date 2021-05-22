clc;
clear;
start = 0; stop = 100;
nu = 0.5;
cond = [0.1; 0.1; 0.07];
f = @(t, y) [(nu-1)*y(1)-y(2)+y(1)*y(3) y(1)+...
    +(nu-1)*y(2)+y(2)*y(3) nu*y(3)-y(1)^2-y(2)^2-y(3)^2];
step = 0.05; 
[T, Y] = runge_kutta(f, cond, start, stop, step);

                    
figure('Name','TimePlot');
plot(T, Y)
axis([0 70 -1 1])
figure('Name','PhazePlot');
plot3(Y(:,1),Y(:,2),Y(:,3))
grid on
axis equal


figure('Name','Y_1');
plot(T, Y(:,1))
grid on
axis equal
figure('Name','Y_2');
plot(T, Y(:,2))
grid on
axis equal