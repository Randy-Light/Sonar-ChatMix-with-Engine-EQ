# Arctis Nova Pro GameDAC - EQ Enabler

This script solves a common issue for SteelSeries headset owners, allowing you to use the **Engine's Equalizer (EQ)** presets and the hardware **ChatMix** dial simultaneously.

The SteelSeries GG software creates a conflict: when the **Sonar** suite is enabled for the headset, it takes over all audio processing and disables the standard **Engine EQ**. This script sends a direct command to the GameDAC to reactivate your saved Engine EQ profile, allowing you to use it together with the hardware ChatMix, without the Sonar software interfering.

This script is written in Python and uses cross-platform libraries, but has only been thoroughly tested on **Windows**.

## Features

* Enables the use of the Engine's EQ alongside the hardware ChatMix dial.
* Sends a single, targeted command to the GameDAC.
* Does not require administrator privileges to run.
* Works without the SteelSeries GG software running in the background (after the initial EQ setup).
* Can be compiled into a standalone `.exe` file for convenience.

## Requirements

* **Python 3.x**: [Download from python.org](https://www.python.org/downloads/windows/)
* **`hidapi` library**: This will be installed automatically in the next steps.
* **Headset**: SteelSeries Arctis Nova Pro with GameDAC.

## Finding Your Device IDs (If Necessary)

This script uses `VENDOR_ID = 0x1038` and `PRODUCT_ID = 0x12CB`, which are correct for the Arctis Nova Pro with GameDAC. If you are adapting this for a different device, you will need to find its specific IDs.

1.  Open **Device Manager** (right-click the Start Menu and select it).
2.  Find your device. It will likely be under **"Sound, video and game controllers"** or **"Human Interface Devices"**.
3.  Right-click the device and select **"Properties"**.
4.  Go to the **"Details"** tab.
5.  In the "Property" dropdown menu, select **"Hardware Ids"**.
6.  You will see a value like `HID\VID_1038&PID_12CB...`. The numbers after `VID_` and `PID_` are the IDs you need.

## Installation and Setup

1.  **Install Python**. If you don't already have it, download and install it from the official website. **Important:** during installation, check the box that says **"Add Python to PATH"**.
2.  **Download the Script**. Download the `enable_eq.py` file from this repository and save it to a convenient location (e.g., your Desktop).
3.  **Install Dependencies**.
    * Open Command Prompt (`cmd`) or PowerShell.
    * Install the required library by running the following command:
        ```sh
        pip install hidapi
        ```

## How to Run (Simple Method)

The easiest way to run the script is directly from the folder where it is saved.

1.  Open the folder where you saved `enable_eq.py`.
2.  In the address bar of File Explorer (where the folder path is shown), type `cmd` and press Enter.
3.  In the black window that appears, type the following command and press Enter:
    ```sh
    python enable_eq.py
    ```
4.  If successful, you will see a confirmation message, and your equalizer profile will be activated.

## Creating an `.exe` File (Optional)

You can create an `.exe` file for one-click execution, so you don't have to open the command prompt every time.

1.  **Install PyInstaller**. In a Command Prompt, run:
    ```sh
    pip install pyinstaller
    ```
2.  **Create the `.exe`**. Open a command prompt in the script's folder (as described above) and run the command:
    ```sh
    pyinstaller --onefile --noconsole enable_eq.py
    ```
3.  **Find Your File**. The finished `enable_eq.exe` will be located in a new folder named **`dist`**.

## Disclaimer

This script is provided "as-is" without any warranty. By using this software, you agree that the author is not responsible for any potential damage to your device. **Use at your own risk.**
