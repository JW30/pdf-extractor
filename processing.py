import textract
import re


def get_numbers(file_path):
    output = ''
    try:
        pdf_content = textract.process(file_path)
    except UnicodeDecodeError:
        pdf_content = textract.process(file_path, method="pdfminer")
    text = str(pdf_content)
    numbers_list = re.sub('\D', ' ', text).split()
    for x in numbers_list:
        if len(x) == 8 and x not in output:
            output += f'{x} '
    return output.rstrip()
