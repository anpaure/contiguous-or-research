# A minimal retained Hall-29 repair needs thirteen length-two/three cells

## Exact singleton-letter geometry, witness-row census, and the minimal 29-address gate

Date: 2026-07-28

Status: pure theorem and audit note.  The run-boundary theorem is
unconditional.  The thirteen-physical-nonsingleton lower bound is proved for repairs
which retain the six old Hall-29 cells and 1,489 reservations and add exactly
29 addresses.  The frozen numerical claims are direct audits of an existing
carrier, not a new search.  No `k=15` compiler is constructed.

## 0. Outcome

There are two different meanings of "singleton" which must not be
identified.

* A **physical singleton cell** is the interval `[j,j]`; its value is the
  whole source letter `A_j`, of any rank.
* A **one-coordinate letter** has `|A_j|=1`.

The exact witness census

\[
 n_1\ge3510,\qquad n_2\ge3509,\qquad n_3\ge3508
\]

counts cells of physical lengths one, two, and three.  It does **not** force
3,510 one-coordinate letters or 3,510 minimum carrier runs.

For a `d=3` Johnson carrier, every interior source letter contains two
run-boundary coordinates

\[
                         \{\alpha_j,\beta_{j-4}\}.
\]

These coordinates coalesce exactly when the carrier has an internal
minimum-length one-run of length four ending at `T_j`.  Consequently the
positions individually capable of carrying a one-coordinate letter are
exactly the eight factor boundaries together with the factor positions
indexed by the terminal carrier indices of internal length-four runs.

For a general physical singleton target occurrence `A_j=S`, the exact local
condition is instead

\[
                         F_j\subseteq S\subseteq E_j,
\]

where `F_j` is the compulsory run-boundary footprint and `E_j` is the
maximal erosion envelope.  Simultaneous occurrences obey one explicit
run-hitting condition.

Applied to the 35-target Hall-29 kernel, the rank profile forces a new
conclusion.  Its six old cells can discharge six of its 25 rank-at-least-six
targets.  Only six physical singleton positions of any `d=3` Johnson factor
have envelope rank at least six.  Hence at least

\[
                         25-6-6=13
\]

of the 29 new addresses in a minimal repair must have physical length two
or three.  A terminal-singleton-only repair is impossible for every such
carrier, independently of how many minimum four-runs it has.

On the frozen Hall-29 carrier there are 1,145 internal length-four runs, but
none of their positions is compatible with a peeled residual target.  Its
minimum-run bank exposes zero residual singleton edges in the fixed-envelope,
fixed-footprint model.

There is a second, independent finite restriction.  In controller language
the flat interior of the maximal erosion `P=E` is a rank-five Johnson path,
and a physical word is a pinning of this walk.  Restrict to positive defect-one repairs `(p,x)` for
which exactly one of the four carrier states defining `P_p` omits `x`.  The
exact sharp count is **24 UNIT controller pins**, not the 14 obtained in the
unrestricted erosion-incidence relaxation.  An old-pair-complementary
24-pin certificate exists; its 29 new cells have physical-length profile
`(7,15,7)`, so 22 are nonsingletons.  Hence the 24-pin exposure constraint
and the thirteen-cell bulk tax are simultaneously feasible before physical
chronology is imposed.  What remains is their common controller-port lift.

## 1. Exact run-boundary theorem

Let

\[
 T_1,\ldots,T_W\in\binom{[k]}r
\]

be a Johnson path, written

\[
 T_{i+1}=T_i\setminus\{\alpha_i\}\cup\{\beta_i\}
 \qquad(1\le i<W).
 \tag{1.1}
\]

Assume `W>=5` and that the path is `d=3` factorable, equivalently every internal coordinate
one-run in `T` has length at least four.  A factor is a nonempty word

\[
 A_1,\ldots,A_{W+3}
\]

with

\[
 T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}
 \qquad(1\le i\le W).
 \tag{1.2}
\]

For `1<=j<=W+3`, define the maximal erosion envelope

