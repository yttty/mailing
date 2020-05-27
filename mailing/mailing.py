"""
Send mail in CSE server
"""
from os.path import basename
from typing import List
import logging
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formatdate


def send_mail(sender,
              send_from,
              send_to: List[str],
              subject,
              text,
              send_cc: List[str] = None,
              send_bcc: List[str] = None,
              files=None,
              server=None):
    """
    Send a mail via smtp server
    """
    assert isinstance(send_to, list)

    logging.info('Preparing to send the mail to ' + ' and '.join(send_to))
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    recipient = send_to
    if send_cc and send_bcc:
        msg['Cc'] = COMMASPACE.join(send_cc)
        msg['Bcc'] = COMMASPACE.join(send_bcc)
        recipient = [recipient] + send_cc + send_bcc
    elif send_bcc:
        msg['Bcc'] = COMMASPACE.join(send_bcc)
        recipient = [recipient] + send_bcc
    elif send_cc:
        msg['Cc'] = COMMASPACE.join(send_cc)
        recipient = [recipient] + send_cc

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(f))
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    try:
        smtp = smtplib.SMTP(server)
        smtp.sendmail(send_from, recipient, msg.as_string())
        smtp.close()
        logging.info(f'Sent mail from {send_from} to ' + ' and '.join(send_to))
        print(f'Sent mail from {send_from} to ' + ' and '.join(send_to))
    except Exception as e:
        # print 'Failed to send the mail to '+you
        err_msg = 'Failed to send the mail to %s, because %s\n' % (
            ' and '.join(send_to), e.__doc__)
        logging.error(err_msg)


def send_mail_cse_smtp(cse_username: str,
                       subject: str,
                       content: str,
                       attachment: List[str],
                       receiver: List[str],
                       cc: List[str] = None,
                       bcc: List[str] = None):
    send_mail(sender=cse_username,
              send_from=cse_username + '@cse.cuhk.edu.hk',
              send_to=receiver,
              subject=subject,
              text=content,
              send_cc=cc,
              send_bcc=bcc,
              files=attachment,
              server='mail.cse.cuhk.edu.hk')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    send_mail_cse_smtp(
        'tyyang',  # cse username
        "TEST",  # subject
        "THIS is a test mail",  # content
        ['mailing.py'],  # attachment
        ['tim.tyyang@outlook.com'],  # receiver list
        ['tyyaa@qq.com'],  # cc list
        ['tyyang@link.cuhk.edu.hk']  # bcc list
        # None  # bcc list
    )
