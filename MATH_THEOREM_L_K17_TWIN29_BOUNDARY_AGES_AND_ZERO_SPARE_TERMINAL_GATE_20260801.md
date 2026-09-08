# The k=17 twin-29 host has two literal boundary failures, and its fixed compiler reserve has rank zero

**Date:** 2026-08-01  
**Lane:** L, boundary residence / one-oriented terminal compiler  
**Status:** exact endpoint-age theorem, exact replay of the frozen seven-factor,
exact cut-index correction, and exact zero-spare strict-gammoid obstruction.
The protected owner/lower/rank-ten factor is taken as an input and is not
re-solved here.  No rethreaded resident chronology, deeper-upper completion,
or terminal compiler is claimed.

## 0. Verdict

For `k=17,d=3`, the protected reset path and the redesigned Ferrers paths
have 29 owners and 26 Johnson edges.  Their interiors are depth-three
resident, but the two bank paths have four clipped ends.  In the coordinate
order

```text
h1,h2,x1,x2,x3,c1,c2,c3,u1,u2,u3,y1,y2,y3,alpha,delta,z
```

the exact endpoint ages are

\[
\begin{array}{c|c|c}
\text{end}&\text{coordinates and ages}&\text{additional-owner debts}\\ \hline
P_X^-&(h_2,x_1,x_2):(3,2,1)&(1,2,3)\\
P_X^+&(h_1,x_3,x_2):(3,2,1)&(1,2,3)\\
P_U^-&(y_1,u_1,u_2):(3,2,1)&(1,2,3)\\
P_U^+&(c_3,u_3,u_2):(3,2,1)&(1,2,3).
\end{array}                                                   \tag{0.1}
\]

The frozen seven-cycle factor supplies enough ambient age at `P_X`-right
and `P_U`-right.  It fails exactly at

\[
                         P_X\text{-left}:x_1,
             \qquad      P_U\text{-left}:u_1.              \tag{0.2}
\]

The previously written two collars cover `P_X`-right and `P_U`-left.
Consequently those two collars plus the *actual* other two continuations
still leave the first failure in (0.2); that conditional two-collar layout
is not a residence certificate for this factor.  Four literal collars
remove dependence on ambient continuation for the four old clipped bank
runs only, and only conditional on legal Johnson realizations with
collision-safe fillers, private q1 resources, no new short runs and legal
outer continuations.  They must be realized by reselecting incidences: the
spanning factor has no unused owner or lower-shore vertices.  Physical
source/compiler cells do not yet exist because no antecedent chronology has
been constructed.

The frozen factor is much farther from a terminal source than these two
boundary failures.  Its seven cycles have `3073` cyclic runs of length two
and `2710` of length three.  Even the best independent opening of every
cycle leaves `5760` short internal runs.  It also has `1502,295,9` missing
upper values at ranks `11,12,13`.  Therefore this factor has no literal
depth-three antecedent and no terminal compiler graph yet.

Finally, the fixed one-pivot compiler atlas has exactly

\[
 |\mathcal T|=|\mathcal C|=65535.                         \tag{0.3}
\]

If a fixed-cap compiler matching exists, the dual transversal/strict
gammoid on its cells has rank zero.  Thus a deletion-only return or collar
hazard is safe **iff it is empty**.  A viable construction must make every
return compiler-transparent, contract a distinct target together with each
reserved cell, or construct and match the final changed cap graph afresh.
This conclusion holds at every best cut.  It is not a proof that a freshly
compiled final chronology is impossible.

## 1. The protected object used as input

The three paths are

```text
packet:
47331 45287 41199 33023 33247 33695 34591
18207 17983 17535 16639 18683 22771 30947

P_X:
63630 63686 63714 63713 61681 57593

P_U:
64259 63811 63587 61543 57455 49279 49405 50397 50845
```

The upstream exact audit proves that these are 29 distinct rank-nine
owners, their 26 intersections are distinct rank-eight values, their 26
unions are distinct rank-ten values, and their protected owner intervals
cover the complete two-triangle leave.  The twelve target ranks are

\[
              10^1,11^2,12^3,13^1,14^2,15^3.             \tag{1.1}
\]

