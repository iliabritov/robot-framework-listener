import smtplib
from datetime import datetime
from configparser import ConfigParser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSenderListener:
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, config_file="mail_config.ini"):
        self.config_file = config_file
        self._read_config()

    def _read_config(self):
        with open(self.config_file) as cfg_file:
            parser = ConfigParser()
            parser.read_file(cfg_file)
            self.server = dict(parser["server"])
            self.sender = dict(parser["sender"])
            self.receiver = dict(parser["receiver"])

    def end_test(self, data, result):
        dataframe = {
            "Suite": data.parent.name,
            "Test name": result.name,
            "Start time": self.reformat_time(result.starttime),
            "End time": self.reformat_time(result.endtime),
            "Result": f"<b>{result.status}</b>",
        }
        if result.message:
            dataframe["Error"] = result.message

        report = "".join(
            [f"<b>{elem}</b> - {dataframe[elem]} <br>" for elem in dataframe]
        )
        self.send_report(report, data.id)

    def send_report(self, report_str, test_case_id):
        message = MIMEMultipart("alternative")

        receiver = self.receiver["address"]

        message["Subject"] = f"Report email. Case {test_case_id}"
        message["From"] = self.sender["username"]
        message["To"] = receiver

        email_content = MIMEText(report_str, "html")
        message.set_payload(email_content)

        with smtplib.SMTP(self.server["address"], self.server["port"]) as session:
            session.starttls()
            session.login(self.sender["username"], self.sender["password"])
            session.sendmail(self.sender["username"], receiver, message.as_string())

    @staticmethod
    def reformat_time(datetime_str):
        datetime_obj = datetime.strptime(datetime_str, "%Y%m%d %H:%M:%S.%f")
        return datetime_obj.strftime("%m/%d/%Y, %H:%M:%S")
