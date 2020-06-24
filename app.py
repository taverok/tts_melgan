from scipy.io import wavfile
from flask import Flask, request, send_file
import uuid
import os

import tts_app.fastspeech as fp
import tts_app.melgan as mg
from tts_app.vendor import load_vendors
from tts_app.tts import synthesis_long_text

save_path = '/tmp/tts'

load_vendors()
fastspeech = fp.get_model()
melgan = mg.get_model()
app = Flask(__name__)

if not os.path.exists(save_path):
	os.makedirs(save_path)


@app.route('/speak/<text>', methods=['GET'])
def speak(text: str):
	audio = synthesis_long_text(text, fastspeech, melgan)
	file_name = uuid.uuid1().hex + '.wav'

	file_name = save_path + '/' + file_name

	wavfile.write(file_name, 22050, audio)

	return send_file(file_name, attachment_filename=file_name, as_attachment=True)
