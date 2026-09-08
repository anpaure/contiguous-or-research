# Coatom-screen versus atom-gap tensors: exact OR/AND deck duality and the boundary obstruction

> **Scope correction (2026-08-01).** This note audits the older raw
> all-lower-screen tensor, whose four screen-owner repetitions are not
> removed.  Its simultaneous internal OR/AND-deck conclusions do **not**
> apply to the authoritative zero-defect mixed-screen tensor.  For the
> canonical mixed schedule, the owner repetitions disappear but internal
> AND transparency fails; see
> `MATH_AUDIT_A_MIXED_COATOM_SCREEN_COMPLEMENT_GAP_AND_U5_20260801.md`.

Date: 2026-08-01  
Lane: A, dimension-uniform `B(k)+O(1)` upper/lower interface  
Status: exact theorem and exact counterexample for the raw all-lower-screen
face only; superseded as a description of the zero-defect packet.  No
all-dimension carrier or additive-constant bound is claimed.

## 0. Verdict

The coatom-screen tensor is stronger internally, and weaker at its boundary,
than its original OR proof records.

* It preserves the distinct internal **OR and AND** decks.
* It preserves the prefix/suffix OR chains, but it does not even preserve the
  compressed prefix/suffix AND decks in either direction.
* Its literal complement is an **atom-gap tensor**.  This dual tensor
  preserves the prefix/suffix AND chains and both internal decks, but it
  fails the compressed prefix/suffix OR decks.
* The direct tensor has all internal positive runs of length at least
  `d+2`, but has singleton filler gaps.  The dual tensor has all internal
  zero-runs of length at least `d+2`, but has singleton filler one-runs.

Thus the same local tensor supplies either the direct OR/residence interface
or the complementary AND/gap interface.  It does **not** supply a simultaneous
OR+AND, run+gap birail interface.  The missing datum is exactly a two-sided
boundary-deck profile (and, on proper cycles, its two-ended version), not an
internal-shadow defect.

## 1. The AND-deck replacement theorem

Fix a finite universe `Omega`.  For a nonempty word
`X=(X_1,...,X_h)` put

\[
\begin{aligned}
 {\cal P}_\cap(X)&=\{X_1\cap\cdots\cap X_j:1\le j\le h\},\\
 {\cal S}_\cap(X)&=\{X_j\cap\cdots\cap X_h:1\le j\le h\},\\
 {\cal I}_\cap(X)&=\{X_i\cap\cdots\cap X_j:1\le i\le j\le h\},\\
 T_\cap(X)&=\bigcap_{i=1}^h X_i.
\end{aligned}                                                   \tag{1.1}
\]

### Theorem 1.1 (linear AND transparency)

If

\[
 {\cal P}_\cap(X)\subseteq{\cal P}_\cap(Y),\qquad
 {\cal S}_\cap(X)\subseteq{\cal S}_\cap(Y),\qquad
 {\cal I}_\cap(X)\subseteq{\cal I}_\cap(Y),\qquad
 T_\cap(X)=T_\cap(Y),                                         \tag{1.2}
\]

then replacing `X` by `Y` in any linear exterior context preserves every
old contiguous interval-intersection value.

#### Proof

An old interval is disjoint from the slot, internal to the slot, crosses
only its left boundary, crosses only its right boundary, or crosses both.
The corresponding slot contribution is respectively unchanged, a member of
`I_cap(X)`, a member of `P_cap(X)`, a member of `S_cap(X)`, or `T_cap(X)`.
Use (1.2) in the four nontrivial cases.  Intersecting the chosen new slot
value with the unchanged exterior contribution reproduces the old value.
\(\square\)

This is exactly the complement dual of compressed OR-deck transparency:

\[
 \bigcap_{i\in J}X_i
 =\Omega\setminus\bigcup_{i\in J}(\Omega\setminus X_i).        \tag{1.3}
\]

Consequently simultaneous preservation of all old interval ORs and ANDs is
obtained by imposing the four OR conditions on `X -> Y` and the four AND
conditions (1.2).  Neither group implies the other.

### Proper cyclic form

Put `P^cap_0(X)=S^cap_(h+1)(X)=Omega`.  If full-cycle intervals are
excluded, separate prefix and suffix AND decks are insufficient.  The
additional context-independent deck is

\[
 {\cal J}^{\circ}_\cap(X)=
 \{P_i^\cap(X)\cap S_j^\cap(X):
        0\le i\le h,\ 1\le j\le h+1,\ i+1<j\}.                 \tag{1.4}
\]

The strict inequality records a nonempty omitted slot gap.  Inclusion
`J^o_cap(X) subseteq J^o_cap(Y)`, together with (1.2), is sufficient for
every proper cyclic exterior.  If the full cycle is admitted, separate
prefix/suffix decks suffice: when chosen new prefix and suffix witnesses
overlap or abut, their intersection is `T_cap(Y)=T_cap(X)` and the full
cycle realizes the value.

