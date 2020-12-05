SUCCESS_MSG = 'You have been aided!'


def add_line_number(filename, num_spaces=2):
    """
    Adds line numbers to the file content and creates the new file.
    Useful for code-based files.
    """
    spaces = num_spaces * ' '
    with open(filename) as file:
        file_content = file.readlines()
    
    new_content = [f'{i + 1}{spaces}{file_content[i]}' for i in range(len(file_content))]
    
    with open('aided_' + filename, 'w') as new_file:
        new_file.writelines(new_content)
    
    print(SUCCESS_MSG)
    

COLOR = {
    "PURPLE": "\033[95m",
    "ORANGE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
}


def color(text, ctype):
    """
    Colors a given text with a specified color.
    """
    if ctype.upper() not in COLOR.keys():
        raise AttributeError(f'{ctype} is not found in COLOR: {tuple(COLOR.keys())}')

    END = "\033[0m"

    return f'{COLOR[ctype.upper()]} {text} {END}'


def convert_to_fasta(filename, max_char=70):
    """
    Converts a single line of text into fasta format (paragraphed).
    """
    with open(filename) as file:
        text = file.readlines

    paragraphed_text = [text[i : i + max_char] for i in range(0, len(text), max_char)]
    to_write = list(map(lambda s: s + '\n', paragraphed_text))

    with open('converted.fasta', 'w') as file:
        file.write('>textaided\n')
        file.writelines(to_write)
    
    print(SUCCESS_MSG)
