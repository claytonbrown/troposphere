from . import AWSObject, AWSProperty
from .validators import *
from .constants import *


# -------------------------------------------
class SNSSubscription(AWSProperty):
    """# Subscription - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-subscription.html",
    "Properties": {
        "Endpoint": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-subscription.html#cfn-sns-topic-subscription-endpoint",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "Protocol": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-subscription.html#cfn-sns-topic-subscription-protocol",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        }
    }
}
    """
    props = {
        'Endpoint': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-subscription.html#cfn-sns-topic-subscription-endpoint'),
        'Protocol': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-subscription.html#cfn-sns-topic-subscription-protocol')
    }

# -------------------------------------------

class SNSSubscription(AWSObject):
    """# AWS::SNS::Subscription - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html",
    "Properties": {
        "Endpoint": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-endpoint",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "Protocol": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-protocol",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "TopicArn": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#topicarn",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        }
    }
}
    """

    resource_type = "AWS::SNS::Subscription"

    props = {
        'Endpoint': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-endpoint'),
        'Protocol': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#cfn-sns-protocol'),
        'TopicArn': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html#topicarn')
    }


# -------------------------------------------

class SNSTopic(AWSObject):
    """# AWS::SNS::Topic - CloudFormationResourceSpecification version: 1.4.0

    {
    "Attributes": {
        "TopicName": {
            "PrimitiveType": "String"
        }
    },
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html",
    "Properties": {
        "DisplayName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html#cfn-sns-topic-displayname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "Subscription": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html#cfn-sns-topic-subscription",
            "DuplicatesAllowed": true,
            "ItemType": "Subscription",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "TopicName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html#cfn-sns-topic-topicname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        }
    }
}
    """

    resource_type = "AWS::SNS::Topic"

    props = {
        'DisplayName': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html#cfn-sns-topic-displayname'),
        'Subscription': ([Subscription], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html#cfn-sns-topic-subscription'),
        'TopicName': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html#cfn-sns-topic-topicname')
    }


# -------------------------------------------

class SNSTopicPolicy(AWSObject):
    """# AWS::SNS::TopicPolicy - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html",
    "Properties": {
        "PolicyDocument": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html#cfn-sns-topicpolicy-policydocument",
            "PrimitiveType": "Json",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "Topics": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html#cfn-sns-topicpolicy-topics",
            "DuplicatesAllowed": true,
            "PrimitiveItemType": "String",
            "Required": true,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::SNS::TopicPolicy"

    props = {
        'PolicyDocument': ((basestring, dict), True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html#cfn-sns-topicpolicy-policydocument'),
        'Topics': ([basestring], True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html#cfn-sns-topicpolicy-topics')
    }


