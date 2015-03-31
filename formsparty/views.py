from django.views.generic import TemplateView

from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView

from formsparty.forms import ContactForm1, ContactForm2


class Index(TemplateView):
    slug = 'index'
    template_name = 'formsparty/index.html'


class ContactWizard(SessionWizardView):
    slug = 'wizard_form'
    form_list = [ContactForm1, ContactForm2]
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
            print "INIT LIST"
            import copy
            self.request.session['mysequence'] = ['first', 'second'] # copy.deepcopy(self.mysequence)

        mysequence = self.request.session.get('mysequence', [])

        import random
        item = random.choice(mysequence)
        context['display_text'] = item
        mysequence.remove(item)

        return context
