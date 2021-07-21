from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.views.generic import View,ListView,CreateView,DetailView,UpdateView,DeleteView
from record.models import History
from accounts.models import UserProfile
from .import historyform

from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q as s

from django.contrib.auth import get_user_model
User = get_user_model()


class HomeView(ListView):
    model = UserProfile

    def get_queryset(self):
        return UserProfile.objects.order_by('-username')

    template_name='record/index.html'

class SearchView(ListView):
    model = UserProfile

    def get_queryset(self):
        query = self.request.GET.get('q')
        return UserProfile.objects.filter(
                        s(bloodgroup__icontains=query) | s(address__icontains=query)
                        )

    template_name='record/index.html'

@login_required()
def CreateHistoryForm(request):
    if request.method == 'POST':
        history_form = historyform.HistroyForm(data=request.POST)

        if history_form.is_valid():
            historycheck=history_form.save(commit=False)
            history=History.objects.get_or_create(
                        user=request.user,
                        lastdonateddate=historycheck.lastdonateddate)
            return redirect("record:historylist")
        else:
            print(history_form.errors)
    else:
        history_form=historyform.HistroyForm()
    context={'history_form':history_form}
    return render(request,'record/history_form.html',context)


class HistoryView(LoginRequiredMixin, ListView):
    model = History
    template_name='record/historylist.html'

    def get_queryset(self):
        return History.objects.order_by('-lastdonateddate')

class ProfileDetailView(LoginRequiredMixin, SelectRelatedMixin, DetailView):
    model = History
    template_name='record/profiledetail.html'
    select_related=("user",)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)


class HistoryUpdateView(LoginRequiredMixin, SelectRelatedMixin,UpdateView):
    login_url='/login'
    redirect_field_name='record/historylist.html'
    template_name='record/profile_form.html'
    select_related=('user',)

    model = History
    form_class=historyform.HistroyForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

class DeleteHistoryView(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = History
    select_related=('user',)
    success_url=reverse_lazy('record:historylist')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)


class Bmi(View):
    def get(self,*args,**kwargs):

        form =historyform.BMIForm()
        dict={'form':form,
                'getvalue':False}
        return render(self.request, "record/bmi.html",context=dict)

    def post(self,*args,**kwargs):
        form=historyform.BMIForm(self.request.POST or None)
        if form.is_valid():
            height_m=form.cleaned_data.get('height_m')
            weight_kg=form.cleaned_data.get('weight_kg')
            bmivalue=height_m/(weight_kg **2)
            my_dict={'form':form,
                    'BMIValue':bmivalue,
                    'getvalue':True}
            return render(self.request,"record/bmi.html", context=my_dict)
        else:
            print('errors')
