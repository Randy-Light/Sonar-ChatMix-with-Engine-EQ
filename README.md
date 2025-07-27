# Sonar-ChatMix-with-Engine-EQ

Arctis Nova Pro GameDAC - EQ Enabler
This script solves a common issue for SteelSeries headset owners, allowing you to use the Engine's Equalizer (EQ) presets and the hardware ChatMix dial simultaneously.

The SteelSeries GG software creates a conflict: when the Sonar suite is enabled for the headset, it takes over all audio processing and disables the standard Engine EQ. This script sends a direct command to the GameDAC to reactivate your saved Engine EQ profile, allowing you to use it together with the hardware ChatMix, without the Sonar software interfering.

This script is written in Python and uses cross-platform libraries, but has only been thoroughly tested on Windows.

Features
Enables the use of the Engine's EQ alongside the hardware ChatMix dial.

Sends a single, targeted command to the GameDAC.

Does not require administrator privileges to run.

Works without the SteelSeries GG software running in the background (after the initial EQ setup).

Can be compiled into a standalone executable for easy use.

Requirements
Python 3.x: Download from python.org

hidapi library: This will be installed automatically in the next steps.

Headset: SteelSeries Arctis Nova Pro with GameDAC.

Finding Your Device IDs (If Necessary)
This script uses VENDOR_ID = 0x1038 and PRODUCT_ID = 0x12CB, which are correct for the Arctis Nova Pro with GameDAC. If you are adapting this for a different device, you will need to find its specific IDs.

The following instructions are for Windows. Users on macOS or Linux will need to use their respective system tools (e.g., lsusb on Linux) to find USB device information.

Open Device Manager (right-click the Start Menu and select it).

Find your device. It will likely be under "Sound, video and game controllers" or "Human Interface Devices".

Right-click the device and select "Properties".

Go to the "Details" tab.

In the "Property" dropdown menu, select "Hardware Ids".

You will see a value like HID\VID_1038&PID_12CB.... The numbers after VID_ and PID_ are the IDs you need.

Installation and Setup
Install Python. If you don't already have it, download and install it from the official website. Make sure to add it to your system's PATH during installation.

Create the Script File.

Create a new file on your computer named enable_eq.py.

Copy and paste the code provided below into this file.

Install Dependencies.

Open a terminal or command prompt.

Install the required library by running the following command:

Bash

pip install hidapi
Usage
Open a terminal or command prompt.

Navigate to the folder where you saved enable_eq.py using the cd command. For example:

Bash

cd C:\Users\YourName\Desktop
Run the script:

Bash

python enable_eq.py
If successful, you will see a confirmation message, and your equalizer profile will be activated.

Creating a Standalone Executable (Optional)
You can package this script into a single executable file for convenience.

Install PyInstaller. In a terminal or command prompt, run:

Bash

pip install pyinstaller
Create the Executable. While in the same folder as your script, run the command:

For Windows (.exe):

Bash

pyinstaller --onefile --noconsole enable_eq.py
For macOS/Linux:

Bash

pyinstaller --onefile enable_eq.py
Find Your File. The finished executable will be located in a new folder named dist.

Disclaimer
This script is provided "as-is" without any warranty. By using this software, you agree that the author is not responsible for any potential damage to your device. Use at your own risk.
