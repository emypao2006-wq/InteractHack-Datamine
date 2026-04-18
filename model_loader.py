import numpy as np

def predict_dummy(features: list):
    """
    Simula una predicción. 
    Acepta una lista de valores y devuelve un valor numérico.
    """
    # Simulamos un procesamiento de ML: 
    # Convertimos a array de numpy (lo que hace Scikit-Learn internamente)
    data_array = np.array(features).reshape(1, -1)
    
    # Simulamos una salida de predicción
    return float(data_array.sum() * 1.5)
