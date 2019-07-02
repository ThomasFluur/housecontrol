# import time, This file/module read the user file


import datetime  # Import all?
filename = 'DefaultUser.txt'


def create_attention_lists(userphoneandmail):
    users = []  # List [
    phones = []  # List of alarms
    status_phones = []   #  List of Status :
    to_mail_list = []   #  List of mail
    status_mail = []   #  Mail status
    user_log = [] # Build list of string to report, Each warning and error should be a line.
      # Or use a file reference and add new string? One log for each start session.
      # Possible to copy a file with open session with contents included?
      # HeaderOnTable= "User" "/t" "Acesslevel" "/t" "Celluar phones" "/t" "Voice phone" "/t" "Mail adress" "/t"
      # "Created" "/t" "Valid until" "/t" "User password" Vände jag på / \?
    logstring = ""
    start = "StartOfTable"
      # EndOfF *undantag*
    try:
        user_file = open(userphoneandmail,'r') # The reference to file? Not the  name!?
        row = 0
        for line in user_file:
            row = row+1
            if line.strip() == (start): # Sort out where the table starts
                found_table_start = True
                break # Jump to read line. Header infromation is not used from text file
            else:
                found_table_start=False # Use false to create an error log if wrong file o
                #  user_log.append("Didn't find file ", userphoneandmail)
                # logstring = logstring +"Didn't find file ", userphoneandmail)
        for line in user_file:
            users.append(line)  #Skip this line?
            row = row+1
            line = line.strip()  #tar bort radslut?
            try:
                acess_level, user_phone,e_mail,valid_until = line.split (',') # The pattern must match. replace with try?
                # Should be  possible to ignore if more fields are added? Check how CSV modules work
                #What happens if blankrow are added?
                try :
                    Year,Month,Day =valid_until.split ('-') # If format doesn't match on the string it assume there should be no limit
                    Year= int(Year) # Convert to integer to use in date function
                    Month= int(Month)
                    Day= int(Day)
                    AcessUntil = datetime.datetime (Year,Month,Day)
                    CurrentTime =datetime.datetime.now ()
                    if AcessUntil > CurrentTime: # Don't add guest user which date have passed to  the list
                        use_line =True
                    else:
                        use_line =False # The user that have pass date should be removed from list
                except ValueError:
                    use_line = True
                if use_line : # Create list of phone and mail to inform with alarm as bugler or  fire
                    phone_check = list(user_phone)
                    phone_number_length = len (user_phone)
                    pc2 = phone_check[:1]  # 0 didn't work contain 0 or + , (Capital letter? ignored for the  moment)
                    # print (pc2)
                    pc1 = ''.join(phone_check[1:])
                    # print (pc1) Skippa felsökning lägg det på format vid inmatning stora bokstäver. #*- finns också
                    phones.append (user_phone) # phone number with capital letter exist in US and UK.
                    # No check for insane  number yet
                    use_mail = e_mail.find ('@') > 0  # Do a simple check that @ is included.
                                                    # Use variabel since bad mail can be added in both mail list
                    if use_mail:
                        to_mail_list.append(e_mail) # No sanity check on mail yet. Wiki have a defintion of unvalid e-mail adress
                    else:
                        mailwithnosnabel = 'Time: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())+'Bad mail in line'+str(row)+" "+str(line)+'in file '+str(userphoneandmail)
                        user_log.append(mailwithnosnabel) #Varför ger inte denna rad fel?
                    if acess_level== '3': # Create  list of  phone  for  status  or  just larm (Enum with string?)
                        status_phones.append (user_phone) # Some phone numbee will be in two  list
                        if use_mail:
                            status_mail.append (e_mail)  # Status mail adress is also larm no need to add twice
            except ValueError:
                # user_log.append("Row ",row," ",line,'in file ',userphoneandmail," bad format")
                add_this_string = 'Time: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())+"row "+str(row)+str(line)+" in file "+str(userphoneandmail)+" bad format(empty value error?)"
                user_log.append(add_this_string)
                # 'in file ', user_file, " bad format")
                # print ("Row ",row," ",line,'in file ',user_file," bad format")
            except TypeError:
                badline = 'Time: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())+"row "+str(row)+": "+str(line)+" in file "+str(userphoneandmail)
                #  print ('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
                user_log.append (badline)
        user_file.close ()
        if found_table_start :
            phones = set (phones) # Delete  phone used twice. Set changes the order but is not important
            to_mail_list =set (to_mail_list)
            status_mail = set (status_mail)
            status_phones = set (status_phones)
        else:
            missingstartrow = 'Time: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())+" Didn't found "+str(start)+' in file '+str(userphoneandmail)
            user_log.append (missingstartrow)#Hur hittar jag path?
            # Och hur ser den ut i byggd miljö?
    except FileNotFoundError:
        user_log.append ("Didn't find file ",userphoneandmail)

    # print (user_log)
    return phones, to_mail_list,status_phones, status_mail, user_log

AlarmPhones,AlarmMail,StatusP,StatusM,Log = create_attention_lists(filename) # Order from defs, Create new list drop error/warninng

print (Log)
LarmMessages = (AlarmMail, AlarmPhones) #create new tupples of phone an mail to use depending on use case to different user
StatusMessages = (StatusM, StatusP)
print (LarmMessages),
print (StatusMessages)
# print (create_attention_lists(filename))