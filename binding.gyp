{
  "targets": [
    {
      "target_name": "notify",
      "sources": [ "addons/notify.cc" ],
      "libraries": [
        "-lsystemd"
      ],
      "include_dirs": ["<!(node -e \"require('nan')\")"]
    }
  ]
}