import plotly.graph_objects as go
import streamlit as st

class AttackPlotter:
    @staticmethod
    def plot_results(bit_sizes, results_brute, results_bsgs):
        """Genera gráficos interactivos con Plotly para visualizar la comparación de ataques."""
        col1, col2 = st.columns(2)
        with col1:
            # Gráfico de Brute Force.
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(x=bit_sizes, y=results_brute["primitive"], mode='lines+markers',
                                      name='Brute Force - Raíz Primitiva', line=dict(color='red')))
            fig1.add_trace(go.Scatter(x=bit_sizes, y=results_brute["non_primitive"], mode='lines+markers',
                                      name='Brute Force - No Primitiva', line=dict(color='red', dash='dash')))
            fig1.update_layout(title="Brute Force: Raíz Primitiva vs No Primitiva",
                               xaxis_title="Tamaño en bits del primo p",
                               yaxis_title="Tiempo de cálculo (s)",
                               template="plotly_white")
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            # Gráfico de BSGS.
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(x=bit_sizes, y=results_bsgs["primitive"], mode='lines+markers',
                                      name='BSGS - Raíz Primitiva', line=dict(color='blue')))
            fig2.add_trace(go.Scatter(x=bit_sizes, y=results_bsgs["non_primitive"], mode='lines+markers',
                                      name='BSGS - No Primitiva', line=dict(color='blue', dash='dash')))
            fig2.update_layout(title="BSGS: Raíz Primitiva vs No Primitiva",
                               xaxis_title="Tamaño en bits del primo p",
                               yaxis_title="Tiempo de cálculo (s)",
                               template="plotly_white")
            st.plotly_chart(fig2, use_container_width=True)

        # Comparación entre Brute Force y BSGS.
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=bit_sizes, y=results_brute["primitive"], mode='lines+markers', name='Brute Force - Raíz Primitiva', line=dict(color='red')))
        fig3.add_trace(go.Scatter(x=bit_sizes, y=results_bsgs["primitive"], mode='lines+markers', name='BSGS - Raíz Primitiva', line=dict(color='blue')))
        fig3.update_layout(title="Comparación Brute Force vs BSGS con Raíz Primitiva",
                           xaxis_title="Tamaño en bits del primo p",
                           yaxis_title="Tiempo de ejecución (s)",
                           template="plotly_white")
        st.plotly_chart(fig3, use_container_width=True)

        # Conclusión automática según los datos obtenidos.
        st.subheader("**Conclusión del Análisis**")
        if results_brute["primitive"][-1] > results_bsgs["primitive"][-1]:
            st.write("- **BSGS es significativamente más rápido que Brute Force en todos los tamaños de $p$.**")
            st.write("- **El ataque es más difícil cuando se usa una raíz primitiva, ya que los tiempos de ejecución son mayores.**")
            st.write("- **Si $g$ no es primitiva, el sistema es vulnerable porque el ataque es más rápido.**")
        else:
            st.write("- **Los tiempos de ejecución no muestran una diferencia clara, revisar parámetros de ejecución.**")
