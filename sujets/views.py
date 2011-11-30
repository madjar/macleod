from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput
from django.views.generic.edit import CreateView
from sujets.models import Question, Option
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms


class VoteForm(forms.Form):
        vote = forms.IntegerField(widget=forms.HiddenInput)


@login_required
def vote(request):
	if request.method == 'POST':
		option = get_object_or_404(Option, pk=request.POST['vote'])
		if request.user in option.voters.all():
			option.voters.remove(request.user)
		else:
			option.voters.add(request.user)
			option.save()
		return redirect(option.question)
	return redirect('/')


class OptionCreateView(CreateView):
    model = Option

#    def __init__(self, **kwargs):
#        super(OptionCreateView, self).__init__(**kwargs)
#        self.question = get_object_or_404(Question, pk=self.kwargs['question'])

    class form_class(ModelForm):
        class Meta:
            model = Option
            exclude = ('voters')
            widgets = {'question': HiddenInput()}

    def get_initial(self):
        self.question = get_object_or_404(Question, pk=self.kwargs['question'])
        return {'question': self.question}

    def get_success_url(self):
        return self.object.question.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(OptionCreateView, self).get_context_data(**kwargs)
        context['question'] = self.question
        return context

