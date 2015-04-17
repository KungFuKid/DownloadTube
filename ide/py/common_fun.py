import subprocess


def run(cmd):
    proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err=proc.communicate()
    code=proc.returncode
    return (out,code)
    
def BoolRun( cmd ):
    print ("exec cmd begin:"+cmd)
    ret = run( cmd )
    if ret[1]==0:
        print ("exec cmd end~~~")
        return True

    print ("exec cmd failed:"+ret[0])
    return False


