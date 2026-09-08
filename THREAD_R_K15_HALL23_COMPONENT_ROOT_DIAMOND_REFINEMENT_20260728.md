# Hall 23, component-root diamond refinement, and the exact Hall-22 gate

Date: 2026-07-28

Status: exact matching theorem; exact audit of the
`Hall 24 -> 24 -> 23` compound braid; exact Hall-23 DM-component atlas; and
a literal conditional root-`24610` matching certificate.  This note is
historical at its Hall-23 endpoint.  A different, now-audited physical
`Hall 23 -> 23 -> 22` pair discharges the remote `2/1` circuit
`{4877,4909}`; see
`THREAD_R_K15_NEUTRAL_ROUTER_DM_CIRCUIT_SPLITTER_20260728.md`.

## 0. Main conclusions

The verified Hall-23 state is now the authoritative base for this lane.  The
second neutral/improving braid pair is

\[
 H24\xrightarrow{\operatorname{FF}(212,3732,4717)}H24^{\rm portal}
 \xrightarrow{\operatorname{FF}(210,1501,4867)}H23.
\]

It preserves the exact middle deck, Johnson chronology, depth-three
residence, every upper support through depth seven, and the four-hole
immediate-lower palette.  Its compiler matching ranks are

\[
                  16359\longrightarrow16359\longrightarrow16360.
\]

The second move deletes, without replacement, the complete `161/160`
deficient DM component rooted at mask `20516`.  The mechanism is an exact
Boolean-diamond fission: a neutral braid first transfers one four-target
diamond between two cells; the improving braid then splits the relevant
coarse profiles into parallel diamond edges and raises local matching rank
from `160` to `161`.

The reusable theorem is stronger than this example.  In an excess-one
component, a new cell discharges the component exactly when it meets an
*exposed root*, namely a target which can be left unmatched by a maximum
matching.  In the audited Hall-23 graph, **every target of every deficient
component is exposed**.  Thus target choice inside a component is not the
next matching obstruction.  The next obstruction is physical: produce one
additional usable cell while retaining the complement matching and all
carrier ledgers.

There is a sharp next matching certificate.  The remaining `161/160`
component rooted at `24610` contains a lower-edge cell and a nearby diamond
cell, separated by 49 starts.  Duplicating the lower edge while retaining the
upper diamond edge and the audited old matching gives Hall 22.  No resident,
upper-safe segment braid realizing that fission has yet been constructed.

The seven zero-degree targets remain separate `1/0` DM components.  Any
continuation which leaves them zero has Hall deficiency at least seven.
Target `2575` has acquired a first cell on a different Hall-25 branch, but no
fusion of that zero repair with the Hall-23 carrier is proved.

## 1. Matching notation

Let

\[
                         G=(L,R,E)
\]

be a finite bipartite target/cell graph.  Write `nu(G)` for its matching
number and

\[
                         h(G)=|L|-\nu(G)
\]

for its left Hall deficiency.  A connected induced subgraph

\[
                         D=G[X,Y]
\]

is called an excess-one component when

\[
                 |X|=|Y|+1,\qquad \nu(D)=|Y|.
\tag{1.1}
\]

Its exposed-root set is

\[
 \rho(D)=\{x\in X:\nu(D-x)=|Y|\}.
\tag{1.2}
\]

Thus `x` is exposed precisely when some maximum matching of `D` leaves `x`
unmatched.

For a target shore `S`, define its deficiency and its slack below the global
maximum by

\[
 \delta_G(S)=|S|-|N_G(S)|,
 \qquad
 \sigma_G(S)=h(G)-\delta_G(S)\geq0.
\tag{1.3}
\]

If a trade changes `G` to `G'`, its exact shore current is

