import subprocess

def sendEmail(dest_email, subject, content):
    """
    Sends an email to a destination with the specified
    subject & content.

    Returns a boolean indicating success/fail.
    """
    cmd = "echo '{}' | mail -s '{}' {}".format(content, subject, dest_email)
    res = subprocess.call(cmd, shell=True)
    return res == 0
