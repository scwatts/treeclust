#!/usr/bin/env python3
import setuptools


source_files = ['src/copheneticd.c', 'src/bindings.c', 'src/dist_nodes.c']
extension = setuptools.extension.Extension(
        '_copheneticd',
        source_files,
        extra_compile_args=['-Wno-maybe-uninitialized'])


setuptools.setup(
        name='cophenetic',
        version='0.1',
        test_suite='tests',
        ext_modules=[extension],
        packages=setuptools.find_packages()
        )
