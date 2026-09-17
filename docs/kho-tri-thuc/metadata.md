<!-- upstream: docs/guides/dataset/set_metadata.md, docs/guides/dataset/manage_metadata.md @ 91f7edf -->

# Metadata

Gắn thông tin bổ sung (metadata) cho tài liệu và dùng nó để lọc khi hỏi đáp.

---

Metadata là các cặp *trường – giá trị* gắn với từng tệp, ví dụ `tác giả`, `phòng ban`, `năm`, `url`. Khi hỏi đáp, metadata của các khối được truy hồi sẽ được gửi kèm cho mô hình ngôn ngữ, và bạn có thể dùng metadata để lọc tài liệu trước khi tìm.

Ví dụ: với kho tri thức gồm nhiều trang web, thêm trường `url` cho từng tệp để mô hình dẫn nguồn đúng địa chỉ.

## Đặt metadata cho một tệp

1. Trên trang **Dữ liệu** của kho tri thức, mở tệp cần gắn metadata.
2. Nhấn vào phương thức phân khối của tệp (ví dụ **General**) rồi chọn **Đặt dữ liệu Meta**.
3. Thêm, sửa hoặc xóa các trường, rồi lưu.

!!! tip "Mẹo"
    Metadata phải ở định dạng JSON hợp lệ, ví dụ `{"phong_ban": "Kế toán", "nam": 2025}`. Nếu sai định dạng, thay đổi sẽ không được áp dụng.

## Quản lý metadata toàn kho tri thức

1. Trong kho tri thức, nhấn **Dữ liệu Meta** để mở trang quản lý.
2. Tại đây bạn có thể:
   - **Sửa giá trị**: đổi tên một giá trị. Nếu đổi hai giá trị thành trùng nhau, chúng được gộp tự động.
   - **Xóa**: xóa một giá trị hoặc cả trường. Thay đổi áp dụng cho mọi tệp liên quan.

Mọi chỉnh sửa ở cấp tệp đều được phản ánh trong thống kê ở trang này.

## Lọc theo metadata

Lọc hoạt động ở hai nơi:

- **Trong kho tri thức**: nhấn nút **Bộ lọc** trên trang **Dữ liệu** để xem số tệp theo từng giá trị metadata và hiển thị các tệp tương ứng.
- **Khi hỏi đáp**: trong cài đặt trợ lý, sau khi chọn kho tri thức, bạn có thể đặt quy tắc lọc metadata:
    - **Tự động**: hệ thống tự lọc dựa trên câu hỏi của người dùng và metadata hiện có.
    - **Bán tự động**: bạn chọn trước các trường được phép lọc (ví dụ `phong_ban`), hệ thống tự chọn giá trị trong phạm vi đó.
    - **Thủ công**: bạn đặt điều kiện cụ thể với các toán tử **Bằng**, **Khác**, **Thuộc**, **Không thuộc**, …

## Câu hỏi thường gặp

### Có đặt metadata cho nhiều tệp cùng lúc không?

Có. Ngoài cách đặt thủ công cho từng tệp, bạn có thể để mô hình ngôn ngữ tự sinh metadata cho nhiều tệp theo quy tắc đã cấu hình (mục **Tạo sinh** trên trang quản lý metadata). Đây là tính năng nâng cao; hãy kiểm tra kết quả sinh trước khi dùng cho hỏi đáp.
