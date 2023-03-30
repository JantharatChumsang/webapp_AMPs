import os
import streamlit as st
from hydralit import HydraHeadApp
from streamlit_lottie import st_lottie
import json
import requests

MENU_LAYOUT = [1,1,1,7,2]


class IntroApp(HydraHeadApp):

    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        # self.__dict__.update(kwargs)
        self.title = title


    #This one method that must be implemented in order to be used in a Hydralit application.
    #The application must also inherit from the hydrapp class in order to correctly work within Hydralit.
    def run(self):

        try:
            st.markdown("<h2 style='text-align: center;'>WAAPP: Web Application for Antimicrobial Peptide Prediction</a></h2>",unsafe_allow_html=True)
            _,_,col_logo, col_text,_ = st.columns((0.2,0.2,0.5,4.1,0.4))
            col_logo.image(os.path.join(".","resources","data.png"),width=80,)
            col_text.subheader("WAAPP It is intended to develop an easy-to-use and accurate antimicrobial peptide probabilistic prediction web application.")
            st.markdown("""---""")
            
            #Intro-----------------------------------------------------------------------------------
            st.write("##")
            _d,_q,col_logo, col_texta,_qq = st.columns((0.5,5,0.1,9,1))
            def load_lottiefile(filepath: str):
                with open (filepath,"r") as f:
                    return json.load(f)
            def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()
            
            
            with _q:
                _q.write("##")
                # _q.image(os.path.join(".","resources","mi.png"),width=100,)
                lottie2_anti = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_hyqjhavp.json")
                st_lottie(lottie2_anti, height=300,  key="codvingaazq") 
            with col_texta:   
                I_intro1 = '<div align="left"><p style="font-sans-serif:; color: #353131; font-size: 16px; background-color: white; border-radius: 5px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Antimicrobial resistance is a serious health problem, causing illnesses and deaths to millions of people globally. <br>To cope with this threat, the discovery of novel drugs against microbes is urgently needed. <br>Antimicrobial peptide (AMP) is a class of peptides with antimicrobial activity, which is considered a potential target for anti-bacterial drug development. AMP has its distinct signatures, e.g., high positive charge, and high hydrophobicity, allowing computational methods to predict peptides that can kill bacteria. In recent years, a machine learning approach has been applied to facilitate AMP prediction, which effectively reduces the cost and time for AMP screening.</p>'
                col_texta.markdown(I_intro1, unsafe_allow_html=True)
                st.write("##")
                I_intro2 = '<div align="left"><p style="font-sans-serif:; color: #353131; font-size: 16px; background-color: white; border-radius: 5px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Therefore, this project aims to develop a machine-learning model for AMP prediction. Sequences of AMP were collected from publicly available databases, including: </p>'
                col_texta.markdown(I_intro2, unsafe_allow_html=True)
                col_texta.image(os.path.join(".","resources","dataso.png"),width=700,)

            aab1,aab2,aab3,aab4,aab5 = st.columns((14.8,3,3,3,3))
            if aab2.button('DBAASP'):
                self.do_redirect("https://dbaasp.org/home")
            if aab3.button('DRAMP'):
                self.do_redirect("http://dramp.cpu-bioinfor.org/")
            if aab4.button('UniProt'):
                self.do_redirect("https://www.uniprot.org/")

            _d,_q,col_logo, col_texta,_qq = st.columns((0.5,5,0.1,9,1))
            col_texta.write("##")
            I_intro3 = '<div align="left"><p style="font-sans-serif:; color: #353131; font-size: 16px; background-color: white; border-radius: 5px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sequences of peptides without antimicrobial activity were collected from Kaggle COVID-19/SARS B-cells: basic predictions and EDA, GitHub poncey/PreAntiCoV, and GitHub BioGenies/NegativeDatasets. After data preprocessing, <br>a total of 13443 positive and 16189 negative AMPs were used for model development. </p>'
            col_texta.markdown(I_intro3, unsafe_allow_html=True)

            _d,_q,col_logo, col_texta,_qq = st.columns((1,9,0.1,5,1))
            with col_texta:
                st.write("##")
                lottie2_codingsdd = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_LmW6VioIWc.json")
                st_lottie(lottie2_codingsdd, height=280,  key="codvingzq")
            _q.write("##")
            _q.write("##") 
            I_intro4 = '<div align="left"><p style="font-sans-serif:; color: #353131; font-size: 16px; background-color: white; border-radius: 5px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Gradient Boosting Model (GBM) was applied to screen for AMPs, and 92.8% accuracy, 92.1% F1 score, <br>and 92.0% cross-validation score were achieved. In addition, Random Forest (RF) model was used to predict potential groups of bacteria, gram-positive and gram-negative, that were targeted by the peptides.</p>'
            _q.markdown(I_intro4, unsafe_allow_html=True)
            I_intro5 = '<div align="left"><p style="font-sans-serif:; color: #353131; font-size: 16px; background-color: white; border-radius: 5px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The performance of RF for gram-positive group prediction was 92.5% accuracy, 95.9% F1 score, and 92.1% cross-validation score. Comparably, 94.2% accuracy, 97.0% F1 score, and 94.0% cross-validation score were calculated in RF for gram-negative group prediction. This project successfully developed machine learning models for AMP prediction and the output of the projects would be beneficial for future anti-bacterial drug development.</p>'
            _q.markdown(I_intro5, unsafe_allow_html=True)
         
            st.write("##")
 
            
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))




    
