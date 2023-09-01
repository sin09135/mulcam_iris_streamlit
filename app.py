# -*- coding:utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scikit-learn as sklearn
import plotly.graph_objs as go


def main():

    st.markdown("# Helloworld")
    st.write(np.__version__)
    st.write(pd.__version__)
    st.write(plt.__version__)
    st.write(sklearn.__version__)
    st.write(go.__version__)

if __name__ == "__main__":
    main()
  