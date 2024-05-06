# BadUSB Payload Encoder

- This Python script is a BadUSB payload encoder designed to generate an encrypted payload for use with BadUSB devices. The encoded payload is based on the provided input file and additional parameters.

## How to Use

1.Clone the Repository:

    git clone https://github.com/scriptkiddieeee/BadUSB-Payload-Encoder.git
    cd BadUSB-Payload-Encoder

2.Run the Script:

    python3 BadUSB-Payload-Encoder.py test-script.ps1

Options:

    -adv: Enable advanced mode.

Example:

    python3 BadUSB-Payload-Encoder.py -adv test-script.ps1

3.Follow the Prompts:

- If advanced mode is enabled, you'll be prompted to provide additional information such as payload title, description, author, and version.        
- You can also choose to add a custom delay in the payload after opening PowerShell.

4.Final Output:

- The generated payload will be saved in the payload.txt file in the same directory.
- Check the console for the location of the generated payload.

## Author

[Malwarekid](https://github.com/malwarekid)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Notes

Feel free to contribute, report issues, or provide feedback and dont forget to follow me on [Instagram](https://www.instagram.com/malwarekid/) and [github](https://github.com/malwarekid/) Happy Hacking!
