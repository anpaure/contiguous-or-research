# The one-cell two-fan seam has an exact one-credit Hall normal form

Date: 2026-08-01  
Lane: AD, twisted-cube U5 transport  
Status: exact conditional matching/common-cap interface, plus an exact
obstruction to its canonical coatom/twisted-cube instantiation.  The theorem
below proves the one-credit implication only once the crossing, native, fan,
and exposed-ear incidences coexist in one literal terminal cap state.  The
canonical adjacent OLD-fan/NEW-crossing assignment has no such state.

## 0. Result

Insert one source position at an internal cut of a depth-`d` source line,
where `d>=2`.  The insertion destroys exactly `d-1` crossing length-`d`
cells and creates the two fans

\[
 {\cal F}=\{L_1,\ldots,L_d,R_1,\ldots,R_d\},\qquad L_1=R_1,
 \qquad |{\cal F}|=2d-1.                                   \tag{0.1}
\]

Choose the destroyed pins to carry a bank `N` of `d-1` new-phase chain
targets.  Suppose post-switch native packet cells carry all of `N`.  Let
`O` be the two old endpoint chains, so

\[
                         |O|=2(d-1).                         \tag{0.2}
\]

This choice of `N` is a hypothesis, not a consequence of the two-fan count.
Sections 5A--6 prove that it is false for one canonical packet and for every
pair of distinct chain families in the four-packet twisted cube.

The two endpoint transporters reduce the remaining question to matching
`O` into `F`.  They certify an injection and hence leave one fan address
unused.  Let `h` be one exposed compiler target, and let its admissible
open-ear sinks be the fan addresses reachable from `h` in the **same**
nonzero common-cap state.

The exact conclusion is:

> The seam supplies one matching credit, `alpha=ell+1`, if and only if an
> `O`-saturating fan matching can leave an admissible sink for `h` unused.

Equivalently, if `G` is the terminal target--fan incidence graph, then

\[
             \nu\bigl(G[O\cup\{h\},{\cal F}]\bigr)=2d-1.     \tag{0.3}
\]

When (0.3) fails but `O` itself is saturable, the residual deficiency is
exactly one.  Its sharp Hall certificate is a tight old-chain set
`X subseteq O` satisfying

\[
             |N_G(X)|=|X|,\qquad N_G(h)\subseteq N_G(X).      \tag{0.4}
\]

Then `X union {h}` has `|X|+1` targets and only `|X|` fan cells.  Thus the
failure is not a diffuse cap loss: after the chain transport is fixed it is
one explicit unit Hall cut.

## 1. Exact accounting

The interval identity is independent of the coatom packet.  An old
length-`j` interval crosses the new source position in `j-1` ways.  Its
transported convex hull has length `j+1`; therefore precisely the `d-1`
crossing intervals of old length `d` leave the depth-`d` band.  Every new
short interval outside the transport image has the inserted position as
one endpoint, and these intervals are exactly (0.1).  Hence

\[
                         (2d-1)-(d-1)=d.                      \tag{1.1}
\]

For the proposed chain closure, the relevant target and cell counts are

\[
\begin{array}{c|c|c}
\text{bank}&\text{targets}&\text{terminal cells}\\ \hline
\text{destroyed new-chain pins}&d-1&d-1\text{ native cells}\\
\text{two old endpoint chains}&2(d-1)&2d-1\text{ fan cells}.
\end{array}                                                   \tag{1.2}
\]

Thus the native bank is square and the fan bank has excess one.  If every
affected old matching edge is exposed in this local normal form, the lost
bank has size

\[
                  \ell_{\rm loc}=(d-1)+2(d-1)=3(d-1),         \tag{1.3}
\]

whereas the terminal native-plus-fan bank has `3d-2=ell_loc+1` cells.  If
some basis-preserving chain returns have already been contracted, (1.3)
decreases by the same number on both sides.  The excess remains exactly
one.  This is the cardinality reason that the seam can give at most one
new credit.

Cardinality is not sufficient: the excess cell must be exposable by an
`O`-matching and reachable from `h` inside one cap state.

## 2. Fixed-state fan theorem

Fix one complete terminal cap state `theta`.  This means that all incidences
used below are simultaneously co-selectable and that the resulting source
word is nonzero.  It is not enough that every incidence occurs in some cap
state.  Let

\[
 G_\theta=(O\mathbin{\dot\cup}\{h\},{\cal F};E_\theta)        \tag{2.1}
\]

