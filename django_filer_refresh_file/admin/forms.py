from django import forms

from ..models import RefreshFile


class RefreshFileForm(forms.ModelForm):

    class Meta:
        model = RefreshFile
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].queryset = self.fields['file'].queryset.order_by('folder_id', 'original_filename')
        for obj in self.fields['file'].queryset:
            print("*", obj, self.request.user.has_perm("filer.change_file"))
