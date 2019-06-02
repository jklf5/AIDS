# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:35:27 2019

@author: Fire
"""

from __future__ import absolute_import, division, print_function, unicode_literals
!pip install -q tensorflow==2.0.0-alpha0
import tensorflow as tf

# 我们将生成注意力分布图，以查看我们的模型
# 在生成字幕期间重点关注哪些图像区域
import matplotlib.pyplot as plt

# Scikit-learn 包含许多有用的实用工具
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

import re
import numpy as np
import os
import time
import json
from glob import glob
from PIL import Image
import pickle