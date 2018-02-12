#include "copheneticd.h"
#include "dist_nodes.h"
#include "macros.h"


PyObject *run(PyObject *self, PyObject *args) {
    // Top-level arguments
    PyObject *py_edges_source, *py_edges_target, *py_distances;
    int tip_num = 0, node_num = 0, edge_num = 0;

    // Collect top-level arguments
    if(!PyArg_ParseTuple(args, "IIOOOI", &tip_num, &node_num, &py_edges_source, &py_edges_target, &py_distances, &edge_num)) {
      return NULL;
    }

    // Check that that python objects are iterables and of correct type
    if (! is_pytype_pysequence(PyLong_Check, py_edges_source)) {
      PyErr_SetString(PyExc_TypeError, "edge_source was not an integer sequence (e.g. list or tuple)");
      return NULL;
    }
    if (! is_pytype_pysequence(PyLong_Check, py_edges_target)) {
      PyErr_SetString(PyExc_TypeError, "edge_target was not an integer sequence (e.g. list or tuple)");
      return NULL;
    }
    if (! is_pysimplenumeric_pysequence(py_distances)) {
      PyErr_SetString(PyExc_TypeError, "py_distances was not a integer or float sequence (e.g. list or tuple)");
      return NULL;
    }

    // Cast python types to c types
    cast_pysequence_to_array(py_edges_source, edge_source, edge_num, PyLong_AsLong, int);
    cast_pysequence_to_array(py_edges_target, edge_target, edge_num, PyLong_AsLong, int);
    cast_pysequence_to_array(py_distances, edge_distances, edge_num, PyFloat_AsDouble, double);

    // Distance matrix
    size_t elements = tip_num + node_num;
    double *distances = (double *)malloc(sizeof(double) * elements * elements);

    // Get pairwise distance between all nodes
    dist_nodes(&tip_num, &node_num, &edge_source, &edge_target, &edge_distances, &edge_num, distances);

    // Cast tip distances to PyObject
    return cast_tip_distances(distances, tip_num, elements);
}


PyObject *cast_tip_distances(double *distances, int tip_num, int elements) {
    PyObject *py_tip_distances = PyList_New(tip_num * tip_num);

    size_t i = 0, j = 0;
    for (size_t k = 0; k < (elements * elements); k++, i++) {
      if (i == tip_num) { j++; i = 0; k += elements - tip_num; }
      if (j >= tip_num) { break; }
      size_t item_index = j * tip_num + i;
      PyList_SetItem(py_tip_distances, item_index, PyFloat_FromDouble(distances[k]));
    }

    return py_tip_distances;
}
