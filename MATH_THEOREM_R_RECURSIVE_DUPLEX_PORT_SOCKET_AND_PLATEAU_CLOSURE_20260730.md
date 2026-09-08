# Recursive duplex port sockets and the exact plateau-closure boundary

Date: 2026-07-30  
Lane: R  
Status: proved local recursive port family; exact global completion criterion;
no unconditional all-`k` word.

## 0. Result

The authenticated `11->12` and `13->14` terminal PBPs contain a common
nonempty typed port which was not exported in their original compiler files.
In each case it consists of one occurrence-labelled depth-two lower provider,
one protected five-state middle collar, an exact order-one facet chart, and
one literal upper-`q=1` socket.  Thus each terminal certificate can be equipped
with a cardinality-one protected output port; the earlier statement that no
nonempty port had been *proved* is strengthened by the explicit extraction
below.

The local port is genuinely recursive, but not under repeated facets of one
type.  A facet consumes one unit of both lower transparency and upper
pair-thickness.  The smallest same-type counterexample already occurs on

```text
24,23,13,12 in J(4,2).
```

The correct invariant has two types.  A guarded connector is sent by the
tagged facet to its complete three-state bridge socket; the natural union mate
then returns the connector, all insertion traces, every departure key, and
every protected literal provider, up to a common fresh tag.  Algebraically,

\[
 \boxed{\nabla\partial_z T=z+T.}                    \tag{0.1}
\]

This gives an explicit infinite family of **duplex sector sockets**.  It also
separates the remaining global theorem sharply: a full plateau child must
embed one such socket while satisfying exact middle ownership, the natural
join of all source fibres, one same-source casualty Hall condition, and the
complete upper bridge/seam catalogue.  Those global conditions are not proved
by the finite `k=12,14` certificates, so no all-`k` word is claimed.

## 1. Typed local sockets

Let a source `Q=(Q_p)` realize a fixed-horizon rank-`r` middle chronology
`T=(T_i)` at depth `D`:

\[
 \varnothing\ne Q_p,\qquad
 T_i=\bigcup_{p=i}^{i+D}Q_p.                        \tag{1.1}
\]

A **guarded one-provider socket of depth `D`** consists of:

1. an occurrence-labelled source interval `C` with target
   `X=union_(p in C)Q_p`, where `|X|<r`;
2. the owner and source collars needed for the declared next Pascal facet;
3. every facet-transparency identity and fixed-tag hit on that occurrence;
4. an occurrence-labelled upper interval together with the complete base
   collar needed to transport it;
5. the local restriction of the common-source fibre; and
6. a declaration that every nonexported lower or upper occurrence is a
   next-stage casualty.

The port is **cardinality one** when its protected matching has the single
edge `X -> C`.  This is the smallest possible nonempty protected matching.
It is not by itself a full PBP: exact middle ownership outside the collar,
global lower Hall, and all unexported upper targets remain global obligations.

## 2. The protected diamond lemma

### Theorem 2.1 (literal phase-balanced diamond)

Assume `D=2`.  Fix three consecutive owners `T_i,T_(i+1),T_(i+2)` in a
protected locally geodesic Johnson collar, and source letters
`Q_(i+1),Q_(i+2),Q_(i+3)`.  Require the complete parent and declared future
dependency collar to be protected and to survive every cut.  Assume also

\[
                 |Q_{i+2}|=r-2,                    \tag{2.1}
\]

and

\[
\begin{aligned}
 T_i\cap T_{i+1}&=Q_{i+1}\cup Q_{i+2},\\
 T_{i+1}\cap T_{i+2}&=Q_{i+2}\cup Q_{i+3},\\
 T_i\cap T_{i+1}\cap T_{i+2}&=Q_{i+2},             \tag{2.2}\\
 (T_i\cap T_{i+1})\cup(T_{i+1}\cap T_{i+2})
   &=T_{i+1}.
\end{aligned}
\]

Let `z` be a fresh coordinate and define the three child source letters

\[
 R_i=Q_{i+1},\qquad
 R_{i+1}=\{z\}\cup Q_{i+2},\qquad
 R_{i+2}=Q_{i+3}.                                  \tag{2.3}
\]

