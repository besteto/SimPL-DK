import sys
import datetime
 
 
class logger(object):
    instance = None
 
    def __init__(self, tag):
        self.tag = '[' + str(tag) + '] '
 
    def timestamp(self):
        return '[' + datetime.datetime.now().strftime('%H:%M:%S') + ']'
 
    def prn(self, msg, prefix='> ', endl='\n', args=[]):
        msg = prefix + self.timestamp() + self.tag + msg + endl
        msg = msg.format(*args,
                         W='\033[97m',  # white
                         R='\033[91m',  # lt red
                         Y='\033[93m',  # lt yellow
                         G='\033[92m',  # lt green
                         C='\033[96m',  # lt cyan
                         B='\033[94m',  # lt blue
                         P='\033[95m',  # lt purple
                         D='\033[37m',  # lt gray
                         d='\033[90m',  # gray
                         r='\033[31m',  # red
                         y='\033[33m',  # yellow
                         g='\033[32m',  # green
                         c='\033[36m',  # cyan
                         b='\033[34m',  # blue
                         p='\033[35m')  # purple
 
        sys.stdout.write(msg)
        sys.stdout.flush()
 
    def nfo(self, msg, endl='\n', args=[]):
        self.prn(msg,
                 prefix='{c}# ',
                 endl=endl,
                 args=args)
 
    def wrn(self, msg, endl='\n', args=[]):
        self.prn(msg,
                 prefix='{y}* ',
                 endl=endl,
                 args=args)
 
    def err(self, msg, endl='\n', args=[]):
        self.prn(msg,
                 prefix='{r}! ',
                 endl=endl,
                 args=args)
 
    def dbg(self, msg, endl='\n', args=[]):
        self.prn(msg,
                 prefix='{d}# ',
                 endl=endl,
                 args=args)
 
    def checker(self, msg, checker, args=[]):
        res = ' ... {g}SUCCESS' if checker else' ... {r}FAILED'
        self.nfo(msg + res, args=args)
 
 
def get(tag):
    return logger(tag)
 
# test
 
if __name__ == '__main__':
 
    log = get('LOG')
    log.prn(
        '{r}RED {p} PURPLE {y} YELLOW {g} GREEN {c} CYAN {b} BLUE {d} DARK ')
    log.prn(
        '{R}RED {P} PURPLE {Y} YELLOW {G} GREEN {C} CYAN {B} BLUE {D} DARK ')
 
    log.dbg('It is debug {g}message')
    log.nfo('It is info  {y}message')
    log.wrn('It is warn  {b}message')
    log.err('It is error {c}message')
 
    for x in xrange(10):
        log.checker('pass: {B}{0}', (x > 5), args=[x])
