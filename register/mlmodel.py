import numpy as np
import pandas as pd
import os
cwd = os.getcwd()

class mlmodelclass():

    def predict_salary(self,exp):
        exp_list = []
        exp_list.append(exp)
        
        dataset = pd.read_csv(cwd+'/register/Salary_Data.csv')
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, 1].values

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

        from sklearn.linear_model import LinearRegression
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)

        a = np.array(exp_list)
        Salary_pred = [regressor.predict(a.reshape(-1,1))]
        print( "====> ",Salary_pred)

        return Salary_pred