At child horizon one they realize the two rank-`r` owners

\[
\begin{aligned}
 P_i&=R_i\cup R_{i+1}
     =\{z\}\cup(T_i\cap T_{i+1}),\\
 P_{i+1}&=R_{i+1}\cup R_{i+2}
     =\{z\}\cup(T_{i+1}\cap T_{i+2}).             \tag{2.4}
\end{aligned}
\]

Moreover,

\[
 \boxed{P_i\cap P_{i+1}=R_{i+1}=\{z\}\cup Q_{i+2}} \tag{2.5}
\]

is a literal protected lower provider, and

\[
 \boxed{P_i\cup P_{i+1}=\{z\}\cup T_{i+1}}        \tag{2.6}
\]

is a literal upper-`q=1` socket.  If the parent protected depth and child
deadline are both two, and this facet is placed after one net phase wall,
then its phase inequality is exact:

\[
 f+(D-d)=1+(2-2)=1=a.                               \tag{2.7}
\]

Under the protected-collar hypotheses, (2.3)--(2.8), the singleton local
fibre `{R}`, and the matching edge

\[
  \{z\}\cup Q_{i+2}\longmapsto[i+1,i+1]            \tag{2.8}
\]

form a one-step cardinality-one port.

#### Proof

Equations (2.4) are (2.2) with the tag placed in the unique source letter
common to both child owner windows.  Intersecting the two equalities in
(2.4) and using the third equality in (2.2) gives (2.5).  Taking their union
and using the last equality in (2.2) gives (2.6).  The rank hypotheses make
the two `P` states Johnson-adjacent rank-`r` states and make (2.5) a strict
rank-`r-1` lower target.  The cell in (2.8) is
literal and exact under the same source `R`; with one target and one cell it
is a matching.  Equation (2.7) is the sharp phase-credit identity.  \(\square\)

The last line of (2.2) is the local **pair-thickness** condition: every
coordinate of the middle state `T_(i+1)` occurs on at least one of its two
incident edges.  In a Johnson collar it fails exactly when a coordinate
enters and immediately leaves at the middle state.

## 3. Exact sockets in the two authenticated certificates

All indices below are zero-based source/middle indices.  Decimal certificate
entries are written in hexadecimal.

### Theorem 3.1 (`k=12` port)

In `scratch/k12_intersection_sixpiece_hallpass_001.word`, take `i=13`.  The
protected middle collar and source collar are

```text
T_12,...,T_16 = 0617,0437,00b7,01a7,01e5,
Q_13,...,Q_17 = 0416,0017,0027,00a5,01a1.
```

The four Johnson events, written departure/arrival, are

```text
0200/0020, 0400/0080, 0010/0100, 0002/0040.
```

They are support-separated.  The exact diamond is

\[
\begin{aligned}
 0437\cap00b7&=0037=0017\cup0027,\\
 00b7\cap01a7&=00a7=0027\cup00a5,\\
 0437\cap00b7\cap01a7&=0027,\\
 0037\cup00a7&=00b7.                               \tag{3.1}
\end{aligned}
\]

Thus the current protected edge is

\[
 0027\longmapsto[15,15],\qquad Q_{15}=0027.         \tag{3.2}
\]

For any fresh tag `z`, its next facet chart is

```text
source: 0017, z+0027, 00a5,
owners: z+0037, z+00a7,
lower:  z+0027,
upper:  z+00b7.
```

The two exterior owner guards in (3.1) give the complete order-one/upper-q1
dependency collar.  The authenticated global word itself is a member of the
current singleton port fibre.

### Theorem 3.2 (`k=14` port)

In `scratch/k14_intersection_sixpiece_hallpass_004a.word`, take `i=11`.  The
corresponding collars are

```text
T_10,...,T_14 = 047b,04fa,14da,14ce,12ce,
Q_11,...,Q_15 = 043a,005a,04ca,10ca,104e.
```

Their Johnson events are

```text
0001/0080, 0020/1000, 0010/0004, 0400/0200.
```

Again they are support-separated, and

