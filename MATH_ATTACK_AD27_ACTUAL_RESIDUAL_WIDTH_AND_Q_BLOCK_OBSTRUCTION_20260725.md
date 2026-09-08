# AD27: actual one-bite residual width and the bounded-\(Q\)-block obstruction

Date: 2026-07-25

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Verdict

Let

\[
 W=\binom{2m}{m},\qquad 1\le Q<H\le m.
\]

After one owner-scale bite, let \(s\) be the number of distinct middle
owners already used.  The **actual** residual hole family \({\cal H}\),
not the donor family, satisfies

\[
 \boxed{W-s\le \operatorname{width}({\cal H})\le W.}
 \tag{0.1}
\]

For either owner-scale normalization currently in use,

\[
 s=O(W/m),
 \tag{0.2}
\]

and hence

\[
 \boxed{\operatorname{width}({\cal H})=W-O(W/m).}
 \tag{0.3}
\]

Thus the actual one-bite residual is not a sparse reserve.  The small
width of the withheld donor strings has no bearing on (0.3).

There is nevertheless no vertical integrality obstruction: every chain
partition of \({\cal H}\) extends, chain by chain, to exact saturated
radius-\(Q\) state columns.  In particular, \({\cal H}\) has an integral
column cover by at most \(W\) exact quotient states.

The obstruction is horizontal and quantitative.  Suppose such a column
cover is compiled into independently initialized genuine rotor paths, and
suppose every path has at most \(CQ\) state endpoints, where \(C>0\) is
fixed.  Then its exact length is at least

\[
 \boxed{
 (W-s)+(2Q+1)
 \left\lceil {W-s\over CQ}\right\rceil
 \ge \left(1+{2\over C}-o(1)\right)W.}
 \tag{0.4}
\]

Consequently a literal bounded-\(O(Q)\)-length block cover cannot give
coefficient one.  If instead the phrase ``\(O(Q)\)-phase block cover'' is
intended to mean a path-count estimate

\[
 p=O(B/Q),
 \tag{0.5}
\]

then (0.5) is sufficient only when the number \(B\) of reserve columns is
\(o(W)\).  Here \(B\ge W-s=(1-o(1))W\), so (0.5) gives only an
\(O(W)\) reset toll.  The exact coefficient-one target after one bite is

\[
 \boxed{p=o(W/Q),}
 \tag{0.6}
\]

equivalently average genuine rotor-run length \(\omega(Q)\).

The grid-strip formulas give the exact successor relation.  If
\(S_0\subset\cdots\subset S_{2Q}\) is one saturated band column, then a
successor column \(T_0\subset\cdots\subset T_{2Q}\) must have one common
arrival label \(y\) and one bottom exchange label \(x\):

\[
 \boxed{
 T_0=S_0-x+y,\qquad
 T_h=S_{h-1}+y\quad(1\le h\le2Q).}
 \tag{0.7}
\]

This is both necessary and sufficient, with the evident membership
conditions and a common carrier.  It shows why separate-rank expansion or
small residual density does not prove the required horizontal Hall
condition: all \(2Q+1\) ranks must use the same \(y\).

No claim is made here that the actual one-bite residual either satisfies
or violates (0.6).  The report proves the exact width, closes vertical
state realization, and rules out the bounded-\(O(Q)\)-length
interpretation sharply.

## 1. Setup and the exact middle residual

Let

\[
 {\cal H}_r\subseteq\binom{[2m]}{m+r},
 \qquad -Q\le r\le Q,
 \tag{1.1}
\]

be the targets not covered after one bite, and put

\[
 {\cal H}=\bigcup_{r=-Q}^{Q}{\cal H}_r.
 \tag{1.2}
\]

Assume only that the bite uses \(s\) mutually distinct middle owners.
This is an exact property of the audited owner-scale bites.  Therefore

\[
 |{\cal H}_0|=W-s.
 \tag{1.3}
\]

For a bite consisting of \(K\) owner-disjoint trajectories with \(L_i\)
physical state endpoints,

\[
 s=\sum_{i=1}^{K}L_i.
 \tag{1.4}
\]

There is no estimate involving duplicate or withheld off-middle claims in
(1.3).

For the full-carrier owner-scale bite one may trim to

