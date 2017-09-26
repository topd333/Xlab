from models import User, TempUser
from slipstream.user.account import UserAccount
from xlab import settings

import logging

log = logging.getLogger("[GRID_USER]:")
auth_host = settings.AUTH_SERVER_URL

class GridUserBackend:

  def authenticate(self, email=None, password=None):
    try:
      if '@' in email:
        xlogin = User.objects.get(email=email)
      else:
        xlogin = User.objects.get(username=email)

      x_user = UserAccount( xlogin.firstname,
                            xlogin.lastname,
                            password,
                            xlogin.email,
                            xlogin.principal_id,
      )

      log.info("Auth: First: %s Last: %s Pass: %s Email: %s PrincipalId %s Username %s"%(

		xlogin.firstname,
                xlogin.lastname,
                password,
                xlogin.email,
                xlogin.principal_id,
                xlogin.username

      ))

      xres = x_user.auth_user(auth_host)
      # We can save the token along with a +30min timestamp in the user
      # if we create the fields for it - TODO
      if xres['result'] == 'success':
        print 'User Token: %s'%xres['token']
        return xlogin
      else:
        return None

    except User.DoesNotExist:
        return None

  def get_user(self, user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return None


