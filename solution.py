import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 348708372 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    func = lambda x: x - 0.095
    x = func(x)
    size = x.size
    max_v = x.max()

    return 0.095 + max_v / ((1 - alpha / 2) ** (1. / size)), 0.095 + max_v / ((alpha / 2) ** (1. / size))
