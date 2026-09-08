# Prime quotient long-cycle covers: exact lift, compiler acceptance, and the constrained edge-colouring gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let `p=2m+1` be prime, let translation act on

\[
                         \Omega=\binom{\mathbb F_p}m,
 \qquad W=|\Omega|,
 \qquad T={W\over p},                                  \tag{0.1}
\]

and start from any oriented exact physical odd-graph factor on `Omega`.
Project its directed arcs to translation necklaces, retaining arc
multiplicity and voltage.

The proposed structural relaxation is correct through the following
point.

1. The projected directed multigraph has indegree and outdegree exactly
   `p` at every necklace.
2. Its bipartite tail--head graph decomposes into `p` perfect matchings.
3. Every perfect matching lifts to a translation-invariant exact directed
   physical odd-graph cycle cover.  Quotient cycles may have arbitrary
   lengths.  A quotient cycle of length `ell` and voltage `v` lifts to

   \[
   \begin{cases}
    p\text{ physical cycles of length }\ell,&v=0,\\
    1\text{ physical cycle of length }p\ell,&v\ne0.
   \end{cases}                                           \tag{0.2}
   \]

Thus the old two-AP-loop plus zero-voltage `p`-cycle normal form is no
longer necessary.  It was forced by insisting that every physical
component itself have the shortest length `p`.  Arbitrary long components
remove that Catalan congruence obstruction completely at the ownership
level.

The constant-one compiler is also factor-blind enough to accept these
long cycles, but not from \(H\)-return-freeness alone.  If \(S\) is the
lifted odd-graph successor, then \(P=S^2\) is a Johnson successor except
at backtracking two-cycles.  Away from those backtracks it gives an exact
alternating \(X/Y\) owner factor.  If its \(K(P)\) Johnson cycles satisfy
the geodesic condition \(G_d\) and the exact positive-dwell condition
\(P_d\), then the direct odd-cycle interface gives the finite bound

\[
 \boxed{
 \nu(p)\le
 W+(2d+1)K(P)
   +2\sum_{q=1}^{d}M_q^-(P)
   +2L_m(m-d-1).}                                  \tag{0.3}
\]

Here \(M_q^-(P)\) is the actual number of missing lower rank-\(m-q\)
targets.  Upper depth-\(q\) traces are complements of opposite-parity
lower depth-\(q\) traces, so their missing-target count is the same.
Ordinary cyclic \(H\)-geodesicity guarantees the exact compiler only with
\(d=H-1\); full \(d=H\) needs the additional positive-dwell condition,
for example geodesicity through \(H+1\) transitions.

Consequently long cycles prove coefficient one if

\[
 {d\over\sqrt m}\longrightarrow\infty,\qquad
 K(P)=o(W/d),\qquad
 \sum_{q=1}^{d}M_q^-(P)=o(W),                       \tag{0.4}
\]

when all cycles are safe and nonbacktracking.  With exceptions, one needs
the literal-invalid-slot or safe path-decomposition ledger of Section 5;
merely having \(o(W)\) bad maximal starts is not sufficient.

The exact component formula is favorable.  If the matching permutation
has quotient cycles `C`, then

\[
 \boxed{
 K(P)=
 p\sum_{C:\,v(C)=0}\gcd(|C|,2)
 +\sum_{C:\,v(C)\ne0}\gcd(|C|,2).}                 \tag{0.5}
\]

Since `H=o(p)`, all nonzero-voltage quotient cycles together contribute
only `O(T)=o(W/H)` Johnson components.  The complete component condition
reduces to

\[
 \sum_{C:\,v(C)=0}\gcd(|C|,2)=o(T/H).              \tag{0.6}
\]

This is a genuine advantage over the shortest-cycle route.

