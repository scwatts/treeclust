#ifndef __MACROS_H__
#define __MACROS_H__

#define is_pytype_pysequence(t, s) ( PySequence_Check(s) && t(PySequence_GetItem(s, 0)) )
#define is_pysimplenumeric_pysequence(s) ( is_pytype_pysequence(PyLong_Check, s) || is_pytype_pysequence(PyFloat_Check, s) )
#define cast_pysequence_to_array(s, d, l, st, dt) dt d[l]; \
  for (size_t i = 0; i < l; i++) { d[i] = (dt)st(PySequence_GetItem(s, i)); }


#endif
