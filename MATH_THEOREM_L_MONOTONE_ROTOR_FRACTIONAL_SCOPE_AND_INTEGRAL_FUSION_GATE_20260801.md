# Audit of the monotone rotor and the exact protected integral-fusion gate

Date: 2026-08-01  
Lane: L, stationary trace / positive-density protected extension  
Status: the normalized fractional monotone-rotor theorem is proved after
the stated scope corrections.  Core-free raw rotor fusion is impossible,
even with owner-changing labels.  A positive-core split rotor and a
guard-complete connected-circulation formulation remain live.  No integral
compiler or new bound on `nu(k)` is claimed.

## 0. Verdict

The core inclusion in
`MATH_CANDIDATE_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md`
is correct:

\[
 \{0\le q_1\le\cdots\le q_{r-1}\le1:\ \sum_s q_s\le d\}
       \subseteq ST_{r,d}                                      \tag{0.1}
\]

for `r>=2` and `1<=d<=r-1`, with `ST` normalized to mass one per
owner and with repeated suffix ranks counted once.  The canonical
left-justified triangular Ferrers vector satisfies the hypotheses, so the
unrooted rank-only fractional marked-trace gate is closed.

The integral conclusion is negative on the most rigid face.  Let the mobile
core be zero and use every positive composition once.  Every legal successor
permutation is the block rotation.  Hence its rotation necklaces cannot be
fused by changing owner labels while retaining that type multiset.  This is
a type inequality and precedes owner, `q1`, upper-shadow, and common-cap
choices.

The weakest exact integral replacement is not a marginal rotor assertion.
It is one occurrence-labelled directed circulation with connectivity cuts,
literal resource capacities, the guarded Ore--Ryser cuts for its incidence
bank, and the named-target/common-cap equations.  On a serial-safe merge
catalogue it becomes a resource-compatible spanning-tree problem on the
contracted necklaces.  Disturbance of only `O(1)` named loads requires a
connected reservoir of payload-transparent macros (or explicit bounded
cancellation); pairwise owner/`q1` disjointness alone supplies neither.

## 1. Proof-safe fractional theorem

Fix `r>=2`, `1<=d<=r-1`, and, for the literal target-load statement, an
ambient ground-set size `k>=r`.  The age-type cone itself is independent of
`k`.  Let

\[
 \mathcal C_{r,d}=\{c=(c_0,\ldots,c_d):c_0>0,\ c_i\ge0,
                                      \sum_i c_i=r\}.
\]

Put `c -> c'` when

\[
                         c'_{i+1}\le c_i\qquad(0\le i<d),        \tag{1.1}
\]

and define the **set** of available proper suffix ranks

\[
 R(c)=\{c_0+\cdots+c_{j-1}:1\le j\le d,
                                  \ c_0+\cdots+c_{j-1}<r\}.     \tag{1.2}
\]

Repeated partial sums caused by zero age classes occur once.  A vector `q`
belongs to normalized `ST_(r,d)` when there are a probability law `pi`, a
stationary type flow `f`, and independent mark variables with

\[
 \sum_c\pi(c)=1,
 \quad\sum_{c'}f(c,c')=\sum_{c'}f(c',c)=\pi(c),
 \quad q_s\le\sum_{c:s\in R(c)}\pi(c).                         \tag{1.3}
\]

### Theorem 1.1 (normalized monotone rotor)

If `r>=2`, `1<=d<=r-1`,

\[
                 0\le q_1\le\cdots\le q_{r-1}\le1,
                 \qquad\sum_s q_s\le d,                         \tag{1.4}
\]

then `q in ST_(r,d)`.  The resulting flow has a same-owner invariant
literal fractional lift.  A fixed rank-`s` target receives load

\[
                         {\binom kr\over\binom ks}q_s.            \tag{1.5}
\]

#### Proof

For `1<=ell<=r-1`, let `v_ell` be the indicator of the final `ell`
ranks.  Writing successive differences of `q` gives uniquely

\[
 q=\sum_\ell\alpha_\ell v_\ell,
 \qquad\alpha_\ell\ge0,
 \quad\sum_\ell\alpha_\ell\le1,
 \quad\sum_\ell\ell\alpha_\ell\le d.                          \tag{1.6}
\]

The vertices of this two-row packing polytope are zero, `v_a` for
`a<=d`, `(d/b)v_b` for `b>d`, and

\[
 {b-d\over b-a}v_a+{d-a\over b-a}v_b
       \qquad(1\le a<d<b\le r-1).                              \tag{1.7}
\]

The type `(r-d,1,...,1)` with its type self-loop supplies `v_a`.  For the
long vertex, put `K=r-b-1` and let

\[
                 a=(a_0,\ldots,a_d),\quad a_i>0,
                 \quad\sum_i a_i=b+1.                           \tag{1.8}
\]

