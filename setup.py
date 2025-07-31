from setuptools import setup, find_packages

setup(
    name="minio_pool_goginski",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "aioboto3",
        "types-aiobotocore[s3]",
    ],
    python_requires=">=3.9",
)
