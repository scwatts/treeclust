#!/usr/bin/env python3
import setuptools
import subprocess
import shutil
import sys


# Set package details
package_name = 'treeclust'
package_description = 'Efficiently calculate cophenetic distance between phylogeny tips'
package_version = '0.0.1'
author = 'Stephen Watts'
licence = 'gpl'

# Check that Python 3.5+ is installed
if sys.version_info < (3,5):
    msg = 'error: %s requires Python 3.5+. Python %d.%d detected'
    print(msg % (package_name, *sys.version_info[:2]))
    sys.exit(1)

# Check for gfortran
if not shutil.which('gfortran'):
    msg = 'error: %s requires gfortran for installation'
    print(msg % package_name)
    sys.exit(1)

# Compile hclust.f
hclustf_src = 'src/hclust.f'
hclustf_obj = 'src/hclustf.o'
cmd = 'gfortran -fPIC -c %s -o %s' % (hclustf_src, hclustf_obj)
stderr = subprocess.run(cmd, shell=True, check=True)

# Set extension details
source_files = ['src/copheneticd.c', 'src/bindings.c', 'src/dist_nodes.c',
                'src/hclust.c', 'src/cuttree.c', 'src/hclust-utils.c']
fortran_objects = [hclustf_obj]
extension = setuptools.Extension(
        '_treeclust',
        source_files,
        extra_objects=fortran_objects,
        extra_compile_args=['-Wno-maybe-uninitialized'])

# Call setup
setuptools.setup(
        name=package_name,
        version=package_version,
        licence=licence,
        test_suite='tests',
        ext_modules=[extension],
        packages=setuptools.find_packages()
        )
