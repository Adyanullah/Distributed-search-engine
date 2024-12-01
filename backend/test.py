import json

# Periksa apakah file JSON ada dan tidak kosong
file_path = 'data/articles.json'
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read().strip()
        if not file_content:
            raise ValueError("File JSON kosong.")
        articles = json.loads(file_content)
except FileNotFoundError:
    print(f"File {file_path} tidak ditemukan.")
except ValueError as e:
    print(f"Error: {e}")
except json.JSONDecodeError as e:
    print(f"Error dalam format JSON: {e}")
