from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', page='home')

@app.route('/basic_math', methods=['GET', 'POST'])
def basic_math():
    result = ''

    if request.method == 'POST':
        expression = request.form['expression']
        try:
            result = eval(expression)
        except Exception as e:
            result = "Error: " + str(e)
    return render_template('basic_math.html', page='basic', result=result)

@app.route('/conversions', methods=['GET', 'POST'])
def conversions():
    result = ''

    if request.method == 'POST':
        from_base = request.form['from']
        to_base = request.form['to']
        value = request.form['inputValue']

        try:
            if from_base == "binary":
                decimal_val = int(value, 2)

                if to_base == 'decimal':
                    result = str(decimal_val)
                elif to_base == 'octal':
                    result = oct(decimal_val)[2:]
                elif to_base == 'hexadecimal':
                    result = hex(decimal_val)[2:].upper()
                elif to_base == 'bcd':
                    decimal_str = str(decimal_val)
                    result = ''.join(bin(int(digit))[2:].zfill(4) for digit in decimal_str)
                elif to_base == 'ascii':
                    if 0 <= decimal_val <= 127:
                        result = chr(decimal_val)
                    else:
                        result = 'Invalid ASCII'
                else:
                    result = value

            elif from_base == "decimal":
                decimal_val = int(value)

                if to_base == 'binary':
                    result = bin(decimal_val)[2:]
                elif to_base == 'octal':
                    result = oct(decimal_val)[2:]
                elif to_base == 'hexadecimal':
                    result = hex(decimal_val)[2:].upper()
                elif to_base == 'bcd':
                    decimal_str = str(decimal_val)
                    result = ''.join(bin(int(digit))[2:].zfill(4) for digit in decimal_str)
                elif to_base == 'ascii':
                    if 0 <= decimal_val <= 127:
                        result = chr(decimal_val)
                    else:
                        result = 'Invalid ASCII'
                else:
                    result = value

            elif from_base == "octal":
                decimal_val = int(value, 8)

                if to_base == 'binary':
                    result = bin(decimal_val)[2:]
                elif to_base == 'decimal':
                    result = str(decimal_val)
                elif to_base == 'hexadecimal':
                    result = hex(decimal_val)[2:].upper()
                elif to_base == 'bcd':
                    decimal_str = str(decimal_val)
                    result = ''.join(bin(int(digit))[2:].zfill(4) for digit in decimal_str)
                elif to_base == 'ascii':
                    if 0 <= decimal_val <= 127:
                        result = chr(decimal_val)
                    else:
                        result = 'Invalid ASCII'
                else:
                    result = value

            elif from_base == "hexadecimal":
                decimal_val = int(value, 16)

                if to_base == 'binary':
                    result = bin(decimal_val)[2:]
                elif to_base == 'decimal':
                    result = str(decimal_val)
                elif to_base == 'octal':
                    result = oct(decimal_val)[2:]
                elif to_base == 'bcd':
                    decimal_str = str(decimal_val)
                    result = ''.join(bin(int(digit))[2:].zfill(4) for digit in decimal_str)
                elif to_base == 'ascii':
                    if 0 <= decimal_val <= 127:
                        result = chr(decimal_val)
                    else:
                        result = 'Invalid ASCII'
                else:
                    result = value

            elif from_base == "bcd":
                if len(value) % 4 != 0 or any(bit not in '01' for bit in value):
                    result = "Invalid BCD"
                else:
                    decimal_str = ''.join(str(int(value[i:i+4], 2)) for i in range(0, len(value), 4))
                    decimal_val = int(decimal_str)

                    if to_base == 'binary':
                        result = bin(decimal_val)[2:]
                    elif to_base == 'decimal':
                        result = str(decimal_val)
                    elif to_base == 'octal':
                        result = oct(decimal_val)[2:]
                    elif to_base == 'hexadecimal':
                        result = hex(decimal_val)[2:].upper()
                    elif to_base == 'ascii':
                        if 0 <= decimal_val <= 127:
                            result = chr(decimal_val)
                        else:
                            result = 'Invalid ASCII'
                    else:
                        result = value

            elif from_base == "ascii":
                if len(value) != 1:
                    result = "Invalid ASCII"
                else:
                    decimal_val = ord(value)

                    if to_base == 'binary':
                        result = bin(decimal_val)[2:]
                    elif to_base == 'decimal':
                        result = str(decimal_val)
                    elif to_base == 'octal':
                        result = oct(decimal_val)[2:]
                    elif to_base == 'hexadecimal':
                        result = hex(decimal_val)[2:].upper()
                    elif to_base == 'bcd':
                        decimal_str = str(decimal_val)
                        result = ''.join(bin(int(digit))[2:].zfill(4) for digit in decimal_str)
                    else:
                        result = value
            else:
                result = "Invalid Input. Try again"

        except ValueError:
            result = "Invalid Input. Try again"

    return render_template('conversions.html', page='conversions', result=result)

@app.route('/physics', methods=['GET', 'POST'])
def physics():
    return render_template('physics.html', page='physics')

@app.route('/higher_math', methods=['GET', 'POST'])
def higher_math():
    return render_template('highermath.html', page='higher')

@app.route('/ai-chatbot', methods=['GET', 'POST'])
def ai_chatbot():
    return render_template('chatbot.html', page='ChatBot')

@app.route('/about')
def about():
    return render_template('about.html', page='about')

if __name__ == "__main__":
    app.run(debug=True)
