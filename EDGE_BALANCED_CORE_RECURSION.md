# Edge-balanced triangular cores: the exact multiset recursion and the ordering obstruction

## 0. Status ledger

### Proved in this note

* The triangular alphabet is `E(K_(S+1))` plus one loop, and strict targets
  are ordered Ferrers rectangles in that edge set.
* The low fold misses exactly the new first-column edges.
* At the multiset level, the edge-balanced size and one-hole profile recurse
  with no waste.
* A valid core must repeat `P_1` or `E_(2,1)`.
* If `P_1` is unique, all diagonals `D_1,...,D_(S-3)` must repeat.
* The occurring star labels form a vertex cover of `1-2-...-S` containing
  vertex one; consequently every edge-balanced core with `S>=7` repeats
  `P_1`.
* A parity-decorated first-column corridor covers every height-one target
  with the minimum possible number `ceil(S/2)` of star labels.
* The observed lean multiplicity profile has an exact order-free reset under
  the fold.  The reset profile itself is impossible to order once the output
  parameter is at least five; it is an algebraic identity, not a recurrence
  of valid cores.

### Certified finite bases

Edge-balanced completion cores are explicitly certified for `S=3,4,5` in
`LINEAR_TRIANGULAR_FOLD_BRAID.md`.  They imply the verified `R=6` word with
five repeats.  No core is claimed for `S>=6`.

### Conjectural

* Edge-balanced cores exist for every `S`.
* A corrected portal trade carrying a second `P_1` can be implemented by an
  interval-preserving edge braid, while separately covering the targets
  with `u=1,x>=2` that are not transported from a strict lower core.
* A Walecki, terrace, Skolem, or parity rotation system supplies that braid.
* Therefore `rho(R)<=R-1`.

None of these four statements is used as a theorem below.  The exact missing
step is the corrected ordering lemma in Section 9, not edge enumeration or
counting.

## 1. Edge-language formulation

Identify

\[
                         E_{s,y}=(s,y)
 \quad\longleftrightarrow\quad
                         \{y,s\}\in E(K_{S+1}),       \tag{1.1}
\]

on vertices `0,1,...,S`, and identify `P_0` with a loop at zero.  For an
ordinary edge `e={a,b}`, `a<b`, write

\[
                         \ell(e)=a,\qquad h(e)=b.      \tag{1.2}
\]

Then a strict-positive target is the Ferrers rectangle

\[
 \mathcal F(u,r,x)=
 \{e:u\le h(e)\le r,\ 0\le\ell(e)\le x\},            \tag{1.3}
\]

with

\[
                         1\le u<r\le S,
                         \qquad1\le x<r.              \tag{1.4}
\]

A contiguous edge interval represents the target exactly when it stays in
`F(u,r,x)` and touches all four sides:

\[
 \min h=u,\quad\max h=r,\quad
 \min\ell=0,\quad\max\ell=x.                         \tag{1.5}
\]

A perfect terminal suffix fan is a nested family of suffixes with extrema

\[
                         [0,x+1]\times[0,x],
                         \qquad1\le x<S.              \tag{1.6}
\]

In diagonal-normalized form, the height-`x` suffix begins at

\[
                         D_x=\{x,x+1\}.               \tag{1.7}
\]

Thus the core problem is an edge-word problem on `K_(S+1)`, but not an
ordinary Euler-tour problem: consecutive letters need not share a vertex,
and the order on vertex labels is essential through (1.3).

## 2. Edge-balanced cores

Call a word `V_S` **edge-balanced** when it is an `(S+1)`-completion core in
the sense of `LINEAR_TRIANGULAR_FOLD_BRAID.md`, has one top-row hole, and

\[
                         |V_S|=\binom{S+1}{2}.         \tag{2.1}
\]

There are

\[
                         \binom S2                    \tag{2.2}
\]

nonpeak edges (edges not incident with zero).  Omitting one of them and
including the terminal loop consumes

\[
                         \binom S2                    \tag{2.3}
\]

positions.  Therefore exactly `S` positions remain for star-edge portals or
repeated nonstar edges.  Equivalently, the core excess is exactly

