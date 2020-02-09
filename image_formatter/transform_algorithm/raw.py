import rawpy
import imageio

path = 'image.nef'
with rawpy.imread(path) as raw:
    rgb = raw.postprocess()
imageio.imsave('default.tiff', rgb)







if __name__ == "__main__":

    #############ARGPARSE########
    parser = argparse.ArgumentParser(description='Transform ORF to JPEG')
    parser.add_argument('input_folder', type=str, help='insert folder containing .ORF photos')
    parser.add_argument('format', type=str, help='insert photo format')
    parser.add_argument('--output_folder', default="Output_jpg" ,type=str, help='insert output folder for the JPEG photos')
    args = parser.parse_args()
    #############################
    transform(args.input_folder, args.output_folder, args.format)




