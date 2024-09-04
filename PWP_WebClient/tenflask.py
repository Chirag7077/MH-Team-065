from  __future__  import absolute_import
from  __future__  import divison
from  __future__  import print_function

import logging
import random
import time

from flask import Flask , jsonify , request

import numpy as numpy
import tensorflow as tf

app = Flask(__name__)

def load_graph(model_file):
	graph = tf.graph()
	graph_def = tf.GraphDef()

	with open(model_file , "rb") as f :
		graph_def.ParseFromString(f.read)
	with graph.as_default():
		tf.import_graph_def(graph_def)

	return  graph

def read_tensor_from_image_file(file_name,input_height = 299, input_width = 299, input_mean = 0 , input_std = 255 ):
	input_name = "file_reader"
	ouput_name = "normalized"
	file_reader = tf.read_file(file_name , input_name)
	if file_name.endswith(".png"):
		image_reader = tf.image.decode_png(file_reader , channels = 3, name = 'png_reader')
	elif file_name.endswith(".gif"):
		image_reader = tf.squeeze(file_reader , name = 'gif_reader')
	elif file_name.endswith(".jpg"):
		image_reader = tf.image.decode_jpg(file_reader , channels = 3 , name = 'jpg_reader')
	elif file_name.endswith(".jpeg"):
		image_reader = tf.image.decode_jpeg(file_reader , channels = 3 , name = 'jpeg_reader')
	else:
		image_reader = tf.image.decode_bmp(file_reader , name = 'bmp_reader')

	float_caster = tf.cast(image_raeder, tf.float32)
	dims_expander = tf.expand_dims(float_caster , 0)
	resized = tf.image.resize_billinear(dims_expander , [input_height,input_width])
	normalized  = tf.divide(tf.subtract(resized,[input_mean]) , [input_std])
	sess = tf.Session()
	result = sess.run(normalized)

	return result

def load_labels(label_file):
	label = []
	proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
	for l in proto_as_ascii_lines:
		label.append(l.rstrip())
	return label

@app.route('/')

def classify():
	file_name = request.args['file']

	t = read_tensor_from_image_file(file_name,input_height = input_height,input_width = input_width, input_mean = input_mean, input_std = input_std)
	with tf.Session(graph = graph) as sess:
		start = time.time()
		results = sess.run(ouput_operation.outputs[0], {input_operation.outputs[0]: t })
		end = time.time()
		results = np.squeeze(results)

		top_k = results.argsort()[-5:][::-1]
		labels = load_labels(label_file)

	print('\n Evaluation time (1-image): {:.3f}s\n'.format(end-start))

	for i in top_k:
		print(labels[i] , results[i])

	return jsonify(labels, resuts.tolist())


if __name__ == '__main__':

	model_file = "frozen_inference_graph.pb"
	label_file = "object-detection.pbtxt"
	input_width = 224
	input_height = 224
	input_mean = 128
	input_std = 128
	input_layer = "input"
	ouput_layer = "final_result"


	graph = load_graph(model_file)

	input_name = "import/" + input_layer
	ouput_name = "import/" + ouput_layer
	input_operation = graph.get_operation_by_name(input_name)
	output_operation = graph.get_operation_by_name(output_name)

	app.run(debug=True, port=8000)




