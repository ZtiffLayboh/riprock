from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hola papus</h1>'

@app.route("/miruta")
def hola():
    return "<p>hola, bienvenidos</p>"

@app.route("/secreto")
def wini():
    return '''
        <div style="display: inline-block;">
            <img src='https://cdn.discordapp.com/attachments/1207874393733333065/1247309636420501577/ac3f86a348a844f3a79021a970fa0225.png?ex=665f8f1f&is=665e3d9f&hm=6d142f53736073925ac08a086a3cb56def2169d39d5a7eb9db22c2cd2d942a76&' alt='xd'>
        </div>
        <div style="display: inline-block;">
            <img src='https://cdn.discordapp.com/attachments/1207874393733333065/1247332085941796866/OIG3.png?ex=665fa407&is=665e5287&hm=cc739557156fcb40a9ff4a490587afd8b7e3326e64148d26381a0a414961ab35&' alt='xd2' width="510">
        </div>
    '''

if __name__ == "__main__":
    app.run(debug=True)
