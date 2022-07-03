import os


#place your fdc -file-directory-command--



with open('cmds\list1.txt') as a:
    list1 = a.read()



#do not touch
cmd = input ('>')
#do not touch






if cmd == list1:
    os.system('cmd.exe')

#place your -cec -command-execution-code--











#end
else:
    print ('[   ERROR  ] command invalid or corupt')
input('press enter to exit')