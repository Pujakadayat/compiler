f_name = input("What is the name of the file?\n")

file_in = open(f_name, 'r')
num_chars = 0

for line in file_in:
    word_list = line.split()
    num_chars += sum(len(word) for word in word_list) #produces length of each word and appends to sum

print(num_chars)
