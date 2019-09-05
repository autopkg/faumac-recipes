#!/usr/bin/python
#
# Copyright (c) 2015-present, RRZE
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
#
#
"""See docstring for FFmpegVersioner class"""

# Disabling warnings for env members and imports that only affect recipe-
# specific processors.
# pylint: disable=e1101,f0401

from autopkglib import Processor, ProcessorError
import tempfile
import subprocess
import os
from xml.dom import minidom

__all__ = ["FFmpegVersioner"]


class FFmpegVersioner(Processor):
  # pylint: disable=missing-docstring
  description = ("Get version from FFmpeg download.")
  input_variables = {
      "pathname": {
          "required": True,
          "description": ("Path to downloaded package.")
      }
  }
  output_variables = {
      "version": {
          "description": ("Version info parsed, naively derived from the "
                          "package's name.")
      }
  }

  __doc__ = description

  def main(self):
    filepath = self.env["pathname"]
    lastChar = filepath.split('ffmpeg-')[1]
    self.env["version"] = lastChar.split('.dmg')[0]
    self.output("Found version: %s" % self.env["version"])
    if not self.env["version"]:
      raise ProcessorError("An error occurred while extracting "
                           "Distribution file")


if __name__ == "__main__":
  PROCESSOR = FFmpegVersioner()
  PROCESSOR.execute_shell()