\[
 E_j=\bigcap_{i=\max(1,j-3)}^{\min(W,j)}T_i
 \tag{1.3}
\]

and the compulsory boundary footprint

\[
 F_j=
 \bigl(\{\alpha_j\}\text{ if }j\le W-1\bigr)
 \cup
 \bigl(\{\beta_{j-4}\}\text{ if }j\ge5\bigr).
 \tag{1.4}
\]

An omitted conditional term in (1.4) means the empty set.

### Theorem 1.1 (exact one-position run-boundary criterion)

Every factor in (1.2) satisfies

\[
                         F_j\subseteq A_j\subseteq E_j.
 \tag{1.5}
\]

Conversely, fix one position `j` and a nonempty set `S`.  There is a factor
with

\[
 A_j=S,\qquad A_h=E_h\quad(h\ne j)
 \tag{1.6}
\]

if and only if

\[
                         F_j\subseteq S\subseteq E_j.
 \tag{1.7}
\]

#### Proof

If `A_j` contributes to `T_i`, then `j in [i,i+3]`; hence `A_j subseteq
T_i`.  Intersecting over all such `i` gives `A_j subseteq E_j`.

For `j<=W-1`, the coordinate `alpha_j` occurs in `T_j` and not in
`T_(j+1)`.  The two source windows are `[j,j+3]` and `[j+1,j+4]`; their
only position belonging to the first but not the second is `j`.  Thus
`alpha_j in A_j`.  Similarly, for `j>=5`, `beta_(j-4)` occurs in
`T_(j-3)` and not in `T_(j-4)`.  The only new source position is `j`, so
`beta_(j-4) in A_j`.  This proves (1.5) and the necessity of (1.7).

For sufficiency, consider one maximal coordinate run `[s,t]` in the carrier
word, using carrier indices.  Its support in the maximal factor `(E_h)` is

\[
 \begin{cases}
 [1,t],&s=1<t<W,\\
 [s+3,t],&1<s\le t<W,\\
 [s+3,W+3],&1<s\le t=W,\\
 [1,W+3],&s=1, t=W.
 \end{cases}
 \tag{1.8}
\]

The length-four source blocks indexed by this interval cover `[s,t]`, so
`D^3E=T`.  Write the support in (1.8) as `[a,b]`, and delete a coordinate
`x in E_j setminus S` only at `j`.  If this destroys `x` from `T_i`, then

\[
                         [i,i+3]\cap[a,b]=\{j\}.
\]

For integer intervals this forces one of three cases.  Either `j=b=i`, so
`b=t<W` and `x=alpha_j`; or `j=a=i+3`, so `a=s+3>1` and
`x=beta_(j-4)`; or `a=b=j`.  In the last case the carrier run is an
internal length-four run, the left singleton boundary run `[1,1]`, or the
right singleton boundary run `[W,W]`, and its compulsory coordinate again
belongs to `F_j`.  Every case contradicts `F_j subseteq S`.  Thus deleting
every member of `E_j setminus S` preserves `D^3E=T`.  Nonemptiness is
explicit, proving (1.6).  \(\square\)

### Theorem 1.2 (exact simultaneous pin criterion)

Let `J subseteq [W+3]`, and prescribe nonempty `S_j` satisfying (1.7) for
`j in J`.  Put

\[
 A_j=\begin{cases}S_j,&j\in J,\\E_j,&j\notin J,
 \end{cases}
 \tag{1.9}
\]

and, for each coordinate `x`, put

\[
 Z_x=\{h:x\in E_h,\ h\notin J\text{ or }x\in S_h\}.
 \tag{1.10}
\]

Then `D^3A=T` if and only if

\[
 [i,i+3]\cap Z_x\ne\varnothing
 \qquad(1\le i\le W, x\in T_i).
 \tag{1.11}
\]

In particular, (1.11) is automatic when distinct members of `J` have
distance at least four.

#### Proof

