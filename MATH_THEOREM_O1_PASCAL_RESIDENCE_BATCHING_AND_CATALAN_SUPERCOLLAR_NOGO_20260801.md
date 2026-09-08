# Pascal residence batching and the Catalan supercollar obstruction

Date: 2026-08-01  
Lane: L, density-matched `B+O(1)` reset  
Status: exact canonical defect-bank theorem, exact trace-level batching, and
exact lower-`q1`/fixed-slot-menu obstruction.  The proposed independent
`O(d)`-seam full reset is false on the edge-local Pascal baseline.  A
Catalan-scale status normal form is constructed, but its Johnson-labelled
physical lift, upper tower, topology, and common compiler cap remain open.

## 0. Verdict

Put

\[
 k=2m-1,\qquad W={2m-1\choose m},\qquad
 c=\operatorname {Cat}_m={2W\over m+1}.                         \tag{0.1}
\]

The canonical four-sector lift has exactly `2W` newborn residence defects:
the `W` runs `A_iX_i` of the new coordinate `x` and the `W` runs `Y_iA_i`
of `y`, all of length two.  These defects really can be grouped into
`Theta(W/d)` contiguous **binary-trace** collars of span and seam budget
`Theta(d)`.  Thus the global `Omega(W)` changed-seam theorem is numerically
compatible with the density-matched proposal.

The proposal nevertheless fails as a full reset.  There are `W-c` required
immediate-lower colours containing both new coordinates, and only `AA`
seams can realize them.  If a repaired chronology has `b_A` maximal
`A`-blocks, it has at most `W-b_A` such seams, whence

\[
                         H_A^-\ge (b_A-c-e)^+.                    \tag{0.2}
\]

Here `e` is the explicitly exported number of colours allowed to be supplied
outside the ordinary central `AA` row; `e=0` on the exact flat row and
`e=O(1)` under a bounded terminal sidecar.

For independently sealed collars, each changing at most `s` seams and
retaining the baseline sector type at its boundary, no `A`-block crosses a
collar boundary and every such block has length at most `s+1`.  Therefore

\[
 \boxed{
 H_A^-\ge
 \left(\left\lceil {W\over s+1}\right\rceil-c-e\right)^+.}       \tag{0.3}
\]

At the deadline scale `d=Theta(sqrt(m))`, taking `s=O(d)` and `e=O(1)`
leaves `Theta(W/d)` lower-`q1` holes.  Exact coverage forces one collar to
contain an `A`-block of length

\[
                    {W\over c+e}-O(1)=\Theta(m)=\Theta(d^2).     \tag{0.4}
\]

The first count-consistent reset scale is consequently `c=Theta(W/m)`
Catalan supercollars, each of span `Theta(m)`, not `Theta(W/d)` independent
microcollars of span `Theta(d)`.

The compressed prefix/suffix/internal OR-deck theorem does not remove this
obstruction.  It governs upper coverage, whereas (0.2) is a literal
immediate-lower seam count.  Moreover, even its weakest total-OR clause
limits a fixed length-`h` standard `(b,c)` C6/ECO slot to at most
`m(h-1)` candidates.  Thus a fixed `h=O(d)` slot has only `O(md)=o(m^2)`
standard candidates.  For the raw anchored C6, internal-deck dominance
reduces the safe list further to exactly one pair.

## 1. The canonical residence-defect bank

Let `T_i`, `i in Z_W`, be the parent lower-`q1`-bijective Johnson cycle and
write

\[
 C_i=T_i\cap T_{i+1},\quad
 Y_i=T_i+y,\quad A_i=C_i+x+y,\quad X_i=T_{i+1}+x.                 \tag{1.1}
\]

At selected indices the empty-signature owner `U_i=T_i union T_{i+1}` is
inserted before `Y_i`.  The canonical status word is

\[
                 [U_i]Y_iA_iX_i,qquad
 U=00,\ Y=01,\ A=11,\ X=10.                                    \tag{1.2}
\]

Let

\[
                         D_*=d(k+2)+1                            \tag{1.3}
\]

be the child minimum positive-run length.

### Theorem 1.1 (exact indexed defect bank)

For every `i in Z_W`, (1.2) contains the two newborn atoms

\[
                         R_i^x=A_iX_i,\qquad R_i^y=Y_iA_i,       \tag{1.4}
\]

each a length-two run of deficit `D_*-2`.  Hence the newborn bank has
exactly `2W` atoms and total weighted deficit `2W(D_*-2)`.

