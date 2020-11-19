import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import time

st.title('Antifragility')

# Add histogram data
a = 1
b = 50
x1 = np.random.beta(a=a, b=b, size=1000)

# Create distplot with custom bin_size
st.subheader('Antifragile distribution')
st.markdown('Large upside, small downside. Large favorable outcomes are possible, large unfavorable ones less so (if not impossible). The right "tail" for favorable outcomes, is larger than the left one')
fig = ff.create_distplot([x1], group_labels=['Event'], bin_size=0.01)
st.plotly_chart(fig, use_container_width=True)


# Live plots
# Bar plot
all_x = []
progress_bar = st.progress(0.0)
st.subheader('In Time Series Space')
st.markdown('**The Antifragile** system: Uncertainty benefits a lot more than it hurts.')
all_x.append(np.random.beta(a=a, b=b, size=1) - x1.mean())
bar_chart = st.bar_chart(all_x)

# Cummulative plot
st.subheader('Cummulative view')
line_chart = st.line_chart(all_x)



steps = 100
for i in range(steps):

	# Update progress bar.
	progress_bar.progress((i + 1) / steps)

	# Add bar data
	all_x.append(np.random.beta(a=a, b=b, size=1) - x1.mean())

	bar_chart.add_rows(all_x[-1])
	line_chart.add_rows([np.array(all_x).sum()])

	# Pretend we're doing some computation that takes time.
	time.sleep(0.1)

st.write('Congratulations, you are now in a **Fuck you, money!** position :)')
st.balloons()







