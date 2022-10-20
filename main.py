import streamlit as st
import pandas as pd


st.set_page_config(page_title='Pathway Analysis', layout='centered')

h = st.container()
h.title('GSDE Pathway Analysis Tool')
st.markdown("""---""")

body = st.container()
target_markers = body.text_input("Paste list of target biomarkers (If more than one separate with a space).")
st.markdown("""---""")

#--Logic--
marker_list = target_markers.split(':')
uniprotid = []
prot_desc = []
for i in range(len(marker_list)):
    if marker_list[i] == 'UniProtKB':
        continue
    uniprotid.append(marker_list[i][0:6])
    prot_desc.append(marker_list[i][7:-10])
targets_df = pd.DataFrame(list(zip(uniprotid, prot_desc)), columns=['uniprotid', 'protein_desc'])
targets_df.drop_duplicates(
    subset=['uniprotid'],
    keep=False,
    inplace=True
    )

menu = pd.read_excel('excel_input/soma_menu-st.xlsx')
overlap = targets_df.merge(menu, on='uniprotid')
overlap.rename(columns={'uniprotid': 'UniProtID', 'protein_desc': 'Protein Description'}, inplace=True)
#----

tail = st.container()
tail.subheader("Results")

#-- Logic for download button--
def convert_df(df):
    return df.to_csv().encode('utf-8')
out = convert_df(overlap)
#-----

tail.download_button(
    label="Download as CSV file",
    data=out,
    file_name="Biomarker Overlap.csv",
    mime="text/csv"
)
tail.success('Biomarkers successfully downloaded!')




