import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
)
from PyQt6.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt6.QtCore import Qt
from Database.DatabaseManager import DatabaseManager
from Database.Database import create_tables
from Classes.Report import ReportManager
from Classes.Project import Project
from Classes.Member import Member
from Classes.Task import Task
import datetime



def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Invalid number. Try again.")


def input_date(msg):
    while True:
        val = input(f"{msg} (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(val, "%Y-%m-%d")
            return val
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")


class Show_Task_Person1(QWidget):
    def god_Help_ME(self, member, page):
        if hasattr(self, "labels_Pname"):
            for lbl in self.labels_TID:
                lbl.deleteLater()
        if hasattr(self, "labels_number"):
            for lbl in self.labels_PID:
                lbl.deleteLater()
        if hasattr(self, "labels_Name"):
            for lbl in self.labels_OID:
                lbl.deleteLater()
        if hasattr(self, "labels_Start"):
            for lbl in self.labels_Ded:
                lbl.deleteLater()
        if hasattr(self, "labels_end"):
            for lbl in self.labels_TI:
                lbl.deleteLater()
        if hasattr(self, "labels_end"):
            for lbl in self.labels_ST:
                lbl.deleteLater()
        self.labels_TID = []
        self.labels_PID = []
        self.labels_OID = []
        self.labels_Ded = []
        self.labels_TI = []
        self.labels_ST = []
        for t in member:
            print(
                f"Task: {t[0]} | Deadline: {t[1]} | Assignee ID: {t[2]} | Task: {t[3]} | Deadline: {t[4]} | Assignee ID: {t[5]}"
            )
        if (len(member) - page * 10) < 10:
            for i in range(len(member)):
                lbl = QLabel(str(member[i + page * 10][0]), self)
                lbl.setStyleSheet("color: black;")
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_TID.append(lbl)

                lbl1 = QLabel(str(member[i + page * 10][1]), self)
                lbl1.setStyleSheet("color: black;")
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_TI.append(lbl1)

                lbl2 = QLabel(str(member[i + page * 10][2]), self)
                lbl2.setStyleSheet("color: black;")
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_PID.append(lbl2)

                lbl3 = QLabel(str(member[i + page * 10][3]), self)
                lbl3.setStyleSheet("color: black;")
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_OID.append(lbl3)
                lbl4 = QLabel(str(member[i + page * 10][4]), self)
                lbl4.setStyleSheet("color: black;")
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_ST.append(lbl4)
                lbl5 = QLabel(str(member[i + page * 10][5]), self)
                lbl5.setStyleSheet("color: black;")
                lbl5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl5.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_Ded.append(lbl5)
        else:
            for i in range(10):
                lbl = QLabel(str(member[i + page * 10][0]), self)
                lbl.setStyleSheet("color: black;")
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_TID.append(lbl)

                lbl1 = QLabel(str(member[i + page * 10][1]), self)
                lbl1.setStyleSheet("color: black;")
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_TI.append(lbl1)

                lbl2 = QLabel(str(member[i + page * 10][2]), self)
                lbl2.setStyleSheet("color: black;")
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_PID.append(lbl2)

                lbl3 = QLabel(str(member[i + page * 10][3]), self)
                lbl3.setStyleSheet("color: black;")
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_OID.append(lbl3)
                lbl4 = QLabel(str(member[i + page * 10][4]), self)
                lbl4.setStyleSheet("color: black;")
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_ST.append(lbl4)
                lbl5 = QLabel(str(member[i + page * 10][5]), self)
                lbl5.setStyleSheet("color: black;")
                lbl5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl5.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_Ded.append(lbl5)

    def __init__(self, pro, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)
        self.page = 0
        self.ProList = pro
        self.db = db
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Member_show.png")
        # labes
        self.lblHeader = QLabel("لیست تسک ها", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # but
        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)
        self.btnB = QPushButton(self)
        self.btnB.setText("قبلی")
        self.btnB.clicked.connect(self.goAM)
        self.btnN = QPushButton(self)
        self.btnN.setText("بعدی")
        self.btnN.clicked.connect(self.goA)
        self.god_Help_ME(self.ProList, self.page)

    def goA(self):
        all_Page = (int(len(self.ProList) + 9) // 10) - 1
        if all_Page > self.page:
            self.page = self.page + 1
            self.god_Help_ME(self.ProList, self.page)

    def goAM(self):
        if self.page > 0:
            self.page = self.page - 1
            self.god_Help_ME(self.ProList, self.page)

    def goB(self):
        self.project_window = Report_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )

            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)

        self.btnback.resize(int(w * 0.1), int(h * 0.05))
        self.btnback.move(int(w * 0.055), int(h * 0.059))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnB.resize(int(w * 0.1), int(h * 0.05))
        self.btnB.move(int(w * 0.34), int(h * 0.85))
        self.btnB.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnN.resize(int(w * 0.1), int(h * 0.05))
        self.btnN.move(int(w * 0.54), int(h * 0.85))
        self.btnN.setFont(QFont("Vazir", max(int(h * 0.02), 1)))
        # label
        self.lblHeader.resize(int(w * 0.2), int(h * 0.3))
        self.lblHeader.move(int(w * 0.4), int(h * 0.00001 - 45))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.032), 1)))

        positions = [
            (0.5, 0.1275),
            (0.5, 0.197),
            (0.5, 0.2655),
            (0.5, 0.3360),
            (0.5, 0.4055),
            (0.5, 0.4755),
            (0.5, 0.545),
            (0.5, 0.6145),
            (0.5, 0.684),
            (0.5, 0.7535),
        ]
        sizes = [
            (0.05, 0.07),
            (0.23, 0.07),
            (0.05, 0.07),
            (0.035, 0.07),
            (0.18, 0.07),
            (0.19, 0.07),
            (0.5, 0.2),
            (0.3, 0.2),
            (0.5, 0.2),
            (0.3, 0.2),
        ]

        for i, lbl in enumerate(self.labels_TID):
            lbl.resize(int(w * sizes[0][0]), int(h * sizes[0][1]))
            lbl.move(int(w * positions[i][0] + 435), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_TI):
            lbl.resize(int(w * sizes[1][0]), int(h * sizes[1][1]))
            lbl.move(int(w * positions[i][0] + 142), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.030), 1)))
        for i, lbl in enumerate(self.labels_PID):
            lbl.resize(int(w * sizes[2][0]), int(h * sizes[2][1]))
            lbl.move(int(w * positions[i][0] + 79), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_OID):
            lbl.resize(int(w * sizes[3][0] + 36), int(h * sizes[3][1]))
            lbl.move(int(w * positions[i][0]), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_ST):
            lbl.resize(int(w * sizes[4][0]), int(h * sizes[4][1]))
            lbl.move(int(w * positions[i][0] - 230), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_Ded):
            lbl.resize(int(w * sizes[5][0]), int(h * sizes[4][1]))
            lbl.move(int(w * positions[i][0] - 465), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))

        super().resizeEvent(event)


