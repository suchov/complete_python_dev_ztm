# 2 inputs and then work with the string and print it

passowrd = input('password please')
secret = input('please give me secret')
pass_length = len(passowrd)
username = "Artem"


print(f'{username}, you passowrd {"*" * pass_length} is {pass_length} and the secret is {secret}')
