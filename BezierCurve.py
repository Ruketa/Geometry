import numpy as np
from KMath import KMath 

class BezierCurve :

    def __init__(self, control_points):
        self._ControlPoints = control_points

    def Bernstein(self, n, i, t):
        return KMath.BiCoe(n, i) * np.power((1-t), (n-i)) * np.power(t, i)

    def CurvePoint(self, t):
        Gt = 0
        n = len(self._ControlPoints) - 1
        for k, point in enumerate(self._ControlPoints):
            Gt += point * self.Bernstein(n, k, t)
            
        return Gt

    def Reverse(self):
        self._ControlPoints = self._ControlPoints[::-1]

    def Tangent(self, t):
        Gt = 0
        n = len(self._ControlPoints) - 1
        for i in range(0, n):
            Gt += self.Bernstein(n-1, i, t) * (self._ControlPoints[i+1] - self._ControlPoints[i])
        return (n-1) * Gt

    def GetControlPoints(self):
        return self._ControlPoints

    def SetControlPoints(self, control_points):
        self._ControlPoints = control_points
