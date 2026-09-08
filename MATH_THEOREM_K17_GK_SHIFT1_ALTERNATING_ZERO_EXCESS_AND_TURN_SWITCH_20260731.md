# K17 adjacent-GK residual matching: zero endpoint excess and the exact turn-aware switch criterion

Date: 2026-07-31  
Status: **proved finite GO** for the 572-direct-bank residual row/rank-eight/
endpoint-capacity/boundary-turn problem.  The canonical twice-up matching has
exact endpoint excess 2,730, while an authenticated alternating re-matching
has excess zero.  Its remaining turn defect is exactly 17 illegal local
wedges plus 1,764 central rank-nine collision units.  A necessary-and-
sufficient finite criterion for any alternating switch to remove those
defects is given below.

This note does **not** construct the 4,534 repeat edges, the prescribed
length-four/five ears, one component path, a prefix, or a K17 word.

## 1. The residual incidence system

Fix the adjacent-cut `s=1` GK seed and the authenticated bank of 572 direct
`B-B` ears.  Let

* `L` be the 8,164 remaining missing rank-six colours;
* `Q` be the 11,906 surviving fresh rank-eight resources;
* `B` be the 6,136 free endpoints of the old GK dominoes;
* `U` be the 12,168 unused rank-seven vertices.

Every supported incidence `e=(D,Q)` has a unique Johnson edge

\[
 \partial e=\{D+a,D+b\},\qquad Q=D+\{a,b\}.             \tag{1.1}
\]

The frozen relation has exactly 242,771 such incidences and 4,658 possible
boundary-turn resources.

After the direct bank, every incidence has type `EU` or `UU`.  Give vertices
the capacities

\[
                 c(v)=1\quad(v\in B),\qquad
                 c(v)=2\quad(v\in U).                   \tag{1.2}
\]

For an `EU` incidence with old endpoint `b`, unused endpoint `u`, and old
mate `\bar b`, define its forced boundary turn

\[
                       h(e)=\bar b\cup b\cup u.           \tag{1.3}
\]

A residual provider matching is a set `M` satisfying

\[
 \deg_M(D)=1\ (D\in L),\qquad \deg_M(Q)\le1\ (Q\in Q).  \tag{1.4}
\]

Its endpoint excess is

\[
 \Phi(M)=\sum_{v\in B}(d_M(v)-1)_+
          +\sum_{v\in U}(d_M(v)-2)_+.                   \tag{1.5}
\]

Thus `Phi=0` is exactly the rank-seven capacity row; it says nothing yet
about pairing selected edges into legal wedges.

## 2. Exact zero-excess theorem

Let `M_0` be the canonical twice-up selection

\[
                         D\longmapsto U_0^2(D).           \tag{2.1}
\]

The order-zero GK chain inverse proves that (2.1) is injective on rank-eight
resources.  Every one of its incidences survives the conditioned residual
provider relation.  Its exact edge-type and degree data are

\[
 (EU,UU)=(4524,3640),                                    \tag{2.2}
\]

\[
\begin{array}{c|rrrrrrr}
\text{degree on free }B&0&1&2&3&4&5&6\\ \hline
\text{number}&3432&1430&858&308&88&18&2,
\end{array}                                               \tag{2.3}
\]

and

\[
\begin{array}{c|rrrrrrr}
\text{degree on }U&0&1&2&3&4&5&6\\ \hline
\text{number}&4004&5434&2002&572&132&22&2.
\end{array}                                               \tag{2.4}
\]

Consequently

\[
 \Phi_B(M_0)=1820,
 \qquad \Phi_U(M_0)=910,
 \qquad \boxed{\Phi(M_0)=2730}.                          \tag{2.5}
\]

### Theorem 2.1 (finite zero-excess residual matching)

There is a residual matching `M_*` with all of the following properties:

1. every one of the 8,164 rows occurs once;
2. its 8,164 rank-eight resources are distinct and disjoint from the direct
   bank and old seed palette;
3. `Phi(M_*)=0`;
4. all `EU` boundary turns (1.3) are distinct and avoid the 1,144 direct-bank
   boundary turns.

Its exact data are

\[
                       (EU,UU)=(3065,5099),               \tag{2.6}
\]

\[
\begin{array}{c|rr}
\text{degree on free }B&0&1\\ \hline
\text{number}&3071&3065,
\end{array}
\qquad
\begin{array}{c|rrr}
\text{degree on }U&0&1&2\\ \hline
\text{number}&4416&2241&5511.
\end{array}                                               \tag{2.7}
\]

#### Proof

The TSV certificate cited in Section 7 has one row for each `D`.  An
independent dependency-free replay reconstructs the seed and direct bank,
checks every selected `(D,Q)` against the complete supported menu, checks
(1.1), rank-eight freshness and injectivity, and evaluates every rank-seven
degree.  It obtains (2.6)--(2.7), so (1.5) is zero.  It also reconstructs
(1.3), obtaining 3,065 distinct new boundary turns, all disjoint from the
direct bank.  Since `Phi` is nonnegative, this certificate proves that the
minimum possible endpoint excess is exactly zero.  No timeout or objective
bound is used in that last conclusion.  \(\square\)

