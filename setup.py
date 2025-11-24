from setuptools import setup

setup(
    name="hello-package",
    version="0.1.0",
    author="Your Name",
    py_modules=["index"],
    install_requires=[
        "Pillow>=9.0.0",
    ],
    entry_points={
        'console_scripts': [
            'hello-package=index:main',
        ],
    },
)
