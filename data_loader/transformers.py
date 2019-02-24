import cv2

from skimage.transform import resize

class Rescale():
    """Rescale the image in a sample to a given size.

    Args:
        output_size (height, width) (tuple): Desired output size (width, height). Output is
            matched to output_size.
    """

    def __init__(self, output_size):
        assert isinstance(output_size, (tuple))
        self.output_size = output_size

    def __call__(self, sample):
        sample = resize(sample, self.output_size)

        return sample
