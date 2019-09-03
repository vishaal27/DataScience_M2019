from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

boston=datasets.load_boston()
print(len(boston.target))