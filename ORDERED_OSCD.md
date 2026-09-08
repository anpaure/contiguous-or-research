# Ordering the standard/complement orthogonal SCD pair

This note audits one concrete version of the new global-chain program.  All
statements called theorems or propositions below are proved.  The conclusion is
negative but useful:

> The standard Greene--Kleitman symmetric-chain decomposition and its
> complement cannot be given the endpoint orders required by an interval-OR
> array.  For even dimension, the obstruction already occurs in the three
> ranks immediately surrounding the middle rank.

Consequently, adding empty chain slots to this pair is not a construction.  The
extra slots must be populated by split or reassigned pieces, and those pieces
must destroy explicit precedence cycles.

Throughout, the empty mask is omitted.  Thus the two longest chains of an
almost-orthogonal SCD pair cease to have their exceptional double intersection:
after deleting the empty mask they meet only in the full mask.  This is the
appropriate punctured-cube adjustment for the nonzero problem.

## 1. The incidence graph and its exact order obstructions

Let `D_k` be the standard Greene--Kleitman SCD of `2^[k]`.  In a bitstring, a
zero is an opening parenthesis and a one a closing parenthesis.  Parentheses are
matched in the usual way.  The successor in a Greene--Kleitman chain is obtained
by changing the leftmost unmatched zero to one.

Let

\[
 D_k^*=\{C^*:C\in D_k\},\qquad
 C^*=\{[k]\setminus S:S\in C\}.
\]

The order in `C*` is, of course, reversed.  The standard result of Shearer and
Kleitman says that `D_k,D_k^*` are almost orthogonal; on the punctured cube they
are orthogonal.

Define a bipartite graph `H_k` as follows.

* The left vertices are chains `C in D_k`.
* The right vertices are chains `R in D_k^*`.
* Every nonempty mask `S` is an edge

  \[
  e_S=C(S)R(S),
  \]

  where `C(S)` and `R(S)` are the unique chains containing `S`.
* The edge label is `|S|`.

Orthogonality says exactly that `H_k` is simple.  Under the natural
identification of a right vertex `C*` with `C`, its endpoints are

\[
 e_S:\quad C(S)\longleftrightarrow C(S^c)^* . \tag{1.1}
\]

Complementation sends `e_S` to `e_{S^c}` and swaps the two chain families.

### The two precedence digraphs

The desired endpoint orders can be tested without guessing the orders.

Define `P_R` on the right-chain vertices.  Whenever two consecutive masks
`S subset T` occur in one left chain, insert the arc

\[
 R(S)\longrightarrow R(T). \tag{1.2}
\]

Define `P_L` on the left-chain vertices.  Whenever two consecutive masks
`S subset T` occur in one right chain, insert the arc

\[
 C(T)\longrightarrow C(S). \tag{1.3}
\]

Only consecutive comparisons are needed, because their transitive closures
give every comparison in a chain.

### Proposition 1 (acyclicity criterion)

There is a linear order of the right chains in which their indices strictly
increase with rank along every left chain if and only if `P_R` is acyclic.
There is a linear order of the left chains in which their indices strictly
decrease with rank along every right chain if and only if `P_L` is acyclic.

#### Proof

Any such linear order respects every arc in (1.2), respectively (1.3), so a
directed cycle is impossible.  Conversely, a topological ordering of the
relevant precedence digraph has exactly the required property.  QED.

Appending isolated empty chain slots changes neither precedence digraph.
Therefore it can never repair a directed cycle.

## 2. A universal obstruction for every `k >= 3`

The parenthesis SCD is equivalent to the standard recursive SCD.  Its longest
chain is

\[
 P_k:\quad \varnothing,\{1\},\{1,2\},\ldots,[k]. \tag{2.1}
\]

For `k>=3` it also has the chain

\[
 Q_k:\quad \{k\},\{1,k\},\{1,2,k\},\ldots,
                 \{1,\ldots,k-2,k\}. \tag{2.2}
\]

Let `R_0=P_k^*`.  Thus `R_0` contains both `{k}` and `[k]`.

