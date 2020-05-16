import re
import os

def select_notes(file_list, regex = None):

    re_select = []
    if regex == None:
        print("None")
    else:
        for f in file_list:
            title_search = re.search(regex, f)
            if title_search:
                re_select.append(f)
            else:
                pass
    
    return re_select
