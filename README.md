# -Windows-application-for-Firewall

This tool is designed to assist users in generating firewall commands for blocking malicious IPs and URLs. By entering a starting number and a list of domains/IPs, the tool will output the necessary "set address" and "set address-group" commands to configure on a firewall.

**Developed by:** Shion Michael

**Prerequisites**
1. Python 3.x
2. PySimpleGUI: Run the command `pip install PySimpleGUI`.

**Setup**
1. Clone this repository.
2. Navigate to the project's directory.
3. Run the script using `python bulk_address_import.py`.

**Running the Application**
- If you wish to directly run the application without any modifications, simply execute the `bulk_address_import.exe` file.

**Customization**
- For those looking to modify or customize the command generation, the source code is available in the `bulk_address_import.py` file. Feel free to edit it to tailor the commands to your needs.

**How to Use**
1. Enter the starting number.
2. Input the list of domains/IPs in the textarea. Each domain or IP should be on a separate line.
3. Click on "Generate Commands".
4. The commands will be displayed in the respective text areas below.
5. Use the "Copy 1" button to copy the first command of each type to the clipboard.
6. Use the "Copy All" button to copy all commands (except the first one) of each type to the clipboard.

**Features**
- Generates firewall "set address" and "set address-group" commands for a list of IPs or domains.
- Remembers the last starting number used and loads it the next time you run the application.
- Provides copy functionality for the generated commands.
- Simple and intuitive GUI for user interaction.

**Troubleshooting**
If an error popup stating "Please enter a valid starting number" appears, ensure that the starting number entered is a valid integer.

**Contributions**
For any suggestions, bugs, or features, please open an issue or submit a pull request.



![image](https://github.com/Shionjee7/-Windows-application-for-Firewall/assets/96959471/dc67624e-0f6b-4a01-825f-821b3544f017)
