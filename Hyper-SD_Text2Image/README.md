## Project Description¶
The goal of this project is to build an AI with text-to-image generative capabilities (text -> image). The aim is to be able to produce an image representing the character of a fiction book we are writing.

### Steps
Install necessary dependencies.
Load the model.
Perform prompt.

## Requirements
Python: Python is an interpreted, high-level, general-purpose programming language.

Integrated Development Environment (IDE): Any integrated development environment that can be used to view, edit, and run Python code, such as:

Google Colab
Jupyter Notebook
Kaggle

### Packages
Please install the following packages in Python before running the code.

´´´Python
%time
!pip install -qq diffusers; # <- Type of generative model
!pip install -qq -U peft; # <- Helps improve the performance of pre-trained models

import torch # <- Fundamental library for neural networks
import transformers

from diffusers import DiffusionPipeline  # Facilitates the import of diffusion models from huggingface.co
from diffusers import DDIMScheduler  # Speeds up the process, making the result faster

from huggingface_hub import hf_hub_download  # Allows interaction with the Hugging Face Hub, repository of models
transformers.utils.move_cache()
´´´
