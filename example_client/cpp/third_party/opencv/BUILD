#
# Copyright (c) 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

package(
    default_visibility = ["//visibility:public"],
)

cc_library(
    name = "opencv",
    srcs = glob([
        "lib/libopencv_core.so",
        "lib/libopencv_imgcodecs.so",
        "lib/libopencv_imgproc.so"
    ]),
    hdrs = glob([
        "include/**/*.*"
    ]),
    strip_include_prefix = "include",
    visibility = ["//visibility:public"],
)