The repeat-edge scalar complement is therefore forced to be

\[
                (EU_{\rm rep},UU_{\rm rep})=(3069,1465). \tag{2.8}
\]

The provider matching touches 7,752 unused vertices.  Selecting 1,879 more
currently untouched vertices leaves unused-vertex degree demand

\[
              2241+2(1879)=5999=3069+2(1465).            \tag{2.9}
\]

Likewise, 3,069 of the 3,071 unused old endpoints can receive repeat `EU`
edges, leaving two path terminals.  Equations (2.8)--(2.9) prove only scalar
capacity compatibility; they do not produce those repeat edges.

## 3. Alternating path/cycle normal form

### Lemma 3.1 (row/rank-eight preserving normal form)

Let `M,N` be two matchings satisfying (1.4).  Their symmetric difference is
a disjoint union of:

* even alternating cycles; and
* alternating paths whose two endpoints lie on the rank-eight shore, one
  endpoint used only by `M` and the other only by `N`.

Toggling any union of complete components preserves one selected incidence
per row and rank-eight injectivity.

#### Proof

In \(M\mathbin\triangle N\), every row has degree zero or two, while every rank-eight
vertex has degree at most two.  Thus every nontrivial component is a path or
a cycle.  A path cannot end on the row shore, so both endpoints are
rank-eight vertices.  Alternation gives the asserted endpoint types.  On a
complete component every row loses and gains one edge; every internal
rank-eight vertex does the same, and the path exchanges its used endpoint
for its unused endpoint.  \(\square\)

Relative to `M_0`, the authenticated `M_*` leaves 667 rows unchanged and
changes 7,497 rows.  Its exact normal form has

\[
 1982\text{ alternating paths carrying }6528\text{ rows},\qquad
 263\text{ alternating cycles carrying }969\text{ rows}. \tag{3.1}
\]

The largest component carries 52 rows.  This is a literal large-support
augment from the canonical matching, not a claim that the components can be
toggled in an arbitrary order while preserving physical capacities.

Indeed, row/rank-eight components can share rank-seven vertices and
rank-nine labels.  Their physical effects therefore add before feasibility
is tested.

## 4. Signed physical effect of a switch

Let `S` be a union of complete alternating components relative to a current
matching `M`, and put `M'=M triangle S`.  Define the signed endpoint change

\[
 \sigma_S(v)=
 \#\{e\in S\setminus M:v\in\partial e\}
 -\#\{e\in S\cap M:v\in\partial e\}.                    \tag{4.1}
\]

For boundary turns define

\[
 \tau_S(H)=
 \#\{e\in(S\setminus M)\cap EU:h(e)=H\}
 -\#\{e\in(S\cap M)\cap EU:h(e)=H\}.                   \tag{4.2}
\]

Then, identically,

