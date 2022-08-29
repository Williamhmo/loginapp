import streamlit as st
from pickle import dump
from pickle import load
import webbrowser
   

def main():
    try:
        file=open('account.obj','rb')
        data=load(file)
        file.close()
    except:
        data={}
    st.title('Simple Login App')
    menu=['Home','Signup','Login']
    choice=st.sidebar.selectbox('Menu',menu)
    
    if choice == 'Home':
        st.subheader('Welcome to the app!')
        
    elif choice== 'Signup':
        st.subheader('Create a new account')
        new_username=st.text_input('Username')
        new_password=st.text_input('Password',type='password')
        if st.button('Enter'):
            st.success('You signed up as {}'.format(new_username))
            st.write('Please go to login section to continue!')
            data[new_username]=new_password
            file=open('account.obj','wb')
            dump(data,file)
            file.close()
            
    elif choice== 'Login':
        st.subheader('Login Section')
        username=st.text_input('Username')
        password=st.text_input('Password',type='password')
        if st.button('Login'):
            if username in data.keys() and password==data[username]:
                st.success('Logged in successful as {}'.format(username))
                st.write(data)
                url='https://www.youtube.com/'
                webbrowser.open_new_tab(url)
            else:
                st.write('Incorrect password or you need to signup first')    

if __name__ =='__main__':
    main()