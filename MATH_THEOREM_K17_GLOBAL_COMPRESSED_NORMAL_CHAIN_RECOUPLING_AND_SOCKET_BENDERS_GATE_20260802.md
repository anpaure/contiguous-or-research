# K17 global compressed-normal chain recoupling and the exact socket Benders gate

**Date:** 2026-08-02  
**Status:** proof-complete static flow/common-basis theorem on the
compressed-normal face, exact fixed-root SCC obstruction, one independently
replayed force-623 static table, and an exact non-TU branch--Hall interface for
short sockets.  The force-623 table fails its two-phase marginal DNF census.
No simultaneous ticket packing, supplier-perfect selected state, chronology,
residence, upper/source/compiler closure, or word is claimed.

## 1. Exact outcome

Let

\[
 L=\bigcup_{s=1}^{6}{[17]\choose s},\qquad
 M={[17]\choose7},\qquad R={[17]\choose8},
\]

with sizes `21,777`, `19,448`, and `24,310`.

The exact global compressed-normal chain problem is integral.  Its variables
are

\[
 x_{mr}\quad(m\in M,r\in R,m\subset r)
\]

and

\[
 y_{lm},y_{lr}\quad(l\in L,l\subset m\text{ or }l\subset r).
\]

The equations are

\[
\begin{aligned}
 \sum_{r\supset m}x_{mr}&=1 &&(m\in M),\\
 \sum_{m\subset r}x_{mr}+\sum_{l\subset r}y_{lr}&=1 &&(r\in R),\\
 \sum_{m\supset l}y_{lm}+\sum_{r\supset l}y_{lr}&=1 &&(l\in L),\\
 \sum_{l\subset m}y_{lm}&\le1 &&(m\in M).
\end{aligned}                                                   \tag{1.1}
\]

This is one bipartite `b`-matching and its matrix is totally unimodular.
The equations force

\[
 \sum y_{lm}=16,915,\qquad \sum y_{lr}=4,862,
\]

and exactly `2,533` rank-seven targets have no low predecessor.  Hence every
integral solution has

```text
L-M-R chains       16,915
L-R chains          4,862
M-R chains          2,533
lengths (1,2,3) (0,7,395,16,915).
```

On H100, deleting every `M -> R` edge into the `623` old rank-seven
union-zero P2 roots still gives full flow

```text
43,758 / 43,758,
```

not a cut.  The emitted table retires all `623/623` roots from the rank-seven
receiver basis, preserves all `65,535` targets and every root/owner, and
changes `1,308` physical rows.  Its table SHA-256 is

```text
6e5f4cf4e083d265f051fc2cc530a3703f321083e4f7411b529983575b02e8d9.
```

An independent implementation replays the complete target table and the
common-basis projections.

This static success is not a socket success.  On the selected long modes of
the emitted table, the two transported owner phases have

\[
\begin{array}{c|rr}
 &\text{positive}&\text{zero}\\ \hline
\phi=0&1,402&5,993\\
\phi=1&1,408&5,987.
\end{array}
\]

Only `1,057/7,395` short roles are positive in both phases, so the union-zero
count is `6,338`.  Among the `623` forced root-type replacements, only `30`
are positive in both phases and `593` remain union-zero.  Therefore the
deterministic force-all table is rejected by the marginal DNF gate.

## 2. Scope correction: compressed normality is load-bearing

The histogram `(0,7395,16915)` alone does not force every three-member chain
to meet `L,M,R` once.  If `a` chains have type `L-L-R`, where necessarily
`0 <= a <= 4,862`, the remaining shape counts may be

\[
\begin{array}{c|r}
L-L-R&a\\
L-M-R&16,915-a\\
L-R&4,862-a\\
M-R&2,533+a.
\end{array}                                                   \tag{2.1}
\]

All level and length counts are unchanged.  Equations (1.1), the common-base
theorem below, and every finite table in this note are therefore explicitly
on the **compressed-normal face** `a=0`.  No claim is made that all
no-singleton histograms have this form.

## 3. The root-bank matroid layer

Let `T_7` be the rank-`19,448` transversal matroid on ground set `R` induced
by rank-seven containment.  Let `T_L` be the rank-`21,777` transversal
matroid on ground set `M disjoint-union R` induced by low-target containment.
Put

\[
             N=T_7^*\oplus U_{16,915,M}.                    \tag{3.1}
\]

