import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 348708372 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    max_x = x.max()
    n = len(x)
    delta = (max_x - 0.095) / np.sqrt(n + 1) * (1 / alpha) ** (1 / (n + 1))

    left_bound = max_x - delta
    right_bound = np.inf

    return left_bound, right_bound
