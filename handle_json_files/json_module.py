"""
 This medule solve the issue using json module
"""

# import modules
import json

def with_json_method():
    # mycontent = None
    try:
        myfile = open('test.json', 'r')
        mycontent = myfile.read()
        file_name = myfile.name
        myfile.close()
        print('\n SUCCESS \n File {} was opened and read successfully.'.format(file_name))
    except Exception as error:
        print('\n ERROR \n Error try to open a file.\n Python said: {}'.format(error))


    show_info2user()
    # print(type(mycontent))
    # print(mycontent)

    """ 
        json.load(fp) - fp must be a text file or
        binary file containing a json document
        -------------------------        
        json.loads(s) - s must be a str, bytes or
        bytearray instance containing a json document.
        return a python dictionary 
    """
    new_content = json.loads(mycontent)
    print('\n TYPE --> {}'.format(type(new_content)))
    print('\n\n')

    print('{}'.format(new_content))

    return


def show_info2user():
    info_sol = """
    ----------------------------------------
        THIS IS THE SOLUTION PERFORMED 
        USING JSON METHOD - loads() 
    ----------------------------------------
    """
    print('{}'.format(info_sol))
    print('\n\n')