### Theorem 3.1 (compressed-normal common bases)

A set `C subset M disjoint-union R` is a common basis of `T_L` and `N` if
and only if it supports a compressed-normal table satisfying (1.1).

Indeed,

\[
 |C\cap M|=16,915,\qquad |C\cap R|=4,862.                  \tag{3.2}
\]

The `T_L` basis matching gives the `L -> M/R` edges.  Since `C cap R` is a
basis of `T_7^*`, its complement

\[
                    B=R\setminus(C\cap R)                  \tag{3.3}
\]

is a `T_7` basis; a representing matching gives every `M -> B` edge.
Conversely, the two edge layers of any compressed-normal table give these
two basis witnesses.

Thus the projected static problem also has Edmonds' exact common-base rows

\[
 r_{T_L}(X)+r_N((M\dot\cup R)\setminus X)\ge21,777
 \quad(X\subseteq M\dot\cup R).                            \tag{3.4}
\]

The root type is now transparent.  `B` is the set of roots receiving
rank-seven targets.  A root-basis exchange is an ordinary fundamental
alternating path in the `T_7` representation; it can retire a bad physical
root from `B` and insert another root.  One need not keep or repair the same
old P2 label.

The finite force-623 table has

```text
rank(T_L)=21,777       |C cap M|=16,915
rank(T_7)=19,448       |C cap R|= 4,862
                       |B|       =19,448.
```

The displayed chain edges are explicit matching witnesses for both ranks.

## 4. Fixed-root SCC ladder

Contract the current matching between rank-seven labels and the `19,448`
rank-eight receiver roots.  Direct an arc from label `m_i` to receiver slot
`j` when `m_i` can enter that root; for a long slot, retain the strict lower
containment whenever the face says the bottom is fixed.  A label can occur
in a nonidentity fixed-root reassignment only inside a nontrivial strongly
connected component.

The independently frozen ladder on the `623` old rank-seven union-zero P2
roles is

\[
\begin{array}{l|rr}
\text{face}&\text{movable}&\text{stuck}\\ \hline
\text{current long slots, protected endpoint hosts excluded,
fixed bottoms}&138&485\\
\text{all current long slots, fixed bottoms}&194&429\\
\text{also all 1,748 short-H slots}&220&403\\
\text{all 19,448 slots, every lower-bottom constraint deleted}&461&162.
\end{array}                                                \tag{4.1}
\]

The final graph has

```text
vertices                 19,448
nonidentity arcs        136,136
SCCs                         421
largest SCC              18,953.
```

Hence `162` bad labels are singleton SCCs even on the bottom-free fixed-root
supergraph.  No fixed-root suffix-circuit packing can move each of the 623
bad labels.  Root-basis exchange or another root-changing architecture is
necessary for a move-each-defect strategy.

This does not exclude indirect repair of an unchanged P2 role by endpoint
modes created when other H middles move.

## 5. Local C4/C6 moves inside the global flow

The authenticated local moves are fundamental circuits of (1.1), but only
on their fixed branch faces.

1. The P2 prefix square is an alternating `C4` between two low targets and
   two root receiver slots in the `y` layer.
2. The rank-seven/rank-eight containment graph has no `C4`.  Its first
   nonidentity circuit is a `C6`, giving the P2--H--H suffix rethread in the
   `x` layer.
3. Changing `B`, or changing whether a middle is hit by a low target, crosses
   these fixed faces.  The full symmetric difference can be a longer
   alternating path/circuit coupling the `x` and `y` layers.

Thus C4/C6 enumeration is a proof-safe harvesting language, not a complete
replacement for the global common-base or `b`-matching master.

## 6. Proof-safe marginal socket variables

For a direct low short, activation is simply

\[
                         q_{lr}=y_{lr}.                      \tag{6.1}
\]

Put

\[
                         h_m=\sum_l y_{lm}\in\{0,1\}.       \tag{6.2}
\]

The rank-seven short on edge `mr` is active when `x_mr=1` and `h_m=0`.
For a frozen complete long-mode branch, let `p_mr` be one exactly when this
short role has an accepted common-phase DNF.  Then

\[
 x_{mr}\le p_{mr}+h_m.                                     \tag{6.3}
\]

Since `sum_r x_mr=1`, the exact integral strengthening is

\[
             \sum_{r:p_{mr}=0}x_{mr}\le h_m.               \tag{6.4}
\]

