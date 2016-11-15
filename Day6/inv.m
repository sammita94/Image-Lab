function[g]=inverse(image,k)

image = rgb2gray(image);
img_fft=fft2(double(image));
img_fft=fftshift(img_fft);

% distance initialization for notch filter
D=zeros(size(image,1),size(image,2));
D(1,1)=1;
D=fftshift(D);
D=bwdist(D);

% H(u,v) - degradation function
H1 = exp(-k*(D.^2).^(5/6));

% inverse filter
img_ifft=ifft2(ifftshift(H1.*img_fft));
g=abs(img_ifft);