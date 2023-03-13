import streamlit as st
from hydralit import HydraHeadApp
# from hydralit_components import CookieManager


class ContactUsAPP(HydraHeadApp):

    def __init__(self, title = 'Loader', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

    def run(self):

        try:   
            st.header(":mailbox: Feedback!")
            contact_form = """
                <form action="https://formsubmit.co/jantharat.c@thainhf.org" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Your name" required>
                    <input type="email" name="email" placeholder="Your email" required>
                    <textarea name="message" placeholder="Your message here"></textarea>
                    <button type="submit">Send</button>
                </form>
                """
            st.markdown(contact_form, unsafe_allow_html=True)
            def local_css(file_name):
                with open(file_name) as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            local_css("style2.css")

            st.markdown("""---""")
            st.header("Contact Us ☎️")
            st.write("##")

            t1,t2,t3,t4 = st.columns((0.2,0.8,1.5,1))
            t1.image('resources/pig2.png', width = 40)
            # t2.write("ภาควิชาวิศวกรรมคอมพิวเตอร์")
            Ideal_d1 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">ภาควิชาวิศวกรรมคอมพิวเตอร์</p>'
            t2.markdown(Ideal_d1, unsafe_allow_html=True)
            # t2.write("มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี")
            Ideal_d2 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี</p>'
            t2.markdown(Ideal_d2, unsafe_allow_html=True)
            # t3.write("ชั้น 10-11, อาคารวิศววัฒนะ, มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี ")
            Ideal_d3 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">ชั้น 10-11, อาคารวิศววัฒนะ, มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี</p>'
            t3.markdown(Ideal_d3, unsafe_allow_html=True)
            # t3.write("126 ถนนประชาอุทิศ แขวงบางมด เขตทุ่งครุ กรุงเทพฯ 10140 ")
            Ideal_d4 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">126 ถนนประชาอุทิศ แขวงบางมด เขตทุ่งครุ กรุงเทพฯ 10140</p>'
            t3.markdown(Ideal_d4, unsafe_allow_html=True)
            # t4.write("(+66) 0-2470-9388")
            Ideal_d5 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">(+66) 0-2470-9388</p>'
            t4.markdown(Ideal_d5, unsafe_allow_html=True)
            # t4.write("E-mail: nongyao.jam@mail.kmutt.ac.th")
            Ideal_d6 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">E-mail: nongyao.jam@mail.kmutt.ac.th</p>'
            t4.markdown(Ideal_d6, unsafe_allow_html=True)
            col_header_text,col_header_logo_right,col_header_logo_right_far = st.columns([2,2,1])

            
            #col_header_logo_right_far.image(os.path.join(".","resources","hydra.png"),width=100,)
            if col_header_text.button('This will open a KMUTT Website'):
                self.do_redirect("https://www.kmutt.ac.th/")
            st.write("##")

#             t1,t2,t3,t4 = st.columns((0.2,0.8,1.5,1))
#             t1.image('resources/pig1.png', width = 40)
#             # t2.write("วิทยาลัยแพทยศาสตร์ศรีสวางควัฒน")
#             Ideal_d7 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">วิทยาลัยแพทยศาสตร์ศรีสวางควัฒน</p>'
#             t2.markdown(Ideal_d7, unsafe_allow_html=True)
#             # t2.write("ราชวิทยาลัยจุฬาภรณ์")
#             Ideal_d8 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">ราชวิทยาลัยจุฬาภรณ์</p>'
#             t2.markdown(Ideal_d8, unsafe_allow_html=True)
#             # t3.write("906 ถ.กำแพงเพชร 6 แขวงตลาดบางเขน เขตหลักสี่ กรุงเทพมหานคร 10210")
#             Ideal_d9 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">906 ถ.กำแพงเพชร 6 แขวงตลาดบางเขน เขตหลักสี่ กรุงเทพมหานคร 10210</p>'
#             t3.markdown(Ideal_d9, unsafe_allow_html=True)
#             # t4.write("สายด่วน รจภ. 1118, 0-2576-6718")
#             Ideal_d10 = '<div align="left"><p style="font-sans-serif:; color: black; font-size: 15px; background-color: white;">สายด่วน รจภ. 1118, 0-2576-6718</p>'
#             t4.markdown(Ideal_d10, unsafe_allow_html=True)
#             col_header_text2,col_header_logo_right,col_header_logo_right_far = st.columns([2,2,1])
#             if col_header_text2.button('This will open a CHULABHORN ROYAL ACADEMY Website'):
#                 self.do_redirect("https://pscm.cra.ac.th/")
#             st.write("##")

      
        except Exception as e:
            st.image("./resources/failure.png",width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))
