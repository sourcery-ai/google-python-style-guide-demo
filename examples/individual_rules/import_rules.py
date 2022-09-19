"""
----------------------------------------------------------------------------------
[2.2 Import Rules](https://docs.sourcery.ai/Reference/Custom-Rules/gpsg/#22-import-rules)
----------------------------------------------------------------------------------

This example file contains pieces of code that either comply with or violate the
import rules `no-wildcard-imports` and `no-relative-imports`, as well as the
rules for standardized import aliases `use-standard-name-for-aliases-*`.
"""

# no violation
import time

# violations of `no-wildcard-imports`
from time import *
from rich.table import *

# violations of `no-relative-imports`
from . import important_function
from .my_module import important_function
from ..my_module import important_function, unimportant_function

# no violation - this is an absolute member import
from my_company.my_module import important_function

# violation of both `no-wildcard-imports` and `no-relative-imports`
from .something import *

# no violations: import common libraries with their "standard" aliases
import numpy as np
import pandas as pd
import tensorflow as tf

# violations of `use-standard-name-for-aliases-*`: warning: chaos ahead!
import numpy as pd
import pandas as tf
import tensorflow as np
