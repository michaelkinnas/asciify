# ASCIIfy
Convert an image to ascii art

## Usage

You will need Python 3.

To run the program navigate to where the asciify.py file is and type in your terminal:

```sh
python3 asciify.py <image_file>
```

The program will print in the terminal the ASCII character representation of the image.

## Options



### Negative

`-n`

The image will be printed using negative values. Usefull if you are using white background with dark characters in your terminal.

### Output file

`-o <file_name>`

The program will output a text file with the given name instead of being printed in the terminal.

### Character set

`-c <character_set_name>`

Which character set to use. By default you can choose between 7 character sets. (In a future version you will be able to user your own also)

```sh
    ascii1      ¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;^:,'.` 
    ascii2      $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'.
    runic       ᛥᛤᛞᚥᚸᛰᛖᚻᚣᛄᚤᛒᚢᚱᛱᚷᚫᛪᚧᚬᚠᛏᚨᚰᚩᚮᚪᚳᚽᚿᛊᛁᛵᛍ᛬ᚲᛌ᛫
    box         ╬╠╫╋║╉╩┣╦╂╳╇╈┠╚┃╃┻╅┳┡┢┹╀╧┱╙┗┞┇┸┋┯┰┖╲╱┎╘━┭┕┍┅╾│┬┉╰╭╸└┆╺┊─╌┄┈╴╶
    block       █▉▇▓▊▆▅▌▚▞▀▒▐▍▃▖▂░▁▏
    geometrick  ◙◘■▩●▦▣◚◛◕▨▧◉▤◐◒▮◍◑▼▪◤▬◗◭◖◈◎◮◊◫▰◄◯□▯▷▫▽◹△◁▸▭◅▵◌▱▹▿◠◃◦◟◞◜ 
    hiragana    ぽぼゑぜぬあおゆぎゐはせぢがきぱびほげばゟぁたかぞぷれひずどらさでけぉちごえすゎにづぇとょついこぐうぅぃくっしへゞゝ゚゙
```

### Width

`-w <integer_value>`

How many characters will be printed per line. Essentially the width of the image.
