
with open('prashant.text', 'r') as testing1:
    content = testing1.readlines()
    with open('prashant.text', 'w') as testing2:
        for i in reversed(content):
            testing2.write(i)
