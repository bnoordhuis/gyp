#!/bin/bash
# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# If this script is invoked through a symlink, follow that symlink to find
# the location of gyp_main.py.
base=$(dirname "$0")
link=$(readlink "$0")
if [ ! -z "$link" ]; then
  base="${base}/$(dirname "$link")"
fi
exec python "${base}/gyp_main.py" "$@"