The suffix `T_j={2,3,...,j}` is the top of a standard chain in `D_j`.  This is
an immediate induction: `T_2={2}` is the top of its singleton chain, and the
long child of a chain with top `T_j` has top `T_j union {j+1}=T_{j+1}`.
Consequently `T_{k-1}` and `T_k` are consecutive in one chain `H_k`.  Put
`R=H_k^*`.  Their complements show that `R` contains both `{1}` and `{1,k}`.

Along the left chain `P_k`, the rank-one mask `{1}` lies in `R` and the full
mask lies in `R_0`.  Hence the desired right-chain order would require

\[
 R<R_0. \tag{2.3}
\]

Along the left chain `Q_k`, `{k}` lies in `R_0` and `{1,k}` lies in `R`.  Hence
it would also require

\[
 R_0<R. \tag{2.4}
\]

This proves the following.

### Theorem 2 (standard/complement no-order theorem)

For every `k>=3`, the standard Greene--Kleitman SCD and its complement do not
admit even the required right-chain order.  By complement symmetry they do not
admit the required left-chain order either.

The obstruction uses no empty mask.  Therefore deleting or moving the empty
mask, and inserting any number of empty placeholder chains, does not affect the
proof.

For `k=3` the complete picture is already visible:

\[
\begin{array}{c|c}
D_3&D_3^*\\ \hline
\varnothing,1,12,123&\varnothing,3,23,123\\
3,13&2,12\\
2,23&1,13
\end{array}
\]

The first left chain forces
`(1,13)<(2,12)<(3,23,123)`, while the second forces the last of these before
the first.

## 3. Exact fixed-central band geometry

The preceding theorem rules out the canonical pair before triangular support
is considered.  The triangular condition itself has an exact useful form.

Let `k=2m` and

\[
 W=\binom{2m}{m}.
\]

Take any two orthogonal SCDs, not necessarily the standard pair.  Every chain
contains a unique middle `m`-set.  Orthogonality makes the middle masks a
perfect matching between the two chain families, so label the matched chains

\[
 L_1,\ldots,L_W,\qquad R_1,\ldots,R_W,
\]

where `L_i cap R_i` contains the same middle mask `M_i`.

Fix `n=W+d` and impose the fixed-central witnesses

\[
 I_{M_i}=[i,i+d],\qquad 1\le i\le W. \tag{3.1}
\]

Here `L_i` is the chain of masks with left endpoint `i`, while `R_j` is the
chain of masks with physical right endpoint `j+d`.

### Theorem 3 (banded incidence theorem)

If `S in L_i cap R_j`, then its prescribed interval is

\[
 I_S=[i,j+d]. \tag{3.2}
\]

Moreover,

\[
\begin{array}{c|c}
|S|<m&1\le i-j\le d,\\
|S|=m&i=j,\\
|S|>m&i<j.
\end{array} \tag{3.3}
\]

#### Proof

Equation (3.2) follows from the definitions of the endpoint chains.  If
`|S|<m`, then in the left chain `L_i` its interval ends before the middle
interval `[i,i+d]`; hence `j<i`.  Nonemptiness of (3.2) gives `i<=j+d`.
This proves the first line.  Orthogonality and the unique middle member give
the second line.  If `|S|>m`, its right endpoint in `L_i` is later than that of
the middle member, so `j>i`.  QED.

Thus the lower incidence edges must fit in a directed bandwidth-`d` strip
strictly below the diagonal.  Acyclicity alone is not enough: a topological
order must also have the stated bandwidth.

### Exact capacity and the boundary correction

Let

\[
 L=\sum_{s=1}^{m-1}\binom{2m}{s},\qquad
 C=\binom{d+1}{2}. \tag{3.4}
\]

The pure `W`-chain band in (3.3) has

\[
 \sum_{h=1}^{d}(W-h)=dW-C \tag{3.5}
\]

cells.  In contrast, all physical intervals of lengths at most `d` in a word
of length `W+d` number

\[
 \sum_{q=1}^{d}(W+d-q+1)=dW+C. \tag{3.6}
\]

