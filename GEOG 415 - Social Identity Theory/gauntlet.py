########################################################################
###  Jeffrey Scarmazzi
###  Fall 2016, GEOG 415 - Selected Problems
########################################################################

import psycopg2

conn = psycopg2.connect(dbname = 'SIT_Fall2016', host = 'localhost', port = 5432, user = 'postgres', password = 'postgres')
conn.autocommit = True
cur = conn.cursor()

def DTN(subject, time):
    cur.execute('''
                select avg(source.dist)
                from 
                (select distinct
                st_length(st_shortestline(''' + time + '''.geom, target.geom)) as dist
                from ''' + time + ''',

                (select *
                from ''' + time + '''
                where subject = ''' + subject + ''') as target

                where 
                ''' + time + '''.subject = ''' + subject + '''
                and
                ''' + time + '''.gid != target.gid
                order by dist asc) as source
                where dist != 0;
                ''')
    res = cur.fetchone()[0]
    if res == None:
        res = 0
    return res
    

def DTO(subject, time):
    cur.execute('''
                select avg(dist)
                from
                (select distinct st_length(st_shortestline(''' + time + '''.geom, originxy.geom)) as dist
                from ''' + time + ''', originxy
                where 
                subject = ''' + subject + '''
                order by dist asc) as target
                where dist != 0;
                ''')
    res = cur.fetchone()[0]
    if res == None:
        res = 0
    return res

def CS_MIN(subject, time):
    cur.execute('''
                select distinct min(round(st_area(''' + time + '''.geom)::numeric, 2)) as circle
                from ''' + time + '''
                where subject = ''' + subject + '''
                ''')
    res = cur.fetchone()[0]
    return res

def CS_MAX(subject, time):
    cur.execute('''
                select distinct max(round(st_area(''' + time + '''.geom)::numeric, 2)) as circle
                from ''' + time + '''
                where subject = ''' + subject + '''
                ''')
    res = cur.fetchone()[0]
    return res

def CS_RANGE(subMin, subMax):
    val =  abs(subMax - subMin)
    return val

def CS_SUR(subject, time):
    cur.execute('''
                select sum(st_area(''' + time + '''.geom)) as total_surface
                from ''' + time + '''
                where subject = ''' + subject + '''
                ''')
    res = cur.fetchone()[0]
    return float(res)

def INT_SUM(subject, time):
    cur.execute('''
                select sum(area)
                from
                (select distinct round(st_area(st_intersection(''' + time + '''.geom, target.geom))::numeric, 2) as area
                from ''' + time + ''', 
                (select *
                from ''' + time + '''
                where subject = ''' + subject + ''') as target
                where 
                st_intersects(''' + time + '''.geom, target.geom)
                and
                ''' + time + '''.gid != target.gid
                and ''' + time + '''.subject = ''' + subject + ''') as source
                ''')
    res = cur.fetchone()[0]
    if res == None:
        res = 0
    return float(res)

def INT_PERC(subInt, subSur):
    val = round(((subInt / subSur) * 100), 2)
    return val
    
def INT_COUNT(subject, time):
    cur.execute('''
                select distinct (count(*)/2)
                from ''' + time + ''',
                (select gid, geom
                from ''' + time + '''
                where subject = ''' +  subject + ''') as target
                where
                subject = ''' + subject + '''
                and
                st_intersects(''' + time + '''.geom, target.geom)
                and
                ''' + time + '''.gid != target.gid
                ''')
    res = cur.fetchone()[0]
    return res

def SUBG_COUNT(subject, time):
    cur.execute('''
                select count(set.recs)
                from
                (select st_dump(source.union_geom) as recs
                from
                (select st_union(geom) as union_geom
                from ''' + time + '''
                where
                subject = ''' +  subject + ''') as source) as set
                ''')
    res = cur.fetchone()[0]
    return res

def R1_NAME(subject, time):
    cur.execute('''
                select upper(social_id)
                from ''' + time + '''
                where
                rank = 1
                and
                subject = ''' +  subject + '''
                ''')
    res = cur.fetchone()[0]
    return res

def R1_TAX(subject, time):
    cur.execute('''
                select left(taxonomy, 1)
                from ''' + time + '''
                where
                rank = 1
                and
                subject = ''' +  subject + '''
                ''')
    res = cur.fetchone()[0]
    if res == '1' or  res == '2':
        res = 1
    else:
        res = 2
    return res

def R1_INT_COUNT(subject, time):
    cur.execute('''
                select source.subject, count(*) as int_count
                from ''' + time + ''', 

                (select subject, rank, taxonomy, social_id, ''' + time + '''.geom as geom
                from ''' + time + '''
                where
                rank = 1
                and
                subject = ''' +  subject + '''
                ) as source

                where 
                st_intersects(''' + time + '''.geom, source.geom)
                and
                source.subject = ''' + time + '''.subject
                and
                source.rank != ''' + time + '''.rank
                and
                ''' + time + '''.subject = ''' +  subject + '''
                group by source.subject
                ''')
    res = cur.fetchone()
    if res == None:
        res = 0
    else:
        res = res[1]
    return res
    
