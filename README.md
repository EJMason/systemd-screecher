# systemd-screecher

This is a super basic C++ plugin for node that will notify systemd that your backend node server has started up.

### Requirements

- Linux distribution that supports **systemd**

- Node >= 8.0.0

- The ability to build c++ during your install step

### Setting up your server

##### C++ build tools (CentoOS 7)

`sudo yum install gcc-c++`

note: probably not the best idea to add c++ compilers to your server so put this in your CI build pipeline

##### Systemd development files (CentOS 7)

`sudo yum install systemd-devel`

##### Tips and Tricks

- This package will attempt to build the c++ when performing npm install. It will only build in a linux environment.

- To ensure this package doesn't fail your `npm install` you can add systemd-screecher as an optional dependency.

- Make sure to change your systemd service file to "Notify" mode. Example:

```
[Service]
Environment="NODE_ENV=production"
Type=notify
ExecStart=/usr/sbin/simple-notifying-service
TimeoutStartSec=30
Restart=always
```

### Installation (Once the other steps have been fufilled)

`npm i systemd-screecher`

### Usage

```javascript
const express = require("express");
const app = express();

const notify = require("systemd-screecher");

app.get("/", (req, res) => res.send("Hello World!"));

app.listen(3000, () => {
  console.log("App is listening on port " + port);

  // once the app has finished bootstrapping...

  notify();
});
```
