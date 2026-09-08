# `k=17` R2 variable residence cuts: exact segment columns, endpoint Hall recourse, and guarded deck separation

**Date:** 2026-08-01  
**Lane:** R2 / protected `ML_9` host / one-oriented reversal quotient  
**Status:** proof-safe exact master formulation and authenticated rejection of
one fixed minimum-cut incumbent.  No feasible variable-cut chronology and no
all-minimum-cut no-go is claimed.

## 0. Outcome and scope

The protected `k=17` factor is now a closed physical owner/lower-`q1`/
upper-`q1` host: it contains all `24,310` rank-nine owners, all `24,310`
rank-eight lower colours, all `19,448` rank-ten upper colours, and the
literal `29`-owner packet-plus-twin-bank object.  Its seven owner components
have sizes

\[
             14305,\ 8615,\ 1362,\ 18,\ 4,\ 3,\ 3.          \tag{0.1}
\]

The factor itself is not resident.  Its `3,073` positive runs of length two
and `2,710` positive runs of length three define `5,783` circular gap
intervals.  The exact protected-gap-avoiding transversal number is

\[
                              \tau=3807.                     \tag{0.2}
\]

The previously chosen fixed minimum transversal is impossible to reconnect
atomically even under a necessary residence relaxation: `1,289` of its
deleted lower colours have no admissible endpoint atom.  The new literal
audit below also finds `1,456` lost rank-ten targets with no such endpoint
provider.  Those facts reject that **one** cut pattern.  They do not reject
another minimum or near-minimum transversal.  Raw Boolean supply is not the
issue: before residence filtering the same fixed pattern has `56,790` atoms
and perfect two-shore projections.  The obstruction is the correlated
placement of endpoint ages, cut colours, and segment boundaries.

The correct next master therefore selects the cuts themselves.  This note
gives an exact finite, although exponentially priced, formulation for:

1. minimum or near-minimum protected residence cuts;
2. the induced consecutive owner segments and their orientations;
3. one incoming and outgoing seam per selected segment;
4. exact recycling of deleted lower colours by conditional Hall flow;
5. connected topology, depth-three residence, and rank-ten survival; and
6. occurrence-labelled witnesses for ranks eleven through seventeen.

The residual terminal compiler and the ae88 quotient attachment master are
linked only after their literal option-labelled crosswalks exist.  They are
not consequences of this physical formulation.

## 1. Variable protected residence-cut face

Let

\[
 G=\mathbin{\dot\bigcup}_{r=1}^7G_r,
 \qquad |G|=24310,                                         \tag{1.1}
\]

be the old owner gaps of the seven cycles.  Gap `g` joins distinct rank-nine
owners `L_g,R_g` and carries the unique labels

\[
 c_g=L_g\cap R_g\in {[17]\choose8},\qquad
 u_g=L_g\cup R_g\in {[17]\choose10}.                       \tag{1.2}
\]

Every rank-eight colour labels exactly one old gap.  Let
`G_prot` be the `26` gaps whose two incidence edges are protected, and let
`H` be the authenticated family of `5,783` short-run collar intervals.

Use a binary variable `d_g`, equal to one when gap `g` is cut.  For a
near-minimum allowance `rho_bar`, impose

\[
\begin{aligned}
 d_g&=0 &&(g\in G_{\rm prot}),                              \tag{1.3}\\
 \sum_{g\in H}d_g&\ge1 &&(H\in\mathcal H),                 \tag{1.4}\\
 \sum_{g\in G_r}d_g&\ge1 &&(1\le r\le7),                  \tag{1.5}\\
 \sum_{g\in G}d_g&=3807+\rho,
 &0\le\rho\le\bar\rho,\quad \rho\in\mathbb Z.          \tag{1.6}
\end{aligned}
\]

The exact minimum face is `rho=0`.  Rows (1.3)--(1.4) imply that every
consecutive owner segment left after cutting is internally positive-run
resident at depth three.  They say nothing about runs crossing new seams.

The value (0.2) is supplied by the exact conditioned circular-interval
optimizer.  No total-unimodularity claim is made for the displayed
circular-arc covering matrix.

## 2. Exact consecutive-segment linkage

For gaps `g,h` on the same old cycle, let `n_gh` mean that `h` is the next
selected cut clockwise after `g`.  Write `(g,h)` for the open cyclic gap
interval between them.  The exact linkage is

