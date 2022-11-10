# Example: Custom Python Package with ArcGIS Pro Python Toolbox

This repository demonstrates how to set up and build a custom python package that includes and ArcGIS Pro Python Toolbox (`pyt`) so that it can be distributed and installed from a Python Wheel (`whl`) file. Notably, this repository shows how to ensure that any third-party modules the package depends on from PyPi will be included as dependencies.

## Developing your custom python package for ArcGIS Pro

If you're developing a package for use in ArcGIS Pro, then start with a custom Conda environment an install the packages you need there. See Esri's [documentation](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-conda.htm) for more information.


## Pre-Build

A Python Toolbox needs some additional metadata files to work in ArcGIS Pro. This [help documentation](https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/extending-geoprocessing-through-python-modules.htm) describes how to generate that.

This script automates some of that work:

`python make_tbx_files.py`

It runs the ArcPy `createtoolboxsupportfiles` function to generate all the files needed and ensures they are placed where they need to be placed. 

## Build

Build the package with the following command:

`python setup.py sdist bdist_wheel`

When the package is built by `setup.py` as a Python wheel and installed into an ArcGIS Pro conda environment, the toolbox appears in the system ArcToolbox.

## Install

ArcGIS Pro comes with a "Python Command Prompt" shortcut available, which runs a batch script that automatically starts a command prompt with ArcGIS Pro's active Conda environment available.

Fire that up, or activate the ArcGIS Pro Conda environment in the shell of your choosing.

Then run `pip install <path-to\pyt-with-setuptools\dist\sample_pyt_package-0.1.0-py3-none-any.whl`.

## Use

After those steps, you should see `Sample Python Toolbox` listed alongside other toolboxes in ArcGIS Pro.

Run the `Sample Tool` (it has no parameters). It will print out your Windows username as well as the name and version of several third-party dependencies included by way of the above build process.