Every `A_h subseteq E_h`, so a source occurrence can create no coordinate
outside its required carrier windows.  Coordinate `x` occurs in the source
exactly at `Z_x`.  Equation (1.2) for `(i,x)` is therefore exactly (1.11).
This proves both directions.

If `J` is four-separated, a carrier window `[i,i+3]` contains at most one
modified position.  The one-position sufficiency in Theorem 1.1 then leaves
every coordinate of `T_i` covered.  \(\square\)

### Corollary 1.3 (a middle-certified common reserve contains the footprint)

Suppose nonempty sets `M_j subseteq E_j` already certify every middle
window:

\[
                         \bigcup_{j=i}^{i+3}M_j=T_i
 \qquad(1\le i\le W).
 \tag{1.12}
\]

Then

\[
                         F_j\subseteq M_j
 \qquad(1\le j\le W+3).
 \tag{1.13}
\]

Consequently, if a terminal replacement satisfies
`M_j subseteq S subseteq E_j`, its compulsory run-boundary condition is
automatic.

#### Proof

For `j<=W-1`, the coordinate `alpha_j` is present in `T_j` and absent from
`T_(j+1)`, so among the four reserve positions for `T_j` only `M_j` can
contain it.  For `j>=5`, `beta_(j-4)` is present in `T_(j-3)` and absent
from `T_(j-4)`, so only `M_j` can supply it.  These are exactly the defined
terms of `F_j`.  \(\square\)

## 2. Minimum four-runs and the witness census

### Corollary 2.1 (one-coordinate-letter positions)

Assume `W>=5`.  A position can individually be assigned a one-coordinate
letter in some factor if and only if it is one of

\[
 1,2,3,4,W,W+1,W+2,W+3
 \tag{2.1}
\]

or it is an interior position `5<=j<=W-1` satisfying

\[
                         \alpha_j=\beta_{j-4}.
 \tag{2.2}
\]

The equality (2.2) holds if and only if that coordinate has the exact
internal minimum run

\[
                         T_{j-3},T_{j-2},T_{j-1},T_j.
 \tag{2.3}
\]

Consequently the number of individually one-coordinate-capable positions is

\[
                         8+\rho_4(T),
 \tag{2.4}
\]

where `rho_4(T)` is the number of maximal internal coordinate runs of length
four.

#### Proof

At each of the eight boundary positions only one conditional term of (1.4)
exists.  At an interior position both exist, so `|F_j|=1` exactly when
(2.2) holds.  By Theorem 1.1 the common coordinate lies in `E_j`, hence in
every one of `T_(j-3),...,T_j`; it is absent from `T_(j-4)` and
`T_(j+1)` by (1.1).  Thus these four sets form its exact maximal run (2.3).
The converse is the same statement read backwards.
Theorem 1.1 now proves the capability assertion and the count.  \(\square\)

Every universal word must realize all 15 one-coordinate targets.  Since an
OR of nonempty letters equals `{x}` only when every letter in that interval
equals `{x}`, the boundary labels together with the labels of the internal
minimum runs must cover all 15 coordinates.  In particular,

\[
                         \rho_4(T)\ge7.
 \tag{2.5}
\]

This weak but genuine run consequence is the most that raw rank-one demand
gives without using label multiplicities.

Now specialize to `k=15`, `r=8`, `W=6435`.  The exact row census for a
putative length-6,438 universal word says

\[
 n_1\ge3510,\qquad n_2\ge3509,\qquad n_3\ge3508.
 \tag{2.6}
\]

Here `n_q` counts selected target witnesses on physical intervals of length
`q`.  Thus `n_1>=3510` says that at least 3,510 source positions have been
selected with pairwise distinct lower-target values `S=A_j`.  Each such
selection obeys `F_j subseteq S subseteq E_j`.  The full shrink set
`{j:A_j ne E_j}` need not coincide with the selected witness positions and
may contain positions outside them; this full shrink set obeys the
simultaneous condition (1.11).  It says nothing like
`rho_4(T)>=3502`.

Likewise

\[
                         n_2+n_3\ge7017
 \tag{2.7}
\]

