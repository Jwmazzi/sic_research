########################################################################
###  Jeffrey Scarmazzi
###  Fall 2016, GEOG 415 - Selected Problems
########################################################################

class Subject:
    def __init__(self, subjectID):
        self.subjectID = subjectID
        self.t1 = self.T1()
        self.t2 = self.T2()

    class T1:
        def __init__(self):

            self.DTN = 0
            self.DTO = 0
            self.INT_PERC = 0.0
            self.CS_RANGE = 0
            
            self.SUBG_COUNT = 0
            
            self.R1_NAME = 0
            self.R1_TAX = 0
            self.R1_INT_COUNT = 0

            self.ConfigA = 0
            self.ConfigB = 0
            self.ConfigurationID = None

    class T2:
        def __init__(self):
            
            self.DTN = 0
            self.DTO = 0
            self.INT_PERC = 0.0
            self.CS_RANGE = 0
            
            self.SUBG_COUNT = 0

            self.R1_NAME = 0
            self.R1_TAX = 0
            self.R1_INT_COUNT = 0

            self.ConfigA = 0
            self.ConfigB = 0
            self.ConfigurationID = None
