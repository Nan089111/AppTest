import flet as ft

# Define the decoding function
def decode_from_CT37c(encoded_text):
    decoding_dict = {
        '1': 'A', '2': 'E', '3': 'I', '4': 'N', '5': 'O', '6': 'T',
        '70': 'B', '71': 'C', '72': 'D', '73': 'F', '74': 'G', '75': 'H',
        '76': 'J', '77': 'K', '78': 'L', '79': 'M', '80': 'P', '81': 'Q',
        '82': 'R', '83': 'S', '84': 'U', '85': 'V', '86': 'W', '87': 'X',
        '88': 'Y', '89': 'Z', '91': '.', '92': ':', '93': "'", '94': '()',
        '95': '+', '96': '-', '97': '=', '99': 'SPC'
    }

    decoded_text = ''
    i = 0
    while i < len(encoded_text):
        code = ''
        if encoded_text[i] == '9' and i + 4 < len(encoded_text):
            code = encoded_text[i:i+5]
            i += 5
        elif encoded_text[i] in ['7', '8', '9'] and i + 1 < len(encoded_text):
            code = encoded_text[i:i+2]
            i += 2
        else:
            code = encoded_text[i]
            i += 1

        if code in decoding_dict:
            decoded_text += decoding_dict[code]

    return decoded_text

# Function to handle button click
def decode_button_click(e):
    input_text = encoded_text_field.value
    decoded_text = decode_from_CT37c(input_text)
    output_text.value = decoded_text
    page.update()

# Create the Flet app
def main(page: ft.Page):
    global encoded_text_field, output_text

    page.title = "CT-37c Decoder"

    encoded_text_field = ft.TextField(label="Encoded Text", multiline=True, width=400)
    output_text = ft.TextField(label="Decoded Text", multiline=True, width=400, readonly=True)

    decode_button = ft.ElevatedButton(text="Decode", on_click=decode_button_click)

    page.add(
        ft.Column(
            [
                encoded_text_field,
                decode_button,
                output_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# Start the Flet app
ft.app(target=main)
