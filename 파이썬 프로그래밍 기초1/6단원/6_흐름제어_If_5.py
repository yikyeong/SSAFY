msg = input()

if msg.isupper():
    print(f"{msg}(ASCII: {ord(msg)}) => {msg.lower()}(ASCII: {ord(msg.lower())})")
elif msg.islower():
    print(f"{msg}(ASCII: {ord(msg)}) => {msg.upper()}(ASCII: {ord(msg.upper())})")
else:
    print(msg)