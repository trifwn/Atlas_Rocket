import os
import sys
import random
import numpy as np
import pandas as pd
import time

import pyqtgraph.examples
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import plotly.graph_objs as go

from collections import deque

from utils.dataloading import SensorsDataset
from config import BASE_PATH, DATA_PATH