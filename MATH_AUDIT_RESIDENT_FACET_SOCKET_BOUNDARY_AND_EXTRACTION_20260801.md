# Audit of the resident facet socket: exact boundary state and protected extraction ledger

Date: 2026-08-01  
Audited source: `MATH_THEOREM_RESIDENT_FACET_SOCKET_20260801.md`  
Status: the internal owner path, upper/lower palette calculation, and the
staircase ages are correct.  The claim that those staircase ages are the
*only* exported residence obligations is false in an arbitrary chronology.
This note gives the missing clean-cut conditions, an exact fixed-boundary
Hall test, and the protected extraction/cascade ledger.  No global socket
availability or cascade closure is claimed.

## 1. Verdict and the first false implication

Write

\[
                         H=h+1
\]

for the required positive-run length.  Inserting a block can do two
different things at one of its boundaries:

1. continue a positive exterior run into a positive initial or terminal
   run of the block; or
2. terminate an exterior run because the first or last block owner has a
   zero in that coordinate.

Equations (1.6) and (1.8) of the source account for the first effect on the
selected labels.  They do not account for the second effect on the endpoint
omitted label or on a coordinate outside the target `U`.

This omission makes the consequence following (1.6), and the analogous
consequence following (1.8), false without a clean-cut hypothesis.

### A literal `h=1` counterexample

Let

\[
 U=\{a,b,c,d\},\qquad v_0=a,\quad v_1=b,
\]

and consider the rank-three Johnson path segment

\[
 \{b,c,e\},\ \{b,c,x\},\
 \underbrace{\{b,c,d\},\ \{a,c,d\}}_{
              U-v_0,\ U-v_1},\
 \{a,c,e\},                                      \tag{1.1}
\]

where `x` is outside `U`.  The compact socket has the two required guards:
the owner immediately to its left contains `v_1=b`, and the owner
immediately to its right contains `v_0=a`.  Thus (1.8) holds.

However, the trace of `x` on (1.1) is

\[
                              0,1,0,0,0.
\]

It has a positive run of length one, below `H=2`.  The socket terminated a
short exterior suffix which was invisible to (1.8).  All consecutive
owners in (1.1) are Johnson-adjacent, so this is not an artefact of using an
illegal owner sequence.

The same construction placed before the long socket refutes the
corresponding unrestricted consequence of (1.6).

## 2. General exact boundary lemma

Let

\[
                           B=(B_0,\ldots,B_{n-1})
\]

be a binary owner block.  For a coordinate `x`, let

* `a_x` be the length of the initial all-one run of the `x`-trace on `B`;
* `b_x` be the length of its terminal all-one run;
* `ell_x` be the all-one suffix age immediately before `B`;
* `rho_x` be the all-one prefix age immediately after `B`.

The ages `ell_x,rho_x` may be zero.  Call an age **clean** when

\[
                         q=0\quad\hbox{or}\quad q\ge H.       \tag{2.1}
\]

Assume every positive run strictly internal to `B` already has length at
least `H`, and assume `n>=H`.  Then no new short positive run meeting `B`
is created if and only if the following coordinatewise conditions hold:

\[
\begin{array}{c|c}
a_x=0&\ell_x\text{ is clean},\\
0<a_x<n&\ell_x+a_x\ge H,\\
a_x=n&\text{no left condition},
\end{array}
\qquad
\begin{array}{c|c}
b_x=0&\rho_x\text{ is clean},\\
0<b_x<n&\rho_x+b_x\ge H,\\
b_x=n&\text{no right condition}.
\end{array}                                             \tag{2.2}
\]

Indeed, these are exactly the six possible ways in which a run can meet a
boundary of `B`.  This proves both necessity and sufficiency.

The clean alternative in the first and fourth rows of (2.2) is essential:
when the block begins or ends with zero, an exterior positive run is not
extended by the block at all.

## 3. Corrected compact socket and its exact Hall test

Let

\[
 B_j=U-\{v_j\},\qquad 0\le j\le h,                  \tag{3.1}
\]

where the `v_j` are distinct.  A selected label `v_j` has

\[
                         a_{v_j}=j,\qquad b_{v_j}=h-j. \tag{3.2}
\]

A label in `U-{v_0,...,v_h}` has `a_x=b_x=h+1`, and a
coordinate outside `U` has `a_x=b_x=0`.  Therefore (2.2) gives the exact
compact boundary conditions:

