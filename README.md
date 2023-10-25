# Python Email Sender

The Python Email Sender is a versatile command-line tool that simplifies the process of sending emails with or without attachments. Whether you need to send important documents or simple messages, this script has you covered.

## How It Works

This Python script uses the `smtplib` library to send emails. It allows you to:

- Send emails from your email account.
- Customize the subject and body of the email.
- Attach files to your emails.

## Prerequisites

Before using this script, make sure you have:

- Python 3.x installed on your machine.
- The `getpass` library, which helps securely handle password input.
- Access to an SMTP server. You can use servers like 'smtp.gmail.com' for Gmail or 'smtp.mail.yahoo.com' for Yahoo.

## Usage

1. Clone this repository to your local machine.

2. Run the script:
   ```
   python send_email.py
   ```

3. Follow the prompts to enter the necessary details:
   - Your email address
   - Your email password (entered securely)
   - Recipient email addresses (separated by commas if multiple)
   - The body of the email
   - Whether you want to attach a file (Yes/No)

4. If you choose to attach a file, provide the file path when prompted.

5. The script will then use the provided SMTP server to send your email.

## Example

Here's an example of how to send an email using this script:

1. Clone the repository to your local machine.

2. Run the script: `python send_email.py`

3. Enter your email address and password.

4. Add the recipient's email addresses (e.g., "example@example.com").

5. Type the content of your email.

6. If you want to attach a file, type "Yes" and provide the file path.

7. Enter the SMTP server (e.g., 'smtp.gmail.com').

8. Your email will be sent, and you'll receive a confirmation message.

## License

This project is open-source and available under the MIT License. You are free to use, modify, and distribute this script according to the terms of the license. For details, please see the [LICENSE](LICENSE) file.

Feel free to contribute to this project or report issues. Your feedback is valuable.

For any questions or assistance, please contact the project maintainer.
