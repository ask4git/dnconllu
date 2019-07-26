
from setuptools import setup, find_packages

setup(
    name='dnconllu',
    version='0.5',
    description='Python module for pre-processing of CoNLL-U corpus',
    author='Jinhyuk Choi',
    author_email='ask4git@gmail.com',
    url='https://github.com/ask4git/dnconllu',
    download_url='',
    install_requires=[],
    packages=find_packages(exclude=['docs', 'tests*']),
    keywords=['natural-language-processing'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)