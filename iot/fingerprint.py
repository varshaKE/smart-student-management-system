import serial
import time

# Configure the serial port (update with your COM port or /dev/ttyUSB0 for Linux)
SERIAL_PORT = 'COM4'  # Change this to your port
BAUD_RATE = 57600      # R307S baud rate

def setup_serial():
    """Set up the serial connection."""
    try:
        return serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

def enroll_fingerprint(serial_conn, id):
    """Enroll a fingerprint using the provided ID."""
    print(f"Enrolling fingerprint ID: {id}")
    
    # Command to start enrollment (replace with correct command as per documentation)
    serial_conn.write(b'\xEF')  # Example command for enrolling
    serial_conn.write(bytes([id]))

    time.sleep(2)  # Wait for the module to process

    if serial_conn.in_waiting:
        response = serial_conn.read(2)  # Read two bytes for the response
        print(f"Enroll Response: {response.hex().upper()}")
    else:
        print("No response after enrolling.")

def fetch_fingerprint_details(serial_conn, id):
    """Fetch details for the enrolled fingerprint."""
    print(f"Fetching details for fingerprint ID: {id}")
    
    serial_conn.write(b'\xF2')  # Command to fetch fingerprint details
    serial_conn.write(bytes([id]))

    time.sleep(2)  # Wait for the module to respond

    if serial_conn.in_waiting:
        print("Fingerprint Details:")
        while serial_conn.in_waiting:
            data = serial_conn.read(1)
            print(data.hex().upper(), end=' ')
        print()
    else:
        print("No response from fingerprint module.")

if __name__ == "__main__":
    ser = setup_serial()
    if ser is not None:
        try:
            # Example: Enroll a fingerprint with ID 1
            enroll_fingerprint(ser, 1)
            time.sleep(5)  # Wait before fetching details
            
            # Fetch the fingerprint details
            fetch_fingerprint_details(ser, 1)
        
        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            ser.close()
