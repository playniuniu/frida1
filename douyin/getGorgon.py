
import frida
import sys

if __name__ == '__main__':
    src = """

        Java.perform(function(){
            
            var tt = Java.use("com.ss.sys.ces.gg.tt$1").a.implementation = function(p1, p2) {
                var res = this.a(p1,p2);
                if (p1.indexOf('/v1/aweme/post') != -1) {
                    console.log("p1", p1);
                    console.log("p2", p2);
                    console.log("--------->" + res);
                }
                return res;
            }
        });
        """


    def on_message(message, data):
        print(message)
        url = message['payload']
        print(url)

    device = frida.get_usb_device()
    pid = device.spawn(["com.ss.android.ugc.aweme"])
    session = device.attach(pid)
    script = session.create_script(src)
    script.on("message", on_message)
    script.load()
    device.resume(pid)
    print(' Start attach')
    sys.stdin.read()
