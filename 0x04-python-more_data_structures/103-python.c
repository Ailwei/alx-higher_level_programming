#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (PyList_Check(p)) {
        Py_ssize_t size = PyList_Size(p);
        Py_ssize_t i;
        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
        for (i = 0; i < size; i++) {
            PyObject *item = PyList_GetItem(p, i);
            const char *type = item->ob_type->tp_name;
            printf("Element %ld: %s\n", i, type);
        }
    } else {
        PyErr_SetString(PyExc_TypeError, "Invalid List Object");
        PyErr_Print();
    }
}

void print_python_bytes(PyObject *p) {
    if (PyBytes_Check(p)) {
        Py_ssize_t size = PyBytes_Size(p);
        Py_ssize_t i;
        Py_ssize_t max_display = (size > 10) ? 10 : size;
        printf("[.] bytes object info\n");
        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", PyBytes_AsString(p));
        printf("[.]\n");
        printf("  first %ld bytes: ", max_display);
        for (i = 0; i < max_display; i++) {
            printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
            if (i + 1 < max_display)
                printf(" ");
        }
        printf("\n");
    } else {
        PyErr_SetString(PyExc_TypeError, "Invalid Bytes Object");
        PyErr_Print();
    }
}
