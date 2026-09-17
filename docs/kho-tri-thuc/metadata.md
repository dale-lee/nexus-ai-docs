<!-- upstream: docs/guides/dataset/set_metadata.md, docs/guides/dataset/manage_metadata.md @ 91f7edf -->

# Metadata

Gắn thông tin bổ sung (metadata) cho tài liệu và dùng nó để lọc khi hỏi đáp.

---

Metadata là các cặp *trường – giá trị* gắn với từng tệp, ví dụ `tac_gia`, `phong_ban`, `nam`, `url`. Khi hỏi đáp, metadata của các khối được truy hồi sẽ được gửi kèm cho mô hình ngôn ngữ, và bạn có thể dùng metadata để lọc tài liệu trước khi tìm.

Ví dụ: với kho tri thức gồm nhiều trang web, thêm trường `url` cho từng tệp để mô hình dẫn nguồn đúng địa chỉ.

## Đặt metadata cho một tệp

1. Trên trang **Tệp** của kho tri thức, cột **Metadata** cho biết số trường hiện có của từng tệp (ví dụ *0 fields*).
2. Nhấn vào cột đó (hoặc mở menu thao tác của tệp và chọn **Đặt dữ liệu Meta**).
3. Thêm, sửa hoặc xóa các trường, rồi lưu.

!!! tip "Mẹo"
    Metadata phải ở định dạng JSON hợp lệ, ví dụ `{"phong_ban": "Kế toán", "nam": 2025}`. Nếu sai định dạng, thay đổi sẽ không được áp dụng.

## Sinh metadata tự động

Trên trang **Cấu hình** của kho tri thức, bật **Metadata tự động** và nhấn **Cài đặt** để định nghĩa các trường cần trích xuất. Khi phân tích tệp, mô hình ngôn ngữ sẽ tự điền giá trị cho các trường này. Hãy kiểm tra kết quả sinh trước khi dùng cho hỏi đáp.

## Lọc theo metadata

Lọc hoạt động ở hai nơi:

- **Trong kho tri thức**: nhấn biểu tượng bộ lọc trên trang **Tệp** để xem số tệp theo từng giá trị metadata và hiển thị các tệp tương ứng.
- **Khi hỏi đáp hoặc tìm kiếm**: trong **Cài đặt nâng cao** của trợ lý (hoặc **Cài đặt tìm kiếm**), mục **Siêu dữ liệu** có các chế độ:
    - **Tự động**: hệ thống tự lọc dựa trên câu hỏi của người dùng và metadata hiện có.
    - **Bán tự động**: bạn chọn trước các trường được phép lọc (ví dụ `phong_ban`), hệ thống tự chọn giá trị trong phạm vi đó.
    - **Thủ công**: bạn đặt điều kiện cụ thể với các toán tử **Bằng**, **Khác**, **Thuộc**, **Không thuộc**, …
    - **Tắt**: không lọc.

Bật **Hiển thị siêu dữ liệu đoạn** để metadata xuất hiện cùng trích dẫn trong câu trả lời.
