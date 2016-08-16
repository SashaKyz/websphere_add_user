import sys
import re

mailplaceholder='@optum.com'


def create_websphere_user(user_str):
    AdminTask.createUser('['+user_str+']')
    AdminConfig.save()
#    print user_str
    print '\nUser created.\n'


def create_group(group_str):
    AdminTask.createGroup ('['+group_str+']')
    AdminConfig.save()
#    print group_str
    print '\nGroup created.\n'

user = sys.argv[0]
login = sys.argv[1]
role = sys.argv[2]

print  '\n USER:',user,' login: ',login,' role:',role,'\n'

if AdminTask.searchUsers ('[-uid '+login+']')=='':
    create_websphere_user('-uid '+login+' -password '+login+'1 -confirmPassword '+login+'1 -cn '+user.split(' ').pop(0)+' -sn '+user.split(' ').pop()+' -mail '+login+mailplaceholder)
if AdminTask.searchGroups ('[ -cn '+role+' ]')=="":
    create_group('-cn '+role+' -description "Script created group"')

if AdminTask.addMemberToGroup('[ -memberUniqueName '+AdminTask.searchUsers ('[-uid '+login+']')+' -groupUniqueName '+AdminTask.searchGroups ('[ -cn '+role+' ]')+' ]')!='':
    print "User: ",login," added to group: ",role,'\n'


