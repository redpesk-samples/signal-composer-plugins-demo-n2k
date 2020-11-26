###########################################################################
# Copyright 2015, 2016, 2017 IoT.bzh
#
# author: Romain Forlot <romain.forlot@iot.bzh>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###########################################################################

PROJECT_TARGET_ADD(${PROJECT_NAME})
CONFIGURE_FILE(
	${CMAKE_SOURCE_DIR}${PROJECT_JSON_CONF_DIR}/config.json
	${CMAKE_CURRENT_BINARY_DIR}/${TARGET_NAME}.json
)
CONFIGURE_FILE(
	${CMAKE_CURRENT_SOURCE_DIR}/source.cpp
	${CMAKE_CURRENT_BINARY_DIR}/${TARGET_NAME}.cpp
)
ADD_LIBRARY(
	${TARGET_NAME}
	MODULE
	${CMAKE_CURRENT_BINARY_DIR}/${TARGET_NAME}.cpp
)
TARGET_INCLUDE_DIRECTORIES(
	${TARGET_NAME}
	PUBLIC
	${composer_INCLUDEDIR}
	${helpers_INCLUDEDIR}
	${controller_INCLUDEDIR}
)
TARGET_LINK_LIBRARIES(
	${TARGET_NAME} 
	signal-composer ${composer_LIBRARIES} -L${composer_LIBDIR}
	${helpers_LIBRARIES} -L${helpers_LIBDIR}
	${controller_LIBRARIES} -L${controller_LIBDIR}
)
SET_TARGET_PROPERTIES(
	${TARGET_NAME}
	PROPERTIES
	LABELS "PLUGIN"
	PREFIX ""
	SUFFIX ${PLUGIN_SUFFIX}
	OUTPUT_NAME ${TARGET_NAME}
	INSTALL_RPATH "$ORIGIN:$ORIGIN/.."
	BUILD_RPATH "$ORIGIN:$ORIGIN/.."
)
ADD_CUSTOM_TARGET(
	install_${TARGET_NAME}
	COMMAND install -d \${DESTDIR}${composer_LIBDIR}/plugins
	COMMAND install ${CMAKE_CURRENT_BINARY_DIR}/${TARGET_NAME}${PLUGIN_SUFFIX} \${DESTDIR}/${composer_LIBDIR}/plugins
	COMMAND install -d \${DESTDIR}${composer_LIBDIR}/../etc
	COMMAND install ${CMAKE_CURRENT_BINARY_DIR}/${TARGET_NAME}.json \${DESTDIR}/${composer_LIBDIR}/../etc
	COMMAND
)