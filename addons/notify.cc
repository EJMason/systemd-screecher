
#include <systemd/sd-daemon.h>
#include <unistd.h>
#include <nan.h>
using namespace v8;

NAN_METHOD(sysnotify) {

    sd_notifyf(0, "READY=1\n"
    "STATUS=NEST_READY\n"
    "MAINPID=%lu",
    (unsigned long) getpid());
}

NAN_MODULE_INIT(init) {
    Nan::SetMethod(target, "sysnotify", sysnotify);
}

NODE_MODULE(sysnotify, init);