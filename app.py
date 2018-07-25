from flask import Flask, jsonify, render_template
import pandas as pd
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/accuracy_plot", methods=['GET'])
def accuracy_plot():
    data_all = pd.read_csv('data/models_analysis.csv')
    data = [{
        "x": data_all.train_test_split.tolist(),
        "y": data_all.accuracy.tolist(),
        "color": ['rgb(209, 82, 39)' if acc < 94.0 else 'rgb(234, 180, 42)' if acc >= 94.0 and acc < 97.0 else 'rgb(56, 193, 99)' for acc in data_all.accuracy.tolist()],
        "names": ['Accuracy < 94.0', 'Accuracy between 94.0 and 97.0', 'Accuracy > 97.0']
    }]

    return jsonify(data)

@app.route("/duration_plot", methods=['GET'])
def duration_plot():
    data_all = pd.read_csv('data/models_analysis.csv')
    data = [{
        "x": data_all.train_test_split.tolist(),
        "y": data_all.duration.tolist(),
        "color": ['rgb(56, 193, 99)' if dur < 20.0 else 'rgb(234, 180, 42)' if dur >= 20.0 and dur < 100.0 else 'rgb(209, 82, 39)' for dur in data_all.duration.tolist()]}]

    return jsonify(data)

@app.route("/duration_vs_accuracy_plot", methods=['GET'])
def duration_vs_accuracy_plot():
    data_all = pd.read_csv('data/models_analysis.csv')
    data = [{
        "x": data_all.accuracy.tolist(),
        "y": data_all.duration.tolist(),
        "text": [i for i in data_all.train_test_split.tolist()],
        "size": [i*10 for i in data_all.complexity.tolist()],
        "color": ['rgb(56, 193, 99)' if dur < 20.0 else 'rgb(234, 180, 42)' if dur >= 20.0 and dur < 100.0 else 'rgb(209, 82, 39)' for dur in data_all.duration.tolist()]
}]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)