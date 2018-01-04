import psutil
import os
import getpass
import time
import os.path
import shutil
import datetime
import operator
import math
import re
import datetime
import calendar
import stat

class errors():
    def __init__(self):
        pass
    def error1(self):
        print("Error 01:The disk could not be found")
    def error2(self):
        print("Error 02:Unable to retreat")
    def error3(self):
        print("Error 03:Incorrect input format")
    def error4(self):
        print("Error 04:The file does not exist")
    def error5(self):
        print("Error 05:File copy failure")
    def error6(self):
        print("Error 06:File path illegal")
    def error7(self):
        print("Error 07:Unable find the file")
    def error8(self):
        print("Error 08:Unable find the dir")
    def error9(self):
        print("Error 09:Command format error")
    def error10(self):
        print("Error 10:There are duplicate files in the current directory")

class screen():
    path = "unknow"
    def __init__(self):
        pass
    def msgPut(self,text):
        print(text)
    def pidPut(self,model):
        if(model == "all"):
            print(psutil.pids())
        else:
            pid = int(model)
            print(psutil.Process(pid))

class powerSet():
    path = "unknow"
    def __init__(self):
        pass
    def userRWSet(self,name,order):
        if(order == "-ur"):
            os.chmod(self.path + '\\' + name,stat.S_IWOTH)
        if(order == "-uw"):
            os.chmod(self.path + '\\' + name,stat.S_IROTH)
    def groupRWSet(self,name,order):
        if(order  == "-gr"):
            os.chmod(self.path + '\\' + name,stat.S_IWGRP)
        if(order  == "-gw"):
            os.chmod(self.path + '\\' + name,stat.S_IRGRP)
    def readOnlySet(self,order,name):
        if(order == "-r"):
            os.chmod(self.path + '\\' + name,stat.S_IREAD)
        if(order == "-rw"):
            os.chmod(self.path + '\\' + name,stat.S_IWRITE)

class shellHelp():
    def Help():
        helpStr = """
        ******本shell系统装载了如下功能******
        help:
            查询帮助信息
        clear:
            清空屏幕
        mem/m:
            查询电脑当前内存使用状态
        date:
            -r:查询电脑开始运行时间
            -t:查询当前时间
            -y year:查询指定年份下日历
            -c year,startmonth,endmonth:查询指定年份下，指定起始及终止月份日历
            -q year,quartor:查询指定年份下，指定季度日历
            -m year,month:查询指定年份下，指定月份的日历
        cp:
            name:复制当前目录下指定名字文件
            name -m:复制指定名字文件到指定目录下
            name -r:复制当前目录下指定名字文件并删除源文件
        echo:
            string:打印输出的字符串
        mkdir:
            dirname:在当前目录下创建指定名字文件夹
        rmdir:
            removeDirName:在当前目录下删除指定名字文件夹
        cd/CD:
            ../.:返回上一级目录
            dirname:进入指定名字的目录
        ls:
            打印当前目录下所有文件名字
        wc:
            -c name:输出当前目录下指定名字的文件的字节数
            -l name:输出当前目录下指定名字的文件的行数
            -m name:输出当前目录下指定名字的文件的字符数
            -w name:输出当前目录下指定名字的文件的字数(数字,大小写字母)
            -L name:输出当前目录下指定名字的文件的最长行长度
        pwd:
            打印当前所在目录的绝对路径
        more:
            name:浏览当前目录下指定名字文件内容 空格向下翻页 b向上翻页 q/quit退出浏览模式
        q/quit:
            退出shell
        "disk:"
            进入指定盘符磁盘下根目录(必须带引号)
        show:
            name:打印当前目录下指定名字文件所有内容
        pid:
            输出当前系统内所有运行进程的pid
            pid:输出指定pid的进程的详细信息
        history:
            打印所有曾输入过的命令
            n:打印距最近输入命令为n的所有命令
        chmod:
            -r name:设置当前路径下的目标文件为只读
            -rw name:取消当前路径下的目标文件的只读限制
            -ur name uid:给予指定uid用户当前路径下的目标文件读权限
            -uw name uid:给予指定uid用户当前路径下的目标文件写权限
            -gr name gid:给予指定用户组当前路径下的目标文件读权限
            -gw name gid:给予指定用户组当前路径下的目标文件写权限
        """
        print(helpStr)

