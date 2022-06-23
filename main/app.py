import streamlit as st
from streamlit_option_menu import option_menu

# Custom imports 
from pages import presentation, the_challenge, crisp_dm, implementation, evaluation, index_page
from config import TITLE_COLORS, SUBTITLE_COLORS

if __name__ == "__main__":

    st.set_page_config(page_title='I2A2Challenge', page_icon='./images/flavi.png')

    #     # Justifying text
    st.markdown("""
    <style>
    footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)


    st.sidebar.image('./images/logo.jpeg', use_column_width=True)

    menu_options = [
        'I2A2 Final Challenge', 
        'Presentation', 
        'The Challenge', 
        'Solution Strategy', 
        'Implementation and Results', 
        'Strategy Evaluation']
    
    menu_icons = ['house'] + ['play'] * (len(menu_options) -1)

    with st.sidebar:
        selected = option_menu("Contents", menu_options,
                           icons=menu_icons, 
                           menu_icon="list-task", 
                           default_index=0, #orientation="horizontal",
                           styles={
                                "container": {"padding": "0!important", "background-color": "#fafafa"},
                                "icon": {"color": f"{TITLE_COLORS}", "font-size": "14px"}, 
                                "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": f"{SUBTITLE_COLORS}"},
                                "menu-title": {"color": f"{TITLE_COLORS}"}
                            })
        
    if selected == menu_options[0]:
            index_page.app()

    elif selected == menu_options[1]:
            presentation.app()
    
    elif selected == menu_options[2]:
            the_challenge.app()
    
    elif selected == menu_options[3]:
            crisp_dm.app()
    
    elif selected == menu_options[4]:
            implementation.app()
    
    elif selected == menu_options[5]:
            evaluation.app()