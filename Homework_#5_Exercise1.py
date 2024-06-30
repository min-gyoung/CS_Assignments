import copy
 
# AES-128 Python
 
    # SubBytes 용 치환 sbox
    # 예: 16진수 19 -> x:1, y:9 -> d4
    #
    #  y   0     1     2     3     4     5     6     7     8     9     a     b     c     d     e     f 
 
Sbox =  [ 0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76, 
          0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 
          0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15, 
          0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 
          0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84, 
          0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 
          0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8, 
          0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 
          0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73, 
          0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 
          0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79, 
          0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08, 
          0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 
          0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e, 
          0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 
          0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16 ]
 
 
 
RC = [ 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
 
key = [ 0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c ]
 
block = [ 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 
          0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F,]
 
 
# block 을 state로 변환
 
def block2state(block):
    state = []
    for row in range(4):
        intm_list = []
        for col in range(4):
            new_col = block[row*4+col]
            intm_list.append(new_col)
        state.append(intm_list)
    return state
 
# SubBytes (Sbox에 맞춰 치환)
 
def SubBytes(input_state):
    state = []
    for row in range(4):
        intm_list = []
        for segment in range(4):
            intm_list.append(Sbox[input_state[row][segment]])
        state.append(intm_list)
    return state
 
# ShiftRows 
 
# (row_1 -> 0, row_2 -> 1, row_3 -> 3, row_4 -> 4 만큼 행 내에서 이동)
 
def ShiftRows(input_state):
    state = []
    for row in range(4):
        intm_list = []
        for segment in range(4):
            intm_list.append(input_state[(row+segment)%4][segment])
        state.append(intm_list)
    return state
 
def SubByte_Col(col):
    new_col = [Sbox[col[cnt_i]] for cnt_i in range(4)]
    return new_col
 
def Xor_Col(c1, c2):
    new_col = [c1[cnt_i] ^ c2[cnt_i] for cnt_i in range(4)]
    return new_col
 
def Rotl(col):
    new_col = [col[1], col[2], col[3], col[0]]
    return new_col
 
def KeySR(col, round):
    new_col = Rotl(col)
    round_constant = [ RC[round-1], 0, 0, 0]
    new_col2 = SubByte_Col(new_col)
    new_col3 = Xor_Col(new_col2, round_constant)
    return new_col3
 
# AES Encrytion용 key schedule
# 입력 : 암호키 (4x4 state)
# 출력 : 11개의 라운드키(4x4 state)
# 출력 rkey : [ rkey[0], rkey[1], ... , rkey[10] ]
# rkey[r] = [ [rk00, rk10, rk20, rk 30], ... , [rk03, rk13, rk23, rk33] ]
 
def key_schedule_Enc(key_state):
    rkey = [ copy.deepcopy(key_state) ]
    for round in range(1,11):
        new_state = []
        new_w0 = Xor_Col(rkey[round-1][0], KeySR(rkey[round-1][3], round))
        new_state.append(new_w0)
        new_w1 = Xor_Col(rkey[round-1][1], new_w0)
        new_state.append(new_w1)
        new_w2 = Xor_Col(rkey[round-1][2], new_w1)
        new_state.append(new_w2)
        new_w3 = Xor_Col(rkey[round-1][3], new_w2)
        new_state.append(new_w3)
        rkey.append(new_state)
    return rkey
 
#rkey = key_schedule_Enc(new_key)
 
 
def AddRoundKey(state , rkey):
    new_state = []
    for col in range(4):
        new_col = [Sbox[state[col][cnt_i]] for cnt_i in range (4)]
        new_state.append(new_col)
    return new_state
 
#output_state = AddRoundKey(new_state , rkey[0])
 
# =========================================================
 
# mixcolumns 시작 부분
 
def x_time(xnum):
    y = (xnum << 1) & (0xff)
    if (xnum >= 128):
        y ^= 0x1b
    return y
 
# 0x02 곱하기
def multi_02(xnum):
    return x_time(xnum)
 
# 0x03 곱하기
def multi_03(xnum):
    return multi_02(xnum)^xnum
 
'''
          Test        Col            state
 
|y1| ( 02 03 01 01 ) |x0|       | 00 01 02 03 |
|y1| ( 01 02 03 01 ) |x1|       | 04 05 06 07 |
|y2| ( 01 01 02 03 ) |x2|       | 08 09 0A 0B |
|y3| ( 03 01 01 02 ) |x3|       | 0C 0D 0E 0F |
 
 
02 |x0| ( m02 * col[0])
03 |x1| ( m03 * col[1])
01 |x2| ( col[2])
01 |x3| ( col[3])
 
'''
 
# 계산시 한 개의 컬럼 생성 / 02x0 + 03x1 + x2 + x3
 
# 한 column에 대한 mixcolumn 연산
 
def MixColumns_one_Col(col):
    out_col = [0]*4
    out_col[0] = multi_02(col[0]) ^ multi_03(col[1]) ^ col[2] ^ col[3]  # 한 A 행 ^ 한 컬럼
    out_col[1] = col[0] ^ multi_02(col[1]) ^ multi_03(col[2]) ^ col[3]  # 한 B 행 ^ 한 컬럼
    out_col[2] = col[0] ^ col[1] ^ multi_02(col[2]) ^ multi_03(col[3])  # 한 C 행 ^ 한 컬럼
    out_col[3] = multi_03(col[0]) ^ col[1] ^ col[2] ^ multi_02(col[3])  # 한 D 행 ^ 한 컬럼
    return out_col
 
 
# MixColumns_one_Col을 이용해 전체 행렬 mixcolumn 연산
def MixColumns(state):
 
    out_state = []                    # 반환 state
    for num in range(4):                            # MixColumns_one_col 4번 사용
        out_col = MixColumns_one_Col(state[num])      # ㄴ input의 state를 사용
        out_state.append(out_col)                   # ㄴ output에 저장
    return out_state                # 완성된 state 반환
 
 
# 10진수 -> 16진수로 변환 함수
def dec2hex(state):
    print('[', end='')
    for cnt_i in range(4):
        print('[%02x, %02x, %02x, %02x]' # [a a a a] 형식으로 표현
        %(state[cnt_i][0], state[cnt_i][1], state[cnt_i][2], state[cnt_i][3]), end='')
        if (cnt_i < 3):
            print(', ', end='')
    print(']')
 
 
# AES 라운드 1개 함수
def AES_One_Round(state, rkey): # AES의 한 라운드 연산을 하는 함수
    # SubBytes -> ShiftRows -> MiColumns -> AddRoundKey 
 
    new_state = copy.deepcopy(state)
    output_state_1 = SubBytes(new_state)
    output_state_2 = ShiftRows(output_state_1)
    output_state_3 = MixColumns(output_state_2)
    output_state_4 = AddRoundKey(output_state_3, rkey)
 
    return output_state_4
 w
# AES 10 라운드 암호화 함수
def AES_128_Encryption(plaintext, key):
    round_key = key_schedule_Enc(key)
    state = copy.deepcopy(plaintext) 
    new_state = AddRoundKey(state, round_key[0])
 
    for cnt_i in range(1,10): # 1~9라운드 반복문 처리
        out_state = AES_One_Round(new_state, round_key[cnt_i])
        new_state = copy.deepcopy(out_state)
        print('   Round',cnt_i, ': ', end='')
        dec2hex(new_state)
 
    # 마지막 라운드 , 믹스컬럼을 제외한 3단계
    # SubBytes -> ShiftRows -> AddRoundKey 
 
    output_state_1 = SubBytes(new_state)
    output_state_2 = ShiftRows(output_state_1)
    output_state_3 = AddRoundKey(output_state_2, round_key[10])
    print('   Round 10 : ', end='')
    dec2hex(output_state_3)
    return output_state_3
    
key = [ 0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6,
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c ]
 
block = [ 0x6e, 0x31, 0x63, 0x65, 0x20, 0x77, 0x30, 0x72, 
          0x6b, 0x20, 0x41, 0x45, 0x53, 0x74, 0x78, 0x74]
 
         
input_state = block2state(block)
key_state = block2state(key)
 
 
print('='*89)
print('')
print('     plaintext : n1ce w0rk AEStxt ')
print('plaintext(hex) : ', end='')
dec2hex(input_state)
 
print('           key : ', end='')
dec2hex(key_state)
 
print('')
print('='*39, 'Rounds', '='*42)
 
new_state = AES_128_Encryption(input_state, key_state)
 
 
print('='*89)
print('')
print('  ciphertext : ', end='')
dec2hex(new_state)
print('')