\[
\begin{aligned}
 04fa\cap14da&=04da=005a\cup04ca,\\
 14da\cap14ce&=14ca=04ca\cup10ca,\\
 04fa\cap14da\cap14ce&=04ca,\\
 04da\cup14ca&=14da.                               \tag{3.3}
\end{aligned}
\]

Hence

\[
 04ca\longmapsto[13,13],\qquad Q_{13}=04ca,         \tag{3.4}
\]

and the next tagged chart is

```text
source: 005a, z+04ca, 10ca,
owners: z+04da, z+14ca,
lower:  z+04ca,
upper:  z+14da.
```

The two finite constructions therefore share the same typed diamond, not
merely the same rank counts.  Because every nonempty protected matching has
at least one edge, (3.2) and (3.4) are cardinality-minimal.

The frozen inputs used here are

```text
f57f775c55c9ae156aeb124fa0016dd835c0efd1c472897e93bc6ea5abfc45d6
  scratch/k12_intersection_sixpiece_hallpass_001.json
a29517e67dd3c9db5f773f5332b3e3e44197cfe79d3d8014ea0770c9bedeb482
  scratch/k12_intersection_sixpiece_hallpass_001.word
d67bb4176b49c0b7be4d0ac6f232cf59e4b0247999dbb5b1f06aeb50c62bbc7d
  scratch/k14_intersection_sixpiece_hallpass_004a.json
7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17
  scratch/k14_intersection_sixpiece_hallpass_004a.word.
```

### Scope of the extraction

The extraction upgrades each frozen terminal certificate to a **declared
one-step local port**.  It does not assert that the next full child exists.
In particular, it does not provide:

- a next-rank exact middle deck;
- a global child source extending the displayed local chart;
- a matching for all other lower targets;
- compatibility with arbitrary future cuts or bridges; or
- a same-type output port after an unpaired second facet.

Those are separate quantified conditions in Section 7.

## 4. Why a pure facet is not a recursive type

### Theorem 4.1 (upper pair-thickness criterion)

Let

\[
 Y=\bigcup_{j=a}^{b}T_j,\qquad
 F_i=\{z\}\cup(T_i\cap T_{i+1}).                   \tag{4.1}
\]

Then the natural facet interval satisfies

\[
 \bigcup_{i=a-1}^{b}F_i=\{z\}\cup Y               \tag{4.2}
\]

if and only if every `y in Y` occurs in at least one adjacent parent pair
`T_i,T_(i+1)` with `a-1<=i<=b`.  For order `A`, replace adjacent pairs by
consecutive `(A+1)`-blocks and let their starts range from `a-A` through
`b`.

#### Proof

Every old-coordinate intersection on the left of (4.2) is contained in one
of `T_a,...,T_b`, so the left side has no old coordinate outside `Y`.  A
coordinate `y in Y` occurs on the left exactly when one of the displayed
adjacent pairs contains it.  The order-`A` statement is identical with
`A+1`-fold intersections.  \(\square\)

Define the **facet-survival height** of an occurrence to be the largest `A`
for which the order-`A` criterion holds with its required guards.  Pascal
associativity immediately gives:

### Corollary 4.2 (height depletion)

If `h>=1`, every transformed guard is retained, and no new cut or endpoint
truncation meets the occurrence, then one order-one facet lowers
facet-survival height by exactly one.  Likewise, if a source presentation is
transparent through order `h`, has aligned starts, and every
descendant-selected restriction has the required hereditary fixed-tag hit,
then its order-one inherited presentation is transparent through order
`h-1`: child order-`b` core transparency is parent order-`b+1`
transparency, while the separate tag-hit hypothesis supplies the literal
fixed coordinate.

Consequently no finite-buffer, same-type port can be invariant under
indefinitely repeated pure facets.  Phase credit changes the admissible
horizon; it does not regenerate pair-thickness or source transparency.

### Proposition 4.3 (small literal same-type counterexample)

In `J(4,2)` take the guarded path

```text
24,23,13,12.
```

The two-state parent upper occurrence `23,13` has target `123`, with `24`
and `12` as its two exterior guards.  With fresh tag `z`, the three natural
facet states are

```text
z2,z3,z1.
```