selected witnesses are already physically non-singleton.  This is a global
row census, not a claim that any of those cells is a new neighbour of the
Hall-29 shore.

The erosion rank profile is forced by three-step residence:

\[
 |E_j|=
 \begin{cases}
 8,&j=1,W+3,\\
 7,&j=2,W+2,\\
 6,&j=3,W+1,\\
 5,&4\le j\le W.
 \end{cases}
 \tag{2.8}
\]

Indeed, in any block `T_a,...,T_(a+h-1)` with `h<=4`, the removed coordinates
`alpha_a,...,alpha_(a+h-2)` are distinct.  A repeated removal would require
an intervening reinsertion and would create an internal one-run of length at
most two.  Moreover every one of these removed coordinates belongs to
`T_a`: if `alpha_b` were absent from `T_a`, choose its last insertion
transition `c` with `a<=c<b`; then its uninterrupted internal run
`T_(c+1),...,T_b` would again have length at most two.  Thus

\[
 \bigcap_{\ell=0}^{h-1}T_{a+\ell}
 =T_a\setminus\{\alpha_a,\ldots,\alpha_{a+h-2}\},
\]

which has rank `8-(h-1)`.  Applying this to the clipped intersection (1.3)
proves (2.8).

Therefore at most six physical singleton witnesses can have target rank at
least six, and at most four can have rank seven.  In particular at least
3,504 of the `n_1` selected targets have rank at most five.

## 3. The exact minimal Hall-29 gate

Retain the 1,489 peeled Hall-29 reservations.  The residual target family
`R_29` has rank profile

\[
                         4^9\,5^1\,6^{17}\,7^8.
 \tag{3.1}
\]

Its six surviving old cells have the disjoint candidate pairs

\[
\begin{array}{c|c}
15899&2420,2932\\
16597&4877,4909\\
18079&17683,21779\\
18088&2676,10868\\
18090&9524,9588\\
18985&19568,27760.
\end{array}
 \tag{3.2}
\]

In every row of (3.2), the first target has rank six and the second rank
seven.

### Theorem 3.1 (exact 29-address selector criterion and bulk floor)

Let a co-designed repair retain the six cells (3.2) with exactly their
displayed candidate pairs, keep the 1,489 peeled reservations, and add
exactly 29 distinct physical cell addresses, none equal to any of the six
old or reserved addresses; their source intervals may overlap.  It completes
the 35-target kernel if and only if there are:

1. one selected target `z_a` from each pair in (3.2);
2. a bijection from `R_29 setminus {z_1,...,z_6}` to the 29 new addresses,
   with every matched address available and base-eligible for its target,
   including every envelope, mandatory-coordinate, and deadline condition;
3. one common literal controller word on the whole source line for which
   each old cell in (3.2) has union `z_a`, every matched new interval has
   union equal to its matched target, all entries `Q_p` are nonempty, every
   active label contains `Q_p`, and at each position there are at most two
   active labels `Gamma_p` whose selected intervals contain `p` and satisfy

   \[
       Q_p=E_p\cap\bigcap_{L\in\Gamma_p}L.
   \]

   Every middle window, every one of the 1,489 retained owner intervals, and
   every other protected window must also keep its exact union.

Declare each matched target active on its assigned interval.  Its union
equality implies `Q_p subseteq S` at every position of that interval, so
this installation causes no additional shrinkage beyond the stated word.

If the new address matched to `S` is the physical singleton `[j,j]`, then
Condition 3 forces

\[
                         F_j\subseteq S\subseteq E_j,
 \tag{3.3}
\]

and the whole family of such singleton assignments must satisfy (1.11).
Equivalently in the bulk/terminal normal form, put the six old cells and all
new length-two/length-three cells into the bulk.  Their exposed cores `B_j`
must admit one reserve

\[
                         \varnothing\ne M_j\subseteq B_j
\]

which realizes every middle, retained-owner, protected, and bulk-target
union.  At every terminal position one must have

\[
                         M_j\subseteq S\subseteq B_j
 \tag{3.4}
\]

