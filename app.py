from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Halaman login (GET) dan menerima input (POST)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')  # Mengambil data dari form
        if username:  # Validasi jika username diisi
            return redirect(url_for('welcome', username=username))  # Corrected to use 'welcome'
        else:
            return render_template('login.html', error="Please enter a username.")
    return render_template('login.html')  # Menampilkan halaman login

# Halaman selamat datang
@app.route('/home')
def welcome():
    username = request.args.get('username')  # Mendapatkan data username dari URL
    if username:
        return render_template('home.html', username=username)
    return redirect(url_for('login'))  # Jika tidak ada username, kembali ke halaman login

if __name__ == '__main__':
    app.run(debug=True)
