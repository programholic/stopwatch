import streamlit as st
import time

st.set_page_config(page_title="Cronómetro", layout="centered")

st.title("⏱️ Cronómetro estilo PyQt en Streamlit")

# Inicializar el estado
if "running" not in st.session_state:
    st.session_state.running = False
    st.session_state.start_time = 0.0
    st.session_state.elapsed = 0.0

# Función para formatear tiempo
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    centisec = int((seconds * 100) % 100)
    return f"{hours:02}:{minutes:02}:{secs:02}.{centisec:02}"

# Botones
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("▶️ Start"):
        if not st.session_state.running:
            st.session_state.running = True
            st.session_state.start_time = time.time() - st.session_state.elapsed

with col2:
    if st.button("⏹️ Stop"):
        if st.session_state.running:
            st.session_state.elapsed = time.time() - st.session_state.start_time
            st.session_state.running = False

with col3:
    if st.button("🔄 Reset"):
        st.session_state.running = False
        st.session_state.start_time = 0.0
        st.session_state.elapsed = 0.0

# Mostrar tiempo actual
if st.session_state.running:
    current_time = time.time() - st.session_state.start_time
else:
    current_time = st.session_state.elapsed

# Estilo y visualización
st.markdown(
    f"""
    <div style='text-align: center; padding: 40px; font-size: 100px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
                font-family: Calibri; font-weight: bold;'>
        {format_time(current_time)}
    </div>
    """,
    unsafe_allow_html=True
)

# Refrescar cada 100ms si está corriendo
if st.session_state.running:
    time.sleep(0.1)
    st.experimental_rerun()
