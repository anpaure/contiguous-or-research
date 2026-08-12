# Explicit competitive-programming constructor for the \(\sqrt2\) bound

The program [construct_sqrt2_or.cpp](construct_sqrt2_or.cpp) takes a dimension
\(k\) and prints a nonzero mask word whose contiguous ORs contain every
nonzero \(k\)-bit mask.

## Compile and run

```bash
g++ -std=c++17 -O2 -pipe construct_sqrt2_or.cpp -o construct_sqrt2_or
echo 12 | ./construct_sqrt2_or --verify
```

Input is `k` followed optionally by a split `p`.  If `p` is omitted, the
program checks every split \(p+q=k\) and uses the one minimizing the proved
exact length.  Output is the length on the first line and the decimal masks
on the second line.

Useful modes:

```bash
echo 20 | ./construct_sqrt2_or --length-only
./construct_sqrt2_or --self-test 16
```

The implementation is output-explicit and deliberately capped at \(k=25\);
the output itself is exponential.

## Construction

Split the coordinates as \(P\dot\cup Q\), with \(|P|=p,|Q|=q\), and
distinguish one coordinate \(z\in P\).

1. Recursively generate a symmetric-chain decomposition of \(2^{P-\{z\}}\).
   Keep the long lifted child of each chain.  There are \(W(p-1)\) such
   chains.
2. Generate all \(W(q)\) symmetric chains of \(2^Q\).
3. Replace a chain \(C_0\subset\cdots\subset C_s\) by
   \[
   B(C)=[C_0,C_1\setminus C_0,\ldots,C_s\setminus C_{s-1},U\setminus C_s],
   \]
   deleting empty blocks.  Prefix ORs expose \(C\); suffix ORs expose its
   complement-dual chain.
4. Take an Euler circuit of the complete bipartite digraph containing both
   arcs between every left and right chain.  Write the bridge word of every
   visited vertex.  Each directed boundary supplies one chain rectangle.
5. Split a shortest right bridge between the two ends when cutting the Euler
   circuit into a linear word.

For a target \(S=X\cup Y\):

* if \(z\in X\), use the directed boundary from the lifted chain containing
  \(P\setminus X\) to the right chain containing \(Y\);
* if \(z\notin X\), use the reverse directed boundary from the right chain
  containing \(Q\setminus Y\) to the lifted chain containing \(X\).

The appropriate suffix followed by the appropriate prefix has OR exactly
\(S\).

## Exact length

Writing \(W(t)=\binom{t}{\lfloor t/2\rfloor}\), the emitted length is

\[
L_{CB}(p,q)=W(q)\bigl(2^{p-1}+2W(p-1)-2\bigr)
+W(p-1)\bigl(2^q+W(q)-2\bigr)+(q\bmod2).
\]

For a balanced split,

\[
L_{CB}(p,q)=(\sqrt2+o(1))W(k).
\]

The `--verify` path independently recomputes all suffix ORs in
\(O(kL_{CB})\) time and checks that all \(2^k-1\) targets occur.

