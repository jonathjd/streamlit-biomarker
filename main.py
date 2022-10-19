import streamlit as st
import pandas as pd
from PIL import Image


st.set_page_config(page_title='Pathway Analysis', layout='centered')

h = st.container()
h.title('GSDE Pathway Analysis Tool')
st.markdown("""---""")

body = st.container()
go_num = body.number_input('How many Gene Ontology categories are you entering?', 1, 10)
go_id = body.text_input("Enter GO identifiers (e.g. GO:0022008, GO:0030221, etc).")
go_desc = body.text_input("Enter GO identifier description")
target_markers = body.text_input("Paste list of target biomarkers (If more than one separate with a space).")
st.markdown("""---""")

marker_list = target_markers.split(':')
uniprotid = []
prot_desc = []
for i in range(len(marker_list)):
    if marker_list[i] == 'UniProtKB':
        continue
    uniprotid.append(marker_list[i][0:6])
    prot_desc.append(marker_list[i][7:-10])

targets_df = pd.DataFrame(list(zip(uniprotid, prot_desc)), columns=['uniprotid', 'protein_desc'])
menu = pd.read_excel('excel_input/soma_menu-st.xlsx')
body.subheader("Dataframe preview:")
st.dataframe(menu, use_container_width=True)
st.dataframe(targets_df, use_container_width=True)

