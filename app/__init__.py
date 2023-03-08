from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html') 

@app.route('/login', methods=['GET', 'POST'])
def login():
  # print(request.method)
  if request.method == 'POST':
    if request.form['usuario'] == 'admin' and request.form['password'] == '12345':
    # print(request.form['usuario'])
    # print(request.form['password'])
      return redirect(url_for('index'))
    else:
      return render_template('auth/login.html')
  else:
    return render_template('auth/login.html')

def pagina_no_encontrada(error):
  return render_template('errors/404.html'), 404


def inicializar_app(config):
  app.config.from_object(config)
  app.register_error_handler(404, pagina_no_encontrada)
  return app

