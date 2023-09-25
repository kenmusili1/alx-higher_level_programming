/*
 * File: python.c
 * Auth: Kennedy Musili
*/

#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#define PY_SSIZE_T_CLEAN

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_hexn(const char *str, int n);

/**
 * print_python_list - prints info about Python lists
 * @p: pointer to a Python object
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    
    if (!PyList_Check(p)) {
        PyErr_Format(PyExc_TypeError, "Invalid List Object");
        PyErr_Print();
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, type);

        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}

/**
 * print_python_bytes - prints info about Python bytes
 * @p: pointer to a Python object
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;

    if (!PyBytes_Check(p)) {
        PyErr_Format(PyExc_TypeError, "Invalid Bytes Object");
        PyErr_Print();
        return;
    }

    size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    if (size > 10)
        printf("  first 10 bytes: ");
    else
        printf("  first %ld bytes: ", size);

    for (i = 0; i < size && i < 10; i++) {
        printf("%02hhx", ((char *)PyBytes_AsString(p))[i]);
        if (i < size - 1 && i < 9)
            printf(" ");
    }

    printf("\n");
}

/**
 * print_python_float - prints info about Python float
 * @p: pointer to a Python object
 */
void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        PyErr_Format(PyExc_TypeError, "Invalid Float Object");
        PyErr_Print();
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
}