and the terminal target must satisfy every protected containment active
there.  The terminal matching must use every position whose exposed bulk
meet has dimension above two or violates a protected containment.  Since
the reserve certifies the middle windows, Corollary 1.3 gives
`F_j subseteq M_j`, so (3.3) adds no further terminal cut.

Every such repair has at least 13 new addresses of physical length two or
three.  Equivalently, at most 16 of the 29 new addresses can be terminal
singletons.

#### Proof

With exactly 29 new cells, all six old cells must be used.  A fixed word
gives each old cell one union value, so it chooses exactly one target from
its displayed pair.  The other 29 distinct targets must use the 29 new cells
bijectively.  Conversely, the three stated conditions literally realize all
35 targets on distinct cells.  This proves the equivalence; (3.3) is
Theorems 1.1--1.2, and (3.4) is the common-reserve terminal criterion.

For the latter equivalence, remove the terminal singleton owners and
intersect all remaining active fixed and bulk labels to obtain `B_j`.  From
an existing word take `M_j=Q_j`; it certifies every listed union.  Conversely,
installing a compatible terminal target `S subseteq B_j` makes the meet at
its position exactly `S`, while both matched `S` and unmatched `B_j` still
contain `M_j`.  Hence every reserve-certified union survives.  Covering all
hot or protected-violating positions gives precisely the remaining
trace-two and containment conditions.

There are 25 targets of rank at least six.  The six old cells discharge at
most six of them, leaving 19.  By (2.8), only six physical singleton
positions have envelope rank at least six.  Hence at most six of those 19
targets can use new singleton cells.  At least `19-6=13` new cells must have
length at least two.  Every lower-target interval has length at most three,
because every interval of length at least four contains a length-four middle
window of rank eight.
Thus those 13 cells have length two or three.  The complementary upper bound
on terminal cells is `29-13=16`.  \(\square\)

The number 13 is sharp at the rank-capacity level: choose the rank-seven
member of each old pair, leaving two rank-seven and 17 rank-six targets;
the six high-rank boundary envelopes can host two plus four of these, while
the ten rank-four/rank-five targets can use interior singleton envelopes.
This is not a construction: the containment graph, run-hitting condition,
common reserve, and controller footprints may still fail.

Independently of minimal-repair architecture, (3.1) and (2.8) show that at
most the ten rank-at-most-five members of `R_29`, plus six high-rank members
at the six high-envelope boundary positions, can contribute to the physical
singleton row.  Combining this bound with (2.6), any full compiler must take
at least

\[
                         3510-16=3494
 \tag{3.5}
\]

of its selected length-one witnesses from targets outside `R_29`.  The
Hall-29 repair is therefore a mixed-row exchange inside a global witness
assignment, not an isolated 29-position singleton append.

### Theorem 3.2 (controller-port form of the sharp UNIT exposure gate)

Identify the maximal erosion envelopes in this note with the controller
states `P_j=E_j`.  In the one-based convention of Sections 1--3, for
`5<=j<=W-1`,

\[
 |P_j|=5,
 \qquad P_j\setminus P_{j+1}=\{\alpha_j\},
 \qquad P_j\setminus P_{j-1}=\{\beta_{j-4}\}.          \tag{3.6}
\]

Thus the footprint `F_j` in (1.4) is exactly the union of the incoming and
outgoing controller ports.  Every physical factor `A` is a pinning of `P`:

\[
 F_j\subseteq A_j\subseteq P_j,                        \tag{3.7}
\]

and on each internal coordinate run in `P`, the selected positions include
both endpoints and have consecutive gaps at most four.

For the finite frozen-carrier statement, switch explicitly to the zero-based
artifact convention

\[
 T_i^{(0)}=T_{i+1},\qquad P_p^{(0)}=P_{p+1},\qquad
 A_p^{(0)}=A_{p+1},                                   \tag{3.8}
\]

