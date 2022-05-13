# Your code here!!
def sing():
    sing = ""
    for i in range(12):
        if i == 4:
            sing += "whisper words of wisdom"
        elif i == 10:
            sing += "there will be an answer"
        else:
            sing += "let it be"
        if i < 11:
            sing += ", "
    return sing

print(sing())
