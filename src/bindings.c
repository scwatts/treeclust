#include "copheneticd.h"
#include "hclust.h"
#include "cuttree.h"


// Method documentation
static char copheneticd_docs[] = "Calculate pairwise distances from a phylogenetic tree";
static char hclust_docs[] = "Cluster distance matrix";
static char cuttree_docs[] = "Cut a hclust dendrogram at a specific threshold";


// Method definition
// TODO: have a single function to run all; this will require pure c-interfaces for all sub-routines
static PyMethodDef TreeclustMethods[] = {
    {"copheneticd", copheneticd, METH_VARARGS, copheneticd_docs},
    {"hclust", hclust, METH_VARARGS, hclust_docs},
    {"cuttree", cuttree, METH_VARARGS, cuttree_docs},
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
