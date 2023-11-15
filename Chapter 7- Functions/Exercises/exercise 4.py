def make_shirt(size='large',message='i love python'):
    summary=('\n''creating a '+size+'-sized shirt with the message:'+message)
    print(summary)

#default message
make_shirt()

#medium size
make_shirt(size='meduim')
make_shirt(size='small',message='rawr')
