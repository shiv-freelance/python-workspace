
# binary files as similar as reading text files.

# rb
# wb

# img\image.jpg
# E:\coding_sessions\file_handling\img\image.jpg

with open('img/image.jpg', mode='rb') as rfile:
    print(rfile.readable())
    print(rfile.writable())

    with open('img/image_copy.png', mode='wb') as wfile:
        wfile.write(rfile.read())