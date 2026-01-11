#!/bin/bash

# Script tự động đồng bộ với GitHub

echo "🔄 Bắt đầu đồng bộ với GitHub..."

# Thêm tất cả file đã thay đổi
git add .

# Kiểm tra xem có thay đổi gì không
if git diff-index --quiet HEAD --; then
    echo "✅ Không có thay đổi nào để đồng bộ"
    exit 0
fi

# Lấy timestamp cho commit message
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

# Commit với message tự động
git commit -m "Auto sync: $timestamp"

# Push lên GitHub
git push origin main

echo "✅ Đồng bộ thành công!"
