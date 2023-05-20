from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')


def about_flask():
    return "<ol > <li>flask는 파이썬 기반 프레임워크임</li><li>문법이 간단함</li><li>작은 앱을 만들때 유용함</li></ol>"



if __name__ == '__main__' :
    app.run()
