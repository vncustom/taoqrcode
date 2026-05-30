"""
Script để chạy Flask app local
"""
import sys
import os

# Thêm thư mục hiện tại vào Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api.index import app

if __name__ == '__main__':
    print("=" * 60)
    print("🎯 Excel QR Generator - Web App")
    print("=" * 60)
    print("Server đang chạy tại: http://localhost:5000")
    print("Nhấn Ctrl+C để dừng server")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