Their union is `z123`, so the old upper target transports.  But their two
consecutive upper colours are only `z23,z13`; there is no child wedge of the
same type.  A second tagged facet with fresh tag `w` gives the identical
states `wz,wz`, loses every old coordinate, and is not a Johnson path.  Thus
successful one-step upper replay
does not imply same-type port closure.  \(\square\)

## 5. The recursive duplex class

The obstruction in Section 4 is removed by retaining the natural union mate.

### Theorem 5.1 (facet/union renewal)

Let `T` be a rank-`r` cyclic Johnson chronology, or a rank-`r` linear
chronology with both literal exterior completion states retained.  Put

\[
 F_i=\{z\}\cup(T_{i-1}\cap T_i).                   \tag{5.1}
\]

Assume no coordinate has a singleton positive run on the displayed collar.
Then every `F_i` is rank `r`, consecutive `F` states are strict Johnson
neighbours, and

\[
 \boxed{F_i\cup F_{i+1}=\{z\}\cup T_i.}            \tag{5.2}
\]

Thus the natural union return

\[
 G_i:=F_i\cup F_{i+1}                              \tag{5.3}
\]

is a rank-`r+1` common-core suspension `G_i={z} union T_i`.  It has the same
Johnson directions, run lengths on every old coordinate, insertion traces,
wedge geometry, and departure keys as `T`; `z` is constant.

For every lower or upper flag occurrence,

\[
\begin{aligned}
 \bigcap_{j=0}^{q}G_{i+j}
   &=\{z\}\cup\bigcap_{j=0}^{q}T_{i+j},\\
 \bigcup_{j=0}^{q}G_{i+j}
   &=\{z\}\cup\bigcup_{j=0}^{q}T_{i+j}.            \tag{5.4}
\end{aligned}
\]

If `Q` realizes `T` at horizon `D>=1`, then

\[
 Q^{z}_p=\{z\}\cup Q_p                             \tag{5.5}
\]

realizes `G` at the same horizon.  Every selected exact interval edge

\[
 X\longmapsto C
\]

is transported occurrence-wise to

\[
 \{z\}\cup X\longmapsto C.                         \tag{5.6}
\]

Distinct target labels and distinct physical interval occurrences remain
distinct.  A nonempty source fibre is carried injectively to a nonempty
source fibre by (5.5).

If the parent presentation is order-`a` facet-transparent on a selected
restriction and that restriction has every hereditary fixed-tag hit, then
the suspended presentation is transparent on the same restriction, since

\[
 \bigcap_{u=0}^{a}G_{i+u}
 =\{z\}\cup\bigcap_{u=0}^{a}T_{i+u},
 \qquad
 \bigcup_{p=i+a}^{i+D}Q^z_p
 =\{z\}\cup\bigcup_{p=i+a}^{i+D}Q_p.               \tag{5.7}
\]

Every selected interval hits `z` automatically.  If order-one transparency
holds at every `i` in the whole declared bridge block, the same source
realizes every facet row there at local horizon `D-1`:

\[
 \bigcup_{p=i}^{i+D-1}Q^z_p
 =\{z\}\cup(T_{i-1}\cap T_i)=F_i,                 \tag{5.8}
\]

where the last equality is the parent order-one transparency identity.
Thus, when `D=d`, this row has the exact plateau phase credit `f=1`.

#### Proof

At `T_i`, the left intersection in (5.1) omits the coordinate which entered
on the left edge, while the right intersection omits the coordinate which
leaves on the right edge.  These coordinates are distinct exactly when no
coordinate has a singleton positive run.  Their union is then all of `T_i`,
which proves (5.2).  Each old intersection in (5.1) has rank `r-1`, so each
`F_i` has rank `r`.  The distinct entering/leaving coordinates show that
`F_i,F_(i+1)` exchange exactly one old coordinate; hence they are strict
Johnson neighbours.  Their union has rank `r+1`, proving the asserted type
of `G`.  Equations (5.4) follow by distributing the common fresh
tag across intersections and unions.  Finally,

\[
 \bigcup_{p=i}^{i+D}Q^z_p
 =\{z\}\cup\bigcup_{p=i}^{i+D}Q_p
 =\{z\}\cup T_i=G_i,                               \tag{5.9}
\]

