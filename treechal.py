from collections import deque
from sqlparse.sql import TokenList

class SQLTokenVisitor:
    def visit(self, token):
        """Visit a token."""
        method = 'visit_' + type(token).__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(token)

    def generic_visit(self, token):
        """Called if no explicit visitor function exists for a node."""
        if not isinstance(token, TokenList):
            return
        for tok in token:
            print(tok)
            self.visit(tok)

def walk_tokens(token):
    queue = deque([token])
    while queue:
        token = queue.popleft()
        if isinstance(token, TokenList):
            queue.extend(token)
        yield token

