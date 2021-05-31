import os

def process_file(my_f):
    with open(my_f, "rb") as data:
        chunks = data.read().split(b"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for chunk in chunks[:-1]:
        meta, payload = chunk.split(b"data\x00\x00\x00\x00")
        __, url = meta.split(b"url", 1)
        try:
            url, __ = url.split(b"srl", 1)
            url = url.replace(b"\x00", b"").replace(b"\n", b"").replace(b" ", b"")[1:-1]
        except ValueError:
            url, __ = url.split(b"mime", 1)
            url = url.replace(b"\x00", b"").replace(b"\n", b"").replace(b" ", b"")[1:]
        root  = b"http://www.humanities-2010.sshrc.ca"
        folder = url.replace(root, b"")[1:]
        folder, fname = folder.rsplit(b"/", 1)
        try:
            __, srl = meta.split(b"srl", 1)
            srl, __ = srl.split(b"mime", 1)
        except ValueError:
            srl = b" None"
        srl = srl.replace(b"\x00", b"").replace(b"\n", b"").replace(b" ", b"")[1:]
        __, mime = meta.split(b"mime", 1)
        mime, __ = mime.split(b"hntt", 1)
        mime = mime.replace(b"\x00", b"").replace(b"\n", b"").replace(b" ", b"").replace(b"\x0b", b"")
        
        payload, footer = payload.rsplit(b"post", 1)
        folder = os.path.join(file_root, folder)
        if not os.path.exists(folder):
            os.makedirs(folder)

        f_path = os.path.join(folder, fname)
        with open(f_path, "wb") as outfile:
            outfile.write(payload)

files = [
    b"V1-FL15145678.waf",    
    b"FL15145681.waf",
    b"FL15145684.waf",
    b"FL15145690.waf",
    b"FL15145687.waf"]

for f in files:
    file_root = f.replace(b".waf", b"")
    if not os.path.exists(file_root):
        os.makedirs(file_root)
    process_file(f)