\[
 K\le C_0{N\over M},\qquad L_i=M,
 \tag{1.5}
\]

for an absolute fixed \(C_0\).  Since the calibrated crossing gives

\[
 {W\over N}=\lambda_H\ge M,
 \tag{1.6}
\]

we obtain the exact bound

\[
 s=KM\le C_0N\le C_0{W\over M}=O(W/m).
 \tag{1.7}
\]

For the geodesic-chunk normalization, if there are \(T\) tags, each chunk
has \(g\) physical phases, \(gT=(1+o(1))W\), and

\[
 K=O(T/m),
 \tag{1.8}
\]

then likewise

\[
 s=Kg=O(Tg/m)=O(W/m).
 \tag{1.9}
\]

All subsequent exact statements use only (1.3); (1.7) or (1.9) is invoked
only for the asymptotic conclusion.

## 2. Exact actual-residual width

### Theorem 2.1 (actual one-bite width sandwich)

For every residual family (1.2) satisfying (1.3),

\[
 W-s\le\operatorname{width}({\cal H})\le W.
 \tag{2.1}
\]

In particular, if \(s=O(W/m)\), then

\[
 \operatorname{width}({\cal H})=W-O(W/m).
 \tag{2.2}
\]

#### Proof

The middle residual \({\cal H}_0\) is an antichain of cardinality
\(W-s\).  Hence

\[
 \operatorname{width}({\cal H})\ge W-s.
\]

On the other hand, \({\cal H}\) is a subposet of the Boolean lattice
\(2^{[2m]}\).  Sperner's theorem gives

\[
 \operatorname{width}(2^{[2m]})=\binom{2m}{m}=W.
\]

Width is monotone under passage to a subposet, proving the upper bound.
Substitute \(s=O(W/m)\) to obtain (2.2). \(\square\)

### Consequence 2.2 (donor width cannot substitute for hole width)

Even if the phase columns withheld by the priority deletion have total
chain width \(o(W/Q)\), the actual complement hole family after one
owner-scale bite has width \((1-o(1))W\).  Therefore those withheld
columns are donor or collision certificates; they are not a chain cover
of the actual residual.

This consequence uses the actual middle complement (1.3), so it is not a
proxy argument.

## 3. Exact saturated-chain-to-state realization

The lower bound (2.1) does not conceal a vertical realization failure.

### Theorem 3.1 (integral radius-\(Q\) columnization)

Let \({\cal A}\) be any family of subsets of \([2m]\) whose ranks lie in
\([m-Q,m+Q]\), and put

\[
 w=\operatorname{width}({\cal A}).
\]

Then there is a multiset of exactly \(w\) exact radius-\(Q\) quotient
states such that every member of \({\cal A}\) is one of the designated
band flags of at least one state.  Every state can be hosted in an
\(M=m+H\) carrier.  Consequently the actual residual \({\cal H}\) has
such a column cover with

\[
 W-s\le w\le W.
 \tag{3.1}
\]

#### Proof

By Dilworth's theorem, partition \({\cal A}\) into \(w\) inclusion
chains.  Fix one chain.  Refine and extend it to a maximal Boolean chain

\[
 \varnothing=F_0\subset F_1\subset\cdots\subset F_{2m}=[2m],
 \qquad |F_j|=j.
 \tag{3.2}
\]

Put

\[
 L=F_{m-Q}
 \tag{3.3}
\]

and, for \(1\le j\le2Q\), let \(z_j\) be the unique label in

\[
 F_{m-Q+j}\setminus F_{m-Q+j-1}.
 \tag{3.4}
\]

Because

\[
 |[2m]\setminus F_{m+Q}|=m-Q\ge H-Q,
 \]

choose any

\[
 R\subseteq[2m]\setminus F_{m+Q},
 \qquad |R|=H-Q.
 \tag{3.5}
\]

Then

\[
 \omega=(L;z_1,\ldots,z_{2Q};R)
 \tag{3.6}
\]

is an exact quotient state in the carrier

\[
 U=F_{m+Q}\mathbin{\dot\cup}R,
 \qquad |U|=m+H=M.
 \tag{3.7}
\]

Its band flag at signed rank \(r\), \(-Q\le r\le Q\), is

