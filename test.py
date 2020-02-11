import dtwp
import random

def calculate_result(blist):

  howmanytrue = blist.count(True)
  howmanyfalse = blist.count(False)

  print('Accepted falses: ' + str(howmanytrue) + '/' + str(howmanytrue+howmanyfalse))
  print('%: ' + str(float(howmanytrue)/(howmanytrue+howmanyfalse)))


# create ranges for (ord/chr)-function for 
# most common letters and nums
lower_alph = range(97, 122)
upper_alph = range(65, 90)
range_num = range(48, 57)
letters_ranges = range_num + upper_alph + lower_alph 

# generate a code
hashlen = 1
code = str(random.randint(0, 1000))
hashed_code = dtwp.hashcode(code, hashlen)

# run tests for this code
print('Random test code[str] is : ' + code + ' Hashed code is: ' + hashed_code)


# test changing a letter
bool_list1 = []
for i in range(len(hashed_code)):
  for j in letters_ranges:
    trycodel = list(hashed_code)
    trycodel[i] = chr(j)
    trycodestr = ''.join(trycodel)

    # check code if it's not the same as original code
    if (trycodestr != hashed_code):
      bool_list1.append(dtwp.check_code(trycodestr, hashlen))

print('\n*** Test replacing a letter ***')
calculate_result(bool_list1)

# test removing a letter
bool_list2 = []
for i in range(len(hashed_code)):
  trycodel = list(hashed_code)
  trycodel.pop(i)
  trycodestr = ''.join(trycodel)
  bool_list2.append(dtwp.check_code(trycodestr, hashlen))

print('\n*** Test removing a letter ***')
calculate_result(bool_list2)

# test adding an extra letter
bool_list3 = []
for i in range(len(hashed_code)+1):
  for j in letters_ranges:
    trycodel = list(hashed_code)
    trycodel = trycodel[0:i] + [chr(j)] + trycodel[i:] 
    trycodestr = ''.join(trycodel)

    bool_list3.append(dtwp.check_code(trycodestr, hashlen))

print('\n*** Test adding an extra letter ***')
calculate_result(bool_list3)


print('\n**** Total results and approximated pass rate are ****')
calculate_result(bool_list1 + bool_list2 + bool_list3)