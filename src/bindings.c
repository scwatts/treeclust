#include "copheneticd.h"


// Method documentation
static char copheneticd_docs[] = "Calculate pairwise distances from a phylogenetic tree";


// Method definition
static PyMethodDef CopheneticdMethods[] = {
    {"run", run, METH_VARARGS, copheneticd_docs},
    {NULL, NULL, 0, NULL}
};


// Module documentation
static char copheneticd_module_docs[] = "Calculate pairwise distances from a phylogenetic tree";


// Module definition
static struct PyModuleDef copheneticd_module = {
    PyModuleDef_HEAD_INIT,
    "copheneticd",
    copheneticd_module_docs,
    -1,
    CopheneticdMethods
};


// Module init
PyMODINIT_FUNC PyInit_copheneticd(void) {
	return PyModule_Create(&copheneticd_module);
}
