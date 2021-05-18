import json,pickle
import numpy as np
__locations = None
__data_columns = None
__model = None

# routine for estimated price by bhk ,bathroom
def get_estimated_price(location,sqft,bhk,bath):
    

    loc_index =  __data_columns.index(location.lower())
    

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index]  = 1

    return round(__model.predict([x])[0],2)


#load our json and pickle file
def load_saved_artifacts():
    print( "loading saved artifacts start .........")
    global __data_columns
    global __locations

    with open("E:/game/real state price pridication/BHP/server/artifacts/columns.json",'r') as f:
        __data_columns =  json.load(f)['data_columns']
        __locations = __data_columns[3:]
    
    global __model
    if __model is None:

        with open("E:/game/real state price pridication/BHP/server/artifacts/banglore_home_prices_model.pickle" ,'rb') as f:
            __model = pickle.load(f)
    
    print("loading the artifacts is done ..........")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    
    print(get_estimated_price('Vijayanagar',2000,6,6))
    print(get_estimated_price('Vijayanagar',1000,3,3))
    print(get_estimated_price('1st Phase JP Nagar',2000,6,6))
    print(get_estimated_price('1st JP Nagar',1000,3,3))
    
    print(get_estimated_price('Kalhalli',1000,3,3)) # other location
    print(get_estimated_price('Ejipura',1000,3,3)) # other location
