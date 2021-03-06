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
        dataPath = os.path.join(THIS_DIR, "test/DataSets/Real/Multiplexer11.csv")
        converter = StringEnumerator(dataPath,"class")
        headers, classLabel, dataFeatures, dataPhenotypes = converter.get_params()
        clf = XCS(learning_iterations=5000, N=1000, mixing_method="inv-var-only-mixing")
        clf.fit(dataFeatures,dataPhenotypes)
        answer = 0.894
        score = clf.get_final_training_accuracy()
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

    def testNew(self):
        #Use StringEnumerator to gather data
        converter = StringEnumerator("test/DataSets/Real/Multiplexer11.csv","class")
        headers,actionLabel,dataFeatures,dataActions = converter.get_params()

        #Shuffle data
        formatted = np.insert(dataFeatures,dataFeatures.shape[1],dataActions,1)
        np.random.shuffle(formatted)
        dataFeatures = np.delete(formatted,-1,axis=1)
        dataActions = formatted[:,-1]

        #Initialize and train model

        clf_inv_var = XCS(learning_iterations=1000, N=200, use_inverse_varinance=True)
        clf_inv_var.fit(dataFeatures, dataActions)
        breakpoint()




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


