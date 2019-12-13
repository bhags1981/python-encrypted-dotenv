# -*- coding: utf-8 -*-
from setuptools import setup


def read_files(files):
    data = []
    for file in files:
        with open(file) as f:
            data.append(f.read())
    return "\n".join(data)


def _requires_from_file(filename):
    return open(filename).read().splitlines()


long_description = read_files(['README.md', 'CHANGELOG.md'])

meta = {}
with open('./src/enc_dotenv/version.py') as f:
    exec(f.read(), meta)

setup(
    name="enc_dotenv",
    description="encrypted env",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=meta['__version__'],
    author="Sinyu Jung",
    author_email="",
    url="https://github.com/bhags1981/python-encrypted-dotenv",
    keywords=['encrypted　environment variables', 'deployments', 'settings', 'env', 'dotenv',
              'configurations', 'python'],
    packages=['enc_dotenv'],
    package_dir={'': 'src'},
    package_data={
        'enc_dotenv': ['py.typed'],
    },
    install_requires=[
        "python-dotenv",
        "pyAesCrypt"
    ],

    # extras_require={
    #     'cli': ['click>=5.0', ],
    # },
    # entry_points='''
    #     [console_scripts]
    #     dotenv=dotenv.cli:cli
    # ''',
    classifiers=[
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.3',
        # 'Programming Language :: Python :: 2.4',
        # 'Programming Language :: Python :: 2.5',
        # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'Environment :: Web Environment',
    ]
)

# (*) Please direct queries to the discussion group, rather than to me directly
#     Doing so helps ensure your question is helpful to other users.
#     Queries directly to my email are likely to receive a canned response.
#
#     Many thanks for your understanding.
# repository: https://upload.pypi.org/legacy/
