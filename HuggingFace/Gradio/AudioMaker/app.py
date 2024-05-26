import gradio as gr
from create_wav import create

gui = gr.Interface(
    fn=create,
    inputs=["textbox", "textbox"],
    outputs="audio"
    )

gui.launch(debug=True)