and suppress the superscript.  Thus an artifact pin `(p,x)` demands
`x in P'_{p+1},A'_{p+1}` in the standing one-based convention, and its
displayed missing index `q` means the one-based carrier state `T_{q+1}`.
In this zero-based convention, restrict the compact atlas to positive
defect-one records with one missing coordinate `x`, and call `(p,x)` a UNIT
controller pin when `p` lies in the target cell and exactly one carrier
state defining `P_p` omits `x`.  Service is measured by a matching of
distinct targets to distinct physical cells for a fixed pin.  Then:

1. there are 1,602 UNIT pin types;
2. 1,594 have service matching number one and exactly eight have service
   matching number two;
3. the conflict graph of the eight double services is a triangle, an edge,
   and three isolated vertices, so at most five double services coexist;
4. every 29-address UNIT repair therefore uses at least 24 pins; and
5. there is an exact 24-pin certificate complementary to the six old cells,
   avoiding all 1,489 reservations, whose 29 new addresses have length
   profile `(7,15,7)`.

#### Proof

The structural assertions (3.6)--(3.7) are erosion--Johnson controller
duality and the exact run-pinning theorem.  For the finite assertion, a pin
serving `a` addresses contributes one base address and `a-1` extras.  No pin
contributes more than one extra.  Among the eight pins capable of one extra,
at most `1+1+3=5` are target/cell-disjoint.  Hence `t` pins serve at most
`t+5` addresses and `t>=29-5=24`.  The complete list of the eight double
services and an explicit old-pair-complementary 24-pin certificate are in
`MATH_K15_HALL29_UNIT_PIN_COVER_20260728.md`; direct comparison with the
authoritative atlas verifies every target, cell, depth, reservation, and
unique missing carrier index.  \(\square\)

The controller interpretation is essential.  A designated repair needs
both a new controller incidence `x in P'_p` and the physical selection
`x in A'_p`.  The forced incoming/outgoing ports at every active position
must lie in every target label whose interval crosses that position, and
all coordinate-run pin gaps must remain at most four.  The old atlas must be
recomputed after rethreading; inserting the 24 incidences alone is not a
physical construction.

There is also an exact global compensation law.  For each coordinate `x`,
the controller count is

\[
 p_x=\binom{14}{7}-3i_x=3432-3i_x,                    \tag{3.9}
\]

where `i_x` is the number of internal `x`-runs in the exact middle carrier.
Hence every old and new controller count is divisible by three.  Writing
`delta^+_(p,x)` and `delta^-_(p,x)` for inserted and deleted controller
incidences relative to the frozen controller, every lift obeys

\[
 \sum_x\delta^+_{p,x}=\sum_x\delta^-_{p,x}
 \quad\text{for every state }p,
 \qquad
 \sum_p(\delta^+_{p,x}-\delta^-_{p,x})\equiv0\pmod3
 \quad\text{for every }x.                             \tag{3.10}
\]

The 24 designated incidences are forced positive terms in (3.10).  Thus a
lift must supply compensating deletions while retaining rank five at every
flat controller state; the pins are not independent additions.

Indeed no nontrivial one-carrier-state edit preserves the exact middle
deck.  If the unique missing state is `T_q` and one tries
`T'_q=T_q-{y}+{x}` with both neighbours frozen, adjacency to a neighbour is
preserved exactly when `x` and `y` have the same membership indicator in
that neighbour.  Even if both local tests pass, `T'_q` is another rank-eight
set already present elsewhere, so the edit duplicates one middle set and
omits `T_q`.  A legal realization must close into a global controller
rethreading.

## 4. Frozen Hall-29 certificate

The authoritative carrier is

`scratch/k15_doubletrans_05_213_hall29.json`,

with SHA-256

`5516482eadaba4f8fb9549b41c79c3b949df2e3224ce68f9dacd3b5b6bc2d21c`.

A direct linear audit of its 6,435 middle sets gives:

\[
 \rho_4(T)=1145,
 \qquad
 \#\{j:|F_j|=1\}=1153,
 \qquad
 \#\{j:|F_j|=2\}=5285.
 \tag{4.1}
\]

