

class HexSpeakHelper:
    def dec2Hex(self,st):
        dec_num = int(st)

        result = []
        while dec_num>0:
            result.append(dec_num%16)
            dec_num //= 16
        return result[::-1]
    def dec2HexSpeak(self,st):
        hex_val = self.dec2Hex(st)

        ans = ""

        lut = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',0:'O',1:'I'}

        for char in hex_val:
            print(char)
            if char in lut:
                ans += lut[char]
            else:
                raise Exception('Hex value: '+str(char)+", does not have a hexspeak value")
        return ans


answer = HexSpeakHelper()
print(answer.dec2Hex('258'))
print(answer.dec2HexSpeak('257'))