\[
                         I(S)=|N_{G'}(S)|-|N_G(S)|.
\tag{1.4}
\]

The identity

\[
 h(G')=h(G)-\min_{S\subseteq L}\bigl(\sigma_G(S)+I(S)\bigr)
\tag{1.5}
\]

is immediate from Hall's formula.  It is the authoritative global test when
a local component is not known to be a matching summand or when a physical
trade removes cells elsewhere.

## 2. The exposed-root discharge theorem

### Theorem 2.1 (one-cell discharge)

Let `D=G[X,Y]` satisfy (1.1), and add one new right vertex `c` whose
neighbourhood lies in `X`.  Then

\[
 \boxed{\nu(D+c)=|X|\quad\Longleftrightarrow\quad
        N(c)\cap\rho(D)\ne\varnothing.}
\tag{2.1}
\]

#### Proof

If `x` lies in the displayed intersection, take a matching of `D-x`
saturating `Y` and add the edge `xc`.  This saturates `X`.

Conversely, suppose `D+c` has a matching saturating `X`.  The new cell `c`
is matched to some `x in N(c)`.  Deleting that edge leaves a matching of
`D-x` of size `|Y|`, so `x in rho(D)`.  This proves both directions.  \(\square\)

### Proposition 2.2 (alternating-path certificate)

Fix a maximum matching `M` of an excess-one component `D`, and let `u` be
the unique left vertex unmatched by `M`.  A target `x in X` belongs to
`rho(D)` if and only if `x` is reachable from `u` by an `M`-alternating path
whose first edge is unmatched and whose last vertex lies in `X`.

#### Proof

Flipping along such a path leaves `x`, instead of `u`, unmatched.  Conversely,
if `M_x` is a maximum matching leaving `x` unmatched, the component of
`M triangle M_x` containing `u` is an alternating path from `u` to `x`.
\(\square\)

This gives a short exact audit of `rho(D)`: one alternating breadth-first
search from an unmatched target suffices.

### Theorem 2.3 (rooted refinement discharge)

Suppose `D=G[X,Y]` is an excess-one matching summand, so some maximum
matching of `G` is the disjoint union of a matching saturating `Y` and a
maximum matching of the complement.  Let a physical trade replace a bank of
right cells by another bank.  Assume that, after the replacement,

1. the complement part of that maximum matching is retained or rerouted
   without loss;
2. for some `x in rho(D)`, a matching of `D-x` saturating `Y` is retained or
   rerouted; and
3. one additional new cell is adjacent to `x` and is distinct from all cells
   used in the preceding matching.

Then the global matching number rises by at least one and the Hall deficiency
falls by at least one.  If the trade changes no matching capacity outside
`D` (in particular, if every changed cell has neighbourhood in `X` and the
complement graph is unchanged), then both changes are exactly one.

#### Proof

Keep the complement matching, keep the matching of `D-x`, and match the new
cell to `x`.  This constructs a matching of size `nu(G)+1`.  Only one new
right-cell unit can be absorbed in the excess-one summand, so under the final
no-outside-change hypothesis the increase is exactly one.  Equivalently, the
old excess-one component becomes balanced and disappears from the deficient
DM shore.  Without that hypothesis the construction still proves the stated
lower bound.  \(\square\)

The last sentence uses the stated matching-summand hypothesis.  Without it,
or when the trade deletes capacity outside `D`, (1.5) must be checked on all
shores.

### Proposition 2.4 (loss-tolerant form)

Let `M_0` be the part of a former maximum matching surviving a refinement of
`D`, and suppose

\[
                         |M_0|=|Y|-r.
\]

The refined component has a matching saturating `X` if and only if it has
`r+1` pairwise vertex-disjoint `M_0`-augmenting paths.

#### Proof

Toggling `r+1` disjoint augmenting paths raises the size from `|Y|-r` to
`|Y|+1=|X|`.  Conversely, the symmetric difference of `M_0` with a matching
saturating `X` decomposes into alternating cycles and paths, and its size
difference forces `r+1` more augmenting than deaugmenting path components.
In particular it contains at least `r+1` vertex-disjoint augmenting paths;
choose any `r+1` of them.  \(\square\)

## 3. Exact form of the Hall-24 compound braid

Let `T` be the Hall-24 middle path and split it into retained forward blocks

\[
\begin{aligned}
X_0&=T[0:210],&X_1&=T[210:212],&X_2&=T[212:515],\\
X_3&=T[515:3732],&X_4&=T[3732:4718],&
X_5&=T[4718:4868],&X_6&=T[4868:6435].
\end{aligned}
\tag{3.1}
\]

The two named `FF` braids compose to the one-path reassembly

\[
                    \boxed{T^{(23)}=X_0X_3X_5X_1X_4X_2X_6.}
\tag{3.2}
\]

All seven blocks retain their orientation.  The deleted seams are

\[
 R_0L_1,R_1L_2,R_2L_3,R_3L_4,R_4L_5,R_5L_6,
\]

and the inserted seams are

\[
 R_0L_3,R_3L_5,R_5L_1,R_1L_4,R_4L_2,R_2L_6.
\]

Their symmetric difference is the union of the two alternating circuits

\[
 R_0-L_1-R_5-L_6-R_2-L_3-R_0,
\tag{3.3}
\]

\[
 R_1-L_2-R_4-L_5-R_3-L_4-R_1.
\tag{3.4}
\]

In the rank-seven/rank-nine flag graph, these are the clean `C6` switches

\[
\begin{array}{c|c|c|c}
\text{core}&\text{rows}&\text{columns}&\text{varying coordinate labels}\\ \hline
22021&(30213,22023,22053)&(30501,30471,22311)&\{13,1,5\}\\
24621&(25645,26669,28717)&(29805,27757,30829)&\{10,11,12\}.
\end{array}
\tag{3.5}
\]

The fixed extra coordinate labels are respectively `8` and `6`.  Hence the
compound braid preserves the adjacent lower and upper flag multisets exactly
while changing their pairing.

An independent reconstruction gives

\[
\begin{array}{c|ccc}
&H24&H24^{\rm portal}&H23\\ \hline
\nu(G)&16359&16359&16360\\
h(G)&24&24&23\\
\text{zero-degree targets}&7&7&7\\
\text{immediate-lower holes}&4&4&4.
\end{array}
\tag{3.6}
\]

Every state is an exact `6435`-owner middle deck, a Johnson path, and
depth-three resident; maximal erosion is nonempty; and every upper support
at depths `q=1,...,7` is complete.

There is one important scope correction.  “Lower holes 4” in (3.6) means
the immediate lower layer.  The final braid loses the two depth-three lower
targets

\[
                         17445,\qquad28677,
\]

so its lower-depth-three hole count rises from four to six.  This compound
is not an all-lower-depth support-preserving theorem.

## 4. The exact root-20516 Boolean diamond

Put

\[
\begin{gathered}
 K=20516,\qquad a=1,\qquad b=8192,\qquad c=1024,\\
 d=2048,\qquad e=8,\qquad
 Q=K+\mathcal P(\{a,b\}).
\end{gathered}
\tag{4.1}
\]

Here addition denotes union of disjoint bit masks.  Inside the root-`K`
component, the neutral move replaces the two profiles

\[
 Q\cup\bigl((c+Q)\setminus\{K+c\}\bigr),\qquad d+Q
\tag{4.2}
\]

by

\[
 (c+Q)\setminus\{K+c\},\qquad Q\cup(d+Q).
\tag{4.3}
\]

Thus it transfers the whole square `Q` between two cells without changing
the component matching rank `160`.

At the second braid, the three coarse profiles

\[
 Q,\qquad(c+Q)\setminus\{K+c\},\qquad e+Q
\tag{4.4}
\]

are replaced by

\[
\begin{gathered}
 \{K,K+a\},\qquad \{K+a+c\},\qquad
 \{K+b,K+a+b\},\\
 \{K+b+c,K+a+b+c\},\qquad
 \{K+b+e,K+a+b+e\}.
\end{gathered}
\tag{4.5}
\]

The square `Q` has been split into its two parallel `a`-edges; the
three-corner `c` layer has been split into a singleton and an edge; and the
`e` layer retains its upper edge.  The component-restricted number of right
cells rises from `160` to `162`, while its matching rank rises

\[
                         160\longrightarrow161.
\tag{4.6}
\]

The corresponding physical old starts are

\[
 (1,212),\quad(2,211),\quad(2,212),
\]

and the new starts are

\[
 (0,3579),\quad(1,3578),\quad(1,3579),
 (2,3578),\quad(2,3579),
\]

where a pair is `(depth,start)`.  A common old lower-edge cell on
`{K,K+a}` remains at `(0,6261)`.  The fission therefore creates the second
independently usable lower edge which the exposed-root theorem requires.

The old canonical DM component has `161` targets and `160` cells, target-rank
histogram

\[
                         (1,9,43,108)
\tag{4.7}
\]

at ranks `4,5,6,7`, and target digest

```text
fd3a77b6401ff1d4b5ec46f606470fd6ac574402ae6df2c9bbb32293cd81ff1d
```

After (4.5), all `161` targets are matched.  No target enters a replacement
deficient component.  This proves that the whole root-`20516` component,
not merely one chosen canonical shore, has been discharged.

## 5. Exact Hall-23 component atlas

The Hall-24 base and its neutral portal have the same canonical deficient
DM shore:

\[
 (|S|,|N(S)|)=(1168,1144),\qquad
 (|S_4|,|S_5|,|S_6|,|S_7|)=(7,63,317,781).
\tag{5.1}
\]

Its target digest is

```text
19ebb6f7d2e7f4f1d9f2ea49d2d4934d074927efa74c877558bf5b5708adccb8
```

The Hall-23 shore is exactly (5.1) with the root-`20516` component removed:

\[
 (|S|,|N(S)|)=(1007,984),\qquad
 (|S_4|,|S_5|,|S_6|,|S_7|)=(6,54,274,673),
\tag{5.2}
\]

with target digest

```text
88895c0ced520217a65802ba03060bf7ff2ed3aec192c90c6e666585f76b5c89
```

Every connected component in (5.2) has excess exactly one.  Its complete
size/core atlas is

\[
\begin{array}{c|c|l}
|X|&|Y|&\text{intersection core(s) of the target masks}\\ \hline
169&168&1920\\
161&160&960,8217,24610\\
160&159&449,8218\\
5&4&4213,7504\\
3&2&1103,18970\\
2&1&2420,2676,4877,9524,17683,19568\\
1&0&2575,5801,13616,13620,17738,21641,29776.
\end{array}
\tag{5.3}
\]

There are therefore exactly 23 deficient components.  For each component,
an exact maximum matching was fixed and the alternating-reachability test of
Proposition 2.2 reached every left vertex.  Hence

\[
                         \boxed{\rho(D)=X}
\tag{5.4}
\]

for every component `D` in (5.3).

Equation (5.4) is the useful Hall-23 simplification: any genuinely additional
cell which touches a component can be used as its root cell.  A physical
trade must still retain or reroute the complement matching; mere support
intersection is not enough.

## 6. The sharp conditional Hall-22 certificate

Consider the remaining `161/160` component with core

\[
                         K=24610.
\]

Its target digest is

```text
dbef9976cb3e26dcfbbfffda56904b44e820c3d0681a0ba4751b731041252dc9
```

Let

\[
                         a=512=2^9,\qquad b=64=2^6,
\tag{6.1}
\]

corresponding to coordinate labels `10` and `7`.  The Hall-23 carrier has
the physical cells

\[
 E_0=(\text{depth }0,\text{ start }4704),\qquad
 \Gamma(E_0)=\{24610,25122\}=K+\mathcal P(\{a\}),
\tag{6.2}
\]

and

\[
 E_1=(\text{depth }1,\text{ start }4655),\qquad
 \Gamma(E_1)=\{24610,24674,25122,25186\}
             =K+\mathcal P(\{a,b\}).
\tag{6.3}
\]

There is an exact rank-`160` matching of this component which leaves `K`
unmatched and uses

\[
                         E_0\mapsto K+a=25122,
 \qquad E_1\mapsto K+a+b=25186.
\tag{6.4}
\]

### Corollary 6.1 (literal matching target for the next braid)

Suppose a carrier-safe trade at Hall 23

1. retains every other edge of the matching in (6.4) and the complement
   matching;
2. retains `K+a+b` through a child cell containing the upper edge
   `\{K+b,K+a+b\}=\{24674,25186\}`; and
3. supplies a second cell containing the lower edge
   `\{K,K+a\}=\{24610,25122\}`.

Then the new lower-edge cell may be matched to `K`, the old anchor remains
matched to `K+a`, and the upper child is matched to `K+a+b`.  All other old
matching edges remain.  Consequently

\[
                         h:23\longrightarrow22.
\tag{6.5}
\]

This is a complete compiler-matching certificate, not a physical braid.
The two existing starts in (6.2)--(6.3) are separated by 49.  This is the
smallest audited edge/diamond start gap among the remaining `161/160`
components; the analogous gaps are 50 at root `960` and 58 at root `8217`.
No endpoint-valid segment reassembly satisfying residence and the full
upper seam ledger has yet been proved to realize (6.5).

## 7. Coupling a zero repair to a component discharge

Each of the seven masks in the last row of (5.3) is an isolated component
`({z},emptyset)`.  By Theorem 2.1, it can be discharged only by creating a
first physical cell adjacent to `z`.

The following bookkeeping theorem states exactly how the two current fronts
can be fused.

### Theorem 7.1 (two-commodity matching fusion)

Let `D_z`, `D_K`, and `C` be pairwise cell-disjoint matching summands of a
bipartite graph, where `D_z=({z},emptyset)` and `D_K` is excess one.  Suppose
a compound physical trade

1. creates a cell adjacent to `z`;
2. perfects `D_K` by Theorem 2.3; and
3. retains all but at most `ell` edges of a fixed maximum matching on `C`,
   after optimal rerouting in `C`.

If the two new component matchings use distinct right cells, then

\[
                  \nu(G')\geq\nu(G)+2-\ell,
 \qquad h(G')\leq h(G)-2+\ell.
\tag{7.1}
\]

#### Proof

Take the new edge at `z`, the perfect matching of `D_K`, and a complement
matching of size at least `nu(C)-ell`.  Their vertex sets are disjoint, so
their union has the displayed size.  Hall deficiency is `|L|-nu`.  \(\square\)

Thus a fused zero/diamond macro with no complement loss would take Hall 23
directly to at most Hall 21 while reducing the zero count to six.  Even one
unavoidable complement loss still gives Hall 22 and zero count six.  This is
the precise target suggested by the separate Pareto branch

\[
                 (25,7)\longrightarrow(26,6)\longrightarrow(25,6),
\]

which creates a first cell for `2575`.  That branch and the Hall-23 branch
are different physical carriers; Theorem 7.1 does not assert that their
braids commute or can be superposed.

## 8. Carrier interface and sharp remaining obstruction

For Corollary 6.1 or Theorem 7.1 to become an exact finite construction, the
same compound reassembly must satisfy all of the following in one physical
word:

1. exact rank-eight middle ownership and Johnson adjacency;
2. depth-three residence at every old and new seam, including overlapping
   collars;
3. complete upper support at every depth `q=1,...,7`;
4. the required lower support ledger, with “four lower holes” interpreted
   as the immediate layer only;
5. nonempty maximal erosion and the exact relation `D^3 A=T`;
6. retention or explicit rerouting of the full complement matching, or,
   equivalently, the all-shore current inequality (1.5); and
7. after outer Hall reaches zero, simultaneous realization of all selected
   cells by one common controller word.

Connector topology alone is cheap and is not this gate.  The Hall-24
compound already shows that two clean flag `C6` seam circuits can implement
a useful global reassembly.  The unresolved step is to orient such a
compound so that its physical compiler profiles perform the root-`24610`
fission, or simultaneously transport the existing `2575` first-cell repair,
without erasing a last upper witness or a needed matching portal.

The following limits are exact.

* Any iteration preserving the seven zero-degree masks can discharge at
  most the sixteen nonzero components in (5.3), and therefore cannot pass
  Hall deficiency seven.
* Any iteration preserving four immediate-lower holes forever cannot reach
  the necessary finite prefix corridor `h_1<=2`.
* Hall zero is still only the outer target/cell matching theorem; it does not
  by itself choose one common physical word.

Accordingly the next finite object is not another rankwise balancing lemma.
It is either

* a resident, all-upper-safe compound braid realizing the explicit
  root-`24610` lower-edge duplication/upper-edge retention of Section 6; or
* a fused two-commodity braid which transports a first cell for one of the
  seven isolated zero targets and loses at most one unit of complement
  matching while discharging a nonzero component.

## 9. Audited artifacts

The three carrier artifacts are

* `scratch/k15_segment_braid_hall24.json`, SHA-256
  `49eb1060ccbe86f056295f0b96fe409f275737b8b759f5b7ca0ee2fa7ca0416e`;
* `scratch/k15_segment_braid_hall24_portal.json`, SHA-256
  `3bc6aa08d3df1b45709cef7e66ccc8bd9f9384a2b247c624252d81a637a032d4`;
* `scratch/k15_segment_braid_hall23.json`, SHA-256
  `8feab1da65f3924d29609246798fc543dc50d076ca9db363e8796dda2c22598d`.

Their comma-separated middle-path digests are respectively

```text
96e7640ebcf8e4c3e372e0e4654b7a7c3934ed5d38be2d13c1371a04eabc49f5
3603210ae65b0a390269d154cd13cc5406745dc8a2231715c8aec36e76feec2f
09b779278edaff5d00d4ef119a1ae6d15df8858557a3c700d9cac4764ef9c66b
```

The independent reconstruction audit gives changed contracted profile-bank
sizes `13` and `25`, contracted ranks

\[
                         8\to8,\qquad19\to20,
\]

and global deficiencies `24,24,23`.  At the time of this three-state audit,
a cross-shore value `22` after the final braid was only the gap of the former
Hall-24 shore; another shore still had gap `23`.  The later Hall-22 carrier
uses the separate neutral-router/remote-splitter pair cited at the start of
this note.
