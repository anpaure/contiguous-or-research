# Hall-23 labelled occurrence-return flow and the protected-tail obstruction

Date: 2026-07-31  
Scope: the frozen K16 `hit_7` carrier, an exact finite return atlas, and a
conditional coupling to the separately authenticated `c279` one-hole
chronology.  This note proves a general labelled-flow criterion and a sharp
obstruction for returns disjoint from the tail dependency collar.  It does
**not** prove that the Hall-23 carrier cannot be repaired by a larger
overlapping packet, by a provider migration, or by changing the flat
schedule; nor does it identify the two authenticated compiler layers.

## 1. Result

Let

```text
Q = scratch/k16_nested_hall24_third_equalblock_20260731/
    pass33_m32/hit_7.targets
```

with SHA-256

```text
57db213117877dc3a41f3426fdce98de4cf754119bc6374639ba635b16c1d252.
```

It has length 12873, the prescribed three flats, exact middle replay, Hall
matching (26309/26332) (deficiency 23), providers `8000` and `4e70`, and
the sole arbitrary-upper hole `4e79`.

The exact conclusions are:

1. The stated tail model has exactly eleven flat-preserving, middle-exact
   pairs $(F,Y)$.  Every pair fills `4e79` and deletes the unique old
   `ce3c` witness.
2. There are twenty raw one-row middle-compatible destinations for the
   displaced `ce38` occurrence in the representative tail context, but
   exactly two also restore `ce3c`: rows 6608 and 12661.  The former consumes
   the `4e70` provider; the latter is `4e70`-collar-safe but has the Boolean
   uncovered-target effect
   
   
   \[
   \{ce3c\}\longmapsto\{ce6c,ce74,cf74\}.
   \]
3. A literal `4e70`-collar-safe facet cycle through 12661 and a disjoint
   $Y$-return cycle exist.  Their union is occurrence-bijective and
   middle-exact.  It is not label-balanced: it leaves 21 upper holes and has
   full Hall deficiency 43.
4. More decisively, every one of the eleven tail pairs destroys the same
   protected `8000` incidence inside the dependency collar
   $[12716,12723)$.  A return disjoint from this collar has identically zero
   `8000` label, so its reachable affine label set lies in the hyperplane
   with net `8000` label $-1$.  It therefore cannot be provider-safe.
5. Even after relaxing occurrence balance, exhausting one additional source
   value at one additional collar row gives 849354 substitutions, of which
   939 remain middle-exact and **none** restores `8000`.  Thus a repair that
   retains that named provider cannot consist solely of a tail pair and one
   otherwise isolated collar-row substitution.  The remaining possibilities
   are at least two changed collar rows, one collar row embedded in a larger
   interacting packet, a changed flat schedule, or migration of the Hall
   certificate to a different incidence with a complete matching of size at
   least 26309.
6. In the separate literal one-hole chronology, every strongest
   `p12826` ghost-breaking edit has $\Delta G=-1,\Delta F=+1$ and leaves
   exactly `{2c6d,c679}`.
7. Those two residuals and the literal singleton `8000` have the unique
   one-cell hinge $0408\subseteq v\subseteq0469$ in the authenticated fixed
   contexts at `p6437`.  It supplies all three literal labels but does not
   restore the separate Hall incidence; it also necessarily loses six
   `0879`-core targets.
8. A complete 69,732-case replay finds no middle-exact pure
   `P-C-Q`/tail permutation using one to three `P-C-Q` rows (including
   `C`) and exactly two or three tail rows.  The literal hinge and Hall
   incidence remain different physical objects, so their joint embedding is
   still conditional.

The fifth statement is a finite, explicitly scoped source-value theorem.  It
is not an unrestricted lower bound on K16.

## 2. The exact occurrence-routing model

### 2.1 Occurrences, not merely values

Write the carrier as an occurrence-labelled word

\[
Q=((q_0,\ell_0),\ldots,(q_{n-1},\ell_{n-1})),
\]

where the labels $\ell_i$ are distinct even when two masks $q_i$ agree.
An occurrence rethread is a partial permutation of these labels.  Its routing
digraph has an arc $s\to t$ when the occurrence at source row $s$ is
installed at destination row $t$.  Literal occurrence conservation is

\[
\deg_x^+(p)=\deg_x^-(p)\le 1
\tag{2.1}
\]

