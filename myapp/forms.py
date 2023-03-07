from django import forms 

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200,
                            widget=forms.TextInput(attrs={"class": "input"}))
    description = forms.CharField(
        label="description", widget=forms.Textarea(attrs={"class": "input"}))

class CreateNewProjects(forms.Form):
    name = forms.CharField(label="Titulo de proyecto", max_length=200)