\[
\begin{aligned}
 \sum_{h\in G_r}n_{gh}&=d_g,                               \tag{2.1}\\
 \sum_{g\in G_r}n_{gh}&=d_h,                               \tag{2.2}\\
 n_{gh}&\le d_g,\quad n_{gh}\le d_h,                       \tag{2.3}\\
 n_{gh}&\le1-d_v &&(v\in(g,h)).                             \tag{2.4}
\end{aligned}
\]

For `g=h`, the interval `(g,g)` means every other gap of that cycle, so this
column is available only when `g` is its sole selected cut.  Equations
(2.1)--(2.4) select exactly the consecutive-cut decomposition.

Choose one orientation of every active segment:

\[
             s_{gh,+}+s_{gh,-}=n_{gh}.                     \tag{2.5}
\]

An oriented segment column

\[
                        \alpha=(g,h,\varepsilon)             \tag{2.6}
\]

contains its literal owner word, entrance owner `H_alpha`, exit owner
`T_alpha`, protected/rooted option labels, capped residence transition, and
occurrence-labelled interval-union summary.  The theorem-level universe has

\[
             \sum_{r=1}^7|G_r|^2=280{,}706{,}652            \tag{2.7}
\]

unoriented next-cut columns and twice that many oriented columns.  It is a
pricing universe, not a matrix that should be materialized eagerly.

### Lemma 2.1 (segment linkage is exact)

For any integral `d`, equations (2.1)--(2.4) select the unique clockwise
successor of each selected cut.  Conversely, the consecutive segments of
any selected cut set satisfy those equations.

#### Proof

If `n_gh=1`, (2.3) selects both endpoints and (2.4) forbids any selected
gap strictly between them.  Row (2.1) gives every selected left endpoint
one successor; row (2.2) gives every selected right endpoint one
predecessor.  Hence it must be the next selected cut.  The converse is
immediate.  \(\square\)

## 3. Guarded endpoint atoms and lower-colour recycling

For active oriented segments `alpha,beta`, let `p_alpha,beta` select the
successor seam from `alpha` to `beta`.  Use

\[
\begin{aligned}
 p_{\alpha\beta}&\le s_\alpha,\quad
 p_{\alpha\beta}\le s_\beta,                               \tag{3.1}\\
 \sum_\beta p_{\alpha\beta}&=s_\alpha,\qquad
 \sum_\gamma p_{\gamma\alpha}=s_\alpha.                    \tag{3.2}
\end{aligned}
\]

These are the requested one-out/one-in equations.  Alone they give a cycle
cover, not a single component.

A literal atom `a=(alpha,beta,g)` exists precisely when

\[
 T_\alpha\cap H_\beta=c_g,\qquad T_\alpha\ne H_\beta,       \tag{3.3}
\]

and both Johnson containments and every selected protected, orientation,
root-owner, and fixed-predecessor option are legal.  Because both endpoints
have rank nine, (3.3) also gives

\[
                       T_\alpha\cup H_\beta\in {[17]\choose10}.
                                                                    \tag{3.4}
\]

With binary atom variables `z_alpha,beta,g`, impose

\[
\begin{aligned}
 \sum_gz_{\alpha\beta g}&=p_{\alpha\beta},                 \tag{3.5}\\
 z_{\alpha\beta g}&\le d_g,                                \tag{3.6}\\
 \sum_{\alpha,\beta}z_{\alpha\beta g}&=d_g.               \tag{3.7}
\end{aligned}
\]

Thus a cyclic reassembly uses every deleted lower colour exactly once.
Together with the unchanged internal gaps, the complete lower palette is
restored exactly once.

### Linear terminal variant

A Hamilton path on `D=sum d_g` segments has only `D-1` new seams.  It cannot
also use all `D` deleted colours as ordinary seams.  Introduce an omitted
colour `o_g` and source/sink segment indicators, replace (3.7) by

\[
 \sum_{\alpha,\beta}z_{\alpha\beta g}+o_g=d_g,
 \qquad \sum_go_g=1,                                      \tag{3.8}
\]

and reduce exactly one incoming and one outgoing degree.  The omitted
colour must be consumed by an explicit boundary/compiler pin; merely
dropping it is not an exact lower-palette construction.  Equivalently, add
one dummy boundary segment and solve the cyclic equations.

## 4. Exact conditional Hall/Benders separator

The explicit `z` layer is a three-resource binary matching and is not a TU
formulation.  It has an exact bipartite recourse after the ordered successor
pairs `p` have been selected.

For a set `X` of option-labelled ordered segment pairs, define its
**complete** colour neighbourhood

