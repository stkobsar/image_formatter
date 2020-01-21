import pytest
import os
import image_formatter.main as mn


absolute_path_every_machine = os.path.abspath(__file__)
directory_path = os.path.dirname(absolute_path_every_machine)


def test_transform(image_orf=directory_path+"/data/P3030005.ORF", image_jpg="P3030005.jpg"):
    if os.path.exists(image_jpg):
        os.remove(image_jpg)
    mn.transform_raw_jpg(image_orf, image_jpg)
    assert os.path.exists(image_jpg)








