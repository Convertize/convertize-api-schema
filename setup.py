#!/usr/bin/env python

import os
import sys

from distutils.command.build import build as BuildCommand

from setuptools import find_packages, setup
from setuptools.command.develop import develop as DevelopCommand
from setuptools.command.sdist import sdist as SDistCommand

ROOT = os.path.dirname(os.path.abspath(__file__))


# add convertize to path so we can import shop.utils.
sys.path.insert(0, os.path.join(ROOT, "src"))

VERSION = "1.0b.dev0"


cmdclass = {
    "sdist": SDistCommand,
    "develop": DevelopCommand,
    "build": BuildCommand,
    # "build_assets": BuildCommand, todo: (gabrielgaliaso) build assets
}


def get_requirements(env):
    with open("requirements-{env}.txt".format(env=env)) as fp:
        return [x.strip() for x in fp.read().split("\n") if not x.startswith("#")]


# Only include dev requirements in non-binary distributions as we don't want these
# to be listed in the wheels. Main reason for this is being able to use git/URL dependencies
# for development, which will be rejected by PyPI when trying to upload the wheel.
extras_require = {}
if not sys.argv[1:][0].startswith("bdist"):
    extras_require["dev"] = get_requirements("dev")

setup(
    name="apidocs",
    version=VERSION,
    author="Convertize E-Commerce",
    author_email="dev@convertize.com.br",
    url="https://www.convertize.com.br",
    description="Convertize E-Commerce",
    long_description=open(os.path.join(ROOT, "README.md")).read(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages("src"),
    zip_safe=False,
    install_requires=get_requirements("base"),
    extras_require=extras_require,
    cmdclass=cmdclass,
    license="SAAS",
    include_package_data=True,
    package_data={},
    exclude_package_data={},
    entry_points={"console_scripts": ["apidocs = apidocs.cli:main"]},
    classifiers=["Convertize :: E-Commerce"],
)