\[
 \Phi_r(\omega)
 =L\cup\{z_1,\ldots,z_{Q+r}\}
 =F_{m+r}.
 \tag{3.8}
\]

Here the prefix is empty when \(r=-Q\).  Every original member of the
chain is therefore a designated flag of \(\omega\).  Repeat independently
for the \(w\) chains.  This proves the theorem. \(\square\)

### Audit note

Theorem 3.1 controls neither the multiplicity of carrier tags nor legal
successors between the resulting states.  It proves exactly the vertical,
integral, literal-state assertion and nothing horizontal.

## 4. Exact horizontal successor formula

Index the flags of a state by absolute collar height:

\[
 S_h=L\cup\{z_1,\ldots,z_h\},
 \qquad 0\le h\le2Q.
 \tag{4.1}
\]

Thus \(|S_h|=m-Q+h\), and \(S_Q\) is its middle owner.

### Theorem 4.1 (common-arrival ribbon criterion)

Let

\[
 \omega=(L;z_1,\ldots,z_{2Q};R)
\]

be a radius-\(Q\) state.  For \(x\in L\) and \(y\in R\), let

\[
 \omega'
 =(L-x+y;x,z_1,\ldots,z_{2Q-1};R-y+z_{2Q})
 \tag{4.2}
\]