\[
\begin{array}{rll}
v_0:&\ell_{v_0}\text{ clean},&\rho_{v_0}\ge1,\\
v_j\ (1\le j<h):
     &\ell_{v_j}\ge h+1-j,&\rho_{v_j}\ge j+1,\\
v_h:&\ell_{v_h}\ge1,&\rho_{v_h}\text{ clean},
\end{array}                                             \tag{3.3}
\]

together with

\[
 \ell_x,\rho_x\text{ clean for every }x\notin U.       \tag{3.4}
\]

There is no condition on an unselected label of `U`, because its run
contains all `h+1` block positions.

For fixed exterior pieces and fixed target `U`, define

\[
\begin{aligned}
A_0&=\{x\in U:\ell_x\text{ clean and }\rho_x\ge1\},\\
A_h&=\{x\in U:\ell_x\ge1\text{ and }\rho_x\text{ clean}\},\\
A_j&=\{x\in U:\ell_x\ge h+1-j,\ \rho_x\ge j+1\},
       \qquad 1\le j<h.                               \tag{3.5}
\end{aligned}
\]

Fix a physical guard-retention state as well.  For each socket position
`j`, let `E_j` be the labels whose facet is physically eligible there;
in particular `E_0,E_h` encode Johnson adjacency to the two fixed
exterior pieces.  Put

\[
                              C_j=A_j\cap E_j.          \tag{3.5a}
\]

### Proposition 3.1 (exact fixed-boundary compact feasibility)

Assume (3.4).  A compact resident facet socket for `U` exists between the
two fixed exterior pieces, in the fixed physical guard state, if and only
if the family

\[
                             C_0,C_1,\ldots,C_h
\]

has a system of distinct representatives.  Equivalently,

\[
                 \left|\bigcup_{j\in J}C_j\right|\ge |J|
                 \quad\hbox{for every }J\subseteq\{0,\ldots,h\}. \tag{3.6}
\]

Choosing the representative of `C_j` as `v_j` proves sufficiency by
(3.3) and physical eligibility.  Necessity follows from (2.2) and the
two exterior Johnson joins.  Thus the local availability gate is an
ordinary Hall row once the exterior pieces and guard state are fixed.
If guard retention is not fixed, exact feasibility is the finite
disjunction of (3.6) over the possible guard states.  The simpler choice
`E_j=U` is exact only when physical endpoint compatibility is supplied
separately.

The compact construction itself only needs

\[
                              r\ge h,                  \tag{3.7}
\]

so that the `(r+1)`-set `U` contains `h+1` distinct labels.  The stronger
source assumption `r>=2h+1` is needed for the long socket, not for the
compact one.

## 4. Corrected long socket

For the long block

\[
                        B_j=U-\{u_j\},\qquad 0\le j\le2h+1,
\]

the exact conditions are:

\[
\begin{array}{rll}
u_0:&\ell_{u_0}\text{ clean},&\text{no right condition},\\
u_j\ (1\le j\le h):
     &\ell_{u_j}\ge h+1-j,&\text{no right condition},\\
u_j\ (h+1\le j\le2h):
     &\text{no left condition},&\rho_{u_j}\ge j-h,\\
u_{2h+1}:&\text{no left condition},&\rho_{u_{2h+1}}\text{ clean},
\end{array}                                             \tag{4.1}
\]

plus clean `ell_x,rho_x` for every `x` outside `U`.  Unselected labels of
`U` need no condition.  The selected labels in the middle of (4.1) agree
with (1.6); the first, last, and outside-`U` clean rows are the missing
conditions.

The long socket needs `2h+2` distinct labels in `U`, hence precisely
`r>=2h+1`.

## 5. Exact extraction and topology ledger

Let `F` be an incumbent linear owner forest, and suppose `U` is absent
from its immediate-upper seam deck.  Then the facets of `U` form an
independent set in `F`: an edge joining two distinct facets of `U` would
have union exactly `U`.

Choose the `n=h+1` facets

\[
                         X=\{U-v_0,\ldots,U-v_h\}.       \tag{5.1}
\]

Let `K` be the set of old incidences retained as the left and right socket
guard edges, so `|K|<=2`.  Since `X` is independent, the exact number of
deleted old edges is

\[
                         q=\sum_{F\in X}\deg_F(F)-|K|.  \tag{5.2}
\]

In a cyclic two-regular owner factor this becomes

\[
                         q=2h+2-|K|.                   \tag{5.3}
\]

Thus two retained old guard incidences give `q=2h`, one gives `2h+1`,
and two newly attached guards give `2h+2`.  In a linear factor, every
selected global endpoint lowers (5.3) by one.  Formula (5.2), rather than
the crude `2(h+1)`, is the exact all-factor statement.

