import streamlit as st
from streamlit_tags import st_tags , st_tags_sidebar
import random

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")
 
#st.text('This is some text by rudra.')

player_names = st_tags_sidebar(
    label='# Enter Player Names',
    text='Press enter to add more',
    value=[],
    suggestions=[],
    key='1') 

st.title(f"WELCOME TO DIVYANSH'S BDAY CELEBRATION")
st.write(f"Please add player names using the sidebar")
print("\n")
if st.button('S H O W'):
    if( len(set(player_names)) <=2):
        st.write(f"Add more players")    
    else:
        player_a = random.choice(player_names)
        player_b = random.choice(player_names)
        player_c = random.choice(player_names)
        while(player_a ==player_b or player_c == player_b or player_a ==player_c):
            player_a = random.choice(player_names)
            player_b = random.choice(player_names)
        #st.write(f"{player_a} will ask {player_b}") 
        t1=f"<span class='highlight blue'> {player_a}</span>" f" &ensp; WILL ASK &ensp; <span class='highlight green'>{player_b}</span>" f"&ensp; AFTER CONSULTING &ensp;<span class='highlight red'>  {player_c}</span>"
        st.markdown(t1, unsafe_allow_html=True)
        
   

