import pytest
import os
import proj1.main as mn



def test_transform(image_raw="/Users/Stephi/Desktop/Photos_raw/P3030005.ORF", image_jpg="P3030005.jpg"):
    if os.path.exists(image_jpg):
        os.remove(image_jpg)
    mn.transform_raw_jpg(image_raw, image_jpg)
    assert os.path.exists(image_jpg)