The socket adds `h` internal edges.  If the number of components of the
linear forest is to remain unchanged, exactly

\[
                              q-h                    \tag{5.4}
\]

additional connector edges are required.  Adding `s` further acyclic
connectors merges `s` old components; deleting `s` fewer leaves `s`
additional components.  This is the exact graphic row.  It is not implied
by the local socket theorem.

## 6. Signed upper and lower resource ledger

Let `D` be the deleted edge set, and let `J` be the new connector edge set
outside the `h` socket edges.  For a seam `e`, write

\[
                 R(e)=\operatorname{union}(e),\qquad
                 Q(e)=\operatorname{intersection}(e).
\]

The exact immediate-upper signed change is

\[
 \Delta^+
   =h\,\mathbf e_U
    +\sum_{e\in J}\mathbf e_{R(e)}
    -\sum_{e\in D}\mathbf e_{R(e)},                  \tag{6.1}
\]

and the exact immediate-lower signed change is

\[
 \Delta^-
   =\sum_{j=0}^{h-1}
       \mathbf e_{U-\{v_j,v_{j+1}\}}
    +\sum_{e\in J}\mathbf e_{Q(e)}
    -\sum_{e\in D}\mathbf e_{Q(e)}.                 \tag{6.2}
\]

The owner multiset does not change.  The `h` internal lower colours in
(6.2) are pairwise distinct.  They are not automatically useful lower
colours: in an exact lower-rainbow factor they must, together with the
connector intersections, reproduce the deleted lower-colour multiset.
Equation (6.2), not distinctness alone, is the lower/compiler gate.

As an upper *resource*, the socket installs the one missing target `U`.
As an upper *occurrence deck*, it installs `h` copies.  After paying for
one missing target it has `(h-1) e_U` occurrence surplus.  Any cap or
endpoint-degree calculation must retain this distinction.

## 7. Protected child-colour branching

For an old upper colour `R`, let `P_R` be its complete incumbent provider
edge set.  After the replacement, `R` is a child hole exactly when

\[
                  P_R\subseteq D
   \quad\hbox{and no new edge has upper colour }R.     \tag{7.1}
\]

Consequently the child set `Gamma^+` satisfies

\[
                              |\Gamma^+|\le q.          \tag{7.2}
\]

The analogous lower casualty set also has size at most `q`, before using
the `h` internal lower colours and the connectors.  This is a branching
bound, not a subcriticality theorem: even the protected two-guard value
`q=2h` exceeds one.

There is, however, a proof-safe zero-branching criterion.  Fix one protected
witness edge `b_R in P_R` for every already covered upper colour outside a
terminal absorber family `A`.  If

\[
                   D\cap\{b_R:R\notin A\}=\varnothing,            \tag{7.3}
\]

then every child lies in `A`.  More generally, it is enough that each
`R notin A` retain any provider outside `D`; (7.3) is the convenient
fixed-basis sufficient form.

### Proposition 7.1 (protected extraction/cascade lemma)

Suppose a finite family of distinct missing targets is processed by
pairwise owner-disjoint compact sockets.  Interpret all deleted edges as
one global set; in particular, either the socket cut sets are edge-disjoint
or a shared cut edge is charged only once.  Assume that:

1. every socket satisfies the corrected boundary Hall test (3.4)--(3.6);
2. every non-socket connector is residence-legal;
3. the graphic count (5.4) and the desired component merges hold;
4. (6.2) is zero, or equals a declared lower-reservoir debt vector;
5. every deleted upper witness either retains another provider or belongs
   to a declared terminal absorber family `A`.

Then simultaneous extraction and rethreading repairs all processed upper
targets, creates no upper holes outside `A`, preserves the owner multiset,
and has exactly the declared lower debt and component change.

This follows by summing (6.1)--(6.2) over the global edge sets; item 5
cancels every negative upper
coordinate outside `A`, while each processed target receives `h>=1`
socket witnesses.  Pairwise owner disjointness prevents double use of a
facet.  The proposition is deliberately conditional: finding the sockets,
guards, connectors, and protected witness basis jointly is the remaining
global theorem.

## 8. A weighted subcritical alternative

Let each nonterminal target `R` have a positive weight `w(R)`.  If one can
choose every socket so that its child set obeys

\[
                  \sum_{S\in\Gamma^+(R)}w(S)
                     \le\theta w(R),\qquad \theta<1,              \tag{8.1}
\]

then a cascade started from `D_0` has total processed weight at most

\[
                  {\sum_{R\in D_0}w(R)\over1-\theta}.             \tag{8.2}
\]

