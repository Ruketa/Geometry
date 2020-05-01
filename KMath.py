import numpy as np
import math

class KMath:
    @staticmethod
    def BiCoe(n, k):
        if n < k :
            return -1
        return math.factorial(n) / (math.factorial(k) * math.factorial((n - k)))
    
    @staticmethod
    def Normalization(vec):
        norm = np.linalg.norm(vec)
        return vec / norm

