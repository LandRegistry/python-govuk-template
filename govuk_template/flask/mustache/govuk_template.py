from flask_stache import render_view


class GovukTemplate(object):

    def render(self):
        return render_view(self)
