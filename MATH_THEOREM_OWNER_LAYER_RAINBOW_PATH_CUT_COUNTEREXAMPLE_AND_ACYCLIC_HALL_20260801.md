# The fixed-owner gate is a coloured directed Hamilton path: exact cuts,
# a protected counterexample, and an acyclic Hall completion theorem

Date: 2026-08-01  
Lane: owner/up/tail/head/graphic correlation  
Status: exact reduction, exact counterexamples, and an exact sufficient
Hall theorem.  Existence of the required Boolean Catalan forest remains
open.

## 0. Outcome

Fix a perfect matching `M_0` in the middle-levels incidence graph between

\[
 \mathcal L={[2m-1]\choose m-1},\qquad
 \mathcal M={[2m-1]\choose m},\qquad |\mathcal L|=|\mathcal M|=W.
\]

The remaining owner-layer object is exactly a colour-covering directed
Hamilton path in a canonical digraph `D_(M_0)`.  This gives a complete
integer cut formulation of the joint tail, head, upper-colour and graphic
conditions.

Two facts sharpen its scope.

1. The protected upper-tail extension theorem cannot be strengthened to
   head injectivity for arbitrary `t<=m` tickets: two legal tickets can
   force the same head.
2. Even distinct heads and an acyclic protected directed linear forest are
   insufficient.  At `m=3` there are three clean protected arcs which do
   not extend to **any** Hamilton path for their fixed `M_0`, independently
   of upper-colour coverage.

Thus the protected pivot bank and `M_0` must be chosen in correlation; the
number `t<=m` alone carries no protected Hamilton-extension theorem.

There is also a positive exact reduction.  Once an upper-exact rooted
Catalan forest `Q_0` is chosen, if its free-port connector reservoir has an
acyclic component subgraph, then the full connector/tree problem is exactly
the one-defect Hall condition

\[
                         |N(X)|\ge |X|-1.             \tag{0.1}
\]

This is a genuine min--max theorem: on an acyclic reservoir, head
injectivity and spanning topology no longer have to be solved separately.

The split-pivot lower-`q1` native-address deficits enter this note only as
protected tickets.  No compiler, residence, or arbitrary-width assertion is
made.

## 1. The canonical coloured digraph

For an incidence `e=LV` outside `M_0`, define

\[
 \lambda(e):L\longrightarrow M_0^{-1}(V),\qquad
 \operatorname {up}(e)=M_0(L)\cup V.                 \tag{1.1}
\]

Let `D_(M_0)` have vertex set `mathcal L` and one arc `lambda(e)` for every
such incidence.  Colour the arc by `up(e)`.

Every vertex has outdegree and indegree `m-1`.  Indeed, a lower set `L` is
contained in exactly `m` middle sets, one used by `M_0`; dually, a fixed
middle set contains `m` lower sets, one equal to its `M_0` preimage.  The
underlying graph is connected: contract all `M_0` edges in the connected
middle-levels graph.  Since the digraph is balanced and weakly connected,
it is strongly connected.

Raw connectivity is therefore not the issue.  Port restrictions and colour
coverage are.

### Theorem 1.1 (rainbow-path equivalence)

A set `Q subseteq ML_m-M_0` is an upper-surjective alternating Hamilton
path shore if and only if its arcs in `D_(M_0)` form a directed Hamilton
path and

\[
       \{\operatorname {up}(e):e\in Q\}
                    ={[2m-1]\choose m+1}.             \tag{1.2}
\]

A protected upper-tail ticket `(R,T)` fixes one arc: put

\[
 L=M_0^{-1}(T),\qquad R=T\cup\{b\},
\]

write `T=L union {a}`, and take

\[
                 e=L\,(L\cup\{b\}).                  \tag{1.3}
\]

Thus protected tickets are literal forced arcs, not merely forced colours.

#### Proof

Tail injectivity is outdegree at most one in `D_(M_0)` and head injectivity
is indegree at most one.  Contracting the `M_0` edges turns the alternating
incidence path into its directed rooted-link path.  The adjacent owner
union at the lower turn `L` is exactly `M_0(L) union V=up(e)`.  These
observations prove both directions and (1.3).  \(\square\)

## 2. Exact integer cut formulation

Let `E` be the arc set of `D_(M_0)`, let `P subseteq E` be a protected bank,
and introduce binary variables `x_e`.  For `S subseteq mathcal L`, write
`E[S]` for arcs whose two rooted endpoints both lie in `S` (directions
forgotten only in this notation).

### Theorem 2.1 (complete owner-layer cut system)

There is an upper-surjective Hamilton path containing `P` if and only if
the following binary system is feasible:

\[
 \begin{aligned}
 &x_e=1 &&(e\in P),\\
 &\sum_{e\in\delta^+(v)}x_e\le1,
 &&\sum_{e\in\delta^-(v)}x_e\le1 &&(v\in\mathcal L),\\
 &\sum_{e\in E}x_e=W-1,\\
 &\sum_{e:\operatorname {up}(e)=R}x_e\ge1
 &&\left(R\in{[2m-1]\choose m+1}\right),\\
 &\sum_{e\in E[S]}x_e\le |S|-1
 &&(\varnothing\ne S\subseteq\mathcal L).
 \end{aligned}                                       \tag{2.1}
\]

