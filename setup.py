import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lisabet",
    version="0.1.49",
    author="Devbrones",
    author_email="crhlm@pm.me",
    description="A stenography training application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devbrones/lisabet",
    project_urls={
        "Bug Tracker": "https://github.com/devbrones/lisabet/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "lisabet"},
    packages=setuptools.find_packages(where="lisabet"),
    python_requires=">=3.10",
    install_requires=[
        'tkinter',
        'collections',
        'time',
        'json',
        'random'
    ]
)
