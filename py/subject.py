from gauntlet import *

class Subject:
    def __init__(self, subjectID):
        
        self.subjectID = str(subjectID)
        
        self.t1 = self.GroupConfig(self.subjectID, 't1_circles')
        self.t2 = self.GroupConfig(self.subjectID, 't2_circles')

  
    class GroupConfig:
        def __init__(self, subjectID, time):

            self.G_DTN = DTN(subjectID, time)
            
            self.G_DTO = DTO(subjectID, time)
            
            intersection = INT_SUM(subjectID, time)
            surface = CS_SUR(subjectID, time)
            self.G_INT_PERC = INT_PERC(intersection, surface)

            self.SUBG_GEOMS = SUBG_GEOMS(subjectID, time)

            self.SUBG_COUNT = len(self.SUBG_GEOMS)

            self.SUBGROUPS = []

            class SubgroupConfig:   
                def __init__(self, ID):
                    
                    self.ID = ID

                    #self.S_DTN
                    #self.S_DTO
                    #self.S_INT_PERC

                    #self.IsPrimary
                    #self.IsAnchor
                    #self.Ranks
    
            def genSubgroups(self, time):
                
                for ID in range(self.SUBG_COUNT):
                    self.SUBGROUPS.append(SubgroupConfig(ID))
                    
            genSubgroups(self, time)
