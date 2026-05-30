# 🎯 Excel QR Generator - Web App

Ứng dụng web tạo QR Code từ file Excel, được chuyển đổi từ desktop app Python Tkinter sang Flask web app để deploy lên Vercel.

## ✨ Tính năng

- 📊 **Tạo QR từ Excel**: Upload file Excel (.xlsx), tự động tạo QR code từ cột E và chèn vào cột Q
- 🔲 **Tạo QR đơn lẻ**: Tạo QR code từ text, URL, số điện thoại bất kỳ
- 🎨 **Giao diện đẹp**: UI hiện đại với gradient màu tím, responsive trên mọi thiết bị
- ⚡ **Drag & Drop**: Kéo thả file Excel trực tiếp vào trình duyệt
- 💾 **Tải xuống ngay**: File Excel có QR code được tải xuống tự động

## 🚀 Deploy lên Vercel

### Bước 1: Chuẩn bị

1. Tạo tài khoản tại [vercel.com](https://vercel.com)
2. Cài đặt Vercel CLI (tùy chọn):
```bash
npm install -g vercel
```

### Bước 2: Deploy

**Cách 1: Deploy qua Vercel Dashboard (Đơn giản nhất)**

1. Đăng nhập vào [vercel.com](https://vercel.com)
2. Click **"Add New Project"**
3. Import repository GitHub của bạn (hoặc upload folder)
4. Vercel sẽ tự động phát hiện cấu hình Python
5. Click **"Deploy"**
6. Đợi vài phút và app của bạn sẽ online! 🎉

**Cách 2: Deploy qua CLI**

```bash
# Trong thư mục project
vercel

# Hoặc deploy production
vercel --prod
```

### Bước 3: Truy cập

Sau khi deploy thành công, bạn sẽ nhận được URL dạng:
```
https://taoqrcode.vercel.app
```

## 🛠️ Chạy Local (Development)

### Yêu cầu
- Python 3.9+
- pip

### Cài đặt

```bash
# Clone repository
git clone <your-repo-url>
cd taoqrcode

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy app
python run.py
```

Mở trình duyệt tại: `http://localhost:5000`

**Lưu ý:** Nếu gặp lỗi với Pillow trên Windows Python 3.14, bạn có thể:
- Dùng Python 3.11 hoặc 3.12
- Hoặc cài Pillow từ wheel: `pip install --upgrade Pillow`
- App vẫn deploy được bình thường trên Vercel (Vercel dùng Python 3.9-3.12)

## 📁 Cấu trúc Project

```
taoqrcode/
├── api/
│   └── index.py          # Flask backend API
├── templates/
│   └── index.html        # Frontend UI
├── qrgen.py             # Desktop app cũ (Tkinter)
├── requirements.txt     # Python dependencies
├── vercel.json          # Vercel configuration
└── README.md            # Tài liệu này
```

## 📝 Cách sử dụng

### Tab "Excel File"
1. Click hoặc kéo thả file Excel (.xlsx) vào vùng upload
2. Click nút **"Tạo QR Code"**
3. Đợi xử lý (có loading spinner)
4. File Excel có QR code sẽ tự động tải xuống

### Tab "QR Đơn"
1. Nhập text/URL/số điện thoại vào ô input
2. Click **"Tạo QR Code"** hoặc nhấn Enter
3. QR code hiển thị ngay lập tức
4. Click **"Tải xuống"** để lưu ảnh QR

## 🔧 API Endpoints

### `POST /api/generate`
Tạo QR code từ file Excel

**Request:**
- Content-Type: `multipart/form-data`
- Body: `file` (Excel .xlsx file)

**Response:**
- Success: File Excel có QR code (download)
- Error: JSON với message lỗi

### `POST /api/generate-single`
Tạo QR code đơn lẻ

**Request:**
```json
{
  "text": "Nội dung QR code"
}
```

**Response:**
```json
{
  "success": true,
  "image": "data:image/png;base64,..."
}
```

## 🎨 Tùy chỉnh

### Thay đổi màu sắc
Chỉnh sửa gradient trong `templates/index.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Thay đổi cột Excel
Chỉnh sửa trong `api/index.py`:
```python
qr_column = "Q"  # Cột chèn QR
value = ws[f"E{row}"].value  # Cột đọc dữ liệu
```

## ⚠️ Lưu ý

- Vercel có giới hạn:
  - File upload tối đa: 4.5MB
  - Thời gian xử lý: 10 giây (Hobby plan)
  - Nếu file Excel quá lớn, xem xét nâng cấp plan
  
- File Excel phải có định dạng `.xlsx` (không hỗ trợ `.xls`)
- Dữ liệu QR được đọc từ cột E, bắt đầu từ hàng 2

## 🐛 Troubleshooting

**Lỗi: "Module not found"**
```bash
pip install -r requirements.txt
```

**Lỗi: "Template not found"**
- Đảm bảo folder `templates/` nằm cùng cấp với `api/`

**Deploy Vercel thất bại**
- Kiểm tra `vercel.json` đúng format
- Đảm bảo `requirements.txt` có đầy đủ dependencies
- Xem logs tại Vercel Dashboard

## 📦 Dependencies

- **Flask**: Web framework
- **openpyxl**: Xử lý file Excel
- **qrcode**: Tạo QR code
- **Pillow**: Xử lý ảnh

## 📄 License

MIT License - Tự do sử dụng và chỉnh sửa

## 👨‍💻 Tác giả

Chuyển đổi từ desktop app (Tkinter) sang web app (Flask) để deploy lên Vercel

---

**Chúc bạn deploy thành công! 🚀**

Nếu có vấn đề, hãy tạo issue trên GitHub.
