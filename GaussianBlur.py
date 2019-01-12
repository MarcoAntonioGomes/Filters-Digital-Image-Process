import skimage.io as io
from skimage.filter import gaussian_filter
import matplotlib.pyplot as plt
import numpy as np
img = io.imread('sobel.png')

def show_images(images,titles=None):
    """Display a list of images"""
    n_ims = len(images)
    if titles is None: titles = ['(%d)' % i for i in range(1,n_ims + 1)]
    fig = plt.figure()
    n = 1
    for image,title in zip(images,titles):
        a = fig.add_subplot(1,n_ims,n) # Make subplot
        if image.ndim == 2: # Is image grayscale?
            plt.gray() # Only place in this blog you can't replace 'gray' with 'grey'
        plt.imshow(image)
        a.set_title(title)
        n += 1
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
    plt.show()




blurred_image = gaussian_filter(img,sigma=3)
really_blurred_image = gaussian_filter(img,sigma=6)

show_images(images=[img,blurred_image,really_blurred_image],
            titles=["Equalized","3 Sigma Blur","6 Sigma Blur"])