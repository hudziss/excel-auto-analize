import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Excel Auto-Analīze", layout="wide")

st.title("Excel tabulu automātisko pārskatu veidotājs")
st.write("Augšupielādē .xlsx failu → saņem datu preview, pivot un pāris grafikus.")

uploaded = st.file_uploader("Ielādē Excel (.xlsx)", type=["xlsx"])

def pick_first_existing(cols, preferred):
    """Atrod pirmo kolonnu, kas eksistē; ja neviena, atgriež None."""
    for c in preferred:
        if c in cols:
            return c
    return None

if uploaded is not None:
    # 1) Nolasa Excel (pirmo lapu)
    df = pd.read_excel(uploaded)

    st.subheader("Datu priekšskatījums")
    st.dataframe(df.head(50), use_container_width=True)

    if df.empty:
        st.error("Fails ielādējās, bet tabula ir tukša.")
        st.stop()

    # 2) Atrod skaitliskās un kategoriskās kolonnas
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = df.select_dtypes(exclude="number").columns.tolist()

    st.write(f"Skaitliskās kolonnas: {numeric_cols}")
    st.write(f"Kategoriskās/teksta kolonnas: {cat_cols}")

    if not numeric_cols or not cat_cols:
        st.warning("Lai uztaisītu pivot un grafikus, vajag vismaz 1 skaitlisku un 1 kategorisku kolonnu.")
        st.stop()

    # 3) Pivot izvēles (ar defaultiem)
    st.subheader("Pivot tabula")
    row_col = st.selectbox("Rindu dimensija (group by)", cat_cols, index=0)
    value_col = st.selectbox("Vērtība (sum/avg)", numeric_cols, index=0)
    agg = st.selectbox("Agregācija", ["sum", "mean", "count"], index=0)

    if agg == "sum":
        pivot = pd.pivot_table(df, index=row_col, values=value_col, aggfunc="sum").sort_values(by=value_col, ascending=False)
    elif agg == "mean":
        pivot = pd.pivot_table(df, index=row_col, values=value_col, aggfunc="mean").sort_values(by=value_col, ascending=False)
    else:
        pivot = pd.pivot_table(df, index=row_col, values=value_col, aggfunc="count").sort_values(by=value_col, ascending=False)

    st.dataframe(pivot.head(30), use_container_width=True)

    # 4) 2 grafiki (automātiski no izvēlēm)
    st.subheader("Grafiki")

    col1, col2 = st.columns(2)

    # Bar chart no pivot (TOP 15)
    with col1:
        st.write("Stabiņu grafiks (Top 15 pēc pivot)")
        pivot_reset = pivot.reset_index().head(15)
        fig_bar = px.bar(pivot_reset, x=row_col, y=value_col, title=f"{agg}({value_col}) pēc {row_col}")
        st.plotly_chart(fig_bar, use_container_width=True)

    # Histogramma skaitliskajai kolonnai
    with col2:
        st.write("Histogramma (vērtību sadalījums)")
        fig_hist = px.histogram(df, x=value_col, nbins=30, title=f"{value_col} sadalījums")
        st.plotly_chart(fig_hist, use_container_width=True)

    # 5) Lejupielāde pivot kā CSV
    st.subheader("Lejupielāde")
    csv = pivot.reset_index().to_csv(index=False).encode("utf-8")
    st.download_button(
        "Lejupielādēt pivot kā CSV",
        data=csv,
        file_name="pivot.csv",
        mime="text/csv",
    )

else:
    st.info("Ielādē Excel failu, lai sāktu.")

