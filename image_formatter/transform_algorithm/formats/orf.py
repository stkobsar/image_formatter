import rawpy
import imageio


def transform_raw_jpg(raw_image, output_image):
    with rawpy.imread(raw_image) as raw:
        rgb = raw.postprocess()
        imageio.imwrite(output_image, rgb)
    return output_image

