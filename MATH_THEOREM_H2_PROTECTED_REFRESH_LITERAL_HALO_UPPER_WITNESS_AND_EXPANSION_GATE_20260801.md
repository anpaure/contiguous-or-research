# Literal halo and upper-witness interface for the protected rolling refresh

Date: 2026-08-01  
Status: exact source-interface reduction, exact protected-expansion cuts,
conditional nested-rail theorem, and sharp common-cap obstruction.  The
refreshed plus phase is fixed throughout; no old/new row inversion is
required or claimed.

## 0. Verdict

Let the split-core packet have depth `h`, source positions `0,...,4h`, and
let `t>=b+1` deadline jumps have occurred from disjoint base depth `b`, so
`h=b+t`.  Service every due pair with a distinct fresh label and protect the
current two paths

\[
 P_t^-:L_0-\cdots-L_t,
 \qquad
 P_t^+:R_{b-1}-\cdots-R_{h-1}.                       \tag{0.1}
\]

The exact answer has four parts.

1. The minimum fixed-address source support of (0.1) is two literal halos
   of total size `O(h)`.  Adding the pivot cell `[X]`, active `K2` cells,
   and selected singleton aliases remains `O(h)`.  Protecting every pivot
   ray makes the whole `4h+1`-letter packet the natural literal block.
2. The anonymous owner-slot forest may retain that block and `O(h)` further
   diamond-halo atoms.  This removes only `o(1)` of every raw tight-
   augmenter menu.  Exact upper-leave cover-down is still the common
   Aharoni--Haxell footprint cut plus the contracted graphic cuts, evaluated
   after one fixed protected bank and one fixed source/cap state.
3. Linear source support does **not** mean a linear witness ledger.  The two
   literal halos contain `Theta(h^2)` arbitrary-upper interval addresses,
   and refreshing two source positions changes `Theta(h^2)` old interval
   addresses.  Old and new phases must be alternatives.  The lost old
   target IDs require a new occurrence matching or a structured rail.
4. A nested Ferrers rail with identical complete prefix/suffix OR signatures
   is a valid `O(h)` realization of a quadratic union grid.  This is only a
   conditional theorem: the refreshed bank and the anonymous DP forest do
   not imply interval-convex occurrence neighborhoods or a common cap.  A
   two-position positive-cover core is the sharp first obstruction.

Thus the protected refresh adds only `O(h)` **forest resources**, but the
remaining compiler gate is targetwise and source-aware.

## 1. Minimum literal support halos

The owner at start `s` is the OR of source positions `[s,s+h]`.  Therefore
the union of the defining source intervals for the left path in (0.1) is

\[
                         J^-=[0,h+t],                 \tag{1.1}
\]

and for the right path is

\[
                         J^+=[3h-t,4h].               \tag{1.2}
\]

Both have length `h+t+1`.  They are disjoint because `t<h`.  They are the
smallest fixed-address position sets containing every defining owner window
of (0.1).

For a particular serviced birth pair `i`, put `a=t-i+1`.  Its five central
point tickets occur at

\[
\begin{array}{c|c}
\text{ticket}&\text{source position}\\ \hline
z_i^-&a-1\\
\alpha_i&h+a-1\\
X&2h\\
\gamma_i&3h-a+1\\
z_i^+&4h+1-a.
\end{array}                                             \tag{1.3}
\]

The four non-`X` cells lie in (1.1)--(1.2).  The inserted task `[X]` is one
extra point pin.  Active enriched `K2` cells and any separately selected
singleton backups are added by literal occurrence ID.

### Theorem 1.1 (literal-halo interface)

Fix the letters on `J^- union J^+`, the cell `[X]`, the active `K2` cells,
and the chosen singleton occurrences.  Export at every open attachment cut:

1. the ordered last/first `h` source letters;
2. the capped signed run age of every live coordinate;
3. the complete prefix and suffix OR signatures; and
4. the endpoint owner, slot, lower-ticket, and root orientation.

This data is sufficient to test a proposed literal continuation: all owner
windows meeting the cut, every shifted native lower cell, every crossing
upper interval, and every residence flip are determined.  The union of the
boundary letters alone is insufficient, because it loses both source order
and signed age.

