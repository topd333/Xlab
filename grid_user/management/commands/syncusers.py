from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
import xlab.settings
from grid_user.models import User, SyncUser

import MySQLdb
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
  option_list = BaseCommand.option_list + (
    make_option('--long', '-l', dest='long',
      help='Help for the long options'),
  )
  help = 'Print Hello!'

  def handle(self, **options):
    dbhost = xlab.settings.USER_DATA_HOST
    dbuser = xlab.settings.USER_DATA_USERNAME
    dbpass = xlab.settings.USER_DATA_USERPASS
    dbname = xlab.settings.USER_DATA_DBNAME

    db=MySQLdb.connect(dbhost, dbuser, dbpass, dbname)
    # csr=db.cursor()
    csr = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    csr.execute("""select FirstName, LastName, PrincipalId, Email, Created from UserAccounts""")
    for row in csr.fetchall():

      try:
        user = User.objects.get(email=row['Email'])
        print 'User exists %s %s'%(user.firstname, user.lastname)
      except ObjectDoesNotExist:
        print '\n'
        print '''User need sync : 
  First Name : %s
  Last Name  : %s
  Id         : %s
  Email      : %s
  Created    : %s ''' % (
          row['FirstName'],
          row['LastName'],
          row['PrincipalId'],
          row['Email'],
          row['Created'],
        )
        print '\n\n'
        #user = User()
        #user.firstname = row[0]

        s_user = SyncUser()
        s_user.email = row['Email']
        s_user.firstname = row['FirstName']
        s_user.lastname = row['LastName']
        s_user.principal_id = row['PrincipalId']
 
        s_user.save()
        
    
