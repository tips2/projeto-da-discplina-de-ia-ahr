from protoclass import proto


def make_fact(ctx, args, ask):
    for key in ctx:
        val = ctx[key]
        val.data = False
        val.seen = False
    for arg in args.data:
        if arg.data in ctx:
            val = ctx[arg.data]
            val.data = True
            val.seen = True
        else:
            ctx[arg.data] = proto(data=True, seen=True, rule=None)


def init_rule(ctx, lhs, rhs):
    # only and supported on right handside
    if rhs.kind == "atom":
        atom = rhs
        if atom.data in ctx:
            val = ctx[atom.data]
            if val.rule == None:
                val.rule = lhs
            else:
                val.rule = proto(kind="or", data=(lhs, val.rule))
        else:
            ctx[atom.data] = proto(data=False, seen=False, rule=lhs)
    elif rhs.kind == "and":
        init_rule(ctx, lhs, rhs.data[0])
        init_rule(ctx, lhs, rhs.data[1])
    else:
        assert False


def make_rule(ctx, args, ask):
    init_rule(ctx, args.data[0], args.data[1])


def eval_atom(ctx, atom, ask):
    if atom.data in ctx:
        val = ctx[atom.data]
        if val.seen:
            return val.data
        elif val.rule == None:
            return False
        else:
            val.seen = True
            val.data = eval_node(ctx, val.rule, ask)
            return val.data
    else:
        print("Answer Yes (y) or No (n):")
        
        val = input(ask[atom.data])
        
        assert val == "y" or val == "n", "You must answer Yes (y) or No (n)."
        
        val = True if val == "y" else False

        ctx[atom.data] = proto(data=val, seen=True, rule=None)

        return ctx[atom.data].data


def eval_not(ctx, arg, ask):
    return not eval_node(ctx, arg.data, ask)


def eval_and(ctx, arg, ask):
    return eval_node(ctx, arg.data[0], ask) and eval_node(ctx, arg.data[1], ask)


def eval_or(ctx, arg, ask):
    return eval_node(ctx, arg.data[0], ask) or eval_node(ctx, arg.data[1], ask)


def eval_xor(ctx, arg, ask):
    return eval_node(ctx, arg.data[0], ask) != eval_node(ctx, arg.data[1], ask)


NODE_DICT = {
    # stmt
    "make_fact": make_fact,
    "make_rule": make_rule,
    # expr
    "atom": eval_atom,
    "not": eval_not,
    "and": eval_and,
    "or": eval_or,
    "xor": eval_xor,
}


def eval_node(ctx, node, ask):
    return NODE_DICT[node.kind](ctx, node, ask)


def evaluate(ctx, tree, ask):
    return [eval_node(ctx, node, ask) for node in tree]
