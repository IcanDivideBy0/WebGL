#!/usr/bin/env python

# Copyright (c) 2019 The Khronos Group Inc.
# Use of this source code is governed by an MIT-style license that can be
# found in the LICENSE.txt file.

"""
  Generator for shaderoperator* tests.
  This file needs to be run in its folder.
"""

import sys

_DO_NOT_EDIT_WARNING = """<!--

This file is auto-generated from shaderoperator_test_generator.py
DO NOT EDIT!

-->

"""

_HTML_TEMPLATE = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>WebGL Shader Operator Conformance Tests</title>
<link rel="stylesheet" href="../../../../resources/js-test-style.css"/>
<script src="../../../../js/js-test-pre.js"></script>
<script src="../../../../js/webgl-test-utils.js"></script>

<script src="../../../../closure-library/closure/goog/base.js"></script>
<script src="../../../deqp-deps.js"></script>
<script>
goog.require('functional.gles3.es3fShaderOperatorTests');
</script>
</head>
<body>
<div id="description"></div>
<div id="console"></div>
<canvas id="canvas" width="256" height="256"> </canvas>
<script>
var wtu = WebGLTestUtils;
var gl = wtu.create3DContext('canvas', null, 2);

functional.gles3.es3fShaderOperatorTests.run(gl, [%(start)s, %(end)s]);
</script>
</body>
</html>
"""

_GROUPS = [
    'unary_operator_00',
    'unary_operator_01',
    'unary_operator_02',
    'binary_operator_00',
    'binary_operator_01',
    'binary_operator_02',
    'binary_operator_03',
    'binary_operator_04',
    'binary_operator_05',
    'binary_operator_06',
    'binary_operator_07',
    'binary_operator_08',
    'binary_operator_09',
    'binary_operator_10',
    'binary_operator_11',
    'binary_operator_12',
    'binary_operator_13',
    'binary_operator_14',
    'binary_operator_15',
    'angle_and_trigonometry_00',
    'angle_and_trigonometry_01',
    'angle_and_trigonometry_02',
    'angle_and_trigonometry_03',
    'exponential',
    'common_functions_00',
    'common_functions_01',
    'common_functions_02',
    'common_functions_03',
    'common_functions_04',
    'common_functions_05',
    'common_functions_06',
    'geometric',
    'float_compare',
    'int_compare',
    'bool_compare',
    'selection',
    'sequence',
]

def GenerateFilename(group):
  """Generate test filename."""
  filename = group
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
  filelist = []
  for ii in range(len(_GROUPS)):
    filename = GenerateFilename(_GROUPS[ii])
    filelist.append(filename)
    WriteTest(filename, ii, ii + 1)
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
