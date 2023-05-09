import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_venn as vplt
import modules.lottie_animation as la
import modules.gene_ontology as gene_ontology

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
    target_markers = st.text_input("Enter Gene Ontology ID.")
    if target_markers:
        st.success("List uploaded successfully!")
    else:
        st.info("Upload a list of biomarkers!", icon="ℹ️")

if len(target_markers) == 10:
    # --Logic--
    targets = gene_ontology.get_ontology_biomarkers(go_id=target_markers)
    targets_df = pd.DataFrame(targets)
    targets_df.drop_duplicates(subset=["UniProtId"], keep=False, inplace=True)

    # -- DataFrames --
    menu = pd.read_excel("static/excel_input/soma_menu-st.xlsx")
    menu.rename(columns={"uniprotid": "UniProtId"}, inplace=True)
    overlap = targets_df.merge(menu, on="UniProtId", how="inner")
    targets_len, menu_len, overlap_len = len(targets_df), len(menu), len(overlap)

    # --Venn Diagram --
    fig, ax = plt.subplots()
    vplt.venn2(
        subsets=(targets_len, menu_len, overlap_len),
        set_labels=("Target Biomarkers", "SomaScan Menu", "Overlap"),
        set_colors=("#4067E2", "#DB40EF"),
        ax=ax,
    )
    vplt.venn2_circles(subsets=(targets_len, menu_len, overlap_len))

    # -- Display figs --
    st.markdown("## Pathway Metrics")
    col1, col2, col3 = st.columns(3)
    st.snow()

    col1.metric("Total Biomarkers", targets_len)
    col2.metric("Overlap", overlap_len)
    perc = round((overlap_len / targets_len) * 100)
    col3.metric("SomaScan Coverage", f"{perc} %")
    st.dataframe(overlap, use_container_width=True)
    st.pyplot(fig)

    with st.sidebar:
        # -- download button --
        out = convert_df(overlap)

        dl_csv = st.download_button(
            label="Download Overlap as CSV file",
            data=out,
            file_name="BiomarkerOverlap.csv",
            mime="text/csv",
        )

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
