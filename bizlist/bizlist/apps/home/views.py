from django.views.generic import TemplateView

class HomeView(TemplateView):

    template_name = 'home/home.html'

    def get_context_data(self, *args, **kwargs):

        context = super(HomeView, self).get_context_data(*args, **kwargs)

        return context