The types `(K+a_0,a_1,...,a_d)` follow the rotation

\[
                 R(a)=(a_d,a_0,\ldots,a_{d-1}).                  \tag{1.9}
\]

Giving every one of the `binom(b,d)` rotation edges mass
`1/binom(b,d)` is a normalized circulation.  Positive compositions are
cut sets of size `d` among `b` positions, so every one of the final `b`
ranks occurs with probability `d/b`.  This gives `(d/b)v_b`.

For (1.7), perform the same construction at depth `d-a` and mobile sum
`b-a+1`, with mass `1/binom(b-a,d-a)` on every rotation edge, then append
`a` singleton age classes.  The appended ranks occur with probability one
and the earlier ranks with probability `(d-a)/(b-a)`.  Convexity proves
(1.4).  The established biregular labelled-partition lift proves the
same-owner literal fractional statement, and symmetric averaging gives
(1.5). \(\square\)

For the actual triangular application one must inherit all of its
quantifiers.  Namely, `k>=3`, `r=ceil(k/2)`, `W=binom(k,r)`,
`Lambda=sum_(s<r)binom(k,s)`, `d` is the optimal triangular depth,
`h=(Lambda-dW)_+`, and `b_s` are the column counts of an actual
left-justified `h`-cell Ferrers board, extended by zero after `d`.  Then

\[
 q_s={\binom ks-b_s\over W}                                    \tag{1.10}
\]

obeys (1.4), and (1.5) is `1-b_s/binom(k,s)`.  This complementarity is
fractional after the common symmetric average; it is not an integral named
target cover.

## 2. Exact rotor necklace count

Let `B=b+1` and `L=d+1`.  The number of rotation necklaces of positive
`L`-part compositions of `B` is

\[
 \boxed{
 \kappa(B,L)={1\over L}
   \sum_{q\mid\gcd(B,L)}\varphi(q)
      \binom{B/q-1}{L/q-1}.}                                   \tag{2.1}
\]

Indeed, a rotation of order `q` fixes precisely the strings obtained by
repeating `q` times a positive `L/q`-part composition of `B/q`; Burnside
gives (2.1).  In particular,

\[
                         \kappa(B,L)\ge {1\over L}\binom{B-1}{L-1}. \tag{2.2}
\]

For `r=9,d=3,b=8`, the core-free long rotor has `kappa=14`.  The mixed
rotors `(a,b)=(1,8)` and `(2,8)` have respectively seven and three
necklaces.  These are type components before the same-owner labelled lift,
which can split further and occurs independently in every owner.

## 3. Raw core-free fusion is impossible

Take the complete core-free set

\[
 \mathcal V=\{a\in\mathbb Z_{>0}^{d+1}:\sum_i a_i=r\}.          \tag{3.1}
\]

### Theorem 3.1 (forced rotation)

If `F` is a permutation of `V` satisfying

\[
                         F(a)_{i+1}\le a_i
                         \qquad(a\in\mathcal V,\ 0\le i<d),    \tag{3.2}
\]

then `F(a)=R(a)` for every `a`.  More generally, every legal coupling with
uniform source and target marginals is supported only on the rotation arcs.

#### Proof

Coordinate symmetry of `V` and bijectivity give

\[
 \sum_{a\in\mathcal V}F(a)_{i+1}
   =\sum_{a\in\mathcal V}a_{i+1}
   =\sum_{a\in\mathcal V}a_i.                                  \tag{3.3}
\]

The nonnegative slacks in (3.2) therefore sum to zero, so every one is
zero.  Thus `F(a)_(i+1)=a_i` for all `i<d`; equality of total sizes forces
`F(a)_0=a_d`.  This is (1.9).  A doubly stochastic coupling is a convex
combination of permutations, so the coupling statement follows as well.
\(\square\)

Owner labels do not appear in (3.2).  Therefore owner-changing endpoints
cannot fuse two different core-free composition necklaces while retaining
the complete uniform type multiset.  Pairwise owner, lower-`q1`, and
upper-`q1` disjointness of separately lifted strands does not weaken this
obstruction.

### Theorem 3.2 (occurrence-edit floor)

Let `kappa` be (2.1) for the core-free set (3.1).  Replace `t` occurrences
of `V` by `t` positive compositions of the same total, allowing repeated
types, and suppose the new occurrence multiset has a legal one-cycle
successor permutation.  Then universally

\[
                         t\ge {\kappa-1\over2(r-d)}.              \tag{3.4}
\]

If `kappa>1`, the stronger form supplied by the same counting argument is

\[
                         t\ge\left\lceil{\kappa\over2(r-d)}\right\rceil.
                                                                    \tag{3.5}
\]

#### Proof

