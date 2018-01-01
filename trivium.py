

# Convert strings of hex to strings of bytes and back, little-endian style
_allbytes = dict([("%02X" % i, i) for i in range(256)])

def _hex_to_bytes(s):
    return [_allbytes[s[i:i+2].upper()] for i in range(0, len(s), 2)]


def hex_to_bits(s):
    return [(b >> i) & 1 for b in _hex_to_bytes(s)
            for i in range(8)]


def bits_to_hex(b):
    return "".join(["%02X" % sum([b[i + j] << j for j in range(8)])
                    for i in range(0, len(b), 8)])

def System_init(s1,s2,s3) :
  garb = []
  #key_s = raw_input("input key : ")
  """key_s = "80000000000000000000"
  
  scale = 16 ## equals to hexadecimal

  num_of_bits = 80 #80bits

  key_s = bin(int(key_s, scale))[2:].zfill(num_of_bits)"""
  key_s = hex_to_bits("0F62B5085BAE0154A7FA")
  print "---------------KEY----------------"
  print key_s

  #init_s = raw_input("input init value : ")
  """init_s = "00000000000000000000"

  init_s  = bin(int(init_s, scale))[2:].zfill(num_of_bits)"""
  init_s = hex_to_bits("288FF65DC42B92F960C7")
  print "---------------IV----------------"
  print init_s
  
  for i in range(93):
    if i < 80:
      s1.append(int(key_s[i]))
    else :
      s1.insert(0,0)
  print "---------------state 1----------------"
  print s1

  for i in range(84):
    if i < 80:
      s2.append(int(init_s[i]))
    else :
      s2.insert(0,0)
  print "---------------state 2----------------"
  print s2
  
  for i in range(111):
    if i < 108:
      s3.append(0)
    else :
      s3.insert(0,1)
  print "---------------state 3----------------"  
  print s3
 ##1152
  for i in range(1152) :
    (s1,s2,s3,garb) = Producekey(s1,s2,s3,garb)
	
  return (s1,s2,s3)
  
  
def Producekey(s1,s2,s3,result) : 
  result.append(s1[-66] ^ s1[-93] ^ s2[-69] ^ s2[-84] ^ s3[-111] ^ s3[-66])
  
  t1 = s1[-66] ^ s1[-93] ^ (s1[-91] & s1[-92]) ^ s2[-78]
  #print "t1 = %d" %t1
  t2 = s2[-84] ^ s2[-69] ^ (s2[-82] & s2[-83]) ^ s3[-87]
  t3 = s3[-111] ^ s3[-66] ^ (s3[-109] & s3[-110]) ^ s1[-69]
  
  s1.append(t3)
  s2.append(t1)
  s3.append(t2)
  
  return s1,s2,s3,result

  
s1 = []
s2 = []
s3 = []
result = []

(s1,s2,s3) = System_init(s1,s2,s3)
#print s1
#outkey_s =  raw_input("How much output key? ")
#outkey = int(outkey_s)

for i in range(128):
  (s1,s2,s3,result) = Producekey(s1,s2,s3,result)


#output_key = ''.join(str(e) for e in result)
print "---------------output----------------"  
print bits_to_hex(result)






