import rawpy
import imageio
import argparse

def transform_raw_jpg(raw_image, output):
    
    with rawpy.imread(raw_image) as raw:
        thumb = raw.extract_thumb()
    if thumb.format == rawpy.ThumbFormat.JPEG:
        with open('thumb.jpeg', 'wb') as f:
            f.write(thumb.data)
    elif thumb.format == rawpy.ThumbFormat.BITMAP:
        imageio.imsave('thumb.jpeg', thumb.data)





if __name__ == "__main__":

    #############ARGPARSE########
    parser = argparse.ArgumentParser(description='Transform ORF to JPEG')
    parser.add_argument('input_folder', type=str, help='insert folder containing .ORF photos')
    parser.add_argument('format', type=str, help='insert photo format')
    parser.add_argument('--output_folder', default="Output_jpg" ,type=str, help='insert output folder for the JPEG photos')
    args = parser.parse_args()
    #############################
    transform(args.input_folder, args.output_folder, args.format)