class dateCommmand():
    error = errors()
    def __init__(self):
        pass
    def runningTime(self):
        now = datetime.datetime.fromtimestamp(time.time())
        startRunTime = datetime.datetime.fromtimestamp(psutil.boot_time ())
        sec = ((now - startRunTime).seconds)  
        print("The computer has been running for " + self.secExchange(sec))
    def whatTime(self):
        print(datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H: %M: %S"))
    def kalendor(self,model,mtime):
        print("*"*40)
        if(model == "y"):
            print ("Below is year " + mtime + "calendar: ")
            calendar.prcal(int(mtime))
        elif(model == "q"):
            mran = mtime.split(",")
            year = mran[0]
            print ("Below is year " + year + "calendar: ")
            q = mran[1]
            if(q == "1"):
                mst = 1
                med = 3
            elif(q == "2"):
                mst = 4
                med = 6
            elif(q == "3"):
                mst = 7
                med = 9
            elif(q == "4"):
                mst = 10
                med = 13
            else:
                self.error.error3()
                return -1
            for i in range(mst,med+1):  
                m = calendar.month(int(year),i)  
                print(m)
        elif(model == "c"):
            mran = mtime.split(",")
            year = int(mran[0])
            print ("Below is year %d calendar: "%(year))  
            mst = int(mran[1])
            med = int(mran[2])
            if(mst <= 0 or med > 12):
                self.error.error3()
                return -1
            for i in range(mst,med+1):  
                m = calendar.month(int(year),i)  
                print(m)
        else:
            mran = mtime.split(",")
            year = int(mran[0])
            print ("Below is year %d calendar: "%(year))
            m = int(mran[1])
            print(calendar.month(int(year),m))
        print("*"*40)
    def secExchange(self,sec):
        day = 24*60*60  
        hour = 60*60  
        min = 60  
        if(sec <60):          
            return  "0d 0h 0min %dsec"%math.ceil(sec)  
        elif(sec > day):  
            days = divmod(sec,day)   
            return "%dd, %s"%(int(days[0]),self.secExchange(days[1]))  
        elif(sec > hour):  
            hours = divmod(sec,hour)  
            return '%dh, %s'%(int(hours[0]),self.secExchange(hours[1]))  
        else:  
            mins = divmod(sec,min)  
            return "%dm, %ds"%(int(mins[0]),math.ceil(mins[1]))

class memoryCommands():
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)
    #def pidGet():
    #    i = 1
    def usingMemory():
        mem = psutil.virtual_memory()
        outPut = "There memory of the system being used is %d b"%(mem.used)
        print(outPut)
    def availableMemory():
        mem = psutil.virtual_memory()
        outPut = "The free memory space of the system remaining number is %d b"%(mem.free)
        print(outPut)
    def totalMemory():
        mem = psutil.virtual_memory()
        outPut = "The total amount of memory in the system is %d \n b"%(mem.total)
        print(outPut)

class filesCommands():
    path = "unknow"
    error = errors()
    def __init__(self):
        pass
    def fcopy(self,path,name):
        if(os.path.exists(path) == False):
            self.error.error6()
            return -2
        self.path = path
        fn = []
        fex = []
        fn,fex = self.fileNameSeparation()
        for i in range(len(fn)):
            if(operator.eq(fn[i],name)):
                if(fex[i] == ''):
                    newName = self.nameCpy(name)
                    self.dirCpy(name,newName)
                    return 1
                else:
                    newName = self.nameCpy(fn[i]) + fex[i]
                    name = name + fex[i]
                    self.fileCpy(name,newName)
                    return 1
        return -1
    def fileCpy(self,name,newName):
        os.chdir(self.path)
        os.rename(name,newName)
        shutil.copy(self.path + "\\" + newName,self.path + "\\" + name)
    def nameCpy(self,name):
        s = name
        while(True):
            i = 0
            while(i <= 5):
                if(s[len(s) - 1] == ')'):
                    try:
                        int(s[len(s) - 2]) + 1
                    except:
                        name = s + "(1)"
                        break
                    else:
                        while(i <= len(s)-2):
                            if(s[len(s) - i - 1] == '('):
                                nameCut = s.split(s[len(s) - i - 1])
                                num = s[len(s) - i - 1:len(s)]
                                num = num[1:len(num) - 1]
                                num = '(' + str(int(num) + 1) + ')'
                                name = nameCut[0] + num
                            i = i + 1
                        break
                else:
                    name = s + "(1)"
                i = i + 1
            break
        return name    
    def dirCpy(self,name,newName):
        newFilePath = self.path + "\\" + newName
        os.chdir(self.path)
        if(self.dirCreate(newName) == 0):
            return -1
        for root,dirs,files in os.walk(self.path + "\\" + name): 
            for all in files: 
                shutil.copy(os.path.join(root,all),newFilePath)
    def fileNameSeparation(self):
        names = os.listdir(self.path)
        fileName = []
        fileEx = []
        i = 0
        for i in range(len(names)):
            fn,fex = os.path.splitext(names[i])
            if(fn.find(".exe") != -1):
                nameCut = fn.split(".")
                fn = nameCut[0]
                fex = '.' + nameCut[1] + fex
            fileName.append(fn)
            fileEx.append(fex)
        return fileName,fileEx
    def fileRemove(self,path,name):
        self.path = path
        if(os.path.isdir(path + '\\' + name) == False):
            try:
                fn,fex = self.fileNameSeparation()
                os.remove(self.path + '\\' + fn + fex)
            except:
                self.error.error8()
        else:
            try:
                shutil.rmtree(path + '\\' + name)
            except:
                self.error.error7()
    def dirCreate(self,name):
        try:
            os.mkdir(self.path + '\\' + name)
        except:
            self.error.error10()
            return 0
        else:
            return 1

