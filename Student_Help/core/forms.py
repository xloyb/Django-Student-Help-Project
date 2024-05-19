from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserChangeForm


from .models import Post, Logement, Transport, Stage, Evenement, Recommandation,Commentaire,Report


class ReportStatusForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['status']
        widgets = {
            'status': forms.Select(choices=Report.STATUS_CHOICES)
        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['reason'].widget = forms.Select(choices=Report.REASON_CHOICES)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['content']

        
class BasePostForm(forms.ModelForm):
    TYPE_CHOICES = (
        (0, 'Offer'),
        (1, 'Request'),
    )

    type = forms.ChoiceField(choices=TYPE_CHOICES, label='Type')
    title = forms.CharField(label='Title', max_length=255, required=True)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=True)
    image = forms.ImageField(label='Image', required=False)


    class Meta:
        model = Post
        fields = ('type', 'title', 'description','image')

class LogementForm(BasePostForm):
    location = forms.CharField(label='Location', max_length=255, required=True)

    class Meta:
        model = Logement
        fields = BasePostForm.Meta.fields + ('location',)

class TransportForm(BasePostForm):
    departure = forms.CharField(label='Departure', max_length=255, required=True)
    destination = forms.CharField(label='Destination', max_length=255, required=True)
    departureTime = forms.TimeField(label='Departure Time', required=True)

    class Meta:
        model = Transport
        fields = BasePostForm.Meta.fields + ('departure', 'destination', 'departureTime')

class StageForm(BasePostForm):
    TYPE_INTERNSHIP_CHOICES = (
        (1, 'Worker'),
        (2, 'Technician'),
        (3, 'PFE'),
    )

    typeInternship = forms.ChoiceField(choices=TYPE_INTERNSHIP_CHOICES, label='Type of Internship')
    company = forms.CharField(label='Company', max_length=255, required=True)
    duration = forms.IntegerField(label='Duration (months)', required=True)
    subject = forms.CharField(label='Subject', max_length=255, required=True)

    class Meta:
        model = Stage
        fields = BasePostForm.Meta.fields + ('typeInternship', 'company', 'duration', 'subject')

class EvenementForm(BasePostForm):
    TYPE_EVENT_CHOICES = (
        (0, 'Cultural'),
        (1, 'Scientific'),
    )

    eventType = forms.ChoiceField(choices=TYPE_EVENT_CHOICES, label='Event Type')
    date = forms.DateField(label='Date', required=True)
    club = forms.CharField(label='Organizing Club (Optional)', max_length=255, required=False)
    price = forms.DecimalField(label='Ticket Price (Optional)', required=False)
    domain = forms.CharField(label='Subject Area (Optional)', max_length=255, required=False)

    class Meta:
        model = Evenement
        fields = BasePostForm.Meta.fields + ('eventType', 'date', 'club', 'price', 'domain')

class RecommandationForm(BasePostForm):
    text = forms.CharField(label='Recommendation', widget=forms.Textarea, required=True)

    class Meta:
        model = Recommandation
        fields = BasePostForm.Meta.fields + ('text',)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class UserProfileForm(UserChangeForm):
#     class Meta:
#         model = User
#         #fields = ['username', 'first_name', 'last_name', 'email']
        
class UserProfileForm(UserChangeForm):
    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput, 
        required=False
    )
    password2 = forms.CharField(
        label='Password confirmation', 
        widget=forms.PasswordInput, 
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password1")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user