#### Proof

A Hamilton path plainly satisfies all rows.  Conversely, the last family
says that the selected rooted links are graphic-independent, including the
two-arc parallel cycle obtained by choosing opposite directions between one
pair.  There are `W` vertices and `W-1` selected links, so this forest is a
spanning tree.  The two degree rows give indegree and outdegree at most one;
hence the tree has undirected maximum degree at most two and is a directed
spanning path.  The colour rows are exactly upper surjectivity.  \(\square\)

This system is exact but not an ordinary matroid-intersection theorem.  The
family of directed linear forests already fails the matroid exchange axiom.
On vertices `1,2,3,4`, both

\[
 I=\{1\to2,,3\to4\},\qquad
 J=\{1\to3,,3\to2,,2\to4\}                         \tag{2.2}
\]

are directed linear forests and `|I|<|J|`, but no edge of `J-I` can be
added to `I`: the three additions respectively repeat outgoing port `1`,
repeat outgoing `3`/incoming `2`, and repeat incoming port `4`.  Therefore
no Rado or matroid-rank formula follows merely by naming the tail, head and
graphic rows separately.

## 3. Two exact protected obstructions at `m=3`

Use ground set `[5]` and abbreviate a set by its digits.  Name the ten
rank-two vertices

\[
 \begin{array}{c|cccccccccc}
 v&A&B&C&D&E&F&G&H&I&J\\ \hline
 L_v&12&13&23&14&24&34&15&25&35&45.
 \end{array}                                         \tag{3.1}
\]

Fix the perfect matching

\[
 \begin{array}{c|cccccccccc}
 v&A&B&C&D&E&F&G&H&I&J\\ \hline
 M_0(L_v)&123&134&234&124&245&345&125&235&135&145.
 \end{array}                                         \tag{3.2}
\]

The twenty arcs of `D_(M_0)`, with their upper colours, are

\[
\begin{array}{c|cc}
A&D:1234&G:1235\\
B&A:1234&I:1345\\
C&A:1234&H:2345\\
D&B:1234&J:1245\\
E&D:1245&C:2345\\
F&B:1345&C:2345\\
G&I:1235&J:1245\\
H&G:1235&E:2345\\
I&H:1235&F:1345\\
J&E:1245&F:1345.
\end{array}                                          \tag{3.3}
\]

Every entry follows directly from (1.1), so the examples below are
human-checkable without search.

### Proposition 3.1 (two upper-tail tickets can force one head)

The tickets

\[
                 (1234,123),\qquad(1245,245)          \tag{3.4}
\]

have distinct upper colours and distinct rooted tails and satisfy `t=2<=m`.
They force the arcs `A->D` and `E->D`, respectively.  Their heads coincide,
so no head-injective extension exists.

This is the smallest semantic reason Theorem 2.2 of the rooted-tail note is
only a semimatching theorem.

### Proposition 3.2 (a clean protected forest need not extend)

The protected set

\[
                  P=\{A\to D,,C\to H,,J\to F\}     \tag{3.5}
\]

has three distinct tails, three distinct heads and three distinct upper
colours `1234,2345,1345`.  Its underlying graph is three disjoint edges, so
it is a directed linear forest.  Nevertheless, no Hamilton path of
`D_(M_0)` contains `P`.

#### Proof

The occupied heads `D,H,F` forbid the other incoming arcs

\[
                       E\to D,quad I\to H,quad I\to F. \tag{3.6}
\]

Both outgoing arcs of `I` are now forbidden, so `I` must be the unique
terminal vertex of any extension.

Vertex `E` is not terminal and only `E->C` remains, so that arc is forced.
Head `C` is then occupied; because `F` is not terminal, `F->B` is forced.
Head `B` is occupied; because `D` is not terminal, `D->J` is forced.  We
now have the chain

\[
                       A\to D\to J\to F\to B.         \tag{3.7}
\]

The choice `B->A` would close this chain into a cycle, so `B->I` is forced.
Likewise `H->E` would close the cycle

\[
                       E\to C\to H\to E,
\]

and therefore `H->G` is forced.  But the two possible heads of `G` are
`I` and `J`, already occupied by `B->I` and `D->J`.  This is impossible.
\(\square\)

Consequently even the strengthened local hypotheses

\[
 \boxed{\text{distinct tails + distinct heads + distinct colours
               + protected acyclicity}}              \tag{3.8}
\]

do not imply protected extension for an arbitrary fixed `M_0` at the
nominal threshold `t<=m`.

## 4. Exact acyclic connector Hall theorem

The counterexample does not prevent a useful positive reduction after the
upper representatives have been selected.

Let `Q_0` be an upper-exact rooted Catalan forest: `up` is a bijection on
its `U=W-C` edges, `Q_0` is a matching, and `lambda(Q_0)` is a forest.  Its
`C` components are coherently directed paths.  Each component `K` has one
free outgoing port `o(K)` and one free incoming port `i(K)`.

