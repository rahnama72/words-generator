import RE 
import String
import RSTR
def words_generator(upper=0,lower=0,digit=0,special=0):
    '''
    Requirement Package: 1.RE 2.String 3.RSTR
    :param upper: Number of Uppercase chars.
    :param lower: Number of lowercase chars.
    :param digit: Number of digits.
    :param special: Number of special chars.
    :return: random word.
    '''
    re_upper  = '[A-Z]'
    re_lower  = '[a-z]'
    re_digit  = '\d'
    re_special= '[,@\'?\.$%_]'
    word = []
    if upper:
        for i in range(upper):
            word.append(re_upper)
    if lower:
        for j in range(lower):
            word.append(re_lower)
    if digit:
        for k in range(digit):
            word.append(re_digit)
    if special:
        for l in range(special):
            word.append(re_special)
    random.shuffle(word)
    final_word = ''.join(word)
    final_word = rstr.xeger(final_word)
    return final_word
# print(words_generator(2,3,2,2))
