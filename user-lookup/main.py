import os, random, time, subprocess, threading, signal, random, string, uuid
clear = lambda: subprocess.call('cls||clear', shell=True)
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
colorama.init()
class THRIDING():
    def __init__(self, target):
        self.threads_list = []
        self.target = target
    
    def gen(self, threads):
        t = threading.Thread(target=x.counter)
        t.setDaemon(True)
        self.threads_list.append(t)
        for i in range(threads):
            t = threading.Thread(target=self.target)
            t.setDaemon(True)
            self.threads_list.append(t)
        return self.threads_list

    def start(self):
        for thread_start in self.threads_list:
            thread_start.start()

    def join(self):
        for thread_join in self.threads_list:
            thread_join.join()
class DESIGN():
    WHITE = '\x1b[1;37;40m'
    YELLOW = '\x1b[1;33;40m'
    RED = '\x1b[1;31;40m'
    BLUE = '\x1b[36m\x1b[40m'
    GREEN = '\x1b[32m\x1b[40m'
    greenplus = f"{WHITE}[ {GREEN}+{WHITE} ]"
    blueplus = f"{WHITE}[ {BLUE}+{WHITE} ]"
    redminus = f"{WHITE}[ {RED}-{WHITE} ]"
    bluelist = f"{WHITE}[ {BLUE}LIST {WHITE}]"
    redlist = f"{WHITE}[ {RED}LIST {WHITE}]"
    blueproxies = f"{WHITE}[ {BLUE}PROXIES {WHITE}]"
    redproxies = f"{WHITE}[ {RED}PROXIES {WHITE}]"
    bluezero = f"{WHITE}[ {BLUE}0 {WHITE}]"
    blueone = f"{WHITE}[ {BLUE}1 {WHITE}]"
    bluetwo = f"{WHITE}[ {BLUE}2 {WHITE}]"
    xrblue = f"\n{blueplus} User Lookup {BLUE}/ {WHITE}Instagram{BLUE}: {WHITE}@xnce {BLUE}/ {WHITE}@ro1c"
users = []
proxies = []
class FILES():
    def __init__(self, bluefile, redfile, my_list):
        self.select_file(f"\n{bluefile} Enter To Select File: ")
        self.open_file(my_list, bluefile, redfile)
    def select_file(self, text):
        print(text, end="")
        input()
        root = Tk()
        root.title(".txt")
        self.path = filedialog.askopenfilename(initialdir="", title="Select A File", filetypes=(("txt document","*.txt"),("All Files", "*.*")))
        root.destroy()
        root.mainloop()
    def open_file(self, my_list, bluefile, redfile):
        filename = self.path.split("/")[-1]
        if self.path[-4:]!=".txt":
            print(f"\n{redfile} Please Select (.txt) File ", end="")
            input()
            exit()
        try:
            for x in open(self.path, "r").read().split("\n"):
                if x!="" and x not in my_list:
                    my_list.append(x)
            print(f"\n{bluefile} Successfully Load {DESIGN.BLUE}{filename}")
            time.sleep(2)
        except Exception as err:
            print(f"\n{redfile} {err} ", end="")
            input()
            exit()
class FILES2():
    def __init__(self, filename, my_list):
        self.open_file(filename, my_list)
    def open_file(self, filename, my_list):
        try:
            file = open(f"{filename}.txt", "r").read().split("\n")
            for x in file:
                if x!="" and x not in my_list:
                    my_list.append(x)
            print(f"\n{DESIGN.blueplus} Successfully Load {DESIGN.BLUE}{filename}.txt")
            time.sleep(2)
        except:
            print(f"\n{DESIGN.redminus} {DESIGN.RED}{filename} {DESIGN.WHITE}is missing ", end="")
            input()
            exit()
class Xnce():
    def __init__(self):
        self.good, self.bad, self.error, self.turn, self.run = 0, 0, 0, 0, True
        print(f"\n{DESIGN.bluezero} HTTP/S {DESIGN.blueone} SOCKS4 {DESIGN.bluetwo} SOCKS5: ", end="")
        self.proxies_type = input()
        if not any(self.proxies_type==x for x in ["0", "1", "2"]):
            print(f'\n{DESIGN.redminus} ["0", "1", "2"]')
            self.inex()
    def inex(self, text):
        self.run = False
        print(f"\n{DESIGN.redminus} {DESIGN.WHITE}run = {DESIGN.RED}False {DESIGN.WHITE}, {text}")
        print(f"\n{DESIGN.redminus} Enter To Exit: ", end="")
        input()
        os.kill(os.getpid(), signal.SIGTERM)
    def remove_user(self, username):
        users.remove(username)
        if len(users) < 1:
            self.inex("No Users")
    def save_user(self, filename, username):
        with open(f"{filename}.txt", "a") as file:
            file.write(f"\n{username}")
            file.close()
    def random_proxy(self):
        prox = random.choice(proxies)
        if self.proxies_type=="0":
            proxy = {"http": prox, "https": prox}
        elif self.proxies_type=="1":
            proxy = {"http": f"socks4://{prox}", "https": f"socks4://{prox}"}
        elif self.proxies_type=="2":
            proxy = {"http": f"socks5://{prox}", "https": f"socks5://{prox}"}
        return proxy
    def check(self, username):
        head = {"user-agent": f"Instagram 150.0.0.0.000 Android"}
        data = {
            "phone_id": uuid.uuid4(),
            "guid": uuid.uuid4(),
            "q": "",
            "device_id": uuid.uuid4(),
            "android_build_type":"release",
            "waterfall_id": uuid.uuid4(),
            "directly_sign_in":"true",
            "is_wa_installed":"false"
        }
        if ":" in username:
            data.update({"q": username.split(":")[0]})
            combo = True
        else:
            data.update({"q": username})
            combo = False
        req = requests.post("https://i.instagram.com/api/v1/users/lookup/", headers=head, data=data, proxies=self.random_proxy())
        #print(req.text, req.status_code)
        if "email_sent" in req.text:
            self.remove_user(username)
            if combo:
                self.save_user("good-combo", username)
            else:
                self.save_user("good", username)
            self.good += 1
        elif "No users found" in req.text:
            self.remove_user(username)
            self.bad += 1
        elif req.status_code==429:
            self.error += 1
        elif "html" in req.text.lower() or req.text=="":
            pass
        else:
            print(f"\n{DESIGN.redminus} {req.text}, {req.status_code}")
    def counter(self):
        while self.run:
            before = self.good + self.bad
            time.sleep(1)
            after = self.good + self.bad
            os.system(f"title Good: {self.good} / Bad: {self.bad} / Error: {self.error} / R/s: {after-before}")
    def main(self):
        while self.run:
            try:
                username = users[self.turn]
            except:
                self.turn = 0
                try:
                    username = users[self.turn]
                except:
                    pass
            self.turn += 1
            try:
                self.check(username)
            except Exception as err:
                pass
try:
    from tkinter import *
    from tkinter import filedialog
    FILES(DESIGN.bluelist, DESIGN.redlist, users)
    FILES(DESIGN.blueproxies, DESIGN.redproxies, proxies)
except:
    FILES2("list", users)
    FILES2("proxies", proxies)
clear()
print(DESIGN.xrblue)
x = Xnce()
print(f"\n{DESIGN.blueplus} Threads: ", end="")
threads = int(input())
print(f"\n{DESIGN.blueplus} Enter To Start: ", end="")
input()
t = THRIDING(x.main)
t.gen(threads)
t.start()
t.join()