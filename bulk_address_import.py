import PySimpleGUI as sg
import os

def generate_commands(start_number, entries):
    address_commands = []
    group_commands = []

    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue

        if "." in entry and all(map(lambda x: x.isdigit(), entry.split("."))):
            address_cmd = f"set address malware-ip{start_number} ip-netmask {entry}"
            group_cmd = f"set address-group BlockedIP static malware-ip{start_number}"
        else:
            address_cmd = f"set address malware-url{start_number} fqdn {entry}"
            group_cmd = f"set address-group BlockedIP static malware-url{start_number}"

        address_commands.append(address_cmd)
        group_commands.append(group_cmd)

        start_number += 1

    group_commands.append("commit")

    return address_commands, group_commands

# Utility function to save last used number
def save_last_number(number):
    with open('last_number.txt', 'w') as f:
        f.write(str(number))

# Utility function to load the last used number
def load_last_number():
    if os.path.exists('last_number.txt'):
        with open('last_number.txt', 'r') as f:
            return int(f.read().strip())
    return None  # Return None if the file doesn't exist

# Set the theme
sg.theme('DarkGrey5')

# Set the default number when the application starts
default_number = load_last_number() or 0

# Define the layout
layout = [
    [sg.Text('Enter Starting Number:', size=(22, 1), justification='left'), sg.InputText(str(default_number), key='-NUMBER-', size=(55, 1))],
    [sg.Text('Enter Domains (one per line):', size=(25, 1), justification='left')],
    [sg.Multiline(size=(80, 6), key='-DOMAINS-', justification='left')],
    [sg.Button('Generate Commands', button_color=(sg.theme_text_color(), 'red'))],
    [sg.Text("'set address' Commands:", size=(25, 1), justification='left')],
    [sg.Multiline(size=(80, 6), key='-ADDRESS_OUTPUT-', disabled=True, justification='left')],
    [sg.Button('Copy 1', key='-COPY1-', button_color=(sg.theme_text_color(), 'dark blue')), 
     sg.Button('Copy All', key='-COPY_ALL1-', button_color=(sg.theme_text_color(), 'dark green'))],
    [sg.Text("'set address-group' Commands:", size=(25, 1), justification='left')],
    [sg.Multiline(size=(80, 6), key='-GROUP_OUTPUT-', disabled=True, justification='left')],
    [sg.Button('Copy 1', key='-COPY2-', button_color=(sg.theme_text_color(), 'dark blue')), 
     sg.Button('Copy All', key='-COPY_ALL2-', button_color=(sg.theme_text_color(), 'dark green'))]
]

window = sg.Window('Bulk Address TOOL RCB : By Shion Michael', layout, size=(1000, 650))


# ... [rest of the code remains the same]

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Generate Commands':
        try:
            start_number = int(values['-NUMBER-'])
            entries = values['-DOMAINS-'].splitlines()

            address_commands, group_commands = generate_commands(start_number, entries)

            window['-ADDRESS_OUTPUT-'].update('\n'.join(address_commands))
            window['-GROUP_OUTPUT-'].update('\n'.join(group_commands))
            
            # Save the next number to the file when generating commands
            save_last_number(start_number + len(entries))

        except ValueError:
            sg.popup_error("Please enter a valid starting number.")

    if event == '-COPY1-':
        sg.clipboard_set(window['-ADDRESS_OUTPUT-'].get().split('\n')[0])

    if event == '-COPY_ALL1-':
        sg.clipboard_set('\n'.join(window['-ADDRESS_OUTPUT-'].get().split('\n')[1:]))

    if event == '-COPY2-':
        sg.clipboard_set(window['-GROUP_OUTPUT-'].get().split('\n')[0])

    if event == '-COPY_ALL2-':
        sg.clipboard_set('\n'.join(window['-GROUP_OUTPUT-'].get().split('\n')[1:]))

window.close()

