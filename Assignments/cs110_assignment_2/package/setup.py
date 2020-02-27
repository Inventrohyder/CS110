import setuptools

with open("./ActivityTasks/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="activityTasks-Udacity-inventrohyder", 
    version="0.1.0-0.1.0",
    author="Haitham Alhad",
    author_email="haitham.hyder@minerva.kgi.edu",
    description="A Activity and Tasks package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages()
)