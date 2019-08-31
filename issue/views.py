from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import IssueAddForm
from .models import Issue
from django.utils import timezone
from django.db.models import Q


class IssuedBookListView(LoginRequiredMixin, ListView):

    model = Issue

    paginate_by = 10

    def get_queryset(self):

        q = self.request.GET.get('q', None)

        if not q is None:

            conditions = Q(member__first_name__icontains=q) | Q(
                member__last_name__icontains=q) | Q(book__name__icontains=q)

            return self.model.objects.filter(conditions)

        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_form'] = IssueAddForm
        return context


class IssuedBookCreateView(LoginRequiredMixin, CreateView):

    model = Issue

    template_name = "issue/form.html"

    form_class = IssueAddForm

    success_url = reverse_lazy('issue:issue-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Add Issue Book"
        context['button_name'] = "Create Issue"
        return context


@login_required
def issue_update_view(request, pk):

    instance = get_object_or_404(Issue, pk=pk)

    form = IssueAddForm(request.POST or None, instance=instance)

    if request.method == "POST":

        if form.is_valid():

            obj = form.save()

            updated_obj = {
                'member': str(obj.member),
                'book': str(obj.book),
                'date': obj.date.strftime("%B. %d, %Y, %I:%M %p"),
            }

        return JsonResponse(updated_obj)


@login_required
def issue_delete_view(request, pk):

    instance = get_object_or_404(Issue, pk=pk)

    message = f"Successfully deleted issued row {instance.pk}."

    instance.delete()

    return JsonResponse({'message': message})


@login_required
def recieve_issue_book_view(request, pk):

    instance = get_object_or_404(Issue, pk=pk)

    instance.return_date = timezone.now()

    instance.save()

    return JsonResponse({'date': instance.date.strftime("%B. %d, %Y, %I:%M %p"), })
