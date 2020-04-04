"""Setup script for the mitsuba2 project."""

import os
from setuptools import setup  
import glob
import shutil

libname = "mitsuba"

# Force platform specific wheel, inpired from Open3D's setup.py
try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    # https://stackoverflow.com/a/45150383/1255535
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    print('Warning: cannot import "wheel" package to build platform-specific wheel')
    print('Install the "wheel" package to fix this warning')
    bdist_wheel = None
cmdclass = {'bdist_wheel': bdist_wheel} if bdist_wheel is not None else dict()

# Copy dlls in ./dist/python/mitsuba
for file in list(glob.glob("./dist/*.dll")):
	shutil.copy2(file,"./dist/python/mitsuba")

for file in list(glob.glob("./dist/*.so")):
	shutil.copy2(file,"./dist/python/mitsuba")
	
os.makedirs("./dist/python/mitsuba/plugins", exist_ok=True)
for file in list(glob.glob("./dist/plugins/*.dll")):
	shutil.copy2(file,"./dist/python/mitsuba/plugins")
	
for file in list(glob.glob("./dist/plugins/*.so")):
	shutil.copy2(file,"./dist/python/mitsuba/plugins")
	
# Setup	
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
    package_data={"mitsuba": ["*.pyd","*.dll","*.so","plugins/*.dll","plugins/*.so"], "enoki": ["*.pyd","*.so"]},
    install_requires=["numpy", "scipy"],
	cmdclass=cmdclass,
	
)