Every oriented parent edge starts exactly one old-coordinate positive run.
Because the parent is lower-`q1` bijective, each old coordinate has
`Cat_(m-1)` runs and singleton runs are impossible.  The identity

\[
                         (2m-1)\operatorname {Cat}_{m-1}=W       \tag{1.5}
\]

therefore canonically indexes all parent runs by the same `Z_W`.  A parent
run of length `ell>=2` becomes an `A`-shore run of length `ell-1`; it is a
child defect exactly when `ell<=D_*`, with weight

\[
                         D_*+1-\ell.                             \tag{1.6}
\]

Thus one base index carries its two newborn atoms and at most one defective
old-coordinate atom.  A `q`-index collar contains exactly `2q` newborn
atoms and at most `q` old atoms.

#### Proof

The two status traces in (1.2) give (1.4) literally.  Every oriented
Johnson edge exchanges one deleted and one inserted old coordinate, hence
starts one positive run.  The induced graph on the parent owners containing
a fixed coordinate has

\[
 {2m-2\choose m-1}-{2m-2\choose m-2}=\operatorname {Cat}_{m-1}
\]

components, because all lower edge colours occur once.  This proves (1.5).
The intersection trace `C_i=T_i intersect T_(i+1)` deletes exactly the
last owner of every non-singleton forward run, giving (1.6).  The impossibility of
singleton runs follows because its two incident lower colours would both be
`T_i-z`.  \(\square\)

On a no-jump step, a parent already resident at threshold `D_*` contributes
only its length-`D_*` runs, each with unit debt.  On a deadline jump, the
two newly exposed lengths have weights two and one.  These old-coordinate
atoms are correlated with the occurrence-transversal and compiler rows;
the theorem does not treat them as freely movable binary tokens.

## 2. Residence alone batches at the tempting scale

The obstruction is not scalar residence capacity.  There is even a
trace-level batching lemma under the stronger pointwise endpoint-time guard.

### Lemma 2.1 (endpoint-time trace collar)

Assume `D_*>=3`.  Take `q` consecutive canonical indices with `q` copies of each of `Y,A,X`
and `u` optional `U` owners.  Rethread exactly this same owner/status
multiset inside the same slot, whose canonical exterior closes the initial
and terminal `x,y` runs.  If the replacement preserves the first and last
occurrence positions of both new coordinates, then

\[
                              q\ge2(D_*-1).                       \tag{2.1}
\]

Conversely, for every `q>=2(D_*-1)`, put

\[
 t=q-2(D_*-1),
\]

and let `epsilon` record whether the first canonical `U` is present.  The
status word

\[
 00^{\epsilon}\,01\,11^{D_*-1+t}\,10^{q-1}\,
 00^{u-\epsilon}\,01^{q-1}\,11^{D_*-1}\,10                    \tag{2.2}
\]

has the same status multiplicities and the same first/last positions for
`x,y` as the old collar, while every new-coordinate run has length at least
`D_*`.  Its length is `3q+u<=4q`.

#### Proof

The old first `y` is immediately followed by the first `x`.  Legal initial
`x` and `y` runs therefore overlap in at least `D_*-1` distinct `A=11`
owners.  The analogous last runs require another `D_*-1` `A` owners.  These
two sets are disjoint.  Otherwise the initial and terminal `x`-runs would be
one run spanning from position `epsilon+1` to the final position.  Its span
would be `3q+u-epsilon-1>2q`, although the word has only `2q` owners
containing `x`.  Hence the `q` available `A` owners satisfy (2.1).

In (2.2), direct counting gives `q` copies of each of `01,11,10` and `u`
copies of `00`.  Its two `x`-runs and two `y`-runs have lengths at least
`D_*`.  The first `01,11` pair and final `11,10` pair occur at the old
addresses, so the first/last positions agree.  \(\square\)

Partitioning `Z_W` into intervals of lengths between `2(D_*-1)` and
`4(D_*-1)-1` gives `Theta(W/d)` such trace collars, each changing `O(d)`
internal status seams.  This is not yet a Johnson chronology: old-coordinate
endpoint data, lower palettes, upper decks, topology, and the compiler are
not certified by (2.2).

The exact new-coordinate seam floor remains

\[
 s_{\rm all}\ge
 2\left(W-\left\lfloor {2W\over D_*}\right\rfloor\right)
 =2W-O(W/d).                                                     \tag{2.3}
\]

