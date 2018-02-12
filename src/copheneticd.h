#ifndef __CORE_H__
#define __CORE_H__


#include <Python.h>


// Callable from python
PyObject *run(PyObject *self, PyObject *args);

// Internal methods
PyObject *cast_tip_distances(double *distances, int tip_num, int elements);


#endif
