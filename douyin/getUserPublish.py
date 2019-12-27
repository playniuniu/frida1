import time

import frida
import sys
import os
import requests

if __name__ == '__main__':
    src = """
    
        Java.perform(function(){
            
            var String_class = Java.use("java.lang.String");
            var HashMap = Java.use("java.util.LinkedHashMap");
            var ArrayList = Java.use("java.util.LinkedList");
		
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
            
            Java.use("com.ss.sys.ces.gg.tt$1").a.implementation = function(p1, p2) {
                var res = this.a(p1,p2);
                if (p1.indexOf('/v1/aweme/post') != -1) {
                    console.log("p1", p1);
                    console.log("p2", p2);
                    console.log("--------->" + res);
                }
                return res;
            }
            
            
            Java.use("com.ss.android.common.applog.UserInfo").getUserInfo.overload('int', 'java.lang.String', '[Ljava.lang.String;', 'java.lang.String').implementation=function(a, b, c, d){
                console.log(a, b, c, d);
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
                    var user_post_url = sb5.toString();
                    console.log("--------------->" + user_post_url);
                    
                    var header = HashMap.$new();
                    var x_ss_tc = ArrayList.$new();
                    x_ss_tc.add("0");
                    var cookie = ArrayList.$new();
                    cookie.add("odin_tt=840fdb02d02dcea77ba2992a54e0720bb1c0b608126e442c3fa46b625f3711bc267212fe3e5fc49dbad39e4c65ebba153b4f1a9e60a4b0d7392cb86b78179456; qh[360]=1; install_id=96960461524; ttreq=1$641e5aed6cc4f663077637e33e984a66ef9a7359");
                    var user_agent = ArrayList.$new();
                    user_agent.add("com.ss.android.ugc.aweme/900 (Linux; U; Android 6.0.1; zh_CN; Nexus 5; Build/M4B30Z; Cronet/58.0.2991.0)");
                    var accept_encoding = ArrayList.$new();
                    accept_encoding.add("gzip");
                    
                    header.put("x-ss-tc", x_ss_tc);
                    header.put("user-agent", user_agent);
                    header.put("cookie", cookie);
                    header.put("accept-encoding", accept_encoding);
                    
                    var tt = Java.use("com.ss.sys.ces.gg.tt$1").$new();
                    var user_post_map = tt.a(user_post_url, header);
                    Java.cast(user_post_map, Java.use("java.util.Map"));
                    var Gorgon = user_post_map.get("X-Gorgon").toString();
                    var Khronos = user_post_map.get("X-Khronos").toString();
                    console.log("==========>", Gorgon, Khronos);
                    var shit = {
                        "user_post_url": user_post_url,
                        "X-Gorgon": Gorgon,
                        "X-Khronos": Khronos,
                    }
                    send(shit);
                }
                return str2;
            };
            
        });
        """


    def on_message(message, data):
        msg = message['payload']
        post_url = msg['user_post_url']
        gorgon = msg['X-Gorgon']
        khronos = msg['X-Khronos']

        response = requests.get(
            url=post_url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
                'Cookie': 'odin_tt=840fdb02d02dcea77ba2992a54e0720bb1c0b608126e442c3fa46b625f3711bc267212fe3e5fc49dbad39e4c65ebba153b4f1a9e60a4b0d7392cb86b78179456; qh[360]=1; install_id=96960461524; ttreq=1$641e5aed6cc4f663077637e33e984a66ef9a7359',
                'X-Gorgon': gorgon,
                'X-Khronos': khronos,
                'X-SS-TC': '0',
            })
        print(response.text)
        print("gorgon:" + gorgon + " khronos" + khronos)

    device = frida.get_usb_device()
    pid = device.spawn(["com.ss.android.ugc.aweme"])
    session = device.attach(pid)
    script = session.create_script(src)
    script.on("message", on_message)
    script.load()
    device.resume(pid)
    print(' Start attach')
    sys.stdin.read()