Equations (2.2)--(2.3) reconcile arithmetically: `Theta(W/d)` collars times
`Theta(d)` changed seams is `Theta(W)`.  In particular, (2.3) refutes
constant-seam collars but not trace batching by itself.

The compressed-deck guard may improve the constant in (2.1), because it no
longer fixes endpoint times.  None of Sections 3--5 uses (2.1); their
obstructions survive under the compressed guard.

## 3. The lower-`q1` block obstruction

There are

\[
                         W-c={2m-1\choose m+1}                    \tag{3.1}
\]

required child lower-`q1` colours containing both `x` and `y`.  Such a
colour is the intersection of two central owners only on an `AA` seam.

### Theorem 3.1 (AA block inequality)

Let a repaired central chronology contain the same `W` distinct `A`
owners, arranged in `b_A` maximal blocks.  If at most `e` members of the
family (3.1) are supplied by an explicitly separate terminal/nonflat row,
then

\[
                         H_A^-\ge(b_A-c-e)^+.                     \tag{3.2}
\]

#### Proof

The `b_A` blocks contain exactly `W-b_A` internal `AA` seams.  Each seam
has one intersection and hence supplies at most one member of (3.1).
Therefore at least

\[
 (W-c)-(W-b_A)-e=b_A-c-e
\]

members remain.  \(\square\)

The parameter `e` prevents a hidden scope change.  On the exact flat
first-lower row `e=0`; allowing a bounded terminal sidecar means only
`e=O(1)`.  An unbounded nonflat lower installer is a different architecture
and must pay its literal cells and common-cap demand.

### Theorem 3.2 (independent microcollar no-go)

Start from the canonical chronology, which has no `AA` seam.  Apply
pairwise-disjoint contiguous collars such that

1. each collar changes at most `s` physical seams; and
2. its two external boundary types are those of the off state, so no `AA`
   seam is created between different collars or across untouched material.

Then

\[
 b_A\ge\left\lceil {W\over s+1}\right\rceil,
\]

and hence (0.3) holds.

#### Proof

Every final `A`-block lies inside one collar or is an untouched singleton.
An `A`-block of length `L` contains `L-1` new `AA` seams, so `L<=s+1`.
Partitioning the `W` `A` owners into such blocks proves the first inequality;
Theorem 3.1 proves the second.  \(\square\)

For `s=Kd`, `d=Theta(sqrt(m))`, and bounded `e`, the first term in (0.3)
is `Theta(W/d)`, whereas `c=Theta(W/m)=o(W/d)`.  Thus the intended
instantiation of the conditional density-matched reset theorem is false.
More invariantly, exact coverage implies `b_A<=c+e`, so some `A`-block has
length at least `W/(c+e)`.  A sealed collar owning that block changes
`Omega(m)` seams.

This statement is scoped to independently sealed repairs of the edge-local
baseline.  One may instead install a global Catalan `A`-forest first, but
that installation is itself the unresolved `Omega(W)`-seam guarded rethread;
it cannot be declared part of the free baseline.

## 4. The count-consistent Catalan supercollar normal form

The AA ledger identifies the correct status scale.  Choose integers
`a_1,...,a_c`, balanced between the floor and ceiling of `(m+1)/2`, with

\[
                         \sum_j a_j=W.                            \tag{4.1}
\]

Set

\[
                         u_j=a_j-1,\qquad
                         x_j=y_j=m+1-a_j.                        \tag{4.2}
\]

For `m>=3`, all four exponents are positive.  Consider the cyclic status
blocks

\[
                         U^{u_j}Y^{y_j}A^{a_j}X^{x_j}.            \tag{4.3}
\]

### Theorem 4.1 (balanced Catalan status skeleton)

The `c` blocks (4.3) have all of the following exact ledgers.

1. Every block has length `2m+1`, so their total length is
   `c(2m+1)=4W-c`, the child middle-layer size.
2. The total numbers of `U,Y,A,X` owners are respectively
   `W-c,W,W,W`.
3. Every `x`-run `A^aX^x` and every `y`-run `Y^yA^a` has length exactly
   `m+1`.
4. The homogeneous/cross slot counts are

   \[
   \begin{array}{c|cccc}
   \text{lower status}&xy&y&x&\varnothing\\ \hline
   \text{available slots}&W-c&W&W&W,
   \end{array}                                                   \tag{4.4}
   \]

   where the four rows use, respectively, `AA`, `YY+YA`, `XX+AX`, and
   `UU+XU+UY` seams.

#### Proof

Equations (4.1)--(4.2) give