at every moved row.  Thus an integral solution is a disjoint union of directed
occurrence cycles.  If one physical cycle is required, add connectedness (or
standard subtour-elimination constraints); the two-cycle macro studied below
does not need this extra condition.

A single-row compatibility arc is only a diagnostic.  Two individually
compatible arcs can interact through a common erosion collar or through a
long upper interval.  To make labels additive, one must do one of the
following:

- use packets whose complete dependency and witness closures are disjoint; or
- state-expand the routing graph so a vertex records every live collar and
  every unfinished witness fragment touched by the next arc.

In the state-expanded graph, an arc is an actual transition between two
partially rethreaded states, not a base-relative guess.

### 2.2 Resource labels

For every upper target $u$, let $W_u(Q)$ be the number of physical
intervals in $Q$ whose OR is $u$.  For a state-correct transition $a$,
define

\[
\lambda^U_u(a)=W_u(Q_{\mathrm{after}})-W_u(Q_{\mathrm{before}}).
\tag{2.2}
\]

These signed occurrence counts telescope along a state-expanded route.  In
particular, upper coverage is exactly

\[
W_u(Q)+\sum_a \lambda^U_u(a)x_a\ge 1
\quad\text{for every required }u.
\tag{2.3}
\]

For the lower compiler, let $I_{t,c}(Q)\in\{0,1\}$ say that target $t$
is eligible for physical chronology cell $c$.  Transported occurrence tuples
are additional provenance state; they are not interchangeable Hall columns.
The Hall label is

\[
\lambda^H_{t,c}(a)
=I_{t,c}(Q_{\mathrm{after}})-I_{t,c}(Q_{\mathrm{before}}).
\tag{2.4}
\]

Scalar matching deficiency is **not** an additive arc label.  Exact
acceptance reconstructs the final physical-incidence bit
$I^{\mathrm{fin}}_{t,c}$ and introduces binary matching variables
$m_{t,c}\in\{0,1\}$ satisfying

\[
\begin{aligned}
&m_{t,c}\le I^{\mathrm{fin}}_{t,c},\\
&\sum_c m_{t,c}\le1 &&(t\text{ fixed}),\\
&\sum_t m_{t,c}\le1 &&(c\text{ fixed}),\\
&\sum_{t,c}m_{t,c}\ge26309.
\end{aligned}
\tag{2.5}
\]

The final inequality is precisely Hall deficiency $<24$.  A smaller model
may protect a fixed matching and its augmenting paths, but then its conclusion
is only for that protected face.

### 2.3 Labelled return-circulation theorem

**Theorem 2.1 (exact layered-state return criterion).**  Fix a finite layered
state automaton whose vertices record the complete partial occurrence
assignment and every overlap datum needed to evaluate (2.2) and (2.4).
Every transition is a literal substitution step and emits zero or more
occurrence-routing arcs.  A prescribed tail return is realizable with exact
occurrence conservation, all required upper witnesses, and Hall deficiency
$<24$ if and only if there are binary transition variables selecting one
initial-to-terminal path in this automaton such that:

1. the aggregate emitted occurrence arcs satisfy (2.1);
2. the path contains the prescribed tail, socket, and return transitions;
3. its terminal state has closed collars and no unfinished witness fragment;
4. the telescoped upper labels satisfy (2.3);
5. the reconstructed final physical incidences and binary matching variables
   satisfy (2.5).

If the output occurrence permutation must itself be one cycle, impose
connectedness on its aggregate emitted routing arcs.

**Proof.**  A literal rethread can be read as one path of literal substitution
states.  It assigns each moved occurrence to exactly one destination and
vacates exactly one source, hence its emitted arcs give (2.1).  Resource
differences telescope, and its actual final matching gives (2.3) and (2.5).

Conversely, the selected automaton path is one coexistent sequence of literal
substitutions, rather than an arbitrary union of pairwise compatible arcs.
The squarefree aggregate flow is an occurrence permutation, while terminal
closure gives a literal middle-exact final state with no live fragment.
Telescoping makes (2.3) its actual upper ledger, and the binary
$m_{t,c}$ form a matching in its physical final incidence graph. \(\square\)

The theorem explains why an arc graph carrying only scalar hole counts or
scalar Hall deficiency is unsound.  All-depth upper intervals and compiler
cells are stateful resources.

### 2.4 Affine-monoid obstruction

