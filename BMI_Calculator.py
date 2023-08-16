#!/usr/bin/env python
# coding: utf-8

import streamlit as st
def BMI(berat_badan, tinggi_badan):
    BMI = berat_badan / ((tinggi_badan / 100) ** 2)
    rounded_BMI = round(BMI, 2)
    return float(rounded_BMI)

underweight = 'Kamu Kurus dan underweight, perbanyak protein dan mulai rutin makan (porsi kecil tapi sering)'
normal = 'Kamu Normal dan Berat badanmu Ideal, jaga pola hidup sehat dan pertahankan ini'
kegemukan = 'Kamu Kegemukan, turunkan berat badanmu ya, demi kesehatan'
obesitas = 'Kamu Obesitas, ayo olahraga dan atur pola makanmu'
obes_extreme = 'Kamu Obesitas berat, mulai olahraga sekarang, perkecil resiko terkena penyakit berbahaya'
def conditional_BMI(BMI):
    if BMI <= 18.5:
        return underweight
    elif 18.5 < BMI <= 24.9:
        return normal
    elif 25 < BMI <= 29.9:
        return kegemukan
    elif 30 < BMI <= 34.9:
        return obesitas
    else:
        return obes_extreme
        
def main():
    # buat header
    st.title("BMI Calculator Sederhana")
    st.image("https://aucklandweightlosssurgery.co.nz/wp-content/uploads/2016/03/BMI-Chart.jpg")
    # Buat layer
    col1, col2 = st.columns(2)
    berat_badan = col1.text_input('Masukan berat badanmu dalam (kg):')
    tinggi_badan = col2.text_input('Masukan tinggi badanmu dalam (cm):')
    # Logic for processing inputs, calculating BMI, and displaying results
    if berat_badan and tinggi_badan:
        berat_badan = int(berat_badan)
        tinggi_badan = int(tinggi_badan)
        
        # Calculate BMI
        calculated_BMI = BMI(berat_badan, tinggi_badan)
        st.write(f"Hasil BMI Kamu adalah = {calculated_BMI} ")
        
        if st.button('Cek Kondisi BMI Kamu:'):
            condition = conditional_BMI(calculated_BMI)
            st.write(condition)
        
if __name__ == "__main__":
    main()

