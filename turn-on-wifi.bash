#!/bin/vbash
source /opt/vyatta/etc/functions/script-template
configure
delete interfaces ethernet $1 disable
commit
exit