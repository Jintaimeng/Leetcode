class Solution:
    def strEncodeAndDecode(self):
        encodedStr = input()
        deStr = ""
        for es in encodedStr:
            if es.isalpha():
                if es == "z":
                    deStr += "A"
                elif es == "Z":
                    deStr += "a"
                else:
                    t = chr(ord(es) + 1)
                    if t.islower():
                        deStr += t.upper()
                    elif t.isupper():
                        deStr += t.lower()
            elif es.isdigit():
                if es == "9":
                    deStr += "0"
                else:
                    deStr += str(int(es) + 1)
        print(deStr)

        decodedStr = input()
        enStr = ""
        for ds in decodedStr:
            if ds.isalpha():
                if ds == "a":
                    enStr += "Z"
                elif ds == "A":
                    enStr += "z"
                else:
                    t = chr(ord(ds) - 1)
                    if t.islower():
                        enStr += t.upper()
                    elif t.isupper():
                        enStr += t.lower()
            elif ds.isdigit():
                if ds == "0":
                    enStr += "9"
                else:
                    enStr += str(int(ds) - 1)
        print(enStr)


def main():
    Solution().strEncodeAndDecode()


if __name__ == "__main__":
    main()