The difference is

\[
 2C=d(d+1). \tag{3.7}
\]

It consists of two boundary triangles, each of size `C`: intervals whose right
endpoint is at most `d`, and intervals whose left endpoint is greater than
`W`.  Such an interval uses an endpoint chain that is not among the `W`
middle-matched chains.

Define the usual arithmetic slack

\[
 \sigma=dW+C-L. \tag{3.8}
\]

### Corollary 4 (when empty slack chains cannot suffice)

A pure pair of `W` SCD chains in the fixed-central geometry is arithmetically
possible only if

\[
 L\le dW-C,
\]

or equivalently

\[
 \boxed{\sigma\ge d(d+1).} \tag{3.9}
\]

If this fails, at least

\[
 \boxed{d(d+1)-\sigma} \tag{3.10}
\]

lower masks must use the two boundary triangles.  Therefore some of the `d`
extra endpoint-chain slots must be populated by nonempty split pieces; merely
adding empty chains is impossible.

For example, at `k=6`, `W=20,d=1,L=21`, so `sigma=0`.  The pure band has only
19 cells and both boundary cells are forced.  This explains structurally why
the added slot cannot remain empty in a sharp construction.

At `k=14`, `W=3432,d=2,L=6475`, and `sigma=392>=6`, so this arithmetic test
does not rule out a pure SCD pair.  The precedence obstruction in Sections 2
and 5 still rules out the *standard/complement* pair.

## 4. The exact adjacent-middle reduction

The first lower and upper shadows have a particularly small normal form.

Identify every chain in each SCD with its unique middle `m`-set.  For a
rank-`m-1` mask `S`, let `X` be the middle member of its left chain and `Y` the
middle member of its right chain.  Then

\[
 S=X\cap Y,
\]

and `X,Y` are adjacent in the Johnson graph `J(2m,m)`.  Direct an edge
`X -> Y` and call the resulting digraph `F_-`.

Similarly, a rank-`m+1` mask `U` determines middle masks `X,Y` with

\[
 U=X\cup Y.
\]

Direct `X -> Y` and call this digraph `F_+`.

Orthogonality is essential here: it prevents the two middle centers from being
equal, since otherwise the same two chains would contain both the adjacent
mask and their middle mask.

### Proposition 5 (partial-permutation criterion)

Each of `F_-` and `F_+` has indegree and outdegree at most one.  Furthermore,

\[
 |E(F_-)|=|E(F_+)|=\binom{2m}{m-1}=W-\operatorname{Cat}_m, \tag{4.1}
\]

where

\[
 \operatorname{Cat}_m=\frac{1}{m+1}\binom{2m}{m}.
\]

There is an ordering putting all lower cells strictly below the diagonal if
and only if `F_-` is acyclic.  In that event `F_-` is a path forest with
exactly `Cat_m` components.

There is one order satisfying both adjacent ranks if and only if the precedence
digraph

\[
 \boxed{P_{\rm mid}=F_-^{\rm rev}\cup F_+} \tag{4.2}
\]

is acyclic.  A bandwidth-`d` fixed-central realization additionally requires

\[
 1\le \operatorname{pos}(X)-\operatorname{pos}(Y)\le d
 \quad\hbox{for every }X\to Y\in F_-. \tag{4.3}
\]

#### Proof

A left SCD chain contains at most one rank-`m-1` member, so every middle vertex
has outdegree at most one in `F_-`.  A right chain gives indegree at most one.
The same argument applies to `F_+`.  The edge count is the size of the
corresponding Boolean layer, and

\[
 \binom{2m}{m}-\binom{2m}{m-1}
 =\frac{1}{m+1}\binom{2m}{m}.
\]

A lower edge `X->Y` occupies cell `(X,Y)` and therefore requires `Y` before
`X`; this reverses `F_-`.  An upper edge requires `X` before `Y`.  Topological
ordering proves the two acyclicity equivalences.  An acyclic graph of maximum
indegree and outdegree one is a path forest, and its component count is
`W-(W-Cat_m)=Cat_m`.  Formula (4.3) is Theorem 3.  QED.

