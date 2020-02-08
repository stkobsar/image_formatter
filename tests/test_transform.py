import pytest
import os
import image_formatter.transform_algorithm.orf as orf
import image_formatter.transform_algorithm.png as png


absolute_path_every_machine = os.path.abspath(__file__)
directory_path = os.path.dirname(absolute_path_every_machine)


def test_transform(image_orf=directory_path+"/data/P3030005.ORF", image_jpg="P3030005.jpg"):
    if os.path.exists(image_jpg):
        os.remove(image_jpg)
    orf.transform_raw_jpg(image_orf, image_jpg)
    assert os.path.exists(image_jpg)

def test_transform_png(image_png=directory_path+"/data/acorn.png", image_jpg="acorn.jpg"):
    if os.path.exists(image_jpg):
        os.remove(image_jpg)
    png.transform_png_jpg(image_png, image_jpg)
    assert os.path.exists(image_jpg)








