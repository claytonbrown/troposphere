from . import AWSObject, AWSProperty
from .validators import *
from .constants import *


# -------------------------------------------
class ConfigConfigSnapshotDeliveryProperties(AWSProperty):
    """# ConfigSnapshotDeliveryProperties - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html",
    "Properties": {
        "DeliveryFrequency": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties-deliveryfrequency",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'DeliveryFrequency': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties-deliveryfrequency')
    }

# -------------------------------------------
class ConfigSource(AWSProperty):
    """# Source - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html",
    "Properties": {
        "Owner": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-owner",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "SourceDetails": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourcedetails",
            "DuplicatesAllowed": false,
            "ItemType": "SourceDetail",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "SourceIdentifier": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourceidentifier",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'Owner': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-owner'),
        'SourceDetails': ([SourceDetail], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourcedetails'),
        'SourceIdentifier': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourceidentifier')
    }

# -------------------------------------------
class ConfigScope(AWSProperty):
    """# Scope - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html",
    "Properties": {
        "ComplianceResourceId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourceid",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "ComplianceResourceTypes": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourcetypes",
            "DuplicatesAllowed": false,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "TagKey": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagkey",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "TagValue": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagvalue",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'ComplianceResourceId': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourceid'),
        'ComplianceResourceTypes': ([basestring], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourcetypes'),
        'TagKey': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagkey'),
        'TagValue': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagvalue')
    }

# -------------------------------------------
class ConfigRecordingGroup(AWSProperty):
    """# RecordingGroup - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html",
    "Properties": {
        "AllSupported": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-allsupported",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "IncludeGlobalResourceTypes": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-includeglobalresourcetypes",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "ResourceTypes": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-resourcetypes",
            "DuplicatesAllowed": true,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'AllSupported': (boolean, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-allsupported'),
        'IncludeGlobalResourceTypes': (boolean, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-includeglobalresourcetypes'),
        'ResourceTypes': ([basestring], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-resourcetypes')
    }

# -------------------------------------------
class ConfigSourceDetail(AWSProperty):
    """# SourceDetail - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html",
    "Properties": {
        "EventSource": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-source-sourcedetail-eventsource",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "MaximumExecutionFrequency": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-sourcedetail-maximumexecutionfrequency",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "MessageType": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-source-sourcedetail-messagetype",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'EventSource': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-source-sourcedetail-eventsource'),
        'MaximumExecutionFrequency': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-sourcedetail-maximumexecutionfrequency'),
        'MessageType': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-source-sourcedetail-messagetype')
    }

# -------------------------------------------

class ConfigDeliveryChannel(AWSObject):
    """# AWS::Config::DeliveryChannel - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html",
    "Properties": {
        "ConfigSnapshotDeliveryProperties": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties",
            "Required": false,
            "Type": "ConfigSnapshotDeliveryProperties",
            "UpdateType": "Mutable"
        },
        "Name": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-name",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "S3BucketName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3bucketname",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "S3KeyPrefix": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3keyprefix",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "SnsTopicARN": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-snstopicarn",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::Config::DeliveryChannel"

    props = {
        'ConfigSnapshotDeliveryProperties': (ConfigSnapshotDeliveryProperties, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties'),
        'Name': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-name'),
        'S3BucketName': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3bucketname'),
        'S3KeyPrefix': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3keyprefix'),
        'SnsTopicARN': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-snstopicarn')
    }


# -------------------------------------------

class ConfigConfigurationRecorder(AWSObject):
    """# AWS::Config::ConfigurationRecorder - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html",
    "Properties": {
        "Name": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-name",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "RecordingGroup": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-recordinggroup",
            "Required": false,
            "Type": "RecordingGroup",
            "UpdateType": "Mutable"
        },
        "RoleArn": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-rolearn",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::Config::ConfigurationRecorder"

    props = {
        'Name': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-name'),
        'RecordingGroup': (RecordingGroup, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-recordinggroup'),
        'RoleArn': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-rolearn')
    }


# -------------------------------------------

class ConfigConfigRule(AWSObject):
    """# AWS::Config::ConfigRule - CloudFormationResourceSpecification version: 1.4.0

    {
    "Attributes": {
        "Arn": {
            "PrimitiveType": "String"
        },
        "Compliance.Type": {
            "PrimitiveType": "String"
        },
        "ConfigRuleId": {
            "PrimitiveType": "String"
        }
    },
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html",
    "Properties": {
        "ConfigRuleName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-configrulename",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "Description": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-description",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "InputParameters": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-inputparameters",
            "PrimitiveType": "Json",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "MaximumExecutionFrequency": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-maximumexecutionfrequency",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "Scope": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-scope",
            "Required": false,
            "Type": "Scope",
            "UpdateType": "Mutable"
        },
        "Source": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-source",
            "Required": true,
            "Type": "Source",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::Config::ConfigRule"

    props = {
        'ConfigRuleName': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-configrulename'),
        'Description': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-description'),
        'InputParameters': ((basestring, dict), False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-inputparameters'),
        'MaximumExecutionFrequency': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-maximumexecutionfrequency'),
        'Scope': (Scope, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-scope'),
        'Source': (Source, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-source')
    }


