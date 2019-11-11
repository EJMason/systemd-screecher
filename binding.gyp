{
  "targets": [
    {
      "target_name": "notify",
      "sources": [ "addons/notify.cc" ],
      "libraries": [
        "-lsystemd"
      ],
      "include_dirs": ["<!(node -e \"require('nan')\")"],
      'conditions': [
        ['OS!="linux"',
          {
            'sources/': [['exclude', 'addons/notify.cc$']],
            'libraries/': [['exclude', '-lsystemd$']],
          }
        ],
    }
  ]
}