Direct `L -> R` edges with empty short DNFs are deleted on that same frozen
branch.

The word *frozen* is essential.  Moving a long bottom, middle, root, owner,
flag, or endpoint resource can create or destroy a ticket.  A zero computed
on one selected table is not an unguarded global edge deletion.

## 7. The socket-labelled lift is not TU

The structural matrix (1.1) is TU, but adjoining (6.3) is not.  For one
middle with two bad root arcs, restrict the middle-output equation and the
two implication rows to columns `x_1,x_2,y_lm`.  The minor is

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&-1\\
 0&1&-1
 \end{pmatrix},
 \qquad \det=2.                                            \tag{7.1}
\]

Even the strengthened aggregate formulation (6.4) has a half-integral
basic feasible solution on a two-low/two-middle/three-root instance; it can
be padded by disjoint forced components to the exact K17 counts.  Therefore
no total-unimodularity conclusion follows from state expansion.

More generally, perfect three-dimensional matching reduces explicitly to
the socket-labelled abstract problem.  Reject as an immediate `NO` instance
if some `c` occurs in no triple; hence assume every `k_c >= 1`.  For an
instance `T subset A times B times C`, with all three shores of size `n`, create one
low vertex `l_a` for each `a` and one middle `m_t` for each triple.  For each
`b`, create a global root `r_b`.  If `c` occurs in `k_c` triples, also create
`k_c-1` private roots for `c`.  Join `l_a` to exactly the middles whose
triples contain `a`; join `m_(a,b,c)` to its global root `r_b` by a
socket-negative edge and to every private root of its `c`-group by a
socket-positive edge.  There are no direct low--root edges.

The root count is

\[
 |B|+\sum_c(k_c-1)=n+|T|-n=|T|=|M|.
\]

Consequently the upper matching is perfect.  Every `c`-group must send at
least one middle to a global root, and the `n` groups and `n` global roots
force exactly one per group.  Root injectivity makes their `b` coordinates
distinct.  Precisely those `n` global-root edges are socket-negative, so
the implication rows and absence of direct low--root edges force the `n`
low vertices to match to those middles; the lower matching makes their `a`
coordinates distinct.  Thus the global-root triples form a perfect 3D
matching, and any perfect 3D matching gives the converse table.  The
decision problem is in `NP`, so the general labelled problem is
`NP`-complete.  Hence a uniform polynomial pure-flow formulation would
imply `P=NP`.  This is not a hardness claim for the one fixed K17 dataset.

## 8. Exact branch--Hall/Benders interface

For a frozen phase/mode screen `p`, Sections 8.1--8.2 give the
**hard-positive** feasibility oracle: every selected short is required to
have a positive ticket.  In the priced optimization of Section 8.3, an
edge whose role is assigned `c=0` is retained structurally and charged in
the objective; the Hall rows are activated only with the corresponding
required-positive branch guards.  With that convention there are two
equivalent proof-safe decompositions.

### 8.1 Branch on hit states

Fix binary `h_m` with

\[
                         \sum_m h_m=16,915.                  \tag{8.1}
\]

Set the lower degree of receiver `m` to `h_m` and delete every
socket-negative `m -> r` edge when `h_m=0`.  Conditional on this branch, the
complete structural `x+y` row is again one bipartite `b`-matching and is
integral.  A maximum flow returns either a table or a Hall shore.

### 8.2 Branch on the upper matching

Fix integral `x` and put

\[
 z_r=\sum_mx_{mr},\qquad
 b_m=\sum_{r:p_{mr}=0}x_{mr}.                              \tag{8.2}
\]

The lower matching has right capacities

\[
 c_m=1,\qquad c_r=1-z_r,                                  \tag{8.3}
\]

and lower demands

\[
 d_m=b_m,\qquad d_r=1-z_r.                                \tag{8.4}
\]

Its exact projected cuts are, for `A subset L`,

\[
 |A|\le |N_M(A)|+\sum_{r\in N_R(A)}(1-z_r),               \tag{8.5}
\]

and, for `W=W_M disjoint-union W_R subset M disjoint-union R`,

\[
 \sum_{m\in W_M}b_m+\sum_{r\in W_R}(1-z_r)
       \le |N_L(W)|.                                      \tag{8.6}
\]