\[
 \sum u_j=W-c,\qquad \sum x_j=\sum y_j=c(m+1)-W=W.
\]

The block length simplifies to
`(a_j-1)+2(m+1-a_j)+a_j=2m+1`.  The two positive-run lengths are
`a_j+x_j=a_j+y_j=m+1`.  Finally,

\[
 \sum(a_j-1)=\sum(y_j-1)=\sum(x_j-1)=W-c,
\]

and `sum(u_j-1)=W-2c`; adding the `c` cross seams of each displayed type
gives (4.4).  \(\square\)

This is a status/count construction, not a physical theorem.  It does not
assign the required distinct Johnson intersection colours, choose the
`U` occurrence transversal, preserve the upper tower, connect a path, or
produce a trace-guarded compiler matching.

It does explain the density mismatch.  There are

\[
 c=\Theta(W/m)=\Theta(W/d^2)                                    \tag{4.5}
\]

supercollars, each with `Theta(m)` seam dependence, and their total seam
mass is `Theta(W)`.  Splitting one supercollar into `O(d)`-span pieces makes
`Theta(m/d)=Theta(d)` adjacent pieces share its AA colour state.  Those
pieces are one correlated superpacket, not independent tasks with separate
quadratic menus.

This also explains why the earlier scalar density calculation looked
exact.  On a no-jump step put `d=d(k)=d(k+2)`.  The Pascal deletion bank
has size

\[
                 D_{\rm del}=dc+3{d+1\choose2}
                    =\left({\pi\over2}+o(1)\right){W\over d}.    \tag{4.6}
\]

The tempting `Theta(W/d)` microcollars have the same order, but they are
grouped `Theta(d)` at a time inside only `c=Theta(W/d^2)` supercollars.
The density identity counts local pressure; it does not make those local
choices independent.

Consequently the prior Haxell instantiation loses its automatic asymptotic
slack: at `D_macro=Theta(m)`, both a putative list size and the generic
`m D_macro` conflict row are `Theta(m^2)`.  A positive theorem now needs
sharp constants or a stronger dispersed/protected-energy construction.
Conditionally, the Catalan-scale extraction at `D_macro=m` would have the
right reservoir order `Omega(W/m)=Omega(c)`; prescribed eligibility and
physical realization remain the missing rows.

## 5. Compressed OR decks do not restore a quadratic fixed-slot menu

The coverage-level replacement theorem requires only

\[
 \mathcal P(X)\subseteq\mathcal P(Y),\quad
 \mathcal S(X)\subseteq\mathcal S(Y),\quad
 \mathcal I(X)\subseteq\mathcal I(Y),\quad
 \operatorname {OR}(X)=\operatorname {OR}(Y).                   \tag{5.1}
\]

The following bound uses only the final equality.

### Theorem 5.1 (fixed-slot outside-column bound)

Let the fixed off collar `X` be a length-`h` Johnson word beginning at
owner `C`.  Let standard candidates `Y_(b,c)` be indexed by at most `m`
choices of `b` and by an outside label `c notin C`, and suppose each
candidate contains its selected `c`.  If `OR(Y_(b,c))=OR(X)`, then

\[
                 \#\{\text{safe standard }(b,c)\}
                 \le m\,|\operatorname {OR}(X)-C|
                 \le m(h-1).                                    \tag{5.2}
\]

With two suspended-ECO orientations the right side is `2m(h-1)`.

#### Proof

Every safe `c` belongs to `OR(X)-C`.  A Johnson word beginning at `C`
introduces at most one previously unseen coordinate at each of its `h-1`
transitions.  Thus at most `h-1` outside columns occur, and each has at most
`m` choices of `b`.  \(\square\)

For `h=O(d)=o(m)`, (5.2) is `o(m^2)`.  Chaining `O(d)` raw atoms inside one
fixed `O(d)` slot does not evade the theorem if the advertised diversity is
still the standard outside-column `c`.

There is a sharper raw-C6 statement.  Put

\[
 Z_{b,c}=(C,C+a,C-b+a,C-b+a+c,C-b+c,C+c).                        \tag{5.3}
\]

Assume `b,b_0 in C`; assume `a,c_0` lie outside `C` and are distinct; and
take every candidate `c`, including `c_0`, from one bank outside
`C union {a}`.  Relative to `Z_(b0,c0)`, equality of total OR already
forces `c=c0`.
The old singleton `C-b0+c0` belongs to `I(Z_(b0,c0))`.  Every interval of
length at least two in a candidate has rank greater than `|C|`, and the
candidate's only rank-`|C|` singleton equal to the old value is
`C-b+c`, which forces `b=b0`.  Hence:

