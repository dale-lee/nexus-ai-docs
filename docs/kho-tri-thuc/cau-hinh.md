<!-- upstream: docs/guides/dataset/configure_knowledge_base.md @ 91f7edf -->

# Cấu hình kho tri thức

Hầu hết trợ lý hỏi đáp và Agent trong Nexus AI đều dựa trên kho tri thức. Mỗi kho tri thức là một nguồn kiến thức: các tệp bạn tải lên (hoặc liên kết từ **Quản lý tệp**) được *phân tích* thành tri thức thực sự cho các cuộc hỏi đáp về sau. Trang này hướng dẫn:

- Tạo kho tri thức
- Cấu hình kho tri thức
- Tìm kho tri thức
- Xóa kho tri thức

## Tạo kho tri thức

Bạn có thể tạo nhiều kho tri thức để phục vụ nhiều mục đích hỏi đáp khác nhau. Để tạo kho tri thức đầu tiên:

1. Nhấn **Kho tri thức** trên thanh điều hướng.
2. Nhấn **Tạo cơ sở kiến thức**, nhập **Tên** rồi nhấn **Lưu**.

## Cấu hình kho tri thức

Trang **Cấu hình** của kho tri thức quyết định chất lượng hỏi đáp về sau. Chọn sai mô hình nhúng hoặc sai phương thức phân khối sẽ làm mất ngữ nghĩa hoặc khiến câu trả lời không khớp. Phần này gồm:

- Chọn phương thức phân khối
- Chọn mô hình nhúng
- Tải tệp lên
- Phân tích tệp
- Can thiệp vào kết quả phân tích
- Kiểm tra truy hồi

### Chọn phương thức phân khối

Nexus AI có sẵn nhiều mẫu phân khối cho các bố cục tài liệu khác nhau, giúp giữ trọn ngữ nghĩa của từng khối. Trong mục **Loại phân tích**, chọn **Tích hợp sẵn** rồi chọn mẫu phù hợp với định dạng tệp của bạn:

| Mẫu | Mô tả | Định dạng tệp |
|-----|-------|---------------|
| General | Chia tệp thành các khối liên tiếp theo số token định trước. Phù hợp cho hầu hết trường hợp. | MD, MDX, DOCX, XLSX, XLS, PPT, PDF, TXT, JPEG, JPG, PNG, TIF, GIF, CSV, JSON, EML, HTML |
| Q&A | Tệp gồm các cặp câu hỏi – câu trả lời. | XLSX, XLS, CSV/TXT |
| Manual | Sổ tay hướng dẫn, tài liệu kỹ thuật có cấu trúc mục. | PDF |
| Table | Bảng dữ liệu; mỗi dòng thành một khối. | XLSX, XLS, CSV/TXT |
| Paper | Bài báo khoa học. | PDF |
| Book | Sách, tài liệu dài nhiều chương. | DOCX, PDF, TXT |
| Laws | Văn bản pháp luật, quy định, hợp đồng. | DOCX, PDF, TXT |
| Presentation | Bài trình chiếu; mỗi trang thành một khối. | PDF, PPTX |
| Picture | Hình ảnh (nhận dạng chữ trong ảnh). | JPEG, JPG, PNG, TIF, GIF |
| One | Mỗi tài liệu là một khối duy nhất. | DOCX, XLSX, XLS, PDF, TXT |
| Tag | Kho tri thức đóng vai trò bộ nhãn cho các kho khác. | XLSX, CSV/TXT |

Bạn cũng có thể đổi phương thức phân khối cho *từng tệp* ngay trên trang **Dữ liệu** của kho tri thức.

??? info "Pipeline nạp dữ liệu tùy chỉnh"
    Ngoài các mẫu tích hợp sẵn, bạn có thể dùng một pipeline nạp dữ liệu do mình tự xây dựng trên trang **Agent** (chọn loại *Ingestion pipeline* khi tạo). Sau khi lưu pipeline, vào trang **Cấu hình** của kho tri thức và chọn pipeline đó trong mục **Pipeline nạp dữ liệu**. Đây là tính năng nâng cao; nếu chưa cần, hãy dùng mẫu tích hợp sẵn.

### Chọn mô hình nhúng

Mô hình nhúng chuyển các khối văn bản thành vector để tìm kiếm theo ngữ nghĩa. **Không thể đổi mô hình nhúng khi kho tri thức đã có khối.** Muốn đổi, bạn phải xóa toàn bộ khối hiện có, vì mọi tệp trong cùng một kho *bắt buộc* phải được nhúng bằng cùng một mô hình.