What fails is the last proposed inference.  Ordinary bipartite
edge-colouring enforces only one incoming and one outgoing arc at each
necklace.  `H`-safety depends on `2H` consecutive lifted arcs, zero voltage
is a whole-cycle sum, component count is a subtour statistic, and target
coverage couples all cycles.  None is controlled by the regular
one-factorization theorem.  Moreover, even perfect two-sided safety gives
only rank-correct literal traces; it does not prevent the same target from
being hit by many different starts.

The surviving object is therefore a **voltage- and memory-constrained
perfect matching** in the projected arc graph, not an ordinary edge
colouring.  This relaxation bypasses the Catalan obstruction but replaces
it by the precise joint gate (0.4), (0.6), and the target-repeat ledger.

## 1. Projection is exactly `p`-regular

Let `F` be an oriented exact physical odd-graph factor and let

\[
                         S_F:\Omega\longrightarrow\Omega        \tag{1.1}
\]

be its successor permutation.  Thus

\[
                         X\cap S_F(X)=\varnothing                \tag{1.2}
\]

for every `X`.

Let `N=Omega/<rho>` be the set of translation necklaces.  For every
physical owner `X`, place one projected arc occurrence

\[
                         [X]\longrightarrow[S_F(X)]              \tag{1.3}
\]

in a directed multigraph `D`.  Parallel arcs and their voltages are
retained.

### Lemma 1.1 (exact projected degrees)

Every vertex of `D` has indegree and outdegree `p`.

#### Proof

Every nonempty proper subset of `F_p` has a free translation orbit, so one
necklace contains exactly `p` physical owners.  Each has one outgoing
successor arc, giving outdegree `p` after projection.  Since `S_F` is a
permutation, the same `p` owners have exactly `p` physical predecessors,
giving indegree `p`. \(\square\)

Split every necklace into a tail copy and a head copy.  Every projected
arc becomes a bipartite edge between these copies.  Lemma 1.1 makes the
resulting bipartite multigraph `p`-regular.

### Corollary 1.2 (arc Latin resolution)

The projected arc multigraph decomposes into `p` directed perfect
matchings

\[
                         E(\mathcal D)=M_0\dot\cup\cdots\dot\cup M_{p-1}.
                                                                    \tag{1.4}
\]

#### Proof

A regular bipartite multigraph has a perfect matching by Hall's theorem.
Remove one and iterate. \(\square\)

This is an exact integral theorem.  No averaging or fractional rounding is
involved.

## 2. Every quotient matching lifts to an exact invariant cover

Choose one representative `A_v` for every necklace `v`.  Write a selected
quotient dart as

\[
                         e:v\xrightarrow{a(e)}w,                  \tag{2.1}
\]

meaning

\[
                         A_v\cap(A_w+a(e))=\varnothing.          \tag{2.2}
\]

Let `M` be any directed perfect matching of the quotient tail--head graph.
Define its physical lift by

\[
 \widetilde S_M(A_v+t)=A_w+a(e)+t
 \qquad(t\in\mathbb F_p),                            \tag{2.3}
\]

where `e` is the unique selected dart leaving `v`.

### Theorem 2.1 (arbitrary-length invariant lift)

The map `S_tilde_M` is a translation-equivariant permutation of `Omega`
supported on physical odd-graph arcs.  Hence it is an exact directed
physical cycle cover.  Its component lift law is (0.2).

#### Proof

Equation (2.2) proves physical adjacency for every translate in (2.3).
The matching has one selected outgoing and one selected incoming dart at
every quotient vertex, so (2.3) is bijective on all fibres.  It plainly
commutes with translation.

On a quotient permutation cycle of length `ell`, one circuit adds the
total voltage `v`.  If `v=0`, every one of the `p` starting phases closes
after one circuit, giving `p` cycles of length `ell`.  If `v` is nonzero,
it has order `p`, so all phases join into one cycle of length `p ell`.
\(\square\)

No restriction `ell=p` appears.  Therefore neither the Catalan congruence
nor the requirement of exactly two AP loops applies to Theorem 2.1.
Those conditions classified only invariant factors whose physical
components were shortest odd cycles.

