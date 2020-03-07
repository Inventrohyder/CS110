import setuptools

setuptools.setup(
    name="minerva-bloom-inventrohyder", 
    version="0.1.0a",
    author="Haitham Alhad",
    author_email="haitham.hyder@minerva.kgi.edu",
    description="Package created for my 3rd CS110 assignment",
    install_requires=[
        'pandas',
        'seaborn'
    ],
    packages=setuptools.find_packages()
)