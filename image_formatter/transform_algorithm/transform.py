import os
import glob
import image_formatter.transform_algorithm.Classes.photo as pt

SUPPORTED_FORMATS = ["ORF", "PNG", "RAW", "BMP"]

def transform(input_folder, output_folder, format):

    if format.upper() in SUPPORTED_FORMATS:

        #######Retrieve pictures to be tranformed########
        input_path = input_folder + "*.{}".format(format.upper())
        photos = glob.glob(input_path)
        if not photos:
            input_path = input_folder + "*.{}".format(format.lower())
            photos = glob.glob(input_path)

        #######Creeate output folder if not exist######
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)

        for photo in photos:
            print(f"transforming {os.path.basename(photo)} to jpg")
            photo = pt.Photo(photo, output_folder, format)
            photo.transform()

    else:
        raise ValueError("Format not supported. Please choose between options {}".format(SUPPORTED_FORMATS))