class Show_Task_Person(QWidget):
    def god_Help_ME(self, member, page):
        if hasattr(self, "labels_Pname"):
            for lbl in self.labels_TID:
                lbl.deleteLater()
        if hasattr(self, "labels_number"):
            for lbl in self.labels_PID:
                lbl.deleteLater()
        if hasattr(self, "labels_Name"):
            for lbl in self.labels_OID:
                lbl.deleteLater()
        if hasattr(self, "labels_Start"):
            for lbl in self.labels_Ded:
                lbl.deleteLater()
        if hasattr(self, "labels_end"):
            for lbl in self.labels_TI:
                lbl.deleteLater()
        if hasattr(self, "labels_end"):
            for lbl in self.labels_ST:
                lbl.deleteLater()
        self.labels_TID = []
        self.labels_PID = []
        self.labels_OID = []
        self.labels_Ded = []
        self.labels_TI = []
        self.labels_ST = []
        for t in member:
            print(
                f"Task: {t[0]} | Deadline: {t[1]} | Assignee ID: {t[2]} | Task: {t[3]} | Deadline: {t[4]} | Assignee ID: {t[5]}"
            )
        if (len(member) - page * 10) < 10:
            for i in range(len(member)):
                lbl = QLabel(str(member[i + page * 10][0]), self)
                lbl.setStyleSheet("color: black;")
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_TID.append(lbl)

                lbl1 = QLabel(str(member[i + page * 10][1]), self)
                lbl1.setStyleSheet("color: black;")
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_TI.append(lbl1)

                lbl2 = QLabel(str(member[i + page * 10][2]), self)
                lbl2.setStyleSheet("color: black;")
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_PID.append(lbl2)

                lbl3 = QLabel(str(member[i + page * 10][3]), self)
                lbl3.setStyleSheet("color: black;")
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_OID.append(lbl3)
                lbl4 = QLabel(str(member[i + page * 10][4]), self)
                lbl4.setStyleSheet("color: black;")
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_ST.append(lbl4)
                lbl5 = QLabel(str(member[i + page * 10][5]), self)
                lbl5.setStyleSheet("color: black;")
                lbl5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl5.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_Ded.append(lbl5)
        else:
            for i in range(10):
                lbl = QLabel(str(member[i + page * 10][0]), self)
                lbl.setStyleSheet("color: black;")
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_TID.append(lbl)

                lbl1 = QLabel(str(member[i + page * 10][1]), self)
                lbl1.setStyleSheet("color: black;")
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_TI.append(lbl1)

                lbl2 = QLabel(str(member[i + page * 10][2]), self)
                lbl2.setStyleSheet("color: black;")
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_PID.append(lbl2)

                lbl3 = QLabel(str(member[i + page * 10][3]), self)
                lbl3.setStyleSheet("color: black;")
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_OID.append(lbl3)
                lbl4 = QLabel(str(member[i + page * 10][4]), self)
                lbl4.setStyleSheet("color: black;")
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_ST.append(lbl4)
                lbl5 = QLabel(str(member[i + page * 10][5]), self)
                lbl5.setStyleSheet("color: black;")
                lbl5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl5.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_Ded.append(lbl5)

    def __init__(self, pro, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)
        self.page = 0
        self.ProList = pro
        self.db = db
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Member_show.png")
        # labes
        self.lblHeader = QLabel("لیست تسک ها", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # but
        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)
        self.btnB = QPushButton(self)
        self.btnB.setText("قبلی")
        self.btnB.clicked.connect(self.goAM)
        self.btnN = QPushButton(self)
        self.btnN.setText("بعدی")
        self.btnN.clicked.connect(self.goA)
        self.god_Help_ME(self.ProList, self.page)

    def goA(self):
        all_Page = (int(len(self.ProList) + 9) // 10) - 1
        if all_Page > self.page:
            self.page = self.page + 1
            self.god_Help_ME(self.ProList, self.page)

    def goAM(self):
        if self.page > 0:
            self.page = self.page - 1
            self.god_Help_ME(self.ProList, self.page)

    def goB(self):
        self.project_window = Task_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )

            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)

        self.btnback.resize(int(w * 0.1), int(h * 0.05))
        self.btnback.move(int(w * 0.055), int(h * 0.059))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnB.resize(int(w * 0.1), int(h * 0.05))
        self.btnB.move(int(w * 0.34), int(h * 0.85))
        self.btnB.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnN.resize(int(w * 0.1), int(h * 0.05))
        self.btnN.move(int(w * 0.54), int(h * 0.85))
        self.btnN.setFont(QFont("Vazir", max(int(h * 0.02), 1)))
        # label
        self.lblHeader.resize(int(w * 0.2), int(h * 0.3))
        self.lblHeader.move(int(w * 0.4), int(h * 0.00001 - 45))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.032), 1)))

        positions = [
            (0.5, 0.1275),
            (0.5, 0.197),
            (0.5, 0.2655),
            (0.5, 0.3360),
            (0.5, 0.4055),
            (0.5, 0.4755),
            (0.5, 0.545),
            (0.5, 0.6145),
            (0.5, 0.684),
            (0.5, 0.7535),
        ]
        sizes = [
            (0.05, 0.07),
            (0.23, 0.07),
            (0.05, 0.07),
            (0.035, 0.07),
            (0.18, 0.07),
            (0.19, 0.07),
            (0.5, 0.2),
            (0.3, 0.2),
            (0.5, 0.2),
            (0.3, 0.2),
        ]

        for i, lbl in enumerate(self.labels_TID):
            lbl.resize(int(w * sizes[0][0]), int(h * sizes[0][1]))
            lbl.move(int(w * positions[i][0] + 435), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_TI):
            lbl.resize(int(w * sizes[1][0]), int(h * sizes[1][1]))
            lbl.move(int(w * positions[i][0] + 142), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.030), 1)))
        for i, lbl in enumerate(self.labels_PID):
            lbl.resize(int(w * sizes[2][0]), int(h * sizes[2][1]))
            lbl.move(int(w * positions[i][0] + 79), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_OID):
            lbl.resize(int(w * sizes[3][0] + 36), int(h * sizes[3][1]))
            lbl.move(int(w * positions[i][0]), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_ST):
            lbl.resize(int(w * sizes[4][0]), int(h * sizes[4][1]))
            lbl.move(int(w * positions[i][0] - 230), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_Ded):
            lbl.resize(int(w * sizes[5][0]), int(h * sizes[4][1]))
            lbl.move(int(w * positions[i][0] - 465), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))

        super().resizeEvent(event)


class Search_State_Panel(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(853, 480)
        self.db = db
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Menu_Member.png")
        self.setAutoFillBackground(True)

        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)

        self.btnS = QPushButton(self)
        self.btnS.setText("جستجو")
        self.btnS_pixmap = QPixmap("UI/button_bg.png")
        self.btnS.clicked.connect(self.goSe)
        # لیبل
        self.lblHeader = QLabel("جستجو وضعیت", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lblP = QLabel("وضعیت", self)
        self.lblP.setStyleSheet("color: black;")
        self.lblP.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.combo = QComboBox(self)
        self.combo.addItems(["ToDo", "In Progress", "Done"])

    def goSe(self):
        tasks = []
        stat = self.combo.currentText()
        for m in self.db.get_tasks_by_status(stat):
            tasks.append(
                [m.id, m.TaskName, m.project_id, m.assignee_id, m.Status, m.Deadline]
            )
        self.project_window = Show_Task_Person(tasks, self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goB(self):
        self.project_window = Task_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )

            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)

        self.btnback.resize(int(w * 0.135), int(h * 0.065))
        self.btnback.move(int(w * 0.15), int(h * 0.15))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.029), 1)))

        self.btnS.resize(int(w * 0.4), int(h * 0.13))
        self.btnS.move(int(w * 0.3), int(h * 0.65))
        self.btnS.setFont(QFont("Vazir", max(int(h * 0.05), 1)))
        # لیبل
        self.lblHeader.resize(int(w * 0.3), int(h * 0.1))
        self.lblHeader.move(int(w * 0.37), int(h * 0.15))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.055), 1)))

        self.lblP.resize(int(w * 0.3), int(h * 0.15))
        self.lblP.move(int(w * 0.505), int(h * 0.4))
        self.lblP.setFont(QFont("Vazir", max(int(h * 0.04), 1)))
        # bux
        self.combo.resize(int(w * 0.25), int(h * 0.055))
        self.combo.move(int(w * 0.23), int(h * 0.45))
        self.combo.setFont(QFont("Vazir", max(int(h * 0.03), 1)))

        super().resizeEvent(event)


