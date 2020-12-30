"""
We will be Using Multilayer Perceptron for this Binary Classification
A Multilayer Perceptron is a feedforward Artificial Neural Network
"""

from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

"""
Steps to Creating the Neural Network Model:
1) Define the Model
2) Compile
3) Fit
4) Evaluate
5) Make Prediction
"""

# Loading the Dataset:
path = "Bike_Data.csv"
df = read_csv( path, header=None )

# Splitting the DataFrame into input and output columns
X, y = df.values[:, :-1], df.values[:, -1]

print( df.head() )

df.drop( "Start date", inplace=True, axis=1 )

print( df.head() )


# To make sure that all data



# Defining the Sequential Model
"""
The Sequential Model Involves defining a Sequential Class and adding
layers to the model one by one in a linear manner, from input to output.
Our network will have one hidden layer, with 10 nodes.
The output layer will have 1 node, to predict the class.
The expected input is a vector (n by 1 matrix) with number of
elements equal to num_features.

To add more hidden layers, just use:
model.add( Dense(x) ) 
Where x is the number of nodes in that hidden layer.
"""
num_features = 8
num_nodes_in_hidden_layer = 10
num_nodes_in_output_layer = 1

model = Sequential( )

model.add( Dense( num_nodes_in_hidden_layer, input_shape=(num_features,) ) )

model.add( Dense( num_nodes_in_output_layer ) )







"""

Add section for Visualising the Deep Learning Model
Add section for Pickling (Saving and Loading Model)

"""


