import streamlit as st
st.set_page_config(page_title='getstreamlit',page_icon='apple')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Downloads'))
st.image('https://th.bing.com/th?id=OIP.HxV79tFMPfBAIo0BBF-sOgHaEy&w=310&h=200&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2')
st.title('STREAMING ')
st.header('by Nikeeta Khetan')
st.text('This is a tutorial on streamlit Library')
if(mymenu=='Home'):
	st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
	st.video('https://www.youtube.com/watch?v=M-mtdN6R3bQ')
elif (mymenu=='FillForm'):
	with st.form('My Form'):
		name=st.text_input('Enter name')
		dob=st.date_input("Choose date of birth")
		marks=st.slider('Choose Marks')
		k=st.form_submit_button("submit form")
	if k:
		st.write('Name:',name,'DOB:',dob,'Marks:',marks)
elif (mymenu=='Downloads'):
	st.header("Downloads")
	st.download_button('Download Now','hello this is your download','Onlei.txt')