<!-- upstream: docs/guides/ai_search.md @ 91f7edf -->

# Tìm kiếm

Hỏi một lượt và nhận câu trả lời tóm tắt kèm danh sách nội dung liên quan.

---

Tìm kiếm là cuộc hỏi đáp *một lượt* dùng chiến lược truy hồi cố định (tìm kiếm lai giữa từ khóa và vector) và mô hình ngôn ngữ mặc định của hệ thống. Nó không dùng các kỹ thuật nâng cao như đồ thị tri thức. Các khối liên quan được liệt kê ngay dưới câu trả lời, xếp theo điểm tương đồng giảm dần — vì vậy tìm kiếm rất tiện để *tra cứu nhanh* và để *kiểm tra* xem kho tri thức có chứa nội dung bạn cần không.

## Tạo ứng dụng tìm kiếm

1. Nhấn **Tìm kiếm** trên thanh điều hướng, rồi nhấn **Tạo tìm kiếm**.
2. Đặt **Tên** và chọn **Bộ dữ liệu** (kho tri thức) muốn tìm trong đó.
3. Tùy chọn trong **Cài đặt tìm kiếm**:
    - **Tóm tắt AI**: hiển thị câu trả lời tóm tắt phía trên danh sách kết quả.
    - **Bật tìm kiếm liên quan**: gợi ý các câu hỏi liên quan.
    - **Hiển thị sơ đồ tư duy truy vấn**: vẽ sơ đồ các ý chính của kết quả.
    - **Mô hình rerank**: xếp hạng lại kết quả; chính xác hơn nhưng chậm hơn.
4. Nhấn **Lưu**.

## Tìm kiếm

Mở ứng dụng tìm kiếm vừa tạo, nhập câu hỏi và nhấn Enter. Kết quả gồm phần tóm tắt (nếu bật) và danh sách các khối tài liệu liên quan; nhấn vào từng khối để xem tài liệu gốc.

!!! tip "Mẹo"
    Khi trợ lý hỏi đáp trả lời chưa đúng, hãy thử cùng câu hỏi trong Tìm kiếm. Nếu Tìm kiếm liệt kê đúng khối cần thiết, vấn đề nằm ở cài đặt trợ lý (prompt, ngưỡng, Top N) chứ không phải ở dữ liệu.

## Điều kiện

- Quản trị viên đã cấu hình mô hình mặc định của hệ thống.
- Kho tri thức đã được cấu hình và các tài liệu đã phân tích xong.

## Câu hỏi thường gặp

### Tìm kiếm khác Hỏi đáp ở điểm nào?

| | Tìm kiếm | Hỏi đáp |
|--|----------|---------|
| Số lượt | Một lượt | Nhiều lượt, có ngữ cảnh |
| Chiến lược truy hồi | Cố định | Tùy chỉnh (ngưỡng, trọng số, rerank, đồ thị tri thức, …) |
| Mô hình | Mặc định của hệ thống | Chọn được cho từng trợ lý |
| Hiển thị khối liên quan | Có, ngay dưới câu trả lời | Chỉ qua trích dẫn |
