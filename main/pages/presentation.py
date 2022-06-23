import streamlit as st

from config import TITLE_COLORS, SUBTITLE_COLORS

def app():
    st.markdown(f"# <span style='color:{TITLE_COLORS}'>Presentation</span>", unsafe_allow_html=True)

    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>About Me</span>", unsafe_allow_html=True)

    st.image("images/me.png", width = 100)

    
    st.markdown("Hi!! :smiley:")

    st.markdown(f"I'm <span style='color:{SUBTITLE_COLORS}'>**Kattson Bastos**</span>, Data Scientist for more than 1 year, currently working at Kogui, and taking a Bachelor's Degree in Economics and in Software Engineering.", unsafe_allow_html=True)
    st.markdown(f"Please, feel free to contact or to connect with me on any social media bellow: ", unsafe_allow_html=True)
    ## badges
    my_linkedin = "[![Linkedin Badge](https://img.shields.io/badge/-KattsonBastos-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/kattson-bastos)](https://www.linkedin.com/in/kattson-bastos)"

    my_medium = "[![my_medium](https://badgen.net/badge/icon/kattsonbastos?icon=medium&label)](https://medium.com/@kattsonbastos)"

    my_gmail = "[![Gmail Badge](https://img.shields.io/badge/-kattsonbastos@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:kattsonbastos@gmail.com)](mailto:kattsonbastos@gmail.com)"

    my_twitter = "[![Twitter Badge](https://badgen.net/badge/icon/KattsonB?icon=twitter&label)](https://twitter.com/KattsonB)"

    my_github = "[![Github Badge](https://badgen.net/badge/icon/kattsonbastos?icon=github&label)](https://github.com/KattsonBastos)"
    my_discord = "[![my_discord](https://badgen.net/badge/icon/kattsonbastos?icon=discord&label)](https://discord.com/users/284341555265929226)"

    st.markdown(f"{my_linkedin} {my_github} {my_medium} {my_gmail} {my_twitter} {my_discord}")

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    ## i2a2
    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>About I2A2</span>", unsafe_allow_html=True)
    st.image("images/i2a2.png", width=200)

    st.markdown(f"Founded in 2017, <span style='color:{SUBTITLE_COLORS}'>**I2A2 - Institute of Artificial Intelligence**</span> helps professionals by training and updating their skills \
        in Atificial Intelligence. They offer free semiannual trainings on *IoT, Machine Learning, Robotics, and Big Data*.", unsafe_allow_html=True)

    st.markdown(f"For more about <span style='color:{SUBTITLE_COLORS}'>**I2A2**</span> and the course's sponsors, please take a look at the links bellow:", unsafe_allow_html=True)

    i2a2_linkedin = "[![Linkedin Badge](https://img.shields.io/badge/-I2A2-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/company/institut-i2a2/)](https://www.linkedin.com/company/institut-i2a2/)"
    i2a2_site = "[<a href='https://www.i2a2.academy/'><img src='https://img.shields.io/badge/I2A2 Academy-red?logo=LOGO'></a>]('https://www.i2a2.academy/')"
    datah_site = "[<a href='https://www.datah.ai/'><img src='https://img.shields.io/badge/Data H-4c84a3?logo=LOGO'></a>]('https://www.datah.ai/')"
    t2i_site = "[<a href='https://www.t2igroup.com/'><img src='https://img.shields.io/badge/T2I Group-323A49?logo=LOGO'></a>]('https://www.t2igroup.com/')"

    st.markdown(f"{i2a2_linkedin} &nbsp;&nbsp; {i2a2_site} &nbsp;&nbsp;  {datah_site} &nbsp;&nbsp; {t2i_site}", unsafe_allow_html=True)


