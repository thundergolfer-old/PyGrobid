from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from setuptools.command.install import install
from codecs import open  # To use a consistent encoding
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pygrobid',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version='0.0.15',

    description='Python bindings to the Grobid machine learning citation extraction software.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/thundergolfer/PyGrobid',

    # Author details
    author='Jonathon Belotti',
    author_email='jonathon.bel.melbourne@gmail.com',

    # Choose your license
    license='Apache License 2.0',

    # See https://PyPI.python.org/PyPI?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='grobid citation-extraction bindings',

    packages=find_packages(),

    install_requires=["py4j", "requests"],

    setup_requires=["py4j", "requests"],

    include_package_data=True,

    #run custom code
    # cmdclass={'install': MyInstall}
)
