import sys


class HelpException(Exception):
    pass
class Help_Message():
    pass

class Flag:
    def __init__(self, short, long, mandatory=None, description = None):
        self.short = short
        self.long = long
        if mandatory is None:
            self.mandatory = False
        else:
            self.mandatory = mandatory
        self.description = description


class StringFlag(Flag):
    pass


class BooleanFlag(Flag):
    pass



class Cli_Args:
    
    def __init__(self, flags):
        self.flags = flags
        self.valid_flags = []
        for aflag in self.flags:
            self.valid_flags.append(aflag.long)
            self.valid_flags.append(aflag.short)
        self.help = ["-h","--h"]
        self.help_message = "Commands ProgramName StringFlag[] Value BooleanFlag[] Description \n LongOption ShortOption Description Mandatory"
        
        for aflag in self.flags:
            self.help_message = self.help_message + "\n" +  "--"+aflag.long +" " +"-"+aflag.short + " " + str(aflag.description) + " " + str(aflag.mandatory)

    def parse(self):
        data = sys.argv
        processed_info = {}
        for aflag in self.flags:
            if type(aflag) == StringFlag:
                processed_info[aflag.long]=None
            else:
                processed_info[aflag.long]=False            
        try:
            for i in range(1,len(data)):
                valid_flags = self.valid_flags
                if data[i].startswith("-") == True or data[i].startswith("--") == True:
                    if data[i].lstrip("--") not in valid_flags:
                        raise HelpException()
                
                for aflag in self.flags:
                    content = data[i]
                    
                    if aflag.short == content.lstrip("-") or aflag.long ==content.lstrip("--"):
                        if type(aflag) == StringFlag:
                            if i+1 < len(data):
                                for k,v in processed_info.items():
                                    if k == aflag.long:
                                        if v is None:
                                            processed_info[k] = data[i+1]
                                        else:
                                            raise HelpException()
                            else:       
                                raise HelpException()
                        if type(aflag) == BooleanFlag:
                            for k,v in processed_info.items():
                                if k == aflag.long:
                                    if v == False:
                                        processed_info[k] = True  
                                    else:
                                        raise HelpException()
        except HelpException as e:
            print(self.help_message)
            sys.exit()
        try:
            for aflag in self.flags:
                if aflag.mandatory:
                    if processed_info[aflag.long] is None:
                        raise HelpException()
        except HelpException as e:
            print(self.help_message)
            sys.exit()
        parsed_data=[]
        for k,v in processed_info.items():
            parsed_data.append(v)
        return parsed_data
             


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
                        servicename_flag,status_flag, start_flag,stop_flag, restart_flag,mask_flag,unmask_flag])
    
    data = cli_argv.parse()       
    print(data)
       
       

# def run():
#     hostname_flag = StringFlag(short="a", long="hostname", mandatory=True)
#     privatekey_flag = StringFlag(short="p", long="privatekey", mandatory=True)
#     servicename_flag = StringFlag(short="n", long="servicename")
#     start_flag = BooleanFlag(short="x", long="start")
#     restart_flag = BooleanFlag(short="r", long="restart")
#     cli_argv = Cli_Args(flags=[hostname_flag, privatekey_flag,
#                         servicename_flag, start_flag, restart_flag])
#     data = cli_argv.parse()
#     print(data)


if __name__ == '__main__':run()


 
        # if len(data)>1:
            
        #     for bflag in self.flags:
        #         content = data[i]
        #         if content == "-h" or content == "--help":
        #             raise HelpException()
        #         if content.startswith("--") == True or content.startswith("-") == True:
        #             content = content.lstrip("--")
        #             if bflag.short == content or bflag.long == content:
        #                 if type(bflag) == StringFlag:
        #                     if i+1<len(data):
        #                         value = data[i+1]
        #                         for k,v in processed_info.items():
        #                             if k == bflag.long:
        #                                 processed_info[k] = value
                                        
        #                     if i+2 <len(data):
        #                         i=i+2
        #                 else:
        #                     for k,v in processed_info.items():
        #                             if k == bflag.long:
        #                                 processed_info[k] = True
        #                                 i=i+1                           
                    
                
                
                # else:
                #     parsed_data = []
                #     for k,v in processed_info.items():
                #         parsed_data.append(v)
        # return processed_info
                

                # if len(data) >1:
                #     for aflag in self.flags:
                #         try:
                #             if i<len(data):
                #                 content = data[i]
                #             if type(aflag) == StringFlag:
                #                 if content.startswith("-") is True or content.startswith("--") is True:
                #                     content = content.lstrip("--")
                #                     if aflag.short == content or aflag.long == content:
                #                         processed_data.append(data[i+1])
                #                         i = i+2
                #                     else:
                #                         raise HelpException
                #                 else:
                #                     processed_data.append(None)
                #             if type(aflag) == BooleanFlag:
                #                 status = False
                #                 if content.startswith("-") is True or content.startswith("--") is True:
                #                     content = content.lstrip("--")
                #                     if aflag.short == content or aflag.long == content:
                #                         status = True
                #                         processed_data.append(status)
                #                         i=i+1
                #                     else:
                #                         processed_data.append(status)
                #                 else:
                #                     processed_data.append(status)
                #         except HelpException as e:
                #             print("couldnt parse")
                #             return
                # else:
                #     for aflag in self.flags:
                #         if type(aflag) == StringFlag:
                #             processed_data.append(None)
                #         else:
                #             processed_data.append(False)
                # return processed_data
