#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="django-cleditor",
    version='0.2.0',
    description="A django form widget for CLEditor (a super clean, MIT licensed WYSIWYG HTML editor) that handles uploading",
    long_description='',
    author="Yuji Tomita",
    author_email="yuji@yujitomita.com",
    url="https://github.com/yuchant/django-cleditor",
    packages=[
        'cleditor',
    ],
    package_dir={
      'cleditor': 'cleditor',
    },
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