Every quotient loop has nonzero voltage: voltage zero would lift to a
physical loop, which the odd graph does not have.  Moreover, if its
voltage is \(v\ne0\), then its lift has edges
\(A+t\to A+t+v\).  Thus \(A\cap(A+v)=\varnothing\).
Reading membership around the \(v\)-cyclic order gives a circular binary
word of length \(2m+1\), with \(m\) ones and no adjacent ones.  It is an
alternating maximum independent word with one double-zero gap.  Hence the
lifted loop is precisely a genuine AP shortest \(p\)-cycle.  Quotient
loops are harmless; the directed-cover caveat begins with zero-voltage
quotient two-cycles.

## 3. Squaring the odd successor gives the Johnson owner chronology

Put

\[
                         P=\widetilde S_M^2.                       \tag{3.1}
\]

Fix

\[
                         X\xrightarrow{S}B\xrightarrow{S}X'.     \tag{3.2}
\]

Because `X` and `B` are disjoint,

\[
                         \mathbb F_p\setminus B=X\dot\cup\{z\}
                                                                    \tag{3.3}
\]

for one coordinate `z`.  Since `X'` is also disjoint from `B`, it is an
`m`-subset of the right side of (3.3).  Therefore exactly one of the
following holds.

1. `X'=X`; the two odd arcs backtrack.
2. `X'=X-a+z` for a unique `a in X`; this is a Johnson edge.

In the second case

\[
                         X\cup X'=B^c.                            \tag{3.4}
\]

### Lemma 3.1 (exact alternating owner factor)

If `S_tilde_M` has no directed two-cycle, then the cycles of `P`, with

\[
                         Y_X=\widetilde S_M(X)^c,                 \tag{3.5}
\]

form an exact alternating `X/Y` factor: the `X` owners partition rank
`m`, the `Y` owners partition rank `m+1`, and every transition satisfies

\[
                         Y_X=X\cup P(X).                          \tag{3.6}
\]

#### Proof

The `X` owners are all vertices of `Omega`, once each.  Absence of
backtracking and (3.4) give (3.6).  Since `S_tilde_M` is a permutation,
its values run through all rank-`m` sets once; their complements in (3.5)
therefore run through all rank-`m+1` sets once. \(\square\)

If backtracks are present, the affected `P`-vertices are fixed points and
(3.6) fails there.  They must be deleted, compiled separately, or charged
as actual missing upper-middle targets.  The one-factorization theorem
does not exclude them.

### Lemma 3.2 (opposite-parity trace duality)

On one physical \(S\)-cycle write

\[
 X_j=A_{r+2j},\qquad X'_j=A_{r+2j+1}.             \tag{3.7}
\]

For \(q\ge0\), put

\[
 L_{j,q}=\bigcap_{t=0}^{q}X_{j+t},\qquad
 U_{j,q}=\bigcup_{t=0}^{q+1}X_{j+t}.             \tag{3.8}
\]

Then