Let `mathcal A` be any collection of admissible connector incidences from
`o(K)` to `i(K')`, with `K!=K'`, such that its component digraph is acyclic.
Make a bipartite graph `H_mathcalA` with one outgoing and one incoming copy
of every component and the corresponding connector edges.

### Theorem 4.1 (one-defect Hall is exact on an acyclic reservoir)

The forest `Q_0` extends using `C-1` edges of `mathcal A` to an
upper-surjective rooted Hamilton path if and only if

\[
              |N_{H_\mathcal A}(X)|\ge |X|-1
              \qquad(X\subseteq\operatorname {Comp}(Q_0)).       \tag{4.1}
\]

Equivalently,

\[
 \nu(H_\mathcal A)=C-1,\qquad
 C-\nu(H_\mathcal A)
   =\max_X\bigl(|X|-|N_{H_\mathcal A}(X)|\bigr)=1.   \tag{4.2}
\]

#### Proof

The deficiency form of Hall gives (4.2), so (4.1) is equivalent to a
matching of size at least `C-1`.  An acyclic component digraph cannot contain
a perfect matching: a selected indegree-one/outdegree-one spanning
subgraph would be a union of directed cycles.  Hence its matching number is
at most `C-1`, and (4.1) gives exactly that size.

The selected connector matching gives every component indegree and
outdegree at most one.  It has no directed cycle because it lies in
`mathcal A`.  Under these degree bounds an undirected cycle would
necessarily be coherently directed, so none exists.  The selected graph is
therefore a disjoint union of directed paths.  It has `C` vertices and
`C-1` edges, hence exactly one component: a directed Hamilton path.  The
converse is immediate.  \(\square\)

### Forced connector version

If a protected connector set is already a directed path forest on the
`Q_0` components, contract each protected path.  Delete its used incoming
and outgoing port copies and retain only candidate connectors which do not
create a directed cycle with the protected paths.  If the resulting
component reservoir is acyclic, Theorem 4.1 applies verbatim to the
contracted components.  Its one-defect Hall inequalities are therefore an
exact protected completion certificate.

This is stronger than checking ordinary graphic rank and port Hall
separately: acyclicity makes the graphic row automatic for every selected
matching, and (4.1) then handles all port choices simultaneously.

## 5. Finite evidence, kept separate from the proofs

Two small exhaustive C++ replays were run on the remote CPU host.

* At `m=3`, all `60` perfect matchings `M_0` admit at least one unprotected
  upper-surjective Hamilton path.
* Across those `60` matchings, among `37,440` protected sets of at most
  three arcs having distinct tails, heads and upper colours and forming an
  undirected forest, `480` do not extend to an upper-surjective Hamilton
  path.  The explicit set (3.5) is one of them.
* For the particular `M_0` in (3.2), there are `40` directed Hamilton paths
  in `D_(M_0)` and none contains (3.5).

These counts are evidence and regression checks only.  Propositions
3.1--3.2 have the independent literal proofs above.

## 6. Revised exact frontier

The protected upper-tail Hall theorem remains useful but cannot be upgraded
by adding only the words “heads distinct” or “protected forest.”  The
correct all-dimensional target must jointly choose `M_0`, the protected
ticket phases, and the upper representatives.

A proof-safe sufficient route is now:

1. choose a head-injective upper-exact rooted Catalan forest `Q_0`
   containing the protected representative tickets;
2. expose an acyclic free-port connector reservoir on its `C` components;
3. prove the one-defect Hall inequalities (4.1), after contracting any
   forced connector paths.

Steps 2--3 then give the spanning rooted-link path exactly.  The unresolved
central correlation is concentrated in Step 1 and in construction of the
acyclic Hall-expanding connector reservoir; it is not an ordinary extension
property of arbitrary protected tickets.

## 7. Finite replay artifacts

The finite counts in Section 5 were produced on the remote CPU host by the
following frozen artifacts:

* `scratch/audit_m3_fixed_m0_upper_hamilton_20260801.cpp`,
  SHA `1f33d41065c6612549d3c166d4308535f7535cb95a9d4527b1543ca28e976dbe`;
  result transcript `.err`,
  SHA `19457891f869a8686073487d9ee12d3bcedff447ce5ee22c9fd31ab734577bb2`;
* `scratch/audit_m3_protected_upper_path_extension_20260801.cpp`,
  SHA `05eb3c0b9b17e205d8146e52e0513f7022a79385ae6c44b2424ad7d52d204879`;
  summary `.err`, SHA
  `a143ace846efb978792fa2ed09b58ef1d518cf7e827a0099282fcae0994d0656`;
* `scratch/replay_m3_protected_counterexample_paths_20260801.cpp`,
  SHA `4433077c18915f5da7bc0264bbdcb2c42fd24abc33b7edacf67186e489c9db35`;
  result `.err`, SHA
  `c20f050862b13c40918367cf24d9ad9e40350ac68dcbfda3471a2ce74e570978`.

The literal proof of Proposition 3.2 is authoritative; the exhaustive
replays are not used to establish it.