Here the direct-root neighborhood uses only DNF-positive edges on the
declared branch.  The two Hall families are necessary and sufficient; a
single lower-bounded matching flow separates them.

For literal tickets, replace `p` by occurrence variables.  Let `s_mr` be the
active rank-seven short indicator, with the exact binary linearization

\[
 s_{mr}\le x_{mr},\qquad s_{mr}\le1-h_m,\qquad
 s_{mr}\ge x_{mr}-h_m.                                  \tag{8.7}
\]

For a short required to be positive, impose

\[
       \sum_{g\in\mathcal G(m,r)}\lambda_g=s_{mr},          \tag{8.8}
\]

where every `lambda_g` implies its complete table, outer-placement, address,
flag, endpoint, and physical-cell DNF.  Direct shorts have the analogous
hard-positive exact-one row.  The optimization below instead puts its
phase-positivity bit on the right-hand side, allowing a priced zero.  A
common-phase role may use different authenticated
occurrences in the two phases; one shared occurrence is a stronger condition
and is not assumed.

### 8.3 Exact two-phase objective

For every physical row `w`, let `a_w` say that the selected chain is short;
the structural equations give `sum_w a_w=7,395`.  In each phase `phi`, let
`c_w^phi` be its positive-ticket selection bit, with an exact-one selector
among complete eligible occurrences:

\[
 \sum_{g\in\mathcal G_\phi(w)}\lambda^phi_{wg}=c_w^\phi,
 \qquad c_w^\phi\le a_w,                                \tag{8.9}
\]

with each ticket also implying the selected direct `y_lr` edge or selected
rank-seven-short `s_mr` edge that owns it.  Introduce `b_w` with

\[
 b_w\le c_w^0,\qquad b_w\le c_w^1,\qquad
 b_w\ge c_w^0+c_w^1-1.                                  \tag{8.10}
\]

The exact compressed-normal marginal objective requested here is

\[
       \max\sum_w b_w
       \quad\Longleftrightarrow\quad
       \min\left(7,395-\sum_w b_w\right).                \tag{8.11}
\]

The right-hand expression is the selected union-zero count.  Protected
private tickets are fixed to one only together with their complete
root/owner rows and forced outer placements; an incompatible root exchange
is excluded on that protected face.  Lower matching Hall and selected-parent
supplier Hall are separated lazily after the branch literals are applied.
Thus (8.11) is a branch-and-Hall master, not an element-weight objective for
the common-base oracle.

## 9. Protected tickets and supplier Hall

The phase-zero protected object is the full tuple

\[
                       (S_H,\tau,E_B;\mu_B),                \tag{9.1}
\]

not just a 1,748-element short set.  It fixes `1,748` literal tickets,
`3,496` distinct directed endpoint hosts, `3,495` movable endpoint
placements, and one soft endpoint; `mu_B` exhibits an extending outer
matching.  The residual edges of that exhibited completion are a witness,
not protected fixed data.  The bank may be contracted in the global master
only while its exact root/owner rows, tickets, endpoint hosts, forced
placements, and soft endpoint remain literal.  It is not transported
automatically to either s7 owner phase.

On its authenticated owner phase, all `1,748/1,748` tickets remain positive.
The complete selected-table marginal census is

```text
positive 2,687 / 7,395
zero     4,708 / 7,395.
```

After tickets and states are selected, let `n_(Q,u)` be the bidirectional OR
that distinct physical supplier identity `u` has an active occurrence into
hard-head shore `Q`.  On the face contracting the protected short set `S_H`,
the exact residual supplier row is

\[
                  \sum_u n_{Q,u}\ge |Q\setminus S_H|.       \tag{9.2}
\]

The first instantiated protected-face selected-state shore has `109` heads
and only `7` active supplier identities.  Its exact Benders row is

\[
                         \sum_u n_{Q_*,u}\ge109,             \tag{9.3}
\]

with incumbent deficiency `102`.  Counting occurrence records instead of
distinct suppliers, or retaining a record after one signed support literal
changes, is unsound.

The protected phase therefore supplies an exact joint cut, not a promoted
endpoint.

## 10. Certified marginal frontier

All numbers below use the same selected-table relaxed-nine marginal pricer
on all `7,395` compressed-normal short roles.  They do not assert ticket
packing or supplier Hall.

