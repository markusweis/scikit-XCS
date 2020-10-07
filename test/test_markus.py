import unittest
import numpy as np
from skXCS.StringEnumerator import StringEnumerator
from skXCS.XCS import XCS

#Use StringEnumerator to gather data
converter = StringEnumerator("test/DataSets/Real/Multiplexer11.csv","class")
headers,actionLabel,dataFeatures,dataActions = converter.get_params()

#Initialize and train model
model = XCS(learning_iterations = 5000)
trainedModel = model.fit(dataFeatures,dataActions)

