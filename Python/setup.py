#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
  author="Jean-Philippe Fortin",
  author_email='fortin946@gmail.com',
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
  description="ComBat algorithm for harmonizing multi-site imaging data",
  license="MIT license",
  url="https://github.com/fortinj2/ComBatHarmonization/python/ComBat",
  project_urls={
    "Source Code": "https://github.com/fortinj2/ComBatHarmonization/python/ComBat",
  },
  name='combat',
  packages=['combat',],
  version='0.1.0',
  zip_safe=False,
)