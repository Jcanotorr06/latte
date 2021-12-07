import re
import sys, os
import ply.lex as lex

error_semantic = 0
error_syntax  = 0

reserved = ('IF', 'ELSE', 'WHILE', 'PRINT', 'ANDALSO', 'ORELSE', 'NOT', 'IN', 'MOD')
tokens = reserved + (
    # >, >=, <>, ==, <=, <, andalso, orelse, ~, ::, member
    'ID', 'GREATER', 'GREATEREQUAL', 'NOTEQUAL', 'EQUAL',         
    'LESSEQUAL', 'LESSTHAN',   
     'CONS', 
    #+, -, %, /, int div, *, **
    'MINUS', 'PLUS', 'INTDIV', 'DIV', 
    'MUL', 'EXPONENT', 

    #[ ], #, ( )
    'LBRACKET', 'RBRACKET', 'TUPLINDEX', 'LPAREN','RPAREN', 'LCURLY', 'RCURLY',     

    #data types
    'INT', 'REAL', 'STRING', 'BOOL',
    #;
    'SEMI', 'COMMA',
    'ASSIGN',
)




