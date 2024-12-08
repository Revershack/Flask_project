from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Setează fișierul unde se vor salva datele
DATA_FILE = 'contacts.txt'

# Funcție pentru a salva datele într-un fișier
def save_to_file(name, email, phone_number):
    with open(DATA_FILE, 'a') as file:
        file.write(f'{name},{email},{phone_number}\n')

# Ruta pentru formularul de contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone_number']

        # Salvăm datele în fișier
        save_to_file(name, email, phone_number)

        return redirect(url_for('thank_you'))

    return render_template('contact.html')

# Pagina de mulțumire după trimiterea formularului
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    # Verifică dacă fișierul există, dacă nu, îl creează
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as file:
            file.write('Name,Email,Phone Number\n')  # Scrie header-ul fișierului

    app.run(debug=True)
