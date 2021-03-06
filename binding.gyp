{
  'variables': {
    'platform': '<(OS)',
  },
  "targets":
  [
    {
      "target_name": "zookeeper",
      'dependencies': ['libzk'],
      "sources": [ "src/node-zk.cpp" ],
      'cflags': ['-Wall', '-Werror', '-O0'],
      'conditions': [
        ['OS=="solaris"', {
          'cflags': ['-Wno-strict-aliasing'],
          'defines': ['_POSIX_PTHREAD_SEMANTICS'],
          'include_dirs': ['/opt/local/include/zookeeper'],
	  'ldflags': ['-lzookeeper_mt'],
        }],['OS=="mac"',{
	  'include_dirs': ['<(module_root_dir)/build/zk/include/zookeeper'],
          'libraries': [
          	'<(module_root_dir)/build/zk/lib/libzookeeper_st.a',
          	'<(module_root_dir)/build/zk/lib/libzookeeper_mt.a'
          ],
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'MACOSX_DEPLOYMENT_TARGET': '10.5'
          }
        }],['OS=="linux"',{
          'include_dirs': ['<(module_root_dir)/build/zk/include/zookeeper'],
          'libraries': [
          	'<(module_root_dir)/build/zk/lib/libzookeeper_st.a',
          	'<(module_root_dir)/build/zk/lib/libzookeeper_mt.a'
          ],
        }]
      ]
    },
    {
      'target_name': 'libzk',
      'type': 'none',
      'actions': [{
        'action_name': 'build_zk_client_lib',
        'inputs': [''],
        'outputs': [''],
        'action': ['sh', 'libzk-build.sh']
      }]
    }
  ],
}
