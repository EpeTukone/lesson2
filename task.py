def ssl(text, set_of):
    text = text.lower()
    counter = 0
    for word in set_of:
        if word in text:
            counter += 1
    return counter
set_of = set(["hel", "life", "Forever","your"])
print(ssl("forever dsdsdsd rrrer life", set_of))


