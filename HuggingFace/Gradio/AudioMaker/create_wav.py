import scipy
import torch
from diffusers import AudioLDMPipeline
from diffusers import AudioLDM2Pipeline

def processing(prompt:str, name_file: str, model:str):

    if model == "good":
      repo_id = "cvssp/audioldm-s-full-v2"
      pipe = AudioLDMPipeline.from_pretrained(repo_id, torch_dtype=torch.float16)
      pipe = pipe.to("cuda")

      prompt = prompt
      audio = pipe(prompt, num_inference_steps=100, audio_length_in_s=5).audios[0]

      scipy.io.wavfile.write(f'{name_file}.wav', rate=16000, data=audio)

    elif model == "better":
      repo_id = "cvssp/audioldm2"
      pipe = AudioLDM2Pipeline.from_pretrained(repo_id, torch_dtype=torch.float16)
      pipe = pipe.to("cuda")

      prompt = prompt
      negative_prompt = "Low quality."

      generator = torch.Generator("cuda").manual_seed(0)

      audio = pipe(
          prompt,
          negative_prompt=negative_prompt,
          num_inference_steps=200,
          audio_length_in_s=10.0,
          num_waveforms_per_prompt=3,
          generator=generator
          ).audios

      scipy.io.wavfile.write(f'{name_file}.wav', rate=16000, data=audio[0])

    audio_file = f'{name_file}.wav'
    return audio_file