\[
                         \kappa(V_S,H_S)=S.            \tag{2.4}
\]

The certified words `V_3,V_4,V_5` have this form.  In each, one of the `S`
portal positions is a repeated edge `{1,2}` and the other `S-1` are star
edges, but that finer multiplicity pattern is not required by the
definition.

Call a core **star-complete** when its `S` portal positions are exactly one
copy of every nonzero star edge `{0,1},...,{0,S}`.  Star-completeness is a
useful stronger target, not part of the proved core examples `V_4,V_5`.

By the core-completion theorem, edge-balanced cores for all `S` would give

\[
                         \rho(R)\le R-1.               \tag{2.5}
\]

## 3. The low fold is an exact edge-set embedding

Define

\[
 \iota_S(\{0,a\})=\{0,a+1\},\qquad
 \iota_S(\{a,b\})=\{a+1,b+1\}\quad(1\le a<b\le S),  \tag{3.1}
\]

and send the loop at zero to the star edge `{0,1}`.  This is exactly the
low lift `lambda_(S+1)`.

### Lemma 1 (exact complement of the low-fold image)

Among ordinary edges of `K_(S+2)`, the edges not in the image of (3.1) are
exactly

\[
                         C_j=\{1,j\},
                         \qquad2\le j\le S+1.         \tag{3.2}
\]

#### Proof

An upper edge incident with zero is `{0,j}`.  For `j>=1` it is the image of
the lower star `{0,j-1}`, with the loop supplying `j=1`.

An upper edge not incident with zero has lower endpoint at least one.  If
that endpoint is at least two, subtracting one from both endpoints gives a
unique lower nonstar edge.  The only remaining possibility is lower endpoint
one, giving exactly (3.2).  QED.

The missing edges (3.2) are precisely the first-column arm cells
`E_(j,1)`.

## 4. The multiset induction is exact

Suppose `V_S` is edge-balanced and its unique omitted nonpeak edge is

\[
                         H_S=\{a,S\},
                         \qquad1\le a<S.              \tag{4.1}
\]

Apply `iota_S` occurrence by occurrence, insert each first-column edge
`C_2,...,C_(S+1)` once, and insert one new terminal loop.

### Theorem 2 (order-free edge-balanced lift)

The resulting multiset has exactly

\[
                         \binom{S+2}{2}               \tag{4.2}
\]

occurrences.  It contains every nonpeak edge of `K_(S+2)` except the one
top-row hole

\[
                         H_{S+1}=\{a+1,S+1\}.          \tag{4.3}
\]

Thus it has exactly the multiset cardinality and spanning profile required
of an edge-balanced `V_(S+1)`.

#### Proof

The old word contributes `binom(S+1,2)` occurrences.  There are `S` new
first-column edges and one loop, so the total is

\[
 \binom{S+1}{2}+S+1=\binom{S+2}{2}.                  \tag{4.4}
\]

By Lemma 1, the image of all old nonpeak edges together with (3.2) is every
new nonpeak edge, except that the omitted old edge (4.1) maps to (4.3).
Multiplicity of old portal occurrences is simply transported and the new
loop occupies the one remaining portal position.  QED.

This is the decisive counting fact: **no new repeated occurrence is needed
at the multiset level.**  The `S` new first-column cells are compulsory new
letters, and the loop is the single new portal slot allowed by the exact
edge count.

Consequently the edge-balanced conjecture is purely an ordering theorem.

### Theorem 3 (a low portal must be duplicated)

For every `S>=4`, an edge-balanced core with a perfect suffix fan and all
strict-positive targets must repeat at least one of

\[
                         P_1=\{0,1\},
                         \qquad E_{2,1}=\{1,2\}.       \tag{4.5}
\]

In particular, a star-complete core (which has every star and every present
nonpeak exactly once) is impossible for `S>=4`.

#### Proof

Choose the height-two suffix.  Its box is

\[
                         [0,3]\times[0,2].             \tag{4.6}
\]

To attain lower endpoint two while keeping high endpoint at most three, it
contains an occurrence of

\[
                         E_{3,2}=\{2,3\}.              \tag{4.7}
\]

