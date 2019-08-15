
# importing modules
from handle_json_files import Formating as fda
import time as t


""" this class implements some solution way to solve 
our issue
"""


class Solutions(object):

    def __init__(self):
        pass

    """ This is the method perform
        the MENU of options
       """
    def menu(self):
        print('\n\n MENU OF SOLUTION AVAILABLE\n'
              '\n [1] -> FILE Text '
              '\n [2] -> SET data type Solution '
              '\n [3] -> DICTIONARY dats type '
              '\n [4] -> TUPLE  data type '
              '\n [5] -> LIST data type '
              '\n [6] -> VARIABLE python '
              '\n [7] -> WITH JSON method '
              '\n [0] -> Quit'
              '\n')
        yes_opt = False
        option = None
        while yes_opt == False:
            try:
                option = int(input('\n Enter an option:  '))
                if option in range(8):
                    yes_opt = True
                else:
                    print('\n You entered --> {}'.format(option))
                    print('\n WARNING: INVALID OPTION!!!\n\n')
            except Exception as error:
                print('\n You entered a CARACTER or a STRING')
                print('\n WARNING: INVALID OPTION!!!')
                print('\n PYTHON SAID: {}'.format(error))
        return option

    """ This is the method performe 
        the smart solution
    """
    def smart_solution(self):
        info = """
        ----------------------------------------
            THIS IS THE SHORT AND SMART SOLUTION
        ----------------------------------------
        """
        print('{}'.format(info))

        file = None
        content = None
        try:
            file = open('test.json', 'r')
            content = file.read()
            # f_name = file.name
            print('\n SUCCESS \n File {} was opened and read successfully.'.format(file.name))
            file.close()
        except Exception as error:
            print('\n ERROR \n Error try to open file -> {}.\n Python said: {}'.format(file.name, error))

        # crearing a object of Fromating class
        fdao = fda.Formating()
        my_var_content, list_one = fdao.formate_all(content)

        return my_var_content, list_one


    def long_solution(self):
        info = """
        ------------------------------------------
          THIS IS THE LONG SOLUTION. I CONSIDER 
          THIS ONE A NOT SMART SOLUTION. 
          IT'S DO NOT FINISHED, SO, IT WAS REMOVED.
          THEREFORE, TEST OTHER SOLUTION BECAUSE IT 
          GOING TO BE CLOSED.
        ------------------------------------------
        """
        print('{}'.format(info))

        t.sleep(15)

        return

    # TODO: code 1 - TO BE IMPLEMENTE, GET NEMA AND CONTENT

    def file_text(self, data):
        self.show_info2user('FILE')
        file_name = 'your_file.txt'
        yes_name = False
        while yes_name is False:
            try:
                file_name = input('\n Enter your file name with 5 or caracters:  ')
                if file_name.isalpha() and file_name.__len__() >= 5:
                    yes_name = True
                else:
                    print('\n You entered --> {}'.format(file_name))
                    print('\n WARNING: INVALID NAME!!!')
                    print('\n You entered a STRING under 5 CARACTERS or an number')
            except Exception as error:
                print('\n You entered a STRING under 5 CARACTERS')
                print('\n WARNING: INVALID NAME!!!')
                print('\n PYTHON SAID: {}'.format(error))

        # cerating the file to write the content
        try:
            file = open(file_name, 'w', encoding='utf8')
            # file.write(data)
            file.writelines(data)
            file.close()
            print('\n Your file -> {} \n was created and filled up successfully'.format(file_name))
        except Exception as error:
            print('\n Error by trying to open file {}\n\n PYTHON SAID: {}'.format(file_name, error))

        # print('\n\n DO NOT IMPLEMENTED Yet. \n\n')


    def set_type(self, data):
        my_set = set()
        my_set.add(data)
        self.show_info2user('SET')
        print('{} '.format(my_set))


    def dict_type(self, data):
        my_dict = {'d':'idelfrides'}
        # method __setitem__(key, value) set a value into
        # the key position informed
        my_dict.__setitem__('d', data)
        self.show_info2user('DICTIONARY')
        print('{} '.format(my_dict))


    def tuple_type(self, list_data):
        my_tuple = tuple(list_data)
        self.show_info2user('TUPLE')
        print('{} '.format(my_tuple))


    def list_type(self, data):
        self.show_info2user('LIST')
        print('{} '.format(data))


    def variable_type(self, data):
        self.show_info2user('VARIABLE')
        print('{} '.format(data))


    def explod_method(self, data):
        self.show_info2user('VARIABLE')
        print('{} '.format(data))


    def show_info2user(self, data_type):
        info_sol = """
        ----------------------------------------
             THIS IS THE SOLUTION PERFORMED 
             IN A FOLLOW PYTHON DATA TYPE 
        ----------------------------------------
        """
        print('{}'.format(info_sol))
        print('\n TYPE -->  {}'.format(data_type))
        print('\n\n')





