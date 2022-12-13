from cli_parser import StringFlag, BooleanFlag, Cli_Args
from ssh_client import Ssh_connect


def run():
    hostname_flag = StringFlag(short="a", long="hostname", mandatory=True)
    privatekey_flag = StringFlag(short="p", long="privatekey", mandatory=True)
    username_flag = StringFlag(short="n", long="username", mandatory=True)
    servicename_flag = StringFlag(short="s", long="servicename")
    status_flag = BooleanFlag(short="z", long="status")
    start_flag = BooleanFlag(short="x", long="start")
    stop_flag = BooleanFlag(short="y", long="stop")
    restart_flag = BooleanFlag(short="r", long="restart")
    mask_flag = BooleanFlag(short="m", long="mask")
    unmask_flag = BooleanFlag(short="u", long="unmask")
    cli_argv = Cli_Args(flags=[hostname_flag, privatekey_flag,username_flag,
                        servicename_flag, status_flag, start_flag,stop_flag, restart_flag,mask_flag,unmask_flag])
    
    hostname, privatekey, user, service_name,status, start, stop, restart, mask, unmask = cli_argv.parse()
    
    ssh_connect = Ssh_connect(hostname, privatekey, username=user)
    
    if start:
        ok = ssh_connect.start(service_name)
        if ok:
            print("service: {} started successfully".format(service_name))
        else:
            print("could not start the service")
    elif stop:
        ok = ssh_connect.stop(service_name)
        if ok:
            print("service: {} stopped successfully".format(service_name))
        else:
            print("could not stop the service")
    elif restart:
        ok = ssh_connect.restart(service_name)
        if ok:
            print("service: {} resetarted successfully".format(service_name))
        else:
            print("could not restart the service")
    elif mask:
        ok = ssh_connect.mask(service_name)
        if ok:
            print("service: {} masked successfully".format(service_name))
        else:
            print("could not mask the service")
    elif unmask:
        ok = ssh_connect.unmask(service_name)
        if ok:
            print("service: {} unmasked successfully".format(service_name))
        else:
            print("could not unmask the service")
    elif status:
        ok = ssh_connect.status(service_name)
        print(ok)
    else:
        services = ssh_connect.list_services()
        print(services)
    
    
            
    

if __name__ == '__main__':run()
