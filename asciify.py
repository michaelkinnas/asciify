"""
Convert images to ascii character representation art.

Options:
    -n Print reversed values (negative).
    -o <file name> Output text file (suppresses output to terminal).
    -c <character set> Character set to use.
    -w <width value> Number of characters per line.
"""
import sys, os
from PIL import Image

def map_values(old_min, old_max, new_min, new_max, value): 
    return int(((new_max - new_min) * ((value - old_min) / (old_max - old_min))) + new_min)

CHARACTER_SETS = {
    'ascii1':"¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;^:,'.` ",
    'ascii2' :"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'.",
    'runic' : "ᛥᛤᛞᚥᚸᛰᛖᚻᚣᛄᚤᛒᚢᚱᛱᚷᚫᛪᚧᚬᚠᛏᚨᚰᚩᚮᚪᚳᚽᚿᛊᛁᛵᛍ᛬ᚲᛌ᛫",
    'box' : "╬╠╫╋║╉╩┣╦╂╳╇╈┠╚┃╃┻╅┳┡┢┹╀╧┱╙┗┞┇┸┋┯┰┖╲╱┎╘━┭┕┍┅╾│┬┉╰╭╸└┆╺┊─╌┄┈╴╶",
    'block' : "█▉▇▓▊▆▅▌▚▞▀▒▐▍▃▖▂░▁▏",
    'geometrick' : "◙◘■▩●▦▣◚◛◕▨▧◉▤◐◒▮◍◑▼▪◤▬◗◭◖◈◎◮◊◫▰◄◯□▯▷▫▽◹△◁▸▭◅▵◌▱▹▿◠◃◦◟◞◜",
    'hiragana' : "ぽぼゑぜぬあおゆぎゐはせぢがきぱびほげばゟぁたかぞぷれひずどらさでけぉちごえすゎにづぇとょついこぐうぅぃくっしへゞゝ゚゙",
}

negative = True
char_set = CHARACTER_SETS['ascii1']
output_file = ''
max_width = 200

image_path = sys.argv[1]
rel_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(rel_path, image_path)

#Parameters handling
for i in range(2, len(sys.argv)): 
    arg = sys.argv[i]
    for j in range(len(arg)):
        if arg[j] == '-':
            match arg[j+1]:
                case 'n':
                    negative = False
                case 'c':
                    char_set = CHARACTER_SETS[sys.argv[i+1]]
                case 'o':
                    output_file = os.path.join(rel_path, sys.argv[i+1])
                case 'w':
                    max_width = int(sys.argv[i+1])
                case _:
                    print(f'Option "{arg[j+1]}" not recognized', file=sys.stderr)
                    exit(-1)

image = Image.open(path)
image = image.convert("L")
image.thumbnail((max_width,max_width), Image.LANCZOS)

image_width, image_heigh = image.size

total_image = ''
for j in range(1, image_heigh):
    line_str = ''
    for i in range(1, image_width):
        pixel_val = image.getpixel((i, j))
        char_index = map_values(0,255,0,len(char_set)-1, pixel_val)
        if negative:
            line_str += char_set[-1 * char_index - 1]
        else:
            line_str += char_set[char_index]
    total_image += line_str + '\n'


if len(output_file) > 0:
    with open(output_file, 'w') as f:
        f.write(total_image)
else:
    print(total_image)