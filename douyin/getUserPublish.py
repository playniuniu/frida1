import time

import frida
import sys
import os

if __name__ == '__main__':
    src = """
    
    
        Java.perform(function(){
            
            var String_class = Java.use("java.lang.String");
		
            var f7757b;
            Java.use("com.ss.android.ugc.aweme.app.b.b").$init.overload('com.ss.android.ugc.aweme.app.AwemeApplication').implementation = function (awemeApplication) {
                f7757b = awemeApplication;
                this.$init(awemeApplication);
            }
            
            var mContext;
            Java.use("com.ss.android.common.applog.GlobalContext").setContext.implementation = function (context) {
                mContext = context;
                console.log("-----------mContext---------------", mContext);
                this.setContext(context);
            }
            
            Java.use("com.ss.android.common.applog.UserInfo").getUserInfo.overload('int', 'java.lang.String', '[Ljava.lang.String;', 'java.lang.String').implementation=function(a, b, c, d){
                var str2 = this.getUserInfo(a, b, c, d);
                if (b.indexOf('/v1/aweme/post') != -1) {
                    var ll = str2.length;
                    var i5 = ll >> 1;
                    var substring = str2.substring(0, i5);
                    
                    var getUserInfo = Java.use("com.ss.android.common.applog.UserInfo").getUserInfo.overload('int', 'java.lang.String', '[Ljava.lang.String;', 'java.lang.String');
                    
                    var class_B = Java.use("com.ss.sys.ces.b");
                    
                    var GlobalContext = Java.use("com.ss.android.common.applog.GlobalContext");
                    
                    
                    var sessionId = Java.use("com.ss.android.ugc.aweme.app.b.e");
                    var sdk = class_B.D(mContext, 1128, 255)
                    sdk.SetRegionType(0);
                    sdk.setSession(sessionId.a());
                    var j = Java.use("com.ss.android.common.applog.j");
                    substring = String_class.$new(substring);
                    var b2 = j.b(sdk.encode(substring.getBytes()));
                    var StringBuilder = Java.use("java.lang.StringBuilder");
                    var sb2 = StringBuilder.$new(b);
                    var sb3 = StringBuilder.$new();
                    var sb5 = StringBuilder.$new();
                    sb3.append(sb2);
                    sb3.append("&as=");
                    sb3.append(substring);
                    sb3.append("&cp=");
                    sb3.append(str2.substring(i5, ll));
                    var sb4 = sb3.toString();
                    sb5.append(sb4);
                    sb5.append("&mas=");
                    sb5.append(b2);
                    var a2 = sb5.toString();
                    console.log("--------------->" + a2);
                    //send(a2);
                }
                return str2;
            };

        });
        """


    def on_message(message, data):
        print(message)
        url = message['payload']
        print(url)


    # 启动
    # os.system('adb shell am force-stop com.ss.android.ugc.aweme')
    # os.system('adb shell am start -n com.ss.android.ugc.aweme/com.ss.android.ugc.aweme.splash.SplashActivity')
    # while True:
    #     try:    #
    #         session = frida.get_remote_device().attach("com.ss.android.ugc.aweme")
    #         break
    #     except Exception as e:
    #         continue
    device = frida.get_usb_device()
    pid = device.spawn(["com.ss.android.ugc.aweme"])
    session = device.attach(pid)
    script = session.create_script(src)
    script.on("message", on_message)
    script.load()
    device.resume(pid)
    print(' Start attach')
    sys.stdin.read()
