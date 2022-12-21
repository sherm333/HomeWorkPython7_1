import imp
import export
import input
import logg

def start():
    if input.mod() == '1':
        info = input.exp()
        export.expp(info)
        logg.log_info(info)
    else:
        info = input.inpp()
        imp.impo(info)
        logg.log_info(info)