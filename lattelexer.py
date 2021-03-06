import re
import sys, os
import ply.lex as lex

error_semantic = 0
error_syntax  = 0

reserved = ('IF', 'ELSE', 'WHILE', 'PRINT', 'ANDALSO', 'ORELSE', 'NOT', 'IN')
tokens = reserved + (
    'ID', 'GREATER', 'GREATEREQUAL', 'NOTEQUAL', 'EQUAL',         
    'LESSEQUAL', 'LESSTHAN','CONC', 'MINUS', 'PLUS', 'INTDIV', 'DIV', 'MOD',
    'MUL', 'EXPONENT', 'LBRACKET', 'RBRACKET', 'TUPLINDEX', 'LPAREN',
    'RPAREN', 'LCURLY', 'RCURLY', 'INT', 'REAL', 'STRING', 'BOOL',
    'SEMI', 'COMMA', 'ASSIGN',
)

t_ASSIGN           = r'='
t_COMMA            = r','
t_GREATER          = r'>'   
t_GREATEREQUAL     = r'>='    
t_NOTEQUAL         = r'<>'  
t_EQUAL            = r'==' 
t_LESSEQUAL        = r'<=' 
t_LESSTHAN         = r'<' 
t_CONC             = r'::' 
t_MINUS            = r'-' 
t_PLUS             = r'\+' 
t_INTDIV           = r'div' 
t_DIV              = r'/'
t_MOD              = r'\%' 
t_MUL              = r'\*' 
t_EXPONENT         = r'\*\*' 
t_LBRACKET         = r'\[' 
t_RBRACKET         = r'\]' 
t_LCURLY           = r'\{'
t_RCURLY           = r'\}'
t_TUPLINDEX        = r'\#'
t_LPAREN           = r'\(' 
t_RPAREN           = r'\)'
t_SEMI             = r';'
t_ignore           = ' \t'


def t_REAL(t):
    r'[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_STRING(t):
     r'(\"([^\"]|(\\.))*\")|((\'([^\"]|(\\.))*\'))'
     return t

def t_BOOL(t):
    r'True|False'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t
    
def t_error(t):
    error_syntax = 1
    return

lex.lex(debug = 0)

if __name__ == '__main__':
    lex.runmain()


