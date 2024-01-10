# Set the background color using set_page_config
st.set_page_config(
page_icon="🧾",
layout="wide", 
background_color="#ffffff"
)


import streamlit as st
import pandas as pd
import math 
import numpy as np


col1, col2, col3,col4,col5,col6 = st.columns([1,1,5,3,1,1])


with col3:
    st.text('')
    st.image("RADAMS.jpg") 
with col4:
    st.image("John H Logo .jpeg")

st.header('')

st.markdown("<h4 style='text-align: center;'>Risk calculator for the prediction of postoperative diplopia following orbital fracture repair in adults</h4>", unsafe_allow_html=True)
#st.header("Risk calculator for the prediction of postoperative enophthalmos")

st.header('')
st.write('**Age at injury (≥18)**')
age_input = st.number_input('Select one of the following', 18, 150)
#st.text("")
st.write('**Preoperative enophthalmos:**')
present_box1 = st.checkbox('Present',key = 1)
#st.text("")
st.write('**Preoperative periorbital swelling:**')
present_box2 = st.checkbox('Present', key =2)
st.write('<span style="font-size: smaller;">*Select present if periorbital swelling might block vision and prevent diplopia.*</span>', unsafe_allow_html=True)
#st.text("")
st.write('**Fracture of medial wall:**')
present_box3 = st.checkbox('Present', key =3)
#st.text("")
st.write('**Fracture size >2 cm² or >3 mm displacement:**')
present_box4 = st.checkbox('Present', key =4)
st.write('<span style="font-size: smaller;">*Select present if area of fracture defect is >2 cm² or fracture displacement is >3 mm. To calculate the **area of fracture defect**, multiply **length (cm)** by **width (cm)** of defect e.g., length on sagital CT scan by width on coronal CT scan. Use **displacement** if defect is not clearly defined or the measurement is complex.*</span>', unsafe_allow_html=True)
#st.text("")
st.write('**Repair of globe/other soft tissue:**')
present_box5 = st.checkbox('Yes', key =5)
st.write('<span style="font-size: smaller;">*Select yes if surgery might block vision and prevent diplopia.*</span>', unsafe_allow_html=True)
#st.text("")
st.write('**Fracture repair at >2 weeks from injury:**')
present_box6 = st.checkbox('Yes', key =6)




calculation = age_input * 0.021


if present_box1:
        calculation += 1 * 0.77

if present_box2:
        calculation += 1 * (-1.249)

if present_box3:
        calculation += 1 * 0.691

if present_box4:
        calculation += 1 * 1.266

if present_box5:
        calculation += 1 * (-0.871)

if present_box6:
        calculation += 1 * 0.536

calculation += (-3.185)


result = ( math.exp(calculation) / (math.exp(calculation) + 1) ) * 100

st.subheader('')

st.markdown(f"<h4>Risk (%) of postoperative diplopia = <span style='color:red'>{result:.2f}%</span></h4>", unsafe_allow_html=True)
