########################################################################
###  Jeffrey Scarmazzi
###  Fall 2016, GEOG 415 - Selected Problems
########################################################################

import csv
from collections import Counter

def subjectDisplay(subject):
    
    print '*' * 75
    print 'Subject ID: ', subject.subjectID
    print '*' * 75
    print 'DTN: ', subject.t1.DTN, '\t', subject.t2.DTN 
    print '-' * 75
    print 'DTO : ', subject.t1.DTO, '\t', subject.t2.DTO
    print '-' * 75
    print 'INT_PERC: ', subject.t1.INT_PERC, '\t', subject.t2.INT_PERC
    print '-' * 75
    print 'CS_RANGE: ', subject.t1.CS_RANGE, '\t', subject.t2.CS_RANGE
    print '-' * 75
    print 'R1_NAME: ', subject.t1.R1_NAME, '\t', subject.t2.R1_NAME
    print '-' * 75
    print 'R1_TAX: ', subject.t1.R1_TAX, '\t', subject.t2.R1_TAX
    print '-' * 75
    print 'R1_INT_COUNT: ', subject.t1.R1_INT_COUNT, '\t', subject.t2.R1_INT_COUNT
    print '-' * 75
    print 'SUBG_COUNT: ', subject.t1.SUBG_COUNT, '\t', subject.t2.SUBG_COUNT
    print '-' * 75
    print 'Config_A: ', subject.t1.ConfigA, '\t', subject.t2.ConfigA
    print '-' * 75
    print 'Config_B: ', subject.t1.ConfigB, '\t', subject.t2.ConfigB
    print '-' * 75
    print 'ConfigurationID: ', subject.t1.ConfigurationID, '\t', subject.t2.ConfigurationID
    print '-' * 75
    print '\n'

def csvGen(outTable):
    
    writer = csv.writer(open(outTable, "wb"), delimiter=",")
    
    writer.writerow(['Subject', \
                     't1_DTN', \
                     't1_DTO', \
                     't1_INT_PERC', \
                     't1_CS_RANGE', \
                     't1_R1_NAME', \
                     't1_R1_TAX', \
                     't1_SUBG_COUNT', \
                     't1_R1_INT_COUNT', \
                     't1_ConfigA', \
                     't1_ConfigB', \
                     't1_ConfigurationID', \
                     't2_DTN', \
                     't2_DTO', \
                     't2_INT_PERC', \
                     't2_CS_RANGE', \
                     't2_R1_NAME', \
                     't2_R1_TAX', \
                     't2_SUBG_COUNT', \
                     't2_R1_INT_COUNT', \
                     't2_ConfigA', \
                     't2_ConfigB', \
                     't2_ConfigurationID' \
                     ])
    return writer

def csvWrite(writer, subject):
    
    rowValues = []
    
    rowValues.append(subject.subjectID)
    # T1 
    rowValues.append(subject.t1.DTN)
    rowValues.append(subject.t1.DTO)
    rowValues.append(subject.t1.INT_PERC)
    rowValues.append(subject.t1.CS_RANGE)
    rowValues.append(subject.t1.R1_NAME)
    rowValues.append(subject.t1.R1_TAX)
    rowValues.append(subject.t1.SUBG_COUNT)
    rowValues.append(subject.t1.R1_INT_COUNT)
    rowValues.append(subject.t1.ConfigA)
    rowValues.append(subject.t1.ConfigB)
    rowValues.append(subject.t1.ConfigurationID)
    
    # T2 
    rowValues.append(subject.t2.DTN)
    rowValues.append(subject.t2.DTO)
    rowValues.append(subject.t2.INT_PERC)
    rowValues.append(subject.t2.CS_RANGE)
    rowValues.append(subject.t2.R1_NAME)
    rowValues.append(subject.t2.R1_TAX)
    rowValues.append(subject.t2.SUBG_COUNT)
    rowValues.append(subject.t2.R1_INT_COUNT)
    rowValues.append(subject.t2.ConfigA)
    rowValues.append(subject.t2.ConfigB)
    rowValues.append(subject.t2.ConfigurationID)

    writer.writerow(rowValues)

