from . import AWSObject, AWSProperty
from .validators import *
from .constants import *


# -------------------------------------------
class RDSIngress(AWSProperty):
    """# Ingress - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html",
    "Properties": {
        "CIDRIP": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-cidrip",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "EC2SecurityGroupId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-ec2securitygroupid",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "EC2SecurityGroupName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-ec2securitygroupname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "EC2SecurityGroupOwnerId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-ec2securitygroupownerid",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        }
    }
}
    """
    props = {
        'CIDRIP': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-cidrip'),
        'EC2SecurityGroupId': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-ec2securitygroupid'),
        'EC2SecurityGroupName': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-ec2securitygroupname'),
        'EC2SecurityGroupOwnerId': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group-rule.html#cfn-rds-securitygroup-ec2securitygroupownerid')
    }

# -------------------------------------------
class RDSOptionSetting(AWSProperty):
    """# OptionSetting - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations-optionsettings.html",
    "Properties": {
        "Name": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations-optionsettings.html#cfn-rds-optiongroup-optionconfigurations-optionsettings-name",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "Value": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations-optionsettings.html#cfn-rds-optiongroup-optionconfigurations-optionsettings-value",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'Name': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations-optionsettings.html#cfn-rds-optiongroup-optionconfigurations-optionsettings-name'),
        'Value': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations-optionsettings.html#cfn-rds-optiongroup-optionconfigurations-optionsettings-value')
    }

# -------------------------------------------
class RDSOptionConfiguration(AWSProperty):
    """# OptionConfiguration - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations.html",
    "Properties": {
        "DBSecurityGroupMemberships": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations.html#cfn-rds-optiongroup-optionconfigurations-dbsecuritygroupmemberships",
            "DuplicatesAllowed": true,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "OptionName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations.html#cfn-rds-optiongroup-optionconfigurations-optionname",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "OptionSettings": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations.html#cfn-rds-optiongroup-optionconfigurations-optionsettings",
            "Required": false,
            "Type": "OptionSetting",
            "UpdateType": "Mutable"
        },
        "Port": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations.html#cfn-rds-optiongroup-optionconfigurations-port",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "VpcSecurityGroupMemberships": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations.html#cfn-rds-optiongroup-optionconfigurations-vpcsecuritygroupmemberships",
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
        'DBSecurityGroupMemberships': ([basestring], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations.html#cfn-rds-optiongroup-optionconfigurations-dbsecuritygroupmemberships'),
        'OptionName': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations.html#cfn-rds-optiongroup-optionconfigurations-optionname'),
        'OptionSettings': (OptionSetting, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations.html#cfn-rds-optiongroup-optionconfigurations-optionsettings'),
        'Port': (positive_integer, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations.html#cfn-rds-optiongroup-optionconfigurations-port'),
        'VpcSecurityGroupMemberships': ([basestring], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-optiongroup-optionconfigurations.html#cfn-rds-optiongroup-optionconfigurations-vpcsecuritygroupmemberships')
    }

# -------------------------------------------

class RDSDBSecurityGroupIngress(AWSObject):
    """# AWS::RDS::DBSecurityGroupIngress - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html",
    "Properties": {
        "CIDRIP": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-cidrip",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "DBSecurityGroupName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-dbsecuritygroupname",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "EC2SecurityGroupId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-ec2securitygroupid",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "EC2SecurityGroupName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-ec2securitygroupname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "EC2SecurityGroupOwnerId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-ec2securitygroupownerid",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::RDS::DBSecurityGroupIngress"

    props = {
        'CIDRIP': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-cidrip'),
        'DBSecurityGroupName': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-dbsecuritygroupname'),
        'EC2SecurityGroupId': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-ec2securitygroupid'),
        'EC2SecurityGroupName': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-ec2securitygroupname'),
        'EC2SecurityGroupOwnerId': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html#cfn-rds-securitygroup-ingress-ec2securitygroupownerid')
    }


# -------------------------------------------

class RDSDBCluster(AWSObject):
    """# AWS::RDS::DBCluster - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html",
    "Properties": {
        "AvailabilityZones": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-availabilityzones",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "BackupRetentionPeriod": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-backuprententionperiod",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "DBClusterParameterGroupName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-dbclusterparametergroupname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "DBSubnetGroupName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-dbsubnetgroupname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "DatabaseName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-databasename",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "Engine": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-engine",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "EngineVersion": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-engineversion",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "KmsKeyId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-kmskeyid",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "MasterUserPassword": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-masteruserpassword",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "MasterUsername": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-masterusername",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "Port": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-port",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "PreferredBackupWindow": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-preferredbackupwindow",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "PreferredMaintenanceWindow": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-preferredmaintenancewindow",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "SnapshotIdentifier": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-snapshotidentifier",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "StorageEncrypted": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-storageencrypted",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "Tags": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-tags",
            "DuplicatesAllowed": true,
            "ItemType": "Tag",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "VpcSecurityGroupIds": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-vpcsecuritygroupids",
            "DuplicatesAllowed": false,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::RDS::DBCluster"

    props = {
        'AvailabilityZones': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-availabilityzones'),
        'BackupRetentionPeriod': (positive_integer, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-backuprententionperiod'),
        'DBClusterParameterGroupName': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-dbclusterparametergroupname'),
        'DBSubnetGroupName': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-dbsubnetgroupname'),
        'DatabaseName': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-databasename'),
        'Engine': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-engine'),
        'EngineVersion': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-engineversion'),
        'KmsKeyId': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-kmskeyid'),
        'MasterUserPassword': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-masteruserpassword'),
        'MasterUsername': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-masterusername'),
        'Port': (positive_integer, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-port'),
        'PreferredBackupWindow': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-preferredbackupwindow'),
        'PreferredMaintenanceWindow': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-preferredmaintenancewindow'),
        'SnapshotIdentifier': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-snapshotidentifier'),
        'StorageEncrypted': (boolean, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-storageencrypted'),
        'Tags': ([Tag], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-tags'),
        'VpcSecurityGroupIds': ([basestring], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#cfn-rds-dbcluster-vpcsecuritygroupids')
    }


# -------------------------------------------

class RDSDBSubnetGroup(AWSObject):
    """# AWS::RDS::DBSubnetGroup - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnet-group.html",
    "Properties": {
        "DBSubnetGroupDescription": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnet-group.html#cfn-rds-dbsubnetgroup-dbsubnetgroupdescription",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "SubnetIds": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnet-group.html#cfn-rds-dbsubnetgroup-subnetids",
            "DuplicatesAllowed": false,
            "PrimitiveItemType": "String",
            "Required": true,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "Tags": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnet-group.html#cfn-rds-dbsubnetgroup-tags",
            "DuplicatesAllowed": true,
            "ItemType": "Tag",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::RDS::DBSubnetGroup"

    props = {
        'DBSubnetGroupDescription': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnet-group.html#cfn-rds-dbsubnetgroup-dbsubnetgroupdescription'),
        'SubnetIds': ([basestring], True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnet-group.html#cfn-rds-dbsubnetgroup-subnetids'),
        'Tags': ([Tag], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnet-group.html#cfn-rds-dbsubnetgroup-tags')
    }


# -------------------------------------------

class RDSOptionGroup(AWSObject):
    """# AWS::RDS::OptionGroup - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html",
    "Properties": {
        "EngineName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-enginename",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "MajorEngineVersion": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-majorengineversion",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "OptionConfigurations": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-optionconfigurations",
            "DuplicatesAllowed": true,
            "ItemType": "OptionConfiguration",
            "Required": true,
            "Type": "List",
            "UpdateType": "Immutable"
        },
        "OptionGroupDescription": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-optiongroupdescription",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "Tags": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-tags",
            "DuplicatesAllowed": true,
            "ItemType": "Tag",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::RDS::OptionGroup"

    props = {
        'EngineName': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-enginename'),
        'MajorEngineVersion': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-majorengineversion'),
        'OptionConfigurations': ([OptionConfiguration], True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-optionconfigurations'),
        'OptionGroupDescription': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-optiongroupdescription'),
        'Tags': ([Tag], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html#cfn-rds-optiongroup-tags')
    }


# -------------------------------------------

class RDSDBParameterGroup(AWSObject):
    """# AWS::RDS::DBParameterGroup - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html",
    "Properties": {
        "Description": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html#cfn-rds-dbparametergroup-description",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "Family": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html#cfn-rds-dbparametergroup-family",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "Parameters": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html#cfn-rds-dbparametergroup-parameters",
            "DuplicatesAllowed": false,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "Map",
            "UpdateType": "Mutable"
        },
        "Tags": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html#cfn-rds-dbparametergroup-tags",
            "DuplicatesAllowed": true,
            "ItemType": "Tag",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::RDS::DBParameterGroup"

    props = {
        'Description': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html#cfn-rds-dbparametergroup-description'),
        'Family': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html#cfn-rds-dbparametergroup-family'),
        'Parameters': (dict, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html#cfn-rds-dbparametergroup-parameters'),
        'Tags': ([Tag], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html#cfn-rds-dbparametergroup-tags')
    }


# -------------------------------------------

class RDSEventSubscription(AWSObject):
    """# AWS::RDS::EventSubscription - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html",
    "Properties": {
        "Enabled": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-enabled",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "EventCategories": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-eventcategories",
            "DuplicatesAllowed": false,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "SnsTopicArn": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-snstopicarn",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "SourceIds": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-sourceids",
            "DuplicatesAllowed": true,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "SourceType": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-sourcetype",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Conditional"
        }
    }
}
    """

    resource_type = "AWS::RDS::EventSubscription"

    props = {
        'Enabled': (boolean, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-enabled'),
        'EventCategories': ([basestring], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-eventcategories'),
        'SnsTopicArn': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-snstopicarn'),
        'SourceIds': ([basestring], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-sourceids'),
        'SourceType': (basestring, False, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html#cfn-rds-eventsubscription-sourcetype')
    }


# -------------------------------------------

class RDSDBInstance(AWSObject):
    """# AWS::RDS::DBInstance - CloudFormationResourceSpecification version: 1.4.0

    {
    "Attributes": {
        "Endpoint.Address": {
            "PrimitiveType": "String"
        },
        "Endpoint.Port": {
            "PrimitiveType": "String"
        }
    },
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html",
    "Properties": {
        "AllocatedStorage": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-allocatedstorage",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "AllowMajorVersionUpgrade": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-allowmajorversionupgrade",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "AutoMinorVersionUpgrade": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-autominorversionupgrade",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Conditional"
        },
        "AvailabilityZone": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-availabilityzone",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "BackupRetentionPeriod": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-backupretentionperiod",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Conditional"
        },
        "CharacterSetName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-charactersetname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "DBClusterIdentifier": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbclusteridentifier",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "DBInstanceClass": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbinstanceclass",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "DBInstanceIdentifier": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbinstanceidentifier",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "DBName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "DBParameterGroupName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbparametergroupname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Conditional"
        },
        "DBSecurityGroups": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbsecuritygroups",
            "DuplicatesAllowed": true,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "DBSnapshotIdentifier": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbsnapshotidentifier",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "DBSubnetGroupName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbsubnetgroupname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "Domain": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-domain",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "DomainIAMRoleName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-domainiamrolename",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "Engine": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-engine",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "EngineVersion": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-engineversion",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Conditional"
        },
        "Iops": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-iops",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "KmsKeyId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-kmskeyid",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "LicenseModel": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-licensemodel",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "MasterUserPassword": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-masteruserpassword",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "MasterUsername": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-masterusername",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "MonitoringInterval": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-monitoringinterval",
            "PrimitiveType": "Integer",
            "Required": false,
            "UpdateType": "Conditional"
        },
        "MonitoringRoleArn": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-monitoringrolearn",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "MultiAZ": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-multiaz",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "OptionGroupName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-optiongroupname",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "Port": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-port",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "PreferredBackupWindow": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-preferredbackupwindow",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "PreferredMaintenanceWindow": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-preferredmaintenancewindow",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Conditional"
        },
        "PubliclyAccessible": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-publiclyaccessible",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "SourceDBInstanceIdentifier": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-sourcedbinstanceidentifier",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "StorageEncrypted": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-storageencrypted",
            "PrimitiveType": "Boolean",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "StorageType": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-storagetype",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Conditional"
        },
        "Tags": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-tags",
            "DuplicatesAllowed": true,
            "ItemType": "Tag",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "Timezone": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-timezone",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "VPCSecurityGroups": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-vpcsecuritygroups",
            "DuplicatesAllowed": true,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::RDS::DBInstance"

    props = {
        'AllocatedStorage': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-allocatedstorage'),
        'AllowMajorVersionUpgrade': (boolean, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-allowmajorversionupgrade'),
        'AutoMinorVersionUpgrade': (boolean, False, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-autominorversionupgrade'),
        'AvailabilityZone': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-availabilityzone'),
        'BackupRetentionPeriod': (basestring, False, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-backupretentionperiod'),
        'CharacterSetName': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-charactersetname'),
        'DBClusterIdentifier': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbclusteridentifier'),
        'DBInstanceClass': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbinstanceclass'),
        'DBInstanceIdentifier': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbinstanceidentifier'),
        'DBName': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbname'),
        'DBParameterGroupName': (basestring, False, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbparametergroupname'),
        'DBSecurityGroups': ([basestring], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbsecuritygroups'),
        'DBSnapshotIdentifier': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbsnapshotidentifier'),
        'DBSubnetGroupName': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-dbsubnetgroupname'),
        'Domain': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-domain'),
        'DomainIAMRoleName': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-domainiamrolename'),
        'Engine': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-engine'),
        'EngineVersion': (basestring, False, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-engineversion'),
        'Iops': (positive_integer, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-iops'),
        'KmsKeyId': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-kmskeyid'),
        'LicenseModel': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-licensemodel'),
        'MasterUserPassword': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-masteruserpassword'),
        'MasterUsername': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-masterusername'),
        'MonitoringInterval': (positive_integer, False, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-monitoringinterval'),
        'MonitoringRoleArn': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-monitoringrolearn'),
        'MultiAZ': (boolean, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-multiaz'),
        'OptionGroupName': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-optiongroupname'),
        'Port': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-port'),
        'PreferredBackupWindow': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-preferredbackupwindow'),
        'PreferredMaintenanceWindow': (basestring, False, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-preferredmaintenancewindow'),
        'PubliclyAccessible': (boolean, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-publiclyaccessible'),
        'SourceDBInstanceIdentifier': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-sourcedbinstanceidentifier'),
        'StorageEncrypted': (boolean, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-storageencrypted'),
        'StorageType': (basestring, False, 'Conditional', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-storagetype'),
        'Tags': ([Tag], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-tags'),
        'Timezone': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-timezone'),
        'VPCSecurityGroups': ([basestring], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-vpcsecuritygroups')
    }


# -------------------------------------------

class RDSDBSecurityGroup(AWSObject):
    """# AWS::RDS::DBSecurityGroup - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html",
    "Properties": {
        "DBSecurityGroupIngress": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-dbsecuritygroupingress",
            "DuplicatesAllowed": false,
            "ItemType": "Ingress",
            "Required": true,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "EC2VpcId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-ec2vpcid",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        },
        "GroupDescription": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-groupdescription",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "Tags": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-tags",
            "DuplicatesAllowed": true,
            "ItemType": "Tag",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::RDS::DBSecurityGroup"

    props = {
        'DBSecurityGroupIngress': ([Ingress], True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-dbsecuritygroupingress'),
        'EC2VpcId': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-ec2vpcid'),
        'GroupDescription': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-groupdescription'),
        'Tags': ([Tag], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html#cfn-rds-dbsecuritygroup-tags')
    }


# -------------------------------------------

class RDSDBClusterParameterGroup(AWSObject):
    """# AWS::RDS::DBClusterParameterGroup - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html",
    "Properties": {
        "Description": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-description",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "Family": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-family",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "Parameters": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-parameters",
            "PrimitiveType": "Json",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "Tags": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-tags",
            "DuplicatesAllowed": true,
            "ItemType": "Tag",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::RDS::DBClusterParameterGroup"

    props = {
        'Description': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-description'),
        'Family': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-family'),
        'Parameters': ((basestring, dict), True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-parameters'),
        'Tags': ([Tag], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html#cfn-rds-dbclusterparametergroup-tags')
    }


