import streamlit as st

st.set_page_config(page_title="Notfall-Assistenzsystem", layout="centered")

st.title("🩺 Notfall-Assistenzsystem – Demo")

st.markdown("Diese Web-Demo zeigt eine vereinfachte Version des chirurgischen Notfall-Assistenzsystems.")

# Dummy login
st.subheader("🔐 Login (Demo-Zugang)")
user = st.text_input("Benutzername")
pw = st.text_input("Passwort", type="password")

if st.button("Einloggen"):
    if user in ["demo_az", "demo_oa"] and pw == "demo123":
        st.success(f"Willkommen, {user}")
        st.markdown("✅ Zugriff auf Notfallfunktionen freigeschaltet.")
        st.markdown("📝 Patientenübersicht, PDF-Export, Verlauf folgen in der Vollversion.")
    else:
        st.error("Login fehlgeschlagen. Testnutzer: demo_az / demo123")
