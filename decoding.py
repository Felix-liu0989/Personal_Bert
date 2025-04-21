import torch
from torch import nn
import torch.nn.functional as F
import transformers
from transformers import AutoTokenizer,AutoConfig,AutoModel,AutoModelForCausalLM
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from IPython.display import Image
# default: 100
mpl.rcParams['figure.dpi'] = 150
device = 'cuda' if torch.cuda.is_available() else 'cpu'
device

