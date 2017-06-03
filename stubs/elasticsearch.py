from . import AWSObject, AWSProperty
from .validators import *
from .constants import *


# -------------------------------------------
class ElasticsearchElasticsearchClusterConfig(AWSProperty):
    """# ElasticsearchClusterConfig - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html",
    "Properties": {
        "DedicatedMasterCount": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmastercount",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "DedicatedMasterEnabled": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmasterenabled",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "DedicatedMasterType": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmastertype",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "InstanceCount": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-instancecount",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "InstanceType": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-instnacetype",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "ZoneAwarenessEnabled": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-zoneawarenessenabled",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'DedicatedMasterCount': (positive_integer, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmastercount'),
        'DedicatedMasterEnabled': (boolean, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmasterenabled'),
        'DedicatedMasterType': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-dedicatedmastertype'),
        'InstanceCount': (positive_integer, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-instancecount'),
        'InstanceType': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-instnacetype'),
        'ZoneAwarenessEnabled': (boolean, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html#cfn-elasticsearch-domain-elasticseachclusterconfig-zoneawarenessenabled')
    }

# -------------------------------------------
class ElasticsearchSnapshotOptions(AWSProperty):
    """# SnapshotOptions - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html",
    "Properties": {
        "AutomatedSnapshotStartHour": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html#cfn-elasticsearch-domain-snapshotoptions-automatedsnapshotstarthour",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'AutomatedSnapshotStartHour': (positive_integer, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html#cfn-elasticsearch-domain-snapshotoptions-automatedsnapshotstarthour')
    }

# -------------------------------------------
class ElasticsearchEBSOptions(AWSProperty):
    """# EBSOptions - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html",
    "Properties": {
        "EBSEnabled": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-ebsenabled",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "Iops": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-iops",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "VolumeSize": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumesize",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "VolumeType": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumetype",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'EBSEnabled': (boolean, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-ebsenabled'),
        'Iops': (positive_integer, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-iops'),
        'VolumeSize': (positive_integer, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumesize'),
        'VolumeType': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html#cfn-elasticsearch-domain-ebsoptions-volumetype')
    }

# -------------------------------------------

class ElasticsearchDomain(AWSObject):
    """# AWS::Elasticsearch::Domain - CloudFormationResourceSpecification version: 1.4.0

    {
    "Attributes": {
        "DomainArn": {
            "PrimitiveType": "String"
        },
        "DomainEndpoint": {
            "PrimitiveType": "String"
        }
    },
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html",
    "Properties": {
        "AccessPolicies": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-accesspolicies",
            "PrimitiveType": "Json",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "AdvancedOptions": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-advancedoptions",
            "DuplicatesAllowed": false,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "Map",
            "UpdateType": "Mutable"
        },
        "DomainName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-domainname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "EBSOptions": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-ebsoptions",
            "Required": false,
            "Type": "EBSOptions",
            "UpdateType": "Mutable"
        },
        "ElasticsearchClusterConfig": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchclusterconfig",
            "Required": false,
            "Type": "ElasticsearchClusterConfig",
            "UpdateType": "Mutable"
        },
        "ElasticsearchVersion": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchversion",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "SnapshotOptions": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-snapshotoptions",
            "Required": false,
            "Type": "SnapshotOptions",
            "UpdateType": "Mutable"
        },
        "Tags": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-tags",
            "DuplicatesAllowed": true,
            "ItemType": "Tag",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::Elasticsearch::Domain"

    props = {
        'AccessPolicies': ((basestring, dict), False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-accesspolicies'),
        'AdvancedOptions': (dict, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-advancedoptions'),
        'DomainName': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-domainname'),
        'EBSOptions': (EBSOptions, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-ebsoptions'),
        'ElasticsearchClusterConfig': (ElasticsearchClusterConfig, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchclusterconfig'),
        'ElasticsearchVersion': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-elasticsearchversion'),
        'SnapshotOptions': (SnapshotOptions, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-snapshotoptions'),
        'Tags': ([Tag], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#cfn-elasticsearch-domain-tags')
    }


