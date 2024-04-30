import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QDialog, QVBoxLayout, QScrollArea, QFrame, QPushButton
import _MLPs
data = [
        'Đưa ra những ý tưởng mới, ý tưởng đột phá',
        'Tranh luận bằng các chứng cứ khoa học',
        'Nhìn nhận vấn đề đầy đủ, tìm ra các mối liên kết giữa các vấn đề',
        'Diễn đạt vấn đề bằng nhiều cách khác nhau',
        'Đánh giá sự vật sự việc khách quan công bằng',
        'Phân tách vấn đề lớn thành nhiều phẩn nhỏ, giải quyết các phần nhỏ',
        'Có khả năng tự xử lý khi gặp khó khăn',
        'Tìm cách bố trí lại những nguyên tắc có thể thay đổi được mà không ảnh hưởng kết quả',
        'Đem nhiều thứ kết hợp lại với nhau bằng cách nối hoặc sắp xếp, liên kết để xác nhập chúng với nhau',
        'Đưa đối tượng nghiên cứu vào một tình thế mới, đưa ra khỏi môi trường quen thuộc',
        'Đổi ngược chức năng của chủ thể giúp hình thành những ý tưởng mới',
        'Thay đổi tỉ lệ, làm cho đối tượng nhỏ hơn',
        'Đánh giá, chọn lọc, góp ý tích cực với quan điểm lạ, bất thường',
        'Tư duy đa chiều',
        'Lắng nghe, tìm được vấn đề cốt lõi',
        'Có tầm nhìn xa, lên kế hoạch chu đáo',
        'Thu thập thông tin đa chiều',
        'Giữ vững lập trường, kiên định với ý kiến của mình',
        'Đặt mình vào vị trí của người khác để thực sự hiểu họ',
        'Khả năng đột nhiên phát hiện các đặc điểm tính cách  hoặc trạng thái cảm xúc mà họ đang có',
        'Tìm câu trả lời cho một vấn đề ngay lập tức mà không cần phân tích nó',
        'Chọn cách tốt nhất để vượt qua hoặc vượt qua khó khăn cá nhân mà không cần thêm kiến thức về vấn đề này',
        'Không nghi ngờ kinh nghiệm chủ quan của mình',
        'Để bản thân “chảy” tự do hơn',
        'Rèn luyện trực giác thông qua thiền định',
        'Tập trung vào cảm giác hơn là lý trí',
        'Tự đưa ra quyết định cho bản thân',
        'Tham gia vào các cuộc thảo luận, tranh luận với người khác',
        'Có khả năng thích ứng với những đối tượng, đồng đội khác nhau',
        'Cung cấp chứng cứ và logic để hỗ trợ quan điểm của mình',
        'Giữ thái độ kiên định, trung thành với những điều bản thân tin là đúng',
        'Biết nhận diện những lập luận phi logic'
]
result = [
    'Tư duy khoa học',
    'Tư duy hệ thống',
    'Tư duy tổng hợp',
    'Tư duy sáng tạo',
    'Tư duy chiến thuật',
    'Tư duy phản biện',
    'Tư duy trực quan',
    'Tư duy phân tích',
    'Tư duy độc lập',
    'Tư duy logic',
    ]
a = [0]*32
class MainWindow(QWidget):
    def change_radio(self, index):
    # Kiểm tra xem radio button nào đang được chọn
        if self.radio_yes_list[index].isChecked():
           self.b[index] += 1
        else:
            self.radio_yes_list[index].setChecked(0)
            self.b[index] = 0
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        scroll_area = QScrollArea()  # Tạo một QScrollArea để cuộn nội dung
        scroll_content = QWidget()  # Tạo một QWidget để chứa nội dung

        layout = QVBoxLayout(scroll_content)  # Tạo một QVBoxLayout cho scroll_content

        # Tạo 32 câu hỏi và thêm chúng vào layout
        self.b = [0]*32
        self.radio_yes_list = []  # Danh sách chứa các radiobutton
        for i in range(0, 32):
            self.a = 1
            frame = QFrame()  # Tạo một QFrame cho mỗi câu hỏi
            frame.setFrameShape(QFrame.Box)  # Thiết lập kiểu frame
            frame_layout = QVBoxLayout(frame)  # Tạo một QVBoxLayout cho frame

            question_text = QLabel(str(i + 1) + ". " + str(data[i]))
            frame_layout.addWidget(question_text)

            radio_yes = QRadioButton('Có')
            frame_layout.addWidget(radio_yes)
            radio_yes.clicked.connect(lambda _, idx=i: self.change_radio(idx))  # Sử dụng lambda function để truyền index
            self.radio_yes_list.append(radio_yes)  # Thêm radiobutton vào danh sách

            radio_no = QRadioButton('Không')
            frame_layout.addWidget(radio_no)
            radio_no.clicked.connect(lambda _, idx=i: self.change_radio(idx))
            layout.addWidget(frame)

        # Thêm nút

        # Đặt widget của QScrollArea là scroll_content
        scroll_area.setWidget(scroll_content)

        # Đặt layout của cửa sổ chính là QVBoxLayout
        self.setLayout(QVBoxLayout())

        # Thêm QScrollArea vào layout của cửa sổ chính
        self.layout().addWidget(scroll_area)

        self.setWindowTitle("Câu hỏi")

        open_dialog_button = QPushButton("Kết Quả", self)
        open_dialog_button.clicked.connect(self.open_dialog)
        layout.addWidget(open_dialog_button)

        self.setLayout(layout)

    def open_dialog(self):
        # Tạo cửa sổ mới
        dialog = Dialog(self.b)
        dialog.exec_()

class Dialog(QDialog):
    def __init__(self, b, parent=None):
        super().__init__(parent)
        self.b = b
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Kết Quả")
        self.setGeometry(400, 400, 600, 600)
        layout = QVBoxLayout()
        for i in range(len(self.b)):
            if self.b[i] != 0:
                label = QLabel(str(i + 1) +". " + data[i])
                layout.addWidget(label)
            else: continue
        self.result = _MLPs.MLPclassifier(self.b)
        for i in range(len(self.result)):
            if self.result[i] != 0:
                label = QLabel(str(self.result[i]))
                layout.addWidget(label)
                label = QLabel(result[self.result[i] - 1])
                layout.addWidget(label)
            else: 
                label = QLabel("Không có kỹ năng tư duy")
                layout.addWidget(label)
        self.setLayout(layout)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
