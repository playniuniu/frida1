import frida
import sys

if __name__ == '__main__':
    src = """

        Java.perform(function(){
        
            Java.use("com.ss.android.common.util.NetworkUtils").executeGetRetry$___twin___.implementation=function(p1, p2, p3, p4, p5, p6, p7, p8, p9) {
                var res = this.executeGetRetry$___twin___(p1, p2, p3, p4, p5, p6, p7, p8, p9);
                if (p3.indexOf('/v1/aweme/post') != -1) {
                    console.log("request -> ", p1, p2, p3, p4, p5, p6, p7, p8, p9);
                    
                    var serverTime = new Date().getTime();
                    str2 = UserInfo.getUserInfo(serverTime, p3, Java.array(), '');
                    
                    console.log("getUserInfo", str2);
                    var res = this.executeGetRetry$___twin___(p1, p2, p3, p4, p5, p6, p7, p8, p9);
                }
                return res;
		    };
		    
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