More explicitly, let `O` be the current endpoint owner, let `S` be the OR
of the ordered `h` source letters retained after the shift, let `U` be a
proposed next owner, and let `E` be the entering nonempty source letter.
The exact set-valued seam test is

\[
 S\subseteq U,qquad U-S\subseteq E\subseteq U,qquad
 E\cap(O-S)=\varnothing,                              \tag{1.4}
\]

together with `|O triangle U|=2` and the point cap on `E`.  Residence is a
separate exact check against the stored signed ages at every coordinate
whose sign changes.  The next cut state then drops the first ordered
overlap letter and appends `E`.  Formula (1.4) explains why `S` alone is
not a continuation state.

If every pivot ray occurrence is also fixed, their defining source
intervals cover `[h+1,3h-1]`.  Together with (1.1)--(1.2) they cover the
entire packet `[0,4h]`.  Hence the proof-safe full-pivot interface is the
literal `4h+1`-letter block plus one ordered `h`-letter cut state at each
open side.  A terminal placement needs only one open cut.

#### Proof

The owner starts in the two paths are `0,...,t` and
`3h-t,...,3h`.  Taking the union of their length-`h+1` source intervals
gives (1.1)--(1.2).  Formula (1.3) follows from the inherited bank indices.
The cut claims follow by writing every crossing interval as an exterior
suffix, a fixed boundary block, and an interior prefix.  Signed ages are
needed because identical owner sets can have different legal next flips.
The ray intervals end at or start at `2h` and have lengths through `h`, so
their union is `[h+1,3h-1]`.  \(\square\)

## 2. Arbitrary-width upper closure

For every source word `A`, every `q>=0`, and every valid start `s`, one has

\[
 D^{h+q}A_s
   =\bigcup_{j=0}^{q}(D^hA)_{s+j}.                    \tag{2.1}
\]

Thus a fixed literal halo and its ordered owner chronology determine all
of its upper interval values.  They do not guarantee that the resulting
values supply the required global target IDs injectively.

Each halo in (1.1)--(1.2) has length `h+t+1`.  The number of internal
interval addresses of widths `h+2,...,h+t+1` is

\[
             \sum_{w=h+2}^{h+t+1}(h+t+2-w)
                   ={t(t+1)\over2}.                  \tag{2.2}
\]

The two halos therefore expose `t(t+1)=Theta(h^2)` arbitrary-upper
addresses.  These are derived cells, not additional owner-slot tokens.

### Lemma 2.1 (full boundary signature)

Let two equal-length blocks have equal OR for every prefix and every
suffix.  Replacing one by the other preserves the OR of every interval
which crosses either boundary of the block, in every fixed exterior
context.  Conversely, preservation for all crossing intervals in all
exterior contexts (including the empty exterior) forces equality of the
complete prefix and suffix signatures.

Equality of endpoints, length, and total union is not sufficient.  With
the shorthand `12={1,2}`, the blocks

\[
                         (12,13,34),\qquad(12,24,34)  \tag{2.3}
\]

have the same endpoints and total union.  Prefixing by `15`, however,
gives the crossing values `1235` and `1245` on the corresponding partial
interval.

### Lemma 2.2 (nested Ferrers rail)

Let

\[
 L_1\supseteq\cdots\supseteq L_p,qquad
 Q_1\subseteq\cdots\subseteq Q_q.                    \tag{2.4}
\]

The `p+q-1` letters

\[
 L_1Q_1,\ldots,L_pQ_1,L_pQ_2,\ldots,L_pQ_q          \tag{2.5}
\]

realize every union `L_i union Q_j` on the interval from the `i`th left
letter through the `j`th right letter.  Hence a quadratic Ferrers OR family
can have a linear literal source realization.

This lemma is the positive nested-ray route.  It is not a cap theorem: the
letters in (2.5), their attachment seams, and every selected occurrence
must still be legal in one common word.

## 3. Old/new alternatives and exact occurrence repair

Let `A^0` be the canonical word and `A^1` its refreshed plus phase.  For one
serviced pair, the changed positions are

\[
                         p^-=a-1,qquad p^+=4h+1-a.    \tag{3.1}
\]

The number of packet interval addresses containing at least one changed
position is exactly

\[
                         a(8h+4-3a).                  \tag{3.2}
\]

At first expiry `h=2b+1,a=b+1`, this is

\[
                         (b+1)(13b+9).                \tag{3.3}
\]

