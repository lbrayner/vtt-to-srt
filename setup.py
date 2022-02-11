from setuptools import setup, find_packages

setup(
    name='vtt_to_srt',
    version='0.1',
    url='',
    license='LGPLv2',
    python_requires='>=3.4',
    author='lbrayner',
    author_email='lbrayner@users.noreply.github.com',
    description='vtt_to_srt',
    py_modules=['vtt_to_srt'],
    install_requires=[
        "pysrt",
        "webvtt-py",
        "argparse"
    ],
    entry_points={
        'console_scripts': ['vtt_to_srt=vtt_to_srt:main']
    }
)
