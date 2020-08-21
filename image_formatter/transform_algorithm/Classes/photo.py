import image_formatter.transform_algorithm.formats.orf as orf
import image_formatter.transform_algorithm.formats.png as png
import os



class Photo():

        def __init__(self, path, output_folder, input_format):
            self.path = path
            photo_jpg = self.path.rsplit(".",1)[0] + ".jpg"
            self.output = os.path.join(output_folder, os.path.basename(photo_jpg))
            self.input_format = input_format.lower()

        def transform(self):
            if self.input_format == "orf":
                orf.transform_raw_jpg(self.path, self.output)
            elif self.input_format == "png":
                png.transform_png_jpg(self.path, self.output)






if __name__ == "__main__":
    #cress objecto classe "photo" con la photo acorn.png
    photo1 = Photo("/Users/Stephi/Desktop/Photos_orf/acorn.png","/Users/Stephi/Desktop/Photos_jpg", "png") 
    photo1.transform() #si no hay mas atributos que el self, no hace falta poner nada
