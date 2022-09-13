import cv2
import numpy as np
import torch
import yaml
from torch.utils import data
from tqdm import tqdm

sd = tqdm

b = np.randn(3, 4)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

f = yaml

dataset = data.Dataset

cap = cv2.VideoCapture(0)
