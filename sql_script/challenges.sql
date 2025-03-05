
-- Chèn dữ liệu mặc định nếu chưa có
INSERT INTO user (username, password)
VALUES 
    ('admin', '123123')

INSERT INTO challenge (name, description, difficulty, answer, solved, category) 
VALUES 
    ('Challenge 1: Basic Caesar Cipher', 'Giải mã một chuỗi mã hóa sử dụng Caesar Cipher với shift = 3.', 'Easy', 'helloworld', FALSE, 'Cryptography'),
    ('Challenge 2: SHA-256 Cracking', 'Phá vỡ một hash SHA-256 với từ điển 100 từ cho trước.', 'Medium', 'secret123', FALSE, 'Hashing'),
    ('Challenge 3: RSA Small Key', 'Phá mã RSA với khóa 1024-bit bằng cách phân tích số nguyên tố.', 'Hard', 'flag{rsa_cracked}', FALSE, 'Cryptography');

