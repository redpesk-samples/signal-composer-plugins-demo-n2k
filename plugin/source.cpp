/*
 * Copyright (C) 2016 "IoT.bzh"
 * Author Romain Forlot <romain.forlot@iot.bzh>
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
*/
/*##################
## DEMO-N2K INCLUDES
##################*/
#include<iostream>
#include <wrap-json.h>
#include <string.h>

#define AFB_BINDING_VERSION 3
#include <afb/afb-binding.h>
#include <ctl-plugin.h>
#include <ctl-config.h>
#include <signal-composer.hpp>

/*###################
## DEMO-N2K VARIABLES
###################*/
#define API_NAME "@PROJECT_NAME@"
#define SIG_SPEED API_NAME "-speed"
#define SIG_ANGLE API_NAME "-angle"
#define DTB_CLASS "@DEMO_SENSOR@"
#define DTB_API "redis"
#define DTB_INSERT "ts_jinsert"
#define DEFAULT_RETENTION 1
#define MICRO 1000000
static int64_t TIMER_SPEED = 0;
static int64_t TIMER_ANGLE = 0;

extern "C"
{
    CTLP_CAPI_REGISTER(API_NAME);
    json_object *processSpeed(Signal *sig)
    {
        std::string time_str;
        json_object *req;
        int err;

        if(!TIMER_SPEED)
            TIMER_SPEED = sig->last_timestamp();
        else if(sig->last_timestamp() >= TIMER_SPEED + (int64_t)(sig->retention_*MICRO))
        {
            TIMER_SPEED = sig->last_timestamp();
            time_str = std::to_string(sig->last_timestamp());
            err = wrap_json_pack(&req, "{s:s s:{s:{s:f s:s}} s:s}",
            "class", DTB_CLASS,
            "data",
            "speed",
            "value", json_object_get_double(sig->average(sig->retention_)), 
            "unit", sig->unit_.c_str(),
            "timestamp", time_str.c_str());
            if(err)
                return NULL;
            return req;
        }
        return NULL;
    }

    json_object *processAngle(Signal *sig)
    {
        std::string time_str;
        json_object *req;
        int err;

        if(!TIMER_ANGLE)
            TIMER_ANGLE = sig->last_timestamp();
        else if(sig->last_timestamp() >= TIMER_ANGLE + (int64_t)(sig->retention_*MICRO))
        {
            TIMER_ANGLE = sig->last_timestamp();
            time_str = std::to_string(sig->last_timestamp());
            err = wrap_json_pack(&req, "{s:s s:{s:{s:f s:s}} s:s}",
            "class", DTB_CLASS,
            "data",
            "angle",
            "value", json_object_get_double(sig->average(sig->retention_)), 
            "unit", sig->unit_.c_str(),
            "timestamp", time_str.c_str());
            if(err)
                return NULL;
            return req;
        }
        return NULL;
    }

    json_object *processData(Signal *sig)
    {
        if(!strcmp(SIG_SPEED, sig->id().c_str()))
            return processSpeed(sig);
        else if(!strcmp(SIG_ANGLE, sig->id().c_str()))
            return processAngle(sig);
        return NULL;
    }

    static void callback(void *closure, json_object *object, const char *error, const char *info, afb_api_t api){}
    CTLP_CAPI(pushData, source, argsJ, eventJ)
    {
        struct signalCBT* ctx;
        Signal* sig;
        json_object *req;
        ctx = (struct signalCBT*)source->context;
        sig = (Signal*) ctx->aSignal;
        req = processData(sig);
        if(req)
            afb_api_call(source->api, DTB_API, DTB_INSERT, req, callback, NULL);
        return 0;
    }
}