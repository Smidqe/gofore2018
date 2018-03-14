Recipebook
##########

.. py:function:: save()

	Save the contents of the recipebook into a file in json format

.. py:function:: load(path=None)

	Load data from a json format into the applications memory, if path is not set it relies on PATH_STORAGE

.. py:function:: add(recipe, backup)

	Add a Recipe object to the storage, if backup is set backup the storage file before it is changed

.. py:function:: remove(recipe, method, backup=False)

	Remove a recipe, depending on the method given, either a value or an index, make a backup if backup parameter is set

.. py:function:: search(what, value)

	Search the recipes for various items assigned in 'what', the values are compared in lowercase
