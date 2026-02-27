import streamlit as st

# simulador de notas

st.title("Simulador de Notas")
nota1 = st.number_input("Nota 1", min_value=0.0, max_value=10.0, step=0.1)
nota2 = st.number_input("Nota 2", min_value=0.0, max_value=10.0, step=0.1)
nota3 = st.number_input("Nota 3", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Calcular Média"):
    media = (nota1 + nota2 + nota3) / 3
    st.write(f"A média é: {media:.2f}")
    if media >= 7.0:
        st.success("Aprovado!")
    elif media >= 5.0:
        st.warning("Recuperação!")
    else:
        st.error("Reprovado!")