""" Basic Key Management using Web.py """
import web
import model

### Url mappings

urls = (
    '/', 'Index',
)


### Templates
render = web.template.render('templates', base='base')



class Index:

    form = web.form.Form(
        web.form.Textbox('code', web.form.notnull,
            description="Code:"),
        web.form.Textbox('assignee', web.form.notnull,
            description="Assignee:"),
        web.form.Textbox('location', web.form.notnull,
            description="Location:"),
        web.form.Textbox('unit', web.form.notnull,
            description="Unit #:"),
        web.form.Textbox('status', web.form.notnull,
            description="Status:"),
        web.form.Button('Create Key'),
    )

    def GET(self):
        """ Show page """
        keys = model.get_keys()
        form = self.form()
        return render.index(keys, form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            keys = model.get_keys()
            return render.index(keys, form)
        model.new_key(form.d.code, form.d.assignee, form.d.location, form.d.unit, form.d.status)
        raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
