# -*- coding: utf-8 -*-
#

import json
import requests
import jmespath
import collections
import pprint
import logging
import colorlog

# create logger
log = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(colorlog.ColoredFormatter('%(log_color)s%(levelname)-8s%(reset)s %(message)s'))
log.addHandler(ch)


schemaUrl = "https://d1uauaxba7bl26.cloudfront.net/latest/CloudFormationResourceSpecification.json"
schema = requests.get(schemaUrl).json()
schema_version = schema[u'ResourceSpecificationVersion']

log.info('Generating stubs from CloudFormationResourceSpecification version : %s' % (schema_version))

tropo_defs = {}

SchemaPropertyTypes = {}
AllPropertyTypes = set()

class_def_template = """

class %s(AWSObject):
    \"\"\"# %s - CloudFormationResourceSpecification version: %s

    %s
    \"\"\"

    resource_type = "%s"

    props = {
%s
    }

"""
class_property_template = """        '%s': (%s, %s, '%s', '%s')"""

class_PropertyTypes_template = """
class %s(AWSProperty):
    \"\"\"# %s - CloudFormationResourceSpecification version: %s

    %s
    \"\"\"
    props = {
%s
    }
"""  # .PropertyName, props


def resource_data_type(resource):
    try:
        if "Type" in resource.keys():
            if resource["Type"] in AllPropertyTypes:
               return '%s' % (resource["Type"])

            if resource["Type"] == "Map":
                return "dict"

            if resource["Type"] == "List":
                if "PrimitiveItemType" in resource.keys() and resource["PrimitiveItemType"] == "String":
                    return "[basestring]"
                if "PrimitiveItemType" in resource.keys() and resource["PrimitiveItemType"] == "Json":
                    return "[basestring]"
                if "ItemType" in resource.keys():
                    return "[%s]" % (resource["ItemType"])

            if resource["Type"] == "Json":
                return "basestring"

            if resource["Type"] in schema["PropertyTypes"].keys():
                return resource["Type"]

            if resource["Type"] == "GeoRestriction":
                return 'GeoRestriction'

        if "PrimitiveType" in resource.keys():

            if resource["PrimitiveType"] == "String":
                return "basestring"

            if resource["PrimitiveType"] == "Timestamp":
                return "basestring"

            if resource["PrimitiveType"] == "List":
                return "list"

            if resource["PrimitiveType"] == "Boolean":
                return "boolean"

            if resource["PrimitiveType"] == "Integer":
                return "positive_integer"

            if resource["PrimitiveType"] == "Long":
                return "float"

            if resource["PrimitiveType"] == "Double":
                return "float"

            if resource["PrimitiveType"] == "Json":
                return "(basestring, dict)"

        log.warn(resource)
        raise Exception("Unampped Types from Schema")

    except:
        log.warn(resource)
        log.warn("\n" + "_" * 50 + "\n" + resource["Type"] + "\n" + "-" * 50 + "\n" + json.dumps(resource, indent=4, sort_keys=True))
    return 'basestring'

for key in schema[u"PropertyTypes"].keys():
    AllPropertyTypes.add("Tag")
    try:
        if key != "Tag":
            resource_type, property_name = key.split(".")
            AllPropertyTypes.add(property_name)
    except Exception as e: 
        log.warn(e)

for key in schema[u"PropertyTypes"].keys():
    log.debug("PropertyTypes: %s " % (key))

    # build lookup array of schema properties
    try:
        if "." not in key:
            AllPropertyTypes.add(key)
            property_name = key
        else:
            resource_type, property_name = key.split(".")
            if resource_type in SchemaPropertyTypes.keys():
                SchemaPropertyTypes[resource_type].append(property_name)
            else:
                SchemaPropertyTypes[resource_type] = [property_name]
            AllPropertyTypes.add(property_name)
    except Exception as e:
        log.warn(e)
        log.warn(key)

    SchemaProperty = schema[u"PropertyTypes"][key]

    log.debug(key)
    log.debug(json.dumps(SchemaProperty, indent=4, sort_keys=True))

    splitkey = key.replace('.','::').split("::")
    if len(splitkey) > 1:
        service_family = splitkey[1]
        resource_type = splitkey[-1]
    else:
        service_family = key
        resource_type = key

    unique_name = service_family + resource_type
    property_attributes = []

    if "Properties" in SchemaProperty.keys():
        for attribute_name in SchemaProperty['Properties'].keys():
            property_attribute = SchemaProperty['Properties'][attribute_name]

            class_property = class_property_template % (
                attribute_name,
                resource_data_type(property_attribute),
                property_attribute["Required"],
                property_attribute["UpdateType"],
                property_attribute["Documentation"]
            )

            property_attributes.append(class_property)
        property_attributes = ",\n".join(property_attributes)
        resource_class = class_PropertyTypes_template % (unique_name,
                                               property_name,
                                               schema_version,
                                               json.dumps(SchemaProperty, indent=4, sort_keys=True),
                                               property_attributes
                                               )

        log.debug(resource_class)
        if service_family not in tropo_defs.keys():
            tropo_defs[service_family] = [resource_class]
        else:
            tropo_defs[service_family].append(resource_class)



for key in schema[u'ResourceTypes'].keys():
    resource = schema[u'ResourceTypes'][key]
    splitkey = key.replace('.','::').split("::")
    service_family = splitkey[1]
    resource_type = splitkey[-1]
    unique_name = service_family + resource_type
    log.debug("service_family: %s" % (service_family))
    log.debug("resource_type: %s" % (resource_type))
    log.debug("unique_name: %s" % (unique_name))
    properties = []
    for attribute_name in resource['Properties'].keys():
        resource_attribute = resource['Properties'][attribute_name]

        class_property = class_property_template % (
            attribute_name,
            resource_data_type(resource_attribute),
            resource_attribute["Required"],
            resource_attribute["UpdateType"],
            resource_attribute["Documentation"]
        )

        properties.append(class_property)
    resource_properties = ",\n".join(properties)
    # json.dumps(resource, indent=4, sort_keys=True).replace("\n", "\n\t")
    log.debug("unique_name: %s" % (unique_name))
    log.debug("key: %s" % (key))
    log.debug("schema_version: %s" % (schema_version))
    log.debug("resource[\"\"]: %s" % (resource))
    log.debug("resource_properties: %s" % (resource_properties))
    resource_class = class_def_template % (unique_name,
                                           key,
                                           schema_version,
                                           json.dumps(resource, indent=4, sort_keys=True),
                                           key,
                                           resource_properties
                                           )

    if service_family not in tropo_defs.keys():
        tropo_defs[service_family] = [resource_class]
    else:
        tropo_defs[service_family].append(resource_class)


for service_family in tropo_defs.keys():
    file = open("./stubs/%s.py" % service_family.lower(), 'w')
    file.write("""from . import AWSObject, AWSProperty
from .validators import *
from .constants import *\n\n
""")

    for classdef in tropo_defs[service_family]:
        file.write(u"# -------------------------------------------%s\n" % (classdef))
    file.close()
    log.info("Written updated stubs for services: %s " % (service_family))

# pprint.pprint(SchemaPropertyTypes)
