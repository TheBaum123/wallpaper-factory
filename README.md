# Wallpaper Factory

## Installation

You can install this package / cli utility by running `pip install wallpaper-factory`.

## Usage

To use this program, run `wallpaper-factory`. You will then get prompted to select your prefered theme like this:

```
Choose your color pallete:
1.: <theme1>
2.: <theme2>
...
Enter the number of the pallete you want:
```

You can now enter the theme you want, after which you will be prompted if you want to generate a denoised version of the image as well. The denoised version oftentimes looks better but takes the program quite a bit of extra time to generate. In addition on images with lots of details, those might suffer from the denoising. If you have some time and processing power to space, I advise you to generate this version and look which one you like better by answering `y`.

```
Enter the number of the pallete you want: 1
Should an attempt be made to denoise the image? This will generate a second version of it. (y/n): y
```

Next you will get prompted to enter the image path, where you can then enter a relative or absolute path to the image you want recolored.

```
Path of the image you want to recolor: /Users/<user>/Pictures/<image_to_recolor.{png|jpg}>
```

Afther that, you will have ot wait a bit for the program to run. It will then output the new image paths like this:

```
saved recolored version at <path/<theme>_<name>.png>
```

and additionally

```
saved recolored version at <path/<theme>_<name>_denoised.png>
```

if you chose to generate a denoised version of the image as well.
