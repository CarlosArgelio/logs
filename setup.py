from setuptools import setup, find_packages
import setuptools

setup(
    name="logs",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias del paquete
    ],
    author="Carlos Palacios",
    author_email="carlosargelio0104@gmail.com",
    description="El paquete es ideal para guardar logs en un repositorio",
    long_description="Descripción detallada del paquete",
    long_description_content_type="text/markdown",
    # url="https://github.com/usuario/mi_libreria",
    # license="MIT",
    # classifiers=[
    #     # Clasificaciones del paquete, como 'Development Status', 'License', 'Operating System', etc.
    # ],
    python_requires=">=3.9",
    classpath_packages= setuptools.CP_no_binary,
)
