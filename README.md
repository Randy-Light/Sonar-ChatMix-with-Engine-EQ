Arctis Nova Pro GameDAC - EQ EnablerThis script solves a common issue for SteelSeries headset owners, allowing you to use the Engine's Equalizer (EQ) presets and the hardware ChatMix dial simultaneously.The SteelSeries GG software creates a conflict: when the Sonar suite is enabled for the headset, it takes over all audio processing and disables the standard Engine EQ. This script sends a direct command to the GameDAC to reactivate your saved Engine EQ profile, allowing you to use it together with the hardware ChatMix, without the Sonar software interfering.This script is written in Python and uses cross-platform libraries, but has only been thoroughly tested on Windows.FeaturesEnables the use of the Engine's EQ alongside the hardware ChatMix dial.Sends a single, targeted command to the GameDAC.Does not require administrator privileges to run.Works without the SteelSeries GG software running in the background (after the initial EQ setup).Can be compiled into a standalone executable for easy use.RequirementsPython 3.x: Download from python.orghidapi library: This will be installed automatically in the next steps.Headset: SteelSeries Arctis Nova Pro with GameDAC.Finding Your Device IDs (If Necessary)This script uses VENDOR_ID = 0x1038 and PRODUCT_ID = 0x12CB, which are correct for the Arctis Nova Pro with GameDAC. If you are adapting this for a different device, you will need to find its specific IDs.The following instructions are for Windows. Users on macOS or Linux will need to use their respective system tools (e.g., lsusb on Linux) to find USB device information.Open Device Manager (right-click the Start Menu and select it).Find your device. It will likely be under "Sound, video and game controllers" or "Human Interface Devices".Right-click the device and select "Properties".Go to the "Details" tab.In the "Property" dropdown menu, select "Hardware Ids".You will see a value like HID\VID_1038&PID_12CB.... The numbers after VID_ and PID_ are the IDs you need.Installation and SetupInstall Python. If you don't already have it, download and install it from the official website. Make sure to add it to your system's PATH during installation.Create the Script File.Create a new file on your computer named enable_eq.py.Copy and paste the code provided below into this file.Install Dependencies.Open a terminal or command prompt.Install the required library by running the following command:pip install hidapi
UsageOpen a terminal or command prompt.Navigate to the folder where you saved enable_eq.py using the cd command. For example:cd C:\Users\YourName\Desktop
Run the script:python enable_eq.py
If successful, you will see a confirmation message, and your equalizer profile will be activated.Creating a Standalone Executable (Optional)You can package this script into a single executable file for convenience.Install PyInstaller. In a terminal or command prompt, run:pip install pyinstaller
Create the Executable. While in the same folder as your script, run the command:For Windows (.exe):pyinstaller --onefile --noconsole enable_eq.py
For macOS/Linux:pyinstaller --onefile enable_eq.py
Find Your File. The finished executable will be located in a new folder named dist.DisclaimerThis script is provided "as-is" without any warranty. By using this software, you agree that the author is not responsible for any potential damage to your device. Use at your own risk.Script Code# enable_eq.py

import hid
import sys

# --- Device Identifiers ---
VENDOR_ID = 0x1038
PRODUCT_ID = 0x12CB
INTERFACE_NUMBER = 4  # The control interface we discovered

def find_device_path(vid, pid, interface_num):
    """Finds the path to the device's HID control interface."""
    devices = hid.enumerate(vid, pid)
    for dev in devices:
        if dev['interface_number'] == interface_num:
            return dev['path']
    return None

def enable_engine_eq(device_path: bytes):
    """Sends the specific command to enable the Engine EQ."""
    h = hid.device()
    try:
        h.open_path(device_path)

        # Construct the report with the specific command to enable the EQ
        report = bytearray(65)
        report[0] = 0x06  # Report ID for the "Set" command
        report[1] = 0x3b  # Parameter ID for "Engine EQ"
        report[2] = 0x01  # Value "1" (to enable)

        print(f"🚀 Sending command: {report[:4].hex()}...")

        # Send the command as a Feature Report
        h.send_feature_report(report)

        print("✅ Command sent successfully. Engine EQ should now be enabled.")

    except Exception as e:
        print(f"🛑 Error while sending the command: {e}")
        print("   On Windows, try running the script as an administrator.")
    finally:
        h.close()

# --- Main execution block ---
if __name__ == "__main__":
    print("--- Enabling SteelSeries Engine EQ ---")
    path = find_device_path(VENDOR_ID, PRODUCT_ID, INTERFACE_NUMBER)

    if path:
        enable_engine_eq(path)
    else:
        print(f"❌ Device on interface #{INTERFACE_NUMBER} not found. Make sure the GameDAC is connected.")
