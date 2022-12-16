


def encrypt(self, filename):
    iv = get_random_bytes(16)
    cipher = AES.new(self.K4, AES.MODE_GCM, iv)
    try:
        with open(filename, 'rb') as src:
            with open(filename + ".enc", 'wb') as des:
                des.write(iv)
                for block in iter(lambda: src.read(AES.block_size * 128), b''):
                    if len(block) == AES.block_size * 128:
                        des.write(cipher.encrypt(block))

                    # Padding the last block
                    else:
                        remain = len(block) % 16
                        if remain == 0:
                            remain = 16
                        block += utility.to_bytes((chr(remain) * remain))
                        des.write(cipher.encrypt(block))
    except (IOError, OSError):
        raise IOError("Cannot open the file to encrypt")


        
