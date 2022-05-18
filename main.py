import os
import sys

from PIL import Image


READ_PATH = "Files"
SAVE_PATH = "Processed"


def main():

    args_1: tuple = ("--file", "-f")
    args_2: tuple = ("--quality", "-q")
    args_3: tuple = ("--display", "-d")
    args_4: tuple = ("--save", "-s")

    filename: str = None
    quality: float = None
    display: bool = False
    save: bool = False

    if args_1[0] in sys.argv: filename = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: filename = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv: quality = int(sys.argv[sys.argv.index(args_2[0]) + 1])
    if args_2[1] in sys.argv: quality = int(sys.argv[sys.argv.index(args_2[1]) + 1])

    if args_3[0] in sys.argv or args_3[1] in sys.argv: display = True

    if args_4[0] in sys.argv or args_4[1] in sys.argv: save = True

    assert filename is not None, "No file specified"
    assert filename in os.listdir(READ_PATH), "File not found"
    assert quality is not None, "No quality specified"
    assert quality < 0 and quality >= 100, "Quality out of range (0-100]"

    image: Image = Image.open(os.path.join(READ_PATH, filename))

    if display: image.show()
    if save: image.save(os.path.join(SAVE_PATH, filename.split(".")[0] + " - Compressed.jpg"), 
                        optimizer=True, 
                        quality=quality)


if __name__ == "__main__":
    sys.exit(main() or 0)




