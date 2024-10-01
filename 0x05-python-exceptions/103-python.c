#include <Python.h>

/**
 * print_python_list - prints python list details
 * @p: the python object
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	size = 0;

	size = PyObject_Length(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List: %zd\n", size);
	printf("[*] Allocated: %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}


/**
 * print_python_bytes - prints python bytes details
 * @p: the python object
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	const char *bytes;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes = PyBytes_AsString(p);

	printf("[*] Python bytes info\n");
	printf("[*] Size of the Python Bytes: %zd\n", size);
	printf("[*] First %zd bytes: ", size > 10 ? 10 : size);
	for (i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf("%02x ", (unsigned char)bytes[i]);
	}
	printf("\n");
}


/**
 * print_python_float - prints python float details
 * @p: the python object
 *
 * Return: nothing
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	printf("[*] Python float info\n");
	printf("[*] Value: %f\n", value);
}
