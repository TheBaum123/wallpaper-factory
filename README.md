# Wallpaper Factory

## Table of Content

-   [Installation](#Installation)
-   [Usage](#Usage)
-   [Currently Available color schemes](#Currently-Available-color-schemes)
    -   [Gruvbox](#Gruvbox)
    -   [rose pine moon](#rose-pine-moon)
    -   [everforest medium dark](#everforest-medium-dark)
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

| made by       | [?Rosé Pine?](https://rosepinetheme.com/)                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------- |
| repository    | [rose-pine-theme](https://github.com/rose-pine/rose-pine-theme)                                                            |
| palette       | ![palette](https://raw.githubusercontent.com/rose-pine/rose-pine-theme/main/assets/palette-moon.png)                       |
| example image | ![./assets/rose_pine_moon/rose_pine_moon_arch_denoised.png](https://raw.githubusercontent.com/TheBaum123/wallpaper-factory/main/assets/rose_pine_moon/rose_pine_moon_arch_denoised.png) |

### everforest medium dark

| made by       | [sainnhe](https://github.com/sainnhe)                                                                                                                                                                                         |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| repository    | [everforest](https://github.com/sainnhe/everforest)                                                                                                                                                                           |
| palette       | ![palette](https://user-images.githubusercontent.com/58662350/214382352-cd7a4f63-e6ef-4575-82c0-a8b72aa37c0c.png)                                                                                                             |
| example image | ![./assets/everforest_dark_medium/everforest_dark_medium_wallhaven-1pwxv1.png](https://raw.githubusercontent.com/TheBaum123/wallpaper-factory/main/assets/everforest_dark_medium/everforest_dark_medium_wallhaven-1pwxv1.png) |

## Attributions

### Example Images

| Original                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Made By                                                      | Link                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------- |
| ![Kaga(Azure Lane) 1920x1080 by voyager](https://w.wallhaven.cc/full/m9/wallhaven-m9e9m1.png)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [voyager](https://wallhaven.cc/user/voyager)                 | https://wallhaven.cc/w/m9e9m1                                     |
| ![Sparkle(Honkai: Star Rail) 1920x1080 by voyager](https://w.wallhaven.cc/full/1p/wallhaven-1pwxv1.png)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [voyager](https://wallhaven.cc/user/voyager)                 | https://wallhaven.cc/w/1pwxv1                                     |
| ![Arch Chan (OC) 3840x2160 by RavioliMavioli](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/dc42d389-b579-448b-a3cb-5e3c91516635/deiz9mv-a855d87e-88ce-48c0-8349-f533524424c7.png/v1/fill/w_1192,h_670,q_70,strp/arch_chan_by_raviolimavioli_deiz9mv-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjE2MCIsInBhdGgiOiJcL2ZcL2RjNDJkMzg5LWI1NzktNDQ4Yi1hM2NiLTVlM2M5MTUxNjYzNVwvZGVpejltdi1hODU1ZDg3ZS04OGNlLTQ4YzAtODM0OS1mNTMzNTI0NDI0YzcucG5nIiwid2lkdGgiOiI8PTM4NDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.bdQYUHMDNZtEYjlfkhMp2Z_x6yIHDFhUEjNyCBdrcPM) | [RavioliMavioli](https://www.deviantart.com/raviolimavioli/) | https://www.deviantart.com/raviolimavioli/art/Arch-chan-878404999 |

All images remain property of their original owners. Owners may request removal of images at any time.
