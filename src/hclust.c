#include "hclust.h"
#include "macros.h"


PyObject *hclust(PyObject *self, PyObject *args) {
    // Input arguments
    double distance[] = {1.920595, 2.320279, 3.088601, 3.019876, 1.208072, 3.227629, 3.158904, 3.627313, 3.558588, 1.617937};
    int n = 5;
    int iopt = 8;

    // Set up variables
    int length = (n*(n-1)/2);
    int ia[n], ib[n], nn[n], flag[n], order[n], iia[n], iib[n];
    double crit[n], disnn[n], membr[n];

    // Initialise all memory
    for (size_t i = 0; i < n; i++) {
        ia[i] = ib[i] = nn[i] = flag[i] = order[i] = iia[i] = iib[i] = crit[i] = disnn[i] = 0;
        membr[i] = 1;
    }

    // Run clustering and interpret results
    hclust_(&n, &length, &iopt, ia, ib, crit, membr, nn, disnn, flag, distance);
    hcass2_(&n, ia, ib, order, iia, iib);

    return PyUnicode_FromString("Returning");
}
