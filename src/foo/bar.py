import os
# ArcPy
import arcpy
# 3rd party modules
import petl
import tqdm
import codetiming
import pint
import marshmallow
# other modules
from baz import run as run_baz


def hello(override_user=None):
    
    s = f'Hello {os.getenv("username")}'
    if override_user:
        s = f'Hello {override_user}'
    
    s += "\nAdditional Modules:"
    for m in [petl, tqdm, codetiming, pint, marshmallow, arcpy]:
        s += f"\n {m.__name__} | {m.__version__}"
    
    s += "\n" + run_baz()

    return s
