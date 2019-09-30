import frida
import sys

if __name__ == '__main__':



    src = """
    Java.perform(function(){
            
        Java.use("com.ss.android.ugc.aweme.app.a.a").a.overload('int', 'java.lang.String', 'java.lang.Class', 'java.lang.String', 'com.ss.android.c.a.b.f').implementation=function(a, b, c, d, e){
            send(a + "----" + b + "----" + c + "----" + d + "----" + e)
        };
    });
    """

    def on_message(message, data):
        print(message)

    session = frida.get_remote_device().attach("com.ss.android.ugc.aweme")
    script = session.create_script(src)
    script.on("message", on_message)
    print(' Start attach')
    script.load()
    sys.stdin.read()