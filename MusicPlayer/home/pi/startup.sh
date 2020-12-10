#!/bin/sh

/usr/bin/screen -S startupSh -d -m /bin/sh -c "echo '----  Starting script   ----'; /usr/bin/python3 music.py; echo '----  Script has ended  ----'; exec /bin/sh"