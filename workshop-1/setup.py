from setuptools import setup

setup(
    name='example',
    version='0.0.1',
    packages=['example'],
    entry_points={
        'console_scripts': ['hello=example.__main__:hello']
    }
)
