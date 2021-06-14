import textract
import re


def get_numbers(file_path):
    output = ''
    pdf_content = textract.process(file_path, encoding="utf-8")
    text = str(pdf_content)
    numbers_list = re.sub('\D', ' ', text).split()
    for x in numbers_list:
        if len(x) == 8 and x not in output:
            output += f'{x} '
    return output.rstrip()
