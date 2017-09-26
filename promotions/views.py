from oscar.apps.promotions.views import HomeView as CoreHomeView
from grid_estates.models import EstateMap


class HomeView(CoreHomeView):
    template_name = 'promotions/new-home-new.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        
        return context
