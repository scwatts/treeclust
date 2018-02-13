#ifndef __HCLUST_H__
#define __HCLUST_H__


#include <Python.h>


// Callable from python
PyObject *hclust(PyObject *self, PyObject *args);

// Internal methods
PyObject *cast_result_to_pytype(int iia[], int iib[], double crit[], int order[], int n);

// External methods (fortran)
void hclust_(int *n, int *len, int *iopt, int ia[], int ib[], double crit[], double membr[], int nn[], double disnn[], int flag[], double diss[]);
void hcass2_(int *n, int ia[], int ib[], int iorder[], int iia[], int iib[]);


#endif
