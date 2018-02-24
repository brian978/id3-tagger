from setuptools import setup, find_packages

setup(
    name='id3-tagger',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'mutagen',
    ],
    url='https://github.com/brian978/id3-tagger',
    license='BSD 3-Clause License',
    author='brian978',
    author_email='',
    description='The repository hosts a small CLI application to get/set ID3 tags'
)