class fileRead():
    path = "unknow"
    error = errors()
    def __init__(self):
        pass
    def readCommand(self,path,name):
        self.path = path
        try:
            text = self.fileOpen(name)
        except:
            self.error.error7()
            return -1
        else:
            page = 0
            maxPage = -1
            while(True):
                order = input()
                os.system("cls")
                paging = 0
                pageInfo = "*******************页面%d*******************"%(page+1)
                if(order == 'b'):
                    if(page != -1):
                        page = page - 1
                        paging = 1
                    else:
                        os.system("cls")
                        print("没有上一页了")
                elif(order == ' '):
                    if(page != maxPage):
                        page = page + 1
                        paging = 1
                    else:
                        os.system("cls")
                        print("没有下一页了")
                if(paging == 1):
                    print(pageInfo)
                    if((page + 1) * 10 <= len(text) and (page + 2) * 10 >= len(text)):
                        for i in range((page + 1) * 10,len(text) - 1):
                            print(text[i])
                            maxPage = page
                    else:
                        for i in range((page + 1) * 10,(page + 2) * 10):
                            print(text[i])
                if(order == 'q' or order == "quit"):
                    return 1
    def fileOpen(self,name):
        path = self.path
        text = []
        for line in open(self.path + "\\" + name,"r"):
            text.append(line)
        return text
    def showAll(self,path,name):
        self.path = path
        try:
            text = self.fileOpen(name)
        except:
            self.error.error7()
            return -1
        else:
            os.system("cls")
            for i in range(len(text) - 1):
                print(text[i])
    def fileCount(self,name,model):
        try:
            text = self.fileOpen(name)
        except:
            self.error.error7()
            return ''
        else:
            max = -1
            characterCount = 0
            digit = 0
            cap = 0
            sma = 0
            for i in range(len(text) - 1):
                j = 0
                row = text[i]
                characterCount = characterCount + len(text[i])
                for j in range(len(row) - 1):
                    if (row[j].isdigit()):
                        digit = digit + 1
                    elif(row[j].isupper):
                        cap = cap + 1
                    elif(row[j].islower):
                        sma = sma + 1
                if(len(text[i]) >= max):
                    max = len(text[i])
            if(model == 0):
                return "The length of the longest row is:" + str(max)
            elif(model == 2):
                return "Total number of words is:" + str(digit + cap + sma)
            else:
                return "Total number of characters  is:" + str(characterCount)

class user():
    def __init__(self):
        pass
    def usernameGet(self):
        defaultUsername = "admin"
        username = defaultUsername
        username = getpass.getuser()
        return username
    def pathInit(self):
        initialPath = r"C:\Users\admin\Desktop"
        path = initialPath
        username = self.usernameGet()
        path = r"C:\Users\%s\Desktop"%(username)
        return path

