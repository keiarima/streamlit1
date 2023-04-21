import streamlit as st
import time

st.title('Streamlit First Project')
st.write('Progress bar')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('Text ont the right column')
if button:
    right_column.write('Right button was pressed')



text = st.text_input('What is your favorite number?', 1)
condition = st.sidebar.slider('What is your favorite number?', 1, 100, 50)

'Your favorite number is', text, '.'
'Your favorite number is', condition, '.'
# if st.checkbox('Show Image'):
#     img = Image.open('pooh.png')
#     st.image(img, caption='pooh', use_column_width=True)


expander = st.expander('FAQ')
expander.write('Write your answer here')
expander.write('Write your answer here')
expander.write('Write your answer here')