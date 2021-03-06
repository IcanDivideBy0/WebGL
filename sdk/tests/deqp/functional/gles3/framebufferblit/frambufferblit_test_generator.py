#!/usr/bin/env python

# Copyright (c) 2019 The Khronos Group Inc.
# Use of this source code is governed by an MIT-style license that can be
# found in the LICENSE.txt file.

"""
  Generator for framebufferblit* tests.
  This file needs to be run in its folder.
"""

import sys

_DO_NOT_EDIT_WARNING = """<!--

This file is auto-generated from framebufferblit_test_generator.py
DO NOT EDIT!

-->

"""

_HTML_TEMPLATE = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>WebGL Framebuffer Blit Conformance Tests</title>
<link rel="stylesheet" href="../../../../resources/js-test-style.css"/>
<script src="../../../../js/js-test-pre.js"></script>
<script src="../../../../js/webgl-test-utils.js"></script>

<script src="../../../../closure-library/closure/goog/base.js"></script>
<script src="../../../deqp-deps.js"></script>
<script>goog.require('functional.gles3.es3fFramebufferBlitTests');</script>
</head>
<body>
<div id="description"></div>
<div id="console"></div>
<canvas id="canvas" width="200" height="200"> </canvas>
<script>
var wtu = WebGLTestUtils;
var gl = wtu.create3DContext('canvas', null, 2);

functional.gles3.es3fFramebufferBlitTests.run(gl, [%(start)s, %(end)s]);
</script>
</body>
</html>
"""

_GROUPS = [
    'rect',
    'conversion',
    'depth_stencil',
    'default_framebuffer',
]

_GROUP_TEST_COUNTS = [
    7,
    35,
    1,
    7
]

def GenerateFilename(group, count, index):
  """Generate test filename."""
  filename = group
  assert index >= 0 and index < count
  if count > 1:
    index_str = str(index)
    if index < 10:
      index_str = "0" + index_str
    filename += "_" + index_str
  filename += ".html"
  return filename

def WriteTest(filename, start, end):
  """Write one test."""
  file = open(filename, "wb")
  file.write(_DO_NOT_EDIT_WARNING)
  file.write(_HTML_TEMPLATE % {
    'start': start,
    'end': end
  })
  file.close

def GenerateTests():
  """Generate all tests."""
  assert len(_GROUPS) == len(_GROUP_TEST_COUNTS)
  test_index = 0
  filelist = []
  for ii in range(len(_GROUPS)):
    group = _GROUPS[ii]
    count = _GROUP_TEST_COUNTS[ii]
    for index in range(count):
      filename = GenerateFilename(group, count, index)
      filelist.append(filename)
      WriteTest(filename, test_index, test_index + 1)
      test_index += 1
  return filelist

def GenerateTestList(filelist):
  file = open("00_test_list.txt", "wb")
  file.write('\n'.join(filelist))
  file.close

def main(argv):
  """This is the main function."""
  filelist = GenerateTests()
  GenerateTestList(filelist)

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
