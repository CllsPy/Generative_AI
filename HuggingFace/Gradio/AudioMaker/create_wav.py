import scipy
import torch
from diffusers import AudioLDMPipeline

repo_id = "cvssp/audioldm-s-full-v2"
pipe = AudioLDMPipeline.from_pretrained(repo_id, torch_dtype=torch.float16)
pipe = pipe.to("cpu")

def create(prompt:str, name_file: str):
  prompt = prompt
  audio = pipe(prompt, num_inference_steps=10, audio_length_in_s=5.0).audios[0]

  # save the audio sample as a .wav file
  scipy.io.wavfile.write(f'{name_file}.wav', rate=16000, data=audio)

  # Assuming your file is named 'audio_file.mp3'
  audio_file = f'{name_file}.wav'

  # Play the audio file
  return audio_file