from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, my name is Sudha Sutaschuto 6710545920. Through this ISP subject, I have learned how real software development projects are planned, organized, and executed in professional environments. This course helped me understand the importance of teamwork, communication, proper task distribution, and recognizing team roles such as frontend, backend, and DevOps. I also gained valuable experience in analyzing and understanding user requirements, which is an essential foundation for building useful and successful software. Additionally, I learned how to plan work, manage deadlines, monitor project progress, and evaluate project outcomes. Overall, this subject has strengthened my awareness of real-world software development processes from start to finish."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)