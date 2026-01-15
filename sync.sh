#!/bin/bash

# Script tự động đồng bộ với GitHub

# Pull các thay đổi mới nhất từ GitHub về trước
echo "📥 Đang kiểm tra cập nhật từ GitHub..."
git pull origin main

# Thêm tất cả file đã thay đổi
git add .

# Kiểm tra xem có thay đổi gì không
if git diff-index --quiet HEAD --; then
    echo "✅ Không có thay đổi nào để đẩy lên"
    exit 0
fi

# Lấy timestamp cho commit message
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

# Commit với message tự động
git commit -m "Auto sync: $timestamp"

# Push lên GitHub
git push origin main

echo "✅ Đồng bộ thành công!"
