<!-- upstream: docs/guides/chat/start_chat.md @ 91f7edf -->

# Bắt đầu hỏi đáp

Tạo một trợ lý hỏi đáp gắn với kho tri thức và bắt đầu trò chuyện.

---

Hỏi đáp trong Nexus AI luôn dựa trên một hoặc nhiều kho tri thức. Sau khi đã tạo kho tri thức, phân tích tệp xong và [kiểm tra truy hồi](../kho-tri-thuc/kiem-tra-truy-hoi.md), bạn có thể bắt đầu hỏi đáp.

## Tạo trợ lý hỏi đáp

Mỗi *trợ lý* là một tổ hợp riêng gồm kho tri thức, prompt, cấu hình tìm kiếm và mô hình ngôn ngữ. Bạn có thể tạo nhiều trợ lý cho nhiều mục đích.

1. Nhấn **Hỏi đáp** trên thanh điều hướng, rồi nhấn **Tạo cuộc trò chuyện**.
2. Đặt tên trợ lý và mở bảng cài đặt. Cập nhật các mục sau:

### Cài đặt trợ lý

- **Tên trợ lý**, **Avatar trợ lý**, **Mô tả về trợ lý**: thông tin hiển thị của trợ lý.
- **Đặt lời mở đầu**: câu chào hiện ra khi bắt đầu cuộc trò chuyện mới.
- **Cơ sở kiến thức**: chọn một hoặc nhiều kho tri thức. Các kho được chọn *phải dùng cùng một mô hình nhúng*, nếu không sẽ báo lỗi.
- **Phản hồi trống**:
    - Muốn trợ lý *chỉ* trả lời dựa trên kho tri thức: nhập một câu trả lời cố định ở đây. Khi không tìm thấy nội dung phù hợp, trợ lý sẽ trả lời đúng câu này.
    - Muốn trợ lý *tự ứng biến* khi không tìm thấy: để trống. Lưu ý cách này có thể sinh ra thông tin không có trong tài liệu.
- **Hiển thị Trích dẫn**: bật mặc định. Trợ lý sẽ chỉ rõ đoạn tài liệu mà câu trả lời dựa vào — đây là điểm mạnh chính của hệ thống, nên giữ bật.

### Công cụ nhắc nhở (prompt)

- **Hệ thống**: prompt hệ thống gửi cho mô hình ngôn ngữ. Lúc đầu có thể giữ nguyên mặc định.
- **Ngưỡng tương đồng**: khối có độ tương đồng thấp hơn ngưỡng bị loại. Mặc định 0.2.
- **Trọng số tương đồng vector**: tỷ lệ đóng góp của độ tương đồng vector vào điểm tổng; phần còn lại là trọng số từ khóa (hoặc điểm rerank nếu chọn mô hình xếp hạng lại).
- **Top N**: số khối *tối đa* gửi cho mô hình ngôn ngữ. Dù truy hồi được nhiều hơn, chỉ N khối tốt nhất được dùng.
- **Tối ưu hóa đa lượt**: dùng ngữ cảnh các lượt trước để làm rõ câu hỏi hiện tại. Bật mặc định; tốn thêm token và thời gian.
- **Sử dụng đồ thị tri thức**: chỉ bật khi kho tri thức đã xây dựng đồ thị tri thức. Làm tăng đáng kể thời gian trả lời.
- **Suy luận**: cho phép mô hình suy luận từng bước và tự tìm thêm thông tin khi gặp chủ đề chưa biết. Chậm hơn đáng kể.
- **Mô hình xếp hạng lại**: để trống theo mặc định. Chọn mô hình sẽ chính xác hơn nhưng chậm hơn.
- **Tìm kiếm đa ngôn ngữ**: chọn ngôn ngữ đích nếu tài liệu có nhiều ngôn ngữ. Chỉ chọn ngôn ngữ thực sự có trong kho tri thức.
- **Biến**: các biến dùng trong prompt hệ thống. `{knowledge}` là biến dành riêng cho nội dung truy hồi được — *giữ nguyên* nếu bạn không rõ về mục này.

### Cài đặt mô hình

- **Mô hình**: mô hình ngôn ngữ dùng để trả lời. Mặc định là mô hình quản trị viên đã cấu hình; bạn có thể chọn mô hình khác cho từng trợ lý.
- **Tự do** (mức sáng tạo): chọn nhanh giữa **Ứng biến**, **Chính xác** (mặc định) và **Cân bằng**. Mỗi mức tương ứng một bộ giá trị **Nhiệt độ**, **Top P**, **Phạt hiện diện**, **Phạt tần suất**:
    - **Nhiệt độ**: độ ngẫu nhiên của câu trả lời. Thấp → ổn định, dễ đoán; cao → sáng tạo, đa dạng. Mặc định 0.1.
    - **Top P**: giới hạn tập từ được chọn theo xác suất tích lũy. Mặc định 0.3.
    - **Phạt hiện diện**: khuyến khích dùng từ mới chưa xuất hiện. Mặc định 0.4.
    - **Phạt tần suất**: hạn chế lặp lại cùng một từ/cụm từ. Mặc định 0.7.

3. Nhấn **Lưu**.

## Trò chuyện

1. Nhấn **Cuộc trò chuyện mới** trong cột **Phiên** bên trái, nhập câu hỏi và nhấn **Gửi**.
2. Câu trả lời hiện kèm các trích dẫn; nhấn vào số trích dẫn để xem đoạn tài liệu gốc.
3. Các cuộc trò chuyện được lưu trong cột bên trái; bạn có thể đổi tên hoặc xóa từng cuộc.

!!! tip "Mẹo"
    - Nhấn biểu tượng bóng đèn phía trên câu trả lời để xem prompt hệ thống đầy đủ đã gửi cho mô hình, kéo xuống để xem thời gian từng bước.
    - Nhấn **Nhiều mô hình** để hỏi cùng một câu với tối đa 3 mô hình khác nhau và so sánh câu trả lời.

## Cập nhật trợ lý đã tạo

Trên trang **Hỏi đáp**, di chuột lên thẻ trợ lý và chọn **Chỉnh sửa** (hoặc mở trợ lý rồi mở bảng cài đặt). Thay đổi cài đặt có hiệu lực với các câu hỏi tiếp theo.

## Nhúng trợ lý vào trang web

Bạn có thể nhúng một trợ lý vào trang web nội bộ bằng iframe:

1. Trên trang **Hỏi đáp**, di chuột lên trợ lý và chọn **Nhúng vào trang web**.
2. Sao chép mã iframe được sinh ra và dán vào trang web của bạn.

!!! note
    Thao tác này cần một khóa API. Nếu hộp thoại báo thiếu khóa API, hãy tạo khóa tại **Cài đặt người dùng** > **API** hoặc liên hệ quản trị viên.
