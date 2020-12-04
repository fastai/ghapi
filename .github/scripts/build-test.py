from fastcore.all import *
from ghapi import *

print('\n'.join(str(o) for o in os.environ.items() if o[0][0] in ('S','I')))

