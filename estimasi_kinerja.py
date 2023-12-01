import pickle
import streamlit as st

model = pickle.load(open('estimasi_kinerja.sav', 'rb'))

st.title('Estimasi Kinerja')

HoursStudied = st.number_input('Input Jam Belajar')
PreviousScores = st.number_input('Input Nilai Sebelumnya')
SleepHours = st.number_input('Input Jam Tidur')
SampleQuestionPapersPracticed = st.number_input('Input Jumlah Soal Latihan yang sudah dikerjakan')

predict = ''

if st.button('Estimasi Kinerja'):
    predict = model.predict([[HoursStudied, PreviousScores, SleepHours, SampleQuestionPapersPracticed]])

    st.write('Estimasi Kinerja: ', predict)