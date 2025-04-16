import streamlit as st
import pandas as pd
import requests
import google.generativeai as genai

try:
    baseUrl = "https://raw.githubusercontent.com/cellehcim/tales-api/main/data.json"
    response = requests.get(baseUrl)
    data = response.json()
    victorsDict = data["victors"]
    
    key = st.secrets["key"]
    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    names = [f"{v['first_name']} {v['last_name']}" for v in victorsDict.values()]
    
    tribute1 = st.selectbox("Choose Tribute 1", names)
    tribute2 = st.selectbox("Choose Tribute 2", names)
    
    def get_stats(name):
        for v in victorsDict.values():
            full_name = f"{v['first_name']} {v['last_name']}"
            if full_name == name:
                return {"name": full_name, "kills": len(v["known_kills"]), "injuries": v["sustained_injuries"] or "None", "weapon": v["weapon_of_choice"]}
    
    t1 = get_stats(tribute1)
    t2 = get_stats(tribute2)
    
    battle_prompt = (
        f"Simulate a Hunger Games battle between {t1['name']} and {t2['name']}. "
        f"{t1['name']} has {t1['kills']} kills, injuries: {t1['injuries']}, weapon: {t1['weapon']}. "
        f"{t2['name']} has {t2['kills']} kills, injuries: {t2['injuries']}, weapon: {t2['weapon']}. "
        "Who would win and why? Describe the battle in detail."
    )
    
    if st.button("Simulate Battle"):
        with st.spinner("Fighting in the arena... 🔥"):
            response = model.generate_content(battle_prompt)
            st.markdown(response.text)

except:
    print("En error ocurred")
    

