import zstandard as zstd
import os

decompressdir="_nabe_"

with open('zdict', 'rb') as fo:
	dictionary=fo.read()

d=zstd.ZstdCompressionDict(dictionary)
dctx = zstd.ZstdDecompressor(d)

def decompress(file_name, dict, extension):
    with open(file_name, 'rb') as fo:
        file_data = fo.read()
    decompressed = dctx.decompress(file_data)
    with open(file_name + extension, 'wb') as fo:
        fo.write(decompressed)

for subdir, dirs, files in os.walk(decompressdir):
    for file in files:
        ext = os.path.splitext(file)[-1].lower()
        if os.path.getsize(os.path.join(subdir,file)) < 32: #avoid file that are 32 bytes in size
    				continue
        if ext == '.zst':
        		decompress(os.path.abspath(os.path.join(subdir,file)), dictionary, '.decrypted')
