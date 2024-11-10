from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# اختيار رقم عشوائي بين 1 و 15
number_to_guess = random.randint(1, 15)
attempts = 0

# قالب HTML مُعدل مع تنسيق CSS لتمركز المحتوى وإضافة عبارة أسفل الصفحة
html_template = '''
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>لعبة تخمين الرقم</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            direction: rtl;
            text-align: center;
        }
        .container {
            max-width: 400px;
            width: 100%;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        footer {
            margin-top: 20px;
            font-size: 14px;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>لعبة تخمين الرقم بين 1 و 15 🎯</h1>
        <form method="POST">
            <label>أدخل تخمينك:</label>
            <input type="number" name="guess" required>
            <button type="submit">إرسال</button>
        </form>
        <h2>{{ message }}</h2>
        <footer>برمجة أبو مصعب</footer>
    </div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    global attempts, number_to_guess
    message = ""

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            attempts += 1

            if guess < number_to_guess:
                message = "الرقم أكبر من ذلك! ⬆️"
            elif guess > number_to_guess:
                message = "الرقم أصغر من ذلك! ⬇️"
            else:
                message = f"مبروك! لقد خمّنت الرقم في {attempts} محاولة! 🎉"
                # إعادة تعيين الرقم العشوائي وعدد المحاولات للعبة جديدة
                number_to_guess = random.randint(1, 15)
                attempts = 0
        except ValueError:
            message = "من فضلك أدخل رقمًا صالحًا!"

    return render_template_string(html_template, message=message)

if __name__ == "__main__":
    app.run(debug=True)
