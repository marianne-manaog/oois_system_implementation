# This Python file contains utility-type of functions leveraged by the file app.py and used by other Python files.

def print_name_strings_from_list(list_of_dicts, prefix_str):
    # type: (List[Dict], str) -> None
    """
    This function prints a list of names (as strings) from a list of dictionaries.

    Args:
        list_of_dicts: List[Dict]
                    a list of dictionaries, wherein each dictionary has a key called 'name'.
        prefix_str: str
                    a text (string) to be used as a prefix of the name to be printed.
    """

    iter_index = 0
    for dicto in list_of_dicts:
        iter_index += 1
        dicto_string = prefix_str.format(iter_index)
        print '{}'.format(dicto.get(dicto_string).name)
