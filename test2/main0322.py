import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 入門')

st.write('Display Image')

Image.open('sample.jpg')
st.image(img, caption='Kohei Imanishi')

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )

# st.map(df)
