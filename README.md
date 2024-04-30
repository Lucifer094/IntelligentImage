# Intelligent Image Analysis course code

# 1.Histogram Equalization

## 1.1. Introduce:

Histogram Equalization can enhance the contrast in image. It can modify the pixel intensity values of an image such that its histogram is approximately flattened, resulting in a more spread-out intensity range and an overall enhancement in contrast.

## 1.2.Processing:

1. Traversing the image and store pixel count in each gray.
2. Calculate each input gray`s output gray.

$$
Gray_{out} = rounr(\frac {Gray_{Max} \ast Count_{Gray_{in}}} {H \ast W} )
$$

3. Replace the $Gray_{in}$ with the cropodding $Gray_{out}$.

# 2.Canny

## 2.1. Introduce:

## 1.2.Processing:

