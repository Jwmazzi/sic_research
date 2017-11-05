from datetime import datetime

from subject import Subject
from gauntlet import genSubjectList
from util import *

def main():

    startTime = datetime.now()
    
    runList = genSubjectList('t2_circles')
 
    for subject in runList:
        
        subject = Subject(subject)
        subjectDisplay(subject)

    print 'Subject Creation: ', datetime.now() - startTime

if __name__ == "__main__":
    main()
