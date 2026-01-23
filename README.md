# Hệ thống Thiết kế (Design System)

Hệ thống design token với công cụ chuyển đổi tự động từ CSS variables sang định dạng JSON.

## 📁 Cấu trúc thư mục

- `token.md` - File chứa các biến CSS (design tokens)
- `convert_tokens.py` - Script Python để chuyển đổi tokens sang JSON
- `tokens.json` - File đầu ra chứa tokens ở định dạng JSON
- `components.md` - Tài liệu hướng dẫn cho các components
- `create-filter.md` - Tài liệu hướng dẫn tạo filter

## 🚀 Cách sử dụng

### Chuyển đổi tokens từ CSS sang JSON

```bash
python convert_tokens.py
```

### Đồng bộ với GitHub

#### Cách 1: Sử dụng script tự động
```bash
./sync.sh
```

#### Cách 2: Đồng bộ thủ công
```bash
git add .
git commit -m "Mô tả thay đổi của bạn"
git push origin main
```

## 👥 Hợp tác & Chia sẻ

Dành cho đồng nghiệp muốn sử dụng bộ Design System này:

### 1. Ban đầu (Sao chép dự án)
```bash
git clone https://github.com/hieud4l/design-system.git
cd design-system
```

### 2. Cập nhật bản mới nhất

#### Cách 1: Sử dụng sync script (nếu có quyền push)
Trước khi bắt đầu làm việc hoặc định kỳ, hãy chạy lệnh sau để nhận các thay đổi mới nhất từ mọi người:
```bash
./sync.sh
```
*(Script này sẽ tự động chạy `git pull` để lấy bản mới nhất về)*

#### Cách 2: Chỉ cập nhật (read-only)
Nếu bạn chỉ muốn xem và sử dụng mà không cần đẩy thay đổi lên:
```bash
git pull origin main
```

## 📝 Quy trình làm việc

1. Luôn chạy `./sync.sh` trước khi bắt đầu để cập nhật bản mới nhất.
2. Chỉnh sửa file trong project.
3. Chạy `./sync.sh` lần nữa để đẩy các thay đổi của bạn lên GitHub.

## 🔗 Kho mã nguồn

[https://github.com/hieud4l/design-system](https://github.com/hieud4l/design-system)
