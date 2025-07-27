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
    finally:
        h.close()

# --- Main execution block ---
if __name__ == "__main__":
    print("--- Enabling SteelSeries Engine EQ ---")
    path = find_device_path(VENDOR_ID, PRODUCT_ID, INTERFACE_NUMBER)

    if path:
        enable_engine_eq(path)
    else:
        print(f"❌ Device on interface #{INTERFACE_NUMBER} not found.")