be its exact incidence graph after the forced native assignment of `N` is
removed.  Assume `G_theta[O,F]` has a matching saturating `O`; the literal
two-sided endpoint carving is one sufficient certificate of this
assumption.

Define the exposable fan set

\[
 \operatorname{Sp}_\theta
  =\{f\in{\cal F}:\nu(G_\theta[O,{\cal F}-\{f\}])=|O|\},      \tag{2.2}
\]

and the legal ear-sink set

\[
                        S_\theta=N_{G_\theta}(h).             \tag{2.3}
\]

### Theorem 2.1 (one-credit equivalence)

Under the preceding hypotheses, the following are equivalent.

1. The seam and chain transport have local augmenting number
   `alpha_loc=ell_loc+1`.
2. `G_theta` has a perfect matching.
3. `S_theta intersect Sp_theta` is nonempty.

If they fail, then `nu(G_theta)=|O|`; the local augmenting number is
`alpha_loc=ell_loc`, and the residual target deficiency is exactly one.

#### Proof

The native cells first saturate the `d-1` targets of `N`.  All other
affected terminal assignments are therefore precisely a matching in
(2.1).  Since

\[
                   |O|+1=2d-1=|{\cal F}|,                   \tag{2.4}
\]

saturating `O union {h}` is equivalent to a perfect matching in `G_theta`.
Together with the retained exterior matching, this restores every lost
edge and adds the formerly unmatched target `h`, giving
`alpha_loc=ell_loc+1`.  Conversely, any local extra augmentation must end
at the sole excess fan address, so such an augmentation induces a perfect
matching of (2.1).

In a perfect matching let `f` be the cell matched to `h`.  Removing that
edge leaves an `O`-saturating matching avoiding `f`, so
`f in S_theta intersect Sp_theta`.  Conversely, for such an `f`, combine
an `O`-saturating matching in `F-{f}` with the edge `hf`.

If there is no perfect matching, the assumed `O`-saturating matching still
has size `|O|`.  Hence the full graph has matching number exactly `|O|`, one
below (2.4).  This restores but cannot improve the old matching, proving
the last assertion.  \(\square\)

The equality `alpha_loc=ell_loc` in the failure case is a statement about
the displayed closed local fibre: it assumes no additional exterior sink.
In a larger compiler an unrelated exterior ear may of course add another
augmentation.  The theorem isolates exactly what the one-cell fan itself
contributes.

## 3. The minimal residual Hall cut

### Theorem 3.1 (tight-set characterization)

With `O` saturable, `G_theta` has no perfect matching if and only if there
is a set `X subseteq O` such that

\[
                    |N_\theta(X)|=|X|,
       \qquad S_\theta\subseteq N_\theta(X).                  \tag{3.1}
\]

For every such `X`, the target set `X union {h}` has Hall deficiency one.
An inclusion-minimal `X` in (3.1) is a smallest residual certificate.

#### Proof

If (3.1) holds, then

\[
 N_\theta(X\cup\{h\})=N_\theta(X),
 \qquad |N_\theta(X\cup\{h\})|=|X|<|X|+1,                  \tag{3.2}
\]

so Hall fails.

Conversely, let `Y subseteq O union {h}` violate Hall.  Since `O` is
saturable, no subset of `O` violates Hall; hence `h in Y`.  Put
`X=Y-{h}`.  Saturability gives `|N_theta(X)|>=|X|`, while

\[
 |N_\theta(X)\cup S_\theta|=|N_\theta(Y)|<|X|+1.             \tag{3.3}
\]

All quantities are integral, so (3.3) forces equality
`|N_theta(X)|=|X|` and containment `S_theta subseteq N_theta(X)`.
The deficiency is necessarily one.  \(\square\)

There is also a canonical, matching-relative certificate.  Choose an
`O`-saturating matching `M`, leaving one fan cell unmatched, and start an
alternating search at `h`.  If no augmenting path reaches an unmatched fan
cell, let `Y` be the reachable target vertices and `Z` the reachable fan
vertices.  Then

\[
                         N_\theta(Y)=Z,
             \qquad |Y|=|Z|+1.                               \tag{3.4}
\]

Thus `Y` is the canonical alternating-reachability cut.  Deleting redundant
branches yields an inclusion-minimal set from Theorem 3.1.

## 3A. The star-hidden fan-only carve

