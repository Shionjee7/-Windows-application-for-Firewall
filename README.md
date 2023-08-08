# -Windows-application-for-Firewall

This tool is designed to assist users in generating firewall commands for blocking malicious IPs and URLs. By entering a starting number and a list of domains/IPs, the tool will output the necessary "set address" and "set address-group" commands to configure on a firewall.

Developed by: Shion Michael

Prerequisites
Python 3.x
PySimpleGUI: pip install PySimpleGUI
Setup
Clone this repository.
Navigate to the project's directory.
Run the script using python <script-name>.py.
How to Use
Enter the starting number.
Input the list of domains/IPs in the textarea. Each domain or IP should be on a separate line.
Click on "Generate Commands".
The commands will be displayed in the respective text areas below.
Use the "Copy 1" button to copy the first command of each type to the clipboard.
Use the "Copy All" button to copy all commands (except the first one) of each type to the clipboard.
Features
Generates firewall "set address" and "set address-group" commands for a list of IPs or domains.
Remembers the last starting number used and loads it the next time you run the application.
Provides copy functionality for the generated commands.
Simple and intuitive GUI for user interaction.
Troubleshooting
If an error popup stating "Please enter a valid starting number" appears, ensure that the starting number entered is a valid integer.

Contributions
For any suggestions, bugs, or features, please open an issue or submit a pull request.
