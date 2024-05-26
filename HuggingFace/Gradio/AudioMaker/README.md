# Descrição do projeto
O objetivo do projeto é, via Gradio e com a utilização do modelo AudioLDM que está hospedado na plataforma Huggingface, criar uma interface na qual seja possível gerar arquivos de áudio .wav via prompt como ser possível a download do arquivo.

![](https://github.com/CllsPy/Generative_AI/blob/main/HuggingFace/Gradio/AudioMaker/assets/gui.png?raw=true)

## Etapas
1. Em primeiro lugar precisamos criar um processo que gera o conteúdo
2. Converter o conteúdo gerado para algo conhecido, nesse caso .wav
3. Criar a interface que recebe o prompt e o novo do arquivo

## Requeriments
O processo foi inteiramente no Google Colabs e em seguida tranferido ao HuggingFace Spaces para deployment. A linguagem utilizada foi Python.

### Pacotes

```python
torch
Transformers
diffusers
gradio
scipy
```

## Autor
[Deployment on HuggingFace](https://huggingface.co/spaces/CASLL/audio-maker)
[Cllspy - Github](https://github.com/CllsPy)
