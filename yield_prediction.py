from geneticalgorithm import geneticalgorithm as ga
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

# Load dataset from CSV
data = pd.read_csv('reaction_data.csv').values

# Independent variables
X = data[:, :3]  # T, P, C
# Dependent variable
y = data[:, 3]   # Yield

# Fit regression model
model = LinearRegression()
model.fit(X, y)

# Define the fitness function using the regression model
def fitness_function(params):
    T, P, C = params
    yield_pred = model.predict([[T, P, C]])[0]
    return -yield_pred  # Negative because GA minimizes by default

# Define variable bounds: [min, max]
varbound = np.array([
    [min(data[:, 0]), max(data[:, 0])],  # Temperature
    [min(data[:, 1]), max(data[:, 1])],  # Pressure
    [min(data[:, 2]), max(data[:, 2])]   # Catalyst Concentration
])

# Initialize the genetic algorithm
algorithm = ga(
    function=fitness_function,
    dimension=3,
    variable_type='real',
    variable_boundaries=varbound
)

# Run the optimization
algorithm.run()

# Print the results
result = algorithm.output_dict
print("Optimal Parameters (T, P, C):", result['variable'])
print("Maximum Predicted Yield:", -result['function'])
