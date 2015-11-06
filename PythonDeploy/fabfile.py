import os,time
from fabric.api import *
from fabric.contrib.files import exists


def vps():
    env.hosts = ['128.16.80.15']
    env.user = 'localuser'
    env.password = 'killer369'
    env.dbname = 'db1'
    env.dbuser = 'root'
    env.dbpass = None

def backup():
    require('hosts', provided_by=[vps])
    require('dbname')
    require('dbuser')
    require('dbpass')

 
    date = time.strftime('%Y%m%d%H%M%S')
    fname = '/tmp/%(database)s-backup-%(date)s.xml.gz' % {
        'database': env.dbname,
        'date': date,
    }

    if exists(fname):
        run('rm "%s"' % fname)

    run('mysqldump -u %(username)s %(database)s --xml | '
        'gzip > %(fname)s' % {'username': env.dbuser,
                              'database': env.dbname,
                              'fname': fname})
    get(fname, os.path.basename(fname))
    run('rm "%s"' % fname)
    
    
    run('sshpass -p "Ueb6tJK11" scp /home/localuser/deploy/%(sfile)s localuser@studvm47-p.cs.ucl.ac.uk:/home/localuser/%(sfile)s' % {'sfile': os.path.basename(fname)})

    
    

def vps1():
    env.hosts = ['localuser@studvm37-p.cs.ucl.ac.uk']
    env.user = 'localuser'
    env.password = 'killer369'
    

def transfer():
    run("scp /home/localuser/fabfile.pyc localuser@studvm47-p.cs.ucl.ac.uk:/home/localuser/fabfile.py")

def vps2():
    env.hosts = ['localuser@studvm37-p.cs.ucl.ac.uk']
    env.user = 'localuser'
    env.password = 'killer369'

def restore():
    run('gunzip /home/localuser/deploy/db1-backup-20151106093140.xml.gz')

    run('xsltproc /home/localuser/deploy/mysqldump-xml-to-sql.xslt /home/localuser/deploy/db1-backup-20151106093140.xml > /home/localuser/deploy/restore.sql')

    run('mysql -u root < /home/localuser/deploy/restore.sql')


    
    


