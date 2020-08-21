import rawpy
import imageio


def transform_raw_jpg(raw_image, output):
    
    with rawpy.imread(raw_image) as raw:
        thumb = raw.extract_thumb()
    if thumb.format == rawpy.ThumbFormat.JPEG:
        with open('thumb.jpeg', 'wb') as f:
            f.write(thumb.data)
    elif thumb.format == rawpy.ThumbFormat.BITMAP:
        imageio.imsave('thumb.jpeg', thumb.data)