class filesListCommands():
    path = "unknow"
    initialPath = "unknow"
    error = errors()
    def __init__(self):
        self.userName = user.usernameGet
        self.initialPath = r"C:\Users\%s\Desktop"%(self.userName)
        self.path = self.initialPath
    def filenameCheck(self,fileName):
        dirs = os.listdir(self.path)
        i = 0
        for i in range(len(dirs)):
            if(fileName == dirs[i]):
                return True
        return False
    def showFiles(self,latestPath):
        path = latestPath
        files = os.listdir(path)
        print("*"*77)
        print("*"*10 + "There are the following contents in the current directory" + "*"*10)
        for i in range(len(files)):
            print(files[i])
        print("*" * 77)
    def pathInto(self,fileName,path):
        self.path = path
        if(self.filenameCheck(fileName) == False):
            self.error.error4()
            return self.path
        self.path = path + "\\" + fileName
        return self.path
    def pathTurnback(self,path):
        i = len(path)
        while(True):
            if(path[i-1:i] == '\\'):
                path = path[0:i-1]
                break
            i = i - 1
            if(i == 0):
                self.error.error2()
                break
        self.path = path
        return path
    def diskSwitch(self,distnation):
        disks = psutil.disk_partitions()
        i = 0
        for i in range(len(disks)):
            disk = disks[i]
            diskSymbol = disk[1]
            if(diskSymbol.find(distnation) == 0):
                return distnation# + "\\"
        self.error.error1()    

