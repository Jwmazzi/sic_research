import psycopg2

conn = psycopg2.connect(dbname = 'sic', host = 'localhost', port = 5432, user = 'postgres', password = 'postgres')
conn.autocommit = True
cur = conn.cursor()

def genSubjectList(targetTable):
    cur.execute('''
                select distinct(subject)
                from ''' + targetTable + '''
                where subject in (14, 47, 58, 62, 114)
                ''')
    res = cur.fetchall()
    subList = []
    for val in res:
        subList.append(val[0])
    subList.sort()
    return subList

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

def SUBG_GEOMS(subject, time):
    cur.execute('''
                select (st_dump(st_union(geom))).geom as geom
                from ''' + time + '''
                where
                subject = ''' + subject + '''
                ''')
    res = cur.fetchall()
    return res
