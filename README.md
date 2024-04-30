# Wallpaper Factory

## Table of Content

-   [Installation](#Installation)
-   [Usage](#Usage)
-   [Currently Available color schemes](#Currently-Available-color-schemes)
    -   [Gruvbox](#Gruvbox)
    -   [rose pine moon](#rose-pine-moon)
-   [Attributions](#Attributions)
    -   [Example Images](#Example-Images)

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

## Currently Available color schemes

### Gruvbox

| made by       | [morhetz](https://github.com/morhetz)                                                                                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| repository    | [gruvbox](https://github.com/morhetz/gruvbox)                                                                                                                                             |
| palette       | ![palette](https://camo.githubusercontent.com/72015eab40bd7a696e2802810d7519480d51a2fba75f0f873dc23b990eb860f8/687474703a2f2f692e696d6775722e636f6d2f776136363678672e706e67)              |
| example image | ![./assets/gruvbox/gruvbox_dark_medium_wallhaven-m9e9m1.png](https://raw.githubusercontent.com/TheBaum123/wallpaper-factory/main/assets/gruvbox/gruvbox_dark_medium_wallhaven-m9e9m1.png) |

### rose pine moon

| made by       | [?Rosé Pine?](https://rosepinetheme.com/)                                                            |
| ------------- | ---------------------------------------------------------------------------------------------------- |
| repository    | [rose-pine-theme](https://github.com/rose-pine/rose-pine-theme)                                      |
| palette       | ![palette](https://raw.githubusercontent.com/rose-pine/rose-pine-theme/main/assets/palette-moon.png) |
| example image | waiting for consent to distribute                                                                    |

### everforest medium dark

| made by       | [sainnhe](https://github.com/sainnhe)                                                                             |
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| repository    | [everforest](https://github.com/sainnhe/everforest)                                                               |
| palette       | ![palette](https://user-images.githubusercontent.com/58662350/214382352-cd7a4f63-e6ef-4575-82c0-a8b72aa37c0c.png) |
| example image | TODO                                                                                                              |

## Attributions

### Example Images

| Original                                                                                      | Made By                                      | Link                          |
| --------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------- |
| ![Kaga(Azure Lane) 1920x1080 by voyager](https://w.wallhaven.cc/full/m9/wallhaven-m9e9m1.png) | [voyager](https://wallhaven.cc/user/voyager) | https://wallhaven.cc/w/m9e9m1 |