and the same calculation on every selected physical interval proves (5.6).
The two equalities in (5.7) are the parent transparency equality with the
same common tag adjoined; (5.8) is its order-one case with shifted indices.
\(\square\)

At the facet stage an upper occurrence of parent depth `q` becomes a tagged
occurrence of depth `q+1`; at the union return it becomes depth `q` again.
Likewise a protected lower occurrence of parent depth `s>=2` has depth
`s-1` at the facet stage and depth `s` after return.  Thus the exact signatures
are

\[
 q\longmapsto q+1\longmapsto q,
 \qquad
 s\longmapsto s-1\longmapsto s.                    \tag{5.10}
\]

For a reciprocal-key connector

\[
 a,u_1\mid u_2,b,
\]

the facet image is the complete bridge triad

\[
\begin{aligned}
 L&=\{z\}\cup(a\cap u_1),\\
 B&=\{z\}\cup(u_1\cap u_2),\\
 R&=\{z\}\cup(u_2\cap b).                          \tag{5.11}
\end{aligned}
\]

The bridge `B` need not itself contain either exchanged key, so it is not in
general another reciprocal-key port.  The keys occur in `L` and `R` under
the protected residence hypotheses.  The natural return satisfies

\[
 L\cup B=\{z\}\cup u_1,
 \qquad
 B\cup R=\{z\}\cup u_2,                            \tag{5.12}
\]

and restores the original keyed connector up to the common tag.  Hence the
smallest closed upper object is two-typed:

\[
 \boxed{
 \text{guarded connector}
 \xrightarrow{\partial_z}
 \text{guarded bridge triad}
 \xrightarrow{\nabla}
 \text{guarded connector}.}                         \tag{5.13}
\]

For a keyed-ear `b=3` port, the whole two-seam block and both exterior guards
must be transformed jointly.  Overlapping bridge collars cannot be exported
as independent endpoint records.

### Definition 5.2 (duplex sector socket)

A duplex sector socket of horizon `D>=1` is an explicit tuple

\[
 \mathsf S=(T,\rho,\phi,\mathcal F,\mathcal M,
             \mathcal U,\partial;D)                 \tag{5.14}
\]

with the following properties.

1. `T` is a cyclic Johnson chronology, or a linear chronology with the two
   literal exterior completion states named in `partial`; it has no singleton
   positive run on every declared collar.  The maps `rho,phi` record the
   actual horizon and phase loss of every typed row.
2. `mathcal F` is a nonempty fibre of sources satisfying (1.1).  Every member
   is order-one facet-transparent at every owner start in the complete
   declared bridge block, and satisfies every hereditary tag hit on every
   descendant-selected restriction.  Every protected edge in `mathcal M` is
   exact under every member of the fibre.
3. `mathcal M` is an occurrence-labelled protected matching and `mathcal U`
   an occurrence-labelled protected upper atlas.  Every selected occurrence
   has its complete next-facet collar, and every lower target selected in
   `mathcal M` has parent depth at least two, so it remains strict at the
   intermediate facet stage.
4. `partial` contains the endpoint completions, canonical bridge states, and
   source collars needed by the declared facet and natural union return.
5. For a fresh tag `z`, apply pointwise to every `Q in mathcal F` the
   canonical bridge-source map `Q^z_p={z} union Q_p`.  It realizes `F` at
   horizon `D-1` by (5.8), while the same source realizes the returned
   connector `G` at horizon `D` by (5.9).  The output fibre is exactly

   \[
      \mathcal F^z=\{Q^z:Q\in\mathcal F\}.          \tag{5.15}
   \]

   The facet rows have `rho=D-1,phi=1`, the returned connector rows have
   `rho=D,phi=0`, and their order-one phase credit is exactly
   `1+(D-D)=1`.  The matching, upper atlas, and boundary records are
   transported by adjoining `z` to every label.

The sparse three-letter facet source in Theorem 2.1 is a
cardinality-minimal local realization.  Clause 5 instead uses the all-tag
canonical source; both are exact, but only the latter is the declared source
map of the general duplex type.

