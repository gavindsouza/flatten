clear all, close all, clc

%% Load full image
disp('Loading full image...')
A=imread("C:\Users\Gavin\Desktop\Code\Python\other_projects\flatten\flatten\samples\images\blue_flower_very_small.jpg");
figure(3);
imshow(A)

%% Make image black and white
Abw2=rgb2gray(A); 
[nx,ny]=size(Abw2); 
figure(1), subplot(2,2,1), imshow(Abw2)
title('Original image','FontSize',18)

%% Compute the FFT of our image using fft2
disp('Doing FFT analysis for sparsity check...')
tic;
At=fft2(Abw2); 

F = log(abs(fftshift(At))+1);
F = mat2gray(F); % Use mat2gray to scale the image between 0 and 1
figure(4)
imshow(F,[]); % Display the result

%% Zero out all small coefficients and inverse transform
disp('Zeroing out small Fourier coefficients...')
tic;
count_pic=2; 
for thresh=.1*[0.001 0.005 0.01] * max(max(abs(At)))
    ind = abs(At)>thresh;
    count = nx*ny-sum(sum(ind));
    Atlow = At.*ind;
    percent=100-count/(nx*ny)*100;
    Alow=uint8(ifft2(Atlow)); 
    figure(1), subplot(2,2,count_pic), imshow(Alow); count_pic=count_pic+1;
    drawnow
    title([num2str(percent) '% of FFT basis'],'FontSize',18)
end
disp(['    done. (' num2str(toc) 's)'])

%% 
figure
Anew = imresize(Abw2,.1);
surf(double(Anew));