The length-four run counts by coordinate `0,...,14` are

\[
 83,73,71,73,83,86,71,79,77,79,71,76,77,70,76.
 \tag{4.2}
\]

No internal run has length below four.  For auditability, the SHA-256 of the
no-newline ASCII string obtained by sorting the 1,145 internal minimum-run
records numerically by zero-based position and joining
`position:coordinate` records with commas is

`3e66f7b673e628fa8f823f66e577e7d3938477dad609c8c56d1a2b0398e8d6c0`.

Before reserved cells are deleted, the exact incidence between the 35 peeled
residual target labels and all physical singleton positions has 81 edges on
81 distinct positions.  They are exactly nine rank-four targets, each of
degree nine:

\[
 89,449,960,1920,8217,8218,16422,20516,24610.
 \tag{4.3}
\]

All 81 positions have `|F_j|=2`, and all 81 cells were already consumed by
the peeled reservations.  No residual target satisfies (3.3) at any of the
1,153 one-coordinate-capable positions.  The SHA-256 of the no-newline ASCII
string obtained by sorting the 81 edges numerically by `(target,position)`
and joining zero-based `target:position` records with commas is

`0c5fad511edcd8d71549c5a268afc6b5bfc58e975e1e2323c4dba41a8df0a67c`.

Thus reopening or terminalizing the existing minimum-run positions exposes
zero residual edges in the fixed-envelope, fixed-footprint model.  The
residual family does have the 81 singleton edges above, but every one is
reserved; hence its unreserved residual singleton graph is empty.  This
agrees with the independently audited peeled graph, whose only six
unreserved cells all have length three.  Completion on the unchanged fixed
candidate graph is impossible.  Any minimal repair satisfying Theorem 3.1's
hypotheses must make at least 13 of its 29 new addresses length two or three.

## 5. Proved and open boundary

Proved:

1. `F_j subseteq A_j subseteq E_j` is exact, including one-position
   sufficiency and the simultaneous run-hitting criterion.
2. One-coordinate-letter positions are exactly the eight boundaries plus
   internal minimum four-runs.
3. The row census counts physical interval lengths and cannot be converted
   into a minimum-run count.
4. Every exactly-29-address Hall-29 repair retaining the six old cells and
   1,489 reservations needs at least 13 length-two/length-three addresses.
5. The frozen carrier's 1,153 one-coordinate-capable positions expose no new
   peeled Hall-29 singleton address.
6. In the positive-defect UNIT controller model, 29 new addresses require
   at least 24 pins; an old-pair-complementary 24-pin incidence certificate
   exists and has 22 nonsingleton addresses.
7. That particular 22-nonsingleton certificate is physically impossible at
   two retained collars.  A different complementary 24-pin certificate has
   profile `(6,16,7)` and passes all fixed retained/new collar tests, but
   still has no controller lift.

Not proved:

1. one physical controller lift of the 22-nonsingleton incidence
   certificate (or of any other admissible mixed-row certificate);
2. a common controller word or reserve realizing a 29-address repair;
3. a Hall-zero `k=15` carrier or a length-6,438 universal word.

The smallest positive replacement lemma is now a controller-port lift:
construct one controller `P'` and one pinning `A'` that realize the
collar-safe old-pair-complementary 24-UNIT-pin cover in
`THREAD_H_K15_COMPENSATED_CONTROLLER_CIRCUIT_GATE_20260728.md`, including at
least 13 length-two or length-three bulk
cells, while satisfying the forced ports, four-gap rule, exact middle deck,
statewise rank balance, coordinatewise mod-three incidence balance,
upper/protected windows, all 1,489 reservations, the six old cells, common
owner/reserve, deadlines, and trace-two footprints.  Failure of all 24-pin
covers would not close the UNIT lane: physical compatibility might require
25--29 serving pins.  A negative theorem must exclude all admissible
old-pair-complementary UNIT covers of sizes 24 through 29, or prove a
reduction to size 24.  This UNIT-lane lemma does not exclude a non-UNIT or
mandatory-defect repair.