The two permitted typed transitions are:

- **suspension:** use the explicit facet source and complete bridge image in
  clause 5, then take the natural union return;
- **copy:** embed the returned socket while avoiding the next fresh
  coordinate.

The interface alternates between connector type and guarded-bridge type as
in (5.13).  A bare linear fragment without the completion records in
`partial` loses one endpoint under the facet/union pair and is not a duplex
socket.

### Corollary 5.3 (explicit infinite sector induction)

Let `S_0` be a rank-`r` duplex sector socket on a ground `Omega_0` of size
`2r`.  For pairwise disjoint fresh coordinates
`z_1,y_1,z_2,y_2,...`, define

\[
 \Omega_n=\Omega_0\cup\{z_1,\ldots,z_n\}
                     \cup\{y_1,\ldots,y_n\},
 \qquad
 Z_n=\{z_1,\ldots,z_n\},\qquad
 T_i^{(n)}=Z_n\cup T_i^{(0)},\qquad
 \mathcal F_n=
 \left\{Q^{(n)}:Q_p^{(n)}=Z_n\cup Q_p^{(0)}
       \text{ for some }Q^{(0)}\in\mathcal F_0\right\}.       \tag{5.16}
\]

Transport every protected lower and upper occurrence by adjoining `Z_n` to
its label and retaining its physical occurrence.  Then `S_n` is a duplex
sector socket for every `n`.  The even-to-odd step is the facet/union renewal
with tag `z_(n+1)`; the following odd-to-even step is the copy operation,
avoiding `y_(n+1)`.  Thus one duplex round raises the ground size by two and
the middle rank by one: `T^(n)` is rank `r+n` on `2(r+n)` coordinates, while
the intermediate `F/G` pair occupies the two middle levels on
`2(r+n)+1` coordinates.  All protected depth differences,
source correlations, occurrence injectivity, Johnson directions, residence,
and boundary traces are invariant.

#### Proof

Apply Theorem 5.1 inductively.  Adding a common tag raises every middle,
lower, and upper rank by one, so depth differences do not change.  The copy
operation changes no set label or trace.  Equations (5.5) and (5.15)
transport the source fibre and matching pointwise at every stage.  \(\square\)

This is an actual recursive family, not a sequence of independently solved
terminal compilers.  It is a **sector** family: it does not assert that its
owners exhaust the whole middle deck at the larger rank.

## 6. What is and is not closed

Theorems 3.1--3.2 and 5.1 give the following exact upgrade.

### Corollary 6.1 (finite certificates have a renewable local germ)

Each authenticated depth-drop terminal PBP contains a one-provider diamond
germ.  If a future construction retains its two exterior guards, canonical
facet bridge states, and natural union mate, then that germ returns as the
same typed socket with a common added tag.  Repeating this prescription gives
the infinite sector induction (5.16).

This is stronger than a terminal calibration.  It proves local port
regeneration.  It does **not** prove that a future global braid can keep the
germ while also realizing every middle owner and every compiler target.

For comparison, the complete upper casualty list of the `11->12` terminal
braid has depths one and two.  Transporting those old occurrences through a
new order-one facet requires protected base collars of respectively three and
four transitions (`a+q_child`), together with every canonical bridge owner.
The terminal replay did not reserve those future collars.  The local diamond
chosen in Theorem 3.1 avoids that issue by exporting its own complete guarded
upper-`q=1` chart explicitly.

## 7. Exact full-plateau criterion

Fix a proposed one-flat plateau skeleton built from order-zero pieces

\[
 N_i=V_i
\]

at horizon `d`, order-one pieces

\[
 F_i=\{z\}\cup(V_i\cap V_{i+1})
\]

at horizon `d-1`, all canonical bridge states, and any explicit replacement
states.  Fix a transported protected matching which includes one duplex
socket germ.

For each ordinary module, let `mathcal R_j` be the relation imposing
nonemptiness, envelope containment, every internal child-owner equation,
every selected child-provider equation, and every fixed-tag hit.  For the
exported duplex germ, `mathcal R_j` also has parent-source variables and, on
every germ source occurrence, imposes the suspension relation

