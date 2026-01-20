2026Jan19 - LabEx - Explore Character Encoding History and Concepts

In Python 3, the default encoding is UTF-8, which allows for the direct use of characters from various languages,

built-in Python functions ord() and chr() to convert between characters and their corresponding integer representations in Unicode.


char1 = 'ਅ'
char2 = 'a'
char3 = ';'

print(f"the Unicode decimal value of '{char1}' is {ord(char1)}")
print(f"the Unicode decimal value of '{char2}' is {ord(char2)}")
print(f"the Unicode decimal value of '{char3}' is {ord(char3)}")

int1 = 2565
int2 = 2569

print(f"The char for Unicode deciment valur {int1} is {chr(int1)}")
print(f"The char for Unicode deciment valur {int2} is {chr(int2)}")



II Convert Between Strings and Bytes with encode() and decode()

how to convert between Python strings (which are Unicode) and bytes objects using the encode() and decode() methods. This is essential when dealing with data that needs to be transmitted or stored in a specific encoding format.
- encode() method is used to convert a string into a bytes object using a specified encoding. It returns a bytes object
- 

