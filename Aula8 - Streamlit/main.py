import streamlit as st
from imc_utils import calcular_imc, classificar_imc

st.title("Calculadora de IMC")
peso = st.number_input("Digite seu peso (kg)", min_value=0.0, step=0.1)
altura = st.number_input("Digite sua altura (m)", min_value=0.0, step=0.01)

if st.button("Calcular IMC"):
    imc = calcular_imc(peso, altura)
    st.write(f"Seu IMC é: {imc}")
    if isinstance(imc, float):
        classificacao = classificar_imc(imc)
        if classificacao == "Abaixo do peso":
            st.warning(f"Classificação: {classificacao}")
        elif classificacao == "Peso normal":
            st.success(f"Classificação: {classificacao}")
        elif classificacao == "Sobrepeso":
            st.warning(f"Classificação: {classificacao}")
        else:
            st.error(f"Classificação: {classificacao}")