\[
\begin{array}{l|rrr}
\text{table skeleton}&\phi_0\text{ positive}&\phi_1\text{ positive}
 &\text{union zero}\\ \hline
\text{raw warm47}&1,371&1,369&6,379\\
\text{force all 623 roots direct}&1,402&1,408&6,338\\
\text{private-outer skeleton transported to s7 phases}&1,904&1,891&5,923.
\end{array}                                                \tag{10.1}
\]

The last row is the best audited **marginal** objective, `5,923`.  Its s7
transport does not inherit the authenticated private tickets.  The only
authenticated protected result is the single original-owner phase in
Section 9, and it still violates the selected-state supplier row (9.3).

The old number `1,641` is a different objective: it is the union-zero count
on `3,899` immutable P2 roles against the much larger potential-mode union.
It must not be compared numerically with (10.1).

No table in (10.1) is a certified joint two-phase ticket-packed,
supplier-perfect solution.  The correct next optimization is (8.1) or
(8.2), with exact ticket activation and lazy lower/supplier Hall separation,
not another unconditioned force-root objective.

## 11. Frozen artifacts

The principal source and result hashes are

```text
raw warm47 input
95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735

global flow producer
85372d9eba8e253b6f0c6fb12a883b4f1fb2cd5daff11478271d257e9f91c404
force-623 table
6e5f4cf4e083d265f051fc2cc530a3703f321083e4f7411b529983575b02e8d9
producer audit
22d3466e10134a6ebcdecc3a1da893e3e34540d341e77a7eba4836227b92ab5f
independent common-basis/table audit
f268a1a41c45eb050779e489d20553540e648da41ba47bfacb8e357e5cde9e6f

phase-0 force-623 DNF census
21d14d1c86b76a9ab2c45ea15c963ae9f113f8acd3563fcc7f2623f27cfba5a7
phase-1 force-623 DNF census
c83e24810027c4a3ebf3e0414522c6ca73e8431157c16726009ac5d305d6bda3
DNF negative summary
a667c1a33405dd9ff5e7ee0880fb4c70806ce5b026f9b189d5c152bbff66421e

SCC ladder source
c44c539c7abd4124352aa8ca891326c6481c3cce486c22d2caa41c2004a3e1d7
SCC ladder summary
a68f1b2a8b40a95bd68a42a38f73ed5aae48a43aaba21b920129d453b4246ee4

audited compressed-normal DNF pricer in the persistent H100 root
5c4a9c6d3e32efce5609a9a217f3df04731b139037e8d8304245a7d48763427f
local generalized-parser derivative, not used to emit the audited censuses
b010a50a2d0cc3fb5ba3bbac7bbaabc7d27b652539644450e1e12354639198a8
frontier/cut audit
96d071bad516c9a3ea9525436935b54543097f5aba3772fcfaf326d81c3e26a6
```

The load-bearing theorem inputs, frozen at the bytes used here, are

```text
three-level normal chainization
1f285da227549171997362454cf5039ae690cc3f8af5f82033cc2406e2e8d9a4
root common-base reduction (restricted here by Section 2)
eb158c0b78926857730e4f195236c33d13f8332cf297c95448372508123927cc
immutable P2 prefix/suffix circuits
a2dac3f683a6d418fa4fceb50e4acd738136998b8a58687d7c1b2be5106c0da3
immutable P2 kernel prefix C4
116242844fa5479ae49905e69e7d98179f8e7de25e9fd0a7332dab2f86ed6377
P2--H two-row/C6 classification
80a3a8b309cc504b0504dddf44bde9e51e1f69dba01c0fcb4558e8e430d0007d
private outer-basis theorem
ad00f320deba5c0cea6e728e3cd3febfb3ad490a6cf0d0a953968575bd328c8e
protected-H branch-flow theorem
854fbeb30cebc817a4ca8a0356d6a01878871c506ba64f700bd5cd0cb82ed8ad
private materialized baseline audit
037a3c4570d24c53428d6cb1d013b34c7b6898184933847d328c47c5cada4825
signed supplier-Hall/Pareto theorem
e1a1b37514378121151966fddda3b3bde5920883c327b22fca4236590418433e
```

The local bundle is

```text
scratch/k17_global_chain_recoupling_20260802/
```

and the unique persistent H100 root is

```text
/home/amodo/or15/work/root_k17_global_chain_recoupling_019fc2f9_20260802/
```

The static table and DNF outputs are exact finite artifacts.  They do not
promote a carrier, compiler, or word.