This corrects a tempting but insufficient target: proving only that the lower
incidence graph is a Catalan-component forest does **not** solve the ordering
problem.  It must be compatible with the oppositely oriented upper graph.

## 5. A central `2m`-cycle in the standard/complement pair

We now show that the canonical pair fails the exact criterion (4.2) for every
even `k>=4`, using only ranks `m-1,m,m+1`.

For intervals of coordinates write

\[
 [a,b]=\{a,a+1,\ldots,b\}.
\]

Define the following `2m` middle sets:

\[
 A_r=[r+1,r+m],\qquad 0\le r\le m-1, \tag{5.1}
\]

and

\[
 B_0=\{1\}\cup[m+1,2m-1], \tag{5.2}
\]

\[
 B_r=[1,r]\cup[m+r+1,2m],\qquad 1\le r\le m-1. \tag{5.3}
\]

All are distinct `m`-sets.

Let `tau` denote the Greene--Kleitman successor: flip the leftmost unmatched
zero.  An upper cell `X->Y`, with `U=X union Y`, is certified by

\[
 \tau(X)=U,\qquad \tau(U^c)=Y^c. \tag{5.4}
\]

Indeed, the first equation puts `U` above `X` in the standard chain, and the
second puts `U` above `Y` in the complement chain.

A lower cell `X->Y`, with `S=X cap Y`, is certified by

