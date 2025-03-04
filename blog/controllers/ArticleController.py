from blog.forms.ArticleForm import ArticleForm
from blog.models.ArticleModel import Article
from blog import db
from flask import redirect, url_for, render_template, flash


class ArticleController:
        def article_add():
            form = ArticleForm()
            if form.validate_on_submit():
                new_article = Article(user_id=1, title=form.title.data, content=form.content.data,)
                db.session.add(new_article)
                db.session.commit()
                flash("تم إضافة المقال بنجاح", "success")
                return redirect(url_for("main_controller.home"))
            return render_template("articles/article_add.jinja", form=form, legend="إضافة مقالة جديدة", title="إضافة مقالة")