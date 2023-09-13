#include <Python.h>

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: PyObject
 */
void print_python_bytes(PyObject *p){
PyBytesObject *bytes;
unsigned int i, size;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
bytes = (PyBytesObject *)p;
size = PyBytes_Size(p);

printf("  size: %d\n", size);
printf("  trying string: %s\n", bytes->ob_sval);

if (size > 10)
size = 10;
    
printf("  first %u bytes: ", size);
for (i = 0; i < size; i++)
{
printf("%02x", (unsigned char)bytes->ob_sval[i]);
if (i < size - 1)
printf(" ");
}
printf("\n");
}

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject
 */
void print_python_list(PyObject *p){
PyListObject *list;
unsigned int i, size, alloc;

printf("[*] Python list info\n");

if (!PyList_Check(p))
{
printf("[ERROR] Invalid List Object\n");
return;
}

list = (PyListObject *)p;
size = PyList_Size(p);
alloc = list->allocated;

printf("[*] Size of the Python List = %u\n", size);
printf("[*] Allocated = %u\n", alloc);

for (i = 0; i < size; i++)
{
PyObject *item = PyList_GetItem(p, i);
const char *item_type = item->ob_type->tp_name;
printf("Element %u: %s\n", i, item_type);

if (strcmp(item_type, "bytes") == 0)
print_python_bytes(item);
}
}