be its legal rotor successor, and let \(T_h\) be the flags of
\(\omega'\).  Then

\[
 \boxed{
 T_0=S_0-x+y,
 \qquad
 T_h=S_{h-1}+y\quad(1\le h\le2Q).}
 \tag{4.3}
\]

Conversely, suppose two saturated band chains \((S_h)_{h=0}^{2Q}\) and
\((T_h)_{h=0}^{2Q}\) satisfy (4.3) for labels

\[
 x\in S_0,
 \qquad
 y\notin S_{2Q}.
 \tag{4.4}
\]

Then, provided \(Q<H\le m\), they admit exact state realizations in one
common \(M\)-carrier for which the second is a legal rotor successor of
the first.

#### Proof

For the forward direction, the bottom flag of (4.2) is

\[
 T_0=L-x+y=S_0-x+y.
\]

For \(h\ge1\),

\[
\begin{aligned}
 T_h
 &=(L-x+y)\cup\{x,z_1,\ldots,z_{h-1}\}\\
 &=L\cup\{z_1,\ldots,z_{h-1}\}\cup\{y\}\\
 &=S_{h-1}+y.
\end{aligned}
 \tag{4.5}
\]

This proves necessity.

For the converse, recover \(z_h\) as the unique member of
\(S_h\setminus S_{h-1}\).  Since \(y\notin S_{2Q}\) and \(H-Q\ge1\),
choose

\[
 R\subseteq[2m]\setminus S_{2Q},
 \qquad |R|=H-Q,
 \qquad y\in R.
 \tag{4.6}
\]

This is possible because the ambient complement has size \(m-Q\ge H-Q\).
Define \(\omega=(S_0;z_1,\ldots,z_{2Q};R)\).  The update (4.2) with the
given \(x,y\) is legal, and (4.3) says its complete flag chain is exactly
\((T_h)\).  Both states lie in the common carrier

\[
 U=S_{2Q}\mathbin{\dot\cup}R.
\]

This proves sufficiency. \(\square\)

### Corollary 4.2 (rankwise Hall is not the successor Hall condition)

For one horizontal edge, every nonbottom target flag is obtained from the
preceding source flag by adjoining the **same** label \(y\).  Therefore
separate matchings between every consecutive pair of ranks do not in
general assemble to rotor successors.  The matchings must be coupled by a
common arrival label, and the bottom row must simultaneously realize the
exchange \(x\mapsto y\).

In the geodesic grid

\[
 G_{i,j}
 =C\cup\{a_{i+1},\ldots,a_g\}
   \cup\{b_1,\ldots,b_j\},
 \]

formula (4.3) is the exact horizontal shift from column \(j=t\) to
column \(j=t+1\), with common new arrival \(y=b_{t+1}\) and bottom
exchange label \(x=a_{t+Q+1}\).  Thus (4.3) is the full grid-strip
carrier formula, not a projection to owners.

### Proposition 4.3 (exact one-bite clean-state expansion)

There is a positive expansion statement at the level of the complete
exact-state universe, although it does not yet descend to a
coefficient-scale residual column cover.

For every signed band rank \(r\), let

\[
 Z_r=\binom{[2m]}{m+r}\setminus{\cal H}_r,
 \qquad
 R_r=\binom{2m}{m+r},
 \tag{4.7}
\]

and put

\[
 \delta=\sum_{r=-Q}^{Q}{|Z_r|\over R_r}.
 \tag{4.8}
\]

Let \(F\) be the number of exact radius-\(Q\) states above one
\(M\)-carrier, let \(N=\binom{2m}{M}\), and let

\[
 D=(m-Q)(H-Q)
 \tag{4.9}
\]

be the exact in- and outdegree of the rotor graph.  Call a state *clean*
when all its \(2Q+1\) designated flags lie in \({\cal H}\).  Then:

1. at least \((1-\delta)NF\) exact states are clean;
2. at least \((1-2\delta)NFD\) directed rotor edges have both endpoints
   clean;
3. if \(\nu_U\) is the maximum matching size in the clean-to-clean
   successor graph above carrier \(U\), and \(B_U\) is its number of clean
   states, then

   \[
    \boxed{
    \sum_U(B_U-\nu_U)\le2\delta NF.}
    \tag{4.10}
   \]

For a full-carrier owner-scale bite satisfying (1.5),

\[
 \delta\le {C_0(2Q+1)\over M}=O(Q/m)=o(1).
 \tag{4.11}
\]

The geodesic-chunk version has the same estimate with \(M\) replaced by
\(m\).

#### Proof

For fixed \(r\), the flag projection

\[
 \omega\longmapsto\Phi_r(\omega)
\]

from the global exact-state universe to the rank-\((m+r)\) row has
constant fibers, by coordinate transitivity.  Hence exactly
\(|Z_r|/R_r\) of all states are dirty at rank \(r\).  The union bound over
the signed rows proves assertion 1.

Every state is the source of exactly \(D\) legal edges and the target of
exactly \(D\) legal edges.  Edges having a dirty source account for at
most \(\delta NFD\) occurrences, and the same is true for dirty targets.
This proves assertion 2.

Fix a carrier \(U\), and let \(E_U\) be its number of clean-to-clean
edges.  In a bipartite graph of maximum degree \(D\), a minimum vertex
cover of size \(\nu_U\) covers at most \(D\nu_U\) edges.  Konig's theorem
therefore gives

\[
 E_U\le D\nu_U.
 \tag{4.12}
\]

Summing (4.12) and using assertion 2 yields

\[
 \sum_U\nu_U\ge(1-2\delta)NF.
\]

Since \(B_U\le F\),

\[
 \sum_U(B_U-\nu_U)
 \le NF-\sum_U\nu_U
 \le2\delta NF,
\]

which is (4.10).

For the full-carrier bite, the middle used density is at most

\[
 {s\over W}\le {C_0\over M}.
\]

At signed depth \(q\ge1\), distinctness of the selected claims and the
catalogue quota give

\[
 |Z_{\pm q}|=K\bar c_q,
 \qquad
 \bar c_q\le c_q\le {R_q\over N}.
\]

Together with \(K\le C_0N/M\), this gives

\[
 {|Z_{\pm q}|\over R_q}\le {C_0\over M}.
\]

Summing the \(2Q+1\) signed rows proves (4.11).  The chunk calculation is
identical from \(K\le C_0T/m\) and
\(\bar c_q^{(g)}\le R_q/T\). \(\square\)

### Corollary 4.4 (component bound for the clean state multicover)

The complete clean exact-state universe has a genuine rotor path/cycle
cover with total charged component count at most

\[
 \boxed{
 2\delta NF+{NF\over2Q+2}.}
 \tag{4.13}
\]

#### Proof

Take a maximum clean successor matching above each carrier.  Its path
component count, excluding directed cycles, is

\[
 \sum_U(B_U-\nu_U)\le2\delta NF.
\]

Every directed rotor cycle has length at least \(2Q+2\).  Track a label
\(x\) chosen from the lower block on the first edge.  It occupies collar
positions \(1,2,\ldots,2Q\) after the next \(2Q\) moves and is ejected
to the residual block on move \(2Q+1\).  The arrival for that move is
chosen before the ejection, so \(x\) cannot return to the lower block
until move \(2Q+2\).  The initial state therefore cannot recur earlier.
Thus the number of cycle components is at most \(NF/(2Q+2)\).  Adding
the two contributions proves (4.13). \(\square\)

The scope is important.  Proposition 4.3 and Corollary 4.4 concern the
uniform multicover of **all** clean exact state types.  Its size \(NF\) is
far above coefficient scale, and every residual Boolean target occurs
with enormous multiplicity.  They prove that one bite does not destroy
global rotor-edge density or global successor matching.  They do not
select one balanced column occurrence per residual target, do not control
the cycle/color desymmetrization, and do not prove (0.6).  The descent from
this state-universe expansion to a \(W+o(W)\)-column resolution is exactly
the unresolved integral gate.

## 5. Exact literal block ledger

A directed radius-\(Q\) rotor path with \(a\ge1\) state endpoints has the
standard exact literal compilation length

\[
 \boxed{a+2Q+1.}
 \tag{5.1}
\]

The \(a\) term is one new word position per state endpoint, and the
\(2Q+1\) term is the complete initialization/history-future certificate.
After every possible legal fusion has been performed, a cover by \(p\)
genuine rotor paths with endpoint counts \(a_1,\ldots,a_p\) therefore has

\[
 B=\sum_{i=1}^{p}a_i
 \tag{5.2}
\]

state endpoints and exact total length

\[
 \boxed{B+(2Q+1)p.}
 \tag{5.3}
\]

If two alleged blocks share enough chronology to avoid a separate
initialization, they are one longer legal rotor path for the purpose of
(5.3).  Thus the ledger already gives all genuine endpoint sharing its
full credit.

### Theorem 5.1 (bounded-\(Q\)-length block obstruction)

Suppose a designated-state column cover of \({\cal H}\) is partitioned
into \(p\) genuine rotor paths, each with at most \(CQ\) state endpoints.
Then

\[
 p\ge\left\lceil{W-s\over CQ}\right\rceil
 \tag{5.4}
\]

and its exact literal length obeys (0.4).

#### Proof

Every state endpoint has exactly one designated rank-\(m\) flag, namely
its middle owner.  The \(W-s\) distinct members of \({\cal H}_0\) must
therefore use at least \(W-s\) state endpoints.  Hence

\[
 B\ge W-s.
 \tag{5.5}
\]

Since every path has at most \(CQ\) endpoints,

\[
 p\ge\left\lceil{B\over CQ}\right\rceil
 \ge\left\lceil{W-s\over CQ}\right\rceil.
 \tag{5.6}
\]

Substitute (5.5)--(5.6) into (5.3):

\[
 \operatorname{len}
 \ge (W-s)+(2Q+1)
       \left\lceil{W-s\over CQ}\right\rceil.
 \tag{5.7}
\]

If \(s=o(W)\) and \(C\) is fixed, the right side is

\[
 \left(1+{2\over C}-o(1)\right)W.
\]

This proves the theorem. \(\square\)

### Scope of Theorem 5.1

The lower bound applies to the state-column/grid-strip route in which
each residual middle set is covered as a designated state flag.  It does
not assert a lower bound against an unrelated literal OR word which
deliberately covers many additional middle sets through nondesignated
intervals.  Such a word would be a direct construction outside the
present rotor-column compiler.

## 6. Block length versus block count

There are two distinct assertions.

1. **Bounded block length:** \(a_i\le CQ\) for every \(i\).  This forces
   (5.4) and the positive constant loss (0.4).
2. **Path-count upper bound:** \(p\le CB/Q\).  By (5.3), this yields only
   
   \[
    \operatorname{len}
    \le \left(1+2C+{C\over Q}\right)B.
    \tag{6.1}
   \]

The second statement is useful in the sparse-reserve regime.  If

\[
 B=o(W),
 \qquad
 p=O(B/Q)+o(W/Q),
 \tag{6.2}
\]

then

\[
 B+(2Q+1)p=o(W).
 \tag{6.3}
\]

This is the correct scope of the braid-Hall reserve theorem in
`ACTUAL_CATALOGUE_RESIDUAL_CHAIN_AND_BRAID_GATES_20260725.md`.

For the actual one-bite residual, however,

\[
 B\ge W-s=(1-o(1))W.
 \tag{6.4}
\]

Therefore an estimate \(p=O(B/Q)\) supplies only \(O(W)\), not \(o(W)\),
reset cost.

### Theorem 6.1 (exact coefficient-one horizontal threshold)

Assume the first bite itself has length \(o(W)\), as it does at owner
scale.  Within the designated-state rotor compiler, suppose the actual
residual is covered by \(B\le W+o(W)\) state columns and those columns are
partitioned into \(p\) genuine rotor paths.  Then the combined word has
length \(W+o(W)\) only if

\[
 p=o(W/Q).
 \tag{6.5}
\]

Conversely, \(B\le W+o(W)\) and (6.5) give an appended compilation of
length \(W+o(W)\), and adding the owner-scale bite preserves that bound.

#### Proof

By (5.3), the reset toll is exactly \((2Q+1)p\).  Since
\(B\ge W-s=W-o(W)\), a coefficient-one total leaves only \(o(W)\) for
this toll, forcing

\[
 (2Q+1)p=o(W),
\]

which is (6.5).  The converse follows by substituting (6.5) and
\(B\le W+o(W)\) into (5.3). \(\square\)

Equivalently, if \(\bar a=B/p\) is the average path length, then

\[
 {\text{reset toll}\over B}={2Q+1\over\bar a}.
 \tag{6.6}
\]

Because \(B=(1+o(1))W\), the toll is \(o(W)\) exactly when

\[
 \boxed{\bar a/Q\longrightarrow\infty.}
 \tag{6.7}
\]

## 7. The exact remaining positive theorem

The vertical part is now unconditional: Theorems 2.1 and 3.1 give an
integral column cover with at most \(W\) columns.  What is not proved is
that one can choose the chain partition, its saturated extensions, and
its carrier tails so that the common-arrival successor graph (4.3) has a
path cover satisfying (6.5).

One exact formulation is the following.

> **Actual-residual long-run gate.**  After the owner-scale bite, choose a
> saturated state-column cover \(\Omega\) of \({\cal H}\) with
> \(|\Omega|\le W+o(W)\), including carrier choices, such that the exact
> successor graph defined by (4.3) has a genuine directed path cover with
> \(o(W/Q)\) components.

For an acyclic phase order, if \(B_\Omega\) is the bipartite exact
successor graph, the path-cover number is

\[
 p(\Omega)=|\Omega|-\nu(B_\Omega).
 \tag{7.1}
\]

Thus (6.5) requires

\[
 \nu(B_\Omega)=|\Omega|-o(W/Q).
 \tag{7.2}
\]

If directed cycles are allowed before cutting, the exact component
functional is

\[
 \min_P\bigl(|\Omega|-|P|+c(P)\bigr),
 \tag{7.3}
\]

where \(P\) ranges over partial successor matchings and \(c(P)\) is the
number of directed-cycle components.  Merely obtaining a cycle cover does
not bound (7.3), because every cycle must still be charged once.

The one-bite row counts and the width identity (0.1) do not prove
(7.2).  Formula (4.3) shows the missing correlation explicitly: a single
arrival label must serve every rank of a horizontal edge.  No positive or
negative assertion about that exact Hall expansion is made without an
additional argument.

## 8. Audited boundary

The proved statements are:

1. the actual hole width after one owner-scale bite is
   \(W-O(W/m)\), with exact sandwich (2.1);
2. every residual chain cover has an exact integral saturated
   radius-\(Q\) state realization, hosted in legal \(M\)-carriers;
3. horizontal successors obey the exact common-arrival formulas (4.3);
4. fixed-constant \(O(Q)\)-length rotor blocks force a positive constant
   excess in the literal compiler;
5. for this dense actual residual, coefficient one requires
   \(p=o(W/Q)\), not merely \(p=O(B/Q)\).

The unproved statement is the actual-residual long-run gate (7.2), with a
choice of columnization and carriers.  This is strictly stronger than
separate-rank Hall and strictly different from the already proved small
donor-width estimate.
