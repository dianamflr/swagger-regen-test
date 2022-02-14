# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="RSA API - Testing Regen Code",
    author_email="",
    url="",
    keywords=["Swagger", "RSA API - Testing Regen Code"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    CRC&#x27;s RSA (Rural Spectrum Analysis) application is a web service that supports  research efforts by providing an interface to generate RSA reports and monitor RSA jobs.       Possible Future Iterations: * Queueing multiple RSA jobs  * Caching  * Validation of paremeters
    """
)
