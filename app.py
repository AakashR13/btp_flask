from flask import Flask, request
import random
import base64
import io
from pydub import AudioSegment

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/process_audio', methods=['POST'])
def process_audio():
    data = request.get_json()

    audio_base64 = data.get('audio')

    if audio_base64:
        audio_data = base64.b64decode(audio_base64)

        # Convert the audio data to an AudioSegment (you may need to install pydub)
        audio = AudioSegment.from_file(io.BytesIO(audio_data))

        # Generate a random integer
        random_int = random.randint(0, 100)

        # Return the random integer as a JSON response
        return {'random_int': random_int}
    else:
        return {'error': 'No audio data provided.'}, 400

if __name__ == '__main__':
    app.run(debug=True)
