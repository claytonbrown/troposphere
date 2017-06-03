from . import AWSObject, AWSProperty
from .validators import *
from .constants import *


# -------------------------------------------

class ECRRepository(AWSObject):
    """# AWS::ECR::Repository - CloudFormationResourceSpecification version: 1.4.0

    {
    "Attributes": {
        "Arn": {
            "PrimitiveType": "String"
        }
    },
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html",
    "Properties": {
        "RepositoryName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositoryname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "RepositoryPolicyText": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositorypolicytext",
            "PrimitiveType": "Json",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::ECR::Repository"

    props = {
        'RepositoryName': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositoryname'),
        'RepositoryPolicyText': ((basestring, dict), False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositorypolicytext')
    }