Let $Dx=b$ denote only the prescribed occurrence boundary and anchor
equations, and let $Ax$ be the exact signed resource label.  If squarefree
capacities and the layered state-path constraints are temporarily relaxed,
the nonnegative integral solutions map to a finite union of affine monoid
translates

\[
A\{x\ge0:Dx=b\}
=\bigcup_j\left(Ax^{(j)}+A\{z\ge0:Dz=0\}\right).
\tag{2.6}
\]

Indeed, there are finitely many coordinate-minimal solutions of $Dx=b$ by
Dickson's lemma, and the nonnegative integral kernel monoid is finitely
generated by Gordan's lemma.  Therefore either of the following is a valid
obstruction for the relaxation, and hence for the literal problem:

- the acceptable resource region misses every affine monoid in (2.6); or
- already a lattice coset containing (2.6) misses the acceptable region.

A single resource coordinate can separate the sets.  Intersection with the
relaxed set would not, conversely, prove a literal squarefree rethread.  The
protected `8000` incidence supplies a separating coordinate below.

## 3. The eleven tail pairs and two debt-closing sockets

The complete local pair table is

\[
\begin{aligned}
F&\in\{0e79,4c79,4e39,4e59,4e78\},
&Y&\in\{c62e,ce26\},\\
(F,Y)&=(4679,ce26).&&
\end{aligned}
\tag{3.1}
\]

This gives eleven pairs.  The two pairs with $F=4e78$ consume row 6608 and
are immediately `4e70`-provider-destructive.  The other nine are safe at that
donor site.  Every pair has the same relaxed uncovered-set transition:

\[
\{4e79\}\longmapsto\{ce3c\}.
\tag{3.2}
\]

Here “relaxed” means that the two tail rows have been substituted but the two
displaced occurrences have not yet been returned.

In the representative $F=4c79,Y=c62e$ context, exactly twenty rows accept
`ce38` while keeping the middle schedule.  Exactly two of those rows also
create an interval OR equal to `ce3c`:

\[
\begin{array}{c|c}
6608 &[6608,6610)=ce38,4e3c,\\
12661 &[12661,12663)=ce38,ce34.
\end{array}
\tag{3.3}
\]

Thus “exactly two sockets” always means *middle-compatible and
`ce3c`-restoring*, not merely middle-compatible.  Socket 6608 consumes the
`4e70` provider.  Socket 12661 preserves that collar, but replacing its old
`ce64` occurrence erases the three rooted witnesses

\[
\begin{aligned}
ce68\vee ce64&=ce6c,\\
ce64\vee ce34&=ce74,\\
ce64\vee ce34\vee cd34&=cf74.
\end{aligned}
\tag{3.4}
\]

Consequently its Boolean uncovered-set transition is

\[
\{ce3c\}\longmapsto\{ce6c,ce74,cf74\}.
\tag{3.5}
\]

Within the provenance-preserving one-centre subclass, the three designated
rooted OR equalities are reproduced precisely when, up to reversal, a
replacement centre $R=ce64$ and its neighbouring rows satisfy

\[
L\vee R=ce6c,\qquad
R\vee R_1=ce74,\qquad
R\vee R_1\vee R_2=cf74.
\tag{3.6}
\]

This is not by itself a valid replacement socket: middle exactness, other
upper witnesses, occurrence balance, and Hall remain separate constraints.
Globally, three unrelated replacement intervals could also effect the same
Boolean repair, so (3.6) is not asserted outside the designated one-centre
shape.

## 4. A literal `4e70`-collar-safe route, and why it fails

For $F=4c79@3105$ and $Y=c62e@8796$, the following two occurrence cycles
are literal:

\[
\begin{aligned}
3105&\to12714\to12661\to7775\to0\to4454\to298\to4156\to3105,\\
8796&\to12717\to2514\to497\to2297\to8796.
\end{aligned}
\tag{4.1}
\]

The first route sends the displaced `ce38` occurrence to the provider-safe
socket 12661.  The second returns the displaced tail-(Y) occurrence.  Their
supports are disjoint, their union is an occurrence permutation, the three
flats remain fixed, and complete middle replay passes.

The final upper-hole set is

```text
396d 3d69 4f2d 4f6d 5b2e 672e 6c79 6d74 766d 7971 7978
8e6d c66d c72e c73e ce6c ce74 cf74 d73e e66d e76d
```

