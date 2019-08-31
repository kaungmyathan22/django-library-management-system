from .models import Member
from django.db.models import Q
from django.http import JsonResponse
from .forms import MemberCreationForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView


class MemberCreateView(LoginRequiredMixin, CreateView):

    template_name = "member/form.html"

    form_class = MemberCreationForm

    success_url = reverse_lazy('member:member-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Create New Member"
        context['button_name'] = "Create Member"
        return context


class MemberUpdateView(LoginRequiredMixin, UpdateView):

    model = Member

    template_name = "member/form.html"

    form_class = MemberCreationForm

    success_url = reverse_lazy('member:member-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Update Member Info"
        context['button_name'] = "Update Member"
        return context


class MemberListView(LoginRequiredMixin, ListView):

    model = Member

    paginate_by = 10

    def get_queryset(self):
            
        q = self.request.GET.get('q', None)

        if not q is None:

            conditions = Q(first_name__icontains=q) | Q(
                last_name__icontains=q) | Q(email__icontains=q) | Q(roll_no__icontains=q)
            
            return self.model.objects.filter(conditions).distinct()

        return super().get_queryset()





@login_required
def member_delete_view(request, pk):

    instance = get_object_or_404(Member, pk=pk)

    if request.method == "POST":

        member_name = str(instance)

        instance.delete()

        return JsonResponse({
            'message': f'Successfully deleted {member_name}.'
        })
