def disemvowel(string_):
    return "".join([str_chr for str_chr in string_ if str_chr.lower() not in "aeiou"])



# def disemvowel(string):
#     return string.translate(None, 'aeiouAEIOU')

print(disemvowel("This website is for losers LOL!"))