from setuptools import setup

f = open("./README.md")
long_description = f.read()

setup(
    name="wallpaper_factory",
    version="0.0.13",
    install_requires=["opencv-python", "pillow"],
    entry_points={
        "console_scripts": ["wallpaper-factory = wallpaper_factory:wallpaper_factory"]
    },
    package_data={"": ["*.json"]},
    long_description=long_description,
    long_description_content_type="text/markdown",
)
