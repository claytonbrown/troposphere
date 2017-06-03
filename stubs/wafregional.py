from . import AWSObject, AWSProperty
from .validators import *
from .constants import *


# -------------------------------------------
class WAFRegionalByteMatchTuple(AWSProperty):
    """# ByteMatchTuple - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html",
    "Properties": {
        "FieldToMatch": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-fieldtomatch",
            "Required": true,
            "Type": "FieldToMatch",
            "UpdateType": "Mutable"
        },
        "PositionalConstraint": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-positionalconstraint",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "TargetString": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstring",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "TargetStringBase64": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstringbase64",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "TextTransformation": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-texttransformation",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'TargetString': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstring'),
        'TargetStringBase64': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-targetstringbase64'),
        'PositionalConstraint': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-positionalconstraint'),
        'TextTransformation': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-texttransformation'),
        'FieldToMatch': (FieldToMatch, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-bytematchtuple.html#cfn-wafregional-bytematchset-bytematchtuple-fieldtomatch')
    }

# -------------------------------------------
class WAFRegionalFieldToMatch(AWSProperty):
    """# FieldToMatch - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html",
    "Properties": {
        "Data": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-data",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "Type": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-type",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'Type': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-type'),
        'Data': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-bytematchset-fieldtomatch.html#cfn-wafregional-bytematchset-fieldtomatch-data')
    }

