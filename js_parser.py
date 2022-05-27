import esprima
class JSParser(esprima.NodeVisitor):
    """Custom node visitor that focuses on one particular function call"""
    def __init__(self):
        self.found_sinks = []

    # # we only care for CallExpression nodes (i.e. function calls)
    # def visit_CallExpression(self, node):
    #     if (node.callee.name == 'sendMessage' and             # function name is `sendMessage`
    #         len(node.arguments) == 1 and                      # it should have 1 argument
    #         node.arguments[0].type == 'ObjectExpression' and  # which is an object
    #         len(node.arguments[0].properties) == 2 and        # which has two properties
    #         all((p.key.name in ['mode', 'delegatesFocus']     # which must have the expected names
    #             for p in node.arguments[0].properties))
    #     ):
    #         self.found_ranges.append(node.arguments[0].range)

    #     # visit everything else in the tree
    #     self.generic_visit(node)

    def visit_ObjectExpression(self,node):
        print("yes")