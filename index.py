import pickle
import streamlit as st
from sklearn.ensemble import GradientBoostingClassifier

# Function to load the model
# @st.cache(allow_output_mutation=True)
def load_model(model_path):
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        st.success(f"Model loaded successfully: {model_path}")
        return model
    except (EOFError, FileNotFoundError, ModuleNotFoundError) as e:
        st.error(f"Error loading model from {model_path}: {e}")
        return None

# Load the models
try:
    diabetes_model = load_model('Trained_Model/Diabetes_Model.pkl')
    print("Diabetes model loaded successfully")
except (EOFError, FileNotFoundError) as e:
    print(f"Error loading diabetes model: {e}")
    st.stop()

try:
    parkinsons_model = load_model('Trained_Model/Parkinsons_Model.pkl')
    print("Parkinson's model loaded successfully")
except (EOFError, FileNotFoundError) as e:
    print(f"Error loading Parkinson's model: {e}")
    st.stop()
    

# Sidebar for navigation
selected = st.sidebar.selectbox(
    'Diabetes and Parkinsons Prediction System',
    ['Diabetes Prediction', 'Parkinsons Prediction']
)

# Title
st.title("Diabetes and Parkinsons Prediction System")

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.subheader('Diabetes Prediction')

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    # Code for Prediction
    diab_diagnosis = ''

    # Button for Prediction
    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        except ValueError:
            st.error("Please enter valid input values")

    st.success(diab_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.subheader("Parkinson's Disease Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # Code for Prediction
    parkinsons_diagnosis = ''

    # Button for Prediction
    if st.button("Parkinson's Test Result"):
        try:
            parkinsons_prediction = parkinsons_model.predict([[
                float(fo), float(fhi), float(flo), float(Jitter_percent),
                float(Jitter_Abs), float(RAP), float(PPQ), float(DDP),
                float(Shimmer), float(Shimmer_dB), float(APQ3), float(APQ5),
                float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE),
                float(DFA), float(spread1), float(spread2), float(D2), float(PPE)
            ]])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
        except ValueError:
            st.error("Please enter valid input values")

    st.success(parkinsons_diagnosis)

# Function to set background image
def set_bg_from_url(url, opacity=1):
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
        <a href="https://www.linkedin.com/in/nithinu" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn Logo" width="20" height="20" style="margin-right: 8px">
        </a>
            <p style="font-size:1.1rem;">
                Rights Reserved as Nithin U
                &nbsp;
            </p>
        <a href="https://github.com/nithinu2802" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub Logo" width="20" height="20">
        </a>
        </div>
       <b> <h1>PROJECT GUIDED BY Mrs. KALPANA V</h1></b>
        <h3>Developer Team</h3>
        <ul>
            <li>Muhilan P</li>
            <li>Nithin U</li>
            <li>Rohan Chakaravarthi V</li>
            <li>Sharan Shakthi G</li>
        </ul>
    </footer>
    """
    st.markdown(footer, unsafe_allow_html=True)

    # Set background image using HTML and CSS
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image from URL
set_bg_from_url(
    "https://img.freepik.com/free-photo/flat-lay-health-still-life-arrangement-with-copy-space_23-2148854064.jpg", opacity=0.875)