There is one important case in which the final edge is automatic rather
than another Hall hypothesis.  It uses the shared singleton of the two
fans, not an arbitrary exposed fan interval.

### Lemma 3A.1 (exact star-hidden gluing criterion)

Let

\[
 O_L=\{P_1,\ldots,P_{d-1}\},\qquad
 O_R=\{S_1,\ldots,S_{d-1}\}                              \tag{3A.1}
\]

be the two target chains.  Suppose the left and right endpoint
transporters have outward source fragments whose first-\(j\) unions are
respectively \(P_j\) and \(S_j\).  Insert between them one source letter
\(Z\).  Then the shifted two-sided fan assignment

\[
       P_j\longmapsto L_{j+1},\qquad
       S_j\longmapsto R_{j+1},\qquad 1\le j\le d-1,       \tag{3A.2}
\]

is literal if and only if

\[
                  Z\subseteq
                  \bigcap_{j=1}^{d-1}(P_j\cap S_j).       \tag{3A.3}
\]

It uses exactly \({\cal F}-\{L_1\}\) and leaves the shared singleton
\(L_1=R_1=\{*\}\) unused.  That singleton is a literal cell for an exposed
target \(h\) if and only if

\[
                              Z=h.                       \tag{3A.4}
\]

Consequently the star-hidden code

\[
 h\ne\varnothing,\qquad h\notin O,\qquad
 h\subseteq\bigcap_j(P_j\cap S_j),\qquad A_*=h          \tag{3A.5}
\]

simultaneously gives the old-chain fan matching and the open-ear edge to
the unique spare star cell in one literal word.  If the unchanged and
transporter source letters are nonempty, that word is nonzero.

#### Proof

The interval \(L_{j+1}\) consists of the inserted source and the first
\(j\) left-transporter sources, read outward from the cut.  Its literal OR
is

\[
                             Z\cup P_j.                  \tag{3A.6}
\]

Likewise \(\operatorname{OR}(R_{j+1})=Z\cup S_j\).  These values equal the
prescribed targets for every \(j\) exactly when (3A.3) holds.  The cells in
(3A.2) are

\[
                 L_2,\ldots,L_d,R_2,\ldots,R_d,          \tag{3A.7}
\]

which are pairwise distinct and comprise all fan cells except the common
singleton.  The OR of that singleton is the inserted source letter \(Z\)
itself, proving (3A.4).  Under (3A.5) every displayed cell is realized
inside the same literal word and the inserted letter is nonempty.  Thus no
union-of-cap-states inference is being made and the new source position
passes nonzeroness directly; all other positions retain their assumed
nonzero sources.  \(\square\)

The equality in (3A.4) is load-bearing.  Mere containment \(Z\subset h\)
does not realize \(h\) as a singleton OR, and choosing some longer fan cell
as the spare reintroduces the common-cap/Hall test of Theorem 2.1.
Likewise, if \(Z\) is not contained in one chain target, that target is
contaminated by the inserted source even though the unshifted endpoint
transporter remains valid.

The lemma proves the displayed fan incidences and nonzeroness.  It does not
prove that the same source letters realize prescribed values on the
destroyed crossing cells.  That additional compatibility is exactly
Theorem 2.1 of
`MATH_THEOREM_ONE_CELL_STAR_HIDDEN_FAN_TRACE_20260801.md`.  Exact replay of
the depth-\(d\) carrier row and preservation of U1--U4 are also separate
geometric hypotheses on the surrounding stutter/packet construction; none
can be deduced from (3A.3).

## 4. The deterministic carved face

Suppose the certified endpoint transporters provide a literal bijection

\[
                  \phi:O\longrightarrow{\cal F}-\{f_*\}.    \tag{4.1}
\]

and, on the certified face, these are the only old-chain/fan incidences.
Then

\[
                         \operatorname{Sp}_\theta=\{f_*\}.   \tag{4.2}
\]

Consequently the one-credit test is the single edge

\[
                              h f_*\in E_\theta.              \tag{4.3}
\]

If (4.3) fails and `S_theta` is the set of other fan cells available to
`h`, put

\[
                       X=\phi^{-1}(S_\theta).                 \tag{4.4}
\]

Then

\[
 |X\cup\{h\}|=|S_\theta|+1,
 \qquad N_\theta(X\cup\{h\})=S_\theta,                      \tag{4.5}
\]

