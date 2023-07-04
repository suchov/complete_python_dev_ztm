# wizard game
is_magician = False
is_expert = True

# check if magician AND expert: "you are the master magician"
if is_magician and is_expert:
    print("you are the master magician")
# check if magician but not expert: "at least you are getting there"
elif is_magician and not is_expert:
    print("at least you are getting there")
# if you not a magician print: "you need magic powers"
elif not is_magician:
    print("you need magic powers")
