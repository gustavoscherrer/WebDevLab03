import streamlit as st
import pandas as pd
import json
import requests

st.title("🏆 Hunger Games Victors Database")

baseUrl = "https://raw.githubusercontent.com/cellehcim/tales-api/main/data.json"
response = requests.get(baseUrl)
data = response.json()

victorsDict = data["victors"]
victorsList = []

for k, v in victorsDict.items():
    victorsList.append({"Name": f"{v['first_name']} {v['last_name']}", "Gender": v["gender"], "Age": v["age"], "District": v["district"], "Weapon": v["weapon_of_choice"], "Kills": len(v["known_kills"]), "Injuries": v["sustained_injuries"] or "None", "Alive": v["alive_by_the_end_of_mockingjay"]})

spreadsheet = pd.DataFrame(victorsList)

if "district" not in st.session_state:
    st.session_state["district"] = spreadsheet["District"].unique()[0]

if "alive" not in st.session_state:
    st.session_state["alive"] = "All"

with st.container(border = True):
    st.markdown("### 🔍 Filter Options")

    districtFilter = st.selectbox("Choose a District", sorted(spreadsheet["District"].unique()), key="district")
    aliveFilter = st.radio("Alive after Mockingjay?", ["All", "Yes", "No"], key="alive")

    filteredSpreadsheet = spreadsheet[spreadsheet["District"] == st.session_state["district"]]

    if st.session_state["alive"] == "Yes":
        filteredSpreadsheet = filteredSpreadsheet[filteredSpreadsheet["Alive"] == True]
    elif st.session_state["alive"] == "No":
        filteredSpreadsheet = filteredSpreadsheet[filteredSpreadsheet["Alive"] == False]

st.subheader(f"Victors from District {st.session_state['district']}")
st.dataframe(filteredSpreadsheet)

st.subheader("Top 10 Weapons in the Arena")
st.caption("x-axis: Weapon used | y-axis: Number of Victors")

weaponCounts = filteredSpreadsheet["Weapon"].value_counts()
battleMap = pd.DataFrame(weaponCounts)
battleMap.columns = ["Number of Victors"]
killChart = battleMap[:10]

st.bar_chart(killChart)
