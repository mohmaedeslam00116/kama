# kama/setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kama-lang"
    version="1.0.0"
    author="Mohamed eslam"
    author_email="mohamedeslam0007@gmail.com"

    description="A custom programming language for AI and data analysis."

    long_description=long_description README.md
    long_description_content_type="text/markdown"
    url="https://github.com/your_username/kama-lang",  # رابط المشروع على GitHub أو أي منصة أخرى
    packages=find_packages()
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    python_requires=">=3.7"

    install_requires=[
        "streamlit",
        "transformers",
        "tensorflow",
        "google-cloud-storage",
        "boto3",
        "pandas",
        "numpy",
        "matplotlib",
        "pickle",
        "nltk",
        "gensim",
        "Pillow",
        "opencv-python"
    ]
)