
// Display mode
mode(0);

// Display warning for floating point exception
ieee(1);

//clearxdel(winsid())
clc

//% Load full image
disp("Loading full image...")
// !! L.5: Matlab function imread not yet converted, original calling sequence used.
A = imread("C:\Users\Gavin\Desktop\Code\Python\other_projects\flatten\flatten\samples\images\blue_flower_very_small","jpeg");
// !! L.6: Matlab function figure not yet converted, original calling sequence used.
// L.6: (Warning name conflict: function name changed from figure to %figure).
%figure(3);
// !! L.7: Matlab toolbox(es) function imshow not converted, original calling sequence used
imshow(A)

//% Make image black and white
// !! L.10: Matlab toolbox(es) function rgb2gray not converted, original calling sequence used
Abw2 = rgb2gray(A);
[nx,ny] = size(Abw2);
// !! L.12: Matlab function figure not yet converted, original calling sequence used.
// L.12: (Warning name conflict: function name changed from figure to %figure).
%figure(1)
subplot(2,2,1)// !! L.12: Matlab toolbox(es) function imshow not converted, original calling sequence used
imshow(Abw2)
title("Original image","FontSize",18)

//% Compute the FFT of our image using fft2
disp("Doing FFT analysis for sparsity check...")
tic;
At = fft2(Abw2);

F = log(mtlb_a(abs(fftshift(At)),1));
// !! L.21: Matlab toolbox(es) function mat2gray not converted, original calling sequence used
F = mat2gray(F);// Use mat2gray to scale the image between 0 and 1
// !! L.22: Matlab function figure not yet converted, original calling sequence used.
// L.22: (Warning name conflict: function name changed from figure to %figure).
%figure(4)
// !! L.23: Matlab toolbox(es) function imshow not converted, original calling sequence used
imshow(F,[]);// Display the result

//% Zero out all small coefficients and inverse transform
disp("Zeroing out small Fourier coefficients...")
tic;
count_pic = 2;
%v0 = abs(At);%v1 = max(%v0,firstnonsingleton(%v0));
for thresh = (0.1*[0.001,0.005,0.01])*max(%v1,firstnonsingleton(%v1))
  ind = mtlb_logic(abs(At),">",thresh);
  count = mtlb_s(nx*ny,mtlb_sum(mtlb_sum(ind)));
  Atlow = At .*ind;
  percent = mtlb_s(100,(count/(nx*ny))*100);
  // !! L.34: Matlab function ifft2 not yet converted, original calling sequence used.
  // !! L.34: Scilab uint8() does not work with Complex values: uint8() call IGNORED.
  // ! L.34: ifft2(Atlow) may be replaced by:
  // !    --> uint8(ifft2(Atlow)) if ifft2(Atlow) is Real.
  Alow = ifft2(Atlow);
  // !! L.35: Matlab function figure not yet converted, original calling sequence used.
  // L.35: (Warning name conflict: function name changed from figure to %figure).
  %figure(1)  
  subplot(2,2,count_pic)  // !! L.35: Matlab toolbox(es) function imshow not converted, original calling sequence used
  imshow(Alow);  count_pic = count_pic+1;
  // L.36: Drawing events are not queued in Scilab.
  //drawnow
  // !! L.37: string output can be different from Matlab num2str output.
  title(string(percent)+"% of FFT basis","FontSize",18)
end;
// !! L.39: string output can be different from Matlab num2str output.
disp("    done. ("+string(toc())+"s)")

//% 
// !! L.42: Matlab function figure not yet converted.
mtlb(figure)
// !! L.43: Matlab toolbox(es) function imresize not converted, original calling sequence used
Anew = imresize(Abw2,0.1);
surf(double(Anew));
