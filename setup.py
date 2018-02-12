#!/usr/bin/env python3
import setuptools


source_files = ['src/copheneticd.c', 'src/bindings.c', 'src/dist_nodes.c']
module_name = 'copheneticd'


extension = setuptools.extension.Extension(
        module_name,
        source_files,
        extra_compile_args=['-Wno-maybe-uninitialized'])


setuptools.setup(
        name=module_name,
        version='0.1',
        test_suite='tests',
        ext_modules=[extension],
        )
