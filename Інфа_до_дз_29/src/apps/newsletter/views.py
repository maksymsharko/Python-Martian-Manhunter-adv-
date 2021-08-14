from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from src.apps.newsletter.forms import NewsLetterModelForm


class NewNewsLetterView(FormView):
    template_name = 'newsletters/subscribe.html'
    form_class = NewsLetterModelForm
    success_url = reverse_lazy('newsletters:success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SuccessTemplateView(TemplateView):
    template_name = 'newsletters/success_page.html'