\[
 \boxed{
 U_{j,q}^{\,c}=\bigcap_{t=0}^{q}X'_{j+t}.}        \tag{3.9}
\]

Consequently, over the complete alternating factor, the upper
rank-\(m+1+q\) multiplicity of \(U\) equals the lower
rank-\(m-q\) multiplicity of \(U^c\).  In particular

\[
                         M_q^+=M_q^-.              \tag{3.10}
\]

#### Proof

By (3.6),

\[
 (X_{j+t}\cup X_{j+t+1})^c=X'_{j+t}.
\]

The union of these \(q+1\) adjacent pairs is exactly \(U_{j,q}\);
taking complements gives (3.9).  On an even physical cycle the two
choices of parity are the two \(P\)-cycles.  On an odd physical cycle
multiplication by two permutes all indices, so opposite parity is a
cyclic rephasing of the same \(P\)-cycle.  Hence opposite parity is a
bijection on all rooted slots, proving the multiplicity assertion and
(3.10). \(\square\)

## 4. Exact component ledger

Let `C` be a quotient cycle of the matching permutation, of length `ell`
and voltage `v`.  By Theorem 2.1 its physical odd-successor lift has
either `p` cycles of length `ell` or one cycle of length `p ell`.  Squaring
a directed cycle of length `L` produces exactly `gcd(L,2)` cycles.
Since `p` is odd, this proves (0.5).

Put

\[
 Z_0(M)=\sum_{C:\,v(C)=0}\gcd(|C|,2),
 \qquad
 Z_*(M)=\sum_{C:\,v(C)\ne0}\gcd(|C|,2).             \tag{4.1}
\]

Then

\[
                         K(P)=pZ_0(M)+Z_*(M),                       \tag{4.2}
\]

and trivially

\[
                         Z_*(M)\le2T.                             \tag{4.3}
\]

For every `H=o(p)`,

\[
                         2T=o(pT/H)=o(W/H).                       \tag{4.4}
\]

Therefore

\[
 \boxed{
 K(P)=o(W/H)
 \quad\Longleftrightarrow\quad
 Z_0(M)=o(T/H),}                                                   \tag{4.5}
\]

up to the harmless `Z_*` term.  A successful matching may have as many as
`Theta(T)` nonzero-voltage quotient cycles; their physical lifts are still
long enough for the interface budget.

Because \(P\) commutes with translation, every trace map does also.
Consequently every physical missing-target set is a union of complete
translation necklaces.  If \(\overline M_q^\pm\) denotes the number of
missing target necklaces, then

\[
                         M_q^\pm=p\,\overline M_q^\pm.            \tag{4.6}
\]

Thus the physical one-sided condition in (0.4) is equivalently

\[
                    \sum_{q=1}^{d}\overline M_q^-=o(T).          \tag{4.7}
\]

## 5. What the constant-one interface actually accepts

For the exterior term in (0.3), put

\[
\begin{aligned}
A_m(a)&=\binom ma-\binom m{a-1},\\
w_m(a)&=
\begin{cases}
m,&a=0,\\
m-2a+1,&a>0,
\end{cases}\\
C_m(t)&=
\begin{cases}
0,&t<0,\\
\displaystyle\binom m{\min(t,\lfloor m/2\rfloor)},&t\ge0,
\end{cases}\\
L_m(r)&=2\sum_{a=0}^{\lfloor m/2\rfloor}
          A_m(a)w_m(a)C_m(r-a).
\end{aligned}                                                     \tag{5.0}
\]

The trimmed odd lift of this product-SCD word has length \(2L_m(r)\).
At \(r=m-d-1\) it covers every rank outside
\([m-d,m+d+1]\), and

\[
 {L_m(m-d-1)\over\binom{2m}m}
 \le C_0\exp\!\left(-{d^2\over8m}\right)                         \tag{5.0a}
\]

for an absolute constant \(C_0\).

For a cyclic \(P\)-row \(X_i\), let \(G_d\) mean that every segment of
at most \(d\) Johnson transitions is geodesic.  Let \(P_d\) mean that
every nonconstant positive coordinate run has at least \(d+1\) states.
The second condition is the exact delay-atom condition.  The stronger
requirement that no coordinate changes twice among any \(d+1\)
consecutive transitions implies both.  Ordinary \(G_H\) implies
\(P_{H-1}\), but not \(P_H\).

For a directed Johnson cycle, call a `q`-window two-sided safe when no
physical coordinate is toggled on two of its `q` edges.  Equivalently its
`2q` removed/inserted labels are distinct.  Then its intersection and
union have the exact ranks `m-q` and `m+q`.

In the odd alternating factor, lower depth `q` uses `q` transitions while
the displayed upper union uses `q+1`.  Two-sided safety through `H+1`
transitions is therefore a convenient support-blind sufficient condition
for protected depths through `H`.  It is not necessary: Lemma 3.2 and the
weaker exact positive-dwell condition give the \(G_H+P_H\) interface in
(0.3).

Assume first that `P` has no fixed points and has this cyclic
`(H+1)`-safety.  For each sign and depth let

\[
 M_q^-(P),\qquad M_q^+(P)                            \tag{5.1}
\]

be the actual numbers of lower and upper physical targets not represented
by any cyclic window, and put

\[
                         D_H(P)=\sum_{q=1}^H
                         (M_q^-(P)+M_q^+(P)).                    \tag{5.2}
\]

### Theorem 5.1 (factor-blind long-cycle compiler)

Along any sequence with

\[
                         {H\over\sqrt m}\longrightarrow\infty,
                         \qquad H=o(m),
\]

the standard exterior range in the direct odd interface gives

\[
 \boxed{
 \nu(p)\le W+(2H+1)K(P)+D_H(P)+o(W).}              \tag{5.3}
\]

In particular (0.4) proves coefficient one along the prime subsequence.

#### Proof

The cycles of `P` and the intermediate complements in Lemma 3.1 form an
exact alternating `X/Y` factor.  Cyclic two-sided safety is precisely the
delay-`H` hypothesis in the direct-support odd cycle interface.  Cut every
cycle once and install its full collar; a cycle of `lambda` `X`-owners
costs `lambda+2H+1` factor letters.  Summing `lambda` gives `W`, and
appending every actually missing signed target costs (5.2).  The standard
outer word is `o(W)`. \(\square\)

The length or shortest-cycle geometry of a component is absent from the
proof.  Only safety, target support, and the number of components enter.

### Exceptional windows require a safe path decomposition

Theorem 5.1 is a theorem for globally safe cycles.  An unsafe local window
cannot merely be deleted while the same cyclic compiler is retained: the
proved delay word uses the consistent `H`-history around the whole
component.

Let `kappa_H(P)` be the minimum number of cyclic cuts needed so that every
resulting open path, together with every uncut cycle, is two-sided safe
through the protected odd range `H+1`.  Let `p_H` be the number of
resulting open paths and `z_H` the number of uncut safe cycles.  The exact
path/cycle interface gives

\[
 \boxed{
 \nu(p)\le W+Hp_H+(2H+1)z_H+M_0^+
       +D_H^{\rm safe}+o(W),}                                  \tag{5.4}
\]

where `M_0^+` is the missing upper-middle mass and `D_H^safe` is the
actual positive-depth deficit of the surviving certified windows.
Cutting one unsafe cyclic component at `r` places makes `r` open paths, so
`p_H<=kappa_H(P)` after harmless conventions for already open/deleted
exceptions.

Consequently the factor-blind safe-cut requirement is

\[
                         H\kappa_H(P)=o(W).                       \tag{5.5}
\]

Knowing only that `e=o(W)` starting positions have bad length-`(H+1)`
windows is insufficient.  The immediate bound is

\[
                         \kappa_H(P)\le e,                       \tag{5.6}
\]

which gives overhead `He`; the safe unstructured rate is therefore
`e=o(W/H)`.  A larger bad-window set is usable only when it is hit by
`o(W/H)` cuts, or when a new stateful compiler is proved to cross it.

Backtracking fixed points obey the same rule.  They may be deleted and
their owners appended at harmless baseline cost if their mass is `o(W)`,
but the resulting path/component and actual shadow ledgers must still
satisfy (5.4)--(5.5).

### Safety is not coverage

Even perfect cyclic safety does not imply `D_H(P)=o(W)`.  Safety proves only that a
window has the correct rank and is a literal target.  Different safe
windows may hit the same target.  Already at depth one, many Johnson edges
in one lower star have the same intersection; choosing several of them
repeats one lower target while leaving others uncovered.  The exact
missing-target identity is still

\[
 \#\{T:k_q(T)=0\}
 =\sum_T(k_q(T)-1)_+-(W-N_q),                       \tag{5.7}
\]

with the appropriate odd-rank `N_q` on each sign.  Return-freeness does
not control the repeat term.

Therefore the condition proposed in the question must be strengthened
from

\[
 \text{`H`-return-free off `o(W)` starts}
\]

to the safe-decomposition and support hypothesis

\[
 \boxed{
 \kappa_H(P)=o(W/H),\qquad
 p_H+z_H=o(W/H),\qquad
 M_0^++D_H^{\rm safe}=o(W).}                                   \tag{5.8}
\]

When every cycle is safe, `kappa_H=0`, `p_H=0`, `z_H=K(P)`, and (5.8)
reduces to (0.4).

## 6. Why ordinary edge-colouring does not enforce the three ledgers

Write `x_(e,c)` for the assertion that projected arc occurrence `e` is
assigned colour `c`.  A proper `p`-edge-colouring satisfies only

\[
\begin{aligned}
 \sum_{e\in\delta^+(v)}x_{e,c}&=1,\\
 \sum_{e\in\delta^-(v)}x_{e,c}&=1,\\
 \sum_cx_{e,c}&=1.                                      \tag{6.1}
\end{aligned}
\]

These are the bipartite one-factorization equations.  Each condition in
(5.8) lies beyond them.

Moreover every prescribed perfect matching extends to a full proper
\(p\)-edge-colouring: delete it and one-factor the remaining
\((p-1)\)-regular bipartite multigraph.  Thus asking for an
edge-colouring with one good colour is exactly the constrained
perfect-matching problem again.  The ordinary colouring theorem provides
no additional selection power.

1. One Johnson transition of the lift uses two consecutive quotient arcs.
   Two-sided protected safety is a constraint on up to `2H+2` consecutive
   arcs of one
   colour, together with their physical voltages and phases.
2. Whether a quotient permutation cycle has zero voltage is the sum of
   all its arc voltages.  It is not determined by any one vertex or arc.
3. The number of cycles is a subtour statistic of the selected
   permutation.
4. A target collision compares windows based at different quotient
   cycles, so it is not even a local forbidden-transition condition.

There is no averaging identity in (6.1) which bounds any of these four
quantities.  In particular, `p`-regularity alone is insufficient.  As an
abstract sharp example, if a quotient perfect matching `M_0` consists of
oppositely paired zero-voltage darts and the multigraph is `p` parallel
copies of `M_0`, every one-factorization consists of copies of `M_0`.
Every physical lift is then a backtracking two-cycle cover with
`Theta(W)` components and no safe Johnson successor.  This example shows
exactly what the regular bipartite theorem fails to see.  Whether a given
projected shortest-cycle factor excludes this extreme pattern is extra
structure; it is not a consequence of Lemma 1.1.

### Lemma 6.1 (closed coboundary-block obstruction)

Suppose the quotient dart support is the disjoint union of \(b\) closed
vertex blocks \(Q_1,\ldots,Q_b\): no supported dart joins distinct
blocks.  Suppose further that on each \(Q_i\) there is a phase potential
\(\phi_i\) such that every supported dart \(e:u\to v\) internal to
\(Q_i\) has voltage

\[
                         a(e)=\phi_i(v)-\phi_i(u).    \tag{6.2}
\]

Then every quotient perfect matching has at least \(b\) zero-voltage
cycles.  Its squared physical lift consequently has at least \(pb\)
Johnson components.  Hence a necessary component condition for constant
one is

\[
                              b=o(T/H).              \tag{6.3}
\]

#### Proof

Closedness forces every perfect matching to restrict to a permutation of
each \(Q_i\), so it contains at least one circuit there.  Summing (6.2)
around any such circuit telescopes to zero.  Thus each block contributes
a zero-voltage quotient cycle.  Formula (4.2) gives at least \(p\)
Johnson components per block, and the collar condition
\(HK(P)=o(W)=o(pT)\) yields (6.3). \(\square\)

This obstruction survives every recolouring or alternating-cycle switch
which stays inside the same support blocks: neither operation creates a
cross-block dart or changes the coboundary identity.

## 7. Exact constrained-matching reformulation

For one selected quotient matching `M`, let

* `kappa_H(M)` be the minimum safe-cut number from Section 5, including
  the treatment of backtracks;
* `c_H(M)=p_H+z_H` be the resulting safe path/cycle count;
* `z_0(M)` be the zero-voltage component statistic (4.1); and
* `d_H(M)=M_0^++D_H^safe` be the actual aggregate signed target deficit.

Then the structural relaxation proves coefficient one exactly under

\[
 \boxed{
 \kappa_H(M)=o(W/H),\qquad
 c_H(M)=o(W/H),\qquad
 z_0(M)=o(T/H),\qquad
 d_H(M)=o(W).}                                      \tag{7.1}
\]

For a completely safe lift the first condition is zero, the second is
equivalent to the third by (4.5), and (7.1) reduces to the clean cycle
criterion (0.4), (0.6).

The matching must still obey one incoming and one outgoing arc at every
necklace.  Equivalently, one may seek a full edge-colouring for which the
sum of the normalized costs in (7.1) over all `p` colours is `o(p)`; then
one colour satisfies (7.1).  But proving such an averaged bound requires
history-state, cycle-voltage, and target-occurrence information absent
from (6.1).

A faithful finite-state model expands an arc to its last `H` lifted
Johnson transitions and imposes de Bruijn overlap between successive
states.  This handles safety.  It must then be intersected with:

1. the root/necklace perfect-matching equations;
2. a nonzero-voltage or sparse-zero-voltage cycle condition; and
3. the simultaneous signed target-cover ledger.

Thus the new route is real but not completed by König edge-colouring.  Its
precise surviving theorem is a **root-transversal, voltage-biased,
target-balanced `H`-memory matching** in the projected arc multigraph.

## 8. Verdict relative to the shortest-cycle route

The relaxation makes one substantial advance:

\[
 \boxed{
 \text{translation-invariant exact ownership no longer requires
 shortest zero-voltage `p`-cycles or two AP loops}.}              \tag{8.1}
\]

Nonzero-voltage quotient cycles are especially useful: their long lifts
make their entire component count negligible when `H=o(p)`.  Only the
zero-voltage quotient cycles must be sparse at scale `o(T/H)`.

It does not yet prove constant one.  The exact failure of the naive
argument is

\[
 \text{regular arc factorization}
 \not\Longrightarrow
 \text{stateful safety, favorable voltage, or target coverage}. \tag{8.2}
\]

The route should therefore be pursued as the constrained matching problem
(7.1), rather than as an ordinary edge-colouring theorem.  A proof of
(7.1) would bypass the Catalan obstruction; a positive edge-colouring
statement without those three ledgers would not.

## 9. Low-switch successor

`MATH_THEOREM_MSW_NECKLACE_EDGE_COLORING_SWITCH_AND_H_WINDOW_GATE_20260726.md`
audits the proposed low-switch refinement. It proves that tagged colour
changes are not the correct statistic when several MSW tags lie in one
translation arc orbit. For the orbit-aware switch count `s_c`, the exact
number of physical splice boundaries in colour `c` is `p s_c`, and the
uncertified depth-`q` starts are the `(2q-1)`-step predecessor dilation of
that splice set.

If `Sw=sum_c s_c`, one colour has at most `Sw` physical splices, at most
`(2H-1)Sw` maximal-depth inheritance defects, and at most `2H^2 Sw`
two-sign all-depth inheritance defects. Thus `Sw=O(T)` closes the
component and maximal-depth gates for `H=o(p)`, but does not close the
all-depth ledger at calibrated `H` without further cancellation. The
successor also gives the exact integer switch optimization and a
`p`-regular abstract transition system forcing `Sw=W`, so König
edge-colouring alone cannot prove a low-switch theorem.
