from setuptools import setup, find_packages

setup(
    name='your_library_name',
    version='0.1.0',
    author='Your Name',
    author_email='yourname@example.com',
    description='A description of your library',
    packages=find_packages(),
    install_requires=[
        'requests>=2.20.0',
        'numpy>=1.19.0',
        # Add other dependencies here
    ],
    # Other parameters like url, license, classifiers, etc.
)
