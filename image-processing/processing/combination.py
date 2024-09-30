import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms as mh
from skimage.metrics import structural_similarity as ssim


def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Specify 2 images with the same shape"
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (scrore, difference_image) = ssim(gray_image1, gray_image2, full=True)
    print(f"Similarity score of the images: {score}")
    min_diff = np.min(difference_image)
    max_diff = np.max(difference_image)
    normalized_difference_image = (difference_image - min_diff) / \
                                  (max_diff - min_diff)
    return normalized_difference_image


def transfer_histogram(image1, image2):
    matched_image = mh(image1, image2, multichannel=True)
    return matched_image
