import md5

def create_codes(start, end, length):
  # returns a list of codes on integer range
  # start..end where hash is length characters (hex) long

  raw_codes = range(start, end)

  hashed_codes = []
  for i in raw_codes:
    hashed_codes.append(hashcode(str(i), length))

  return hashed_codes

def hashcode(code, length):
  # forms the code from the codeword and hash
  return code + calchash(code, length)


def calchash(code, length):
  # calculates and returns length character of hash
  md5sum = md5.md5(code)
  return md5sum.hexdigest()[0:length]


def check_code(code, length):
  hash = code[len(code)-length:len(code)]
  raw_code = code[0:len(code)-length]
  
  if calchash(raw_code, length) == hash:
    return True
  else:
    return False