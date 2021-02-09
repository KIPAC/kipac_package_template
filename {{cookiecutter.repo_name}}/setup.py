from setuptools import setup

from python.bolo import version

setup(
    name="{{cookiecutter.package_name}}",
    version=version.get_git_version(),
    author="",
    author_email="",
    url = "https://github.com/KIPAC/{{cookiecutter.repo_name}}",
    package_dir={"":"python"},
    packages=["{{cookiecutter.package_name}}"],
    description="={{cookiecutter.package_desc}}",
    long_description=open("README.md").read(),
    package_data={"": ["README.md", "LICENSE"]},
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
    install_requires=[],
)
