from PIL import Image
from numpy import asarray

import gradio as gr

def transform_image(file):
	'''
	Essa função recebe a imagem 
	e retorna uma array

	Arg:
	file(png/jpg): arquivo a ser transformado

	Return:
	numpy.array: retorna uma array que representa a iamgem
	'''
	numpydata = asarray(file)
	return numpydata

# Criando interface com gradio
demo = gr.Interface(transform_image, 
					inputs="image", 
					outputs="textbox",
					theme=gr.themes.Base())
				
demo.launch()