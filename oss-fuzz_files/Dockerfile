# Copyright 2024 Google LLC
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
################################################################################

FROM gcr.io/oss-fuzz-base/base-builder-python

# Clone the project repository
RUN git clone --depth 1 --branch main https://github.com/bernardoras/fuzzed_project_example.git

WORKDIR /src/fuzzed_project_example

# Copy the build script and fuzzer script into the source directory
COPY build.sh example_fuzzer.py $SRC/

# Copy the seed corpus ZIP into the source directory so it's accessible during the build
COPY example_fuzzer_seed_corpus.zip $SRC/

# Run the build script
RUN bash $SRC/build.sh