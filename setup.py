from setuptools import setup, find_packages

setup(
    name='import_validator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'import_validator=import_validator.validator:main',
        ],
    },
    description='A tool for validating Strivacity import files',
    author='Norbert Kiss',
    author_email='norbert.kiss@strivacity.com',
    url='https://github.com/Strivacity/import_validator',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)