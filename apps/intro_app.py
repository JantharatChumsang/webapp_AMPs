import os
import streamlit as st
from hydralit import HydraHeadApp

MENU_LAYOUT = [1,1,1,7,2]


class IntroApp(HydraHeadApp):

    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title


    #This one method that must be implemented in order to be used in a Hydralit application.
    #The application must also inherit from the hydrapp class in order to correctly work within Hydralit.
    def run(self):

        try:
            st.markdown("<h2 style='text-align: center;'>Web Application for Antimicrobial Peptide Prediction</a></h2>",unsafe_allow_html=True)
            _,_,col_logo, col_text,_ = st.columns((0.2,0.2,0.5,4.1,0.4))
            col_logo.image(os.path.join(".","resources","data.png"),width=80,)
            col_text.subheader("Web Application for Antimicrobial Peptide Prediction Project It is intended to develop an easy-to-use and accurate antimicrobial peptide probabilistic prediction web application.")
            st.markdown("""---""")
           
            #Intro-----------------------------------------------------------------------------------
            st.write("##")
            _,_,col_logo, col_text,_ = st.columns((1,0.5,2.55,8.5,2))
            Ideal_01 = '<div align="left"><p style="font-sans-serif:; color: #F36C23; font-size: 40px; background-color: white; border-radius: 5px;">01━━</p>'
            col_logo.markdown(Ideal_01, unsafe_allow_html=True) 
            # col_logo.markdown(f'<h1 style="color:#F36C23;font-size:35px;">{"01━━"}</h1>', unsafe_allow_html=True)
            Ideal_int = '<div align="left"><p style="font-verdana:; color: #F36C23; font-size: 30px; background-color: white; border-radius: 5px;">Introduction</p>'
            col_logo.markdown(Ideal_int, unsafe_allow_html=True) 
             
            # col_logo.image(os.path.join(".","resources","denoise.png"),width=80,)
            col_text.info("""
            Microorganisms are microscopic organisms that cannot be seen by naked eye. Statistically, microorganism that cause the most global mortality is antibiotic-resistant bacteria.[[1]](https://www.who.int/en/news-room/fact-sheets/detail/antimicrobial-resistance) 
            Bacteria are microorganisms that can become pathogenic. They can be divided into gram-positive and gram-negative by their cell wall characteristics.[[2]](https://www.scimath.org/lesson-biology/item/9795-2019-02-21-07-08-54). 
            Usually, antibiotics are used to kill bacteria. But since bacteria are developing drug resistance, a newly discovered substance that can inhibit bacteria is being interested, antimicrobial peptides.[[3]](https://www.biorxiv.org/content/10.1101/2022.01.28.478081v1.abstract)
            However, the peptide must have specific amino acid pattern to possess antimicrobial properties. Therefore, machine learning needs to be applied to help analyze whether the peptide is likely to be an antimicrobial peptide for future antimicrobial development.""")
            col_text.info("""
            Therefore, this web application is developed as an accurate and accessible solution to predict the likelihood of peptides having an antimicrobial activity. Data from publicly available databases: [DBAASP](https://dbaasp.org/home), [DRAMP](http://dramp.cpu-bioinfor.org/), 
            and [UniProt](https://www.uniprot.org/) were used to analyze the peptide's potential of antimicrobial activity using machine learning. 
            There are two parts to the procedure.""")
            col_text.info("""
            The first part is to predict the likelihood that the peptide will exhibit antimicrobial activity. This section applied Gradient Boosting Model (GBM) which has prediction accuracy of 0.928 and F1-Score of 0.921. The Area Under Curve (AUC) of the model was 0.977 and the 5-fold cross-validation score was 0.920.""")
            col_text.info("""
            The second part predicts which type of bacteria the peptides exhibit antimicrobial activity. This was done using Random Forest (RF) model, which divides the peptides into gram-positive and gram-negative. The positive gram has a prediction accuracy of 0.925 
            and the model's performance was measured with an F1-Score of 0.959, the Area Under Curve (AUC) of the model of 0.966, and a 5-fold Cross-Validation Score of 0.921.
            And at the negative gram, the improved prediction accuracy was 0.942 and the model performance was measured with an F1-Score of 0.970, the Area Under Curve (AUC) of the model was 0.979, and the Cross-Validation Score was 0.940. can serve two objectives as follows...""")
            #Purpose -----------------------------------------------------------------------------------------------
            st.write("##")
            _,_,col_logo, col_text,_ = st.columns((1,0.5,2.55,8.5,2))
            Ideal_02 = '<div align="left"><p style="font-sans-serif:; color: #F36C23; font-size: 40px; background-color: white; border-radius: 5px;">02━━</p>'
            col_logo.markdown(Ideal_02, unsafe_allow_html=True) 
            # col_logo.markdown(f'<h1 style="color:#F36C23;font-size:35px;">{"02━━"}</h1>', unsafe_allow_html=True)
            # col_logo.subheader("Purpose")
            Ideal_pro = '<div align="left"><p style="font-verdana:; color: #F36C23; font-size: 30px; background-color: white; border-radius: 5px;">Purpose</p>'
            col_logo.markdown(Ideal_pro, unsafe_allow_html=True) 
            
            
            _,_,col_logo1, col_text1,col_btn1 = st.columns((1,0.5,2.55,8.5,2))
            col_text1.info("⓵ 󠀠 To apply machine learning in microbial inhibitability prediction.")
            col_text1.info("⓶ 󠀠 To develop accurate and accessible web application in microbial inhibitability prediction.")
            st.write("##")

            #Theory ------------------------------------------------------------------------------------------------
            _,_,col_logo2, col_text2,_ = st.columns((1,0.5,2.55,8.5,2))
            # col_logo2.markdown(f'<h1 style="color:#F36C23;font-size:35px;">{"03━━"}</h1>', unsafe_allow_html=True)
            # col_logo2.subheader("Theory")
            Ideal_03 = '<div align="left"><p style="font-sans-serif:; color: #F36C23; font-size: 40px; background-color: white; border-radius: 5px;">03━━</p>'
            col_logo2.markdown(Ideal_03, unsafe_allow_html=True) 
            Ideal_th = '<div align="left"><p style="font-verdana:; color: #F36C23; font-size: 30px; background-color: white; border-radius: 5px;">Theory</p>'
            col_logo2.markdown(Ideal_th, unsafe_allow_html=True) 
            
            _,_,col_logo3,col_pic3,col_text3,col_btn3 = st.columns((1,0.5,2.55,1,8,2))
            col_text3.markdown(f'<h3 style="color:#1F3D7C;font-size:16px;">{"📙 Peptides"}</h3>', unsafe_allow_html=True)

            _,_,col_logo4,col_pic4,col_text4,col_btn4 = st.columns((1,0.5,2.55,1,8,2))
            col_pic4.write("##")
            col_pic4.image(os.path.join(".","resources","pep.png"),width=75,)
            col_text4.info("""Peptide is a short chain of amino acids, which are connected sequentially with peptide bonds. Peptides can perform biological functions. For example, some peptides can act as hormones.[[4]](https://www.nature.com/scitable/definition/peptide-317/)""")
            st.write("##")

            _,_,col_logo5,col_pic5, col_text5,col_btn5 = st.columns((1,0.5,2.55,1,8,2))
            col_text5.markdown(f'<h3 style="color:#1F3D7C;font-size:16px;">{"📙 Microbe"}</h3>', unsafe_allow_html=True)

            _,_,col_logo6,col_pic6,col_text6,col_btn6 = st.columns((1,0.5,2.55,1,8,2))
            col_pic6.write("##")
            col_pic6.image(os.path.join(".","resources","mi2.png"),width=75,)
            col_text6.info(""" Microbes, also called microorganisms are tiny organisms that can be found environmentally. These organisms are too small to be seen by naked eye and can affect human health, both positively and negatively. The most common types are bacteria, viruses, and fungi.[[5]](https://www.ncbi.nlm.nih.gov/books/NBK279387/#:~:text=Microbes%20are%20tiny%20living%20things,are%20important%20for%20our%20health.)""")
            st.write("##")

            _,_,col_logo7,col_pic7, col_text7,col_btn7 = st.columns((1,0.5,2.55,1,8,2))
            col_text7.markdown(f'<h3 style="color:#1F3D7C;font-size:16px;">{"📙 Antimicrobial peptides"}</h3>', unsafe_allow_html=True)

            _,_,col_logo8,col_pic8,col_text8,col_btn8 = st.columns((1,0.5,2.55,1,8,2))
            col_pic8.write("##")
            col_pic8.image(os.path.join(".","resources","antimi.png"),width=75,)
            col_text8.info("""Antimicrobial peptides, abbreviated as AMPs, are peptides that play vital role in defense mechanisms against invasion of pathogenic microorganisms in living organisms, including humans. These peptides are currently the topic of interest to develop into antimicrobial drugs.[[6]](Srinagarind Medical Journal (ejnal.com))""")
            st.write("##")

            _,_,col_logo7,col_pic7, col_text7,col_btn7 = st.columns((1,0.5,2.55,1,8,2))
            col_text7.markdown(f'<h3 style="color:#1F3D7C;font-size:16px;">{"📙 Models"}</h3>', unsafe_allow_html=True)

            _,_,col_logo8,col_pic8,col_text8,col_btn8 = st.columns((1,0.5,2.55,1,8,2))
            col_pic8.write("##")
            col_pic8.image(os.path.join(".","resources","model.png"),width=75,)
            col_text8.info("""This application consists of two machine learning models for classification task. A gradient boosting model is used to predict microbial inhibitability of input peptides, whereas a random forest model is used to predict which gram strain the peptide can inhibit. The two models were selected among other models from the highest accuracy during testing.""")
            st.write("##")
            # _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            #Citation -----------------------------------------------------------------------------------------------------------            
            _,_,col_logo, col_text,_ = st.columns((1,0.5,20,0.01,2))
            # col_logo.markdown(f'<h1 style="color:#F36C23;font-size:35px;">{"04━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"}</h1>', unsafe_allow_html=True)
            # col_logo.subheader("Citation")
            Ideal_04 = '<div align="left"><p style="font-sans-serif:; color: #F36C23; font-size: 40px; background-color: white; border-radius: 5px;">04━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</p>'
            col_logo.markdown(Ideal_04, unsafe_allow_html=True) 
            Ideal_ci = '<div align="left"><p style="font-verdana:; color: #F36C23; font-size: 30px; background-color: white; border-radius: 5px;">Citation</p>'
            col_logo.markdown(Ideal_ci, unsafe_allow_html=True) 

            col_logo.caption("""
            ```
            [1] World Health Organization. (2021/11/17).Antimicrobial resistance.
            link. https://www.who.int/en/news-room/fact-sheets/detail/antimicrobial-resistance
            [2] พจนา เพชรคอน. (2020/11/03).รู้ทันแบคทีเรีย.
            link. https://www.scimath.org/lesson-biology/item/9795-2019-02-21-07-08-54
            [3] Cold Spring Harbor Laboratory. (2022/01/28).Comparative analysis of machine learning algorithms on the microbial strain-specific AMP prediction
            link. https://www.biorxiv.org/content/10.1101/2022.01.28.478081v1.abstract
            [4] Sciatable by nature educayion . (2023).Peptide.
            link. https://www.nature.com/scitable/definition/peptide-317/
            [5] Institute for Quality and Efficiency in Health Care (IQWiG). (2019/08/29).What are microbes?
            link. https://www.ncbi.nlm.nih.gov/books/NBK279387/
            [6] Sakawrat Kanthawong. (2023). Antimicrobial Peptides: Alternative Therapy for Cancer Treatment?. 
            link. Srinagarind Medical Journal (ejnal.com)
            ``` """)
            st.write("##")
            st.write("##")
            
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))




    