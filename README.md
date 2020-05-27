# mailing

Python package for sending mail in cuhk-cse server

## Requirement
- Python 3

## Install
```pip install --force-reinstall git+https://github.com/yttty/mailing.git```

## Basic usage
```python
from mailing import send_mail_cse_smtp

send_mail_cse_smtp(
    'tyyang',  # cse username
    "TEST",  # subject
    "THIS is a test mail",  # content
    ['./README.md'],  # attachment
    ['tim.tyyang@outlook.com']  # receiver list
)

send_mail_cse_smtp(
    'tyyang',  # cse username
    "TEST",  # subject
    "THIS is a test mail",  # content
    None,  # no attachment
    ['tim.tyyang@outlook.com']  # receiver list
)

send_mail_cse_smtp(
    'tyyang',  # cse username
    "TEST",  # subject
    "THIS is a test mail",  # content
    ['mailing.py'],  # attachment
    ['tim.tyyang@outlook.com'],  # receiver list
    ['tyyaa@qq.com'],  # cc list
    ['tyyang@link.cuhk.edu.hk']  # bcc list
)
```
