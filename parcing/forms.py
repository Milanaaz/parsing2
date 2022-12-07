from django import forms
from . import parser, models, parser_2


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Math quizzes', 'Math quizzes'),
        ('Geography quizzes', 'Geography quizzes'),

    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        field = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'Geography quizzes':
            geo_parser = parser.parser()
            for i in geo_parser:
                models.TvParser.objects.create(**i)
        if self.data['media_type'] == 'Math quizzes':
            math_parser = parser_2.parser()
            for i in math_parser:
                models.TvParser.objects.create(**i)