Call this required occurrence of `E_(3,2)` the height-two barrier.  Every
occurrence with high endpoint `S>3` lies before the beginning of the
height-two suffix, and hence before that barrier.

The height-one suffix has box `[0,2]x[0,1]`.  It contains an occurrence of
`E_(2,1)`, and this occurrence lies after the height-two barrier; its suffix
cannot contain (4.7), because its lower maximum is only one.

Now consider the two strict targets

\[
 [1,2]\times[0,1],
 \qquad
 [1,S]\times[0,1].                                   \tag{4.8}
\]

The first target requires occurrences of both `P_1` (the only letter with
high endpoint one) and `E_(2,1)` (the only height-one letter with high
endpoint at most two) in one clean height-one interval.

The second target also requires `P_1`, and it requires some occurrence with
high endpoint `S`.  Every such occurrence is before the height-two barrier.

If `P_1` occurs only once, the second target forces it to occur before the
barrier.  The first target then needs an occurrence of `E_(2,1)` before the
barrier as well.  But the height-one suffix already needs one after the
barrier, so `E_(2,1)` is repeated.  Otherwise `P_1` itself is repeated.
QED.

This theorem explains the repeated low portal in all certified cores:
`V_4` repeats `E_(2,1)`, while `V_5` repeats both `E_(2,1)` and `P_1`.
It also corrects the most naive Walecki target.  The useful inductive
multiset must deliberately trade at least one star label for a repeated low
portal; it cannot simply be “all complete-graph edges once, minus the top
hole, plus the loop.”

Call the observed multiplicity pattern **lean** when it consists of:

* every nonpeak edge once except one top-row hole;
* one additional copy of `E_(2,1)`;
* exactly `S-1` nonzero-star occurrences (labels may repeat);
* one loop `P_0`.

These counts sum to `binom(S+1,2)`.

### Theorem 4 (the lean profile has an exact reset identity)

Apply the order-free lift of Theorem 2 to a lean `S`-multiset.  Its repeated
`E_(2,1)` becomes a repeated `E_(3,2)`.  Delete that extra copy of
`E_(3,2)` and add one extra copy of the newly inserted `E_(2,1)`.
The resulting `(S+1)`-multiset is lean, has the shifted top-row hole, and has
the same total size.

#### Proof

The low fold shifts every nonstar endpoint by one, so the sole extra
`{1,2}` becomes an extra `{2,3}`.  All first-column edges, including the new
base `{1,2}`, are inserted once by Theorem 2.  Exchanging only the *extra*
`{2,3}` for an extra `{1,2}` preserves one base occurrence of every required
nonpeak and preserves total length.

The `S-1` old nonzero-star occurrences shift upward, while the old loop maps
to one additional nonzero star `{0,1}`.  Hence the new word has `S`
nonzero-star occurrences, exactly `(S+1)-1`.  The new loop and shifted hole
are unchanged.  QED.

The reset is forced in spirit by Theorem 3: without a trade, the naive lifted
profile has only one `P_1` and one `E_(2,1)`, so it cannot be ordered as a
valid core.  The algebraic lean trade is

\[
                         E_{3,2}^{\rm extra}
                         \longrightarrow
                         E_{2,1}^{\rm extra}.          \tag{4.9}
\]

However, the reset output has unique `P_1` and repeats only `D_1=E_(2,1)`.
For output parameter at least five, Theorem 5 below forces both `D_1` and
`D_2` to repeat whenever `P_1` is unique.  Consequently no ordering of the
lean-reset multiset is a valid core in that range.  A viable recursion must
make a different trade, such as redirecting the shifted extra diagonal to a
second `P_1`.

### Theorem 5 (nested-barrier hierarchy)

Let `S>=4`.  If `P_1` occurs only once in a valid edge-balanced core, then
every diagonal

\[
                         D_y=E_{y+1,y},
                         \qquad1\le y\le S-3           \tag{4.10}
\]

occurs at least twice.

#### Proof

Fix `y<=S-3`.  Let `F_(y+1)` be the perfect suffix of height `y+1`.  It
contains a diagonal occurrence

