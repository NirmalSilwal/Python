import mymodule

mymodule.user_func()
print('i am in myprogram.py file and just called module in myprogram.py')

# ===================OR============================

from mymodule import user_func
user_func()


# ===================OR============================

import myprogram as mm
print('using alias')
mm.user_func()

# ===================OR============================

from mymodule import *
print('importing all modules using *, this is very inefficient one')
user_func()