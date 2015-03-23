from setuptools import setup
setup(
    name='simpleWatch',
    packages=['src'],
    version='1.0',
    description='Extemely simple file watcher',
    author='Marcus Buffett',
    author_email='marcusbuffett@me.com',
    url='',
    download_url='',
    entry_points={
        'console_scripts': [
            'simpleWatch = src.main:main',
        ],
    },
    keywords=['file-watcher, watch, file'],
    classifiers=["Programming Language :: Python :: 3"],
)