\[
 Q^{\rm child}_p=\{z\}\cup Q^{\rm parent}_p         \tag{7.1}
\]

at a suspension step, or equality with the parent source at a copy step.
Join all module relations with every cross-interface owner equation, and
project the result to the child-source coordinates:

\[
 \mathcal F_*=
 \pi_{\rm child}\!\left(\Join_j\mathcal R_j\right). \tag{7.2}
\]

Thus every child source in `mathcal F_*` has a compatible parent source and
preserves the recursive germ correlation, not only its target labels.

Let `T_cas` be every strict lower target not in the protected matching and
`C_free` every unallocated physical interval.  For `Q in mathcal F_*`, put

\[
 T\sim_Q C\quad\Longleftrightarrow\quad
 \bigcup_{p\in C}Q_p=T.                             \tag{7.3}
\]

### Theorem 7.1 (same-source plateau closure)

Assume the fixed skeleton has the exact child middle deck, all transitions
are legal, every selected collar survives, the exhaustive internal/bridge/
seam/multi-seam window catalogue covers the whole upper ideal, and every
residence, endpoint, terminal, and singleton condition passes.  Then, relative
to this skeleton and protected matching, a terminal child preserving the
duplex germ exists if and only if

\[
 \boxed{
 \exists Q\in\mathcal F_*
 \text{ such that }
 G_Q=(\mathcal T_{cas},\mathcal C_{free},\sim_Q)
 \text{ has a matching saturating }\mathcal T_{cas}.} \tag{7.4}
\]

If the completed child also exports the renewed socket data of Definition
5.2, it is a ported child of the same recursive type.

#### Proof

Given (7.4), the common source reconstructs every internal and cross-interface
owner and keeps every protected edge exact.  The protected matching and the
matching in `G_Q` cover the strict lower ideal.  The fixed hypotheses cover
the middle and upper ideals and every physical boundary obligation.  The
child is therefore terminal, and the additional typed export makes it
ported.

Conversely, any completion preserving the skeleton and protected germ
restricts to a member of the natural join.  Choose one actual unallocated
witnessing interval for each casualty target.  Distinct labels cannot use the
same exact interval, so these choices give a saturating matching in `G_Q`.
\(\square\)

The quantifier order in (7.4) is essential.  Nonemptiness of `mathcal F_*`
and Hall in the union of the graphs `G_Q` do not suffice; all protected and
casualty edges must coexist under one source.

## 8. Sharp remaining theorem

The local recursive port problem is solved by the duplex class.  The global
ported plateau extension is reduced to the following single existence
statement.

> **PBBS duplex-embedding lemma (UNPROVED).**  At every plateau rank, one
> exact PBBS/Pascal child skeleton can be chosen so that (i) it contains a
> guarded diamond/duplex germ, (ii) its exact middle and complete upper
> catalogues pass, and (iii) the same-source condition (7.4) holds while the
> renewed germ is protected.

If this lemma and the separately typed nonplateau/even-to-odd deck transition
hold for one recursive carrier family, Corollary 5.3 and the ported PBP
composition theorem give an all-`k` induction.  The present note does not
prove the lemma.  In particular:

- a nonempty renewable port does not imply the global Hall matching;
- upper duplex closure does not imply exact middle ownership;
- a cyclic abstract socket must still be installed in one literal linear
  chronology with endpoint completions; and
- the finite `k=12,14` source fibres do not automatically extend to the next
  rank.

The decisive advance is therefore exact but scoped: the recursive **port
regeneration** obstruction is removed for a nonempty typed germ; the remaining
obstruction is its global common-source/middle/upper embedding.

## 9. Audit boundary

The finite equalities in Section 3 are direct reads from the already
authenticated words and middle paths.  No SAT, exhaustive search, or remote
computation is used.  All other statements are algebraic.

The report makes none of the following stronger claims:

1. that the whole `k=12` or `k=14` compiler matching is facet-transparent;
2. that the original terminal certificates reserved every future bridge;
3. that a pure facet exports the same port type;
4. that the duplex sector exhausts the next middle deck; or
5. that (7.4) has been solved at arbitrary rank.