class Search_Project_Panel(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(853, 480)
        self.db = db
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Menu_Member.png")
        self.setAutoFillBackground(True)

        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)

        self.btnS = QPushButton(self)
        self.btnS.setText("جستجو")
        self.btnS_pixmap = QPixmap("UI/button_bg.png")
        self.btnS.clicked.connect(self.goSe)
        # لیبل
        self.lblHeader = QLabel("جستجو پروژه", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lblP = QLabel("ID پروژه :", self)
        self.lblP.setStyleSheet("color: black;")
        self.lblP.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.textbox = QLineEdit(self)

    def goSe(self):
        tasks = []
        stat = int(self.textbox.text())
        for m in self.db.get_tasks_by_project(stat):
            tasks.append(
                [m.id, m.TaskName, m.project_id, m.assignee_id, m.Status, m.Deadline]
            )
        self.project_window = Show_Task_Person(tasks, self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goB(self):
        self.project_window = Task_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )

            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)

        self.btnback.resize(int(w * 0.135), int(h * 0.065))
        self.btnback.move(int(w * 0.15), int(h * 0.15))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.029), 1)))

        self.btnS.resize(int(w * 0.4), int(h * 0.13))
        self.btnS.move(int(w * 0.3), int(h * 0.65))
        self.btnS.setFont(QFont("Vazir", max(int(h * 0.05), 1)))
        # لیبل
        self.lblHeader.resize(int(w * 0.3), int(h * 0.1))
        self.lblHeader.move(int(w * 0.365), int(h * 0.15))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.055), 1)))

        self.lblP.resize(int(w * 0.3), int(h * 0.15))
        self.lblP.move(int(w * 0.499), int(h * 0.4))
        self.lblP.setFont(QFont("Vazir", max(int(h * 0.04), 1)))
        # bux
        self.textbox.resize(int(w * 0.25), int(h * 0.055))
        self.textbox.move(int(w * 0.23), int(h * 0.45))
        self.textbox.setFont(QFont("Vazir", max(int(h * 0.04), 1)))

        super().resizeEvent(event)


class Search_Person_Panel(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(853, 480)

        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Menu_Member.png")
        self.setAutoFillBackground(True)

        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)

        self.btnS = QPushButton(self)
        self.btnS.setText("جستجو")
        self.btnS_pixmap = QPixmap("UI/button_bg.png")
        self.btnS.clicked.connect(self.goSe)
        # لیبل
        self.lblHeader = QLabel("جستجو فرد", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lblP = QLabel("ID عضو :", self)
        self.lblP.setStyleSheet("color: black;")
        self.lblP.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.textbox = QLineEdit(self)

    def goSe(self):
        tasks = []
        stat = int(self.textbox.text())
        for m in self.db.get_tasks_by_assignee(stat):
            tasks.append(
                [m.id, m.TaskName, m.project_id, m.assignee_id, m.Status, m.Deadline]
            )
        self.project_window = Show_Task_Person(tasks, self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goB(self):
        self.project_window = Task_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )

            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)

        self.btnback.resize(int(w * 0.135), int(h * 0.065))
        self.btnback.move(int(w * 0.15), int(h * 0.15))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.029), 1)))

        self.btnS.resize(int(w * 0.4), int(h * 0.13))
        self.btnS.move(int(w * 0.3), int(h * 0.65))
        self.btnS.setFont(QFont("Vazir", max(int(h * 0.05), 1)))
        # لیبل
        self.lblHeader.resize(int(w * 0.3), int(h * 0.1))
        self.lblHeader.move(int(w * 0.365), int(h * 0.15))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.055), 1)))

        self.lblP.resize(int(w * 0.3), int(h * 0.15))
        self.lblP.move(int(w * 0.499), int(h * 0.4))
        self.lblP.setFont(QFont("Vazir", max(int(h * 0.04), 1)))
        # bux
        self.textbox.resize(int(w * 0.25), int(h * 0.055))
        self.textbox.move(int(w * 0.23), int(h * 0.45))
        self.textbox.setFont(QFont("Vazir", max(int(h * 0.04), 1)))

        super().resizeEvent(event)


class Search_Project_Panel1(QWidget):
    def __init__(self, db, repo):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(853, 480)
        self.db = db
        self.repo = repo
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Menu_Member.png")
        self.setAutoFillBackground(True)

        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)

        self.btnS = QPushButton(self)
        self.btnS.setText("جستجو")
        self.btnS_pixmap = QPixmap("UI/button_bg.png")
        self.btnS.clicked.connect(self.goSe)
        # لیبل
        self.lblHeader = QLabel("جستجو پروژه", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lblP = QLabel("ID پروژه :", self)
        self.lblP.setStyleSheet("color: black;")
        self.lblP.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.textbox = QLineEdit(self)

    def goSe(self):
        tasks = []
        stat = int(self.textbox.text())
        summary = repo.project_summary(stat)
        for line in summary:
            print(line)
        self.project_window = Report_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goB(self):
        self.project_window = Report_Menu(self.db, self.repo)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )

            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)

        self.btnback.resize(int(w * 0.135), int(h * 0.065))
        self.btnback.move(int(w * 0.15), int(h * 0.15))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.029), 1)))

        self.btnS.resize(int(w * 0.4), int(h * 0.13))
        self.btnS.move(int(w * 0.3), int(h * 0.65))
        self.btnS.setFont(QFont("Vazir", max(int(h * 0.05), 1)))
        # لیبل
        self.lblHeader.resize(int(w * 0.3), int(h * 0.1))
        self.lblHeader.move(int(w * 0.365), int(h * 0.15))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.055), 1)))

        self.lblP.resize(int(w * 0.3), int(h * 0.15))
        self.lblP.move(int(w * 0.499), int(h * 0.4))
        self.lblP.setFont(QFont("Vazir", max(int(h * 0.04), 1)))
        # bux
        self.textbox.resize(int(w * 0.25), int(h * 0.055))
        self.textbox.move(int(w * 0.23), int(h * 0.45))
        self.textbox.setFont(QFont("Vazir", max(int(h * 0.04), 1)))

        super().resizeEvent(event)


