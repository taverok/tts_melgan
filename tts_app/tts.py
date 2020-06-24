import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow_tts.processor.ljspeech import LJSpeechProcessor
from tensorflow_tts.processor.ljspeech import symbols

processor = LJSpeechProcessor(None, "english_cleaners")

def synthesis_long_text(input_text, text2mel_model, vocoder_model) -> np.ndarray:
	cuts = []

	for sentence in input_text.split("."):
		if len(sentence.strip()) == 0:
			continue
		_, audio = synthesis(sentence, text2mel_model, vocoder_model)
		cuts.append(audio)

	return np.concatenate(cuts)


def synthesis(input_text, text2mel_model, vocoder_model):
	input_ids = processor.text_to_sequence(input_text)
	input_ids = np.concatenate([input_ids, [len(symbols) - 1]], -1)

	# text2mel part
	mel_before, mel_outputs, duration_outputs = text2mel_model.inference(
		input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
		attention_mask=tf.math.not_equal(tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0), 0),
		speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
		speed_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
	)

	# vocoder part
	audio = vocoder_model(mel_outputs)[0, :, 0]
	return mel_outputs.numpy(), audio.numpy()


def visualize_attention(alignment_history):
	import matplotlib.pyplot as plt

	fig = plt.figure(figsize=(8, 6))
	ax = fig.add_subplot(111)
	ax.set_title(f'Alignment steps')
	im = ax.imshow(
		alignment_history,
		aspect='auto',
		origin='lower',
		interpolation='none')
	fig.colorbar(im, ax=ax)
	xlabel = 'Decoder timestep'
	plt.xlabel(xlabel)
	plt.ylabel('Encoder timestep')
	plt.tight_layout()
	plt.show()
	plt.close()


def visualize_mel_spectrogram(mels):
	mels = tf.reshape(mels, [-1, 80]).numpy()
	fig = plt.figure(figsize=(10, 8))
	ax1 = fig.add_subplot(311)
	ax1.set_title(f'Predicted Mel-after-Spectrogram')
	im = ax1.imshow(np.rot90(mels), aspect='auto', interpolation='none')
	fig.colorbar(mappable=im, shrink=0.65, orientation='horizontal', ax=ax1)
	plt.show()
	plt.close()