\[
 N_{\mathcal A}(X)=
 \{g:\text{some }(\alpha,\beta)\in X
                 \text{ has the literal atom }(\alpha,\beta,g)\}.  \tag{4.1}
\]

Then colour recourse exists if and only if

\[
 \boxed{
 \sum_{(\alpha,\beta)\in X}p_{\alpha\beta}
 \le \sum_{g\in N_{\mathcal A}(X)}d_g
 \qquad(X\subseteq\mathcal S\times\mathcal S).}           \tag{4.2}
\]

### Theorem 4.1 (Hall projection and min-cut separation)

On the cyclic face `sum p=sum d`, equations (4.2) are necessary and
sufficient for variables `z` satisfying (3.5)--(3.7).

#### Proof

Build the network

```text
source -> selected ordered pair (alpha,beta)   capacity p_alpha,beta
pair -> deleted gap-colour g                   capacity INF for a literal atom
gap-colour g -> sink                           capacity d_g.
```

Take `INF>sum d`.  A finite source cut is determined by a pair set `X` and
must retain every neighbour `N_A(X)` on the source side.  Its capacity is
`sum p-p(X)+d(N_A(X))`.  It is deficient exactly when (4.2) is violated.
Max-flow integrality supplies integral `z` when all rows hold.  \(\square\)

The same separator handles (3.8) after adding the dummy/boundary colour.
It is proof-safe only when `N_A` is computed in the complete option-labelled
universe.  A zero degree or deficient shore in a truncated incumbent atlas
is only an incumbent-guarded rejection.

In particular, if a complete universe proves that a lower colour set `Z`
has no endpoint providers, then

\[
 \sum_{g\in Z}d_g=0                                      \tag{4.3}
\]

on the cyclic face, or

\[
 \sum_{g\in Z}d_g\le\sum_{g\in Z}o_g\le1                 \tag{4.4}
\]

on the one-hole path face.  The `1,289` zero colours of the fixed atlas do
**not** justify (4.3) or (4.4) for other cut patterns.

## 5. Topology and exact boundary residence

For one final cycle, add activated directed subtour rows.  A globally valid
node-selection form is

\[
 \sum_{\alpha\in S,\,\beta\notin S}p_{\alpha\beta}
 \ge s_\mu+s_\nu-1                                      \tag{5.1}
\]

for every option-column set `S`, `mu in S`, and `nu notin S`.  These rows
are separated by SCC or directed min-cut on an integral incumbent.  A
Hamilton path is handled by a dummy boundary node or the usual source/sink
flow rows.

For residence, let

\[
 Q=\{0,1,2,3,4\}^{17},                                   \tag{5.2}
\]

where coordinate state zero means that the latest owner omits the
coordinate and state four means a positive run safely saturated at length
at least four.  Reading a zero from state one, two, or three is forbidden.
Every literal oriented segment has a deterministic transition

\[
              \delta_\alpha:Q\longrightarrow Q\cup\{\mathrm{BAD}\}.
                                                                    \tag{5.3}
\]

Use entry-state variables `w_alpha,q` and state-carry variables
`y_alpha,beta,q`:

\[
\begin{aligned}
 \sum_qw_{\alpha q}&=s_\alpha,                              \tag{5.4}\\
 p_{\alpha\beta}&=\sum_qy_{\alpha\beta q},                 \tag{5.5}\\
 \sum_\beta y_{\alpha\beta q}&=w_{\alpha q},              \tag{5.6}\\
 w_{\beta r}&=
 \sum_{\substack{\alpha,q:\,\delta_\alpha(q)=r}}
 y_{\alpha\beta q},                                      \tag{5.7}
\end{aligned}
\]

with BAD transitions omitted.  These equations are exact for positive-run
residence on every selected directed cycle.  They are theorem-sized
(`|Q|=5^17`) and should be implemented by deterministic replay.  When a
literal selected chain `J` first closes an outside-independent positive run
at length below four, the replay returns the valid clause

\[
                    \sum_{a\in J}p_a\le |J|-1.             \tag{5.8}
\]

A pairwise robust-seam failure is not automatically a valid clause: a
short all-one segment may carry the run to another segment and repair it.
If the eventual induction interface requires signed rather than only
positive residence, apply the same replay to complemented owner bits.

Protected packet/collar age conditions are literal transition guards.  On
a frozen predecessor face they may force a protected segment orientation.
If the root-owner matching is co-designed, the segment must instead carry
the corresponding option/state pin; no orientation may be hard-wired from
the old alternating physical matching.

