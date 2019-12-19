import frida
import sys

if __name__ == '__main__':



    src = """
    Java.perform(function(){
    
        Java.use("com.fuluoge.motorfans.security.Security").getSecret.implementation=function(){
            send("shit:" + this.getSecret());
            return this.getSecret();
        };
        
        Java.use("com.fuluoge.motorfans.util.c").a.implementation=function(str){
            send("fuck:" + this.a(str));
            return this.a(str);
        };
        
    });
    """

    def on_message(message, data):
        print(message)
        print(data)

    session = frida.get_remote_device().attach("com.fuluoge.motorfans")
    script = session.create_script(src)
    script.on("message", on_message)
    print(' Start attach')
    script.load()
    sys.stdin.read()