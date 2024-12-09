# Intelligent Image Analysis course code

# 1.Histogram Equalization

## 1.1. Introduce:

Histogram Equalization can enhance the contrast in image. It can modify the pixel intensity values of an image such that its histogram is approximately flattened, resulting in a more spread-out intensity range and an overall enhancement in contrast.

## 1.2.Processing:

1. Traversing the image and store pixel count witch is smalller than each gray.
2. Define the $GrayMax_{out}$ and calculate each input gray`s output gray.

$$
Gray_{out} = rounr(\frac {GrayMax_{out} \ast SmallerCount_{Gray_{in}}} {H \ast W} )
$$

3. Replace the $Gray_{in}$ with the cropodding $Gray_{out}$.

# 2.Canny

## 2.1. Introduce:

Canny edge detection is one of the image segmentation method. Canny edge detection is to find the position of the largest gradient change in the image, so as to determine the position of the edge.

## 2.2.Processing:

1. Gaussian filtering: Use two-dimensional Gaussian function create one gaussian filter which size is 3*3 and standard deviation is 1. Image multiplied the gaussian filter to smooth the image data.

$$
G(x,y) = \frac{1}{2\pi \sigma ^ {2}} exp(-\frac{x^{2}+y^{2}} {2\sigma^{2}})
$$

$$
\begin{bmatrix}0.0751136&0.1238414&0.0751136\\
0.1238414&0.2041799&0.1238414\\
0.0751136&0.1238414&0.0751136\end{bmatrix}
$$

2. Pixel gradient calculation: Using Sobel Operator calculate each direction gradient value, total gradient value and gradient direction.

- Each direction gradient value:

$$
G_{x}=S_{x}\ast I=
\begin{bmatrix}-1&0&+1\\
-2&0&+2\\
-1&0&+1\end{bmatrix}\ast I
$$
$$
G_{y}=
S_{y}\ast I=
\begin{bmatrix}-1&-2&-1\\
0&0&0\\
+1&+2&+1\end{bmatrix}\ast I
$$

3. Non-maximum suppression: Traverse all points on the gradient matrix and preserve pixels with maximum values in the edge direction.

![Non-maximum suppression](img/Non-maximum%20suppression.jpg)

- For more accurate calculation, linear interpolation is usually used between two adjacent pixels spanning the gradient direction to obtain the pixel gradient to be compared.


$$
g_{up}(i,j)=(1-t) \cdot g_{xy}(i,j+1)+t \cdot g_{xy}(i-1,j+1)
$$

$$
g_{down} \left(i,j \right)=(1-t) \cdot g_{xy}(i,j-1)+t \cdot g_{xy}(i+1,j-1)
$$

4. Hysteresis threshold processing:
5. Isolated weak edge suppression:


[Reference link](https://zhuanlan.zhihu.com/p/99959996)