import streamlit as st
import random

# App title
st.title("Værdiskabelse ved Outsourcing af Konsulentydelser")

# Beskrivelse
st.write("""
Indtast en konsulentydelse (f.eks. *motorskadebehandling*) og få et forslag til værdiskabelse samt en vurderingsscore.
""")

# Inputfelt
service = st.text_input("🔧 Indtast en serviceydelse:")

# Når brugeren har indtastet noget
if service:
    # Simuleret AI-genereret tekst
    value_proposition = f"""
Outsourcing af '{service}' kan give adgang til specialiseret ekspertise, reducere faste omkostninger og øge fleksibiliteten i driften.
Det muliggør også hurtigere skalering og forbedret kundeservice, hvis det implementeres korrekt.
"""

    # Simuleret score (til demo)
    score = round(random.uniform(6.5, 9.5), 1)

    # Vis resultat
    st.subheader("💡 Forslag til værdiskabelse:")
    st.write(value_proposition)

    st.subheader("📊 Vurderingsscore:")
    st.metric(label="Score (1-10)", value=score)