# -------------------------------------------
class WAFRegionalXssMatchTuple(AWSProperty):
    """# XssMatchTuple - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html",
    "Properties": {
        "FieldToMatch": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-fieldtomatch",
            "Required": true,
            "Type": "FieldToMatch",
            "UpdateType": "Mutable"
        },
        "TextTransformation": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-texttransformation",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'TextTransformation': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-texttransformation'),
        'FieldToMatch': (FieldToMatch, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-xssmatchtuple.html#cfn-wafregional-xssmatchset-xssmatchtuple-fieldtomatch')
    }

# -------------------------------------------
class WAFRegionalRule(AWSProperty):
    """# Rule - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html",
    "Properties": {
        "Action": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-action",
            "Required": true,
            "Type": "Action",
            "UpdateType": "Mutable"
        },
        "Priority": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-priority",
            "PrimitiveType": "Integer",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "RuleId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-ruleid",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'Action': (Action, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-action'),
        'Priority': (positive_integer, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-priority'),
        'RuleId': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-rule.html#cfn-wafregional-webacl-rule-ruleid')
    }

# -------------------------------------------
class WAFRegionalIPSetDescriptor(AWSProperty):
    """# IPSetDescriptor - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html",
    "Properties": {
        "Type": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-type",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "Value": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-value",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'Type': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-type'),
        'Value': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-ipset-ipsetdescriptor.html#cfn-wafregional-ipset-ipsetdescriptor-value')
    }

# -------------------------------------------
class WAFRegionalFieldToMatch(AWSProperty):
    """# FieldToMatch - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html",
    "Properties": {
        "Data": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-data",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "Type": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-type",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'Type': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-type'),
        'Data': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-xssmatchset-fieldtomatch.html#cfn-wafregional-xssmatchset-fieldtomatch-data')
    }

# -------------------------------------------
class WAFRegionalSizeConstraint(AWSProperty):
    """# SizeConstraint - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html",
    "Properties": {
        "ComparisonOperator": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-comparisonoperator",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "FieldToMatch": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-fieldtomatch",
            "Required": true,
            "Type": "FieldToMatch",
            "UpdateType": "Mutable"
        },
        "Size": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-size",
            "PrimitiveType": "Integer",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "TextTransformation": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-texttransformation",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'ComparisonOperator': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-comparisonoperator'),
        'Size': (positive_integer, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-size'),
        'TextTransformation': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-texttransformation'),
        'FieldToMatch': (FieldToMatch, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-sizeconstraint.html#cfn-wafregional-sizeconstraintset-sizeconstraint-fieldtomatch')
    }

# -------------------------------------------
class WAFRegionalAction(AWSProperty):
    """# Action - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html",
    "Properties": {
        "Type": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html#cfn-wafregional-webacl-action-type",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'Type': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-webacl-action.html#cfn-wafregional-webacl-action-type')
    }

# -------------------------------------------
class WAFRegionalFieldToMatch(AWSProperty):
    """# FieldToMatch - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html",
    "Properties": {
        "Data": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-data",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "Type": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-type",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'Type': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-type'),
        'Data': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sizeconstraintset-fieldtomatch.html#cfn-wafregional-sizeconstraintset-fieldtomatch-data')
    }

# -------------------------------------------
class WAFRegionalPredicate(AWSProperty):
    """# Predicate - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html",
    "Properties": {
        "DataId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-dataid",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "Negated": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-negated",
            "PrimitiveType": "Boolean",
            "Required": true,
            "UpdateType": "Mutable"
        },
        "Type": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-type",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'Type': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-type'),
        'DataId': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-dataid'),
        'Negated': (boolean, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-rule-predicate.html#cfn-wafregional-rule-predicate-negated')
    }

# -------------------------------------------
class WAFRegionalFieldToMatch(AWSProperty):
    """# FieldToMatch - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html",
    "Properties": {
        "Data": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-data",
            "PrimitiveType": "String",
            "Required": false,
            "UpdateType": "Mutable"
        },
        "Type": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-type",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'Type': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-type'),
        'Data': (basestring, False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-fieldtomatch.html#cfn-wafregional-sqlinjectionmatchset-fieldtomatch-data')
    }

# -------------------------------------------
class WAFRegionalSqlInjectionMatchTuple(AWSProperty):
    """# SqlInjectionMatchTuple - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html",
    "Properties": {
        "FieldToMatch": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-fieldtomatch",
            "Required": true,
            "Type": "FieldToMatch",
            "UpdateType": "Mutable"
        },
        "TextTransformation": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-texttransformation",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Mutable"
        }
    }
}
    """
    props = {
        'TextTransformation': (basestring, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-texttransformation'),
        'FieldToMatch': (FieldToMatch, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuple-fieldtomatch')
    }

# -------------------------------------------

class WAFRegionalSizeConstraintSet(AWSObject):
    """# AWS::WAFRegional::SizeConstraintSet - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html",
    "Properties": {
        "Name": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-name",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "SizeConstraints": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-sizeconstraints",
            "ItemType": "SizeConstraint",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::WAFRegional::SizeConstraintSet"

    props = {
        'SizeConstraints': ([SizeConstraint], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-sizeconstraints'),
        'Name': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html#cfn-wafregional-sizeconstraintset-name')
    }


# -------------------------------------------

class WAFRegionalSqlInjectionMatchSet(AWSObject):
    """# AWS::WAFRegional::SqlInjectionMatchSet - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html",
    "Properties": {
        "Name": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-name",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "SqlInjectionMatchTuples": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuples",
            "ItemType": "SqlInjectionMatchTuple",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::WAFRegional::SqlInjectionMatchSet"

    props = {
        'SqlInjectionMatchTuples': ([SqlInjectionMatchTuple], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-sqlinjectionmatchtuples'),
        'Name': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html#cfn-wafregional-sqlinjectionmatchset-name')
    }


# -------------------------------------------

class WAFRegionalXssMatchSet(AWSObject):
    """# AWS::WAFRegional::XssMatchSet - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html",
    "Properties": {
        "Name": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-name",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "XssMatchTuples": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-xssmatchtuples",
            "ItemType": "XssMatchTuple",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::WAFRegional::XssMatchSet"

    props = {
        'XssMatchTuples': ([XssMatchTuple], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-xssmatchtuples'),
        'Name': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html#cfn-wafregional-xssmatchset-name')
    }


# -------------------------------------------

class WAFRegionalByteMatchSet(AWSObject):
    """# AWS::WAFRegional::ByteMatchSet - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html",
    "Properties": {
        "ByteMatchTuples": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-bytematchtuples",
            "ItemType": "ByteMatchTuple",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "Name": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-name",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        }
    }
}
    """

    resource_type = "AWS::WAFRegional::ByteMatchSet"

    props = {
        'ByteMatchTuples': ([ByteMatchTuple], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-bytematchtuples'),
        'Name': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html#cfn-wafregional-bytematchset-name')
    }


# -------------------------------------------

class WAFRegionalWebACLAssociation(AWSObject):
    """# AWS::WAFRegional::WebACLAssociation - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html",
    "Properties": {
        "ResourceArn": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-resourcearn",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "WebACLId": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-webaclid",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        }
    }
}
    """

    resource_type = "AWS::WAFRegional::WebACLAssociation"

    props = {
        'ResourceArn': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-resourcearn'),
        'WebACLId': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html#cfn-wafregional-webaclassociation-webaclid')
    }


# -------------------------------------------

class WAFRegionalWebACL(AWSObject):
    """# AWS::WAFRegional::WebACL - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html",
    "Properties": {
        "DefaultAction": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-defaultaction",
            "Required": true,
            "Type": "Action",
            "UpdateType": "Mutable"
        },
        "MetricName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-metricname",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "Name": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-name",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "Rules": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-rules",
            "ItemType": "Rule",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::WAFRegional::WebACL"

    props = {
        'MetricName': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-metricname'),
        'DefaultAction': (Action, True, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-defaultaction'),
        'Rules': ([Rule], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-rules'),
        'Name': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html#cfn-wafregional-webacl-name')
    }


# -------------------------------------------

class WAFRegionalRule(AWSObject):
    """# AWS::WAFRegional::Rule - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html",
    "Properties": {
        "MetricName": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-metricname",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "Name": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-name",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        },
        "Predicates": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-predicates",
            "ItemType": "Predicate",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        }
    }
}
    """

    resource_type = "AWS::WAFRegional::Rule"

    props = {
        'MetricName': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-metricname'),
        'Predicates': ([Predicate], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-predicates'),
        'Name': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html#cfn-wafregional-rule-name')
    }


# -------------------------------------------

class WAFRegionalIPSet(AWSObject):
    """# AWS::WAFRegional::IPSet - CloudFormationResourceSpecification version: 1.4.0

    {
    "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html",
    "Properties": {
        "IPSetDescriptors": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-ipsetdescriptors",
            "ItemType": "IPSetDescriptor",
            "Required": false,
            "Type": "List",
            "UpdateType": "Mutable"
        },
        "Name": {
            "Documentation": "http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-name",
            "PrimitiveType": "String",
            "Required": true,
            "UpdateType": "Immutable"
        }
    }
}
    """

    resource_type = "AWS::WAFRegional::IPSet"

    props = {
        'IPSetDescriptors': ([IPSetDescriptor], False, 'Mutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-ipsetdescriptors'),
        'Name': (basestring, True, 'Immutable', 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html#cfn-wafregional-ipset-name')
    }


