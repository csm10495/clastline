from setuptools import setup
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'clastline'))
from __init__ import __version__

setup(
    name='clastline',
    author='csm10495',
    author_email='csm10495@gmail.com',
    url='http://github.com/csm10495/clastline',
    version=__version__,
    packages=['clastline'],
    license='MIT License',
    python_requires='>=3.6',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    include_package_data = True,
    install_requires=[''],
    entry_points={},
)