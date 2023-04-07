import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 348708372 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    s = x.std(ddof = 1)
    return x.mean() + s * norm.ppf(alpha / 2) / np.sqrt(len(x)), \
           x.mean() + s * norm.ppf(1 - alpha / 2) / np.sqrt(len(x))
