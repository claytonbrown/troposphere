from . import AWSObject, AWSProperty
from .validators import *
from .constants import *


# -------------------------------------------

class CloudFormationWaitCondition(AWSObject):
    """# AWS::CloudFormation::WaitCondition - CloudFormationResourceSpecification version: 1.4.0

    {
    "Attributes": {
        "Data": {
            "PrimitiveType": "Json"
        }
    },
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html",
    "Properties": {
        "Count": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-count",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "Handle": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-handle",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "Timeout": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-timeout",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::CloudFormation::WaitCondition"

    props = {
        'Count': (positive_integer, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-count'),
        'Handle': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-handle'),
        'Timeout': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-timeout')
    }


# -------------------------------------------

class CloudFormationStack(AWSObject):
    """# AWS::CloudFormation::Stack - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html",
    "Properties": {
        "NotificationARNs": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-notificationarns",
            "DuplicatesAllowed": false,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "Parameters": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-parameters",
            "DuplicatesAllowed": false,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "Map",
            "UpdateType": "Mutable"
        },
        "Tags": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-tags",
            "DuplicatesAllowed": true,
            "ItemType": "Tag",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "TemplateURL": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-templateurl",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "TimeoutInMinutes": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-timeoutinminutes",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::CloudFormation::Stack"

    props = {
        'NotificationARNs': ([basestring], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-notificationarns'),
        'Parameters': (dict, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-parameters'),
        'Tags': ([Tag], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-tags'),
        'TemplateURL': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-templateurl'),
        'TimeoutInMinutes': (positive_integer, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-timeoutinminutes')
    }


# -------------------------------------------

class CloudFormationWaitConditionHandle(AWSObject):
    """# AWS::CloudFormation::WaitConditionHandle - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html",
    "Properties": {}
}
    """

    resource_type = "AWS::CloudFormation::WaitConditionHandle"

    props = {

    }


# -------------------------------------------

class CloudFormationCustomResource(AWSObject):
    """# AWS::CloudFormation::CustomResource - CloudFormationResourceSpecification version: 1.4.0

    {
    "AdditionalProperties": true,
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html",
    "Properties": {
        "ServiceToken": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#cfn-customresource-servicetoken",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        }
    }
}
    """

    resource_type = "AWS::CloudFormation::CustomResource"

    props = {
        'ServiceToken': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#cfn-customresource-servicetoken')
    }