## 6. Rank-ten and all deeper interval tickets

Let `m_10^0(R)` be the old multiplicity of rank-ten adjacent-union colour
`R`.  Cutting `g` deletes one occurrence `u_g`; adding a seam
`alpha -> beta` adds `T_alpha union H_beta`.  Therefore the exact final
upper-`q1` row is

\[
 \boxed{
 m_{10}^0(R)-\sum_{g:u_g=R}d_g
 +\sum_{\alpha,\beta:T_\alpha\cup H_\beta=R}p_{\alpha\beta}
 \ge1
 }
 \qquad\left(R\in{[17]\choose10}\right).                 \tag{6.1}
\]

This is a global row; it counts every removed and added adjacency exactly.

For ranks eleven through seventeen, a sum of seam-local deltas is not
exact because an interval may cross several seams.  Use occurrence labels.
For every old occurrence `omega`, let `F(omega)` be its old-gap footprint
and impose

\[
 v_\omega\le1-d_g\ (g\in F(\omega)),\qquad
 v_\omega\ge1-\sum_{g\in F(\omega)}d_g.                   \tag{6.2}
\]

For every new consecutive witness chain `w`, let `A(w)` be its complete
segment/seam footprint.  Its activation variable satisfies

\[
 v_w\le s_\alpha\quad(\alpha\in A(w)),\qquad
 v_w\le p_{\alpha\beta}\quad((\alpha,\beta)\in A(w)).     \tag{6.3}
\]

For every required target `R`, impose

\[
 \sum_{\omega:\operatorname{val}(\omega)=R}v_\omega
 +\sum_{w:\operatorname{val}(w)=R}v_w\ge1,
 \qquad 11\le |R|\le17.                                  \tag{6.4}
\]

The witness-chain universe must be complete.  Equivalently, compose the
exact occurrence-labelled block summaries

\[
                         U=(I,P,S,t)                         \tag{6.5}
\]

by the associative accumulated-union product of
`MATH_THEOREM_AD_K17_ACCUMULATED_UNION_BLOCK_AUTOMATON_AND_Q1_SCOPE_20260801.md`
(input SHA-256 `dccc67c8...`).  A missing target discovered by replay without
a complete provider universe yields an incumbent/segmentation no-good, not
a global target cut.  All ranks through seventeen must be replayed.

## 7. Terminal compiler and ae88 attachment are separate recourse

Once a resident chronology and its literal interval occurrences exist, a
terminal compiler allocation is a bipartite `b`-flow on the newly built
option-labelled admissibility graph `Adm_A`.  Its exact Hall family is

\[
 d_{\rm cmp}(X)\le
 \sum_{c\in N_{\operatorname{Adm}_A}(X)}\operatorname{cap}(c).  \tag{7.1}
\]

It is separated by the standard target--cell min-cut.  Before chronology,
only an explicitly encoded omitted-lower boundary pin from (3.8) is valid.
An incumbent compiler atlas cannot supply global cuts after cut placement,
orientation, or boundary caps change.  The reset-return packet's internal
compiler transport remains proved; the **residual host terminal compiler**
is the object still meant here.

### Lemma 7.1 (no automatic ae88 quotient descent)

The physical seven-factor is not invariant under the cyclic coordinate
action `C_17`.

#### Proof

An action of a prime-order group on seven components has component orbits of
size one or seventeen, hence fixes every component.  The coordinate rotation
acts freely on rank-nine masks: an invariant proper nonempty subset of a
transitive seventeen-cycle does not exist.  Every invariant component size
would therefore be divisible by seventeen.  None of the seven sizes in
(0.1) is divisible by seventeen.  \(\square\)

Consequently the physical segment variables cannot be identified with the
ae88 quotient state variables.  A literal physical-to-option/state/phase
crosswalk is required.  After such a crosswalk is frozen, retain the exact
ae88 maximum-closure family, writing its fixed term as `M_ae88` to avoid a
collision with packet notation:

\[
 \boxed{
 M_{\rm ae88}+x(X)-x(\Gamma^+(X))\le1430
 \qquad(X\subseteq\Omega_{\rm st}).}                       \tag{7.2}
\]

Its two-layer maximum-closure separator is unchanged.  Likewise a final
functional root-owner matching `theta` must be selected on the rebuilt
option-labelled attachment graph; the alternating predecessor matching of
the physical factor is not the authenticated ae88 `1,141`-edge incumbent.

Global reversal permits one complete oriented child and a reflected
certificate when the induction interface is reversal-closed.  It removes
a same-address cross-phase compiler intersection.  It does not supply the
missing physical/ae88 crosswalk or solve a named one-sided socket.

