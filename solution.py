import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 348708372 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    a = 0.095
    alpha = 1 - p  
    n = len(x)  
    b = np.max(x)
    
    return a, b + (1 - np.sqrt(1 - alpha)) * (1 - b)
