from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Hello World Hamses Henrique - HMS SOFTWARE"

if __name__ == '__main__':
    app = Flask(__name__)
    csrf.init_app(app)