#!C:\ci\anaconda-navigator_1537565961304\_h_env\pythonw.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'anaconda-navigator==1.9.2','gui_scripts','anaconda-navigator'
__requires__ = 'anaconda-navigator==1.9.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('anaconda-navigator==1.9.2', 'gui_scripts', 'anaconda-navigator')()
    )
