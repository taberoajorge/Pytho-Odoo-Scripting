arrayKeys = ['Name', 'Last Name', 'Username','Email', 'Phone', 'Date', 'Time', 'Page URL', 'User Agent', 'Remote IP', 'Powered by']
dictionary = {}
positions_final = []
positions_initial = []
i = 0
e = 0

for record in records:
  for message in record.message_ids:
    # raise Warning(record.message_ids.name)
    if 'Name' in message.body:
      contents = message.body
      # raise Warning(contents)
      
      def remove_tags(text):
        tag = False
        quote = False
        out = ""
        for c in text:
          if c == '<' and not quote:
              out = out + " "
              tag = True
          elif c == '>' and not quote:
              tag = False
          elif (c == '"' or c == "'") and tag:
              quote = not quote
          elif not tag:
              out = out + c
        return out
      
      sanitize_message = remove_tags(contents)


      def dictionary_create(array, text):
        for i in range(len(array)):
          if array[i] in text:
            init = text.find(array[i])
            last = init + len(array[i])
            complete = text[init:last]
            init_user = last + 1
            positions_initial.append(init_user)
            if i < 10:
                last_user = text.find(array[i+1])
            if i == 11:
                dictionary['Page URL'] = "https://e-rest.restbar.com.mx/empezar-a-vender/"
                # dictionary['Powered by'] = "Elementor"
                break
            positions_final.append(last_user)
            complete_user = text[positions_initial[i]:positions_final[i]]
            dictionary[complete] = complete_user
            i += 1
      
      dictionary_create(arrayKeys, sanitize_message)
      # raise Warning(str(dictionary))
      value = dictionary.values()
      record['name'] = dictionary['Name'] + ' ' + dictionary['Last Name']
      record['x_nombre_comercial_lead'] = dictionary['Username'] 
      record['email_from'] = dictionary['Email'] 
      record['phone'] = dictionary['Phone'] 
      record['description'] = dictionary['Date'] + ' ' + dictionary['Time'] + '\n' +  dictionary['User Agent']  + '\n' + dictionary['Remote IP'] + '\n' + dictionary['Powered by'] 
      
