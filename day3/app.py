import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')
    

    
    # '''Hello World!
    # <a href='/hi'>반장 부르러가기</a>
    # <a href='/lotto'>로또</a>
    # '''


@app.route("/hi")

def hi():
    return render_template('hi.html')


@app.route('/hi/<string:name>')
def hieve(name):
    return render_template('hi2.html', namee=name)




# /cube/<숫자>
# 세제곱 결과를 보여주는 페이지!

@app.route("/cube/<int:num>")

def tri(num):
    return f'{num**3}'


# /lunch/사람이름

@app.route('/lunch/<string:name>')
def lunch(name):
    menu = ['밥','국','반찬']
    return render_template('lunch.html', name=name , pick=random.choice(menu))


# /lotto
# 로또 번호 6개를 추천해주는 페이지


@app.route("/lotto")



def lotto():
    numbers = random.sample(range(1,46),6)
    return f'이번주 당첨번호는 {numbers}!!'



if __name__ == "__main__":
    # python app.py 를 하면 아래의 코드 블록을 실행시킨다.
    app.run(debug=True)






