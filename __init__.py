import ast
from ast import *
from .api import *
from .constants import *
from .object import *
import pyperclip
import os
import gzip
import base64

async def do_send(final):
    import websockets
    async with websockets.connect("ws://localhost:31371") as socket:
        dumped = json.dumps(final)
        zipped = gzip.compress(dumped.encode())
        b = base64.b64encode(zipped).decode()
        template = {
            "data": json.dumps({
                "author": "PyToDF",
                "name": "PyToDF Generated Template",
                "data": b
            }),
            "type": "template",
            "source": "PyToDF"
        }
        json_dat = json.dumps(template)
        await socket.send(json_dat)


def get_const(node, default, top=True):
    if type(node) == Constant:
        return node.value
    if type(node) == Name:
        return node.value.id
    if type(node) == Attribute:
        if type(node.value) == Attribute:
            return ConstantDict.get(get_const(node.value, default) + "." + node.attr, default, False)
        if type(node.value) == Name:
            if top:
                return ConstantDict.get(node.value.id + "." + node.attr, default)
            else:
                return node.value.id + "." + node.attr
        if type(node.value) == Constant:
            if top:
                return ConstantDict.get(node.value + "." + node.attr, default)
            else:
                return node.value + "." + node.attr

class RunManager(NodeVisitor):
    def __init__(self):
        self.outputs = []

    def visit_Module(self, node):
        for item in node.body:
            self.visit(item)
        return self.outputs

    def visit_FunctionDef(self, node):
        func_name = node.name
        body = node.body
        first_dec = node.decorator_list[0]
        decorator: Name | Call = ("", ())
        if type(first_dec) == Name:
            # A decorator without ()
            decorator = (first_dec.id, ())
        elif type(first_dec) == Call:
            decorator = (first_dec.func.id, tuple(get_const(arg, "ERROR") for arg in first_dec.args))
        self.outputs.append(("fdef", func_name, decorator))
        for item in body:
            self.visit(item)

    def visit_Expr(self, node):
        if type(node) == Call:
            # function call
            pass


def execute(tree: list, obj_list: list):
    for item in tree:
        i_type = item[0]
        if i_type == "fdef":
            # fdef, DEC_TYPE, NAME, DEC_ARGS
            if item[1] == "function":
                obj_list.append(Object(
                    block=Code.B_FUNCTION,
                    items=[get_const(item[3], "lapis_lazuli")],
                    data=item[2]
                ))
            elif item[1] == "process":
                obj_list.append(Object(
                    block=Code.B_PROCESS,
                    items=[get_const(item[3], "emerald")],
                    data=item[2]
                ))
            elif item[1] == "playerEvent":
                obj_list.append(Object(
                    block=Code.B_EVENT,
                    action=get_const(item[3], PlayerEvent.JOIN)
                ))
            elif item[1] == "entityEvent":
                obj_list.append(Object(
                    block=Code.B_ENTITY_EVENT,
                    action=get_const(item[3], EntityEvent.DEATH)
                ))
            else:
                print(f"unknown decorator: {item[1]}({item[3]})")


def run(file, output=None, send=True):
    """
    "Run" or transpiles the code into DiamondFire templates

    Parameters:
        file - The file to parse
        output - The file to write to, defaults to clipboard
        send - Whether to send the templates to recode

    No examples
    """
    with open(file) as f:
        code = f.read()
    obj_list = []
    tree = ast.parse(code)
    print(ast.dump(tree, indent=4))
    rmanager = RunManager()
    print(rmanager.visit(tree))
    """
    final = {"blocks": [i.to_dict() for i in obj_list]}
    dumped = json.dumps(final, indent=2)
    if output:
        if os.path.exists(output):
            with open(output, "w") as f:
                f.write(dumped)
        else:
            with open(output, "x") as f:
                f.write(dumped)
    else:
        print(dumped)
        pyperclip.copy(dumped)
    if send:
        import asyncio
        asyncio.run(do_send(final))
    """
