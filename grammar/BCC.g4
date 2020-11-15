/** Grammars always start with a grammar header. This grammar is called
 *  ArrayInit and must match the filename: ArrayInit.g4
 */
grammar BCC;

prog  : f* main_prog;

f     : 'function' FID ':' DATATYPE '(' (var_dec (',' var_dec)*)? ')' stmt_var_list? stmt_block;

    main_prog : stmt_var_list? stmt* 'end';

stmt_var_list : 'var' var_dec (',' var_dec)* ';';

var_dec : ID ':' DATATYPE ;

stmt_block : '{' stmt* '}'
            | stmt
            ;
stmt : PRINT lexpr ';'
      | INPUT ID ';'
      | WHEN par_lexpr do_block
      | IF par_lexpr do_block ELSE stmt_block
      | CICLE par_lexpr do_block
      | do_block CICLE2 par_lexpr
      | RETURN lexpr ';'
      | LOOP stmt_block
      | REPEAT  TK_NUM ':' stmt_block
      | FOR'(' lexpr ';' lexpr ';' assignation ')' do_block
      | NEXT ';'
      | BREAK ';'
      | assignation
      ;

assignation: ID ((OPERATION lexpr)|('++' | '--'))';'
            | ('--' | '++') ID ';'
            ;

do_block : 'do' stmt_block;

par_lexpr : '(' lexpr ')';

lexpr : nexpr ((AND nexpr) | (OR nexpr))*;

nexpr: NOT '(' lexpr ')'
      | rexpr;

rexpr: simple_expr (('<' | '==' | '<=' | '>' | '>=' | '!=') simple_expr)?;

simple_expr : term (('+' | '-') term)*;

term: factor (('*' | '/' | '%') factor)*;

factor: TK_NUM
      | TK_BOOL
      | ID ('++' | '--')
      | ('++' | '--') ID
      | ID
      | '(' lexpr ')'
      | FID '(' (lexpr (',' lexpr)*)? ')'
      ;

WS  :   [ \t\r\n]+ -> skip ; // Define whitespace rule, toss it out
COMMENT : '#' ~[\r\n]* -> skip ;
FID : '@' [a-zA-Z] [a-zA-Z_0-9]* ;
TK_NUM : [0-9]+;
OPERATION : (':=' | '+=' | '-=' | '*=' | '*=' | '/='| '%=');
PRINT : 'print';
INPUT : 'input';
WHEN : 'when';
IF    : 'if';
ELSE: 'else';
CICLE : ('unless' | 'while' | 'until');
CICLE2 : ('while' | 'until');
RETURN : 'return';
LOOP : 'loop';
REPEAT :'repeat';
FOR : 'for' ;
NEXT : 'next';
BREAK : 'break';
AND : 'and';
OR : 'or';
NOT : 'not';
TK_BOOL : ('true' | 'false');
DATATYPE : ('bool' | 'num');
ID  : [a-zA-Z] [a-zA-Z_0-9]*;