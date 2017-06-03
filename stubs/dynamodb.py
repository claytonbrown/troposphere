from . import AWSObject, AWSProperty
from .validators import *
from .constants import *


# -------------------------------------------
class DynamoDBKeySchema(AWSProperty):
    """# KeySchema - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html",
    "Properties": {
        "AttributeName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-attributename",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "KeyType": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-keytype",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'AttributeName': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-attributename'),
        'KeyType': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-keytype')
    }

# -------------------------------------------
class DynamoDBAttributeDefinition(AWSProperty):
    """# AttributeDefinition - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html",
    "Properties": {
        "AttributeName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "AttributeType": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename-attributetype",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'AttributeName': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename'),
        'AttributeType': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename-attributetype')
    }

# -------------------------------------------
class DynamoDBProjection(AWSProperty):
    """# Projection - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html",
    "Properties": {
        "NonKeyAttributes": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-nonkeyatt",
            "DuplicatesAllowed": true,
            "PrimitiveItemType": "String",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "ProjectionType": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-projtype",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'NonKeyAttributes': ([basestring], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-nonkeyatt'),
        'ProjectionType': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-projtype')
    }

# -------------------------------------------
class DynamoDBLocalSecondaryIndex(AWSProperty):
    """# LocalSecondaryIndex - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html",
    "Properties": {
        "IndexName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-indexname",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "KeySchema": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-keyschema",
            "DuplicatesAllowed": true,
            "ItemType": "KeySchema",
            "Required": true,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "Projection": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-projection",
            "Required": true,
            "Type": "Projection",
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'IndexName': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-indexname'),
        'KeySchema': ([KeySchema], True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-keyschema'),
        'Projection': (Projection, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-projection')
    }

# -------------------------------------------
class DynamoDBProvisionedThroughput(AWSProperty):
    """# ProvisionedThroughput - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html",
    "Properties": {
        "ReadCapacityUnits": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-readcapacityunits",
            "PrimitiveType": "Integer",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "WriteCapacityUnits": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-writecapacityunits",
            "PrimitiveType": "Integer",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'ReadCapacityUnits': (positive_integer, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-readcapacityunits'),
        'WriteCapacityUnits': (positive_integer, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-writecapacityunits')
    }

# -------------------------------------------
class DynamoDBGlobalSecondaryIndex(AWSProperty):
    """# GlobalSecondaryIndex - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html",
    "Properties": {
        "IndexName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-indexname",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "KeySchema": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-keyschema",
            "DuplicatesAllowed": true,
            "ItemType": "KeySchema",
            "Required": true,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "Projection": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-projection",
            "Required": true,
            "Type": "Projection",
            "UpdateType": "Mutable"
        },
        "ProvisionedThroughput": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-provisionedthroughput",
            "Required": true,
            "Type": "ProvisionedThroughput",
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'IndexName': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-indexname'),
        'KeySchema': ([KeySchema], True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-keyschema'),
        'Projection': (Projection, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-projection'),
        'ProvisionedThroughput': (ProvisionedThroughput, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-provisionedthroughput')
    }

# -------------------------------------------
class DynamoDBStreamSpecification(AWSProperty):
    """# StreamSpecification - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-streamspecification.html",
    "Properties": {
        "StreamViewType": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-streamspecification.html#cfn-dynamodb-streamspecification-streamviewtype",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'StreamViewType': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-streamspecification.html#cfn-dynamodb-streamspecification-streamviewtype')
    }

# -------------------------------------------

class DynamoDBTable(AWSObject):
    """# AWS::DynamoDB::Table - CloudFormationResourceSpecification version: 1.4.0

    {
    "Attributes": {
        "StreamArn": {
            "PrimitiveType": "String"
        }
    },
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html",
    "Properties": {
        "AttributeDefinitions": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-attributedef",
            "DuplicatesAllowed": true,
            "ItemType": "AttributeDefinition",
            "Required": true,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "GlobalSecondaryIndexes": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-gsi",
            "DuplicatesAllowed": true,
            "ItemType": "GlobalSecondaryIndex",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "KeySchema": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-keyschema",
            "DuplicatesAllowed": true,
            "ItemType": "KeySchema",
            "Required": true,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "LocalSecondaryIndexes": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-lsi",
            "DuplicatesAllowed": true,
            "ItemType": "LocalSecondaryIndex",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "ProvisionedThroughput": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-provisionedthroughput",
            "Required": true,
            "Type": "ProvisionedThroughput",
            "UpdateType": "Mutable"
        },
        "StreamSpecification": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-streamspecification",
            "Required": false,
            "Type": "StreamSpecification",
            "UpdateType": "Mutable"
        },
        "TableName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tablename",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Immutable"
        }
    }
}
    """

    resource_type = "AWS::DynamoDB::Table"

    props = {
        'AttributeDefinitions': ([AttributeDefinition], True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-attributedef'),
        'GlobalSecondaryIndexes': ([GlobalSecondaryIndex], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-gsi'),
        'KeySchema': ([KeySchema], True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-keyschema'),
        'LocalSecondaryIndexes': ([LocalSecondaryIndex], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-lsi'),
        'ProvisionedThroughput': (ProvisionedThroughput, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-provisionedthroughput'),
        'StreamSpecification': (StreamSpecification, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-streamspecification'),
        'TableName': (basestring, False, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tablename')
    }


