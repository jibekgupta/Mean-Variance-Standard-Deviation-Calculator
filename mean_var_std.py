import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    calculations = {
        'mean': [],
        'variance':[],
        'standard deviation': [],
        'max': [],
        'min':[],
        'sum': []
    }

    # converting the list to a 3x3 numpy array
    array = np.array(list).reshape(3,3)

    # calculating along axis 0 (columns)
    calculations['mean'].append(np.mean(array, axis=0).tolist())
    calculations['variance'].append(np.var(array, axis=0).tolist())
    calculations['standard deviation'].append(np.std(array, axis=0).tolist())
    calculations['max'].append(np.max(array, axis=0).tolist())
    calculations['min'].append(np.min(array, axis=0).tolist())
    calculations['sum'].append(np.sum(array, axis=0).tolist())

    # calculating along axis 1 (rows)
    calculations['mean'].append(np.mean(array, axis=1).tolist())
    calculations['variance'].append(np.var(array, axis=1).tolist())
    calculations['standard deviation'].append(np.std(array, axis=1).tolist())
    calculations['max'].append(np.max(array, axis=1).tolist())
    calculations['min'].append(np.min(array, axis=1).tolist())
    calculations['sum'].append(np.sum(array, axis=1).tolist())

    # calculating for the flattened array
    calculations['mean'].append(np.mean(array).item())
    calculations['variance'].append(np.var(array).item())
    calculations['standard deviation'].append(np.std(array).item())
    calculations['max'].append(np.max(array).item())
    calculations['min'].append(np.min(array).item())
    calculations['sum'].append(np.sum(array).item())


    return calculations