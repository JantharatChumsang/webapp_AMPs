import streamlit as st
from hydralit import HydraHeadApp

# -------------------------------------------------------------------------------------------------------------------------------------
class HowtoApp(HydraHeadApp):

    def __init__(self, title = 'How to use', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self):
        Ideal_hp = '<div align="center"><p style="font-family:; color:#000000; font-size: 35px; background-color: #C2DFFF; border-radius: 5px;">How to use web application</p>'
        st.markdown(Ideal_hp, unsafe_allow_html=True)
        st.write('##')
        l_c1, l_c2, gg, la, ll = st.columns((0.6,8,1,6,0.6))
        with l_c2:  
            st.write('##') 
            st.write('##')
            st.write('##')  
            st.write('##') 
            st.image('resources/001.png', width = 750)
            st.write('##')
            st.write('##')
            st.write('##') 
            
        with la:
            Ideal_hp = '<div align="center"><p style="font-family:; color:#000000; font-size: 25px; background-color: #C2DFFF; border-radius: 5px;">Home Page</p>'
            st.markdown(Ideal_hp, unsafe_allow_html=True)
            st.info('⓵ Home page is the main web page of a website or he start page shown in a web browser when the application first opens.')
            st.info('⓶ Predict your peptide page is the web page of a predicted antimicrobial peptide.')
            st.info('⓷ How to use web application page is a web page for users know to specify how the web application is used.')
            st.info('⓸ Dashboard page is the web page that displays information data for use in training and testing models.')
            st.info('⓹ About us page have two part first part is the introduction page to show information about the detail of a website second part is the page to show a member of the project.')
            st.info('⓺ Contact us page is the web page for users who want to feedback about the project and can contact them.')
            st.info('⓻ Button for show credits photo of the home page.')
        
        ss1, ss2, ss3, ss4, ss5 = st.columns((0.6,6,1,8,0.6))
        with ss2:
            st.write('##') 
            st.write('##') 
            Ideal_pp = '<div align="center"><p style="font-family:; color:#000000; font-size: 25px; background-color: #C2DFFF; border-radius: 5px;">Predict your peptide page</p>'
            st.markdown(Ideal_pp, unsafe_allow_html=True)
            st.info('⓵ Enter user peptide in format FASTA text format.')
            st.info('⓶ Upload user peptides in FASTA file format. A single channel should be selected for the input of peptides between FASTA text format or FASTA file format.')
            st.info('⓷ Press for predicting peptide.')
            st.info('⓸ Press for want to know how to input data for prediction.')
            st.write('##')
            st.write('##')
            st.write('##') 

        with ss4:
            st.write('##') 
            st.image('resources/002.png', width = 750)
            st.write('##')
            st.write('##')
            st.write('##') 
            
            
