import textract
import re


def get_numbers(file_path):
    output = ''
    pdf_string = str(textract.process(file_path))
    numbers_list = re.sub('\D', ' ', pdf_string).split()
    for x in numbers_list:
        if len(x) == 8 and x not in output:
            output += f'{x} '
    return output.rstrip()