## 8. Fixed-incumbent H100 calibration

The materialized fixed-incumbent audit uses the sorted-mask cycle order and
the deterministic anchor/rightmost-greedy convention of the contracted C++
endpoint audit.  This convention need not emit the lexicographically first
minimum transversal.  Its factor is

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
```

The H100 `g++ -O3` run gives:

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
\text{cuts / resident paths}&3807\\
\text{oriented endpoint atoms}&56790\\
\text{atoms with a definite short-run hazard}&43616\\
\text{atoms surviving the necessary relaxation}&13174\\
\text{pairwise-robust atoms}&9618\\
\text{zero lower colours, necessary relaxation}&1289\\
\text{zero lower colours, pairwise robust}&1686
\end{array}                                                 \tag{8.1}
\]

The targets absent from every internal path interval, by ranks ten through
seventeen, are

\[
             2423,\ 3116,\ 1297,\ 249,\ 12,\ 0,\ 0,\ 0.   \tag{8.2}
\]

Among the `2,423` lost rank-ten targets, `1,456` have no endpoint provider
even in the necessary relaxation (`1,662` under the pairwise-robust filter).
Thus this fixed cut pattern fails independently on both the lower-colour
and rank-ten rows.

The materialized five-column certificate has SHA-256 `3effd7d1...`.  This
is not identified with the separately frozen Python-order certificate
`cde33b3f...`; different cycle-start and tie conventions are possible.
All endpoint counts in (8.1)--(8.2) are bound only to the materialized
`3effd7d1...` incumbent and the exact hashes in the audit manifest.

## 9. Proof-safe Benders discipline

The following rows are globally valid when their complete option-labelled
universes are used:

* the collar hitting, protected-gap, budget, and next-cut rows;
* endpoint activation, degree, full-neighbourhood Hall rows (4.2), and
  topology cuts;
* the exact rank-ten balance (6.1);
* residence conflicts whose literal chain closes a short run independently
  of its exterior; and
* deeper-ticket rows built from a complete occurrence/witness universe.

The following conclusions are only incumbent-guarded:

* zero colours or Hall shores in a truncated atom atlas;
* a residence failure that disappears after inserting another cut into an
  incumbent segment;
* a replayed missing deep target before all alternative witness chains have
  been priced;
* failure of one orientation/successor order; and
* failure of the materialized `3,807`-cut pattern.

If the **complete** orientation, atom, residence, and deck subproblem is
infeasible for a fixed cut vector `d*`, the proof-safe pattern no-good is

\[
 \sum_{g:d_g^*=1}(1-d_g)+\sum_{g:d_g^*=0}d_g\ge1.          \tag{9.1}
\]

Failure of only one successor order excludes that order, not the whole cut
pattern.

### Theorem 9.1 (exactness of the variable-cut core)

With complete segment, atom, residence-state, and occurrence-witness
universes, integral solutions of (1.3)--(6.4), plus (5.1), are in bijection
with protected-gap-preserving cut-and-rewire cycles that retain every owner,
restore every lower and adjacent rank-ten colour, are positive-run resident
at depth three, and contain every required rank-eleven-through-seventeen
interval target.  The path variant is exact after adding its one explicit
boundary colour pin.

#### Proof

Given a chronology, mark its removed old gaps, its consecutive segments,
their orientations, new seams, seam colours, automaton states, and literal
target occurrences.  These data satisfy every row.  Conversely, Lemma 2.1
partitions all old owners exactly once; (3.2) and (5.1) order the active
segments into one cycle; Theorem 4.1 assigns every deleted lower colour;
(5.4)--(5.7) certify residence; (6.1) restores the adjacent rank-ten row;
and (6.2)--(6.4) provide literal witnesses for every deeper target.  No
unencoded topology, compiler, or ae88 conclusion is used.  \(\square\)

## 10. Exact open gates

This theorem closes the formulation, not the existential solve.  Still open
in this lane are:

1. pricing and solving an alternative `rho=0` or controlled `rho>0` cut
   pattern jointly with endpoint Hall, topology, and residence;
2. literal all-rank deck replay and the residual terminal compiler;
3. the physical-to-ae88 option/state/phase crosswalk and then the independent
   ae88 maximum-closure/functional-matching test; and
4. regeneration after the one-oriented child is reflected.

No upper-row, compiler, topology, or ae88 gain is claimed beyond the rows
explicitly encoded above.
