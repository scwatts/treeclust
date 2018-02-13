#ifndef __CUTTREE_H__
#define __CUTTREE_H__


#include <Python.h>


// Callable from python
PyObject *cuttree(PyObject *self, PyObject *args);

// Internal methods
PyObject *cast_membership(int membership[], int n);


#endif
