from setuptools import setup

setup(
    name="wallpaper_factory",
    version="0.0.1",
    install_requires=["opencv-python", "pillow"],
    entry_points={
        "console_scripts": ["wallpaper-factory = wallpaper_factory:wallpaper_factory"]
    },
)
