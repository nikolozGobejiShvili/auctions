from django import forms
from auctions.models import Post, Comment, User



class PostCreateFrom(forms.ModelForm):
    def save(self, commit=True, user=None):
        post = super().save(commit=False)
        if user is not None:
            post.user = user
        if commit:
            post.save()
        return post

    class Meta:
        model = Post
        exclude = ["user"]



class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [  "body"]
        Widget = {
            "post" : forms.HiddenInput
        }


class BidForm(forms.Form):
    bid_amount = forms.DecimalField(decimal_places=2, min_value=0.01)

    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post')
        super().__init__(*args, **kwargs)

    def clean_bid_amount(self):
        bid_amount = self.cleaned_data.get('bid_amount')
        if bid_amount <= self.post.highest_bid or bid_amount < self.post.starting_bid:
            raise forms.ValidationError('Your bid must be greater than the current highest bid and the starting bid.')
        return bid_amount        