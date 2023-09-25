import importlib.resources
import importlib.metadata


def test():
    installed_packages = []

    # Get a list of installed package distributions
    distributions = list(importlib.metadata.distributions())

    for distribution in distributions:
        package_name = distribution.metadata["Name"]
        package_version = distribution.version

        # Use importlib.resources to get the location of the package
        with importlib.resources.path(package_name, "__init__.py") as package_location:
            installed_packages.append((package_name, package_version, package_location))

    for package_name, package_version, package_location in installed_packages:
        print(f"Package Name: {package_name}")
        print(f"Package Version: {package_version}")
        print(f"Package Location: {package_location}")
        print("-" * 40)


test()
