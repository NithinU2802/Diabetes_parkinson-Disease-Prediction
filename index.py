import pickle
import streamlit as slt
from streamlit_option_menu import option_menu


# loading saved models

diabeties_model = pickle.load(
    open('Trained_Model/Diabetes_Model.sav', 'rb'))

parkinson_model = pickle.load(open('Trained_Model/Parkinsons_Model.sav', 'rb'))


# slidebar navigation

with slt.sidebar:
    selected = option_menu('Diabetes and Parkinsons Prediction System',

                           ['Diabetes Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    slt.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = slt.columns(3)

    with col1:
        Pregnancies = slt.text_input('Number of Pregnancies')

    with col2:
        Glucose = slt.text_input('Glucose Level')

    with col3:
        BloodPressure = slt.text_input('Blood Pressure value')

    with col1:
        SkinThickness = slt.text_input('Skin Thickness value')

    with col2:
        Insulin = slt.text_input('Insulin Level')

    with col3:
        BMI = slt.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = slt.text_input(
            'Diabetes Pedigree Function value')

    with col2:
        Age = slt.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if slt.button('Diabetes Test Result'):
        diab_prediction = diabeties_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    slt.success(diab_diagnosis)

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    # page title
    slt.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = slt.columns(5)

    with col1:
        fo = slt.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = slt.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = slt.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = slt.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = slt.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = slt.text_input('MDVP:RAP')

    with col2:
        PPQ = slt.text_input('MDVP:PPQ')

    with col3:
        DDP = slt.text_input('Jitter:DDP')

    with col4:
        Shimmer = slt.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = slt.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = slt.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = slt.text_input('Shimmer:APQ5')

    with col3:
        APQ = slt.text_input('MDVP:APQ')

    with col4:
        DDA = slt.text_input('Shimmer:DDA')

    with col5:
        NHR = slt.text_input('NHR')

    with col1:
        HNR = slt.text_input('HNR')

    with col2:
        RPDE = slt.text_input('RPDE')

    with col3:
        DFA = slt.text_input('DFA')

    with col4:
        spread1 = slt.text_input('spread1')

    with col5:
        spread2 = slt.text_input('spread2')

    with col1:
        D2 = slt.text_input('D2')

    with col2:
        PPE = slt.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if slt.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                          Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                          DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    slt.success(parkinsons_diagnosis)


hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}

footer{
    visibility:visible;
}

footer:after{
    diplay:block;
    position:relative;
    color:tomato;

}

"""
slt.markdown(hide_menu, unsafe_allow_html=True)
