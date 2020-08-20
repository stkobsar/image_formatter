from PIL import Image
import rawpy
import imageio
import os
import glob
import argparse
import image_formatter.transform_algorithm.orf as orf
import image_formatter.transform_algorithm.png as png


SUPPORTED_FORMATS = ["ORF", "PNG", "RAW", "BMP"]


def transform(RAW_FOLDER, folder, format):
    if format.upper() in SUPPORTED_FORMATS:
        input_path = RAW_FOLDER + "*.{}".format(format.upper())
        photos = glob.glob(input_path)

        if not photos:
            input_path = RAW_FOLDER + "*.{}".format(format.lower())
        photos = glob.glob(input_path)
        if not os.path.exists(folder):
            os.mkdir(folder)
        
        for photo in photos:
            photo = photo(photo, folder)
            photo.transoform()
            photo_jpg = photo.rsplit(".", 1)[0] + ".jpg"
            photo_folder = os.path.join(folder, os.path.basename(photo_jpg))
            print(photo_folder)
            if format.upper() == "ORF":
                orf.transform_raw_jpg(photo, photo_folder)
            elif format.upper() == "PNG":
                png.transform_png_jpg(photo, photo_folder)
    else:
        raise ValueError("Format not supported. Please choose between options {}".format(SUPPORTED_FORMATS))



if __name__ == "__main__":

    #############ARGPARSE########
    parser = argparse.ArgumentParser(description='Transform ORF to JPEG')
    parser.add_argument('-input', '--input_folder', type=str, help='insert folder containing .ORF photos')
    parser.add_argument('-f', '--format', type=str, help='insert photo format')
    parser.add_argument('-output', '--output_folder', default="Output_jpg" ,type=str, help='insert output folder for the JPEG photos')
    args = parser.parse_args()
    #############################


    transform(args.input_folder, args.output_folder, args.format)
