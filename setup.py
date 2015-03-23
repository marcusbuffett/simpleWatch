from setuptools import setup
setup(
    name='simpleWatch',
    packages=['src'],
    version='1.1',
    description='Extemely simple file watcher',
    author='Marcus Buffett',
    author_email='marcusbuffett@me.com',
    url='https://github.com/marcusbuffett/simpleWatch/tree/master',
    download_url='',
    install_requires=[
        'termcolor',
        'watchdog'
    ],
    entry_points={
        'console_scripts': [
            'swatch = src.main:main',
        ],
    },
    keywords=['file-watcher, watch, file'],
    classifiers=["Programming Language :: Python :: 3"],
)
