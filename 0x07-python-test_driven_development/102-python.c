#include <Python.h>

/**
 * print_python_string - Print information about a Python string object
 * @p: PyObject pointer
 */
void print_python_string(PyObject *p)
{
    if (PyUnicode_Check(p))
    {
        Py_ssize_t length;
        Py_UNICODE *unicode;

        printf("[.] string object info\n");
        printf("  type: %s\n", Py_TYPE(p)->tp_name);

        length = PyUnicode_GET_LENGTH(p);
        printf("  length: %ld\n", length);

        unicode = PyUnicode_AS_UNICODE(p);
        if (PyUnicode_IS_COMPACT_ASCII(p))
        {
            printf("  value: %ls\n", unicode);
        }
        else if (PyUnicode_IS_COMPACT(p))
        {
            printf("  value: %ls\n", unicode);
        }
        else
        {
            printf("  value: %ls\n", unicode);
        }
    }
    else
    {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
    }
}
