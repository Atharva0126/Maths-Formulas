import streamlit as st
import pandas as pd
import os


def show_anova():

    st.header("ANOVA")

    st.write(
        """
        ANOVA (Analysis of Variance) is a statistical method
        used to determine whether there is a significant
        difference between the means of three or more groups.
        """
    )

    st.subheader("Important Formulas")

    st.latex(r"\bar{X}=\frac{\sum X}{N}")

    st.latex(
        r"SSB=\sum n_i(\bar{x_i}-\bar{x})^2"
    )

    st.latex(
        r"SSE=\sum(x_{ij}-\bar{x_i})^2"
    )

    st.latex(
        r"SST=SSB+SSE"
    )

    st.latex(
        r"F=\frac{MSB}{MSE}"
    )

    excel_path = "data/Anova.xlsx"

    if not os.path.exists(excel_path):
        st.error("Anova.xlsx not found inside data folder.")
        return

    xls = pd.ExcelFile(excel_path)

    sheet = st.selectbox(
        "Select Session",
        xls.sheet_names
    )

    df = pd.read_excel(
        excel_path,
        sheet_name=sheet
    )

    st.subheader("Session Data")

    st.dataframe(
        df,
        use_container_width=True
    )

    with open(excel_path, "rb") as file:

        st.download_button(
            label="📥 Download Excel File",
            data=file,
            file_name="Anova.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
