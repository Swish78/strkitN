from setuptools import setup, find_packages

setup(
    name='strkitN',
    version='0.1.0',
    author='Swayam Patil',
    author_email='swayampatil7803@gmail.com',
    description='A string manipulation package with additional features',
    long_description='''strkitN is a Python package that provides various string manipulation functions 
                        along with additional features such as palindrome detection, substring operations, 
                        and more.''',
    url='https://github.com/Swish78/strkitN',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='string manipulation utilities',
    install_requires=[
        'numpy>=1.18.0',
    ],
    python_requires='>=3.7',
)
