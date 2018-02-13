#ifndef __COPHENETIC_H__
#define __COPHENETIC_H__


#include <Python.h>


// Callable from python
PyObject *copheneticd(PyObject *self, PyObject *args);

// Internal methods
PyObject *cast_tip_distances(double *distances, int tip_num, int elements);


#endif