The combined factor

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
```

contains all 52 protected incidences, has all 24,310 owners and all 24,310
rank-eight lower colours at degree two, and covers every one of the 19,448
rank-ten values.  It has component sizes

\[
                  14305,8615,1362,18,4,3,3.              \tag{1.2}
\]

This note reads that certificate.  It does not repeat its residual-flow or
`C6` search.

## 2. Exact endpoint-age criterion

Let `Z_0,...,Z_s` be a protected owner path and suppose a coordinate `a`
has a positive run of length `e<4` beginning at `Z_0`.  Let
`W_1,W_2,...` be the ambient owners encountered outward from `Z_0`.

### Lemma 2.1 (one-ended age criterion)

If this join is internal to the final chronology, the old clipped run of
`a` is resident iff

\[
             W_1,\ldots,W_{4-e}\ \hbox{all contain }a.     \tag{2.1}
\]

At a global endpoint the run may instead remain clipped.  Formula (2.1)
certifies only the old clipped run: the outward continuation must separately
have no new internally bounded run below four.

#### Proof

Let `b` be the number of consecutive outward owners containing `a` before
the first omission.  The joined positive run has length `e+b`.  It is
internal and is resident exactly when `e+b>=4`, which is (2.1).  If no
omission occurs before the global endpoint, the run is clipped instead.
\(\square\)

Applying Lemma 2.1 to the explicit masks gives (0.1).  Equivalently, the
two continuations omitted by the conditional two-collar theorem must obey
the nested superlevel constraints

\[
\begin{aligned}
P_X^-:\quad&A_1\supseteq\{h_2,x_1,x_2\},\quad
 A_2\supseteq\{x_1,x_2\},\quad A_3\supseteq\{x_2\},\\
P_U^+:\quad&B_1\supseteq\{c_3,u_3,u_2\},\quad
 B_2\supseteq\{u_3,u_2\},\quad B_3\supseteq\{u_2\}.
                                                               \tag{2.2}
\end{aligned}
\]

They must additionally be Johnson-attached, preserve private owner/lower/
upper resources, create no new short run, and obey the eventual rooted
`M_0` and compiler rows.  Containment (2.2) alone is not a host theorem.

The raw protected forest has 29 owners, 26 Johnson edges, and 52 incidence
edges.  Two length-three collars give upper bounds `35,32,64`; four give
`41,38,76`.  These are protected-subgraph sizes, not extra vertices of the
spanning factor and not extra positions in the length-24,313 word.

## 3. Literal boundary replay in the seven-factor

All three protected paths lie in its 14,305-owner component.  The first
three outward owners at the four bank ends are

\[
\begin{array}{c|ccc}
P_X^-&63642&59547&59609\\
P_X^+&58553&26297&26283\\
P_U^-&64011&64138&96906\\
P_U^+&42653&9917&5821.
\end{array}                                                \tag{3.1}
\]

The reader records the following prefix ages, truncated at eight, against
(0.1):

\[
\begin{array}{c|ccc|c}
\text{end}&\multicolumn{3}{c|}{\text{ambient ages in the coordinate order of (0.1)}}
 &\text{verdict}\\ \hline
P_X^-&2&0&\ge8&x_1\text{ fails}\\
P_X^+&4&2&\ge8&\text{pass}\\
P_U^-&\ge8&0&4&u_1\text{ fails}\\
P_U^+&\ge8&4&6&\text{pass}.
\end{array}                                                \tag{3.2}
\]

For example, `x_1` already has age two inside `P_X^-` but is absent from
the first outside owner 63642, so its joined run remains length two.
Likewise `u_1` is absent from 64011.  This proves (0.2).

The two collars frozen in the general theorem act at `P_X^+` and `P_U^-`.
These are proposed collar schedules, not collars constructed by the present
audit.  If legally realized, the latter repairs the `u_1` failure, while the former covers an endpoint
which the present ambient cycle already passes.  The uncollared `P_X^-`
still fails.  One may prospectively move a collar to a failing end, but its
new owners and q1 colours have not been embedded in this factor.  The
four-collar option is unconditional only as a boundary-residence module;
even there it is conditional on actual collision-free Johnson collars and
legal outer continuations.  It is not an unconditional global residence
completion, and its finite `k=17` factor/root/compiler compatibility remains
open.

The alternating `M_0/M_1` parity on the common component has one further
literal local consequence.  The displayed packet and `P_X` orientations
induce the same `M_0` parity, while displayed `P_U` induces the opposite
parity.  Reversing `P_U` makes all three protected paths coherent with one
alternating `M_0`.  Its interval deck and q1 resources are reversal
invariant, but its boundary/collar directions must then be replayed.  This
closes only the protected parity screen, not the global fixed-`M_0` head or
graphic row.

## 4. The frozen factor is not a compiler input

For a cyclic component `C` and coordinate `a`, let a short run be a maximal
cyclic positive run of length at most three.  Opening at one edge can make
a short run boundary-clipped exactly when that edge lies in its run or one
of its two bounding edges.  Hence, if `g_C(e)` counts the short runs clipped
by opening edge `e`, the exact number remaining after independently opening
all components is

\[
       \sum_C\left(s_C-\max_{e\in E(C)}g_C(e)\right).      \tag{4.1}
\]

The replay of all component-coordinate runs gives

\[
 \#R_1=0,\qquad \#R_2=3073,\qquad \#R_3=2710,
 \qquad (4.1)=5760.                                      \tag{4.2}
\]

Thus choosing component orientations and openings, then concatenating at
those openings, cannot give depth-three residence.  An internal exchange
or a different residual factor is necessary.  Separately, its cyclic
upper deck has holes

\[
                 1502,295,9\quad\text{at ranks }11,12,13. \tag{4.3}
\]

Rank-ten completeness does not imply (4.3) is repaired.  Residence,
deeper-upper support, and seven-component joining must be solved on one
rethreaded order before maximal erosion produces a source `A`.  Until then
there is no literal allowed-incidence graph `Adm_A` on which to run a
terminal Hall or common-cap test.

## 5. Cut indexing and the six best cuts

Let `Z_i` be the cyclic packet owners and

\[
                  A_i=Z_i\cap Z_{i-1}\cap Z_{i-2}\cap Z_{i-3}.
                                                               \tag{5.1}
\]

Then `A_c,...,A_(c+13),A_c,A_(c+1),A_(c+2)` reconstructs the owner path

\[
                         Z_c,Z_{c+1},\ldots,Z_{c-1}.       \tag{5.2}
\]

Therefore the source start `c` omits owner edge `(c-1,c)`, not `(c,c+1)`.
The exact source/edge pairs for the six minimum-loss starts are

\[
 (3,2),(4,3),(5,4),(10,9),(11,10),(12,11).              \tag{5.3}
\]

The old all-cut producer used `solve_cut(c)` for the factor while using
source start `c` for restitution.  Since every one of its fourteen factor
rows passed, the all-cut existence theorem survives; only a cut-specific
factor/master association needs the shift (5.3).

An explicit coordinate conjugacy maps the displayed 29-owner object to
source start 4 / omitted owner edge 3.  Whole reversal gives source 11 /
edge 10.  Hence the frozen complete-29 factor materializes only the pair
`{4,11}`.  Separate protected templates/factors are still needed for
`{3,12}` and `{5,10}`.

For existential quotient induction only starts `3,4,5` require independent
one-oriented solves; reflection sends them to `12,11,10`.  “Common” means
one cap/source/compiler jointly serving the chosen oriented child.  It does
not mean a fixed-address matching in an intersection with its reflection or
one factor common to all six starts.

## 6. The exact zero-spare strict-gammoid theorem

The one-pivot terminal atlas has

\[
 24313\text{ singleton cells},\qquad
 24312\text{ adjacent-pair cells},\qquad
 16910\text{ triple cells},                              \tag{6.1}
\]

whose total is 65,535, the number of nonempty strict-lower Boolean targets.
Fix a cap/trace state `theta` and suppose its compiler graph

\[
                G_\theta=(\mathcal T,\mathcal C;E_\theta) \tag{6.2}
\]

has a matching saturating all targets.  Let `M_theta` be its transversal
matroid on the cell ground set.

### Theorem 6.1 (rank-zero deletion reserve)

For the square atlas (6.1),

\[
                         r(M_\theta^*)=0.                 \tag{6.3}
\]

Consequently a cell-deletion hazard `D` preserves a target-saturating
matching iff `D=emptyset`.

#### Proof

Target saturation and (0.3) give

\[
              r_{M_\theta}(\mathcal C)=65535=|\mathcal C|.
\]

Thus `M_theta` is the free matroid on its whole cell ground set and its dual
has rank zero.  Equivalently, for every `D`,

\[
\begin{aligned}
r_{M_\theta^*}(D)
 &=|D|-65535+r_{M_\theta}(\mathcal C-D)\\
 &\le |D|-65535+(65535-|D|)=0.                           \tag{6.4}
\end{aligned}
\]

By the exact dual-transversal identity, safe deletion is independence in
`M_theta^*`, so only the empty set is safe. \(\square\)

If `q` target-cell pairs are allowed edges in the final cap state and are
jointly extendable to a perfect matching, contract those pairs.  The
residual graph is again perfectly matchable and square, so every
**additional** deletion is still impossible.  Distinct target and cell
labels alone do not imply this extendibility.  Under the stated hypothesis,
this is the correct
way to charge reserved cells in zero slack: each must carry its own distinct
target pin.  Merely naming a protected owner, collar, or return does not
produce such a pin.

Theorem 6.1 is uniform over all six cuts.  It does not assert that the final
packet changes delete a particular nonempty set from a fixed compiler, nor
that a new compiler cannot exist.  It says that a deletion-only reuse proof
has no positive radius.  If the chronology or cap changes, build the final
literal graph `Adm_A` and solve

\[
 \sum_{c\in Adm_A(S)}z_{S,c}=1,
 \qquad \sum_S z_{S,c}\le1,\qquad z_{S,c}\in\{0,1\},     \tag{6.5}
\]

together with the common-cap reconstruction/guard rows.  Rankwise Hall or
the old matching alone is not enough.

## 7. Exact cut-by-cut status

\[
\begin{array}{c|c|c|c|c}
\text{source start}&\text{owner edge}&\text{reversal mate}&
 \text{complete-29 factor}&\text{terminal status}\\ \hline
3&2&12&\text{not materialized}&\text{fresh chronology/cap open}\\
4&3&11&\text{frozen seven-factor}&\text{blocked by (4.2), (4.3)}\\
5&4&10&\text{not materialized}&\text{fresh chronology/cap open}\\
10&9&5&\text{not materialized}&\text{reflection only after a solve}\\
11&10&4&\text{reflected frozen factor}&\text{same exact blockers}\\
12&11&3&\text{not materialized}&\text{reflection only after a solve}.
\end{array}                                                \tag{7.1}
\]

For every row, a nonempty deletion-only hazard fails Theorem 6.1.  No row
currently has a full owner order, maximal source, terminal cap state, three
typed return hazards, or compiler certificate.  Therefore it would be
unsound either to report a compiler deficiency number or to claim common-cap
compatibility from the factor alone.

## 8. Exact next master

A proof-safe one-oriented solve may select `c in {3,4,5}` and must carry,
on the same branch:

1. the correctly indexed 29-owner template, its 52 incidences, 26 lower and
   26 upper q1 colours, twelve fixed interval witnesses, and four literal
   boundary sockets;
2. a protected-preserving rethread to one owner chronology, including the
   fixed-`M_0` parity choice (reverse `P_U` in the present factor);
3. zero short internal runs, all rank-11 through rank-13 witnesses, and a
   legal opening;
4. a nonempty maximal depth-three source with exact owner replay; and
5. one freshly built cap/guard graph satisfying the perfect compiler
   matching (6.5).

The collars cannot be added as new owners to the saturated `ML_9` factor.
They are path-reselection modules with deleted old incidences, new q1 values,
and displaced bulk obligations.  If the final chronology instantiates the
fixed 65,535-cell one-pivot atlas and matches it perfectly, Theorem 6.1 then
leaves no spare compiler cells; the present factor by itself makes no claim
about physical source cells.
This is why the topology/residence/deeper-upper/compiler rows must now be
optimized jointly rather than tested as independent appendages.

## 9. Audit artifacts and scope

The independent reader used on H100 is

```text
scratch/audit_l_k17_twin29_boundary_terminal_20260801.cpp
SHA256 ef2dd5402c71002333831130d2e53c44a72dffd4e6116c45b774695b4760a605

