#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	const char *type_name;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("Not a valid Python list\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	PyListObject *list_object = (PyListObject *)p;
	Py_ssize_t allocated = list_object->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type_name = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, type_name);
	}
}
