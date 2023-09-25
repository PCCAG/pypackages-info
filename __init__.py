import os
import datetime
import pkg_resources

# A simple tool.
# Can output the name, version, last modified time, and location of the installed module in the current environment in a tabular form at the terminal.
# +----------------------------+--------------+---------------------+----------------------------------------------------------------------+
# | Module: 426 total          | Version      | Last Modified       | Location                                                             |
# +----------------------------+--------------+---------------------+----------------------------------------------------------------------+
# | pyzmq                      | 24.0.1       | 2022-12-06 22:24:51 | c:\users\s\appdata\roaming\python\python310\site-packages            |
# | ipython                    | 8.7.0        | 2022-12-06 22:24:51 | c:\users\s\appdata\roaming\python\python310\site-packages            |
# | jupyter-client             | 7.4.8        | 2022-12-06 22:24:51 | c:\users\s\appdata\roaming\python\python310\site-packages            |
# | ipykernel                  | 6.17.1       | 2022-12-06 22:24:51 | c:\users\s\appdata\roaming\python\python310\site-packages            |
# | tornado                    | 6.2          | 2022-12-06 22:24:51 | c:\users\s\appdata\roaming\python\python310\site-packages            |
# | psutil                     | 5.9.4        | 2022-12-06 22:24:51 | c:\users\s\appdata\roaming\python\python310\site-packages            |
# | traitlets                  | 5.6.0        | 2022-12-06 22:24:51 | c:\users\s\appdata\roaming\python\python310\site-packages            |

installed_packages = list(pkg_resources.working_set)
package_info = []
for package in installed_packages:
    package_name = package.project_name
    package_version = package.version
    package_location = package.location

    timestamp = datetime.datetime.fromtimestamp(
        os.path.getctime(package_location)
    ).strftime("%Y-%m-%d %H:%M:%S")

    package_info.append((package_name, package_version, timestamp, package_location))

sorted_packages = sorted(
    package_info,
    key=lambda x: datetime.datetime.strptime(x[2], "%Y-%m-%d %H:%M:%S"),
    reverse=True,
)


# a function for outputing Two-dimensional list in a tabular form at the terminal
def print_table(data):
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

    # Print the table header border
    for width in column_widths:
        print(f"+{'-' * (width + 2)}", end="")
    print("+")

    # Print head
    for item, width in zip(data[0], column_widths):
        print(f"| {item:{width}} ", end="")
    print("|")

    # Print form border
    for width in column_widths:
        print(f"+{'-' * (width + 2)}", end="")
    print("+")

    # Print row
    for row in data[1:]:
        for item, width in zip(row, column_widths):
            print(f"| {item:{width}} ", end="")
        print("|")

    # Print table bottom border
    for width in column_widths:
        print(f"+{'-' * (width + 2)}", end="")
    print("+")


# data
data = [
    [f"Module: {len(sorted_packages)} total", "Version", "Last Modified", "Location"]
] + sorted_packages

# Call the function to print a table with borders
print_table(data)
