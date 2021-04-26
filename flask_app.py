from flask import Flask, make_response, request, render_template
from werkzeug.utils import secure_filename
import os

from processing import get_numbers

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def my_page():
    if request.method == "POST":
        f = request.files.get("file")
        filename = secure_filename(f.filename)
        file_path = os.path.join('temp_files', filename)
        f.save(file_path)
        output_data = get_numbers(file_path)
        response = make_response(output_data)
        response.headers["Content-Disposition"] = \
            f"attachment; filename={filename[:-4]}.txt"
        os.remove(file_path)

        return response

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
