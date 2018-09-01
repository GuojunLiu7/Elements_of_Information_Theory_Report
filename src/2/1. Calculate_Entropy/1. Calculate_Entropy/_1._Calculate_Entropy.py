# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:52:41 2017

@author: Newton
"""

"""filename: Calculate.py"""

from math import log2 as log2

class getEntropy:
    """This class aims to get the related entropy of a distribution.
    
    The distribution should contain 3 or 2 inputs.
    
    if 2:
        A distribution
    if 3:
        A joint distribution
    
    +----+----+
    |    |  X |
    +----|----+
    | Y  |    |
    +----+----+
    
    """
    def __init__(self, x_value, dim = 1):
        """H(X) = sum(p * log(p))"""
        self.distribution = x_value   # x's distribution
        self.dim = dim
        if dim not in {1, 2}:
            raise ValueError("dimension wrong!")
    
    def entropy(self, which='X'):
        """Calculate the Entropy."""
        ans = 0
        
        if which == 'X':
            for i in range(len(self.distribution)):
                ans += -1 * self.distribution[i] * log2(self.distribution[i])
            return ans
        
        if which == 'Y':
            if self.dim != 2:
                raise ValueError("No Y distribution is imput!")
            row = len(self.distribution)
            column = len(self.distribution[0])

            distribution_y = list()

            for i in range(column):
                tmp = list()
                for j in range(row):
                    tmp.append(self.distribution[j][i])
            distribution_y.append(sum(tmp))

            for i in range(len(distribution_y)):
                ans += -1 * distribution_y[i] + log2(distribution_y)
            return ans
        
        if which == 'joint':
            tmp = list()    # to contain all the elements
            if self.dim != 2:
                raise ValueError("No Y distribution is imput!")
            for i in range(len(self.distribution)):
                for j in range(len(self.distribution[0])):
                    tmp.append(self.distribution[i][j])
            for i in tmp:
                if i == 0:
                    log_tmp = 0
                else:
                    log_tmp = log2(i)
                ans += -1 * i * log_tmp
            return ans
    
    def condEntropy(self, which='X|Y'):
        """Default: H(X|Y)"""
        ans = 0

        if which == "X|Y":
            y_distribution = list()
            tmp = 0
            for i in range(len(self.distribution)):
                for j in range(len(self.distribution[0])):
                    tmp += self.distribution[i]
                y_distribution.append(tmp)

            for i in range(len(self.distribution[0])):
                tmp = 0
                for j in range(len(self.distribution)):
                    tmp_cond = y_distribution[i] * self.distribution[i][j]
                    tmp += tmp_cond * log2(tmp_cond)
                tmp *= y_distribution[i]
                ans += tmp
            return ans

if __name__ == "__main__":
    tmp = [[ 1/8, 1/16, 1/32, 1/32],\
           [1/16,  1/8, 1/32, 1/32],\
           [1/16, 1/16, 1/16, 1/16],\
           [ 1/4,    0,    0,    0]]
    
    c = getEntropy(tmp, 2)
    d = c.condEntropy("H(X|Y)")
    e = c.entropy("joint")
    print("The joint entropy of this distribution is ", e, "bit.")
    print("The conditional entropy of this distribution is ", d, "bit.")