\[
             d_{M'}(v)=d_M(v)+\sigma_S(v),qquad
             b_{M'}(H)=b_M(H)+\tau_S(H),                 \tag{4.3}
\]

where `b_M` includes the fixed direct-bank boundary turns.  Hence endpoint
capacity and boundary privacy are equivalent to the finite inequalities

\[
 0\le d_M(v)+\sigma_S(v)\le c(v),qquad
 0\le b_M(H)+\tau_S(H)\le1.                              \tag{4.4}
\]

The exact endpoint-excess change, useful for an augmenting algorithm, is

\[
 \Delta\Phi(S)=
 \sum_v\left[(d_M(v)+\sigma_S(v)-c(v))_+
                    -(d_M(v)-c(v))_+\right].             \tag{4.5}
\]

Formula (4.5), rather than a count of changed rows, is the correct
capacity-descent score.

For fixed nonnegative physical-resource prices, finding a minimum-price
row-perfect/rank-eight-injective selection is an ordinary weighted bipartite
matching problem.  But the exact caps (4.4) couple two rank-seven resources
to each `(D,Q)` incidence, and turn legality below couples pairs of selected
incidences.  Thus the unpriced exact problem is not reduced here to an
ordinary min-cost flow.  The finite zero-excess theorem is supplied by the
authenticated integral certificate, not by an unproved total-unimodularity
claim.

## 5. Wedges and the exact rank-nine defect

Suppose an unused vertex `u` has degree two in `M`, with selected edges
`ux` and `uy`.  Its prospective central turn is

\[
                            H_u=x\cup u\cup y.            \tag{5.1}
\]

Call this selected pair a **legal wedge** when:

1. `|H_u|=9`;
2. if `x,y` are both old endpoints, they lie in distinct old dominoes; and
3. `H_u` differs from every forced boundary turn contributed locally by
   an incident `EU` edge.

The global central-turn bank is legal exactly when, in addition, all values
`H_u` are distinct and avoid the entire boundary bank.

For `M_*`, all 5,511 degree-two unused vertices have the correct rank and
old-component geometry.  Exactly 17 fail condition 3: in every one of those
17 cases the central value (5.1) is literally equal to an incident `EU`
boundary turn.  There are no other local failure types.

After omitting those 17 illegal pairs, the 5,494 compatible centres use only
3,991 distinct central values.  Thus

\[
                 5494-3991=1503                         \tag{5.2}
\]

central repeat units occur.  Exactly 261 of the 3,991 central values also
occur in the already injective direct-plus-`EU` boundary bank.  Therefore

\[
            \boxed{1503+261=1764}                       \tag{5.3}
\]

is the exact central rank-nine collision excess of this certificate.  The
17 illegal wedges are separate from (5.3).

Define the turn potential

\[
 \Psi(M)=I(M)+\sum_H\bigl(m_M(H)-1\bigr)_+,              \tag{5.4}
\]

where `I(M)` is the number of illegal degree-two wedges and `m_M(H)` counts
the boundary bank plus the central turns of legal wedges.  Then

\[
                         \Psi(M_*)=17+1764=1781.          \tag{5.5}
\]

This is an exact diagnostic for `M_*`, not a lower bound over all residual
matchings.

## 6. Exact finite switch criterion

Let `A(S)` be the unused rank-seven vertices incident with a changed edge of
an alternating switch `S`.  Only centres in `A(S)` can change their selected
wedge.  For each rank-nine value `H`, let

\[
 \gamma_S(H)=
 \#\{u\in A(S):u\text{ is legal in }M',\ H_u(M')=H\}
 -\#\{u\in A(S):u\text{ is legal in }M,\ H_u(M)=H\}.      \tag{6.1}
\]

### Theorem 6.1 (turn-aware alternating-switch criterion)

An alternating union `S` converts `M` into a row/rank-eight/endpoint/
turn-clean provider selection `M'` if and only if all of the following hold:

1. `S` is a union of complete components from Lemma 3.1;
2. the endpoint and boundary inequalities (4.4) hold;
3. every degree-two unused vertex outside `A(S)` was already a legal wedge,
   and every degree-two unused vertex in `A(S)` is a legal wedge after the
   switch;
4. for every rank-nine mask `H`,

\[
              0\le m_M(H)+\tau_S(H)+\gamma_S(H)\le1.     \tag{6.2}
\]

#### Proof

Condition 1 is exactly Lemma 3.1, so it is equivalent to preservation of
the row and rank-eight matching rows.  Equations (4.3) make condition 2
equivalent to endpoint capacity and boundary injectivity.  A wedge changes
only when one of its incident edges changes, proving the locality statement
in condition 3.  Finally, (4.2) and (6.1) partition the signed change of the
complete rank-nine bank into boundary and central contributions.  Hence
(6.2) is equivalent to global rank-nine injectivity.  These are precisely
the declared provider-stage constraints, proving necessity and sufficiency.
\(\square\)

For a switch that is not yet clean, (4.5) and

\[
 \Delta\Psi(S)=I(M')-I(M)+
 \sum_H\left[(m_M(H)+\tau_S(H)+\gamma_S(H)-1)_+
                         -(m_M(H)-1)_+\right]             \tag{6.3}
\]

give an exact lexicographic augment score.  Path/cycle components are
independent in row/rank-eight space but not in (4.4) or (6.2); their signed
vectors must be summed before accepting a packet.  Theorem 6.1 is therefore
the proof-safe finite criterion for an alternating-cycle search or a
min-cut/column-generation algorithm.

It still omits the 4,534 repeat-edge columns.  In particular, `Psi=0` would
not by itself prove the final `f`-factor, prescribed ear lengths, or one-path
topology.

## 7. Frozen artifacts and hashes

Inputs and selected matching:

```text
scratch/h2_k17_cyclic_supported_hall_20260731/shift01.providers.tsv
  SHA-256 6b2d9802d028cca79064278a65020d8ec28e3cc1b04d59c518d29b66b1a68e97
scratch/independent_k17_gk_shift1_exceptional_bb_20260731.tsv
  SHA-256 7abcbd84c926a4b6fb7154b2b2554d07282508eae10e7b411e2b9a2217231b8d
scratch/independent_k17_gk_shift1_residual_cap_20260731.tsv
  SHA-256 7e5706b65996e6d303108114c69f41c381a8743799da048c928eb9b2e50a47ff
```

Independent alternating/zero-excess/turn replay:

```text
scratch/audit_k17_gk_shift1_residual_zero_excess_20260731.py
  SHA-256 6cdd43a5712fc351829f3cc26f082c1df19a3d5e63b2b256d9f82b6884549648
scratch/k17_gk_shift1_residual_zero_excess_20260731.audit.json
  SHA-256 d10f6bcf9b35f3c26984732dc2bab7dc9d20daa04ce6b9381dbaa8f01c10ba71
  canonical payload 35631aa48f137f281588a40f2edc393ad93cc1edd0a18bcb2b63ce47244378b0
```

The earlier independent wedge replay agrees exactly:

```text
scratch/audit_independent_k17_gk_shift1_residual_cap_20260731.py
scratch/independent_k17_gk_shift1_residual_cap_replay_20260731.audit.json
  canonical payload 952b19f4df8b8a920107448a9b66bc4e1c4d2ee6b5760538933222d23c538ff5
```
