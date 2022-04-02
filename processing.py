import textract
import re
from datetime import datetime


def get_numbers(file_path):
    # Get PDF content and filter for 8 digit numbers
    output, out_string = [], ''
    try:
        pdf_content = textract.process(file_path)
    except UnicodeDecodeError:
        pdf_content = textract.process(file_path, method='pdfminer')
    text = str(pdf_content)
    numbers_list = re.sub('\D', ' ', text).split()
    for x in numbers_list:
        if len(x) == 8 and x not in output:
            output.append(x)
    numbs_amnt = len(output)
    # Formatting of output string
    out_string += f'{numbs_amnt} product numbers found:\\n'
    for i, x in enumerate(output):
        if (i+1) % 10 == 0:
            out_string += f'{x}\\n'
        else:
            out_string += f'{x} '
    out_string.rstrip()

    # Save datetime, PDF-name and amount of numbers extracted to record.txt
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("record.txt", "a") as f:
        f.write(f'Last time used: {dt_string}\n'
                f'PDF file: {file_path.split("/", 1)[1]}\n'
                f'Numbers extracted: {numbs_amnt}\n\n')
    return out_string
