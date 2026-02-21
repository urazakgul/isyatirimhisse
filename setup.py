from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name="isyatirimhisse",
    version="5.0.1",
    packages=find_packages(),
    author="Uraz Akgül",
    author_email="urazdev@gmail.com",
    description="Fetches data from the IS Investment website.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/urazakgul/isyatirimhisse",
    license="MIT",
    install_requires=[
        "requests",
        "pandas",
        "openpyxl",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=">=3.8",
)