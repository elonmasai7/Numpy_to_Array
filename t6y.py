# Python conversion program
# image from numpy array
# Import any necessary libraries
import numpy as np
from PIL import Image as im


# defining a main function
def main():
    # Construct an array from scratch with numpy.
    # using a function for arrays
    # 1024x720 = 737280 is the amount
    # count of pixels
    # The data type np. uint8 contains
    # Numbers must range from 0 to 255, but there must be
    # and no non-negative integers
    array = np.arange(0, 737280, 1, np.uint8)
    # Check the type of array
    print(type(array))
    # Our collection will be wide
    # 737280 pixels That means it
    # an extended, dark line
    print(array.shape)
    # Resize the array to a more recognizable resolution.
    array = np.reshape(array, (1024, 720))
    # Illustrate the array's form
    print(array.shape)
    # showing the array
    print(array)
    # Constructing an image of
    # across the array
    data = im.
    from array(array)
    # Saving the finished product
    # as a PNG file
    data.save('gfg_dummy_pic.png')


# driver code
if __name__ == "__main__":
    # function call
    main()