with rank histogram (14,5,2) at ranks (9,10,11).  The macro gains the
previously missing `4e79` and keeps `ce3c`, but leaves these 21 upper
targets uncovered.
It retains `4e70`, loses `8000`, and has

\[
\operatorname{match}=26289,\qquad
\operatorname{def}=43=26+17.
\tag{4.2}
\]

Here 26 is the zero-provider term and 17 the shared-component term.

There are two useful fixed-matching diagnostics.  Freezing chronology cell
IDs loses 74 base-matching eligibilities.  Transporting literal occurrence
tuples loses 102.  The exact reconciliation is

\[
102=74+29-1:
\]

29 physical cells retain eligibility after acquiring different occurrence
tuples, while one canonical tuple migrates to a different physical cell.
The occurrence-labelled number 102 is the correct routing diagnostic; neither
scalar replaces the authoritative full rematching in (4.2).

This proves a rejection of the concrete route (4.1), not of every path to
12661.

## 5. The protected-tail affine obstruction

### 5.1 Exact profile change

In the frozen Hall-23 carrier, the named `8000` provider is the singleton
compiler cell at physical row 12720 (source label 6613).  After every pair in
(3.1), its allowed mask remains

\[
P=8a0e,
\]

but its mandatory mask becomes

\[
M=\begin{cases}
8800,&Y=c62e,\\
8008,&Y=ce26.
\end{cases}
\tag{5.1}
\]

Since $M\nsubseteq8000$, the cell cannot host target `8000`.

The extra mandatory bit is forced by row 12718=`ca2e`.  For $Y=c62e$, the
only surviving carrier position for bit `0800` in that row is 12720.  For
the case $Y=ce26$, the analogous unique carrier bit is `0008`.  All data determining
this cell lie in

\[
C=[12716,12723).
\tag{5.2}
\]

### 5.2 Monoid separation

**Theorem 5.1 (disjoint-return obstruction).**  Fix any of the eleven tail
pairs.  Every completed occurrence-return packet whose additional support is
disjoint from $C$ has net protected-provider label

\[
\lambda_{8000}=-1.
\tag{5.3}
\]

Hence the tail translate of the reachable kernel-label monoid is disjoint
from the face that retains the named `8000` incidence.

**Proof.**  The tail pair changes the cell profile according to (5.1), so it
contributes $-1$.  The cell envelope and mandatory mask are functions only
of the rows in $C$.  Every additional substitution disjoint from $C$
therefore has zero label in this coordinate.  Projection onto the `8000`
coordinate separates the affine reachable set from the provider-safe
face. \(\square\)

This is the requested exact zero-exclusion result.  Its scope is the named
provider.  Full Hall deficiency can in principle be restored by a different
provider and a new augmenting path, so (5.3) alone is not a global Hall
obstruction.

### 5.3 One-extra-row strengthening

The independent audit next relaxes occurrence balance and tries every rank-8
source value already present in the carrier at one additional row of $C$,
for each of the eleven tail pairs.  It finds

\[
849354\text{ substitutions},\quad
939\text{ middle-exact},\quad
0\text{ restoring `8000`}.
\tag{5.4}
\]

Because occurrence balance was not required, this is stronger than rejecting
one-cycle completions in that finite one-row atlas.

**Corollary 5.2.**  Within the frozen flats and the exact experiment in which
all rows except one additional row of $C$ remain fixed, no source-value
substitution retains the named `8000` provider.  A still-live retaining
packet must therefore use at least two collar rows, or couple one collar-row
change to additional interacting support not represented by this frozen
one-row experiment.  Provider migration remains a separate alternative.

## 6. Exact next port signature

The smallest still-live macro is not a disjoint facet cycle plus a disjoint
$Y$ cycle.  It must contain a genuinely overlapping tail packet satisfying
one of two alternatives.

### Alternative A: retain the named providers

The packet must:

1. either alter at least two additional rows of $C$, or couple one changed
   collar row to a larger interacting packet outside the frozen one-row
   atlas;
2. restore the `8000` cell, so its Hall label has
   \(\lambda_{8000}=+1\) relative to the relaxed tail;
3. preserve `4e70`;
4. supply witnesses for `ce6c`, `ce74`, and `cf74` (or avoid deleting them);
5. return both displaced occurrences and introduce no other unique-upper
   debt.

