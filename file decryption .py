

def decrypt(self, ciphertext):
        try:
            with open(ciphertext, 'rb') as src:
                with open(ciphertext.strip(".enc") + ".dec", 'wb+') as des:
                    iv = src.read(16)
                    cipher = AES.new(self.K4, AES.MODE_GCM, iv)
                    for block in iter(lambda: src.read(AES.block_size * 128), b''):
                        des.write(cipher.decrypt(block))

                    # Remove padding
                    # Set the pos to the beginning of the last byte
                    des.seek(-1, os.SEEK_END)
                    # Read the last byte
                    last = des.read(1)
                    des.seek(-int.from_bytes(last, byteorder='big'), os.SEEK_END)
                    des.truncate()
        except (IOError, OSError):
            raise IOError("Cannot open the file to decrypt")

