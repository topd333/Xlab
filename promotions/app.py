from oscar.apps.promotions.app import (
    PromotionsApplication as CorePromotionsApplication
    )
from promotions.views import HomeView


class PromotionsApplication(CorePromotionsApplication):
    home_view = HomeView

application = PromotionsApplication()
