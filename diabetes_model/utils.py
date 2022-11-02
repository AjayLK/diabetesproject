import pickle
import json
import pandas as pd
import numpy as np
import config


class DiabetesDisease():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age

    def load_file(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.diabetes_model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)


    def get_predicted_disease(self):
        self.load_file()  # calling load_file method to get

        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.Glucose
        array[1] = self.BloodPressure
        array[2] = self.SkinThickness
        array[3] = self.Insulin
        array[4] = self.BMI
        array[5] = self.DiabetesPedigreeFunction
        array[6] = self.Age

        print("Test Array -->\n",array)
        predicted_disease = self.diabetes_model.predict([array])[0]
        return predicted_disease





if __name__ == "__main__":

    Glucose = 170
    BloodPressure= 60
    SkinThickness = 40
    Insulin =1.5
    BMI = 22.5
    DiabetesPedigreeFunction = 0.62
    Age = 45

    dd = DiabetesDisease(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    disease = dd.get_predicted_disease()
    print()
    print(f"predicted diabetes disease patients {disease}")
    # if disease == 1:
    #     print('yes patient has a heart disease')
    # else:
    #     print('patient has not a heart disease')

