import sys

from gen.BCCVisitor import BCCVisitor
from gen.BCCParser import BCCParser


class MyVisitor(BCCVisitor):
    def __init__(self):
        self.functions = dict()
        self.variables = list()
        self.variables.append(dict())

    def printError(self, errorContext, flag):
        print("Error semantico:" + flag)
        sys.exit()

    # Visit a parse tree produced by BCCParser#prog.
    def visitProg(self, ctx: BCCParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#f.
    def visitF(self, ctx: BCCParser.FContext):
        self.functions[ctx.FID().getText()] = ctx
        return None

    # Visit a parse tree produced by BCCParser#main_prog.
    def visitMain_prog(self, ctx: BCCParser.Main_progContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#stmt_var_list.
    def visitStmt_var_list(self, ctx: BCCParser.Stmt_var_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#var_dec.
    def visitVar_dec(self, ctx: BCCParser.Var_decContext):
        self.variables[-1][ctx.ID().getText()] = False if ctx.DATATYPE().getText() == 'bool' else 0
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BCCParser#stmt_block.
    def visitStmt_block(self, ctx: BCCParser.Stmt_blockContext):
        for stmt in ctx.stmt():
            res = self.visitStmt(stmt)
            if res is not None:
                return res

    # Visit a parse tree produced by BCCParser#stmt.
    def visitStmt(self, ctx: BCCParser.StmtContext):
        if ctx.PRINT():
            print(self.visitLexpr(ctx.lexpr()[0]))
        elif ctx.INPUT():
            for context in self.variables[::-1]: 
                if ctx.ID().getText() in context:
                    context[ctx.ID().getText()] = input()
                    return None
            else:
                self.printError(ctx.ID(), "Variable no declarada")
        elif ctx.IF():
            ans = self.visitPar_lexpr(ctx.par_lexpr())
            if ans:
                return self.visitDo_block(ctx.do_block())
            else:
                return self.visitStmt_block(ctx.stmt_block())
        elif ctx.WHEN():
            ans = self.visitPar_lexpr(ctx.par_lexpr())
            if ans:
                return self.visitDo_block(ctx.do_block())

        elif ctx.CICLE():
            ans = self.visitPar_lexpr(ctx.par_lexpr())
            if ctx.CICLE().getText() == "unless":
                if not ans:
                    return self.visitDo_block(ctx.do_block())
            elif ctx.CICLE().getText() == "while":
                exit_loop = ""
                while ans and exit_loop != "break":
                    exit_loop = self.visitDo_block(ctx.do_block())
                    ans = self.visitPar_lexpr(ctx.par_lexpr())
                if type(exit_loop) is not str:
                    return exit_loop
            elif ctx.CICLE().getText() == "until":
                exit_loop = ""
                while not ans and exit_loop != "break":
                    exit_loop = self.visitDo_block(ctx.do_block())
                    ans = self.visitPar_lexpr(ctx.par_lexpr())
                if type(exit_loop) is not str:
                    return exit_loop
        elif ctx.CICLE2():
            self.visitStmt_block(ctx.do_block())
            ans = self.visitPar_lexpr(ctx.par_lexpr())
            if ctx.CICLE2().getText() == "while":
                exit_loop = ""
                while ans and exit_loop != "break":
                    exit_loop = self.visitDo_block(ctx.do_block())
                    ans = self.visitPar_lexpr(ctx.par_lexpr())
                if type(exit_loop) is not str:
                    return exit_loop
            elif ctx.CICLE2().getText() == "until":
                exit_loop = ""
                while not ans and exit_loop != "break":
                    exit_loop = self.visitDo_block(ctx.do_block())
                    ans = self.visitPar_lexpr(ctx.par_lexpr())
                if type(exit_loop) is not str:
                    return exit_loop
            else:
                if not ans:
                    self.visitDo_block(ctx.do_block())
        elif ctx.RETURN():
            return self.visitLexpr(ctx.lexpr()[0])
        elif ctx.LOOP():
            exit_loop = False
            while not exit_loop:
                if self.visitStmt_block(ctx.stmt_block()):
                    exit_loop = False
        elif ctx.REPEAT():
            for i in range(int(ctx.TK_NUM())):
                self.visitStmt_block(ctx.stmt_block())
        elif ctx.FOR():
            self.visitLexpr(ctx.lexpr(0))
            ran = self.visitLexpr(ctx.lexpr(1))
            exit_loop = False
            while ran and not exit_loop:
                exit_loop = self.visitDo_block(ctx.do_block())
                self.visitAssignation(ctx.assignation())
        elif ctx.BREAK():
            return "break"
        elif ctx.NEXT():
            return "next"
        else:
            self.visitChildren(ctx)
        return None

    # Visit a parse tree produced by BCCParser#assignation.
    def visitAssignation(self, ctx: BCCParser.AssignationContext):
        error = True
        for i in self.variables[::-1]:
            if ctx.ID().getText() in i:
                error = False
                if ctx.getChild(0) == ctx.ID():
                    if ctx.OPERATION():
                        ans = self.visitLexpr(ctx.lexpr())
                        if ctx.OPERATION().getText() == ":=":
                            i[ctx.ID().getText()] = ans
                        elif ctx.OPERATION().getText() == "+=":
                            i[ctx.ID().getText()] += ans
                        elif ctx.OPERATION().getText() == "-=":
                            i[ctx.ID().getText()] -= ans
                        elif ctx.OPERATION().getText() == "*=":
                            i[ctx.ID().getText()] *= ans
                        elif ctx.OPERATION().getText() == "/=":
                            i[ctx.ID().getText()] /= ans
                        elif ctx.OPERATION().getText() == "%=":
                            i[ctx.ID().getText()] %= ans
                    elif ctx.getChild(1).getText() == '++':
                        i[ctx.ID().getText()] += 1
                    elif ctx.getChild(1).getText() == '--':
                        i[ctx.ID().getText()] -= 1
                elif ctx.getChild(0).getText() == '++':
                    i[ctx.ID().getText()] += 1
                elif ctx.getChild(0).getText() == '--':
                    i[ctx.ID().getText()] -= 1
        if error:
            self.printError(ctx, "variable no delclarada")
        return

    # Visit a parse tree produced by BCCParser#do_block.
    def visitDo_block(self, ctx: BCCParser.Do_blockContext):
        return self.visitStmt_block(ctx.stmt_block())

    # Visit a parse tree produced by BCCParser#par_lexpr.
    def visitPar_lexpr(self, ctx: BCCParser.Par_lexprContext):
        return self.visitLexpr(ctx.lexpr())

    # Visit a parse tree produced by BCCParser#lexpr.
    def visitLexpr(self, ctx: BCCParser.LexprContext):
        res = self.visitNexpr(ctx.nexpr()[0])
        if len(ctx.nexpr()) > 1:
            for i in range(1, len(ctx.nexpr())):
                op2 = self.visitNexpr(ctx.nexpr()[i])
                if ctx.getChild(2*i-1).getText() == 'or':
                    res = res or op2
                else: 
                    res = res and op2
            return res
        else:
            return res

    # Visit a parse tree produced by BCCParser#nexpr.
    def visitNexpr(self, ctx: BCCParser.NexprContext):
        if ctx.lexpr():
            ans = self.visitLexpr(ctx.lexpr())
            return not ans
        elif ctx.rexpr():
            return self.visitRexpr(ctx.rexpr())

    # Visit a parse tree produced by BCCParser#rexpr.
    def visitRexpr(self, ctx: BCCParser.RexprContext):
        res = self.visitSimple_expr(ctx.simple_expr()[0])
        if len(ctx.simple_expr()) > 1:
            op2 = self.visitSimple_expr(ctx.simple_expr()[1])
            if ctx.getChild(1).getText() == '<':
                res = res < op2
            elif ctx.getChild(1).getText() == '==':
                res = res == op2
            elif ctx.getChild(1).getText() == '<=':
                res = res <= op2
            elif ctx.getChild(1).getText() == '>':
                res = res > op2
            elif ctx.getChild(1).getText() == '>=':
                res = res >= op2
            elif ctx.getChild(1).getText() == '!=':
                res = res != op2
            return res
        else:
            return res

    # Visit a parse tree produced by BCCParser#simple_expr.
    def visitSimple_expr(self, ctx: BCCParser.Simple_exprContext):
        res = self.visitTerm(ctx.term()[0])
        if len(ctx.term()) > 1:
            for i in range(1, len(ctx.term())):
                op2 = self.visitTerm(ctx.term()[i])
                if ctx.getChild(2*i-1).getText() == '+':
                    res = res + op2
                else: 
                    res = res - op2
            return res
        else:
            return res

    # Visit a parse tree produced by BCCParser#term.
    def visitTerm(self, ctx: BCCParser.TermContext):
        res = self.visitFactor(ctx.factor()[0])
        if len(ctx.factor()) > 1:
            for i in range(1, len(ctx.factor())):
                op2 = self.visitFactor(ctx.factor()[i])
                if ctx.getChild(2*i-1).getText() == '*':
                    res = res * op2
                elif ctx.getChild(2*i-1).getText() == '/':
                    res = res / op2
                elif ctx.getChild(2*i-1).getText() == '%':
                    res = res % op2
            return res
        else:
            return res

    # Visit a parse tree produced by BCCParser#factor.
    def visitFactor(self, ctx: BCCParser.FactorContext):
        if ctx.ID():
            for i in self.variables[::-1]:
                if ctx.ID().getText() in i:
                    if '+' in ctx.getText():
                        i[ctx.ID().getText()] += 1
                    if '-' in ctx.getText():
                        i[ctx.ID().getText()] -= 1
                    res = i[ctx.ID().getText()]
                    if '+' == ctx.getText()[-1]:
                        return res - 1
                    if '-' == ctx.getText()[-1]:
                        return res + 1
                    return res
            else: 
                self.printError(ctx, "Variable no delcarada")
        elif ctx.TK_NUM():
            return int(ctx.TK_NUM().getText())
        elif ctx.TK_BOOL():
            return ctx.TK_BOOL().getText() == 'true'
        elif ctx.FID():
            return self.run_func(self.functions[ctx.FID().getText()], ctx.lexpr())
        else:
            return self.visitLexpr(ctx.lexpr()[0])
        
    def run_func(self, ctx: BCCParser.FContext, args):
        self.variables.append(dict())
        i = 0
        if len(ctx.var_dec()) != len(args):
            self.printError(ctx, "la cantidad de argumentos de funcion no coinciden")
        for var_dec in ctx.var_dec():
            self.visitVar_dec(var_dec)
            self.variables[-1][var_dec.ID().getText()] = self.visitLexpr(args[i])
            i += 1
        res = self.visitStmt_block(ctx.stmt_block())
        self.variables.pop()
        return res

