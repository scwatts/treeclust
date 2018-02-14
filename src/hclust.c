#include "hclust.h"
#include "macros.h"


PyObject *hclust(PyObject *self, PyObject *args) {
    // Top-level arguments
    PyObject *py_distances;
    int n = 0, iopt = 0;

    // Collect top-level arguments
    if(!PyArg_ParseTuple(args, "OII", &py_distances, &n, &iopt)) {
      return NULL;
    }

    // Check that that python objects are iterables and of correct type
    // TODO: move these checks to the python interface
    if (! is_pysimplenumeric_pysequence(py_distances)) {
      PyErr_SetString(PyExc_TypeError, "py_distances was not a integer or float sequence (e.g. list or tuple)");
      return NULL;
    }

    // Cast python types to c types
    size_t distance_num = (size_t)PySequence_Size(py_distances);
    double *distances = (double *)malloc(distance_num * sizeof(double));
    for (size_t i = 0; i < distance_num; ++i){
        distances[i] = PyFloat_AsDouble(PySequence_GetItem(py_distances, i));
    }

    // Set up variables
    int length = (n*(n-1)/2);
    int ia[n], ib[n], nn[n], flag[n], order[n], iia[n], iib[n];
    double crit[n], disnn[n], membr[n];

    // Initialise all memory
    // TODO: better way to do this? memset?
    for (size_t i = 0; i < (size_t)n; i++) {
        ia[i] = ib[i] = nn[i] = flag[i] = order[i] = iia[i] = iib[i] = crit[i] = disnn[i] = 0;
        membr[i] = 1;
    }

    // Run clustering and interpret results
    hclust_(&n, &length, &iopt, ia, ib, crit, membr, nn, disnn, flag, distances);
    hcass2_(&n, ia, ib, order, iia, iib);

    free(distances);
    return cast_result_to_pytype(iia, iib, crit, order, n);
}


PyObject *cast_result_to_pytype(int iia[], int iib[], double crit[], int order[], int n) {
    PyObject *py_data = PyDict_New();
    PyObject *py_crit = PyList_New(n-1);
    PyObject *py_merge = PyList_New(n-1);
    PyObject *py_order = PyList_New(n);

    // Zip iia and iib together
    // Cast crit to list
    for (size_t i = 0; i < (size_t)(n-1); i++) {
        // Create merge list item and then record
        PyObject *py_merge_item = PyList_New(2);
        PyList_SetItem(py_merge_item, 0, PyLong_FromLong(iia[i]));
        PyList_SetItem(py_merge_item, 1, PyLong_FromLong(iib[i]));
        PyList_SetItem(py_merge, i, py_merge_item);

        // Record crit item
        PyList_SetItem(py_crit, i, PyFloat_FromDouble(crit[i]));
    }
    // Cast order to py list
    for (size_t i = 0; i < (size_t)n; i++) { PyList_SetItem(py_order, i, PyLong_FromLong(order[i])); }

    // Set py dict items
    PyDict_SetItemString(py_data, "merge", py_merge);
    PyDict_SetItemString(py_data, "height", py_crit);
    PyDict_SetItemString(py_data, "order", py_order);

    return py_data;
}
