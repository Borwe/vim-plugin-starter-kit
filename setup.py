from setuptools import setup, find_packages


setup(
    name="vim-plugin-starter-kit",
    version='1.0.1',
    description="A tool that creates a scafold for Vim plugins to be written in Python.",
    long_description=open('README.rst').read(),
    author="Jarrod C. Taylor",
    author_email="jarrod.c.taylor@gmail.com",
    url="http://github.com/JarrodCTaylor/vim-plugin-starter-kit",
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Topic :: Text Editors",
        'Intended Audience :: Developers',
    ],
    tests_require=[
        'nose',
        'mock',
        'flake8'
    ],
    test_suite='nose.collector'
)
