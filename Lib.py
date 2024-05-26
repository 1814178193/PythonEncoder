def encoding(string):
    code="!@#$%^&*()_+{}:<"
    result=""
    output=[]
    for i in range(len(string)):
        output.append(hex(ord(string[i]))[2:])
        while len(output[i])<4:
            output[i]="0"+output[i]
        output[i]=code[int(output[i][3],16)]+code[int(output[i][0],16)]+code[int(output[i][2],16)]+code[int(output[i][1],16)]
        result=result+output[i]
    return(result)

def decoding(string):
    code="!@#$%^&*()_+{}:<"
    output=[]
    result=""
    for i in range(int(len(string)/4)):
        output.append(string[i*4:i*4+4])
        output[i]=str(hex(code.index(output[i][1])))[2:]+str(hex(code.index(output[i][3])))[2:]+str(hex(code.index(output[i][2])))[2:]+str(hex(code.index(output[i][0])))[2:]
        output[i]=chr(int(output[i],16))
        result=result+output[i]
    return(result)


