try:
    file = open("a_file.txt")
except:
    open("a_file.txt", "w")
finally:
    file.close()