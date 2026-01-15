# Design System

Design token system với converter tự động từ CSS variables sang JSON format.

## 📁 Cấu trúc thư mục

- `token.md` - File chứa các CSS variables (design tokens)
- `convert_tokens.py` - Script Python để convert tokens sang JSON
- `tokens.json` - Output file chứa tokens ở format JSON
- `components.md` - Documentation cho components
- `create-filter.md` - Documentation cho filter creation

## 🚀 Cách sử dụng

### Convert tokens từ CSS sang JSON

```bash
python convert_tokens.py
```

### Đồng bộ với GitHub

#### Cách 1: Sử dụng script tự động
```bash
./sync.sh
```

#### Cách 2: Manual sync
```bash
git add .
git commit -m "Mô tả thay đổi của bạn"
git push origin main
```

## 👥 Hợp tác & Chia sẻ

Dành cho đồng nghiệp muốn sử dụng bộ Design System này:

### 1. Ban đầu (Clone project)
```bash
git clone https://github.com/hieud4l/design-system.git
cd design-system
```

### 2. Cập nhật bản mới nhất
Trước khi bắt đầu làm việc hoặc định kỳ, hãy chạy lệnh sau để nhận các thay đổi mới nhất từ mọi người:
```bash
./sync.sh
```
*(Script này sẽ tự động chạy `git pull` để lấy bản mới nhất về)*

## 📝 Workflow

1. Luôn chạy `./sync.sh` trước khi bắt đầu để cập nhật bản mới nhất.
2. Chỉnh sửa file trong project.
3. Chạy `./sync.sh` lần nữa để đẩy các thay đổi của bạn lên GitHub.

## 🔗 Repository

[https://github.com/hieud4l/design-system](https://github.com/hieud4l/design-system)
