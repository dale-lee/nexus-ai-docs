<!-- upstream: docs/faq.mdx (end-user items only) @ 91f7edf -->

# Câu hỏi thường gặp

## Sử dụng

### Tìm kiếm khác Hỏi đáp ở điểm nào?

Tìm kiếm là hỏi *một lượt* với chiến lược truy hồi cố định và hiển thị các khối liên quan ngay dưới câu trả lời. Hỏi đáp là trò chuyện *nhiều lượt*, có ngữ cảnh, cho phép tùy chỉnh chiến lược truy hồi và mô hình. Xem [Tìm kiếm](tim-kiem.md).

### Trợ lý có nhớ các câu hỏi trước trong cùng cuộc trò chuyện không?

Có. Khi **Tối ưu hóa đa lượt** được bật (mặc định), câu hỏi hiện tại được làm rõ dựa trên các lượt trước. Mỗi cuộc trò chuyện mới bắt đầu với ngữ cảnh trống.

### Vì sao trợ lý trả lời "không tìm thấy" dù tài liệu có nội dung đó?

Kiểm tra theo thứ tự:

1. Tệp đã **phân tích xong** chưa (cột **Số lượng khối** trên trang **Tệp** của kho tri thức)? Tệp có đang **Bật** không?
2. Chạy [Kiểm tra truy hồi](kho-tri-thuc/kiem-tra-truy-hoi.md) với cùng câu hỏi. Nếu không thấy khối mong muốn, thử giảm **Ngưỡng tương đồng** hoặc điều chỉnh **Trọng số tương đồng từ khóa**.
3. Nếu kiểm tra truy hồi tìm được khối đúng nhưng trợ lý vẫn không trả lời, tăng **Top N** hoặc xem lại prompt **Hệ thống** trong **Cài đặt nâng cao** của trợ lý.

### Vì sao câu trả lời có thông tin không có trong tài liệu?

Nếu **Phản hồi trống** để trống, trợ lý được phép tự ứng biến khi không tìm thấy nội dung phù hợp. Nhập một câu trả lời cố định vào **Phản hồi trống** để giới hạn trợ lý trong phạm vi kho tri thức. Xem [Bắt đầu hỏi đáp](hoi-dap/bat-dau.md).

### Có chia sẻ được cuộc trò chuyện qua đường dẫn không?

Không. Bạn có thể [nhúng trợ lý hoặc Agent vào trang web](agent/nhung-vao-website.md) để đồng nghiệp dùng chung.

## Tài liệu và phân tích

### Vì sao phân tích tài liệu lâu?

Thời gian phụ thuộc kích thước tệp, số trang và loại nội dung. PDF nhiều hình, bảng hoặc bản scan cần nhận dạng ký tự và bố cục nên chậm hơn nhiều so với văn bản thuần. Với PDF chỉ có văn bản, chọn **Naive** trong [Chọn bộ phân tích PDF](kho-tri-thuc/chon-bo-phan-tich-pdf.md). Nếu nhiều người cùng tải tài liệu, tệp của bạn có thể phải xếp hàng chờ.

### Phân tích dừng ở dưới 1% hoặc gần 100% rất lâu

Thường do tệp quá lớn hoặc hệ thống đang bận. Hãy thử lại sau ít phút; nếu vẫn kẹt, xóa tệp và tải lên lại, hoặc chia tệp thành các phần nhỏ hơn. Nếu tình trạng lặp lại, liên hệ quản trị viên kèm tên tệp và thời điểm.

### Tôi có thể đổi mô hình nhúng của kho tri thức không?

Không, khi kho đã có khối. Muốn dùng mô hình nhúng khác, hãy tạo kho tri thức mới hoặc xóa toàn bộ tệp trong kho hiện tại rồi đổi. Xem [Cấu hình kho tri thức](kho-tri-thuc/cau-hinh.md).

### Giới hạn kích thước tệp là bao nhiêu?

Giới hạn do quản trị viên cấu hình. Nếu tải lên bị từ chối vì kích thước, hãy chia nhỏ tệp hoặc liên hệ quản trị viên.

### Xóa kho tri thức có mất tệp gốc không?

Tệp tải *trực tiếp* vào kho sẽ mất. Tệp *liên kết* từ **Quản lý tệp** chỉ mất liên kết, tệp gốc vẫn còn. Xem [Quản lý tệp](tep.md).

## Tài khoản

### Tôi quên mật khẩu

Liên hệ quản trị viên để đặt lại mật khẩu. Sau khi đăng nhập, bạn có thể đổi mật khẩu tại **Cài đặt người dùng**.

### Tôi không thấy kho tri thức mà đồng nghiệp đã chia sẻ

Kiểm tra: (1) bạn đã **Đồng ý** lời mời vào nhóm trong **Cài đặt người dùng** > **Nhóm** chưa; (2) đồng nghiệp đã đổi **Quyền** của kho tri thức thành **Nhóm** chưa. Xem [Tham gia hoặc rời nhóm](nhom/tham-gia.md).