Let `M_i` be the sum of coordinate `i` over the modified multiset.  Summing
the legal inequalities gives `D_i=M_i-M_(i+1)>=0`.  The total selected-arc
slack is

\[
             \sum_{i=0}^{d-1}D_i=M_0-M_d.                       \tag{3.5}
\]

Every nonrotation arc contributes at least one to (3.5).  In a positive
`(d+1)`-part composition of `r`, `a_0-a_d` lies between
`-(r-d-1)` and `r-d-1`.  Hence one deletion and one insertion change
`M_0-M_d` by at most `2(r-d-1)`, so the number of nonrotation arcs is at
most `2(r-d-1)t`.

A deletion or insertion touches at most one original rotation necklace;
there are therefore at least `kappa-2t` untouched necklaces.  Except for
the vacuous case `kappa=1,t=0`, an untouched necklace cannot be the whole
active multiset and each needs a nonrotation exit in a single successor
cycle.
Thus

\[
             \kappa-2t\le2(r-d-1)t
\]

when `kappa>1`, which is (3.5); the universally weakened form (3.4)
includes the exceptional case. \(\square\)

Since `kappa>=binom(r-1,d)/(d+1)`, this edit floor is unbounded and is
typically enormous.  It rules out `O(1)` **occurrence** edits.  It becomes
a lower bound on disturbed named targets only under a private-anchor or
no-cancellation hypothesis.  Although the strictly increasing full suffix
rank list determines a positive composition, changed rank slots can be
rehosted or their named-target effects can cancel.  That distinction is
essential.

## 4. Positive permanent core: the split-rotor gate

For the long rotor with permanent core `K=r-b-1>0`, retain the complete
uniform positive mobile-composition set.  Let a selected successor send
`a` to `a'`.  Summing the legal inequalities still forces equality in
coordinates `i=1,...,d-1`, but the first inequality has core slack.

### Proposition 4.1 (exact selected-arc form)

Every arc used by a legal successor permutation has the form

\[
 a'=(a_0+a_d-t,\ t,\ a_1,\ldots,a_{d-1}),                       \tag{4.1}
\]

where

\[
                 1\le t\le\min\{a_0+a_d-1,K+a_0\}.              \tag{4.2}
\]

Conversely every permutation selecting arcs of (4.1)--(4.2) is a legal
type successor system.

#### Proof

For `i>=1`, coordinate symmetry and the same zero-total-slack argument as
in (3.3) force `a'_(i+1)=a_i`.  Put `t=a'_1`.  Total mass gives
`a'_0=a_0+a_d-t`; positivity gives the first upper bound in (4.2), and
the `i=0` transition inequality gives the second.  The converse is direct.
\(\square\)

Thus positive core is not covered by the no-go.  Its raw integral problem
is exactly a perfect assignment in the split-rotor digraph plus subtour
cuts.  No all-parameter Hamilton theorem for that digraph is proved here.
Even a positive type Hamilton cycle would not provide literal owners,
palettes, upper witnesses, or a compiler cap.

## 5. Weakest guard-complete integral fusion statement

Let `Omega` be the occurrence-labelled rotor/rail vertices to be used once,
and let `A` be a catalogue of **literal-safe directed transition bundles**.
An arc bundle includes its source spelling, owner transition, lower and
upper `q1` resources, all internal and crossing interval witnesses, and all
trace/common-cap guards.  Let `R_e` be its unit resources and let
`Delta_e(t)` be its signed effect on named target load `t` relative to the
declared baseline.  Here a *disturbed named load* means a target whose net
signed load error is nonzero after all selected effects cancel; it does not
mean every target occurrence touched by a macro.  Let `P(x)` be the
middle-level incidence bank exposed by selected arcs.

Work in the odd host `ML_n`.  Fix an edge catalogue `Z` which is disjoint
from every possible `P(x)` and is **complete for the completion guards**:
every completion edge outside `Z` is compatible with every selected bundle,
and every remaining selected-bundle upper/trace/cap condition is already one
of the displayed literal equations.  If a completion-edge conflict depends
on `x`, its completion variable must instead be included in the joint model;
`delta_star(P(x),Z)` alone is then not an exact projection.  An even-host or
different all-`k` incidence analogue likewise needs its own factor cut.

### Theorem 5.1 (protected rotor-fusion equivalence)

Under the literal bundle and complete-fixed-guard semantics above, a
one-cycle protected chronology
on `Omega`, disturbing at most `H` named target loads and extendable to the
declared owner/lower-`q1` factor, exists if and only if there are binary
variables `x_e` and `y_t` satisfying

