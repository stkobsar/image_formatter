import os
import glob
import image_formatter.transform_algorithm.orf as orf
import image_formatter.transform_algorithm.png as png

def transform(input_folder, output_folder, format, SUPPORTED_FORMATS):


    if format.upper() in SUPPORTED_FORMATS:
        input_path = input_folder + "*.{}".format(format.upper())
        photos = glob.glob(input_folder)

        if not photos:
            input_path = input_folder + "*.{}".format(format.lower())
            photos = glob.glob(input_path)
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)


        for photo in photos:
            print(photo)
            photo = photo(photo, output_folder) #???

            photo.transform()
            photo_jpg = photo.rsplit(".", 1)[0] + ".jpg"
            photo_folder = os.path.join(output_folder, os.path.basename(photo_jpg))
            print(photo_folder)
            if format.upper() == "ORF":
                orf.transform_raw_jpg(photo, photo_folder)
            elif format.upper() == "PNG":
                png.transform_png_jpg(photo, photo_folder)
    else:
        raise ValueError("Format not supported. Please choose between options {}".format(SUPPORTED_FORMATS))