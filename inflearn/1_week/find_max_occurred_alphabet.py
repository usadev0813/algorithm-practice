# ord() : 아스키코드 -> 숫자 변환 함수
# chr() : 숫자 -> 아스키코드 변환 함수
# isalpha() : 알파벳인지 유무 체크 함수

def find_max_occurred_alphabet(string):
    alphabet_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    print(alphabet_array)

    for index in range(len(alphabet_array)):
        alphabet_occurrence = alphabet_array[index]

        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index
    return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet
print(f"정답 : {result("hello my name is jeongho")}")