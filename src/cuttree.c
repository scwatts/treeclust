#include "cuttree.h"
#include "hclust-utils.h"
#include "macros.h"


PyObject *cuttree(PyObject *self, PyObject *args) {
    // Top-level arguments
    PyObject *py_merge;
    int n = 0, k = 0;

    // Collect top-level arguments
    if(!PyArg_ParseTuple(args, "OII", &py_merge, &k, &n)) {
      return NULL;
    }

    // Cast python types to c types
    int merge[(n-1) * 2];
    for (size_t i = 0;  i < (size_t)(n - 1); i++) {
        PyObject *py_merge_pair = PySequence_GetItem(py_merge, i);
        merge[i] = PyLong_AsLong(PySequence_GetItem(py_merge_pair, 0));
        merge[i + (n - 1)] = PyLong_AsLong(PySequence_GetItem(py_merge_pair, 1));
    }

    // Call cutree
    int membership[n];
    int karr[1] = { k };
    cutree(merge, karr, n, membership);

    return cast_membership(membership, n);
}


PyObject *cast_membership(int membership[], int n) {
    PyObject *py_membership = PyList_New(n);

    for (size_t i = 0; i < (size_t)n; i++) {
        PyList_SetItem(py_membership, i, PyLong_FromLong(membership[i]));
    }

    return py_membership;
}
