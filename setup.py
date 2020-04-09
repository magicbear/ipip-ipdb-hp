#!/usr/bin/env python3
# encoding: utf-8

from distutils.core import setup, Extension

ipdb_module = Extension('ipdb', sources = ['py-ipdb.c', 'ipdb.c'], extra_link_args=["-ljson-c"])

setup(name='ipdb',
      version='0.1.0',
      description='IPIP.net officially supported IP database ipdb format parsing library for python',
      ext_modules=[ipdb_module])