which is the unique inclusion-minimal cut containing every legal `h`-edge.
If `S_theta` is empty, it reduces to the singleton zero-neighbour cut
`{h}`.

This is the sharp meaning of “the one common-`q1` spare is the open ear.”
The chain transport itself proves that `f_*` is an unused matching address.
The basis-changing step is exactly (4.3), including its trace and cap
guards.

## 5. Common-`Q` and nonzero scope

Let `Theta_nz` be the set of complete terminal cap states which satisfy all
positive rows and have a nonempty source letter at every position.  The
exact nonlinear statement is

\[
 \boxed{
  \alpha_{\rm loc}=\ell_{\rm loc}+1
  \iff
  \exists\theta\in\Theta_{nz}:\quad
       S_\theta\cap\operatorname{Sp}_\theta\ne\varnothing.}  \tag{5.1}
\]

One may not replace the right side by the union graph
`union_theta G_theta`: the `O`-matching and the edge to the spare must
coexist in one state.

If the endpoint letters and fan pins are exhibited as one literal nonzero
antecedent word, their common-`Q` compatibility and nonzeroness are proved
directly.  Only the edge to `f_*` remains to be checked.  If adding that pin
is impossible, the exact common-`Q` theorem produces either

1. a positive interval whose legal coordinate positions are covered by at
   most `d+1` negative pins, or
2. one source position whose complete maximal envelope is deleted, with a
   certificate using at most `r` negative pins.

Thus a negative result has two sharply separated forms: the unit matching
cut (3.1) inside every legal state, or a bounded mixed-cover/nonzero core
showing that the proposed spare edge belongs to no legal state.

## 5A. The canonical OLD-fan/NEW-crossing assignment is trace-infeasible

Use one canonical packet with ordered active pair \((a,b)\), third role
\(c\), common fixed set

\[
                         Z=K\cup\{\infty,c\},                  \tag{5A.1}
\]

and internal filler flag \(\pi=(g_1,\ldots,g_d)\).  Its two old-only chains
are

\[
\begin{aligned}
 P_j^-&=Z\cup\{b,g_1,\ldots,g_j\},\\
 S_j^-&=Z\cup\{a,g_{d-j+1},\ldots,g_d\},
                         &&1\le j\le d-1,                     \tag{5A.2}
\end{aligned}
\]

while its two new-only chains are

\[
\begin{aligned}
 P_j^+&=Z\cup\{a,g_1,\ldots,g_j\},\\
 S_j^+&=Z\cup\{b,g_{d-j+1},\ldots,g_d\}.
                                                                  \tag{5A.3}
\end{aligned}
\]

These are exactly the negative and positive terms of the one-packet flag
action, reindexed by increasing chain length.

### Theorem 5A.1 (forced crossing-row obstruction)

Suppose the old chains (5A.2) are carved on the two fans by

\[
                  P_j^-\mapsto L_{j+1},\qquad
                  S_j^-\mapsto R_{j+1}.                       \tag{5A.4}
\]

The typed socket code takes

\[
                              S_\tau=A_*=Z.                    \tag{5A.4a}
\]

Then every destroyed length-\(d\) crossing cell
\(C_i\), \(1\le i\le d-1\), is forced outside \(Z\) to contain

\[
                         \{a,b,g_1,\ldots,g_d\}.               \tag{5A.5}
\]

Consequently no \(C_i\) can equal any target in either new chain (5A.3).
Thus putting the \(d-1\) NEW-chain pins on the destroyed crossing cells,
repaying them natively, and using the fans for all OLD-chain pins has no
literal common-cap state.

#### Proof

The exact star trace identity gives

\[
                 Z\cup C_i=L_{i+1}\cup R_{d-i+1}.             \tag{5A.6}
\]

Using (5A.4), the right side is

\[
\begin{aligned}
 P_i^-\cup S_{d-i}^-
   &=Z\cup\{b,g_1,\ldots,g_i\}
       \cup\{a,g_{i+1},\ldots,g_d\}\\
   &=Z\cup\{a,b,g_1,\ldots,g_d\}.                             \tag{5A.7}
\end{aligned}
\]

Therefore (5A.5) is forced independently of how the coordinates of \(Z\)
are copied to side sources.  Every \(P_j^+\) omits \(b\), and every
\(S_j^+\) omits \(a\).  Hence neither can be a crossing value.  \(\square\)

