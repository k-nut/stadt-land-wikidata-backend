from setuptools import setup

setup(
    name='stadt_land_wikidata',
    packages=['stadt_land_wikidata'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)