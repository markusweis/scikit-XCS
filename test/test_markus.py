import unittest
import numpy as np
from skXCS.StringEnumerator import StringEnumerator
from skXCS.XCS import XCS
import os

THIS_DIR = os.path.dirname(os.path.abspath("test_eLCS.py"))
if THIS_DIR[-4:] == 'test': #Patch that ensures testing from Scikit not test directory
    THIS_DIR = THIS_DIR[:-5]



class test_markus(unittest.TestCase):

    def testInverseVariance(self):
        dataPath = os.path.join(THIS_DIR, "test/DataSets/Real/Multiplexer6Modified.csv")
        converter = StringEnumerator(dataPath,"Class")
        headers, classLabel, dataFeatures, dataPhenotypes = converter.get_params()
        clf = XCS(learning_iterations=1000,N=500,nu=10, use_inverse_varinance=True, p_explore=0.5   )
        clf.fit(dataFeatures,dataPhenotypes)
        answer = 0.894
        score = clf.get_final_training_accuracy()
        clf.printFitness()
        clf.printGatingParams()
        print("#####################################\n6 Bit 1000 Iter: "+str(score))
        #self.assertTrue(self.approxEqualOrBetter(0.2, score, answer, True))

    def testPredictInvVar(self):
        dataPath = os.path.join(THIS_DIR, "test/DataSets/Real/Multiplexer6Modified.csv")
        converter = StringEnumerator(dataPath,"Class")
        headers, classLabel, dataFeatures, dataPhenotypes = converter.get_params()
        clf = XCS(learning_iterations=1000,N=500,nu=10, use_inverse_varinance=True, p_explore=0.5   )
        clf.fit(dataFeatures,dataPhenotypes)
        print("kkkkkkkkkkkkkkkkkkkkkkkkkkk")
        print(clf.predict(clf.env.formatData.savedRawTrainingData[0]))






        ###Util Functions###
    def approxEqual(self, threshold, comp, right):  # threshold is % tolerance
        return abs(abs(comp - right) / right) < threshold

    def approxEqualOrBetter(self, threshold, comp, right,
                            better):  # better is False when better is less, True when better is greater
        if not better:
            if self.approxEqual(threshold, comp, right) or comp < right:
                return True
            return False
        else:
            if self.approxEqual(threshold, comp, right) or comp > right:
                return True
            return False


