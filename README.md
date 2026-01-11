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

## 📝 Workflow

1. Chỉnh sửa file trong project
2. Chạy `./sync.sh` để tự động đồng bộ lên GitHub
3. Hoặc sử dụng các lệnh git thông thường

## 🔗 Repository

[https://github.com/hieud4l/design-system](https://github.com/hieud4l/design-system)
