import streamlit as st

from config import TITLE_COLORS, SUBTITLE_COLORS

def app():
    st.markdown(f"# <span style='color:{TITLE_COLORS}'>I2A2 Final Challenge</span>", unsafe_allow_html=True)
    st.write("This presentation was made for the I2A2 training's final challenge. It was delivered on Sunday the 12th of June, 2022.")

    st.write("The training was sponsored by **PTI**, **T2I Group**, and **DATA H**.")

    st.write("More details in the 'Presentation' section.")

    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>Acknowledgements</span>", unsafe_allow_html=True)

    st.write("I would like to thanks I2A2 and the sponsors, **T2I Group**, **DATA H**, **PTI**, for the amazing course and attention during the last months.")

    st.write("I also would like to thanks professor Celso Azevedo for the amazing lectures and talks.")

    st.write("I couldn't forget to thank colleague Onédio Seabra for the help he gave to all of us during this time together.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    st.image("images/patronos.png")


    st.write()