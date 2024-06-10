import os
import cv2
from PIL import Image
from .available_palletes import available_palletes


def main():
    # Choosing a color pallete available in available_palletes.py
    # and loading it into available_colors for recoloring
    print("Choose your color pallete:")
    pallete_index = 1
    for color_pallete in available_palletes:
        print(f"{pallete_index}.: {color_pallete[0]}")
        pallete_index += 1

    chosen_pallete = int(input("Enter the number of the pallete you want: ")) - 1
    if chosen_pallete < 0 or chosen_pallete > len(available_palletes) - 1:
        print(f"Please choose a number within the range 0-{len(available_palletes)}")
        quit(1)

    print(f"Chosen theme: {available_palletes[chosen_pallete][0].replace("-", " ")}")

    available_colors = available_palletes[chosen_pallete][1]

    # ask the user if an attempt at denoising the image should be made
    denoise_image = (
        input(
            "Should an attempt be made to denoise the image? This will generate a second version of it. (y/n): "
        ).lower()
        == "y"
    )

    # denoise image func
    def denoise(image_path: str):
        image = cv2.imread(image_path)

        new_image = cv2.fastNlMeansDenoisingColored(
            image, h=10, hColor=10, searchWindowSize=21
        )

        new_path = image_path.split(os.sep)
        image_name = new_path.pop()
        image_name = image_name.split(".")
        image_name.pop()
        image_name.append("_denoised")
        image_name = "".join(image_name)
        image_name = image_name + ".png"
        new_path.append(image_name)
        new_path = f"{os.sep}".join(new_path)
        cv2.imwrite(new_path, new_image)
        # remove black background that somehow happens while denoising
        if not (0, 0, 0, 255) in available_colors:
            remove_bg_after_denoise(new_path)
        print("saved denoised version at " + new_path)

    # remove bg from image after bg is added in denoising
    def remove_bg_after_denoise(image_path: str):
        image = Image.open(image_path)
        image = image.convert("RGBA")
        pix = image.load()
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                if type(pix[x, y]) is tuple and not pix[x, y] == (0, 0, 0, 0):
                    if pix[x, y] == (0, 0, 0, 255):
                        pix[x, y] = (0, 0, 0, 0)
        image.save(image_path)

    # get the image path to the image the user wants to convert
    # to the prefered color scheme
    image_path = os.path.abspath(input("Path of the image you want to recolor: "))

    # recolor the image and write it to the original directory
    # as <color-scheme>_<original-name>.png
    def recolor_image(path: str):
        image = Image.open(path)
        image = image.convert("RGBA")
        pix = image.load()
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                if type(pix[x, y]) is tuple and not pix[x, y] == (0, 0, 0, 0):
                    differences = []
                    for color in available_colors:
                        difference = int(0)
                        difference += int(abs(int(pix[x, y][0]) - int(color[0])))
                        difference += int(abs(int(pix[x, y][1]) - int(color[1])))
                        difference += int(abs(int(pix[x, y][2]) - int(color[2])))
                        difference += int(abs(int(pix[x, y][3]) - int(color[3])))
                        differences.append(difference)
                    min_diff = 1020
                    new_color = available_colors[0]

                    for i in range(len(differences)):
                        if differences[i] <= min_diff:
                            min_diff = differences[i]
                            new_color = available_colors[i]

                    pix[x, y] = new_color

        new_path = path.split(os.sep)
        image_name = new_path[-1]
        image_name = image_name.split(".")
        image_name.pop()
        image_name = ".".join(image_name) + ".png"
        new_path.pop()
        new_path = (
            f"{os.sep}".join(new_path)
            + os.sep
            + available_palletes[chosen_pallete][0]
            + "_"
            + image_name
        )
        image.save(new_path)
        print("saved recolored version at " + new_path)

        # denoise image if the user wants to
        if denoise_image:
            denoise(new_path)

    recolor_image(image_path)
