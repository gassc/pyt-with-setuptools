# -*- coding: utf-8 -*-
r""""""
__all__ = ['SampleTool']
__alias__ = 'SamplePythonToolbox'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Tools
@gptooldoc('SampleTool_SamplePythonToolbox', None)
def SampleTool():
    """SampleTool_SamplePythonToolbox()"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SampleTool_SamplePythonToolbox(*gp_fixargs((), True)))
        return retval
    except Exception as e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject