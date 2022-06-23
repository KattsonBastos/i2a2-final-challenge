import streamlit as st

from config import TITLE_COLORS, SUBTITLE_COLORS

def app():
    st.markdown(f"# <span style='color:{TITLE_COLORS}'>Solution Strategy</span>", unsafe_allow_html=True)
    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>CRISP-DM</span>", unsafe_allow_html=True)


    st.write("For this implementation, we'll follow the CRISP-DM Methodology.")
    st.write("CRISP-DM stands for **CR**oss **I**ndustry **S**tandard **P**rocess for **D**ata **M**ining. \
        This is one of the most used techniques for Data Science Projects.")
    
    st.write("As said by [Wirth and Hipp](http://www.cs.unibo.it/~danilo.montesi/CBD/Beatriz/10.1.1.198.5133.pdf) (p. 04), 'the CRISP-DM reference model for data mining provides an overview of the life cycle of a data mining project'. This process allows us to iterate over the steps and we can map all possible problems in the project.")

    st.write("Aiming to provide more productivity and effectiveness, the Data Science project is broken in six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment.")

    st.write("The image bellow summarizes its steps:")

    st.image('images/crispdm.png', use_column_width=True)

    st.write("The main reason why CRISP-DM was used is because it has four main advantages:")

    st.markdown("* for each complete cycle, we have and end-to-end solution that can be implemented and attend some of business demands;")

    st.markdown("* it provides a more quickly business results than many others methodologies;")

    st.markdown("* we can map many problems and antecipate impediments and avoid them;")

    st.markdown("* it helps us not to spend too much time on a particular step.")

    st.write("In order to get it closer to our challenge, we'll rename some of that CRISP-DM. So, The final pipeline is the following:")

    st.markdown("**1. Problem Understanding**: in this step, we'll look a bit deeper on the challenge itself and try to design some ways we could take.")
    st.markdown("**2. Data Understanding and Preparation**: this is the time to better understand the dataset we're given and do some data preparation in order to fit the data in the strategy we've decided to follow.")
    st.markdown("**3. Implementation**: to implement the solution looking forward to find similar series to the baseline one.")
    st.markdown("**4. Evaluation**: evaluate the results testing for generalization capacity")
    st.markdown("**5. Deployment**: put a application in production where the user can pass the baseline, the list of target series, and the period and the app return the top 5 similar series.")

    st.write("Since we're following th CRISP-DM methodology, leading the project in cycles, we'll skip the deployment step in this first cycle and work on it in the second one.")


    st.markdown(f"### <span style='color:{SUBTITLE_COLORS}'>The solution: in summary</span>", unsafe_allow_html=True)

    st.markdown("After some research, we found some ways to get the similarity between series, such as Dynamic Time Warping, \
        Correlation, Regression, Standard Deviation, Return analysis, Euclidean Distance.")

    st.markdown(f"However, for simplicity, we went with a comparison of the area between both curves. \
        The challenge is that the values of all series could range over different values. So we reach the <span style='color:{TITLE_COLORS}'>*Min Max*</span> scaling option, bringing the series to the range of 0 to 1.", unsafe_allow_html=True)

    st.markdown("So we did. The solution is basically the sum of the absolute areas between the two scaled series divided by the \
        total area bellow both curves")

    st.markdown("The image bellow shows us the area between two normalized curves.")

    st.image("images/auc.png")

    st.markdown("Since we have a lot of Ticker-Exchange pairs to analyze, for this project cycle we decided to randomly select \
        200 of them. In a further cycle, we could go to a best designed selection, like same company business (bank), same Exchange Ticker, an so on.")
    
    st.markdown("Thus, we'll iterate over the entire target series and get the period with higher similarity. Since we need to find at least 5 series similar to the baseline, \
        we'll take the top 5 similar from that 200 series.")
    
    
        