Strict separation is necessary.  In
`Omega={a,b,c,e}`, take

```text
X = ce, ace, abe,       Y = bce, ace, abe,       exterior = abc.
```

These are the complements of the standard OR-deck counterexample.  They
satisfy all four linear AND conditions, including the weak two-ended test
that permits abutting pieces.  The old proper wrap interval

\[
                    abe,abc,ce
\]

has intersection `empty`.  Every proper interval in the new four-cell
cycle has nonempty intersection; only the forbidden full cycle has empty
intersection.  The strict deck (1.4) detects the loss.

## 2. Exact internal AND decomposition of the coatom-screen tensor

Let `A` be an active universe, let
`V=(V_0,...,V_(t-1))` be a constant-rank Johnson word on `A`, and write

\[
                         I_j=V_j\cap V_{j+1}.                   \tag{2.1}
\]

Let `F={f_0,...,f_(n-1)}`, with `n>=2`, be disjoint from `A` and a fixed
core `K`, and put `C_i=F-{f_i}`.  The coatom-screen expansion is

\[
 B(V_0),S(I_0),B(V_1),\ldots,S(I_{t-2}),B(V_{t-1}),             \tag{2.2}
\]

where

\[
 B(V)=(K\cup V\cup C_0,\ldots,K\cup V\cup C_{n-1}),\qquad
 S(I)=K\cup I\cup F.                                           \tag{2.3}
\]

For the linear filler order define

\[
\begin{aligned}
 {\cal G}_n&=\{\varnothing,F\}\cup
     \{\{f_p,\ldots,f_q\}:0\le p\le q<n\},\\
 [p,q]_F&=\{f_p,\ldots,f_q\}.
\end{aligned}                                                   \tag{2.4}
\]

### Theorem 2.1 (internal AND tensor formula)

The distinct internal intersection deck of (2.2) is exactly

\[
\begin{aligned}
 {\cal I}_\cap(\widetilde V)= {}&
 \{K\cup V_j\cup(F\setminus[p,q]_F):
          0\le j<t,\ 0\le p\le q<n\}\\
 &\cup\{K\cup I_j\cup G:
          0\le j<t-1,\ G\in{\cal G}_n\}\\
 &\cup\{K\cup A_0:A_0\in{\cal I}_\cap(V)\}.                \tag{2.5}
\end{aligned}
\]

#### Proof

Classify an expanded interval by the number of screens it contains.

* With no screen it lies in one coatom block.  If its first and last
  coatom indices are `p,q`, its filler intersection is
  `F-[p,q]_F` and its active intersection is `V_j`.
* A singleton screen gives `I_j union F`.  An interval containing exactly
  one screen and at least one adjacent coatom letter has active intersection
  `I_j`.  Its filler intersection is a prefix, suffix, middle interval, or
  the empty set in the linear filler order.  These, together with the
  singleton screen, are exactly `G_n`.
* An interval containing at least two screens contains the whole coatom
  block between two consecutive screens.  The intersection of all coatoms
  in that block is empty on `F`, while the active part is the intersection
  of one contiguous interval of the base word.

Conversely every value in the first two displayed families is realized by
the indicated local interval.  Every base interval intersection is realized
with empty filler: use a whole block for one owner, the two whole blocks and
their screen for two owners, and the full corresponding expanded span for a
longer base interval.  This proves equality in (2.5). \(\square\)

### Corollary 2.2 (two-sided internal preservation)

Two base phases have equal expanded internal AND decks provided that they
have the same owner support, the same adjacent-intersection support, and the
same base internal AND support.  Therefore the audited ECO row-1 phases,
which have these three properties, preserve both expanded internal OR and
expanded internal AND support for every `n>=2`.

This conclusion concerns distinct support.  It says nothing about interval
multiplicities or width grading.

## 3. Boundary AND decks pass through rather than disappear

Write

\[
 A_j=\bigcap_{s=0}^jV_s,qquad
 Z_j=\bigcap_{s=j}^{t-1}V_s.                                  \tag{3.1}
\]

Direct inspection of the first and last coatom blocks gives the exact
boundary formulas

\[
\begin{aligned}
 {\cal P}_\cap(\widetilde V)
  ={}&\{K\cup V_0\cup(F\setminus\{f_0,\ldots,f_i\}):0\le i<n\}
       \cup\{K\cup A_j:0\le j<t\},\\
 {\cal S}_\cap(\widetilde V)
  ={}&\{K\cup V_{t-1}\cup(F\setminus\{f_i,\ldots,f_{n-1}\}):0\le i<n\}
       \cup\{K\cup Z_j:0\le j<t\}.                           \tag{3.2}
\end{aligned}
\]

After a complete first block the filler intersection is empty forever, so
the later prefix chain is precisely the base prefix-intersection chain;
the suffix assertion is its reversal.  In particular, when the two phases
have common first and last owners, tensoring preserves their boundary AND
decks **if and only if** their base boundary AND decks agree.

