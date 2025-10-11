import pyperclip
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

image = Image.open('./static/test.jpg')


@app.route('/')
def home():
    hex_colours = run_fetch(image)
    return render_template('index.html', colours=hex_colours)

@app.route('/copy-colour')
def copy_colour():
    colour = request.args.get('colour')
    pyperclip.copy(colour)
    return redirect(url_for('home'))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))



def run_fetch(image):
    image = image.resize((150, 150))
    data = np.array(image).reshape(-1, 3)

    kmeans = KMeans(n_clusters=10)
    kmeans.fit(data)

    colours = kmeans.cluster_centers_
    labels = kmeans.labels_

    frequency = {}
    for label in labels:
        frequency[label] = frequency.get(label, 0) + 1

    sorted_indices = sorted(frequency, key=frequency.get, reverse=True)

    hex_colours = [rgb_to_hex(colours[i]) for i in sorted_indices]
    return hex_colours

@app.route('/file-uploaded', methods=['POST'])
def file_upload():
    global image
    file = request.files.get('file')
    if not file:
        return "No file uploaded", 400

    try:
        file.stream.seek(0)  # Ensure the stream is at the beginning
        image = Image.open(file.stream)
        image.load()  # Fully load the image before the stream closes
        image = image.convert("RGB")
        image.save('./static/test.jpg', format='JPEG')

        return redirect(url_for('home'))
    except Exception as e:
        return f"Error opening image: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)