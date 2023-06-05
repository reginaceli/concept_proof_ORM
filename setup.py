import os
from setuptools import setup, find_packages


def read(*paths):
    """Read a text file and return its lines"""
    rootpath= os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)

    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(filepath):
    return[
        line.strip()
        for line in read(filepath).split("\n")
        if not line.startswith(("#","git+",'"',"-"))
    ]



setup(
    name="player",
    version="0.1.0",
    description="reward system players",
    author="regina celi da sivla",
    packages=find_packages(),
    entry_points={
        "console_scripts":[
            "player = player.__main__:main"
        ]
    },
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test":read_requirements("requirements.test.txt"),
        "dev":read_requirements("requirements.dev.txt")
    }
)
