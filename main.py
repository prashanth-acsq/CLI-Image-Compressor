import os
import sys

from PIL import Image


READ_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Files")
SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Processed")


def main():

    args_1: tuple = ("--file", "-f")
    args_2: tuple = ("--quality", "-q")
    args_3: tuple = ("--display", "-d")

    filename: str = None
    quality: float = None
    display: bool = False

    if args_1[0] in sys.argv: filename = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: filename = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv: quality = int(sys.argv[sys.argv.index(args_2[0]) + 1])
    if args_2[1] in sys.argv: quality = int(sys.argv[sys.argv.index(args_2[1]) + 1])

    if args_3[0] in sys.argv or args_3[1] in sys.argv: display = True

    assert filename is not None, "No file specified"
    assert filename in os.listdir(READ_PATH), "File not found"
    assert quality is not None, "No quality specified"
    assert quality > 0 and quality <= 100, "Quality out of range (0-100]"

    image: Image = Image.open(os.path.join(READ_PATH, filename))

    path = os.path.join(SAVE_PATH, filename.split(".")[0] + " - Compressed.jpg")
    image.save(path, optimizer=True, quality=quality)

    if display:
        image: Image = Image.open(path)
        image.show()


if __name__ == "__main__":
    sys.exit(main() or 0)
