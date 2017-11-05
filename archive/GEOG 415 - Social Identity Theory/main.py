########################################################################
###  Jeffrey Scarmazzi
###  Fall 2016, GEOG 415 - Selected Problems
########################################################################

import random
from datetime import datetime

from subject import Subject
from gauntlet import *
from util import *

def main():

    startTime = datetime.now()

    outTable = r'C:\Users\jeffr_000\Desktop\Fall_2016\415\GEOG_415_Scarmazzi\Results\FinalRun_C.csv'
    writer = csvGen(outTable)

    ##
    # T1 = 134 Subjects, T2 = 133 Subjects
    ##
    subjectList = genSubjectList('t2_circles') 
    errList = []
    runList = []
    for subject in subjectList:
        
        subjectNumber = subject
        subject = Subject(subject)
        
        try:
            t1Generation(subject, 't1_circles')
            t2Generation(subject, 't2_circles')
            
        except Exception as e:
            errList.append(subjectNumber)
            print '#' * 75
            print 'Problem: ', e.args
            print '#' * 75

        subjectDisplay(subject)

        csvWrite(writer, subject)

        runList.append(subject)

    print 'Subject Creation: ', datetime.now() - startTime
    print 'Problem Subjects: ', len(errList), errList
    print '*' * 50
    print '*' * 50

    ##
    # Console Logging 
    ##
    r1Logging(runList)
    configLogging(runList)
 
def genSubjectList(targetTable):
    cur.execute('select distinct(subject) as subs from ' + targetTable + '')
    res = cur.fetchall()
    subs = list(res)
    subList = []
    for a in subs:
        for b in a:
            subjectID = int(b)
            subList.append(subjectID)

    ##
    # Subjest 130, 32, & (196 Not In T2) Only Reported 4 Identities
    ##
    cutList = [130, 32]
    for sub in cutList:
        subList.remove(sub)

    sampleList = random.sample(subList, 66)
    sampleList.sort()
    return sampleList

def t1Generation(subject, time):
    subjectID = str(subject.subjectID)
    
    subject.t1.DTN = DTN(subjectID, time)
    subject.t1.DTO = DTO(subjectID, time)

    subInt = INT_SUM(subjectID, time)
    subSur = CS_SUR(subjectID, time)
    subject.t1.INT_PERC = INT_PERC(subInt, subSur)

    subMin = CS_MIN(subjectID, time)
    subMax = CS_MAX(subjectID, time)
    subject.t1.CS_RANGE = CS_RANGE(subMin, subMax)
    
    subject.t1.SUBG_COUNT = SUBG_COUNT(subjectID, time)
    
    subject.t1.R1_NAME = R1_NAME(subjectID, time)
    subject.t1.R1_TAX = R1_TAX(subjectID, time)
    subject.t1.R1_INT_COUNT = R1_INT_COUNT(subjectID, time)

    subject.t1.ConfigA = subject.t1.SUBG_COUNT + subject.t1.R1_INT_COUNT
    subject.t1.ConfigB = subject.t1.SUBG_COUNT - subject.t1.R1_INT_COUNT
    subject.t1.ConfigurationID = str(subject.t1.ConfigA) + ',' + str(subject.t1.ConfigB)

def t2Generation(subject, time):
    subjectID = str(subject.subjectID)
    
    subject.t2.DTN = DTN(subjectID, time)
    subject.t2.DTO = DTO(subjectID, time)
    
    subInt = INT_SUM(subjectID, time)
    subSur = CS_SUR(subjectID, time)
    subject.t2.INT_PERC = INT_PERC(subInt, subSur)

    subMin = CS_MIN(subjectID, time)
    subMax = CS_MAX(subjectID, time)
    subject.t2.CS_RANGE = CS_RANGE(subMin, subMax)
    
    subject.t2.SUBG_COUNT = SUBG_COUNT(subjectID, time)
    
    subject.t2.R1_NAME = R1_NAME(subjectID, time)
    subject.t2.R1_TAX = R1_TAX(subjectID, time)
    subject.t2.R1_INT_COUNT = R1_INT_COUNT(subjectID, time)

    subject.t2.ConfigA = subject.t2.SUBG_COUNT + subject.t2.R1_INT_COUNT
    subject.t2.ConfigB = subject.t2.SUBG_COUNT - subject.t2.R1_INT_COUNT
    subject.t2.ConfigurationID = str(subject.t2.ConfigA) + ',' + str(subject.t2.ConfigB)
        
main()
