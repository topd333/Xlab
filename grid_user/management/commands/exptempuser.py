from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from grid_user.models import TempUser
from datetime import datetime, timedelta
from django.utils import timezone

class Command(BaseCommand):
  option_list = BaseCommand.option_list + (
    make_option('--long', '-l', dest='long',
      help='Help for the long options'),
  )
  help = 'Expire temporary users who failed to register'

  def handle(self, **options):
    now = timezone.now()
    time_threshold = now - timedelta(hours=24)
    results = TempUser.objects.filter(created__lt=time_threshold)
    for k in results:
     print '%s %s : %s' %(k.firstname, k.lastname, k.created) 