scratch/k17_twin29_boundary_terminal_20260801.audit.json
SHA256 933190b3e061452e4a0935678dc14bee9b569006c412e8fa743b53b0c6470a97

scratch/k17_twin29_boundary_terminal_20260801.run.out
SHA256 7c9024e89b6da11a85b74c955192aca8bb6a23b948e5e67d2f2072ccae07810e
```

It verifies all four ambient chains (to the recorded truncation), the
relative protected `M_0` parity, the displayed source-4/edge-3 cut conjugacy,
the seven literal components, rank-ten
completeness, the exact opening obstruction, and the square-compiler
arithmetic conditional on a target-saturating matching.  The other five
best cut rows and the pair `{4,11}` are imported frozen inputs rather than
recomputed by this reader.  It deliberately does not regenerate the
residual flow or the `C6` walk and does not claim a fresh compiler test.  The
deeper hole row is independently frozen by the upstream factor verifier.

Retained upstream inputs are

```text
factor TSV     7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
factor verifier 5fe2128850bfd9672f55c370131a46a6f2f993215a22a3d523a703dc74e51c3d
verifier output d49405282c791e408a20e2ff378aa66317e61c567129f50dd5f2b64ebd8ad9df
```

No statement here proves a length-24,313 universal word or improves the
known numerical upper bound for `nu(17)`.
