"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    # get colors
    p_r = pixel.red
    p_g = pixel.green
    p_b = pixel.blue

    # find square of pixel colors and the average colors
    r_square = (red - p_r)**2
    g_square = (green - p_g)**2
    b_square = (blue - p_b)**2

    # find square root
    color_distance = math.sqrt(r_square + g_square + b_square)

    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    pixel_num = len(pixels)
    sum_r = 0  # summation of red pixels
    sum_g = 0  # summation of green pixels
    sum_b = 0  # summation of blue pixels

    for i in range(pixel_num):
        sum_r += pixels[i].red
        sum_g += pixels[i].green
        sum_b += pixels[i].blue

    red = sum_r // pixel_num  # get the average of red pixels
    green = sum_g // pixel_num  # get the average of green pixels
    blue = sum_b // pixel_num  # get the average of blue pixels

    return red, green, blue


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    best_distance = math.inf
    red, green, blue, = get_average(pixels)

    for i in range(len(pixels)):
        p_dist = get_pixel_dist(pixels[i], red ,green, blue)
        if p_dist < best_distance:
            best_distance = p_dist
            best_pixel = pixels[i]

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            pixels = []
            for i in range(len(images)):
                pixels += [images[i].get_pixel(x, y)]

            best_pixel = get_best_pixel(pixels)
            result_p = result.get_pixel(x, y)

            result_p.red = best_pixel.red
            result_p.green = best_pixel.green
            result_p.blue = best_pixel.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