class Report_Menu(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)
        self.db = db
        repo = ReportManager(db)
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Menu.png")
        self.setAutoFillBackground(True)
        # labes
        self.lblHeader = QLabel("گزارش ها", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # but
        self.btnMemMan = QPushButton(self)
        self.btnMemMan.setText("نمایش تسک های عقب مانده")
        self.btnMemMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnMemMan.clicked.connect(self.goAT)

        self.btnPMan = QPushButton(self)
        self.btnPMan.setText("نمایش خلاصه همه پروژه ها در فایل")
        self.btnPMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnPMan.clicked.connect(self.goCP)

        self.btnTMan = QPushButton(self)
        self.btnTMan.setText("نمایش خلاصه وضعیت هر پروژه")
        self.btnTMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnTMan.clicked.connect(self.goCS)

        self.btnRMan = QPushButton(self)
        self.btnRMan.setText("نمایش تسک ها با ددلاین نزدیک")
        self.btnRMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnRMan.clicked.connect(self.goSTP)

        self.btnEMan = QPushButton(self)
        self.btnEMan.setText("نمایش تسک های عقب مانده در فایل")
        self.btnEMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnEMan.clicked.connect(self.goSTM)

        self.btn1 = QPushButton(self)
        self.btn1.setText("نمایش تسک های فعال اعضا در فایل")
        self.btn1.clicked.connect(self.go1)

        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)
        # label
        self.lblHeader.resize(int(w * 0.3), int(h * 0.2))
        self.lblHeader.move(int(w * 0.38 - 30), int(h * 0.0001 - 20))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.05), 1)))
        # but
        self.btnMemMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnMemMan.move(int(w * 0.18), int(h * 0.25))
        self.btnMemMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnPMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnPMan.move(int(w * 0.53), int(h * 0.25))
        self.btnPMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnTMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnTMan.move(int(w * 0.18), int(h * 0.5))
        self.btnTMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnRMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnRMan.move(int(w * 0.53), int(h * 0.5))
        self.btnRMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnEMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnEMan.move(int(w * 0.18), int(h * 0.75))
        self.btnEMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btn1.resize(int(w * 0.33), int(h * 0.11))
        self.btn1.move(int(w * 0.53), int(h * 0.75))
        self.btn1.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnback.resize(int(w * 0.1), int(h * 0.05))
        self.btnback.move(int(w * 0.07), int(h * 0.01 + 15))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

    def goB(self):
        self.project_window = First_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goAT(self):
        tasks = []
        for m in repo.postpone_task():
            tasks.append(
                [m.id, m.TaskName, m.project_id, m.assignee_id, m.Status, m.Deadline]
            )
        self.project_window = Show_Task_Person1(tasks, self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goCS(self):
        self.project_window = Search_Project_Panel1(self.db, repo)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goCP(self):
        repo.export_all_projects_summary()

    def goSTM(self):
        repo.export_postpone_tasks_summary()

    def goSTP(self):
        tasks = []
        for m in repo.dueon_task():
            tasks.append(
                [m.id, m.TaskName, m.project_id, m.assignee_id, m.Status, m.Deadline]
            )
        self.project_window = Show_Task_Person1(tasks, self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def go1(self):
        repo.export_members_tasks()


class Change_Person_Task(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1065, 600)
        self.db = db
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_CT.png")
        self.setAutoFillBackground(True)
        # labes
        self.lblHeader = QLabel("تغییر مسئول تسک", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lblSe = QLabel(":ID تسک", self)
        self.lblSe.setStyleSheet("color: black;")
        self.lblSe.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lblSS = QLabel("مسئول :", self)
        self.lblSS.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSS.hide()

        self.lblX = QLabel("سهیل", self)
        self.lblX.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblX.hide()

        self.lblNS = QLabel(":مسئول جدید ID", self)
        self.lblNS.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblNS.hide()

        self.lblSN = QLabel("وضیعت کنونی:", self)
        self.lblSN.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSN.hide()

        self.lblSSN = QLabel("در حال انجام", self)
        self.lblSSN.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSSN.hide()
        # but
        self.btnEMan = QPushButton(self)
        self.btnEMan.setText("جست و جو")
        self.btnEMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnEMan.clicked.connect(self.Search)

        self.btnS = QPushButton("ثبت", self)
        self.btnS.hide()
        self.btnS.clicked.connect(self.Save)

        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)

        # bux
        self.textbox = QLineEdit(self)

        self.combo = QLineEdit(self)
        self.combo.hide()

    def Search(self):
        w, h = self.width(), self.height()
        self.tasks = self.db.get_all_tasks()
        self.members = self.db.get_all_members()
        for tas in self.tasks:
            if tas.id == int(self.textbox.text()):
                self.btnS.show()
                self.lblSS.show()
                for mem in self.members:
                    if mem.id == tas.assignee_id:
                        self.lblX.setText(str(mem.name))
                self.lblX.show()
                self.combo.show()
                self.lblNS.show()
                self.lblSSN.setText(str(tas.Status))
                self.lblSSN.show()
                self.lblSN.show()

    def Save(self):
        w, h = self.width(), self.height()
        id = self.textbox.text()
        don = self.combo.text()
        db.update_task_assignee(id, don)
        self.project_window = Task_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()
        self.close()

    def goB(self):
        self.project_window = Task_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)
        # label
        self.lblHeader.resize(int(w * 0.3), int(h * 0.2))
        self.lblHeader.move(int(w * 0.38 - 30), int(h * 0.0001))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.04), 1)))

        self.lblSe.resize(int(w * 0.3), int(h * 0.2))
        self.lblSe.move(int(w * 0.7), int(h * 0.18))
        self.lblSe.setFont(QFont("Vazir", max(int(h * 0.03), 1)))

        self.lblSS.resize(int(w * 0.3), int(h * 0.2))
        self.lblSS.move(int(w * 0.7), int(h * 0.48))
        self.lblSS.setFont(QFont("Vazir", max(int(h * 0.03), 1)))

        self.lblX.resize(int(w * 0.3), int(h * 0.2))
        self.lblX.move(int(w * 0.55), int(h * 0.48))
        self.lblX.setFont(QFont("Vazir", max(int(h * 0.03), 1)))

        self.lblNS.resize(int(w * 0.5), int(h * 0.2))
        self.lblNS.move(int(w * 0.59), int(h * 0.68))
        self.lblNS.setFont(QFont("Vazir", max(int(h * 0.025), 1)))

        self.lblSN.resize(int(w * 0.3), int(h * 0.2))
        self.lblSN.move(int(w * 0.30), int(h * 0.48))
        self.lblSN.setFont(QFont("Vazir", max(int(h * 0.03), 1)))

        self.lblSSN.resize(int(w * 0.3), int(h * 0.2))
        self.lblSSN.move(int(w * 0.15), int(h * 0.48))
        self.lblSSN.setFont(QFont("Vazir", max(int(h * 0.03), 1)))
        # box
        self.textbox.resize(int(w * 0.25), int(h * 0.05))
        self.textbox.move(int(w * 0.47), int(h * 0.253))
        self.textbox.setFont(QFont("Vazir", max(int(h * 0.03), 1)))

        self.combo.resize(int(w * 0.25), int(h * 0.05))
        self.combo.move(int(w * 0.475), int(h * 0.75))
        self.combo.setFont(QFont("Vazir", max(int(h * 0.02), 1)))
        # but
        self.btnEMan.resize(int(w * 0.25), int(h * 0.09))
        self.btnEMan.move(int(w * 0.12), int(h * 0.39))
        self.btnEMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnS.resize(int(w * 0.25), int(h * 0.09))
        self.btnS.move(int(w * 0.12), int(h * 0.8 + 15))
        self.btnS.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnback.resize(int(w * 0.1), int(h * 0.05))
        self.btnback.move(int(w * 0.12), int(h * 0.09))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.02), 1)))


class Change_States_Task(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1065, 600)
        self.db = db
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_CT.png")
        self.setAutoFillBackground(True)
        # labes
        self.lblHeader = QLabel("تغییر وضیعت تسک", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lblSe = QLabel(":ID تسک", self)
        self.lblSe.setStyleSheet("color: black;")
        self.lblSe.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lblSS = QLabel("مسئول :", self)
        self.lblSS.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSS.hide()

        self.lblX = QLabel("سهیل", self)
        self.lblX.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblX.hide()

        self.lblNS = QLabel("وضیعت جدید:", self)
        self.lblNS.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblNS.hide()

        self.lblSN = QLabel("وضیعت کنونی:", self)
        self.lblSN.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSN.hide()

        self.lblSSN = QLabel("در حال انجام", self)
        self.lblSSN.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblSSN.hide()
        # but
        self.btnEMan = QPushButton(self)
        self.btnEMan.setText("جست و جو")
        self.btnEMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnEMan.clicked.connect(self.Search)

        self.btnS = QPushButton("ثبت", self)
        self.btnS.hide()
        self.btnS.clicked.connect(self.Save)

        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)
        # bux
        self.textbox = QLineEdit(self)

        self.combo = QComboBox(self)
        self.combo.addItems(["ToDo", "In Progress", "Done"])
        self.combo.hide()

    def goB(self):
        self.project_window = Task_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def Search(self):
        w, h = self.width(), self.height()
        self.tasks = self.db.get_all_tasks()
        self.members = self.db.get_all_members()
        for tas in self.tasks:
            if tas.id == int(self.textbox.text()):
                self.btnS.show()
                self.lblSS.show()
                for mem in self.members:
                    if mem.id == tas.assignee_id:
                        self.lblX.setText(str(mem.name))
                self.lblX.show()
                self.combo.show()
                self.lblNS.show()
                self.lblSSN.setText(str(tas.Status))
                self.lblSSN.show()
                self.lblSN.show()

    def Save(self):
        w, h = self.width(), self.height()
        id = self.textbox.text()
        don = self.combo.currentText()
        db.update_task_status(id, don)
        self.project_window = Task_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)
        # label
        self.lblHeader.resize(int(w * 0.3), int(h * 0.2))
        self.lblHeader.move(int(w * 0.38 - 30), int(h * 0.0001))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.04), 1)))

        self.lblSe.resize(int(w * 0.3), int(h * 0.2))
        self.lblSe.move(int(w * 0.7), int(h * 0.18))
        self.lblSe.setFont(QFont("Vazir", max(int(h * 0.03), 1)))

        self.lblSS.resize(int(w * 0.3), int(h * 0.2))
        self.lblSS.move(int(w * 0.7), int(h * 0.48))
        self.lblSS.setFont(QFont("Vazir", max(int(h * 0.03), 1)))

        self.lblX.resize(int(w * 0.3), int(h * 0.2))
        self.lblX.move(int(w * 0.55), int(h * 0.48))
        self.lblX.setFont(QFont("Vazir", max(int(h * 0.03), 1)))

        self.lblNS.resize(int(w * 0.5), int(h * 0.2))
        self.lblNS.move(int(w * 0.59), int(h * 0.68))
        self.lblNS.setFont(QFont("Vazir", max(int(h * 0.025), 1)))

        self.lblSN.resize(int(w * 0.3), int(h * 0.2))
        self.lblSN.move(int(w * 0.30), int(h * 0.48))
        self.lblSN.setFont(QFont("Vazir", max(int(h * 0.03), 1)))

        self.lblSSN.resize(int(w * 0.3), int(h * 0.2))
        self.lblSSN.move(int(w * 0.15), int(h * 0.48))
        self.lblSSN.setFont(QFont("Vazir", max(int(h * 0.03), 1)))
        # box
        self.textbox.resize(int(w * 0.25), int(h * 0.05))
        self.textbox.move(int(w * 0.47), int(h * 0.253))
        self.textbox.setFont(QFont("Vazir", max(int(h * 0.03), 1)))
        # but
        self.btnEMan.resize(int(w * 0.25), int(h * 0.09))
        self.btnEMan.move(int(w * 0.12), int(h * 0.39))
        self.btnEMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnS.resize(int(w * 0.25), int(h * 0.09))
        self.btnS.move(int(w * 0.12), int(h * 0.8 + 15))
        self.btnS.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnback.resize(int(w * 0.1), int(h * 0.05))
        self.btnback.move(int(w * 0.12), int(h * 0.09))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.02), 1)))
        # combo box
        self.combo.resize(int(w * 0.25), int(h * 0.05))
        self.combo.move(int(w * 0.49), int(h * 0.75))
        self.combo.setFont(QFont("Vazir", max(int(h * 0.02), 1)))