### Proposition 3.1 (phase separation is forced)

At a refreshed position the new mandatory lower bound contains `z_i`.
Every old interval or guard target through that position omits packet-fresh
`z_i`.  Retaining even one such old row in the same literal source state
forces the maximal cap at that position to omit `z_i`, contradicting its
mandatory lower bound.  Therefore the complete old all-width incidence
halo through (3.1) must be released.  A common cap vector may admit both
phases, but the old and new singleton letters are not one common source
word.

This is not fixed-row inversion.  Choose the refreshed plus word, retain
every old target occurrence whose typed cell is unchanged, and rematch only
the released target IDs.

Formally, let `E` be the typed interval cells whose OR or guard changes.
From an old matching retain every edge outside `E`; let `U` be the released
target IDs and let `D` be genuinely new required tickets.  Delete the
retained/forced cells and form the new occurrence graph `G^1`.  Marginal
repair is equivalent to

\[
             |N_{G^1}(Y)|\ge |Y|
             \qquad(Y\subseteq U\mathbin{\dot\cup}D).          \tag{3.4}
\]

At `b=2`, the first duplicated pair (`h=3`) already loses two width-two
target values and fourteen old values in total.  At the first forced
service (`h=5`) it loses `2,6,18,54` values having an old witness of width
at most `2,3,5,all`, respectively.  The changed-address count is `105`.
These are scoped literal controls, not an all-`h` asymptotic formula.

The singleton layer itself is small.  In the `h=5` control,

\[
 N(X)=\{[10]\},\quad N(\alpha_1)=\{[7]\},\quad
 N(\gamma_1)=\{[13]\},\quad N(z_1)=\{[2],[18]\}.     \tag{3.5}
\]

Choose one ordinary target occurrence for `z_1`; an occurrence-multiset
model may instead use the two cells as distinct clones.  A typed guard
forcing two required `z_1` clones to one cell is the minimal Hall failure.
If an active `alpha/gamma` central cell is enriched, its singleton needs an
external backup ticket.

## 4. Inclusion in the protected alternating-forest cover-down

Let `P` be the current protected bank and add `q_h=O(h)` compatible halo
diamonds.  If the augmented bank `P_*` is still a four-resource matching
with linear-forest projection, put

\[
 p_*=|P_*|,qquad z_*=4p_* .                           \tag{4.1}
\]

For the current two paths, `|P|=2t` and `z(P)=8t`; for the full packet,
`|P|=3h` and `z(P)=12h`.  Thus `p_*=O(h)=O(sqrt(m))`, and the protected
Delcourt--Postle theorem retains `P_*` inside a physical linear forest of
order `U-o(W)`.

For a fixed missing upper colour, the exact tight-augmenter menu and maximum
non-target resource load are

\[
 N_R=16(m+1)m(m-2)(m-1),qquad
 \Lambda_R=8m(m-1)(m-2).                              \tag{4.2}
\]

Deleting the `z_*` permanent typed resources leaves at least

\[
 N_R-z_*\Lambda_R
     =N_R\left(1-{z_*\over2(m+1)}\right).             \tag{4.3}
\]

Hence an `O(h)` halo removes only `O(h/m)=o(1)` of each raw menu and cannot
by itself realize the absolute `2(m+1)`-atom facet-boundary obstruction.

### Theorem 4.1 (exact protected expansion cut)

Fix one incumbent owner-slot forest `M` containing `P_*` and one literal
occurrence/cap state `Q`.  For each missing upper `R`, let
`mathscr T_R^{P_*,Q}(T)` be the clean expansion trees of at most `T` nodes
whose auxiliaries, blockers, and increment triples avoid `P_*` and are
literal-compatible with `Q`.  Their compressed footprint has rank at most

\[
                         B=5T-1.                       \tag{4.4}
\]

There are disjoint clean witnesses for every missing upper if, for every
nonempty `I` in the missing shore,

\[
 \boxed{
 \nu\!\left(\bigcup_{R\in I}
       \{\Xi(\mathcal T):\mathcal T\in
          \mathscr T_R^{P_*,Q}(T)\}\right)
       >(10T-5)(|I|-1).}                               \tag{4.5}
\]

