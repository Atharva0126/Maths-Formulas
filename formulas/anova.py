import streamlit as st
import pandas as pd

def show_anova():

```
st.header("ANOVA")

st.write("""
ANOVA (Analysis of Variance) is a statistical method used
to compare the means of three or more groups.
""")

st.subheader("Important Formulas")

st.latex(r"Grand\ Mean=\frac{\sum X}{N}")

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

excel_file = "data/Anova.xlsx"

xls = pd.ExcelFile(excel_file)

selected_sheet = st.selectbox(
    "Select Session",
    xls.sheet_names
)

df = pd.read_excel(
    excel_file,
    sheet_name=selected_sheet
)

st.subheader("Dataset")

st.dataframe(
    df,
    use_container_width=True
)
```

