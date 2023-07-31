from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name="isyatirimhisse",
    version="0.2.1",
    packages=find_packages(),
    author="Uraz Akgül",
    author_email="urazdev@gmail.com",
    description="İş Yatırım'ın web sitesinden veri çekme işlemlerini kolaylaştıran ve isteğe göre özelleştirilebilen bir kütüphane.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/urazakgul/isyatirimhisse",
    license="MIT",
    install_requires=[
        "requests",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=">=3.8",
)