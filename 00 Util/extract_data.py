import re

path1 = "./fine_tuning01.txt"
path2 = "./fine_tuning02.txt"



# 1. read files: string lists
fine_tuning_file1 = open(path1)
fine_tuning_file2 = open(path2)
content1 = fine_tuning_file1.readlines()
content2 = fine_tuning_file2.readlines()



# 2. extract necessary lines: string lists
train_lines1, valid_lines1, train_lines2, valid_lines2 = [], [], [], []
line_lists = [train_lines1, valid_lines1, train_lines2, valid_lines2]

for i in range(8):
    train_lines1.append(content1[3 + i*5])
    valid_lines1.append(content1[4 + i*5])

for i in range(10):
    train_lines2.append(content2[3 + i*5])
    valid_lines2.append(content2[4 + i*5])

for li in line_lists:
    for line in li:
        print(line)

        
        
# 3. extract numeric values: float lists

train_loss_1, valid_loss_1, train_loss_2, valid_loss_2 = [], [], [], []
train_acc_1, valid_acc_1, train_acc_2, valid_acc_2 = [], [], [], []

loss_results = [train_loss_1, valid_loss_1, train_loss_2, valid_loss_2]
acc_results  = [train_acc_1, valid_acc_1, train_acc_2, valid_acc_2]

loss_pattern = "loss:\s+\d+\.\d+"
acc_pattern  =  "acc:\s+\d+\.\d+"
value_pattern = "\d+\.\d+"

for i, line_list in enumerate(line_lists):
    for line in line_list: 
        loss_t = re.search(loss_pattern, line).group()
        loss_t = re.search(value_pattern, loss_t).group()
        loss_results[i].append(float(loss_t))
        acc_t = re.search(acc_pattern, line).group()
        acc_t = re.search(value_pattern, acc_t).group()
        acc_results[i].append(float(acc_t))

print(train_loss_1)
print(valid_loss_1)
print(train_loss_2)
print(valid_loss_2)
print()
print(train_acc_1)
print(valid_acc_1)
print(train_acc_2)
print(valid_acc_2)