\[
                         D_{y+1}=E_{y+2,y+1},          \tag{4.11}
\]

because this is the only cell simultaneously attaining lower endpoint
`y+1` while keeping high endpoint at most `y+2`.  Call this occurrence `q`.

Every high-`S` occurrence lies before the beginning of `F_(y+1)`, since
`S>y+2`, and hence lies before `q`.  The target

\[
                         [1,S]\times[0,y]              \tag{4.12}
\]

requires `P_1` and a high-`S` occurrence in a word interval containing no
lower endpoint above `y`.  It cannot cross `q`.  If `P_1` is unique, it is
therefore before `q`.

Now the target

\[
                         [1,y+1]\times[0,y]            \tag{4.13}
\]

requires `P_1` and an occurrence of `D_y`; the latter is the only cell with
lower endpoint `y` and high endpoint at most `y+1`.  Its witness also cannot
cross `q`, so it uses an occurrence of `D_y` before `q`.

On the other hand, the perfect suffix `F_y` contains an occurrence of
`D_y`.  Since `F_y` has lower maximum `y`, it cannot contain `q`; as both
are suffixes ending at the same final position, `F_y` starts after `q`.
Thus a second `D_y` occurs after `q`.  QED.

For `S=4`, this forces the repeated `E_(2,1)` seen in `V_4`.  For larger
`S`, keeping `P_1` unique consumes at least `S-3` portal slots on repeated
diagonals.  A single extra `P_1` can in principle cross all these nested
barriers simultaneously, explaining why `V_5` changes regime and repeats
`P_1`.

This gives a concrete multiplicity design rule for any recurrence: either
carry two strategically placed `P_1` occurrences, or budget a linearly long
ladder of repeated low diagonals.  A rotational edge enumeration that does
neither cannot be a completion core.

### Lemma 6 (star labels form a path vertex cover)

Let `A` be the set of labels `j` for which the core contains an occurrence
of the star `P_j`.  Then

\[
                         1\in A,\qquad
                         |A|\ge\lceil S/2\rceil.       \tag{4.14}
\]

#### Proof

For every `r=2,...,S`, the strict target

\[
                         [r-1,r]\times[0,1]            \tag{4.15}
\]

needs a height-zero letter whose high endpoint belongs to `{r-1,r}`.
Therefore `A` meets every edge of the path

\[
                         1-2-\cdots-S.                 \tag{4.16}
\]

The target `[1,2]x[0,1]` also forces `P_1`, so `1 in A`.  A vertex cover of
this path constrained to contain vertex one has minimum size `ceil(S/2)`.
QED.

### Corollary 7 (two `P_1` portals are eventually forced)

Every edge-balanced core with `S>=7` contains at least two occurrences of
`P_1`.

#### Proof

If `P_1` were unique, Theorem 5 would consume at least `S-3` of the `S`
portal positions on repeated nonpeak diagonals.  Lemma 6 consumes at least
`ceil(S/2)` further positions on star occurrences.  For `S>=7`,

\[
                         S-3+\lceil S/2\rceil>S,       \tag{4.17}
\]

contradicting the exact portal budget.  QED.

Thus the asymptotic recurrence has no genuine choice between the two regimes:
it must carry a second `P_1`.  The remaining star labels must still form a
path vertex cover, suggesting that an alternating-parity star set—not all
stars as in the naive corridor—is the correct Walecki/terrace skeleton.

If the lower core is star-complete, then the lifted multiset is again
star-complete: the old loop supplies `{0,1}`, and the old nonzero stars shift
to `{0,2},...,{0,S+1}`.  For a general edge-balanced core, some of these star
labels may instead be replaced by repeated nonstar portals.

## 5. Target coverage also folds exactly above height one

If a lower interval represents `[u,r]x[0,x]` with `x>=1`, applying (3.1)
to its letters represents

\[
                         [u+1,r+1]\times[0,x+1].       \tag{5.1}
\]

Indeed, a lower peak maps to a new peak and every positive lower endpoint
increases by one.  Since a completion core supplies lower targets only for
`u>=1`, the low-fold word inherits upper strict targets with
`u>=2,x>=2`.  It does **not** automatically cover the upper family
`u=1,x>=2`; those targets correspond to lower boundary targets with `u=0`,
which are not part of the core definition.

