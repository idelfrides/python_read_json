"""Docstrings."""

# TODO: describe the problem gonna be solved in this project here
# importing modules
import os

from handle_json_files import json_module as jm
from handle_json_files import Solutions as sol
import time as t


""" 
 This method is main one. It start and 
 controle this app
"""


def main_test():

    # metodo clear aqui
    """ crearing a object of modules:
     -> Solutions as sol
    """

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

    data_var, data_list = sol_ob.smart_solution()

    if choice == 1:   # short solution
        root_path = os.getcwd()

        sol_ob.file_text(data_var, root_path)
        main_test()    # call the main method again to run the app
    elif choice == 2:  # long solution
        sol_ob.set_type(data_var)
        main_test()
    elif choice == 3:
        sol_ob.dict_type(data_var)
        main_test()
    elif choice == 4:
        sol_ob.tuple_type(data_list)
        main_test()
    elif choice == 5:
        sol_ob.list_type(data_list)
        main_test()
    elif choice == 6:
        sol_ob.variable_type(data_var)
        main_test()
    else:
        pass


if __name__ == '__main__':
    main_test()
