import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_venn as vplt
import numpy as np
import lottie_animation as la

st.set_page_config(
    page_title="Pathway Analysis", layout="centered", initial_sidebar_state="expanded"
)

with open("./static/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# --Download df--
def convert_df(df):
    return df.to_csv().encode("utf-8")


with st.sidebar:
    st.title("GSDE Pathway Analysis Tool")
    target_markers = st.text_input(
        "Paste list of target biomarkers (If more than one separate with a space)."
    )
    if target_markers:
        st.success("List uploaded successfully!")
    else:
        st.info("Upload a list of biomarkers!", icon="ℹ️")

# --Logic--
marker_list = target_markers.split(":")
uniprotid = []
prot_desc = []
for i in range(len(marker_list)):
    if marker_list[i] == "UniProtKB":
        continue
    uniprotid.append(marker_list[i][0:6])
    prot_desc.append(marker_list[i][7:-10])
targets_df = pd.DataFrame(
    list(zip(uniprotid, prot_desc)), columns=["uniprotid", "protein_desc"]
)
targets_df.drop_duplicates(subset=["uniprotid"], keep=False, inplace=True)

# -- DataFrames --
menu = pd.read_excel("excel_input/soma_menu-st.xlsx")
overlap = targets_df.merge(menu, on="uniprotid")
overlap.rename(
    columns={"uniprotid": "UniProtID", "protein_desc": "Protein Description"},
    inplace=True,
)
display_df = targets_df.merge(menu, on="uniprotid", how="right")
display_df.rename(
    columns={"uniprotid": "UniProtID", "protein_desc": "Present in Menu (Y/N)"},
    inplace=True,
)

# Change all non-null values to col2 to 'Y'
display_df["Present in Menu (Y/N)"].loc[
    ~display_df["Present in Menu (Y/N)"].isnull()
] = "Y"
display_df["Present in Menu (Y/N)"].loc[
    display_df["Present in Menu (Y/N)"].isnull()
] = "N"

# --Venn Diagram --
targets_len, menu_len, overlap_len = len(targets_df), len(menu), len(overlap)
fig, ax = plt.subplots()
vplt.venn2(
    subsets=(targets_len, menu_len, overlap_len),
    set_labels=("Target Biomarkers", "SomaScan Menu", "Overlap"),
    set_colors=("#4067E2", "#DB40EF"),
    ax=ax,
)
vplt.venn2_circles(subsets=(targets_len, menu_len, overlap_len))

# -- Display figs --
if target_markers:
    st.markdown("## Pathway Metrics")
    col1, col2, col3 = st.columns(3)
    st.snow()
    col1.metric("Total Biomarkers", targets_len)
    col2.metric("Overlap", overlap_len)
    perc = round((overlap_len / targets_len) * 100)
    col3.metric("SomaScan Coverage", f"{perc} %")
    st.dataframe(display_df, use_container_width=True)
    st.pyplot(fig)

else:
    lottie_hello = la.load_lottie_url(
        "https://assets10.lottiefiles.com/packages/lf20_8olbnwvj.json"
    )

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height=None,
        width=None,
        key=None,
    )


if target_markers:
    with st.sidebar:
        # -- download button --
        out = convert_df(overlap)

        dl_csv = st.download_button(
            label="Download Overlap as CSV file",
            data=out,
            file_name="BiomarkerOverlap.csv",
            mime="text/csv",
        )

        if len(overlap) > 0 and dl_csv == True:
            st.success("Biomarkers successfully downloaded!")
        else:
            st.warning("Whoops! You downloaded an empty list", icon="🚨")