If `w_min` is the minimum nonterminal weight, the number of sockets is at
most the right side of (8.2) divided by `w_min`.  Hence their selected
owners, deleted seams, and internal lower resources are at most

\[
 (h+1)T,\qquad (2h+2)T,\qquad hT,                    \tag{8.3}
\]

respectively.  This is the exact sense in which a protected weighted
cascade would be subcritical.  The raw bound (7.2) by itself supplies no
such `theta`.

## 9. The local lower-incidence phase options

Put

\[
                         K_j=U-\{v_j,v_{j+1}\},
                         \qquad 0\le j<h.              \tag{9.1}
\]

Each `K_j` may be assigned to the left facet `F_j=U-v_j` or the right
facet `F_{j+1}=U-v_{j+1}`.  Owner injectivity forbids a right assignment
at `j-1` followed by a left assignment at `j`, since both would use
`F_j`.  Thus the assignment word contains no `RL`, and is exactly

\[
                           L^pR^{h-p},\qquad 0\le p\le h.          \tag{9.2}
\]

It uses every socket facet except the unique pivot `F_p`.  Conversely each
word in (9.2) is injective.  Hence the compact socket has exactly `h+1`
local pivot phases.  This is the precise local interface to a four-row SCD
phase; extension to one pre-existing common owner basis is an additional
Hall condition.

## 10. Reconciliation with the asymptotic two-stratum bank

In the Catalan notation

\[
 W={2m-1\choose m-1},\qquad C=\operatorname{Cat}_m
   ={2W\over m+1},                                    \tag{10.1}
\]

and the phase-compatible paired-Kneser bank uses central supply

\[
 N={2m-3\choose m-2},\qquad
 {C\over N}={4(2m-1)\over m(m+1)}=O(m^{-1}).          \tag{10.2}
\]

If at most `C` compact sockets of width `h=o(m)` are reserved, their crude
total resource loads are

\[
\begin{array}{c|c}
\text{selected owner facets}&(h+1)C
   ={2(h+1)W\over m+1},\\[1mm]
\text{deleted seams}&\le2(h+1)C
   ={4(h+1)W\over m+1},\\[1mm]
\text{internal lower seams}&hC
   ={2hW\over m+1},\\[1mm]
\text{non-socket connectors}&\le(h+2)C
   ={2(h+2)W\over m+1}.
\end{array}                                             \tag{10.3}
\]

All are `o(W)`.  They also reserve only `O(hC)=o(N)` resources in each
central rank.  Dividing the forbidden-resource losses by the raw paired
block count in the two-stratum greedy proof gives `O(hC/N)=O(h/m)=o(1)`.
Therefore the even paired-block bulk remains resource-abundant after such
a socket reserve.

For odd `C`, the existing proof first plants a directed odd Kneser cycle.
An arbitrary `o(N)` forbidden reserve need not be avoided by that particular
cycle: its `Theta(m)` vertices can have nonzero intersection with a reserve
of density `o(1)`.  Full odd-bank coexistence therefore requires either
planting the odd seed before the sockets and avoiding it prospectively, or
a new odd-seed avoidance lemma.  The scale estimate alone does not supply
that row.

This is only a compatibility-of-scales statement.  It does not prove that
the socket targets are the two-stratum endpoint holes, that the two
staircase guards occur in the selected chronology, or that the planted
`3C` phase rows and the socket pivot rows extend to one common owner basis.
Moreover, one socket contributes `h` occurrences of one upper colour,
whereas one two-stratum packet contributes one target resource; the
`(h-1)e_U` surplus in Section 6 must not be erased in a compiler-cap
calculation.

## 11. Proof-safe conclusion

The facet path is a valid resident socket only relative to a complete
boundary state.  The strongest unconditional statements are:

* the internal owner, upper, and lower calculations in the source;
* the corrected boundary criterion (2.2), and the compact Hall test (3.6);
* the exact extraction count (5.2);
* the signed deck identities (6.1)--(6.2);
* the child bound `|Gamma^+|<=q` and the fixed-basis protected criterion
  (7.3);
* the `h+1` pivot phases (9.2);
* `o(W)` resource compatibility with the asymptotic two-stratum bank when
  `h=o(m)`.

An all-`k` positive cascade still needs one of two genuinely new inputs:

1. a protected zero-branching extractor satisfying (3.6), (5.4), (6.2),
   and (7.3); or
2. a weighted/absorbing selector satisfying (8.1), together with a
   terminal family that closes the declared upper and lower debts.

The unweighted `2h` or `2h+2` cut bound alone is supercritical and does not
imply either input.
