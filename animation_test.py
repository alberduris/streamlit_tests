import streamlit as st
import numpy as np
import time

MEAN = 0
STDEV = 20
st.title('Iepa')
progress_bar = st.progress(0.0)
status_text = st.empty()
chart = st.line_chart(MEAN + STDEV * np.random.randn(1, 3))
end = 10



for i in range(end):
    # Update progress bar.
    progress_bar.progress((i + 1) / end)

    new_rows = MEAN + STDEV * np.random.randn(1, 3)

    # Update status text.
    status_text.text(
        'The latest random numbers are: %s' % new_rows[-1, :])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(1)

status_text.text('Done!')
st.write('Goooooo!')
st.balloons()

