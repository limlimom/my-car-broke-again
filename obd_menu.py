import obd
import time

PORT = "/dev/tty.usbserial-140"   # replace with your port if different

def connect():
    print("🔌 Connecting to adapter...")
    connection = obd.OBD(PORT)
    if not connection.is_connected():
        print("❌ No connection to the vehicle")
        return None
    return connection

def show_vin(connection):
    print("\n🚗 Vehicle VIN:")
    try:
        vin = connection.query(obd.commands.VIN)
        if vin.is_null():
            print("Failed to retrieve VIN")
        else:
            # vin.value may be a bytearray - decode it
            vin_str = "".join([chr(b) for b in vin.value]) if isinstance(vin.value, bytearray) else str(vin.value)
            print(vin_str)
    except Exception as e:
        print("Error retrieving VIN:", e)

def show_errors(connection):
    print("\n📋 Active trouble codes (DTC):")
    try:
        response = connection.query(obd.commands.GET_DTC)
        if response.is_null():
            print("No errors found")
        else:
            for e in response.value:
                if len(e) == 2:
                    code, desc = e
                    print(f" - {code}: {desc}")
                elif len(e) == 3:
                    code, desc, status = e
                    print(f" - {code}: {desc} [{status}]")
    except Exception as e:
        print("Error reading trouble codes:", e)

def clear_errors(connection):
    print("\n⚠️ Clearing trouble codes...")
    try:
        connection.query(obd.commands.CLEAR_DTC)
        print("✅ Trouble codes cleared")
    except Exception as e:
        print("Error clearing codes:", e)

def show_live_data(connection):
    print("\n📊 Live data (press Ctrl+C to exit):")
    try:
        while True:
            rpm = connection.query(obd.commands.RPM)
            speed = connection.query(obd.commands.SPEED)
            coolant = connection.query(obd.commands.COOLANT_TEMP)
            maf = connection.query(obd.commands.MAF)
            throttle = connection.query(obd.commands.THROTTLE_POS)

            print("---------------------------")
            print("Engine RPM:", rpm.value if not rpm.is_null() else "—")
            print("Speed:", speed.value if not speed.is_null() else "—")
            print("Coolant Temperature:", coolant.value if not coolant.is_null() else "—")
            print("Air Flow (MAF):", maf.value if not maf.is_null() else "—")
            print("Throttle Position:", throttle.value if not throttle.is_null() else "—")

            time.sleep(1)
    except KeyboardInterrupt:
        print("\n⏹ Exiting live data")

def main():
    while True:
        print("\n====== OBD-II Menu ======")
        print("1 — Show VIN")
        print("2 — Show trouble codes")
        print("3 — Clear trouble codes")
        print("4 — Live data (loop)")
        print("0 — Exit")

        choice = input("Select an option: ").strip()

        if choice == "0":
            print("👋 Exit")
            break

        connection = connect()
        if not connection:
            continue

        if choice == "1":
            show_vin(connection)
        elif choice == "2":
            show_errors(connection)
        elif choice == "3":
            clear_errors(connection)
        elif choice == "4":
            show_live_data(connection)
        else:
            print("Invalid choice")

        connection.close()

if __name__ == "__main__":
    main()