from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, FormView

from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView

from formsparty.forms import ContactForm1, ContactForm2, RegistrationForm
from formsparty.models import Author

class Index(TemplateView):
    slug = 'index'
    template_name = 'formsparty/index.html'


class ContactWizard(SessionWizardView):
    slug = 'wizard_form'
    form_list = [ContactForm2, ContactForm1]
    template_name = 'formsparty/wizardforms.html'
    mysequence = ['first', 'second']

    def done(self, form_list, **kwargs):
        return render_to_response('formsparty/wizarddone.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get_context_data(self, form, **kwargs):
        context = super(ContactWizard, self).get_context_data(form, **kwargs)
        step = int(self.steps.current)

        if step == 0:
            self.request.session['mysequence'] = ['first', 'second']

        mysequence = self.request.session.get('mysequence', [])

        import random
        item = random.choice(mysequence)
        context['display_text'] = item
        mysequence.remove(item)

        return context


class AuthorCreate(CreateView):
    slug = 'author-create'
    model = Author
    fields = ['name']


class AuthorDetail(DetailView):
    slug = 'author-detail'
    model = Author


class AuthorList(ListView):
    slug = 'author-list'
    model = Author


class AuthorUpdate(UpdateView):
    slug = 'author-update'
    model = Author


class Registration(FormView):
    slug = 'registration'
    template_name = 'formsparty/registration.html'
    form_class = RegistrationForm
    success_url = '/'
