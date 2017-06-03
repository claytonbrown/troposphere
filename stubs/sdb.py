from . import AWSObject, AWSProperty
from .validators import *
from .constants import *


# -------------------------------------------

class SDBDomain(AWSObject):
    """# AWS::SDB::Domain - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simpledb.html",
    "Properties": {
        "Description": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simpledb.html#cfn-sdb-domain-description",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::SDB::Domain"

    props = {
        'Description': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simpledb.html#cfn-sdb-domain-description')
    }


