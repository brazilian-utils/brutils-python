import importlib
import inspect
import pkgutil
import unittest


def get_public_functions(module):
    """Get all public functions and methods in the module."""
    return [
        name
        for name, obj in inspect.getmembers(module, inspect.isfunction)
        if not is_private_function(name) and inspect.getmodule(obj) == module
    ] + [
        name
        for name, obj in inspect.getmembers(module, inspect.ismethod)
        if obj.__module__ == module.__name__ and not name.startswith("_")
    ]


def get_imported_methods(module):
    """Get all names in the module's namespace."""
    return [
        name
        for name in dir(module)
        if not is_private_function(name) and not is_standard_function(name)
    ]


def is_private_function(name):
    """Check if a function is private."""
    return name.startswith("_")


def is_standard_function(name):
    """Check if a function name is a standard or built-in function."""
    return name in dir(__builtins__) or (
        name.startswith("__") and name.endswith("__")
    )


class TestImports(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the package and its __init__.py module."""
        cls.package_name = "brutils"
        cls.package = importlib.import_module(cls.package_name)
        cls.init_module = importlib.import_module(
            f"{cls.package_name}.__init__"
        )

        cls.all_public_methods = []
        cls.imported_methods = []

        # Iterate over all submodules and collect their public methods
        for _, module_name, _ in pkgutil.walk_packages(
            cls.package.__path__, cls.package.__name__ + "."
        ):
            module = importlib.import_module(module_name)
            cls.all_public_methods.extend(get_public_functions(module))

        # Collect imported methods from __init__.py
        cls.imported_methods = get_imported_methods(cls.init_module)

        # Filter out standard or built-in functions
        cls.filtered_public_methods = [
            method
            for method in cls.all_public_methods
            if not is_standard_function(method)
        ]
        cls.filtered_imported_methods = [
            method
            for method in cls.imported_methods
            if not is_standard_function(method)
        ]

        # Remove specific old methods
        cls.filtered_public_methods = [
            method
            for method in cls.filtered_public_methods
            if method not in {"sieve", "display", "validate"}
        ]

        # Ensure all public methods are included in __all__
        cls.all_defined_names = dir(cls.init_module)
        cls.public_methods_in_all = getattr(cls.init_module, "__all__", [])

        cls.missing_imports = [
            method
            for method in cls.filtered_public_methods
            if method not in cls.filtered_imported_methods
        ]

    def test_public_methods_in_imports(self):
        """Test that all public methods are imported or aliased."""
        aliases_imports = [
            method
            for method in self.filtered_imported_methods
            if method not in self.filtered_public_methods
        ]

        diff = len(self.missing_imports) - len(aliases_imports)

        if diff != 0:
            self.fail(
                f"{diff} public method(s) missing from imports at __init__.py. You need to import the new brutils features methods inside the brutils/__init__.py file"
            )

    def test_public_methods_in_all(self):
        """Test that all public methods are included in __all__."""
        missing_in_all = set(self.filtered_imported_methods) - set(
            self.public_methods_in_all
        )

        if missing_in_all:
            self.fail(
                f"Public method(s) missing from __all__: {missing_in_all}. You need to add the new brutils features methods names to the list __all__ in the brutils/__init__.py file"
            )


if __name__ == "__main__":
    unittest.main()
