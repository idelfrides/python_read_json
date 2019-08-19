
# class contain methods to help solving
# this issue
import os


class Formating(object):

    # thunder init do nothing
    def __init__(self):
        pass

    # this method formate all content to an
    # pyhon variable. used on the smart solution
    def formate_all(self, content):
        key_help = ''
        list_help = []
        list_help_one = []
        try:
            for c in content:  # c = caracter
                # count = count + 1
                key_help = key_help + c
                list_help.append(c)

            list_help_one.append(key_help)
            return key_help, list_help_one

        except Exception as error:
            print('\n Error. Python said: {}'.format(error))

    # this method formate all keys to a list
    # used on the long solution
    def format_multi_key(self, key, content, st, list_help):
        key_help = ''
        # list_help = []
        count = st
        try:
            for c in content[st:]:  # c = caracter
                count = count + 1
                key_help = key_help + c
                key_help_len = key_help.__len__()
                key_len = key.__len__()
                if key_help_len == key_len:
                    # remove left white space
                    key_help = key_help.lstrip()
                    if key_help == key:
                        list_help.append(key_help)
                        break
                    else:
                        continue
                else:
                    pass
            return list_help, count
        except Exception as error:
            print('\n Error. Python said: {}'.format(error))

    # this method formate all values to the same list
    # used on the long solution
    def format_values_all(self, value, content, st, list_help):
        key_help = ''
        # list_help = []
        count = st
        try:
            for caracter in content[st:]:
                count = count + 1
                key_help = key_help + caracter

                key_help_len = key_help.__len__()
                key_len = value.__len__()

                if key_help_len == key_len:
                    # remove left white space
                    key_help = key_help.lstrip()

                    if key_help == value:
                        list_help.append(key_help)
                        break
                    else:
                        continue
                else:
                    pass
            return list_help, count

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
