from setuptools import setup, find_packages

setup(
    name='the-lord-of-the-rings-sdk',
    version='0.1.0',
    author='Sebastijan Stevanovic',
    author_email='sebastijan94@yahoo.com',
    description='A Python SDK for accessing the Lord of the Rings API',
    long_description=open('README.md').read(),  # Include your README as the long description
    long_description_content_type='text/markdown',
    url='https://github.com/sebastijan94/Sebastijan-SDK',
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9.19',  # Specify the Python version required
)
