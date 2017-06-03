from . import AWSObject, AWSProperty
from .validators import *
from .constants import *


# -------------------------------------------

class WorkSpacesWorkspace(AWSObject):
    """# AWS::WorkSpaces::Workspace - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html",
    "Properties": {
        "BundleId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-bundleid",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Conditional"
        },
        "DirectoryId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-directoryid",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Conditional"
        },
        "RootVolumeEncryptionEnabled": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-rootvolumeencryptionenabled",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Conditional"
        },
        "UserName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-username",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "UserVolumeEncryptionEnabled": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-uservolumeencryptionenabled",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Conditional"
        },
        "VolumeEncryptionKey": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-volumeencryptionkey",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Conditional"
        }
    }
}
    """

    resource_type = "AWS::WorkSpaces::Workspace"

    props = {
        'BundleId': (basestring, True, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-bundleid'),
        'DirectoryId': (basestring, True, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-directoryid'),
        'RootVolumeEncryptionEnabled': (boolean, False, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-rootvolumeencryptionenabled'),
        'UserName': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-username'),
        'UserVolumeEncryptionEnabled': (boolean, False, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-uservolumeencryptionenabled'),
        'VolumeEncryptionKey': (basestring, False, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-volumeencryptionkey')
    }


