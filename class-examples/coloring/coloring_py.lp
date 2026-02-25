color(X)  :- X = @color().
node(X)   :- X = @node().
edge(X,Y) :- (X,Y) = @edge().

node(X) :- edge(X,Y).
node(Y) :- edge(X,Y).