The fixed protected/halo tokens are deleted globally; they must not be
copied into every witness footprint.  If a witness carries `q` additional
variable source tokens, replace `B` by `5T-1+q` and the coefficient by
`10T+2q-5`.

After deleting the selected auxiliary and blocker edges, let `G_0` be the
retained physical forest and contract its components.  If `E^+` is the set
of all projected on-edges, exact forest preservation is

\[
                         |E^+[X]|\le |X|-1             \tag{4.6}
\]

for every nonempty set `X` of contracted components.  This includes the
no-loop row and is necessary and sufficient for graphic independence.
The footprint cut (4.5) does not imply (4.6).

## 5. One-source common-cap condition

Fix the refreshed phase.  Let `F` be its frozen source positions, `V` the
free halo/exterior positions, `C_p` the point caps, and `D_p` mandatory
subsets.  Include in the hard-row family every protected owner/q1 row,
selected upper witness, terminal row, and mixed exterior guard.  For a
selected occurrence matching `M`, define at a free position

\[
 K_p(M)=C_p
   \cap\!\bigcap_{R:p\in I_R}S_R
   \cap\!\bigcap_{(T,c)\in M:p\in I_c}T.             \tag{5.1}
\]

At a frozen position use its fixed letter.  One common nonzero source word
exists exactly when

\[
 D_p\subseteq K_p(M)\ne\varnothing                    \tag{5.2}
\]

at every free position, every fixed letter obeys the analogous cap and row
intersections, and every hard or selected row reconstructs:

\[
                 B_R\cup\bigcup_{p\in I_R}K_p(M)=S_R. \tag{5.3}
\]

Equations (3.4), (4.5), (4.6), and (5.2)--(5.3) must hold for **one common
`Q`**.  Taking a union of occurrence or expansion edges legal under
different cap states is invalid.  This is the exact combined all-cut/
common-cap interface.

### Corollary 5.1 (conditional convex/laminar closure)

Suppose one fixed source state passes (5.2)--(5.3), every residual target
neighborhood is an interval in a common order of cells, and the protected
prefix/suffix rows use the full signatures of Lemma 2.1.  Then occurrence
Hall is equivalent to the interval cuts

\[
 \bigl|\{T:N(T)\subseteq[r,s]\}\bigr|\le s-r+1       \tag{5.4}
\]

for every cell interval `[r,s]`; earliest-deadline matching gives a
zero-defect occurrence assignment.  If its expansion catalog also passes
(4.5)--(4.6), the protected refresh survives exact upper cover-down at the
anonymous forest level and all declared literal witnesses survive in the
same source.

This is the desired positive nested-ray theorem.  Its trace-convex and
one-`Q` hypotheses are load-bearing and are not consequences of the DP
forest.

### Proposition 5.2 (sharp two-position common-cap obstruction)

Take two free positions with caps `{z,a}` and `{z,b}`.  Require their union
to realize `{z,a,b}`, and select singleton rows `{a}` and `{b}` at the two
positions.  The occurrence matching is perfect and its neighborhoods are
convex, but the maximal letters are `{a}` and `{b}`; the protected union
loses `z`.  Therefore ordinary Hall, even on a two-position convex graph,
does not imply (5.3).  This is the first collective positive-cover core
after singleton cap/mandatory failures have been prefiltered.

## 6. Exact remaining gate

The current refresh can be included in the clean alternating-forest start
with only `O(h)` protected resources.  What remains is to construct, for the
actual leave, one state satisfying simultaneously:

1. the targetwise occurrence Hall cuts (3.4);
2. the clean-expansion packing cuts (4.5);
3. the contracted graphic cuts (4.6); and
4. the maximal common-word equations (5.2)--(5.3).

The nested Ferrers rail is a valid linear-size candidate host for the
quadratic witness family, but no theorem yet makes its point caps, seams,
and expansion footprints compatible with the actual Pascal child.

## 7. Independent replay

The dependency-free audit

```text
scratch/audit_h2_protected_refresh_literal_halo_20260801.py
```

checks the literal halo indices, point occurrences, arbitrary-width union
identity, quadratic address counts, first-expiry casualty census, Ferrers
rail, prefix-signature counterexample, protected-menu arithmetic, and the
two-position common-cap obstruction.  Its fail-closed output is

```text
scratch/h2_protected_refresh_literal_halo_20260801.audit.json
```
