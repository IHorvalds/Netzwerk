# -*- coding: utf-8 -*-

import setuptools
import versioneer

short_description = "Framework"
try:
  with open("README.md", "r") as handle:
    long_description = handle.read()
except: # noqa
  long_description = short_description

if __name__ == "__main__":
  setuptools.setup(
    name='framework',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description=short_description,
    author='Mihail Stoian',
    author_email='mihail.stoian@tum.de',
    url='https://github.com/stoianmihail/Lumina/',
    license='MIT',
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
    install_requires=[
      'numpy>=1.7',
    ],
    zip_safe=True,
    long_description=long_description,
    long_description_content_type="text/markdown"
)
