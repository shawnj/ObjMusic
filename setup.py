# -*- coding: utf-8 -*-
import codecs
import os
import re
import setuptools


def local_file(file):
  return codecs.open(
    os.path.join(os.path.dirname(__file__), file), 'r', 'utf-8'
  )

install_reqs = [
  line.strip()
  for line in local_file('requirements.txt').readlines()
  if line.strip() != ''
]

setuptools.setup(
  name = "objmusic",
  version = '0.1.1',
  author = "Shawn Junell",
  author_email = "none@none.com",
  description = "ObjMusic for Python",
  license = "MIT",
  keywords = "python objmusic API",
  url = "https://github.com/shawnj/objmusic",
  install_requires = install_reqs,
  packages = ['objmusic'],
  long_description = local_file('README.md').read(),
  classifiers = [
    'Development Status :: 4 - Beta',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3'
  ]
)