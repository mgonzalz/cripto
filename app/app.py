import streamlit as st
import pandas as pd
from src.attack_simulator import DiscreteLogAttack
from src.plot_results import AttackPlotter

st.set_page_config(layout="wide")
st.title("🔐 Comparador de Métodos de Ataque en DSA.")

bit_sizes = st.multiselect("Selecciona tamaños de bits para analizar:", [12, 16, 20, 24, 28], default=[12, 16, 20])

if st.button("Ejecutar Análisis."):
    results_brute = {"primitive": [], "non_primitive": []}
    results_bsgs = {"primitive": [], "non_primitive": []}

    with st.spinner("Ejecutando ataques..."):
        for bits in bit_sizes:
            attack = DiscreteLogAttack(bits)
            results = attack.run_attack()

            results_brute["primitive"].append(results["brute_primitive"])
            results_brute["non_primitive"].append(results["brute_non_primitive"])
            results_bsgs["primitive"].append(results["bsgs_primitive"])
            results_bsgs["non_primitive"].append(results["bsgs_non_primitive"])

    df = pd.DataFrame({
        "Bits": bit_sizes,
        "Brute Force - Primitiva": results_brute["primitive"],
        "Brute Force - No Primitiva": results_brute["non_primitive"],
        "BSGS - Primitiva": results_bsgs["primitive"],
        "BSGS - No Primitiva": results_bsgs["non_primitive"],
    })
    
    st.dataframe(df)
    
    st.subheader("**Visualización de Resultados.**")
    AttackPlotter.plot_results(bit_sizes, results_brute, results_bsgs)

    st.success("Análisis completado.")
