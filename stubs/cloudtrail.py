from . import AWSObject, AWSProperty
from .validators import *
from .constants import *


# -------------------------------------------

class CloudTrailTrail(AWSObject):
    """# AWS::CloudTrail::Trail - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html",
    "Properties": {
        "CloudWatchLogsLogGroupArn": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsloggrouparn",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "CloudWatchLogsRoleArn": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsrolearn",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "EnableLogFileValidation": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-enablelogfilevalidation",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "IncludeGlobalServiceEvents": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-includeglobalserviceevents",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "IsLogging": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging",
            "PrimitiveType": "Boolean",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "IsMultiRegionTrail": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "KMSKeyId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "S3BucketName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3bucketname",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "S3KeyPrefix": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3keyprefix",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "SnsTopicName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-snstopicname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::CloudTrail::Trail"

    props = {
        'CloudWatchLogsLogGroupArn': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsloggrouparn'),
        'CloudWatchLogsRoleArn': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsrolearn'),
        'EnableLogFileValidation': (boolean, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-enablelogfilevalidation'),
        'IncludeGlobalServiceEvents': (boolean, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-includeglobalserviceevents'),
        'IsLogging': (boolean, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging'),
        'IsMultiRegionTrail': (boolean, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail'),
        'KMSKeyId': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid'),
        'S3BucketName': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3bucketname'),
        'S3KeyPrefix': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3keyprefix'),
        'SnsTopicName': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-snstopicname')
    }


