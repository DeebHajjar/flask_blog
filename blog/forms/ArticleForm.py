from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileAllowed


class ArticleForm(FlaskForm):
    title = StringField("عنوان المقالة", validators=[DataRequired(), Length(min=5, max=255)])
    article_img = FileField("صورة المقالة", validators=[FileAllowed(['jpg', 'png'])])
    content = TextAreaField("محتوى المقالة", validators=[DataRequired(), Length(min=100, max=10000)])
    submit = SubmitField("نشر المقالة")