### Corollary 5.2 (raw anchored C6)

Under (5.1), exactly one of the `m^2` raw pairs is safe:

\[
                              (b,c)=(b_0,c_0).                    \tag{5.4}
\]

The formal quadratic suspended-ECO count has a related planting issue: in
one fixed off matching, fixing `b` and an orientation fixes the first off
atom's lower resource; its matched upper then determines `c`.  Thus the
formal relabelled atlas is not a quadratic eligible menu on one fixed host.

The exact twelve-owner ECO core escapes the raw-C6 singleton argument, but
supplies only constant many realizations for one fixed label set.  Its
retained interiors remain a real gate: the authenticated fourteen-owner
detour has zero compressed-deck-valid comparisons in either direction
among all `28*28=784` cut/orientation pairs.  This is a literal fixture, not
a universal ECO no-go.

There is also a separate obstruction to using only the positive fixed-4
deck-neutral atom.  For one binary coordinate trace, let `N` be its number
of ones, `A` the number of adjacent pairs whose OR is one, `T` the number of
transitions, and `e_1,e_h` its endpoint bits.  Then identically

\[
 T=2A-(2N-e_1-e_h),\qquad
 R={T+e_1+e_h\over2},                                             \tag{5.5}
\]

where `R` is the number of positive runs.  The fixed-4 atom preserves the
graded length-one and length-two OR multiplicities and its endpoint bits,
so it preserves `N,A,R` for every coordinate.  Any chain of such atoms with
unchanged inter-atom boundary bits therefore preserves the canonical run
count `W` and cannot perform the reset to at most `floor(2W/D_*)` runs.  The
twelve-owner ECO atom changes OR multiplicities and is not covered by this
run invariant; its obstruction is instead the fixed-host/list quantifier
above.

## 6. `K15 -> K17` calibration

For `m=8`,

\[
 W=6435,\qquad c=1430,\qquad D_*=4.                              \tag{6.1}
\]

The canonical newborn bank has `12870` length-two atoms, and (2.3) gives

\[
                         s_{\rm all}\ge6436.                     \tag{6.2}
\]

Even the optimistic grouping into `q=d'=3` residence blocks has

\[
                         6435/3=2145
\]

`A`-blocks, hence leaves at least

\[
                         2145-1430=715                            \tag{6.3}
\]

both-new lower-`q1` colours.  The balanced status skeleton instead has
`1430` blocks of length `17`, with `A`-sizes `4` and `5` (715 of each).

This calibration is independent of the stronger fixed-parent occurrence
obstruction: that parent also has `1425` old-coordinate length-four runs,
including its authenticated immutable/correlated subbanks.  The present
theorem says that even a hypothetical solution of those old-coordinate
choices would not make independent `O(d)` full-reset collars exact.

## 7. Exact surviving target

The conditional density-matched selector theorem remains logically valid;
its intended canonical `D_macro=d` realization does not.  The shortest live
replacement is:

> Construct a Johnson-labelled version of the `c` balanced supercollars,
> or a different global Catalan `A/U` braid, with all four immediate-lower
> palettes exact, the complete upper tower deck-dominant, one physical path
> topology, residence boundary state, and one trace-guarded common compiler
> basis.  Only after that global `Omega(W)` rethread is installed may local
> `O(d)` packets be treated independently.

Candidate-dependent off slots, an `Omega(m)` preloaded halo, or a
nonstandard atlas whose diversity is not an outside-column label are not
ruled out by Theorem 5.1.  None currently supplies the complete protected
interface.

## 8. Audit

Run

```text
python3 scratch/audit_o1_pascal_residence_batching_catalan_supercollar_20260801.py
```

The audit checks:

* all binomial/Catalan/status identities for `2<=m<=64`;
* the endpoint-time trace batching construction through `D_*=12`;
* the raw-C6 compressed-deck safe set for `2<=m<=9`;
* the binary length-one/length-two OR run identity through length `12`;
* the exact `K15 -> K17` numbers; and
* the frozen fourteen-owner retained-detour result `0/784` in both
  directions.

Its output is

```text
scratch/o1_pascal_residence_batching_catalan_supercollar_20260801.audit.json
```

No all-`m` physical supercollar, no unconditional `B(k)+O(1)` theorem, and
no compiler or upper-tower construction is claimed.