Allowing a smaller star payload \(S_\tau\subsetneq Z\) cannot escape the
obstruction.  The exact identity with \(S_\tau\) in place of \(Z\) then
forces the missing coordinates \(Z-S_\tau\) into every crossing cell as
well; (5A.5) is unchanged.

The same obstruction applies even more directly to the four
coefficientwise chain pairings of the twisted cube.

### Theorem 5A.2 (all four natural cube pairings fail)

Each natural cancellation pair can be written, after absorbing its two
fixed socket labels into a base \(B\), as

\[
 O_j^0=B\cup\{x_0\}\cup H_j,\qquad
 O_j^1=B\cup\{x_1\}\cup H_j,\qquad 1\le j\le d-1,             \tag{5A.8}
\]

where \(x_0\ne x_1\), neither \(x_s\) belongs to \(B\cup H_{d-1}\), and
\(H_1\subset\cdots\subset H_{d-1}\) is one orientation of the neutral
filler flag.  The new phase exchanges the two occurrence chains, so every
candidate NEW-chain target is a member of one of the two families in
(5A.8).

If the two OLD families in (5A.8) are put on the two fan shores, every
crossing value contains both \(x_0,x_1\).  Hence no crossing value is a
NEW-chain target.  This holds for all four natural pairings and every
\(d\ge2\).

#### Proof

Put \(O_j^0\) on \(L_{j+1}\) and \(O_j^1\) on \(R_{j+1}\); exchanging the
shores makes no difference.  The common star payload is contained in
\(B\cup H_1\) and contains neither \(x_0\) nor \(x_1\).  For every crossing
index \(i\), the exact fan--crossing identity gives

\[
 S_\tau\cup C_i
   =O_i^0\cup O_{d-i}^1
   \supseteq B\cup\{x_0,x_1\}.                               \tag{5A.9}
\]

Thus \(x_0,x_1\in C_i\).  A target \(O_j^s\) contains \(x_s\) and omits
\(x_{1-s}\), so it cannot equal \(C_i\).  \(\square\)

For completeness, the four rows of (5A.8), suppressing
\(K\cup\{\infty\}\), are

\[
\begin{array}{c|c|c|c}
\text{paired OLD chains}&B&(x_0,x_1)&\text{neutral order}\\ \hline
0P,\ 1P&\{b_0,c_0\}&(a_1,a_0)&M\\
0S,\ 2P&\{b_1,c_0\}&(a_0,a_1)&M^{\rm rev}\\
1S,\ 3P&\{b_0,c_1\}&(a_1,a_0)&M^{\rm rev}\\
2S,\ 3S&\{b_1,c_1\}&(a_0,a_1)&M.
\end{array}                                                   \tag{5A.10}
\]

Therefore the proposed closure is not rescued by choosing another one of
the four synchronized cancellation pairs.  A viable one-cell construction
must mix chain families beyond these natural pairs, use non-NEW crossing
targets, or alter the seam geometry.

The obstruction has a smallest possible local certificate: one proposed
crossing row together with coordinate \(b\) for a prefix target, or
coordinate \(a\) for a suffix target.  The fans force that coordinate to
one while the typed NEW target forces it to zero.  This is a trace
incompatibility, not a Hall overload.

In the language of Section 5, the cap-state family for this prescribed
OLD/NEW assignment is empty.  The abstract fan graph may have the desired
perfect matching, and the typed singleton \(A_*=S_\tau\) may itself be a
literal nonzero occurrence, but neither fact reaches (5.1), because the
same source letters cannot realize the prescribed crossing pins.

The exact live alternatives are therefore to change at least one of:

1. the pair of old chains assigned to the two fans;
2. the \(d-1\) crossing targets;
3. the filler alignment or packet used on one shore; or
4. the one-cell seam normal form.

For any revised proposal, the simultaneous fan--crossing criterion must be
checked before applying the residual Hall criterion (3.1).

### Theorem 5A.2 (all twisted-cube chain pairings are excluded)

The eight OLD chain families of the twisted cube have, after suppressing
the common `K infinity` part and the nested neutral flag, the eight distinct
cube triples

\[
                         \{a_i,b_j,c_k\},\qquad
                         (i,j,k)\in\{0,1\}^3.                \tag{5A.8}
\]

No ordered pair of distinct OLD chain families can occupy the two fans while
the destroyed crossing cells carry targets from any OLD or NEW twisted-cube
chain family.  Reusing the same chain family on both fans does not give the
required `2(d-1)` distinct targets.  Hence there is no alternative
cross-packet chain pairing inside this four-cube which repairs the canonical
crossing defect.

