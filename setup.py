from setuptools import setup, find_packages

setup(
    name='ridethebus',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ridethebus=main:main',
        ],
    },
)
