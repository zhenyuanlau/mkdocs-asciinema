from setuptools import setup

setup(
    name="mkdocs-asciinema",
    version="1.0.0",
    author="",
    author_email="",
    description="A Python library that make asciinema play in mkdocs",
    long_description="make asciinema play in mkdocs",
    long_description_content_type="text/markdown",
    url="https://github.com/zhenyuanlau/mkdocs-asciinema",
    packages=["mkdocs-asciinema"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    entry_points={
        "mkdocs.plugins": [
            "mkdocs-asciinema = src.mkdocs_asciinema.plugin:MkdocsAsciinemaPlugin"
        ]
    },
)