#### Proof

Let the two distinct fan-chain base triples be `B` and `B'`.  Their common
star payload is contained in the intersection of every fan target, hence in

\[
                  K\cup\{\infty\}\cup(B\cap B').             \tag{5A.9}
\]

Every label in the symmetric difference of `B,B'` is therefore outside the
star payload and occurs in every target on one fan shore.  The exact
star-hidden identity forces all labels of that symmetric difference into
every crossing cell.  Since `B` and `B'` are distinct transversals of the
three pairs `\{a_0,a_1\}`, `\{b_0,b_1\}`, `\{c_0,c_1\}`, they differ on at
least one axis.  The symmetric difference then contains both labels on that
axis.  Every target in every OLD or NEW cube chain contains exactly one
label on each axis, so equality is impossible.  Common labels of `B,B'`
may be programmed through the star; this does not affect the forced doubled
axis.

If the two fan families coincide, their `d-1` target sets coincide.  They
cannot constitute the `2(d-1)`-element target bank `O` assumed in (0.2).
This exhausts all pairs.  At `d=2` a distinct pair gives one crossing demand
with no chain-bank neighbour, so the obstruction is already the smallest
`1/0` incidence cut.  \(\square\)

The repeated-family case is excluded by the target-injective ledger, not by
a trace contradiction.  A differently budgeted occurrence-multiset design
which does not require the bank (0.2) is outside Theorem 5A.2, as are
noncatalogue fan targets, altered/non-disjoint label cores, and an exterior
gammoid return.

## 6. Interface with the twisted cube

The four-packet twisted cube pairs its nested lower-chain occurrences
coefficientwise at every depth.  The endpoint-chain theorem turns those
pairs into literal return columns when the cells are prepared independently
of the one-cell seam.

The attractive combined ledger would choose the \(d-1\) destroyed crossing
pins from a new-chain bank, repay them on post-switch native cells, and put
the \(2(d-1)\) old-chain targets on the fans.  Theorem 5A.1 proves that this
specific simultaneous realization is impossible: the OLD fan values force
crossing values which are not NEW-chain values.  Theorem 5A.2 rules out a
different pairing of two cube-chain families as an escape.  Thus the formal
count \(\alpha=\ell+1\) is not physically attained anywhere in this
chain-only four-cube face.

For a revised seam whose fan and crossing rows first pass the exact
star-trace criterion, the remaining strict gain is indeed concentrated in
(5.1).  A literal two-sided carve and spare edge (4.3) in one nonzero cap
state then give the one-cell seam hypothesis of the Pascal stutter theorem.
Without that edge, the closed local outcome is \(\alpha=\ell\) and (3.1)
is the minimal residual Hall cut.

The remaining route is genuinely nonlocal: change the crossing target bank
to the forced star-compatible shapes and exhibit other cells for it, alter a
fan chain outside the cube-chain catalogue, or use a trace-guarded exterior
gammoid return whose endpoint is not one of these crossing cells.  No such
return is constructed here.

## 7. Independent audits

Three dependency-free symbolic replays cover the decisive interfaces.

* `scratch/audit_ad_one_cell_oldfan_newcrossing_obstruction_20260801.py`
  checks Theorem 5A.1 for `2<=d<=16`; its payload is
  `a6bc184079accfc37ac7c960df385d55cd76e5b3d9a747ef8d73b6747349de28`.
* `scratch/audit_ad_twisted_cube_all_fan_pair_obstruction_20260801.py`
  checks all 56 ordered distinct pairs and the eight repeated pairs in
  Theorem 5A.2.  It reports
  `PASS_AD_TWISTED_CUBE_ALL_FAN_PAIR_OBSTRUCTION` with payload
  `e6bbd350239aff11b2fb987c136aeaf14e662a9446db5c4551696de251bb4cbd`.
* `scratch/audit_ad_one_cell_two_fan_coatom_glue_20260801.py` independently
  materializes the same-packet glue for `2<=d<=32`, replays the owner
  stutter, and verifies zero crossing incidence to the NEW bank.  Its
  payload is
  `1400d4bca88dac45822762d5c18c8f2da773d01e5c5d8cbe3c2c764ec52b6762`.

These are finite replays of dimension-independent set identities; the
proofs above, rather than extrapolation from the checked depths, establish
the all-`d` statements.
