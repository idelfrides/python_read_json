"""
----------------------
    THE CHALLENGE
----------------------

The CHALLENGE consist in read a content from a json file('test.json' to our purpose) 
without using the 'loads()' method from json package. 
The CHALLENGE itself is only a reproduction of what the python function json.loads() does.

-------------------
     SOLUTION
-------------------

So, the technique used to solve this CHALLENG is - reading the documents character by character,
to recover the test.json file content to a python variables.
The test.json file is only an example, the most important thing here is
that the script be able to work with other files in json format,
with different data structures, so the script must be dynamic.

"""

import os

from handle_json_files import json_module as jm
from handle_json_files import Solutions as sol
import time as t


def main_test():
   """ This method is main one. It start and controle this app """

    sol_ob = sol.Solutions()
    choice = sol_ob.menu()

    if choice == 0:  # quit
        quit_info = """ 
    ---------------------------------------
        You chose to quit app. 
        The app going to be quited. 
        God bless you.  See you later!
    ---------------------------------------
    """
        print('\n\n {}'.format(quit_info))
        t.sleep(5)
        exit(0)
    elif choice == 7:
        jm.with_json_method()
        main_test()
    else:
        pass

    data_variable, data_list = sol_ob.smart_solution()

    if choice == 1: 
        root_path = os.getcwd()
        sol_ob.file_text(data_variable, root_path)
        main_test()   
    elif choice == 2:  
        sol_ob.set_type(data_variable)
        main_test()
    elif choice == 3:
        sol_ob.dict_type(data_variable)
        main_test()
    elif choice == 4:
        sol_ob.tuple_type(data_list)
        main_test()
    elif choice == 5:
        sol_ob.list_type(data_list)
        main_test()
    elif choice == 6:
        sol_ob.variable_type(data_variable)
        main_test()
    else:
        pass


if __name__ == '__main__':
    main_test()
