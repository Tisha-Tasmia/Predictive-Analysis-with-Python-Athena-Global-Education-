//(Flask Application)//

from flask import Flask, render_template, request
import statistics

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numbers = request.form['numbers']
        try:
            numbers_list = [float(num) for num in numbers.split(',')]
            sum_ = sum(numbers_list)
            average = statistics.mean(numbers_list)
            std_dev = statistics.stdev(numbers_list)
            return render_template('result.html', sum=sum_, average=average, std_dev=std_dev)
        except ValueError:
            error_message = "Invalid input. Please enter a comma-separated list of numbers."
            return render_template('index.html', error_message=error_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
