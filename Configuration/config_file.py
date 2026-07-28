# Configuration/config_file.py
config = {
    'base_url': "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
    'browser': "chromium",
    'headless': False,
    'screenshot_path': "./Screenshots/",
    'log_path': "Logs/test.log",
    'username': "Admin",
    'encrypted_password': "YWRtaW4xMjM=",   # base64 encoded 'admin123'
    'date_format': "%Y-%m-%d %H:%M:%S"}
