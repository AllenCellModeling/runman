#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

test_requirements = [
    "codecov",
    "pytest",
    "pytest-cov",
    "pytest-raises",
    "flake8",
    "black",
]

setup_requirements = ["pytest-runner"]

dev_requirements = [
    "bumpversion>=0.5.3",
    "coverage>=5.0a4",
    "ipython>=7.5.0",
    "m2r>=0.2.1",
    "pytest>=4.3.0",
    "pytest-cov==2.6.1",
    "pytest-raises>=0.10",
    "pytest-runner>=4.4",
    "Sphinx>=2.0.0b1",
    "sphinx_rtd_theme>=0.1.2",
    "tox>=3.5.2",
    "twine>=1.13.0",
    "wheel>=0.33.1",
]

requirements = ["cloudpickle"]

extra_requirements = {
    "test": test_requirements,
    "setup": setup_requirements,
    "dev": dev_requirements,
    "all": [*requirements, *test_requirements, *setup_requirements, *dev_requirements],
}

setup(
    author="David Williams",
    author_email="cdavew@alleninstitute.org",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: Free for non-commercial use",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    description="Mange runs of stochastic simulations",
    install_requires=requirements,
    license="Allen Institute Software License",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="runman",
    name="runman",
    packages=find_packages(),
    python_requires=">=3.6",
    setup_requires=setup_requirements,
    test_suite="runman/tests",
    tests_require=test_requirements,
    extras_require=extra_requirements,
    url="https://github.com/AllenCellModeling/runman",
    # Do not edit this string manually, always use bumpversion
    version="0.2.0",
    zip_safe=False,
)
