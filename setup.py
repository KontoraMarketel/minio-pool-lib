from setuptools import setup, find_packages

setup(
    name="src",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "aioboto3",
        "types-aiobotocore[s3]",
    ],
    python_requires=">=3.9",
)
