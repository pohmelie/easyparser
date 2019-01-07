from setuptools import setup
from os.path import join, dirname

setup(
    name='easyparser',
    version='0.1.0',
    python_requires='>=3.6.0',
    description='data ejector',
    author='Andrey C, Nikita M',
    author_email='frill2one@gmail.com',
    packages=['findrecursive'],
    install_requires=['requests', 'lxml'],
    long_description=open(join(dirname(__file__), 'README.md')).read()
)