Thông thường bạn chỉ cần giữ mô hình mặc định mà quản trị viên đã cấu hình.

!!! danger "Quan trọng"
    Một số mô hình nhúng được tối ưu cho ngôn ngữ nhất định. Dùng chúng cho tài liệu ngôn ngữ khác có thể làm giảm chất lượng.

### Tải tệp lên

Có hai cách đưa tệp vào kho tri thức:

- **Liên kết từ Quản lý tệp**: tải tệp lên **Quản lý tệp** trước, rồi liên kết vào một hoặc nhiều kho tri thức. Kho tri thức chỉ giữ *tham chiếu* đến tệp.
- **Tải trực tiếp**: trên trang **Dữ liệu** của kho tri thức, nhấn **Thêm tệp** > **Tệp cục bộ** để tải một tệp hoặc cả thư mục. Kho tri thức giữ *bản sao* của tệp.

Tải trực tiếp có vẻ tiện hơn, nhưng chúng tôi *khuyến nghị* tải lên **Quản lý tệp** rồi liên kết. Như vậy, khi xóa tệp khỏi kho tri thức hoặc xóa cả kho, tệp gốc vẫn còn.

### Phân tích tệp

Phân tích tệp gồm hai việc: chia tệp thành các khối theo bố cục và lập chỉ mục (nhúng vector + chỉ mục từ khóa) cho các khối đó. Sau khi đã chọn phương thức phân khối và mô hình nhúng:

1. Trên trang **Dữ liệu**, tìm tệp vừa tải lên.
2. Nhấn nút **Phân tích cú pháp** (biểu tượng chạy) ở cột **Hành động**.
3. Theo dõi cột **Trạng thái phân tích cú pháp** cho đến khi hoàn tất.

- Bạn có thể chọn phương thức phân khối riêng cho từng tệp, khác với mặc định của kho tri thức.
- Bạn có thể **Bật**/**Tắt** từng tệp để tạm loại tệp đó khỏi hỏi đáp mà không cần xóa.

!!! note "Phân tích mất bao lâu?"
    Tùy kích thước và loại tệp. PDF có nhiều hình, bảng hoặc chữ dạng ảnh mất nhiều thời gian hơn vì phải nhận dạng ký tự và bố cục. Xem thêm [Chọn bộ phân tích PDF](chon-bo-phan-tich-pdf.md).

### Can thiệp vào kết quả phân tích

Nexus AI cho phép xem và chỉnh sửa kết quả phân khối:

1. Nhấn vào tên tệp đã phân tích xong để mở trang **Khối**.
2. Di chuột qua từng khối để xem nhanh nội dung.
3. Nhấn đúp vào một khối để sửa nội dung, thêm từ khóa hoặc câu hỏi.

!!! tip "Mẹo"
    Thêm từ khóa cho một khối sẽ tăng thứ hạng của khối đó với các câu hỏi chứa từ khóa ấy.

4. Sang trang **Kiểm tra truy hồi**, nhập một câu hỏi vào **Văn bản kiểm tra** để xác nhận cấu hình hoạt động đúng.

### Kiểm tra truy hồi

Nexus AI kết hợp tìm kiếm toàn văn (từ khóa) và tìm kiếm vector. Trước khi tạo trợ lý hỏi đáp, hãy cân nhắc điều chỉnh:

- **Ngưỡng tương đồng**: khối có độ tương đồng thấp hơn ngưỡng sẽ bị loại. Mặc định 0.2.
- **Trọng số tương đồng vector**: tỷ lệ đóng góp của độ tương đồng vector vào điểm tổng. Mặc định 0.3.

Xem chi tiết tại [Kiểm tra truy hồi](kiem-tra-truy-hoi.md).

## Tìm kho tri thức

Ô tìm kiếm trên trang **Kho tri thức** hiện chỉ hỗ trợ tìm theo tên.

## Xóa kho tri thức

Di chuột lên thẻ kho tri thức, nhấn biểu tượng ba chấm rồi chọn **Xóa**. Khi xóa kho tri thức:

- Các tệp tải trực tiếp vào kho sẽ bị xóa theo.
- Các tệp *liên kết* từ **Quản lý tệp** chỉ mất liên kết; tệp gốc vẫn còn.