class totalCommands():
    order = "wait"
    path = "unknow"
    error = errors()
    his = []
    def __init__(self,value):
        self.order = value
        self.path = user().pathInit()
        print(self.path + " ",end = '')
    def CommandsCheck(self,order):
        isRun = 0
        self.his.append(order)
        if((order.find(':') != -1) and isRun == 0):
            self.diskChange(order)
            isRun = 1
        if((order.find("cp") != -1 or order.find("CP") != -1) and isRun == 0):
            if(order.find("-m") != -1 or order.find("-M") != -1):
                if(order.find("-r") != -1 or order.find("-R") != -1):
                    isRemove = True
                    orderCut = order.split(" ")
                    self.cpMove(orderCut[3],orderCut[4],isRemove)
                else:
                    isRemove = False
                    orderCut = order.split(" ")
                    self.cpMove(orderCut[2],orderCut[3],isRemove)
            else:
                orderCut = order.split(" ")
                self.cp(orderCut[1])
            isRun = 1
        if((order.find("cd") != -1 or order.find("CD") != -1) and isRun == 0):
            if(order.find(" ") == -1):
                self.error.error3()
                print(self.path + " ",end = '')
                return -1
            orderCut = order.split(" ")
            destination = orderCut[1]
            self.cd(destination)
            isRun = 1
        if((order.find("more") != -1) and isRun == 0):
            orderCut = order.split(" ")
            self.more(orderCut[1])
            isRun = 1
        if((order.find("show") != -1) and isRun == 0):
            orderCut = order.split(" ")
            self.show(orderCut[1])
            isRun = 1
        if((order.find("mkdir") != -1) and isRun == 0):
            orderCut = order.split(" ")
            self.mkdir(orderCut[1])
            isRun = 1
        if((order.find("rmdir") != -1) and isRun == 0):
            orderCut = order.split(" ")
            self.rmdir(orderCut[1])
            isRun = 1
        if(order == "pwd" and isRun == 0):
            self.pwd()
            isRun = 1
        if(order == "clear"):
            os.system("cls")
        if((order.find("pid") != -1) and isRun == 0):
            self.pid(order)
            isRun = 1
        if((order == "mem" or order == "m" or order == "M") and isRun == 0):
            self.mem()
            isRun = 1
        if((order.find ("ls") != -1 or order.find ("LS") != -1) and isRun == 0):
            if(operator.eq('ls',order)):
                self.ls()
            else:
                self.error.error3()
            isRun = 1
        if((order.find("chmod") != -1) and isRun == 0):
            self.Chmod(order)
            isRun = 1
        if((order.find("wc") != -1 or order.find("WC") != -1) and isRun == 0):
            self.wc(order)
            isRun = 1
        if((order.find("echo") != -1) and isRun == 0):
            self.echo(order)
            isRun = 1
        if((order.find("date") != -1) and isRun == 0):
            self.date(order)
            isRun = 1
        if((order.find("history") != -1) and isRun == 0):
            self.history(order)
            isRun = 1
        if((order.find("help") != -1) and isRun == 0):
            self.Help()
            isRun = 1
        print(self.path + " ",end = '')
    def mem(self):
        memoryCommands.totalMemory()
        memoryCommands.usingMemory()
        memoryCommands.availableMemory()
    def ls(self):
        print("Current path:"+self.path)
        show = filesListCommands()
        show.showFiles(self.path)
    def cd(self,destination):
        fileOperation = filesListCommands()
        if(destination == ".." or destination == "."):
            self.path = fileOperation.pathTurnback(self.path)
        else:
            self.path = fileOperation.pathInto(destination,self.path)
    def cp(self,name):
        fcp = filesCommands()
        if(fcp.fcopy(self.path,name) == -1):
            self.error.error4()
    def mkdir(self,name):
        md = filesCommands()
        md.path = self.path
        md.dirCreate(name)
    def rmdir(self,name):
        rm = filesCommands()
        rm.fileRemove(self.path,name)
    def pid(self,order):
        id = screen()
        if(order == "pid"):
            id.pidPut("all")
        else:
            orderCut = order.split(" ")
            id.pidPut(orderCut[1])
    def show(self,name):
        sho = fileRead()
        sho.showAll(self.path,name)
    def cpMove(self,name,path,isRemove):
        fcp = filesCommands()
        if(fcp.fcopy(path,name) == -1):
            self.error.error4()
        if(isRemove == True):
            fcp.fileRemove(path,name)
    def diskChange(self,destination):
        diskChoose = filesListCommands()
        self.path = diskChoose.diskSwitch(destination)
    def more(self,name):
        sho = fileRead()
        sho.readCommand(self.path,name)
    def history(self,order):
        print("the order you've input:")
        if(order == "history"):
            for i in range(len(self.his) - 1):
                print(str(i) + ": " + self.his[i])
        else:
            orderCut = order.split(" ")
            if(int(orderCut[1]) >= len(self.his)):
                n = 0
            else:
                n = int(orderCut[1])
            for i in range(n,len(self.his) - 1):
                print(str(i) + ": " + self.his[i])
    def Chmod(self,order):
        orderCut = order.split(" ")
        pw = powerSet()
        pw.path = self.path
        if(orderCut[1].find("u") != -1):
            pw.userRWSet(orderCut[1],orderCut[2])
        elif(orderCut[1].find("g") != -1):
            pw.groupRWSet(orderCut[1],orderCut[2])
        else:
            pw.readOnlySet(orderCut[1],orderCut[2])
    def pwd(self):
        print("Current directory is:" + self.path)
    def wc(self,name):
        orderCut = name.split(" ")
        fname = orderCut[len(orderCut) - 1]
        fr = fileRead()
        fr.path = self.path
        print("*"*40)
        print("filename:" + fname)
        for i in range(1,len(orderCut) - 1):
            if(orderCut[i] == "-c"):
                print("file size:" + str(os.path.getsize(self.path + '\\' + fname)) + "byte")
            if(orderCut[i] == "-l"):
                print("row count:" + str(len(fr.fileOpen(fname))))
            if(orderCut[i] == "-m"):
                print(fr.fileCount(fname,1))
            if(orderCut[i] == "-w"):
                print(fr.fileCount(fname,2))
            if(orderCut[i] == "-L"):
                print(fr.fileCount(fname,0))
        print("*"*40)
    def echo(self,order):
        oredrCut = order.split(" ")
        text = ""
        for i in range(1,len(oredrCut)):
            text = text + ' ' + oredrCut[i]
        printf = screen()
        printf.msgPut(text)
    def date(self,order):
        t = dateCommmand()
        orderCut = order.split(" ")
        for i in range(1,len(orderCut)):
            if(orderCut[i] == "-t"):
                t.whatTime()
            if(orderCut[i] == "-r"):
                t.runningTime()
            if(orderCut[i] == "-y"):
                t.kalendor("y",orderCut[len(orderCut) - 1])
            if(orderCut[i] == "-m"):
                t.kalendor("m",orderCut[len(orderCut) - 1])
            if(orderCut[i] == "-q"):
                t.kalendor("q",orderCut[len(orderCut) - 1])
            if(orderCut[i] == "-c"):
                t.kalendor("c",orderCut[len(orderCut) - 1])
    def Help(self):
        hel = shellHelp
        hel.Help()

def __main__():
    #aaa()

    order = "wait"
    path = "unknow"
    com = totalCommands(order)
    while(True):
        order = input()
        if(order == "quit" or order == "q" or order == "Q"):
            break
        com.CommandsCheck(order)
        order = "wait"

__main__()