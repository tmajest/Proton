import io
from setuptools import setup, find_packages

VERSION = "0.1"

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name="Proton",
    version=VERSION,
    author="Tony Majestro",
    description="Proton - the RSS and Atom feed aggregator.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'python-dateutil',
        'feedparser',
    ],
    extras_require={
        'test': ['pytest'],
    },
)
    
