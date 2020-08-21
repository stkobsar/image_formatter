import argparse
import image_formatter.transform as tr

SUPPORTED_FORMATS = ["ORF", "PNG", "RAW", "BMP"]

def parse_args(parser):
    parser.add_argument('-input', '--input_folder', type=str, help='insert folder with photos to convert')
    parser.add_argument('-f', '--format', type=str, help='insert photo format')
    parser.add_argument('-output', '--output_folder', default="output_jpg", type=str,
                        help='insert output folder for the JPEG photos')
    args = parser.parse_args()




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Transform ORF to JPEG')
    parse_args(parser)
    args = parser.parse_args()

    tr.transform(args.input_folder, args.output_folder, args.format, SUPPORTED_FORMATS)
