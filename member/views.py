from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy, reverse
from .models import Member
from .forms import MemberCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MemberCreateView(LoginRequiredMixin, CreateView):

    template_name = "member/form.html"

    form_class = MemberCreationForm

    success_url = reverse_lazy('member:member-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Create Member"
        context['button_name'] = "Create Member"
        return context


class MemberListView(LoginRequiredMixin, ListView):

    model = Member