### Alternative B: migrate the Hall certificate

The packet may leave `8000` dead, but then it must produce an independently
audited final matching of size at least 26309.  A raw count of gained cells or
a scalar matching-loss score is insufficient.

In either alternative, the exact finite search object is Theorem 2.1: a
state-expanded, label-balanced occurrence circulation with the full upper
witness inequalities and matching flow.  The current result removes every
return whose second cycle is disjoint from the protected collar and purports
to retain the same provider.

## 7. Audit and artifacts

Primary solver-free replay:

```text
scratch/audit_k16_hall23_label_balanced_return_20260731.py
SHA-256 98a691644e2dd22f8786178454a1e4c6c1610e1b87ed85a68a64c5d5f61dcc7a

scratch/k16_hall23_label_balanced_return_20260731.audit.json
SHA-256 d5c6ac8eae01587aa324477cb14aed9a0c5723c04dfa4206e1eb90e1eaae0c48
payload  56189f3fddfe344bf12770d4be8316783e359ac8777b61b3dc424b648638e6e4
```

The replay authenticates the input, reconstructs all eleven pairs, counts the
twenty raw and two debt-closing sockets, checks every pair's exact provider
profile, materializes (4.1), verifies occurrence bijection and complete
middle/upper replay, rebuilds both Hall graphs, distinguishes physical-cell
from occurrence-labelled matching losses, and performs the complete
one-extra-row collar census (5.4).  Peak resident memory in the timed replay
was below 131 MB; no SAT or heavy search was used.

Independent audits reproduced the eleven-pair table, the two qualified
sockets, the concrete cycle ledger, the $43=26+17$ Hall result, and the
protected-provider profile (5.1).  The only corrected wording is that there
are twenty raw middle-compatible `ce38` destinations; “exactly two” refers to
those that additionally restore `ce3c`.

## 8. Coupling the protected Hall loss to the `c279` ghost

The ghost coordinate lives on a completed literal compiler word, whereas
`hit_7` is a middle-target schedule with a Hall incidence graph.  These
layers must not be silently identified.

### 8.1 The two authenticated layers

For a literal word, let \(J_{T,q}=1\) when some start first reaches rank eight
with label \(T\) at right deadline \(q\).  Then

\[
G_T=\left(\sum_qJ_{T,q}-1\right)_+,\qquad G=\sum_TG_T.
\tag{8.0a}
\]