\[
 \tau(S)=X,\qquad \tau(Y^c)=S^c. \tag{5.5}

The following parenthesis checks are direct.

### Lemma 6 (the cycle cells)

For `0<=r<m-1`, there are upper cells

\[
 A_r\longrightarrow A_{r+1}. \tag{5.6}
\]

There is a lower cell

\[
 B_0\longrightarrow A_{m-1}. \tag{5.7}
\]

For `0<=r<m-1`, there are upper cells

\[
 B_r\longrightarrow B_{r+1}. \tag{5.8}
\]

Finally there is a lower cell

\[
 A_0\longrightarrow B_{m-1}. \tag{5.9}
\]

#### Proof

For (5.6), the bitstring of `A_r` is

\[
 0^r1^m0^{m-r}.
\]

Its leftmost unmatched zero is at position `r+m+1`.  If
`U=A_r union A_{r+1}`, then

\[
 U^c=1^r0^{m+1}1^{m-r-1},
\]

whose leftmost unmatched zero is at position `r+1`.  These are exactly the two
checks in (5.4).

For the transition `B_0->B_1`, the bitstring of `B_0` is

\[
 1\,0^{m-1}1^{m-1}0,
\]

whose leftmost unmatched zero is at `2m`.  The complementary lower word
`(B_0 union B_1)^c=0\,1^{m-1}0^m` has leftmost unmatched zero at `m+1`.
This proves (5.8) for `r=0`.

For `1<=r<m-1`, the bitstring of `B_r` is

\[
 1^r0^m1^{m-r},
\]

whose leftmost unmatched zero is at `r+1`.  For
`U=B_r union B_{r+1}`,

\[
 U^c=0^{r+1}1^{m-1}0^{m-r},
\]

whose leftmost unmatched zero is at `m+r+1`.  Again (5.4) holds.

For (5.7), put

\[
 S=B_0\cap A_{m-1}=[m+1,2m-1].
\]

The leftmost unmatched zero of `S` is position `1`, so `tau(S)=B_0`.
Moreover

\[
 A_{m-1}^c=[1,m-1]\cup\{2m\}
\]

has leftmost unmatched zero at `m`; adding it gives `S^c`.  This is (5.5).

For (5.9), put

\[
 S=A_0\cap B_{m-1}=[1,m-1].
\]

Its leftmost unmatched zero is at `m`, so `tau(S)=A_0`.  Also

\[
 B_{m-1}^c=[m,2m-1]
\]

has leftmost unmatched zero at `2m`, and adding it gives `S^c`.  This proves
(5.5).  QED.

Upper cells preserve their displayed orientation in the precedence digraph,
whereas lower cells reverse orientation.  Lemma 6 therefore forces

\[
 A_0<A_1<\cdots<A_{m-1}<B_0<B_1<\cdots<B_{m-1}<A_0. \tag{5.10}
\]

### Theorem 7 (central-cycle obstruction)

For every even `k=2m>=4`, the adjacent-middle precedence graph

\[
 F_-^{\rm rev}\cup F_+
\]

of the standard Greene--Kleitman SCD and its complement contains the explicit
directed `2m`-cycle (5.10).  Consequently, this pair cannot be made triangular
by any ordering of its middle-matched chains, for any bandwidth `d`.

This is stronger than Theorem 2 in the even case: the failure is already
present before ranks farther from the middle or pin survival are considered.

For `m=2`, the cycle is

\[
 12<23<13<14<12,
\]

where the first and third comparisons arise from upper masks and the other two
from lower masks with their orientation reversed.

## 6. What the minimal repair actually is

There are three distinct meanings of “add `d` chains,” and they must not be
confused.

1. **Empty placeholders.**  These only insert gaps into a proposed order.
   They do not change `P_L`, `P_R`, or (4.2), so they cannot break any cycle.

2. **Splitting a nonempty chain.**  A cut removes the rank comparison across
   that cut and places the two pieces in different endpoint slots.  This can
   break precedence cycles and can populate a boundary triangle.

3. **Reassigning masks between chains.**  This changes incidence edges and is
   the most general repair, but orthogonality and the chain property must be
   rechecked.

Theorem 2 shows that at least one nontrivial cut or reassignment is required in
each endpoint decomposition: cuts only in the left family cannot remove a
cycle generated inside right chains, and vice versa.  Theorem 7 shows that in
even dimension at least one of the `2m` explicit adjacent-middle incidences in
Lemma 6 must change.  Corollary 4 can force still more: at least
`d(d+1)-sigma` lower masks must use split boundary pieces whenever that number
is positive.

These are necessary repairs, not a claim that one cut per family is globally
sufficient.  In fact, the correct remaining problem is:

> Starting from an orthogonal chain pair, use the `d` extra slots as nonempty
> split pieces so that `P_L` and `P_R` become acyclic, the adjacent-middle
> digraph (4.2) becomes acyclic with lower bandwidth at most `d`, every mask
> lies in the triangular support, and the coordinatewise pin-survival
> conditions hold.

The standard/complement pair remains a useful algebraic seed, but the phrase
“order it and add `d` empty chains” is false.

## 7. Consequences for the broader program

The useful part of the orthogonal-SCD idea survives in a sharper form.

* Orthogonality converts masks into distinct cells.
* The adjacent lower layer is a partial permutation and, when acyclic, a
  Catalan-component path forest.
* Equality near the Boolean width is a **banded simultaneous topological-order
  problem**, not merely an SCD existence problem.
* The `d` slack chains have a concrete job: they are split endpoint pieces
  that break cycles and supply the two missing boundary triangles.
* Even after the ordered triangular incidence problem is solved, pin survival
  remains an independent coordinatewise condition.

The next mathematical target should therefore be an operation on orthogonal
SCD pairs that breaks the mixed cycles in `F_-^{rev} union F_+` while preserving
orthogonality and controlling the number of new pieces.  A theorem that does
this with at most `B(k)-W(k)` pieces per side would be materially closer to the
conjecture than another abstract existence theorem for unordered orthogonal
SCDs.

## References used for the standard facts

* Hunter Spink, [Orthogonal Symmetric Chain Decompositions of
  Hypercubes](https://arxiv.org/abs/1706.08545).
* Karl Däubel, Sven Jäger, Torsten Mütze, and Manfred Scheucher,
  [On orthogonal symmetric chain
  decompositions](https://arxiv.org/abs/1810.09847).
* The parenthesis description and recursive equivalence of the
  Greene--Kleitman SCD are standard; a convenient explicit account is in
  [Venn Diagrams and Symmetric Chain Decompositions in the Boolean
  Lattice](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v11i1r2).

