import sys, os
from PIL import Image

def map_values(old_min, old_max, new_min, new_max, value):
    OLD_PERCENT = (value - old_min) / (old_max - old_min)
    return int(((new_max - new_min) * OLD_PERCENT) + new_min)

PIXEL_VALUES = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

image_path = sys.argv[1]
rel_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(rel_path, image_path)

image = Image.open(path)
image = image.convert("L")

image.thumbnail((200,200), Image.ANTIALIAS)

imageSizeW, imageSizeH = image.size

total_image = ''
for j in range(1, imageSizeH):
    line_str = ''
    for i in range(1, imageSizeW):
        pixVal = image.getpixel((i, j))
        value = map_values(0,255,0,len(PIXEL_VALUES)-1, pixVal)
        line_str += PIXEL_VALUES[value]
    total_image += line_str + '\n'


# with open(working_dir + "output2.txt", 'w') as f:
#     f.write(total_image)

print(total_image)