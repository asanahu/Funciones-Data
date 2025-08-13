from pathlib import Path
from setuptools import setup, find_packages

README = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

setup(
    name="formulas",
    version="0.1.0",
    description="Funciones reutilizables para ETL y análisis de datos.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt")],
)
