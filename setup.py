import os

from setuptools import setup, find_packages

GH_USER = os.getenv("GH_USER")
GH_TOKEN = os.getenv("GH_TOKEN")

setup(
    name="jobsim",
    packages=find_packages(include=["jobsim"]),
    version="1.0.0",
    install_requires=[
        "dacite",
        "names",
        "pyyaml",
        "pytest",
        "pytest-cov",
        f"pytest-splunk @ git+https://{GH_USER}:{GH_TOKEN}@github.com/uoboda-splunk/pytest-splunk.git@main",
    ],
    package_data={"": ["departments/*yaml", "locations/*.yaml"]},
    include_package_data=True,
)
