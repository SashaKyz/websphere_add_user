#!/usr/bin/python
import sys
import re
import csv



mailplaceholder='@optum.com'


def create_websphere_user(user_str):
    AdminTask.createUser('['+user_str+']')
    AdminConfig.save()
    print '\nConfigurarion saved.\n'


def create_group(group_str):
    AdminTask.createGroup ('['+group_str+']')
    AdminConfig.save()
    print '\nConfigurarion saved.\n'



with open('text.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         if row['User']!='':
            users=row['User']
         print( users, row['LoginID'] ,row ['Role'])
         from subprocess import call
         call(['/opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/wsadmin.sh', '-username', 'admin', '-password', 'wasadmin', '-lang', 'jython', '-f', 'adduser_j.py', users, row['LoginID'] ,row ['Role']])
         



