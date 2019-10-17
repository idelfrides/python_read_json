
""" class contain methods to help solving  this issue """

import os


class Formating(object):
    """ Formatin data class """

    def __init__(self):
        """  thunder init do nothing """
        pass


    def formate_all(self, content):
        """ This method formate all content to an pyhon variable.
        It's only used in the smart solution """
        
        key_help = ''
        list_help = []
        list_help_one = []
        try:
            for c in content:  # c = caracter
                key_help = key_help + c
                list_help.append(c)

            list_help_one.append(key_help)
            return key_help, list_help_one

        except Exception as error:
            print('\n Error. Python said: {}'.format(error))


    def change_dir(self, code, root_path):
        if code == 1:   # go to handle_json_files
            path_dir = os.path.dirname(os.path.abspath(__file__))
            os.chdir(path_dir)
        elif code == 2:  # to files_dir  folder
            os.chdir('files_dir')
        elif code == 0: # to root project dir
            os.chdir(root_path)
            print(os.chdir(root_path))
        else:
            pass
