i1 = input("Geben Sie Ihr zu reduzierendes Polynom an (x^20+1 --> 100001 ohne Ox): ")
i2 = input("Geben Sie Ihre erzeugende Relation an (x^20+1 --> 100001 ohne Ox): ")

try:
    ini1 = format(int(i1, 16), "b")  # Convert to binary and remove "0b" prefix
    ini2 = format(int(i2, 16), "b")
except ValueError:
    print("Sie haben keine gültige Hexadezimalzahl eingegeben.")

def shifter(var1, var2):
    var1str = str(var1)
    var2str = str(var2)
    index1 = 0
    index2 = 0
    liste1 = []
    liste2 = []

    for bit in var1str:
        if bit == "1":
            liste1.append(index1)
        index1 += 1
    liste1.reverse()
    print(liste1)

    for bit in var2str:
        if bit == "1":
            liste2.append(index2)
        index2 += 1
    liste2.reverse()
    print(liste2)

    highestpoly1 = max(liste1)
    highestpoly2 = max(liste2)

    highestpoly1 = int(highestpoly1)
    highestpoly2 = int(highestpoly2)

    x = highestpoly1 - highestpoly2
    print(x)
    return x

def modreduct(strini1, strini2, xlast, counter = 0):
    x = shifter(strini1, strini2)

    if x < 0:
        print("There is nothing to do.")
        result = strini1
        return result
    else:
        int_str1 = int(strini1, 2)
        int_str2 = int(strini2, 2)

        if x == xlast and counter >= 1:
            outputstr = int_str1 ^ int_str2
            result = format(outputstr, "b")
            return result

        elif x != 0:
            outputstr = int_str1 ^ (int_str2 << x)
            result = modreduct(format(outputstr, "b"), strini2, x, counter + 1)
            return result

        else:
            outputstr = int_str1 ^ int_str2
            result = format(outputstr, "b")
            return result

result = modreduct(ini1, ini2, -1)
hexstr_result = "0x" + hex(int(result, 2))[2:]
hex_result = hex(int(result, 2))[2:]
print(hexstr_result)