The state-expanded model should track the deadline indicators \(J_{T,q}\);
scalar \(G\) is only their final projection.  More explicitly, for a changed
support let \(F_T\) be the unaffected deadline set and let \(L_T,L'_T\) be
the affected old and new deadline sets.  Then

\[
\Delta G=\sum_T\left[
  (|F_T\cup L'_T|-1)_+-(|F_T\cup L_T|-1)_+
\right].
\tag{8.0b}
\]

This formula is exact even when a move merges two groups rather than merely
deleting one witness.

The maximal-envelope realization of `hit_7` has 12873 first-middle
deliveries, 12870 distinct targets, and ghost count \(G=0\).  Its unique
`c279` delivery starts at 11613, ends at deadline 11615, and uses

\[
8271,\quad c261,\quad 8269
\]

with cumulative ranks \(6,7,8\).  Thus the Hall carrier itself does not
contain the extra literal `c279` deadline that needs removal.

The separately authenticated one-hole literal word

```text
scratch/k16_upper12874_best_delete.word
SHA a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

has two `c279` deadline groups, at 11728 and 12828.  Its second group
is supported by

```text
p12826..p12828 = c261 8231 c219.
```

The sixteen exact strongest substitutions at 12826 are

\[
x_G=4001\vee a\,0020\vee b\,0840\vee c\,0200\vee d\,8000,
\qquad a,b,c,d\in\{0,1\}.
\tag{8.1}
\]

Each removes exactly the later `c279` deadline, creates no other
ghost, and leaves the exact literal residual

\[
H=2c6d,\qquad U=c679.
\tag{8.2}
\]

For the fixed following cells,

\[
8231\vee c219=c239,\qquad
8231\vee c219\vee c608=c639.
\]

The paired switch \(0840=0040\vee0800\) in (8.1) gives

\[
\begin{array}{c|cc}
&\text{three-cell OR}&\text{four-cell OR}\\ \hline
b=0&c239&c639\\
b=1&ca79&ce79.
\end{array}
\tag{8.3}
\]

In particular the branch can never preserve `c679`: supplying its
missing bit `0040` automatically introduces the forbidden bit
`0800`.  This is why `c679` is forced into the post-ghost
residual.

The deadline inventory is sharper.  At the recipient the old consecutive
first-delivery chain is

\[
A-C-B=(ca71,c279,c639).
\]

The \(b=0\) branch changes it to \(A-B-B\), while \(b=1\) changes it to
\(A-A-B\).  Hence every strongest edit has

\[
\Delta G=-1,\qquad \Delta F=+1.
\tag{8.4}
\]

The ghost charge is converted into a neighbouring same-deadline flat; it is
not simply deleted from the inventory.

### 8.2 Fixed-context two-arm hinge theorem

**Lemma 8.1 (exact fixed-context oriented hinge).**  Let fixed left and right
contexts have
ORs \(L\) and \(R\), and let one pivot cell \(v\) be required to satisfy

\[
L\vee v=U,\qquad v\vee R=H.
\tag{8.5}
\]

Put

\[
M=(U\setminus L)\cup(H\setminus R),\qquad K=U\cap H.
\]

A (possibly zero) solution exists if and only if

\[
L\subseteq U,\qquad R\subseteq H,\qquad M\subseteq K.
\tag{8.6}
\]

When it exists, the complete solution set is

\[
M\subseteq v\subseteq K.
\tag{8.7}
\]

A nonzero solution exists exactly when these conditions hold and $K\ne0$.

**Proof.**  Every bit of \(U\setminus L\) and \(H\setminus R\) must occur in
\(v\), while every bit of \(v\) must lie in both targets.  This proves
necessity and (8.7).  Conversely, (8.6)--(8.7) make both unions in (8.5)
equal to their targets. \(\square\)

For the residual (8.2), the literal word has the fixed six-cell port

```text
positions 6434..6439: 0600 4071 8000  v  2869 206d.
```

Here

\[
L=c671,\qquad R=286d,\qquad M=0408,\qquad K=0469.
\]

Therefore the complete pivot cube is

\[
v=0408\vee e\,0001\vee f\,0020\vee g\,0040,
\qquad e,f,g\in\{0,1\}.
\tag{8.8}
\]

Every one of these eight pivots realizes the nested three-label fork

\[
\begin{aligned}
[6434,6437]&\longmapsto c679,\\
[6436,6436]&\longmapsto 8000,\\
[6437,6439]&\longmapsto 2c6d.
\end{aligned}
\tag{8.9}
\]

Within these fixed contexts and this one-pivot geometry, the orientation is
forced because `8000` belongs to \(U\) but not to \(H\).  Thus the
`2c6d` arm begins after the singleton `8000` cell.  A wider edit may
alter or relocate the contexts.  Equation (8.9) is the exact one-cell
three-label conservation law suggested by the post-ghost residual.

Every hinge value contains bit `0400`, which is absent from all six
old private targets

```text
2879 287d a879 a87d c879 e879.
```

Every old witness for each of these targets passes through the pivot.
Therefore all six losses are forced, solver-free, for every value in (8.8).
A separate `0879`-core provider avoiding the hinge is necessary.

### 8.3 Algebraic bridge to the tail facet

The three relevant labels satisfy

\[
\begin{aligned}
c279&=8000\vee4279,\\
4679&=4279\vee0400,\\
c679&=8000\vee4679=c279\vee0400,\\
2c6d\cap8000&=\varnothing,\\
2c6d\vee c679&=2c6d\vee c279=ee7d.
\end{aligned}
\tag{8.10}
\]

Among the eleven exact tail pairs, the unique pair using physical target row
`4679@12826` is

\[
(F,Y)=(4679,ce26).
\tag{8.11}
\]

It is also the `ce26` branch of (5.1), so it changes the named
`8000` Hall cell to allowed `8a0e`, mandatory `8008`.
Thus the same mask identity selects the ghost-facing facet and the
provider-destructive tail branch.  This is a cross-artifact algebraic
alignment, not yet one physical occurrence map.

Equation (8.10) says that a literal `8000` socket plus a clean
`4679` wing can witness `c679`.  It does not prove that the
literal singleton at 6436 is the Hall incidence `8000--J31761`.  They
belong to different authenticated artifacts, and no occurrence map between
them is known.  A source-compensated embedding must preserve or restore the
Hall incidence separately, or rebuild the complete matching after a proved
provider migration.

There is also a local contamination obstruction to reusing the current named
Hall cell directly.  In (8.11), the moved `4679` delivery is at row
12714, the named `8000` cell is at 12720, and the intervening
depth-two target at row 12717 is `ce26`.  Any interval containing the
whole `4679` delivery window and the cell at 12720 also contains the
`ce26` delivery window, but

\[
ce26\setminus c679=0806\ne0.
\tag{8.12}
\]

So that direct complete-window span cannot be a `c679` witness.  This
does not exclude a different witness elsewhere or a wider partial-window
braid.

### 8.4 The C-allocation invariant and the small-support no-go

In the `hit_7` target order, the unique `c279` owner lies in

\[
(P,C,Q)=(c371,c279,e269)
\]

at rows \(11612,11613,11614\).  With neighbouring rows \(P,Q\) fixed, a
rank-eight replacement \(D\) preserving both donor colours must satisfy

\[
P\vee D=c379,\qquad D\vee Q=e279.
\]

Then

\[
D\subseteq c379\cap e279=c279=C,
\]

and rank equality forces \(D=C\).  Thus, in this fixed-neighbour subclass,
moving the unique \(C\) owner destroys at least these two donor colours
unless they are rehosted elsewhere.  Simultaneous changes of \(P\) or
\(Q\) are not covered.

The single-row compatibility arcs from the \(P,C,Q\) rows into the full tail
are exactly

```text
c371 -> 12711
c279 -> 12712,12713,12714
e269 -> 12712.
```

There is no compatible arc in the reverse direction from any row
12710--12722.  The compatibility cut is one-way.

The exact finite occurrence census selects one to three of the \(P,C,Q\)
rows (always including \(C\)), two or three tail rows, deranges every selected
occurrence, and requires \(C\) to enter the tail.  Complete middle replay
gives

\[
\begin{array}{c|r|r}
\text{tail range}&\text{tested}&\text{middle-exact}\\ \hline
12710\ldots12716&8946&0\\
12710\ldots12722&69732&0.
\end{array}
\tag{8.13}
\]

Thus no pure ghost--tail occurrence macro in this tested class can provide
the desired collar overlap.  A surviving pure packet lies in the untested
one-tail-row class or uses at least four tail rows; a mediated packet is also
untested.  No numerical support lower bound is claimed.  This is a scoped
finite no-go, not a lower bound for arbitrary braids.

### 8.5 Exact live macro

A packet in the proposed composite branch (strongest `p12826` breaker,
`(4679,ce26)` tail pair, and the `ce38@12661` socket) must satisfy all
of the following.

1. Remove the extra literal `c279` deadline, with the authenticated
   strongest branch leaving exactly `{2c6d,c679}`.
2. Realize the hinge (8.9), or a wider debt-neutral substitute, and provide
   a separate reserve for the six `0879`-core debts if (8.9) is used.
3. Overlap the Hall dependency collar enough to restore the named
   `8000` incidence, or give an independently audited replacement
   matching of size at least 26309.
4. Restore the `ce64`-root upper resources from (3.4), retain
   `4e70`, and close both occurrence boundaries; this item is specific to
   the chosen `ce38@12661` socket.
5. Preserve the two authenticated donor colours in Section 8.4 or rehost
   them; stronger donor-tower preservation is a separate ledger.
6. Leave the class closed by (8.13): use one tail row, at least four tail
   rows, or an external mediator.

This is the sharp proved/conditional boundary for that composite branch.  A
different ghost-free chronology, a different ghost cell, or a different tail
route need not satisfy this list.  The branch has an explicit three-label
hinge and an explicit protected-collar obligation, but no literal embedding
joining them has yet been constructed.

Independent coupling replay:

```text
scratch/audit_k16_hall23_ghost_provider_coupling_20260731.py
SHA-256 24b07899fa7f582b67eab233766f59b4e759348eab5b429e8c0528eda34308a6

scratch/k16_hall23_ghost_provider_coupling_20260731.audit.json
SHA-256 2ecc0e1f5970215ce9f2327a31e3d67b5ca53f0da381892ff0c8f4144b23e504
payload  f20eaec4eebb83a326d0b7e6a4d1674ada10782bddaa459a5f6a72a6bf8eabf4
```
