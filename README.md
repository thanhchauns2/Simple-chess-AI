# Bài tập lớn môn Thực tập cơ sở

## Họ và tên: Nguyễn Thanh Châu
## MSV: B19DCCN096
## Đề tài: AI cờ vua, sử dụng Minimax, nhánh cận và hàm Heuristic.

Cách sử dụng:

- Để máy tự học, đặt biến machine_learning = True trong file "main.py"
- Để chơi cờ vua, đặt biến machine_learning = False trong file "main.py"
  + Để chơi với máy, đặt biến play_vs_computer = True trong file "main.py"
  + Để chơi với người, đặt biến play_vs_computer = False trong file "main.py"

Sau đó, chạy file main.py để khởi động chương trình, nếu khởi động trong trạng thái "machine_learning = True", một game mới sẽ bắt đầu ngay sau khi game cũ kết thúc.

Thư viện yêu cầu: pygame, time, sqlite3.

Để thay đổi hình ảnh quân cờ, thay thế các hình ảnh trong file "/images/" theo sở thích cá nhân. Kích cỡ yêu cầu: 60 x 60 pixel.

Để thay đổi hàm heuristic, thay thế các biến trong file "evaluation.py", tuy nhiên không được thay đổi dữ liệu trong hai từ điển "pieces" và "color".

Để thay đổi màu sắc bàn cờ, độ lớn bàn cờ, màu sắc highlight, kích cỡ chữ in ra màn hình, v/v, thay thế các biến trong file "config.py".
