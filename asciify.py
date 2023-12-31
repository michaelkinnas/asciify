HELP = """
Convert images to ascii-like character representation art.

Usage: python3 asciify.py <image_file> [options]

Options:
    -p                          Print reversed values (positive).
    -o <file_name>              Output text file (suppresses output to terminal).
    -c <character_set_name>     Character set to use.
    -w <integer_value>          Number of characters per line.
"""

CHARACTER_SETS = {
    'symbols':"¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;^:,'.` ",
    'chars':"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|(1{[?-_+~<i!lI;:,^`'.",
    'runic':"ᛥᛤᛞᚥᚸᛰᛖᚻᚣᛄᚤᛒᚢᚱᛱᚷᚫᛪᚧᚬᚠᛏᚨᚰᚩᚮᚪᚳᚽᚿᛊᛁᛵᛍ᛬ᚲᛌ᛫",
    'box':"╬╠╫╋║╉╩┣╦╂╳╇╈┠╚┃╃┻╅┳┡┢┹╀╧┱╙┗┞┇┸┋┯┰┖╲╱┎╘━┭┕┍┅╾│┬┉╰╭╸└┆╺┊─╌┄┈╴╶",
    'block':"█▉▇▓▊▆▅▌▚▞▀▒▐▍▃▖▂░▁▏",
    'geometric':"◙◘■▩●▦▣◚◛◕▨▧◉▤◐◒▮◍◑▼▪◤▬◗◭◖◈◎◮◊◫▰◄◯□▯▷▫▽◹△◁▸▭◅▵◌▱▹▿◠◃◦◟◞◜",
    'hiragana':"ぽぼゑぜぬあおゆぎゐはせぢがきぱびほげばゟぁたかぞぷれひずどらさでけぉちごえすゎにづぇとょついこぐうぅぃくっしへゞゝ゚゙",
    'simple':"@#&$%{[!+;:-,. " 
}

import sys, os
from PIL import Image

rel_path = os.getcwd() #use current working dir as relative path

# FLAGS
positive = False
char_set = CHARACTER_SETS['simple']
output_file = ''
max_width = 160
resize = False

try:
    if sys.argv[1] == '-h':
        print(HELP)
        sys.exit(0)
    else:
        image_path = sys.argv[1]
except IndexError as err:
    print("No file provided")
    sys.exit(1)

#Parameters handling
for i in range(2, len(sys.argv)): 
    arg = sys.argv[i]
    for j in range(len(arg)):
        if arg[j] == '-':
            match arg[j+1]:
                case 'p':
                    positive = True
                case 'c':
                    char_set = CHARACTER_SETS[sys.argv[i+1]]
                case 'o':
                    output_file = os.path.join(rel_path, sys.argv[i+1])
                case 'w':
                    max_width = int(sys.argv[i+1])
                    resize = True
                case _:
                    print(f'Option "{arg[j+1]}" not recognized', file=sys.stderr)
                    sys.exit(1)

path = os.path.join(rel_path, image_path)

try:
    image = Image.open(path)
except FileNotFoundError as err:
    print(err)
    sys.exit(1)

image = image.convert("L") #convert to greyscale

if resize:
    image.thumbnail((max_width, max_width), Image.LANCZOS)

image_width, image_heigh = image.size

def map_values(old_min, old_max, new_min, new_max, value): 
    return int(((new_max - new_min) * ((value - old_min) / (old_max - old_min))) + new_min)

total_image = ''
for j in range(1, image_heigh):
    line_str = ''
    for i in range(1, image_width):
        pixel_val = image.getpixel((i, j))
        char_index = map_values(0, 255, 0, len(char_set)-1, pixel_val)
        if not positive:
            line_str += char_set[-1 * char_index - 1]
        else:
            line_str += char_set[char_index]
    total_image += line_str + '\n'

if len(output_file) > 0:
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(total_image)
    except FileExistsError as err:
        print(err)
        sys.exit(1)
else:
    print(total_image)