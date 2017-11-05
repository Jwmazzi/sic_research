def subjectDisplay(subject):
    
    print '*' * 75
    print 'Subject ID: ', subject.subjectID
    print '*' * 75
    print 'Time One'
    print 'Group Configuration Properties'
    print '*' * 75
    print 'DTN: ', subject.t1.G_DTN 
    print '-' * 75
    print 'DTO : ', subject.t1.G_DTO 
    print '-' * 75
    print 'INT_PERC: ', subject.t1.G_INT_PERC
    print '-' * 75
    print 'SUBG_COUNT: ', subject.t1.SUBG_COUNT
    print '*' * 75
    print 'Time Two'
    print 'Group Configuration Properties'
    print '*' * 75
    print 'DTN: ', subject.t2.G_DTN 
    print '-' * 75
    print 'DTO : ', subject.t2.G_DTO 
    print '-' * 75
    print 'INT_PERC: ', subject.t2.G_INT_PERC
    print '-' * 75
    print 'SUBG_COUNT: ', subject.t2.SUBG_COUNT
    print '*' * 75
    print '\n'