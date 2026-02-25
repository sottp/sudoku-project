#script (python)
def main(prg):
    ctx = prg.get_context()
    for fact in ctx.initial():
        prg.add("base", [], f"initial({fact.arguments[0]},{fact.arguments[1]},{fact.arguments[2]}).")
#end.
