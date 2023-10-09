#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic information about a Python list.
 * @p: A pointer to a Python object (should be a list).
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = Py_SIZE(p);
    Py_ssize_t alloc = list->allocated;
    Py_ssize_t i;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
    }
}
