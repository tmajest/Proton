from setuptools import setup, find_packages

VERSION = "0.1"

setup(
	name="AtomBomb",
	version=VERSION,
	packages=find_packages(),
	install_requires=[
		'flask',
	],
	author="Tony Majestro",
	description="Site that aggregates my rss feeds",
)
    
