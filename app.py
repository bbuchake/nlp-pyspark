from flask import Flask, jsonify, render_template
import pandas as pd
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/accuracy_plot")
def accuracy_plot():
    data_all = pd.read_csv('data/models_analysis.csv')
    data = [{
        "x": data_all.train_test_split.tolist(),
        "y": data_all.accuracy.tolist(),
        "color": ['lightgreen' if acc < 94.0 else 'lightblue' if acc >= 94.0 and acc < 97.0 else 'lightpink' for acc in data_all.accuracy.tolist()]
    }]

    return jsonify(data)

@app.route("/duration_plot")
def duration_plot():
    data_all = pd.read_csv('data/models_analysis.csv')
    data = [{
        "x": data_all.train_test_split.tolist(),
        "y": data_all.duration.tolist(),
        "color": ['green' if dur < 20.0 else 'blue' if dur >= 20.0 and dur < 100.0 else 'red' for dur in data_all.duration.tolist()]}]

    return jsonify(data)

@app.route("/duration_vs_accuracy_plot")
def duration_vs_accuracy_plot():
    data_all = pd.read_csv('data/models_analysis.csv')
    data = [{
        "x": data_all.accuracy.tolist(),
        "y": data_all.duration.tolist(),
        "text": [i for i in data_all.train_test_split.tolist()],
        "size": [int(i/10) for i in data_all.duration.tolist()],
        "color": ['green' if dur < 20.0 else 'blue' if dur >= 20.0 and dur < 100.0 else 'red' for dur in data_all.duration.tolist()]
}]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)