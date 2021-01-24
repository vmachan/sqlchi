import os
import sqlparse
from sqlparse import tokens
import treechal as tc

def get_selected_columns(s):
    # get selected column names from input sql s
    None
    
def chal_node(n, d):
    if hasattr(n, 'tokens'):
        for t in n.tokens:
            chal_node(t, d+1)
    else:
        return n

def print_node(n, d):
    if hasattr(n, 'tokens'):
        for t in n.tokens:
            print_node(t, d+1)
    else:
        print(' ' * d, n, "--", n.ttype)

in_sql_file = open("test.sql")
in_sql_str = in_sql_file.read().replace('\n', '').replace('  ', ' ')

parsed_sql = sqlparse.parse(in_sql_str)

for sql_stmt in parsed_sql:
    # print("********** SQL STATEMENT-->", sql_stmt)
    for parsed_sql_token in sql_stmt.tokens:
        if (
                parsed_sql_token.ttype != tokens.Token.Text.Whitespace 
            and parsed_sql_token.ttype != tokens.Token.Text.Whitespace.Newline
           ):
            # print("********** TOKEN-->", parsed_sql_token, " -- TTYPE-->", parsed_sql_token.ttype)
            print_node(parsed_sql_token, 0)
      


