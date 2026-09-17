# Giới thiệu

Nexus AI là nền tảng hỏi đáp và trợ lý AI dựa trên tài liệu nội bộ của doanh nghiệp. Bạn tải tài liệu lên, hệ thống phân tích và lập chỉ mục, sau đó bạn có thể hỏi đáp, tìm kiếm hoặc xây dựng Agent trả lời dựa trên đúng nội dung đó — kèm trích dẫn nguồn.

Tài liệu này hướng dẫn các thao tác hằng ngày của người dùng. Việc cài đặt hệ thống, cấu hình mô hình và quản trị người dùng do quản trị viên phụ trách và không nằm trong phạm vi tài liệu này.

## Các khái niệm chính

| Khái niệm | Ý nghĩa |
|-----------|---------|
| **Kho tri thức** | Nơi chứa tài liệu đã được phân tích thành các *khối* (chunk) và lập chỉ mục. Mọi câu trả lời của hệ thống đều dựa trên kho tri thức. |
| **Hỏi đáp** | Trò chuyện nhiều lượt với một *trợ lý* gắn với một hoặc nhiều kho tri thức. |
| **Tìm kiếm** | Hỏi một lượt, nhận câu trả lời tóm tắt kèm danh sách các khối liên quan. |
| **Agent** | Luồng xử lý tự động (workflow) gồm nhiều bước, dùng cho các kịch bản phức tạp hơn hỏi đáp thông thường. |
| **Quản lý tệp** | Kho tệp trung tâm; một tệp có thể được liên kết vào nhiều kho tri thức. |
| **Nhóm** | Chia sẻ kho tri thức và Agent với đồng nghiệp. |

## Đăng nhập

1. Mở địa chỉ Nexus AI do quản trị viên cung cấp.
2. Nhập **email** và **mật khẩu** của tài khoản đã được cấp, rồi nhấn **Đăng nhập**.
3. Sau khi đăng nhập, thanh điều hướng phía trên gồm: **Kho tri thức**, **Hỏi đáp**, **Tìm kiếm**, **Agent**, **Quản lý tệp**. Ảnh đại diện ở góc phải mở trang **Cài đặt người dùng** (đổi mật khẩu, nhóm, đăng xuất).

!!! note "Chưa có tài khoản?"
    Liên hệ quản trị viên hệ thống để được cấp tài khoản hoặc mời vào nhóm.

## Quy trình làm việc điển hình

1. [Tạo kho tri thức và tải tài liệu lên](kho-tri-thuc/cau-hinh.md).
2. Đợi tài liệu phân tích xong, rồi [kiểm tra truy hồi](kho-tri-thuc/kiem-tra-truy-hoi.md) để chắc chắn hệ thống tìm được đúng nội dung.
3. [Tạo trợ lý hỏi đáp](hoi-dap/bat-dau.md) gắn với kho tri thức và bắt đầu trò chuyện.
4. Khi cần, [chia sẻ kho tri thức với nhóm](nhom/chia-se.md).
