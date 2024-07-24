from setuptools import setup, find_packages

setup(
    name='hello_world',
    version='0.6',
    packages=find_packages(include=['hello_lib', 'hello_lib.*']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'hello=hello_lib.main:hello',
        ],
    },
)
