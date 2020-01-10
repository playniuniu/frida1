import time

import frida
import sys
import os

if __name__ == '__main__':
    src = """
        Java.perform(function(){
            var HashMap = Java.use("java.util.HashMap");
            Java.use("com.ss.android.common.applog.c").S.implementation = function (p1) {
                this.S(p1);
                Java.cast(p1, HashMap);
                p1.put("openudid", "9774d56d682e549c");
                console.log("req", p1);
                return;
            }

        });
        """

    #70342278382
    def on_message(message, data):
        print(message)
        url = message['payload']
        print(url)

    device = frida.get_remote_device()
    pid = device.spawn(["com.ss.android.ugc.aweme"])
    session = device.attach(pid)
    script = session.create_script(src)
    script.on("message", on_message)
    script.load()
    device.resume(pid)
    print(' Start attach')
    sys.stdin.read()
