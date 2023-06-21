from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_blocks():
    if request.method == 'POST':
        try:
            room_width = float(request.form['room_width'])
            room_length = float(request.form['room_length'])
            block_width = float(request.form['block_width'])
            block_length = float(request.form['block_length'])

            total_area = room_width * room_length
            block_area = block_width * block_length
            num_blocks = math.ceil(total_area / block_area)

            return render_template('index.html', result=num_blocks)
        except ValueError:
            error_message = "Please enter valid numeric values."

            return render_template('index.html', error=error_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
