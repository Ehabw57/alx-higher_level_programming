#include <Python.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t i = 0;
    PyObject *name = NULL;
    PyObject *type = NULL;

    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    while(i < PyList_Size(p))
    {
        name = PyList_GetItem(p, i);
        type = PyObject_Type(name);
        printf("Element %ld: %s\n", i,  ((PyTypeObject*)type)->tp_name);
        i++;
    }
}
