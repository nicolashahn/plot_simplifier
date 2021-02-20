import sys
import diffimg
from PIL import Image, ImageDraw

H = 1872
W = 1404

def image_from_rmlamp(input_file):
    commands = []
    with open(input_file, "r") as infile:
        for line in infile.readlines():
            tokens = line.strip().split(" ")
            if tokens[1] == "up":
                commands.append(("up",None,None))
            else:
                commands.append((tokens[1], int(tokens[2]), int(tokens[3])))

    im = Image.new(mode="RGB", size=(H, W))
    draw = ImageDraw.Draw(im)
    
    for i, c1 in enumerate(commands[:-1]):
        c2 = commands[i+1]
        if (c1[0] == "up" or c2[0] == "up"):
            continue
        xy1 = c1[1], c1[2]
        xy2 = c2[1], c2[2]
        draw.line([xy1, xy2], fill=255)

    return im

def main(infile1, infile2):
    len1 = len(open(infile1, "r").readlines())
    len2 = len(open(infile2, "r").readlines())
    image1 = image_from_rmlamp(infile1)
    image2 = image_from_rmlamp(infile2)

    print("{} length / {} length = {}/{} = {}".format(
        infile1, infile2, len1, len2, float(len1)/float(len2)
    ))
    print("image difference: {}".format(
        diffimg.diff_inner(image1, image2, delete_diff_file=True)
    ))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: harness.py <rmlamp file 1> <rmlamp file 2>")
    main(sys.argv[1], sys.argv[2])
