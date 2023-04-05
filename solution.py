import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 348708372 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    scale = (x.max() - 0.095) / np.sqrt(3)
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
