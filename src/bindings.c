#include "copheneticd.h"


// Method documentation
static char copheneticd_docs[] = "Calculate pairwise distances from a phylogenetic tree";


// Method definition
static PyMethodDef TreeclustMethods[] = {
    {"copheneticd", copheneticd, METH_VARARGS, copheneticd_docs},
    {NULL, NULL, 0, NULL}
};


// Module documentation
static char treeclust_module_docs[] = "Tree clustering utilities";


// Module definition
static struct PyModuleDef treeclust_module = {
    PyModuleDef_HEAD_INIT,
    "_treeclust",
    treeclust_module_docs,
    -1,
    TreeclustMethods
};


// Module init
PyMODINIT_FUNC PyInit__treeclust(void) {
	return PyModule_Create(&treeclust_module);
}
