import gradio as gr
from create_wav import processing

gui = gr.Interface(processing,
 [
     gr.Textbox(label="Your prompt", info="digite qual tipo de som gostaria de criar?"),
     gr.Textbox(label="Como será o nome do seu arquivo?", info="escolha um nome para o seu arquivo!"),
     gr.Radio(["good", "better"], label="Modelo", info="qual modelo gostaria de utilizar nessa tarefa?")
     ],
      theme = gr.themes.Soft(),
      examples=[
        ["storm and thunder", "aiMusic", "better"],
    ],
      outputs="audio")

gui.launch(debug=True)