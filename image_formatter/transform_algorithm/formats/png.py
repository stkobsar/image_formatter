from PIL import Image
import argparse
import glob
import os


def transform_png_jpg(png_image, output):
    im = Image.open(png_image)
    im.convert('RGB').save(output, "JPEG") #this converts png image as jpeg

if __name__ == "__main__":

    #############ARGPARSE########
    parser = argparse.ArgumentParser(description='Transform PNG to JPEG')
    parser.add_argument('input_folder', type=str, help='insert folder containing .png photos')
    parser.add_argument('format', type=str, help='insert photo format')
    parser.add_argument('--output_folder', default="Output_jpg" ,type=str, help='insert output folder for the JPEG photos')
    args = parser.parse_args()
    #############################
    transform_png_jpg(args.input_folder, args.output_folder) 
