"""Setup script for the mitsuba2 project."""

from setuptools import setup  
import glob
import shutil

libname = "mitsuba"

for file in list(glob.glob("./dist/*.dll")):
	shutil.copy2(file,"./dist/python/mitsuba")
setup(
    name=libname,
    version="0.0.1",
    author=" Wenzel Jakob, Merlin Nimier-David, Guillaume Loubet, Sébastien Speierer, Delio Vicini, and Tizian Zeltner.",
    author_email="",
    description="Mitsuba 2: A Retargetable Forward and Inverse Renderer.",
    url="https://github.com/mitsuba-renderer/mitsuba2",
    license="",
    packages=["mitsuba","enoki"],
	package_dir={'mitsuba': "./dist/python/mitsuba","enoki":"./dist/python/enoki"},
    package_data={"mitsuba": ["*.pyd","*.dll"], "enoki": ["*.pyd"]},
    install_requires=["numpy", "scipy"],
	
)