\[
\begin{aligned}
 \sum_{e\in\delta^+(v)}x_e&=1=
      \sum_{e\in\delta^-(v)}x_e &&(v\in\Omega),                 \tag{5.1}\\
 \sum_{e\in\delta^+(X)}x_e&\ge1
      &&(\varnothing\ne X\subsetneq\Omega),                     \tag{5.2}\\
 \sum_{e:r\in R_e}x_e&\le1 &&(\text{every unit resource }r),   \tag{5.3}\\
 -M_ty_t\le\sum_e\Delta_e(t)x_e&\le M_ty_t
      &&(\text{every named target }t),                          \tag{5.4}\\
 \sum_t y_t&\le H,                                             \tag{5.5}
\end{aligned}
\]

together with all literal target-reproduction/common-cap equations and

\[
       P(x)\text{ simple of maximum degree two},\qquad
       \delta_{\rm star}(P(x),Z)=0.                              \tag{5.6}
\]

Here `M_t` is any valid absolute bound on the signed load change, and
`delta_star` is the exact guarded Ore--Ryser deficiency of
`MATH_THEOREM_L_ORBIT_WEIGHTED_ACTUATOR_PLANTING_AND_GUARDED_STAR_CUT_20260801.md`.

#### Proof

Equations (5.1) make the selected arcs a disjoint union of directed cycles;
(5.2) leaves exactly one cycle.  Equations (5.3)--(5.5) are precisely the
declared resource and net-load disturbance conditions.  The literal bundle equations
preserve arbitrary-width upper witnesses and the same trace/common-cap
cells.  Finally, (5.6) is necessary and sufficient for the selected
incidence bank to extend while avoiding `Z`.  Conversely, projecting any
protected one-cycle chronology gives every displayed row. \(\square\)

At type multiplicity level, (5.1)--(5.2) become the compact integral
circulation system

\[
 \sum_{c'}f_{cc'}=m_c=\sum_{c'}f_{c'c},\qquad
 \sum_{c\in X,c'\notin X}f_{cc'}\ge1                            \tag{5.7}
\]

for every nonempty proper active type set `X`.  A connected balanced
multidigraph has an Euler tour, which expands to one successor cycle once
its parallel arcs have occurrence-private literal bundle representatives
and, at every type, an endpoint-state-conserving matching pairs incoming
literal heads to outgoing literal tails.  Without that state-conserving
representative matching, (5.7) is only a type certificate.

## 6. The exact `O(1)`-disturbance boundary

Contract the forced rotation necklaces and suppose a merge macro replaces
the appropriate baseline arcs of two components.  Call a selected macro set
**serial-safe** when it has a rooted leaf order in which every macro's
deleted baseline arcs still exist when processed, its ports are distinct
from all earlier ports, and the switch merges two current components without
splitting either.  This is stronger than pairwise resource-disjointness.
Within such a catalogue, fusion reduces exactly to selecting a
resource-compatible, serial-safe spanning tree of the contracted merge
graph, with the same payload equations (5.3)--(5.5).

Two opposite consequences are immediate.

1. If the payload-zero merge graph contains a resource-compatible spanning
   tree and the resulting incidence bank passes (5.6), all necklaces fuse
   with **zero** named-load disturbance.
2. If every merge macro exposes a source-private changed target, any fusion
   of `kappa` necklaces disturbs at least `kappa-1` named targets.  More
   generally, after contracting the payload-zero merge graph, at least one
   paid macro is needed across every component cut.  Under private additive
   payloads, `H` disturbed targets is possible only if that quotient can be
   connected with at most `H` paid macro edges.

The raw core-free catalogue has no edge between distinct necklaces by
Theorem 3.1, so it is on the negative side of this dichotomy.  Transparent
`C6`/longer macros can evade the private-load lower bound, but their
resource-compatible spanning tree, literal upper tickets, and guarded
star cuts are then exactly the missing theorem.  Pairwise owner/`q1`
disjointness of the open strands does not imply any of these connector
cuts, even asymptotically.

## 7. Correct frontier

The proof-safe implication chain is

\[
\boxed{
\begin{array}{c}
\text{canonical triangular vector in normalized fractional }ST
       \quad\text{proved}\\
\Downarrow\\
\text{raw complete core-free rotor fusion}
       \quad\text{impossible}\\
\text{positive-core split rotor / transparent off-rotor macros}
       \quad\text{live}\\
\Downarrow\\
\text{one connected literal-bundle circulation + guarded star cuts}
       \quad\text{exact gate}\\
\Downarrow\\
\text{rooted opening and final compiler chronology}
       \quad\text{still open}.
\end{array}}
\]

Thus owner-changing connectors do **not** fuse the forced core-free
positive-composition necklaces at `O(1)` cost.  The weakest viable integral
rotor-fusion theorem must exhibit either a Hamilton assignment in a
positive-core split-rotor host or a payload-transparent, resource-compatible
spanning merge system satisfying the literal factor/compiler cuts.