The missing height-one targets *would* all be represented by the single
alternating edge corridor

\[
 \mathcal X_{S+1}=
 C_{S+1},\{0,S\},C_S,\{0,S-1\},\ldots,C_2,\{0,1\}.
                                                               \tag{5.2}
\]

For `[u,r]x[0,1]`, start at `C_r={1,r}` and stop at the star `{0,u}`.

The new column edges are always present.  The required star labels are
automatically present only under the stronger star-complete hypothesis.  A
general edge-balanced induction must either preserve star-completeness or
replace (5.2) by a noncanonical height-one corridor using its available
portal multiset.

In fact all stars are unnecessary.  Let

\[
                         A_S=\{j\le S:j\text{ is odd}\}. \tag{5.3}
\]

Define the parity corridor by scanning `s=S,S-1,...,2`, outputting
`E_(s,1)` and then `P_s` when `s` is odd, and finally outputting `P_1`.

### Lemma 8 (optimal star-sparse height-one corridor)

The parity corridor covers every strict target of height one.  It uses every
first-column edge once and exactly

\[
                         \lceil S/2\rceil              \tag{5.4}
\]

star occurrences.  No height-one corridor can use fewer distinct star
labels while also supplying the mandatory label `P_1`.

#### Proof

For `[u,r]x[0,1]`, start at `E_(r,1)` and scan downward.  Every integer
interval `[u,r]` of length at least two contains an odd label.  If an odd
star occurs before reaching row `u`, stop at `E_(u,1)` (or continue safely
within row `u`).  If the only odd label is `u`, continue through `P_u`.  For
`u=1`, stop at the terminal `P_1`.  The scanned high endpoints stay in
`[u,r]`, a first-column edge supplies height one, and an odd star supplies
height zero.

There are `ceil(S/2)` odd labels.  Optimality follows from Lemma 6: the star
labels form a vertex cover of the path `1-2-...-S`.  When `S` is even, a
minimum cover containing vertex one has size `S/2`; when `S` is odd, every
cover containing vertex one has size at least `(S+1)/2`.  QED.

Combining Corollary 7 with Lemma 8 suggests the asymptotic portal profile:

* one parity vertex cover of star labels;
* a second, late occurrence of `P_1` beyond the diagonal barriers;
* the remaining roughly `S/2-1` portal slots used for repeated nonpeak
  absorbers.

This is the first profile compatible simultaneously with the exact `S`-slot
budget, the height-one corridor, and the nested suffix obstruction.  It is a
more plausible terrace skeleton than the all-star corridor (5.2), although
coverage of heights at least two is still unproved.

Thus an inductive ordering has only three jobs:

1. retain the old low-fold witnesses, which cover `u>=2,x>=2`;
2. construct the missing strict family `u=1,x>=2`;
3. ensure the necessary star labels (or substitute portal providers) and
   thread the new first-column letters so that (5.2), or an equivalent clean
   corridor, exists;
4. preserve the nested terminal suffix fan.

The raw multiset of Theorem 2 is itself ruled out by Theorem 3, so these jobs
must be performed after a valid multiplicity trade.

## 6. Suffix compatibility is local and automatic

Write a diagonal-normalized suffix fan as

\[
 D_{S-1}B_{S-1}D_{S-2}B_{S-2}\cdots D_1B_1P_0.       \tag{6.1}
\]

The low fold sends `D_x` to `D_(x+1)`.  Appending the new loop changes the
folded suffix box

\[
                         [1,x+1]\times[0,x]
\]

to the desired

\[
                         [0,x+1]\times[0,x].          \tag{6.2}
\]

The new first-column edge `C_(x+1)={1,x+1}` and star edge `{0,x}` both lie
inside this box.  More generally, any letter from

\[
                         [0,x+1]\times[0,x]            \tag{6.3}
\]

may be placed in shell `B_x` without changing any suffix extrema: smaller
suffixes start later, while larger suffixes contain (6.3).

Hence, whenever the indicated star occurrence is available (in particular
for a star-complete multiset), every pair

