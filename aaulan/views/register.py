from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django import forms
from django_registration.views import RegistrationForm
from django_registration.backends.activation.views import RegistrationView, ActivationView


def validation_tos(value):
    if not bool(value):
        raise ValidationError(_('You must agree to the terms of service to register'))


class AttendeeRegistrationForm(RegistrationForm):
    first_name = forms.CharField(
        label=_('First name'),
        required=True,
        localize=True,
    )
    last_name = forms.CharField(
        label=_('Last name'),
        localize=True,
        required=True,
    )
    legal_agreed = forms.BooleanField(
        label=_('I agree to the terms of service and privacy policy'),
        localize=True,
        validators=[validation_tos],
    )


class AttendeeRegistrationView(RegistrationView):
    form_class = AttendeeRegistrationForm
    success_url = reverse_lazy('attendee-registration-success')

    def register(self, form):
        pass  # ToDO


class AttendeeActivationView(ActivationView):
    success_url = reverse_lazy('attendee-registration-complete')

    def activate(self, *args, **kwargs):
        pass  # ToDo

