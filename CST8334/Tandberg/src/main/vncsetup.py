##########################################################
# CST8334 2018W-Software Development Project             #
# Author: Binh Minh Do                                   #
# April 7 2018                                           #
#update code from https://pypi.python.org/pypi/telnetlib3#
##########################################################
import asyncio, telnetlib3

@asyncio.coroutine
def shell(reader, writer):#--shell=my_module.fn_shell
    while True:
        # read stream until found
        outp = yield from reader.read(1024)
        if not outp:
            # End of File
            break
        # Using API library xconfiguration to set up a vnc with Tandberg system
        elif 'Password:' in outp:
            writer.write('TANDBERGsys##01\r\nxconfiguration vnc password: 1234\r\n')


# Set the event loop to use
loop = asyncio.get_event_loop()

# Connect to a TCP Telnet server as a Telnet client
coro = telnetlib3.open_connection('10.50.18.143', 23, shell=shell)

# Blocking call which  returns when connecting is done
reader, writer = loop.run_until_complete(coro)

# Executing command
writer.protocol