\[
                         C_{x+1},\{0,x\}               \tag{6.4}
\]

has a natural safe shell.  The suffix fan imposes no global Hall-type
obstruction to inserting the new column.

## 7. The exact obstruction: shell safety versus corridor continuity

Under the star-complete specialization, if the pairs (6.4) are placed in
their natural successive shells, the old
diagonal starts

\[
                         D_{x-1}=\{x-1,x\}             \tag{7.1}
\]

lie between consecutive pairs.  Their lower endpoint is `x-1>1` for
`x>2`, so they contaminate a height-one target.  Conversely, moving all
pairs together to form the clean corridor (5.2) can place a high first-
column edge inside a smaller suffix or inside an inherited low-fold witness.

This is the precise braid conflict:

\[
 \boxed{
 \text{local shell safety}
 \quad\text{versus}\quad
 \text{global height-one corridor continuity}.}
                                                               \tag{7.2}
\]

An all-`S` proof needs a sequence of interval-preserving switches that moves
the shell-local pairs into one corridor, or it needs a different family of
height-one witnesses that can cross the diagonal separators without actually
including them.

The latter cannot mean literal inclusion: every height-one witness contains
only edges with lower endpoint zero or one.  It must instead use duplicated
portal occurrences already present in the `S` allowed portal slots.

## 8. Why a bare Walecki or terrace construction is not yet a proof

Walecki decompositions, rotational terraces, and Skolem-type schedules are
natural candidates because they order all edges of a complete graph and can
place prescribed star/column pairs in regular rounds.  They solve the
**enumeration** part of Theorem 2.

They do not automatically solve (1.3)--(1.5).  The Ferrers target family is
defined by the *linear* order

\[
                         0<1<\cdots<S,                 \tag{8.1}
\]

not by the cyclic group structure used in a rotational terrace.  Translating
an edge modulo `S+1` can wrap its endpoints across zero and changes both its
low and high coordinates discontinuously.  Therefore coverage of one
Ferrers rectangle does not translate to coverage of another.

Likewise, an Euler or Hamilton edge trail controls shared graph vertices,
whereas a clean interval here is controlled by four numerical extrema.
Consecutive edge incidence is neither necessary nor sufficient.

The precise extra lemma a Walecki/terrace proposal must prove is:

> after cutting and linearly labelling the rotational edge schedule, every
> Ferrers box (1.3) has a contiguous segment touching all four sides, and the
> terminal segments form (1.6).

No such lemma is presently known.  Quoting complete-graph decompositions
without this order-compatibility statement leaves the central problem
untouched.

## 9. A corrected inductive theorem sufficient for completion

The raw multiset from Theorem 2 cannot satisfy the old edge-braid lemma: it
has unique `P_1` and unique `E_(2,1)`, contradicting Theorem 3.  The lean
reset from Theorem 4 also fails from output parameter five onward.  Moreover,
transported strict witnesses cover only `u>=2,x>=2` and leave the whole
family `u=1,x>=2` untreated.

A proof-grade recurrence sufficient for completion must therefore say:

> **Corrected edge-braid target.**  From an edge-balanced core `V_S`, choose
> an upper edge-balanced multiset—not necessarily the raw lift—such that it
> contains every upper nonpeak except one top-row hole, one terminal loop,
> and portal multiplicities satisfying Theorems 3, 5, and Corollary 7.  Order
> it so that:
>
> * every transported lower strict witness survives;
> * every upper target with `u=1,x>=2` occurs;
> * every height-one strict target occurs; and
> * the word ends in a diagonal-normalized suffix fan.

If this corrected target can be met at the exact edge-balanced size, it
inducts from a certified base and proves

\[
                         \rho(R)\le R-1.              \tag{9.1}
\]

No such ordering theorem is presently proved.  Theorem 2 supplies a
no-waste edge inventory before the necessary portal trade; Sections 6 and 7
isolate suffix-shell safety and corridor continuity, but the missing
`u=1` family is an additional independent braid condition.  The corrected
statement remains substantially sharper than arbitrary-word search while
making every unresolved condition explicit.
