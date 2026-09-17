<!-- upstream: docs/guides/dataset/select_pdf_parser.md @ 91f7edf -->

# Chọn bộ phân tích PDF

Chọn cách trích xuất nội dung từ tệp PDF để cân bằng giữa tốc độ và độ chính xác.

---

Với tệp PDF, Nexus AI tách riêng bước *trích xuất dữ liệu* khỏi bước *phân khối*. Bạn có thể chọn bộ phân tích thực hiện nhận dạng ký tự (OCR), nhận dạng cấu trúc bảng và nhận dạng bố cục trang. Nếu PDF của bạn chỉ chứa văn bản thuần, chọn **Naive** để bỏ qua các bước này và rút ngắn đáng kể thời gian phân tích.

## Điều kiện

Mục **PDF parser** chỉ xuất hiện khi bạn chọn phương thức phân khối hỗ trợ PDF: **General**, **Manual**, **Paper**, **Book**, **Laws**, **Presentation** hoặc **One**.

## Các bước

1. Trên trang **Cấu hình** của kho tri thức, chọn một phương thức phân khối, ví dụ **General**.

   *Mục **PDF parser** xuất hiện.*

2. Chọn tùy chọn phù hợp:

   - **DeepDoc** (mặc định): mô hình thị giác tích hợp sẵn, nhận dạng ký tự, bảng và bố cục. Chính xác nhưng tốn thời gian.
   - **Naive**: bỏ qua OCR, nhận dạng bảng và bố cục. Chỉ dùng khi *tất cả* PDF là văn bản thuần (có thể bôi đen, sao chép chữ được).
   - Các tùy chọn khác (nếu quản trị viên đã bật): bộ phân tích bên ngoài hoặc mô hình thị giác của nhà cung cấp. Các tùy chọn này được đánh dấu **Experimental**.

3. Nhấn **Lưu**, rồi phân tích lại các tệp PDF nếu cần.

!!! warning "Lưu ý"
    Thay đổi bộ phân tích PDF không tự áp dụng cho tệp đã phân tích. Hãy phân tích lại tệp để dùng cấu hình mới.

## Câu hỏi thường gặp

### Khi nào nên chọn DeepDoc thay vì Naive?

Chọn DeepDoc (hoặc mô hình thị giác) khi PDF chứa bảng, hình, cột phức tạp hoặc chữ dạng ảnh (bản scan). Chọn Naive khi PDF chỉ có văn bản thuần và bạn muốn phân tích nhanh.

### Có chọn được bộ phân tích cho tệp DOCX không?

Không. Mục này chỉ áp dụng cho PDF. Nếu cần, hãy chuyển DOCX sang PDF trước.