def r1Logging(runList):

    print 'R1 Has No Intersection @ T1 & T2'
    
    t1_r1Yes = 0
    t1_r1No = 0
    t2_r1Yes = 0
    t2_r1No = 0
    
    for subject in runList:
        if subject.t1.R1_INT_COUNT == 0:
            t1_r1No += 1
        else:
            t1_r1Yes +=1        
    for subject in runList:
        if subject.t2.R1_INT_COUNT == 0:
            t2_r1No += 1
        else:
            t2_r1Yes +=1
            
    print 'Yes: ', t1_r1Yes, t2_r1Yes
    print 'No: ', t1_r1No, t2_r1No
    print '*' * 50
    print '*' * 50

def configLogging(runList):

    ##
    # Checking For Unique Configuration IDs
    ##
    t1_IDs = []
    t2_IDs = []
    for subject in runList:
        if subject.t1.ConfigurationID not in t1_IDs and subject.t1.R1_INT_COUNT != 0:
            t1_IDs.append(subject.t1.ConfigurationID)
        else:
            pass
        if subject.t2.ConfigurationID not in t2_IDs and subject.t2.R1_INT_COUNT != 0:
            t2_IDs.append(subject.t2.ConfigurationID)
        else:
            pass
        
    t1_IDs.sort()
    t2_IDs.sort()
    
    print 'T1 ConfigurationIDs: ', len(t1_IDs)
    print t1_IDs
    print 'T2 ConfigurationIDs: ', len(t2_IDs)
    print t2_IDs

    ##
    # Counting Configuration IDs
    ##
    t1ID = []
    t2ID = []
    for subject in runList:
        t1ID.append(subject.t1.ConfigurationID)
        t2ID.append(subject.t2.ConfigurationID)
        
    t1cnt = Counter()
    for configID in t1ID:
        t1cnt[configID] += 1
    t2cnt = Counter()
    for configID in t2ID:
        t2cnt[configID] += 1

    print 'T1'
    print '*' * 50
    for key, value in t1cnt.items():
        print key, ':', value
    print 'T2'
    print '*' * 50
    for key, value in t2cnt.items():
        print key, ':', value

    print '*' * 50
    print '*' * 50

    ##
    # Checking Subjects with Fine Configuration Change
    ##
    subChange = []
    subSame = []
    for subject in runList:
        if subject.t1.ConfigurationID != subject.t2.ConfigurationID:
            subChange.append(subject.t2.R1_NAME)
        else:
            subSame.append(subject.t2.R1_NAME)

    print 'Changed: ', len(subChange)
    print 'Same: ', len(subSame)
    
    print '*' * 50
    print '*' * 50

    ##
    # Checking R1_NAME Counts
    ##
    
    changeCnt = Counter()
    for social in subChange:
        changeCnt[social] += 1
    sameCnt = Counter()
    for social in subSame:
        sameCnt[social] += 1

    for key, value in changeCnt.items():
        print key, value
    print '-' * 50
    for key,value in sameCnt.items():
        print key, value

    ##
    # Checking Subjects with Fine Configuration Change
    ##
    subChange = []
    subSame = []
    for subject in runList:
        if subject.t1.ConfigurationID != subject.t2.ConfigurationID:
            subChange.append(subject.t2.R1_TAX)
        else:
            subSame.append(subject.t2.R1_TAX)
    
    print '*' * 50
    print '*' * 50

    ##
    # Checking Taxonomy Change
    ##
    
    changeCnt = Counter()
    for tax in subChange:
        changeCnt[tax] += 1
    sameCnt = Counter()
    for tax in subSame:
        sameCnt[tax] += 1

    print '1 = Relational, 2 = Collective'

    print 'Change'
    for key, value in changeCnt.items():
        print key, value
    print 'No Change'
    for key,value in sameCnt.items():
        print key, value


    



    
    







 