For the explicit row-1 ECO opening, suppressing `K` and writing `infinity`
as `I`, the base decks are

\[
\begin{array}{c|c|c}
 &\text{old}&\text{new}\\ \hline
 {\cal P}_\cap&\{Iab,Ib,b,\varnothing\}
               &\{Iab,Ia,a,\varnothing\}\\
 {\cal S}_\cap&\{eab,eb,e,\varnothing\}
               &\{eab,ea,e,\varnothing\}.
\end{array}                                                     \tag{3.3}
\]

Thus neither directed inclusion holds.  For example `K union {I,b}` and
`K union {b}` occur only in the old expanded prefix deck, whereas
`K union {I,a}` and `K union {a}` occur only in the new one.  Similarly
`K union {e,b}` is old-only and `K union {e,a}` is new-only on the suffix
side.  This is an exact all-`d` obstruction: increasing the filler bank
cannot repair it.

## 4. The atom-gap complement tensor

Let the ambient universe be the disjoint union

\[
                       \Omega=K\dot\cup A\dot\cup F\dot\cup L.
                                                                    \tag{4.1}
\]

Complement every letter of (2.2) in `Omega`.  The resulting tensor has
atom blocks and empty-filler gaps

\[
\begin{aligned}
 D(V)&=(L\cup(A\setminus V)\cup\{f_0\},\ldots,
         L\cup(A\setminus V)\cup\{f_{n-1}\}),\\
 G(V,W)&=L\cup\bigl(A\setminus(V\cap W)\bigr).                 \tag{4.2}
\end{aligned}
\]

### Theorem 4.1 (exact atom-gap dual)

If consecutive base owners are Johnson-adjacent, (4.2) is a constant-rank
Johnson walk.  For the two ECO phases it has

1. the same endpoints and physical multiset in both phases;
2. pointwise-equal prefix and suffix AND chains;
3. equal distinct internal AND and OR decks;
4. the same four repeated gap occurrences as the four repeated screens of
   the direct tensor; and
5. identical clipped zero-run boundary states, with every internal zero-run
   of length at least `n=d+2`.

#### Proof

Inside an atom block, consecutive letters exchange `f_i` and `f_(i+1)`.
If `V=P+x` and `W=P+y`, then

\[
 A\setminus P=(A\setminus V)\cup\{x\}
              =(A\setminus W)\cup\{y\}.                       \tag{4.3}
\]

Hence the last atom before a gap exchanges its filler atom for `x`, and the
gap exchanges `y` for the first filler atom after it.  This proves rank and
Johnson adjacency.

All remaining assertions are De Morgan duals.  Pointwise OR-boundary
equality of the direct tensor becomes pointwise AND-boundary equality.
Its internal OR equality becomes internal AND equality.  Corollary 2.2
becomes internal OR equality.  Multiplicity and endpoints are carried by the
complement bijection.  Finally, zero-runs in the dual are precisely one-runs
in the direct tensor, whose minimum and clipped boundary states were proved
by the coatom-screen residence ledger. \(\square\)

The dual tensor is not OR-transparent at its boundary: complementing (3.3)
gives old-only and new-only prefix/suffix OR values.  Thus literal
complementation moves the obstruction from the AND shore to the OR shore;
it does not remove it.

## 5. Exact residence/gap scope and the surviving gate

The direct and dual fillers give the smallest possible counterexample to
automatic bi-residence.

* In the direct tensor, `f_i` is absent exactly at the `i`-th coatom in
  every block and is present in both neighbours.  Hence it has internal
  zero-runs of length one.
* In the atom-gap tensor, `f_i` is present exactly at the `i`-th atom in
  every block and is absent in both neighbours.  Hence it has internal
  one-runs of length one.

Therefore either tensor fails a simultaneous minimum run and minimum gap
threshold as soon as that threshold is at least two.  AND/OR deck equality
does not control this state.  A birail replacement must separately export,
for every coordinate, the clipped leading/trailing one-run state and the
clipped leading/trailing zero-run state, together with internal legality for
both signs.

For a linear even/birail lift there are consequently two exact options.

1. Use the coatom tensor and atom-gap tensor on separately guarded rails,
   asking only OR transparency on the direct rail and AND transparency on
   the complementary rail; or
2. enlarge the active packet until its base phases satisfy both compressed
   prefix/suffix deck systems (and both clipped boundary states).

For a proper cyclic lift, option 2 additionally requires both separated
two-ended decks `J^o_union` and `J^o_cap`.  Merely pairing one tensor with
its complement, or proving both internal deck equalities, does not imply
these boundary conditions.

The exact remaining local theorem is therefore a **two-sided profiled
screen splitter**: remove the four repeated screen/gap occurrences while
exporting simultaneous OR and AND boundary decks, both residence signs, and
the proper two-ended decks when the carrier remains cyclic.  The present
tensor proves all internal shadow rows but not that boundary theorem.
