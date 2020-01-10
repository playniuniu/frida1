import time

import frida
import sys
import os
import requests
import threading

if __name__ == '__main__':

    def hello_for():
        while True:
            url = "https://aweme.snssdk.com/aweme/v1/aweme/post/?user_id=64269185197&max_cursor=0&count=20&retry_type=no_retry&iid=96960461524&device_id=70015318587&ac=wifi&channel=gdt_growth1_cp1&aid=1128&app_name=aweme&version_code=180&version_name=1.8.0&device_platform=android&ssmix=a&device_type=Nexus+5&device_brand=google&language=zh&os_api=23&os_version=6.0.1&uuid=359250052518709&openudid=86eee3dabb685bc6&manifest_version_code=180&resolution=1080*1776&dpi=480&update_version_code=1800&_rticket=1578063545578&ts=1578063545"
            msg = script.exports.hoho(url)
            print("fuck:" + str(msg))
            time.sleep(5)
            if msg is None:
                continue
            post_url = msg['user_post_url']
            gorgon = msg['X-Gorgon']
            khronos = msg['X-Khronos']

            response = requests.get(
                url=post_url,
                headers={
                    'User-Agent': 'com.ss.android.ugc.aweme/900 (Linux; U; Android 6.0.1; zh_CN; Nexus 5; Build/MOB31E; Cronet/58.0.2991.0)',
                    'X-Gorgon': gorgon,
                    'X-Khronos': khronos,
                    'X-SS-TC': '0'
                })
            print(response.text)

    src = """
        rpc.exports = {

            hoho: function(b) {
                var shit;
                var systemTime = parseInt(new Date().getTime() / 1000);
                Java.perform(function() {
                    try {
                        var UserInfo = Java.use("com.ss.android.common.applog.UserInfo");;
                        var String = Java.use("java.lang.String");
                        var substring = b.substring(b.lastIndexOf("?") + 1);
                        var param_c = "";
                        var arr1 = substring.split("&");
                        for(var i = 0; i < arr1.length; i++) {
                            var s = arr1[i].replace("=", ",");
                            param_c = param_c + s + ",";
                        }
                        param_c = param_c.substring(0, param_c.length - 1);
                        var fffff = param_c.split(",");
                        var str2 = UserInfo.getUserInfo.overload('int', 'java.lang.String', '[Ljava.lang.String;', 'java.lang.String')
                            .call(UserInfo, 1578328824, b, fffff, "70015318587");
                        var ll = str2.length;
                        var i5 = ll >> 1;
                        var substring = str2.substring(0, i5);


                        var substring = str2.substring(0, i5);
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

                        var header = HashMap.$new();
                        var x_ss_tc = ArrayList.$new();
                        x_ss_tc.add("0");
                        var cookie = ArrayList.$new();
                        cookie.add("install_id=96960461524; ttreq=1$641e5aed6cc4f663077637e33e984a66ef9a7359; qh[360]=1; odin_tt=5d1ec749cd9a7aa91443937b2036eae2d9118412e524eabab992306c23f05a46df84bfcbc2a13bb24b99c0515bbac86cf9b9566d37d3ba7df60e3469ed1106a1");
                        var user_agent = ArrayList.$new();
                        user_agent.add("com.ss.android.ugc.aweme/900 (Linux; U; Android 6.0.1; zh_CN; Nexus 5; Build/MOB31E; Cronet/58.0.2991.0)");
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

                        shit = {
                            "user_post_url": user_post_url,
                            "X-Gorgon": Gorgon,
                            "X-Khronos": Khronos
                        }
                    } catch (error) {
                        console.log("error", error);
                    }
                })
                return shit;
            }

        }

        var String_class;
        var HashMap;
        var ArrayList;
        var mContext;

        Java.perform(function(){

            String_class = Java.use("java.lang.String");
            HashMap = Java.use("java.util.LinkedHashMap");
            ArrayList = Java.use("java.util.LinkedList");

            Java.use("com.ss.android.common.applog.GlobalContext").setContext.implementation = function (context) {
                mContext = context;
                console.log("-----------mContext---------------", mContext);
                this.setContext(context);
            }
            
        });

        """

    device = frida.get_remote_device()
    pid = device.spawn(["com.ss.android.ugc.aweme"])
    session = device.attach(pid)
    script = session.create_script(src)
    script.load()
    device.resume(pid)
    print(' Start attach')
    threading.Thread(target=hello_for).start()
    sys.stdin.read()