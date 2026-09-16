import streamlit as st


def render_kpi_card(label: str, value, delta: float | None = None, icon: str = "📊"):
    """Une carte KPI unique : icône, libellé, valeur, variation optionnelle."""
    delta_html = ""
    if delta is not None:
        color = "#006A4E" if delta >= 0 else "#D21034"
        arrow = "↑" if delta >= 0 else "↓"
        delta_html = (
            f'<div class="tdi-kpi-delta" style="color:{color}">{arrow} {abs(delta):.1f} %</div>'
        )
    st.markdown(
        f"""
        <div class="tdi-kpi-card">
            <div class="tdi-kpi-icon">{icon}</div>
            <div class="tdi-kpi-label">{label}</div>
            <div class="tdi-kpi-value">{value if value is not None else "—"}</div>
            {delta_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_kpi_row(kpis: list[dict]):
    """kpis: liste de dicts {label, value, delta, icon}."""
    cols = st.columns(len(kpis))
    for col, kpi in zip(cols, kpis):
        with col:
            render_kpi_card(**kpi)
