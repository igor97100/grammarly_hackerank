def decode(encoded_message):
    decoded_list = []
    for word in encoded_message:
        word = re.sub(r'[^a-zA-Z,:;.?!]+', '', word) #Removing everything except letters, commas, colons, semicolons and closing punctuation
        #Adding space after comma, colomn and semicolomn
        word = re.sub(r'(?<=[;:,])(?=[^\s])', ' ', word)
        decoded_list.append(word)

    #Finding dublicates
    dublicates = [cur for cur, next in zip(decoded_list, decoded_list[1:]) if cur == next]
    
    for dublicate in set(dublicates):
        dublicates_index = [i for i, x in enumerate(decoded_list) if x == dublicate] #Finding indexes of dublicates
        to_remove = []
        for i in range(len(dublicates_index)-1):
            if dublicates_index[i]+1 == dublicates_index[i+1]: #consequent dublicates must be removed
                to_remove.append(dublicates_index[i])
        
        for index in sorted(to_remove, reverse=True):# Pop in reverse order in order to maintain the indexes integrity
            decoded_list.pop(index)
    

    
    decoded_string = ' '.join(decoded_list) #joining all pieces of the message with a space
    return decoded_string