{
  'targets': [
    {
      'target_name': 'chromiumcontent_all',
      'type': 'none',
      'dependencies': [
        'chromiumcontent',
        '<(DEPTH)/chrome/chrome.gyp:chromedriver',
      ],
      'conditions': [
        ['OS=="linux"', {
          'dependencies': [
            'chromiumviews',
            '<(DEPTH)/build/linux/system.gyp:libspeechd',
            '<(DEPTH)/third_party/mesa/mesa.gyp:osmesa',
          ],
        }],
        ['OS=="win"', {
          'dependencies': [
            'chromiumviews',
          ],
        }],
      ],
    },
    {
      'target_name': 'chromiumcontent',
      # Build chromiumcontent as shared_library otherwise some static libraries
      # will not build.
      'type': 'shared_library',
      'dependencies': [
        'libchromiumcontent_pak',
        '<(DEPTH)/base/base.gyp:base_prefs',
        '<(DEPTH)/components/components.gyp:devtools_discovery',
        '<(DEPTH)/components/components.gyp:devtools_http_handler',
        '<(DEPTH)/content/content.gyp:content',
        '<(DEPTH)/content/content.gyp:content_app_both',
        '<(DEPTH)/content/content_shell_and_tests.gyp:content_shell_pak',
        '<(DEPTH)/net/net.gyp:net_with_v8',
        '<(DEPTH)/ppapi/ppapi_internal.gyp:ppapi_host',
        '<(DEPTH)/ppapi/ppapi_internal.gyp:ppapi_proxy',
        '<(DEPTH)/ppapi/ppapi_internal.gyp:ppapi_ipc',
        '<(DEPTH)/ppapi/ppapi_internal.gyp:ppapi_shared',
        '<(DEPTH)/third_party/google_toolbox_for_mac/google_toolbox_for_mac.gyp:google_toolbox_for_mac',
        '<(DEPTH)/third_party/libyuv/libyuv.gyp:libyuv',
        '<(DEPTH)/third_party/webrtc/modules/modules.gyp:desktop_capture',
      ],
      'sources': [
        'empty.cc',
      ],
      'conditions': [
        ['OS=="win"', {
          'dependencies': [
            '<(DEPTH)/pdf/pdf.gyp:pdf',
          ],
        }],
      ],
    },
    {
      'target_name': 'libchromiumcontent_pak',
      'type': 'none',
      'dependencies': [
        '<(DEPTH)/chrome/chrome_resources.gyp:chrome_strings_map',
        '<(DEPTH)/content/content_shell_and_tests.gyp:content_shell_pak',
      ],
      'actions': [
        {
          'action_name': 'repack_content_shell_pack',
          'variables': {
            'pak_inputs': [
              '<(SHARED_INTERMEDIATE_DIR)/chrome/generated_resources_en-US.pak',
              '<(PRODUCT_DIR)/content_shell.pak',
            ],
            'pak_output': '<(PRODUCT_DIR)/libchromiumcontent.pak',
          },
          'includes': [ '../build/repack_action.gypi' ],
        },
      ],
    },
  ],
  'conditions': [
    ['OS in ["win", "linux"]', {
      'targets': [
        {
          'target_name': 'chromiumviews',
          'type': 'none',
          'dependencies': [
            '<(DEPTH)/ui/content_accelerators/ui_content_accelerators.gyp:ui_content_accelerators',
            '<(DEPTH)/ui/display/display.gyp:display',
            '<(DEPTH)/ui/display/display.gyp:display_util',
            '<(DEPTH)/ui/views/controls/webview/webview.gyp:webview',
            '<(DEPTH)/ui/views/views.gyp:views',
            '<(DEPTH)/ui/wm/wm.gyp:wm',
          ],
          'conditions': [
            ['OS=="linux"', {
              'dependencies': [
                '<(DEPTH)/chrome/browser/ui/libgtk2ui/libgtk2ui.gyp:gtk2ui',
              ],
            }],  # OS=="linux"
          ],
        },
      ],
    }],
  ],
}
