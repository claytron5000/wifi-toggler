#!/bin/vbash
source /opt/vyatta/etc/functions/script-template
configure
set interfaces ethernet $1 disable
commit
exit
sleep $2
configure
delete interfaces ethernet $1 disable
commit
exit