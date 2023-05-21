import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/kolla/Desktop/Folders/SELF PROJECTS/trained_model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
    


def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    st.sidebar.header('User Input Parameters')
    Pregnancies = st.sidebar.slider('Number of Pregnancies',0,10,0)
    Glucose = st.sidebar.slider('Glucose Level',50,180,100)
    BloodPressure = st.sidebar.slider('Blood Pressure value',50,120,80)
    SkinThickness = st.sidebar.slider('Skin Thickness value',0,50,0)
    Insulin = st.sidebar.slider('Insulin Level',0,1000,0)
    BMI = st.sidebar.slider('BMI value',18.5,50.5,25.5)
    DiabetesPedigreeFunction = st.sidebar.slider('Diabetes Pedigree Function value',0.000,0.999,0.000)
    Age = st.sidebar.slider('Age of the Person',20,80,20)
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()