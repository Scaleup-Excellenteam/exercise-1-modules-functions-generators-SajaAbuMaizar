# Open the logo file in binary mode
with open('resources/logo.jpg', 'rb') as f:
    # Read the first 100 bytes of the file
    data = f.read(100)

    # Search for the secret messages
    messages = []
    start_index = data.find(b'\xff\xc0\x00\x11\x08')
    while start_index != -1:
        # Extract the message
        message = data[start_index + 5:start_index + 10].decode('ascii')
        messages.append(message)

        # Move to the next message
        start_index = data.find(b'\xff\xc0\x00\x11\x08', start_index + 10)

    # Print the messages
    for message in messages:
        print(message)
