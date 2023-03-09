import os
import apps
import streamlit as st
import json
import requests
# from apps import pred_app
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from hydralit import HydraHeadApp
#-----------------------------------------------------------------------------------------------------------------------------

MENU_LAYOUT = [1,1,1,7,2]
class HomeApp(HydraHeadApp):


    def __init__(self, title = 'home', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):

        try:    
            # #### sticker image ####
            def load_lottiefile(filepath: str):
                with open (filepath,"r") as f:
                    return json.load(f)

            # json animation ---------------------------------------------------------------------
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()         
  
            with st.container():
                left_column1,left_column2, right_column,right_column2 = st.columns((0.65,2.5,2.5,0.55))
                with right_column:                  
                    st.text("Welcome to✨")
                    st.title("Web Application for Antimicrobial Peptide Prediction ")
                    st.subheader("เว็บแอปพลิเคชันสำหรับการทำนายเพปไทด์ต้านจุลชีพ")
                    Ideal_title = '<p style="font-family:; color:#31333F; font-size: 20px; ">Web Application to test the antimicrobial peptide activity against bacteria.</p>'
                    # st.markdown(Ideal_title, unsafe_allow_html=True)
                    # st.write("##")
                    Ideal_title = '<p style="font-family:; color:#06BBCC; font-size: 18px; ">Click to see photo credits.</p>'
                    st.markdown(Ideal_title, unsafe_allow_html=True)
                    
                    
                    if st.button("📸 Image credit from") is True:                                
                        st.caption("""
                        ```
                        [1] Journal Article. (2023). Host-Pathogen Interaction Analysis | Genetic mechanism studies with NGS. 
                        link. https://www.illumina.com/areas-of-interest/microbiology/infectious-diseases/host-pathogen-interactions.html
                        [2] ANMJ Staff. (2020/11/19).Superbugs on track to kill more people than COVID-19, infectious disease experts warn.
                        link. https://anmj.org.au/superbugs-on-track-to-kill-more-people-than-covid-19-infectious-disease-experts-warn/
                        [3] @InfusioBH. (2023).Peptide Therapy | Infusio.org.
                        link. https://www.infusio.org/peptide-therapy/
                        [4] Hannah Balfour. (2022/07/8).Microbial risks presented by aging facilities.
                        link. https://www.europeanpharmaceuticalreview.com/news/173017/microbial-risk-presented-by-aging-facilities/
                        ``` """)     
                    
                        
                with left_column2:                    
                    st.image('resources/pig5.png',width=450,use_column_width=None, clamp=False, channels="RGB", output_format="auto")
               
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))





