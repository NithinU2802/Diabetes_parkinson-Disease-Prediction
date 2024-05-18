import pickle
import streamlit as st
import pandas as pd

# Function to load the model
# @st.cache(allow_output_mutation=True)
def load_model(model_path):
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model
    except (EOFError, FileNotFoundError, ModuleNotFoundError) as e:
        st.error(f"Error loading model from {model_path}: {e}")
        return None

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
        return None

def validate_input(df, column, value):
    min_val = df[column].min()
    max_val = df[column].max()
    if value < min_val or value > max_val:
        st.error(f"The input value for {column} should be between {min_val} and {max_val}")
        return False
    return True

diabetes = load_data('Dataset/CSV_Files/diabetes.csv')
parkinson = load_data('Dataset/CSV_Files/parkinsons.csv')

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
    
    input_valid = True
    
    if not (Pregnancies and Glucose and BloodPressure and SkinThickness and Insulin and BMI and DiabetesPedigreeFunction and Age):
        st.warning("Please provide values for all input fields.")
    else:
        input_valid &= validate_input(diabetes, 'Pregnancies', float(Pregnancies))
        input_valid &= validate_input(diabetes, 'Glucose', float(Glucose))
        input_valid &= validate_input(diabetes, 'BloodPressure', float(BloodPressure))
        input_valid &= validate_input(diabetes, 'SkinThickness', float(SkinThickness))
        input_valid &= validate_input(diabetes, 'Insulin', float(Insulin))
        input_valid &= validate_input(diabetes, 'BMI', float(BMI))
        input_valid &= validate_input(diabetes, 'DiabetesPedigreeFunction', float(DiabetesPedigreeFunction))
        input_valid &= validate_input(diabetes, 'Age', float(Age))
    
    if(not input_valid):
        st.error("Is it readings from human...! Please provide valid input..?")
    else:
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
                st.error("Hey..! Fields are empty..?")
            

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
        
    input_valid=True
    
    if not (fo and fhi and flo and Jitter_percent and Jitter_Abs and RAP and PPQ and DDP and Shimmer and Shimmer_dB and APQ3 and APQ5 and APQ and DDA and NHR and HNR and RPDE and DFA and spread1 and spread2 and D2 and PPE):
        st.warning("Please provide values for all input fields.")
    else:
    
        input_valid &= validate_input(parkinson, 'MDVP:Fo(Hz)', float(fo))
        input_valid &= validate_input(parkinson, 'MDVP:Fhi(Hz)', float(fhi))
        input_valid &= validate_input(parkinson, 'MDVP:Flo(Hz)', float(flo))
        input_valid &= validate_input(parkinson, 'MDVP:Jitter(%)', float(Jitter_percent))
        input_valid &= validate_input(parkinson, 'MDVP:Jitter(Abs)', float(Jitter_Abs))
        input_valid &= validate_input(parkinson, 'MDVP:RAP', float(RAP))
        input_valid &= validate_input(parkinson, 'MDVP:PPQ', float(PPQ))
        input_valid &= validate_input(parkinson, 'Jitter:DDP', float(DDP))
        input_valid &= validate_input(parkinson, 'MDVP:Shimmer', float(Shimmer))
        input_valid &= validate_input(parkinson, 'MDVP:Shimmer(dB)', float(Shimmer_dB))
        input_valid &= validate_input(parkinson, 'Shimmer:APQ3', float(APQ3))
        input_valid &= validate_input(parkinson, 'Shimmer:APQ5', float(APQ5))
        input_valid &= validate_input(parkinson, 'MDVP:APQ', float(APQ))
        input_valid &= validate_input(parkinson, 'Shimmer:DDA', float(DDA))
        input_valid &= validate_input(parkinson, 'NHR', float(NHR))
        input_valid &= validate_input(parkinson, 'HNR', float(HNR))
        input_valid &= validate_input(parkinson, 'RPDE', float(RPDE))
        input_valid &= validate_input(parkinson, 'DFA', float(DFA))
        input_valid &= validate_input(parkinson, 'spread1', float(spread1))
        input_valid &= validate_input(parkinson, 'spread2', float(spread2))
        input_valid &= validate_input(parkinson, 'D2', float(D2))
        input_valid &= validate_input(parkinson, 'PPE', float(PPE))
    
    if not input_valid:
        st.error("Is it readings from human...! Please provide valid input to enable Test Result..?")
    
    else:
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
                st.error("Hey..! Fields are empty..?")
                

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
st.markdown(
    """
    <style>
    .stSelectbox > div > div > div {
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set background image from URL
set_bg_from_url(
    "https://img.freepik.com/free-photo/flat-lay-health-still-life-arrangement-with-copy-space_23-2148854064.jpg", opacity=0.875)