class Add_Task(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background.png")
        # ایجاد سه لیبل
        self.labels = []
        texts = ["عنوان", "مسئول ID", "پروژه ID", "تاریخ دد لاین", "/", "/"]
        lbl = QLabel("افزودن تسک", self)
        lbl.setStyleSheet("color: black;")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labels.append(lbl)
        for text in texts:
            lbl = QLabel(text, self)
            lbl.setStyleSheet("color: black;")
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.labels.append(lbl)
        # bux
        self.textbox = QLineEdit(self)
        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        self.textbox4 = QLineEdit(self)
        self.textbox5 = QLineEdit(self)
        # but
        self.btn = QPushButton(self)
        self.btn.setText("ثبت")
        self.btn_pixmap = QPixmap("UI/button_bg.png")
        self.btn.clicked.connect(self.goS)

        self.btnB = QPushButton(self)
        self.btnB.setText("برگشت")
        self.btnB_pixmap = QPixmap("UI/button_bg.png")
        self.btnB.clicked.connect(self.goB)

    def goB(self):
        self.project_window = Task_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goS(self):
        name = self.textbox.text()
        MeID = self.textbox1.text()
        PeoID = self.textbox2.text()
        SY = self.textbox5.text()
        SM = self.textbox4.text()
        SD = self.textbox3.text()
        start = f"{SY}-{SM}-{SD}"
        db.CreateTask(Task(name, "باید آپدیت شود", MeID, start, "ToDo"), PeoID, MeID)
        self.project_window = Task_Menu(db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # but
        self.btn.resize(int(w * 0.25), int(h * 0.08))
        self.btn.move(int(w * 0.6), int(h * 0.8))
        self.btn.setFont(QFont("Vazir", max(int(h * 0.02), 1)))
        # box
        self.textbox.resize(int(w * 0.2), int(h * 0.04))
        self.textbox.move(int(w * 0.59), int(h * 0.185))
        self.textbox.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox1.resize(int(w * 0.2), int(h * 0.04))
        self.textbox1.move(int(w * 0.59), int(h * 0.33))
        self.textbox1.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox2.resize(int(w * 0.2), int(h * 0.04))
        self.textbox2.move(int(w * 0.59), int(h * 0.475))
        self.textbox2.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox3.resize(int(w * 0.036), int(h * 0.04))
        self.textbox3.move(int(w * 0.732), int(h * 0.63))
        self.textbox3.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox4.resize(int(w * 0.036), int(h * 0.04))
        self.textbox4.move(int(w * 0.672), int(h * 0.63))
        self.textbox4.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox5.resize(int(w * 0.06), int(h * 0.04))
        self.textbox5.move(int(w * 0.59), int(h * 0.63))
        self.textbox5.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        #
        self.btnB.resize(int(w * 0.07), int(h * 0.05))
        self.btnB.move(int(w * 0.52), int(h * 0.05))
        self.btnB.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        # label
        positions = [
            (0.55, 0.00005),
            (0.75, 0.1),
            (0.75, 0.25),
            (0.75, 0.40),
            (0.75, 0.55),
            (0.512, 0.552),
            (0.569, 0.552),
        ]
        sizes = [
            (0.4, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
        ]

        for i, lbl in enumerate(self.labels):
            if i == 0:
                lbl.resize(int(w * sizes[i][0]), int(h * sizes[i][1]))
                lbl.move(int(w * positions[i][0]), int(h * positions[i][1] - 20))
                lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
            else:
                lbl.resize(int(w * sizes[i][0]), int(h * sizes[i][1]))
                lbl.move(int(w * positions[i][0]), int(h * positions[i][1]))
                lbl.setFont(QFont("Vazir", max(int(h * 0.025), 1)))

        scaled_pixmap = self.pixmap.scaled(
            self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
        )
        palette = self.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

        super().resizeEvent(event)

    def selection_changed(self, index):
        print(f"Selected: {self.combo.currentText()}")


class Task_Menu(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)

        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Menu.png")
        self.setAutoFillBackground(True)
        # labes
        self.lblHeader = QLabel("مدیریت تسک ها", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # but
        self.btnMemMan = QPushButton(self)
        self.btnMemMan.setText("ساخت تسک جدید")
        self.btnMemMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnMemMan.clicked.connect(self.goAT)

        self.btnPMan = QPushButton(self)
        self.btnPMan.setText("تغییر وضیعت تسک")
        self.btnPMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnPMan.clicked.connect(self.goCP)

        self.btnTMan = QPushButton(self)
        self.btnTMan.setText("تغییر مسئول تسک")
        self.btnTMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnTMan.clicked.connect(self.goCS)

        self.btnRMan = QPushButton(self)
        self.btnRMan.setText("نمایش تسک های یک پروژه")
        self.btnRMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnRMan.clicked.connect(self.goSTP)

        self.btnEMan = QPushButton(self)
        self.btnEMan.setText("نمایش تسک های یک عضو")
        self.btnEMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnEMan.clicked.connect(self.goSTM)

        self.btnD = QPushButton(self)
        self.btnD.setText("نمایش تسک بر اساس حالت")
        self.btnD.clicked.connect(self.goSTMD)

        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)
        # label
        self.lblHeader.resize(int(w * 0.3), int(h * 0.2))
        self.lblHeader.move(int(w * 0.38 - 30), int(h * 0.0001 - 20))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.05), 1)))
        # but
        self.btnMemMan.resize(int(w * 0.27), int(h * 0.09))
        self.btnMemMan.move(int(w * 0.32 + 60), int(h * 0.2))
        self.btnMemMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnPMan.resize(int(w * 0.27), int(h * 0.09))
        self.btnPMan.move(int(w * 0.32 + 60), int(h * 0.33))
        self.btnPMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnTMan.resize(int(w * 0.27), int(h * 0.09))
        self.btnTMan.move(int(w * 0.32 + 60), int(h * 0.46))
        self.btnTMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnRMan.resize(int(w * 0.27), int(h * 0.09))
        self.btnRMan.move(int(w * 0.32 + 60), int(h * 0.59))
        self.btnRMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnEMan.resize(int(w * 0.27), int(h * 0.09))
        self.btnEMan.move(int(w * 0.32 + 60), int(h * 0.72))
        self.btnEMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnback.resize(int(w * 0.1), int(h * 0.05))
        self.btnback.move(int(w * 0.07), int(h * 0.01 + 15))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnD.resize(int(w * 0.27), int(h * 0.09))
        self.btnD.move(int(w * 0.32 + 60), int(h * 0.85))
        self.btnD.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

    def goB(self):
        self.project_window = First_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goAT(self):
        self.project_window = Add_Task(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goCS(self):
        self.project_window = Change_Person_Task(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goCP(self):
        self.project_window = Change_States_Task(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goSTM(self):
        self.project_window = Search_Person_Panel(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goSTP(self):
        self.project_window = Search_Project_Panel(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goSTMD(self):
        self.project_window = Search_State_Panel(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()


class Show_Project(QWidget):
    def god_Help_ME(self, member, page):
        if hasattr(self, "labels_Pname"):
            for lbl in self.labels_Pname:
                lbl.deleteLater()
        if hasattr(self, "labels_number"):
            for lbl in self.labels_number:
                lbl.deleteLater()
        if hasattr(self, "labels_Name"):
            for lbl in self.labels_Name:
                lbl.deleteLater()
        if hasattr(self, "labels_Start"):
            for lbl in self.labels_Start:
                lbl.deleteLater()
        if hasattr(self, "labels_end"):
            for lbl in self.labels_end:
                lbl.deleteLater()
        self.labels_Pname = []
        self.labels_number = []
        self.labels_Name = []
        self.labels_Start = []
        self.labels_end = []
        if (len(member) - page * 10) < 10:
            for i in range(len(member)):
                lbl = QLabel(str(member[i + page * 10][0]), self)
                lbl.setStyleSheet("color: black;")
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_Pname.append(lbl)

                lbl1 = QLabel(str(i + 1 + page * 10), self)
                lbl1.setStyleSheet("color: black;")
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_number.append(lbl1)

                lbl2 = QLabel(str(member[i + page * 10][2]), self)
                lbl2.setStyleSheet("color: black;")
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_Name.append(lbl2)

                lbl3 = QLabel(str(member[i + page * 10][3]), self)
                lbl3.setStyleSheet("color: black;")
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_Start.append(lbl3)
                lbl4 = QLabel(str(member[i + page * 10][4]), self)
                lbl4.setStyleSheet("color: black;")
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_end.append(lbl4)
        else:
            for i in range(10):
                lbl = QLabel(str(member[i + page * 10][0]), self)
                lbl.setStyleSheet("color: black;")
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_Pname.append(lbl)

                lbl1 = QLabel(str(i + 1 + page * 10), self)
                lbl1.setStyleSheet("color: black;")
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_number.append(lbl1)

                lbl2 = QLabel(str(member[i + page * 10][2]), self)
                lbl2.setStyleSheet("color: black;")
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_Name.append(lbl2)

                lbl3 = QLabel(str(member[i + page * 10][3]), self)
                lbl3.setStyleSheet("color: black;")
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px black;
                    border-left: 2px black;
                """
                )
                self.labels_Start.append(lbl3)
                lbl4 = QLabel(str(member[i + page * 10][4]), self)
                lbl4.setStyleSheet("color: black;")
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl4.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_end.append(lbl4)

    def __init__(self, pro, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)
        self.page = 0
        self.ProList = pro
        self.db = db
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Member_show.png")
        # labes
        self.lblHeader = QLabel("لیست پروژه ها", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # but
        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)
        self.btnB = QPushButton(self)
        self.btnB.setText("قبلی")
        self.btnB.clicked.connect(self.goAM)
        self.btnN = QPushButton(self)
        self.btnN.setText("بعدی")
        self.btnN.clicked.connect(self.goA)
        self.god_Help_ME(self.ProList, self.page)

    def goA(self):
        all_Page = (int(len(self.ProList) + 9) // 10) - 1
        if all_Page > self.page:
            self.page = self.page + 1
            self.god_Help_ME(self.ProList, self.page)

    def goAM(self):
        if self.page > 0:
            self.page = self.page - 1
            self.god_Help_ME(self.ProList, self.page)

    def goB(self):
        self.project_window = Project_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )

            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)

        self.btnback.resize(int(w * 0.1), int(h * 0.05))
        self.btnback.move(int(w * 0.055), int(h * 0.059))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnB.resize(int(w * 0.1), int(h * 0.05))
        self.btnB.move(int(w * 0.34), int(h * 0.85))
        self.btnB.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnN.resize(int(w * 0.1), int(h * 0.05))
        self.btnN.move(int(w * 0.54), int(h * 0.85))
        self.btnN.setFont(QFont("Vazir", max(int(h * 0.02), 1)))
        # label
        self.lblHeader.resize(int(w * 0.2), int(h * 0.3))
        self.lblHeader.move(int(w * 0.4), int(h * 0.00001 - 45))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.032), 1)))

        positions = [
            (0.5, 0.1275),
            (0.5, 0.197),
            (0.5, 0.2655),
            (0.5, 0.3360),
            (0.5, 0.4055),
            (0.5, 0.4755),
            (0.5, 0.545),
            (0.5, 0.6145),
            (0.5, 0.684),
            (0.5, 0.7535),
        ]
        sizes = [
            (0.05, 0.07),
            (0.22, 0.07),
            (0.17, 0.07),
            (0.16, 0.07),
            (0.16, 0.07),
            (0.3, 0.2),
            (0.5, 0.2),
            (0.3, 0.2),
            (0.5, 0.2),
            (0.3, 0.2),
        ]

        for i, lbl in enumerate(self.labels_number):
            lbl.resize(int(w * sizes[0][0]), int(h * sizes[0][1]))
            lbl.move(int(w * positions[i][0] + 435), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_Pname):
            lbl.resize(int(w * sizes[1][0]), int(h * sizes[1][1]))
            lbl.move(int(w * positions[i][0] + 155), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.030), 1)))
        for i, lbl in enumerate(self.labels_Name):
            lbl.resize(int(w * sizes[2][0]), int(h * sizes[2][1]))
            lbl.move(int(w * positions[i][0] - 58), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_Start):
            lbl.resize(int(w * sizes[3][0]), int(h * sizes[3][1]))
            lbl.move(int(w * positions[i][0] - 261), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_end):
            lbl.resize(int(w * sizes[4][0]), int(h * sizes[4][1]))
            lbl.move(int(w * positions[i][0] - 465), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))

        super().resizeEvent(event)


class ADD_Project(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)
        self.db = db
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background.png")

        self.labels = []
        texts = [
            " عنوان :",
            " توضیح کوتاه :",
            "مدیر پروژه : ID",
            "تاریخ شروع :",
            "تاریخ پایان :",
            "/",
            "/",
            "/",
            "/",
        ]
        lbl = QLabel("ساخت پروژه", self)
        lbl.setStyleSheet("color: black;")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labels.append(lbl)
        for text in texts:
            lbl = QLabel(text, self)
            lbl.setStyleSheet("color: black;")
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.labels.append(lbl)
        self.textbox = QLineEdit(self)
        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        self.textbox4 = QLineEdit(self)
        self.textbox5 = QLineEdit(self)
        self.textbox6 = QLineEdit(self)
        self.textbox7 = QLineEdit(self)
        self.textbox8 = QLineEdit(self)
        # but
        self.btn = QPushButton(self)
        self.btn.setText("ثبت")
        self.btn_pixmap = QPixmap("UI/button_bg.png")
        self.btn.clicked.connect(self.goS)
        self.btnB = QPushButton(self)
        self.btnB.setText("برگشت")
        self.btnB_pixmap = QPixmap("UI/button_bg.png")
        self.btnB.clicked.connect(self.goB)

    def goS(self):
        name = self.textbox.text()
        dis = self.textbox1.text()
        man = self.textbox2.text()
        SY = self.textbox5.text()
        SM = self.textbox4.text()
        SD = self.textbox3.text()
        EY = self.textbox8.text()
        EM = self.textbox7.text()
        ED = self.textbox6.text()
        start = f"{SY}-{SM}-{SD}"
        end = f"{EY}-{EM}-{ED}"
        db.create_project(Project(name, dis, man, start, end), man)
        self.project_window = Project_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goB(self):
        self.project_window = Project_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # but
        self.btn.resize(int(w * 0.25), int(h * 0.08))
        self.btn.move(int(w * 0.6), int(h * 0.8))
        self.btn.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnB.resize(int(w * 0.07), int(h * 0.05))
        self.btnB.move(int(w * 0.52), int(h * 0.05))
        self.btnB.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        # box
        self.textbox.resize(int(w * 0.2), int(h * 0.036))
        self.textbox.move(int(w * 0.57), int(h * 0.205))
        self.textbox.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox1.resize(int(w * 0.2), int(h * 0.036))
        self.textbox1.move(int(w * 0.57), int(h * 0.345))
        self.textbox1.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox2.resize(int(w * 0.2), int(h * 0.036))
        self.textbox2.move(int(w * 0.57), int(h * 0.467))
        self.textbox2.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox3.resize(int(w * 0.036), int(h * 0.04))
        self.textbox3.move(int(w * 0.712), int(h * 0.598))
        self.textbox3.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox4.resize(int(w * 0.036), int(h * 0.04))
        self.textbox4.move(int(w * 0.652), int(h * 0.598))
        self.textbox4.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox5.resize(int(w * 0.06), int(h * 0.04))
        self.textbox5.move(int(w * 0.57), int(h * 0.598))
        self.textbox5.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox6.resize(int(w * 0.036), int(h * 0.04))
        self.textbox6.move(int(w * 0.712), int(h * 0.728))
        self.textbox6.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox7.resize(int(w * 0.036), int(h * 0.04))
        self.textbox7.move(int(w * 0.652), int(h * 0.728))
        self.textbox7.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox8.resize(int(w * 0.06), int(h * 0.04))
        self.textbox8.move(int(w * 0.57), int(h * 0.728))
        self.textbox8.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        # label
        positions = [
            (0.57, 0.00005),
            (0.75, 0.12),
            (0.75, 0.26),
            (0.75, 0.39),
            (0.75, 0.52),
            (0.75, 0.65),
            (0.492, 0.52),
            (0.549, 0.52),
            (0.494, 0.65),
            (0.551, 0.65),
        ]
        sizes = [
            (0.4, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
            (0.3, 0.2),
        ]

        for i, lbl in enumerate(self.labels):
            lbl.resize(int(w * sizes[i][0]), int(h * sizes[i][1]))
            lbl.move(int(w * positions[i][0]), int(h * positions[i][1]))
            if i == 0:
                lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
            else:
                lbl.setFont(QFont("Vazir", max(int(h * 0.025), 1)))

        scaled_pixmap = self.pixmap.scaled(
            self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
        )
        palette = self.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

        super().resizeEvent(event)


class Project_Menu(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)
        self.db = db
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Menu_Member.png")
        self.setAutoFillBackground(True)
        # labes
        self.lblHeader = QLabel("مدیریت پروژه ها", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # but
        self.btnMemMan = QPushButton(self)
        self.btnMemMan.setText("ساخت پروژه جدید")
        self.btnMemMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnMemMan.clicked.connect(self.goMP)

        self.btnPMan = QPushButton(self)
        self.btnPMan.setText("نمایش همه ی پروژه ها")
        self.btnPMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnPMan.clicked.connect(self.goSP)

        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)
        # label
        self.lblHeader.resize(int(w * 0.4), int(h * 0.2))
        self.lblHeader.move(int(w * 0.31), int(h * 0.13))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.055), 1)))
        # but
        self.btnMemMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnMemMan.move(int(w * 0.34), int(h * 0.43))
        self.btnMemMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnPMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnPMan.move(int(w * 0.34), int(h * 0.63))
        self.btnPMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnback.resize(int(w * 0.1), int(h * 0.05))
        self.btnback.move(int(w * 0.14), int(h * 0.15))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

    def goB(self):
        self.project_window = First_Menu(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goMP(self):
        self.project_window = ADD_Project(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goSP(self):
        members_list = []
        for m in self.db.get_all_projects():
            members_list.append(
                [m.ProjectName, m.Description, m.id, m.StartDate, m.EndDate]
            )  ##########ایدی مسئول اسمش چیه فعلا یه چیزی میزارم
        self.project_window = Show_Project(members_list, self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()


class Member_show(QWidget):
    page = 0

    def god_Help_ME(self, member, page):
        if hasattr(self, "labels_name"):
            for lbl in self.labels_name:
                lbl.deleteLater()
        if hasattr(self, "labels_number"):
            for lbl in self.labels_number:
                lbl.deleteLater()
        if hasattr(self, "labels_email"):
            for lbl in self.labels_email:
                lbl.deleteLater()
        if hasattr(self, "labels_do"):
            for lbl in self.labels_do:
                lbl.deleteLater()
        self.labels_name = []
        self.labels_number = []
        self.labels_email = []
        self.labels_do = []
        if (len(member) - page * 10) < 10:
            for i in range(len(member) - page * 10):
                lbl = QLabel(str(member[i + page * 10][0]), self)
                lbl.setStyleSheet("color: black;")
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_name.append(lbl)

                lbl1 = QLabel(str(i + 1 + page * 10), self)
                lbl1.setStyleSheet("color: black;")
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_number.append(lbl1)

                lbl2 = QLabel(str(member[i + page * 10][2]), self)
                lbl2.setStyleSheet("color: black;")
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_email.append(lbl2)

                lbl3 = QLabel(str(member[i + page * 10][1]), self)
                lbl3.setStyleSheet("color: black;")
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_do.append(lbl3)
        else:
            for i in range(10):
                lbl = QLabel(str(member[i + page * 10][0]), self)
                lbl.setStyleSheet("color: black;")
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);  
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_name.append(lbl)

                lbl1 = QLabel(str(i + 1 + page * 10), self)
                lbl1.setStyleSheet("color: black;")
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl1.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_number.append(lbl1)

                lbl2 = QLabel(str(member[i + page * 10][2]), self)
                lbl2.setStyleSheet("color: black;")
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl2.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_email.append(lbl2)

                lbl3 = QLabel(str(member[i + page * 10][1]), self)
                lbl3.setStyleSheet("color: black;")
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                lbl3.setStyleSheet(
                    """
                    color: black;
                    background-color: rgba(255,255,255,0);   
                    border-bottom: 2px solid gray;
                    border-left: 2px solid gray;
                """
                )
                self.labels_do.append(lbl3)

    def __init__(self, member, db):
        super().__init__()
        self.page = 0
        self.memberList = member
        self.db = db
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)

        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Member_show.png")
        # labes
        self.lblHeader = QLabel("لیست اعضا", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # but
        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)
        self.btnB = QPushButton(self)
        self.btnB.setText("قبلی")
        self.btnB.clicked.connect(self.goAM)
        self.btnN = QPushButton(self)
        self.btnN.setText("بعدی")
        self.btnN.clicked.connect(self.goA)
        self.god_Help_ME(self.memberList, self.page)

    def goA(self):
        all_Page = (int(len(self.memberList) + 9) // 10) - 1
        if all_Page > self.page:
            self.page = self.page + 1
            self.god_Help_ME(self.memberList, self.page)

    def goAM(self):
        if self.page > 0:
            self.page = self.page - 1
            self.god_Help_ME(self.memberList, self.page)

    def goB(self):
        self.project_window = First_Menu_Member(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )

            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)

        self.btnback.resize(int(w * 0.1), int(h * 0.05))
        self.btnback.move(int(w * 0.055), int(h * 0.059))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnB.resize(int(w * 0.1), int(h * 0.05))
        self.btnB.move(int(w * 0.34), int(h * 0.85))
        self.btnB.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnN.resize(int(w * 0.1), int(h * 0.05))
        self.btnN.move(int(w * 0.54), int(h * 0.85))
        self.btnN.setFont(QFont("Vazir", max(int(h * 0.02), 1)))
        # label
        self.lblHeader.resize(int(w * 0.2), int(h * 0.3))
        self.lblHeader.move(int(w * 0.4), int(h * 0.00001 - 45))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.032), 1)))

        positions = [
            (0.5, 0.1275),
            (0.5, 0.197),
            (0.5, 0.2655),
            (0.5, 0.3360),
            (0.5, 0.4055),
            (0.5, 0.4750),
            (0.5, 0.5445),
            (0.5, 0.6140),
            (0.5, 0.6835),
            (0.5, 0.7530),
        ]
        sizes = [
            (0.05, 0.07),
            (0.178, 0.07),
            (0.40, 0.07),
            (0.138, 0.07),
            (0.1, 0.05),
            (0.3, 0.2),
            (0.5, 0.2),
            (0.3, 0.2),
            (0.5, 0.2),
            (0.3, 0.2),
        ]

        for i, lbl in enumerate(self.labels_number):
            lbl.resize(int(w * sizes[0][0]), int(h * sizes[0][1]))
            lbl.move(int(w * positions[i][0] + 435), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_name):
            lbl.resize(int(w * sizes[1][0]), int(h * sizes[1][1]))
            lbl.move(int(w * positions[i][0] + 208), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_email):
            lbl.resize(int(w * sizes[2][0]), int(h * sizes[2][1]))
            lbl.move(int(w * positions[i][0] - 292), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
        for i, lbl in enumerate(self.labels_do):
            lbl.resize(int(w * sizes[3][0]), int(h * sizes[3][1]))
            lbl.move(int(w * positions[i][0] - 465), int(h * positions[i][1]))
            lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))

        super().resizeEvent(event)


class ADDMemberWin(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)
        self.db = db
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background.png")

        self.labels = []
        texts = ["نام و نام خانوادگی", "نقش", "ایمیل"]
        lbl = QLabel("افزودن عضو", self)
        lbl.setStyleSheet("color: black;")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labels.append(lbl)
        for text in texts:
            lbl = QLabel(text, self)
            lbl.setStyleSheet("color: black;")
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.labels.append(lbl)
        self.textbox = QLineEdit(self)
        self.textbox1 = QLineEdit(self)
        # ComboBox
        self.combo = QComboBox(self)
        options = ["مدیر", "معاون", "کارمند ساده"]
        self.combo.addItems(options)
        # but
        self.btn = QPushButton(self)
        self.btn.setText("ثبت")
        self.btn_pixmap = QPixmap("UI/button_bg.png")
        self.btn.clicked.connect(self.goS)
        self.btnB = QPushButton(self)
        self.btnB.setText("برگشت")
        self.btnB_pixmap = QPixmap("UI/button_bg.png")
        self.btnB.clicked.connect(self.goB)

    def goS(self):
        name = self.textbox.text()
        email = self.textbox1.text()
        role = self.combo.currentText()
        self.db.addMemberdb(Member(name, role, email))
        self.project_window = First_Menu_Member(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goB(self):
        self.project_window = First_Menu_Member(self.db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # but
        self.btn.resize(int(w * 0.25), int(h * 0.08))
        self.btn.move(int(w * 0.6), int(h * 0.8))
        self.btn.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnB.resize(int(w * 0.07), int(h * 0.05))
        self.btnB.move(int(w * 0.52), int(h * 0.05))
        self.btnB.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        # combo box
        self.combo.resize(int(w * 0.201), int(h * 0.04))
        self.combo.move(int(w * 0.57), int(h * 0.428))
        self.combo.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        # box
        self.textbox.resize(int(w * 0.2), int(h * 0.04))
        self.textbox.move(int(w * 0.57), int(h * 0.245))
        self.textbox.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.textbox1.resize(int(w * 0.2), int(h * 0.04))
        self.textbox1.move(int(w * 0.57), int(h * 0.605))
        self.textbox1.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        # label
        positions = [(0.57, 0.00005), (0.75, 0.17), (0.75, 0.35), (0.75, 0.53)]
        sizes = [(0.4, 0.2), (0.3, 0.2), (0.3, 0.2), (0.3, 0.2)]

        for i, lbl in enumerate(self.labels):
            lbl.resize(int(w * sizes[i][0]), int(h * sizes[i][1]))
            lbl.move(int(w * positions[i][0]), int(h * positions[i][1]))
            if i == 0:
                lbl.setFont(QFont("Vazir", max(int(h * 0.035), 1)))
            else:
                lbl.setFont(QFont("Vazir", max(int(h * 0.025), 1)))

        scaled_pixmap = self.pixmap.scaled(
            self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
        )
        palette = self.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

        super().resizeEvent(event)


class First_Menu_Member(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)

        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Menu_Member.png")
        self.setAutoFillBackground(True)
        # labes
        self.lblHeader = QLabel("مدیریت اعضای تیم", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # but
        self.btnMemMan = QPushButton(self)
        self.btnMemMan.setText("افزودن عضو جدید")
        self.btnMemMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnMemMan.clicked.connect(self.goAM)

        self.btnPMan = QPushButton(self)
        self.btnPMan.setText("نمایش همه ی اعضا")
        self.btnPMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnPMan.clicked.connect(self.goSM)

        self.btnback = QPushButton(self)
        self.btnback.setText("برگشت")
        self.btnback_pixmap = QPixmap("UI/button_bg.png")
        self.btnback.clicked.connect(self.goB)

    def goB(self):
        self.project_window = First_Menu(db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goAM(self):
        self.project_window = ADDMemberWin(db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goSM(self):
        members_list = []
        for m in db.get_all_members():
            members_list.append([m.name, m.role, m.email])
        self.project_window = Member_show(members_list, db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)
        # label
        self.lblHeader.resize(int(w * 0.4), int(h * 0.2))
        self.lblHeader.move(int(w * 0.31), int(h * 0.13))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.055), 1)))
        # but
        self.btnMemMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnMemMan.move(int(w * 0.34), int(h * 0.43))
        self.btnMemMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnPMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnPMan.move(int(w * 0.34), int(h * 0.63))
        self.btnPMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnback.resize(int(w * 0.1), int(h * 0.05))
        self.btnback.move(int(w * 0.14), int(h * 0.15))
        self.btnback.setFont(QFont("Vazir", max(int(h * 0.02), 1)))


class First_Menu(QWidget):
    def __init__(self, db):
        super().__init__()

        self.setWindowTitle("Responsive Background & Buttons")
        self.resize(1278, 720)
        # عکس بک‌گراند
        self.pixmap = QPixmap("UI/background_Menu.png")
        self.setAutoFillBackground(True)
        # labes
        self.lblHeader = QLabel("منو", self)
        self.lblHeader.setStyleSheet("color: black;")
        self.lblHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # but
        self.btnMemMan = QPushButton(self)
        self.btnMemMan.setText("مدیریت اعضای تیم")
        self.btnMemMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnMemMan.clicked.connect(self.goMM)

        self.btnPMan = QPushButton(self)
        self.btnPMan.setText("مدیریت پروژه ها")
        self.btnPMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnPMan.clicked.connect(self.goMP)

        self.btnTMan = QPushButton(self)
        self.btnTMan.setText("مدیریت تسک ها")
        self.btnTMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnTMan.clicked.connect(self.goMT)

        self.btnRMan = QPushButton(self)
        self.btnRMan.setText("گزارش ها")
        self.btnRMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnRMan.clicked.connect(self.goMR)

        self.btnEMan = QPushButton(self)
        self.btnEMan.setText("خروج")
        self.btnEMan_pixmap = QPixmap("UI/button_bg.png")
        self.btnEMan.clicked.connect(self.goME)

    def goMM(self):
        self.project_window = First_Menu_Member(db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goMP(self):
        pass
        self.project_window = Project_Menu(db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goMT(self):
        self.project_window = Task_Menu(db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goMR(self):
        self.project_window = Report_Menu(db)
        self.project_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.project_window.show()
        self.close()

    def goME(self):
        self.close()

    def resizeEvent(self, event):
        w, h = self.width(), self.height()
        # بک‌گراند proportional
        if not self.pixmap.isNull():
            scaled_pixmap = self.pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)
        # label
        self.lblHeader.resize(int(w * 0.2), int(h * 0.2))
        self.lblHeader.move(int(w * 0.38), int(h * 0.0001))
        self.lblHeader.setFont(QFont("Vazir", max(int(h * 0.06), 1)))
        # but
        self.btnMemMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnMemMan.move(int(w * 0.32), int(h * 0.2))
        self.btnMemMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnPMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnPMan.move(int(w * 0.32), int(h * 0.35))
        self.btnPMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnTMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnTMan.move(int(w * 0.32), int(h * 0.5))
        self.btnTMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnRMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnRMan.move(int(w * 0.32), int(h * 0.65))
        self.btnRMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))

        self.btnEMan.resize(int(w * 0.33), int(h * 0.11))
        self.btnEMan.move(int(w * 0.32), int(h * 0.8))
        self.btnEMan.setFont(QFont("Vazir", max(int(h * 0.02), 1)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    create_tables()
    db = DatabaseManager("TaskManagement.db")
    repo = ReportManager(db)
    window = First_Menu(db)
    window.show()
    sys.exit(app.exec())
