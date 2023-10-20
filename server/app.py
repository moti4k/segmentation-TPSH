from flask import Flask, render_template


class VueFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',
        variable_end_string='%%',
    ))


app = VueFlask(__name__)


@app.route('/')
def main():  # put application's code here
    template = 'main.html'
    return render_template(template)


if __name__ == '__main__':
    app.run()
