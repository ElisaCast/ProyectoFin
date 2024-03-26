import streamlit as st

st.set_page_config(
    page_title="Bienvenidos",
    page_icon="👋",
)

# Título principal centrado
st.markdown("<h2 style='text-align: center;color:blue;'>VARIABLES COMBINADAS </h2>", unsafe_allow_html=True)

# Tamaño de texto y alineación centrada
st.markdown("En el dataset se han generado ciertas variables para poder incluir aquellas que no tienen ninguna correlación con la variable objetivo. Las analizamos a continuación.")
# Descripción de variables
st.markdown("<h2 style='font-size: 24px;color:#6fa8dc;'>TENURE-AGE: TENURE ⇄ AGE</h2>", unsafe_allow_html=True)

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)

# Mostrar imagen debajo del título
imagen_url = "DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/Tenure-age.jpg"
st.image(imagen_url,  width=1000, use_column_width="always")

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)

# Lista de variables en formato HTML
st.markdown("""
<h2 style='font-size: 20px;'>Variables Analizadas</h2>
<ul>
    <li>Tenure-Age: Variable que relaciona la antigüedad con la edad. Tenure/Age</li>
    <li>Tenure*Age: Similar a Tenure-Age, pero representa el producto de la antigüedad y la edad.</li>
    <li>Con esta combinación podemos incluir en el modelo la variable antigüedad (Tenure) que tenía inicialmente una correlación casi nula.</li>
</ul>
""", unsafe_allow_html=True)

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)

# Descripción de variables
st.markdown("<h2 style='font-size: 24px;color:#6fa8dc;'>MEM-NO-PRODUCTS: ISACTIVEMEMBERS ⇄ NUMOFPRODUCTS</h2>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Mostrar imagen debajo del título
imagen_url = "DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/Mem-no-products.jpg"
st.image(imagen_url, width=1000, use_column_width="always")

# Espaciado entre los nombres
st.markdown("<br>", unsafe_allow_html=True)

# Texto en formato HTML
st.markdown("""
<h2 style='font-size: 20px;'>Variables Analizadas</h2>
<ul>
    <li>Mem-No-Products: Variable que relaciona la variable miembro activo (IsActiveMember) con la variable Numero de productos financieros (NumOfProducts).</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Descripción de variables
st.markdown("<h2 style='font-size: 24px;color:#6fa8dc;'>CRED-BAL-SAL: CREDITSCORE ⇄ BALANCE ⇄ SALARY</h2>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Mostrar imagen debajo del título
imagen_url = "DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/Cred-Bal-sal.jpg"
st.image(imagen_url, width=1000, use_column_width="always")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style='font-size: 20px;'>Variables Analizadas</h2>
<ul>
    <li>Cred-Bal-Sal: Variable que relaciona la variable Credit Score con la variable Balance y el Salario estimado (Credit*Balance/Salary).</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Descripción de variables
st.markdown("<h2 style='font-size: 24px;color:#6fa8dc;'>BAL-SAL: BALANCE ⇄ SALARY</h2>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Mostrar imagen debajo del título
imagen_url = "DATA-SCIENCE-Y-MACHINE-LEARNING.jpg/Bal-sal.jpg"
st.image(imagen_url, width=1000, use_column_width="always")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style='font-size: 20px;'>Variables Analizadas</h2>
<ul>
    <li>Bal-Sal: Variable que relaciona la variable Balance y el Salario estimado (Balance/Salary).</li>
</ul>
""", unsafe_allow_html=True)