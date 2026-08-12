# Per-chain Shearer--Kleitman lifts fail on every good `Q_6` seed

## Status

The global-mode lift search found `24` almost-orthogonal, union-perfect SCD
pairs on `Q_6`, but no global-mode continuation to `Q_8`.  Allowing an
independent Shearer--Kleitman mode on every chain does **not** repair this.

For every one of the `24` seeds, even the following relaxation is
impossible:

* ignore orthogonality at `Q_7` and `Q_8`;
* ignore consistency between choices made for different lower masks;
* let every rank-three lower mask independently choose any rank-five union
  obtainable from any local per-chain modes.

The unavoidable pointwise condition that the two successors be distinct is
retained: equal successors have a rank-four union and cannot represent an
upper colour.  No other orthogonality condition is used.

The resulting lower-to-upper candidate graph has maximum matching only
`55/56`.  In every seed there is a three-to-two Hall obstruction of the
form

\[
 \{ab6,c67,c68\}\longrightarrow
 \{abc67,abc68\}.
\tag{0.1}
\]

Thus all `24` per-chain lift instances are unconditionally UNSAT for union
injectivity.  SAT is useful for checking the full formulation, but is not
needed for the proof.

The local cause is a **lift fork**, defined in Section 4.  It gives a new
necessary inductive invariant: a pair intended to survive another
two-coordinate per-chain lift must be fork-free.  All `84` good `Q_4` pairs
are fork-free; all `24` good `Q_6` pairs produced by the simple global lift
contain a fork.  Fork-freeness is not known to be sufficient.

## 1. The per-chain lift

Let

\[
 C=(x_0,x_1,\ldots,x_t)
\]

be a symmetric saturated chain in `Q_n`, and let `z` be the new coordinate.
There are two standard lifts.

Mode zero produces

\[
 (x_0,x_1,\ldots,x_t,x_tz),
 \qquad
 (x_0z,x_1z,\ldots,x_{t-1}z),
\tag{1.1}
\]

with the second chain omitted when empty.  Mode one produces

\[
 (x_0,x_0z,x_1z,\ldots,x_tz),
 \qquad
 (x_1,x_2,\ldots,x_t).
\tag{1.2}
\]

Either mode may be chosen independently for every chain; the resulting
chains still form an SCD.

Starting with one SCD of `Q_6`:

* there are `20` first-stage choices, one per `Q_6` chain;
* the lift has `35` `Q_7` chains, hence `35` second-stage choices.

For a pair of SCDs the complete `Q_6 -> Q_7 -> Q_8` problem therefore has

\[
 2(20+35)=110
\tag{1.3}
\]

Boolean variables.

## 2. Exact SAT structure

### Proposition 2.1 (one lift is 2-SAT for orthogonality)

Fix an almost-orthogonal pair `D,E` on `Q_n`.  Give each `D`-chain `C` a
mode bit `x_C` and each `E`-chain `F` a mode bit `y_F`.

For a fixed pair `(C,F)`, whether their lifted descendants violate almost
orthogonality depends only on `(x_C,y_F)`.  For each bad value `(a,b)`, add

\[
 (x_C\ne a)\lor(y_F\ne b).
\tag{2.1}
\]

The conjunction of these clauses over all chain pairs is necessary and
sufficient for the lifted decompositions to be almost orthogonal.

#### Proof

Every lifted mask descending from `C` lies in one of the two children in
(1.1) or (1.2), and similarly for `F`.  Thus the complete intersection
pattern of their children is fixed by two mode bits.  Clause (2.1) deletes
exactly a bad truth-table row.  Cross-pair orthogonality is the conjunction
over all original chain pairs.  QED.

This formulation automatically handles the exceptional longest-chain pair
that may share the old bottom and top; no separate endpoint convention is
hidden.

For two simultaneous lifts, a pair of original `Q_6` parent chains has at
most two `Q_7` children on each side.  Its final `Q_8` intersection pattern
depends on at most

* two first-stage parent bits, and
* four second-stage child bits.

Hence final orthogonality has an exact local CNF of width at most six.
Requiring intermediate `Q_7` orthogonality adds the 2-SAT clauses from
Proposition 2.1.

### Proposition 2.2 (central unions have width-eight collision clauses)

Fix a rank-three mask `S` in `Q_8`.  In one lifted decomposition, its
rank-four successor is determined by

1. the first-stage bit of the unique `Q_6` chain containing `S cap [6]`;
2. the second-stage bit of the active `Q_7` child containing
   `S cap [7]`.

Thus the union of its `D`- and `E`-successors depends on at most four bits.
For two lower masks `S,T`, a specified equal-union event depends on at most
eight bits and is forbidden by one clause.

The exact encoder

```text
scratch/per_chain_oscd_lift_q6_q8_sat.py
```

uses these local truth tables.  After exact clause subsumption, every seed
has

\[
\begin{array}{c|c}
\text{constraint family}&\text{clauses}\\ \hline
\text{orthogonality only}&776\\
\text{union injectivity only}&2661\\
\text{both}&3325.
\end{array}
\tag{2.2}
\]

Kissat returns SAT for orthogonality alone and UNSAT for union injectivity
alone on every seed.  The Hall proof below independently explains and
certifies the latter result.

## 3. The candidate Hall relaxation

For one `Q_6` seed `(D,E)` and a rank-three mask `S` of `Q_8`, define

\[
 \Gamma(S)=
 \{f_{D'}(S)\cup f_{E'}(S):
   \text{all local per-chain modes on the active ancestries},
   \ f_{D'}(S)\ne f_{E'}(S)\},
\tag{3.1}
\]

where `D',E'` denote the resulting `Q_8` decompositions.  The choices in
(3.1) are deliberately allowed to vary independently with `S`.

Any genuine per-chain lift assignment gives one member of `Gamma(S)` for
every `S`.  Therefore union injectivity requires a matching saturating all
`56` lower vertices in the bipartite candidate graph

\[
 S\sim U\quad\Longleftrightarrow\quad U\in\Gamma(S).
\tag{3.2}
\]

This is a relaxation: it forgets shared mode variables and all
orthogonality constraints.

### Theorem 3.1 (exact `55/56` obstruction)

For each of the `24` good `Q_6` seeds, the candidate graph (3.2) has maximum
matching size `55`.  More precisely, there are distinct old coordinates
`a,b,c in [5]` such that

\[
\begin{aligned}
 \Gamma(ab6)&=\{abc67,abc68\},\\
 \Gamma(c67)&=\{abc67\},\\
 \Gamma(c68)&=\{abc68\}.
\end{aligned}
\tag{3.3}

Consequently

\[
 \left|\Gamma(\{ab6,c67,c68\})\right|=2<3,
\tag{3.4}
\]

so Hall's theorem rules out an injective union map.

The proof of the uniform form (3.3) is the lift-fork lemma in the next
section.  The complete seed-by-seed certificate appears in Section 5.

## 4. The lift-fork lemma

The Hall obstruction is not an accidental finite collision.

Let `D,E` be SCDs of `Q_{2m}` and let `S` have rank `m-1`.  Suppose:

1. `S` is not the bottom member of either of its two chains;
2. its central successors are

   \[
   f_D(S)=S+a,\qquad f_E(S)=S+b,qquad a\ne b;
   \tag{4.1}
   \]

3. for some `c in S`, put

   \[
   A=(S-c)+a+b,qquad V=S+a+b=A+c;
   \tag{4.2}
   \]

4. `A` is a singleton chain in one decomposition, while in the other it
   has at least two chain members below it and immediate successor `V`.

Call this configuration a **lift fork**.

### Lemma 4.1 (two-coordinate Hall fork)

Add new coordinates `p,q` by two arbitrary per-chain lifts.  Then, for the
resulting central successor unions,

\[
\begin{aligned}
 \Gamma(S+p)&=\{V+p\},\\
 \Gamma(S+q)&=\{V+q\},\\
 \Gamma(A)&\subseteq\{V+p,V+q\}.
\end{aligned}
\tag{4.3}

Both values in the last line are locally attainable, but containment is
all Hall's theorem needs.  Hence no pair containing a lift fork can have a
union-injective two-coordinate per-chain lift.

#### Proof

First note three elementary consequences of (1.1)--(1.2).

* If `x<y` is a chain edge and `x` is not bottom, then after two arbitrary
  lifts the successors of `x+p` and `x+q` are respectively `y+p` and
  `y+q`.  The edge persists in the high child at one stage and the low child
  at the other; the nonbottom condition prevents either copy from becoming
  the exceptional moved bottom.
* If `x<y` and at least two chain members lie below `x`, then the successor
  of the old mask `x` remains `y` after both lifts.  Removing the old bottom
  in mode one can lower the depth by only one at each first-stage split, so
  `x` is still nonbottom when the second low-copy lift is made.
* A singleton chain `{x}` first becomes `(x,x+p)`.  At the second lift, the
  successor of `x` is `x+p` in mode zero and `x+q` in mode one.

Apply the first statement to the two edges in (4.1).  The two successors at
`S+p` are `S+a+p` and `S+b+p`, whose union is `V+p`; the argument for
`S+q` is identical.

At `A`, the nonsingleton decomposition keeps successor `V` by the second
statement.  The singleton decomposition supplies `A+p` or `A+q` by the
third.  Since `A subset V`, the two possible unions are `V+p,V+q`.  This
proves (4.3), and the three-to-two Hall obstruction follows.  QED.

## 5. All twenty-four certificates

Coordinates `7,8` below are the two newly lifted coordinates.

| seed | `Q_4` pair | history | Hall lower family | Hall upper family |
|---:|---:|:---:|:---|:---|
| 0 | `3,236` | `11` | `356,467,468` | `34567,34568` |
| 1 | `9,232` | `00` | `256,167,168` | `12567,12568` |
| 2 | `15,178` | `00` | `256,167,168` | `12567,12568` |
| 3 | `19,174` | `11` | `456,367,368` | `34567,34568` |
| 4 | `27,214` | `11` | `256,467,468` | `24567,24568` |
| 5 | `28,210` | `00` | `356,167,168` | `13567,13568` |
| 6 | `31,118` | `00` | `356,167,168` | `13567,13568` |
| 7 | `37,112` | `11` | `456,267,268` | `24567,24568` |
| 8 | `45,150` | `00` | `456,167,168` | `14567,14568` |
| 9 | `46,152` | `11` | `256,367,368` | `23567,23568` |
| 10 | `54,96` | `00` | `456,167,168` | `14567,14568` |
| 11 | `59,90` | `11` | `356,267,268` | `23567,23568` |
| 12 | `62,223` | `11` | `356,467,468` | `34567,34568` |
| 13 | `69,221` | `00` | `156,267,268` | `12567,12568` |
| 14 | `75,162` | `00` | `156,267,268` | `12567,12568` |
| 15 | `77,161` | `11` | `456,367,368` | `34567,34568` |
| 16 | `87,190` | `11` | `156,467,468` | `14567,14568` |
| 17 | `88,196` | `00` | `356,267,268` | `23567,23568` |
| 18 | `105,136` | `00` | `456,267,268` | `24567,24568` |
| 19 | `106,134` | `11` | `156,367,368` | `13567,13568` |
| 20 | `122,205` | `11` | `256,467,468` | `24567,24568` |
| 21 | `125,203` | `00` | `156,367,368` | `13567,13568` |
| 22 | `147,184` | `11` | `156,467,468` | `14567,14568` |
| 23 | `149,180` | `00` | `256,367,368` | `23567,23568` |

For every row, the three candidate-set sizes are `2,1,1`, and the maximum
matching in the full `56 x 56` candidate graph has size exactly `55`.

## 6. Inductive consequence

The natural invariant

\[
 \text{almost orthogonal} + \text{central unions injective}
\tag{6.1}
\]

is not closed under even the fully per-chain two-coordinate lift.  The
missing state information is already visible locally.

### Necessary strengthened invariant

A pair meant to survive the next two-coordinate per-chain lift must be

\[
 \text{almost orthogonal} + \text{union-perfect} + \text{fork-free}.
\tag{6.2}
\]

The checker finds:

* all `84` union-perfect almost-orthogonal `Q_4` pairs are fork-free;
* all `24` union-perfect `Q_6` pairs produced by the simple global lift have
  a lift fork.

Thus the simple induction loses exactly the new invariant at its first
successful nontrivial step.  Fork-freeness is only necessary; other Hall
obstructions or shared-mode conflicts may remain.

There are now two credible ways to continue this SCD route.

1. Search for a different union-perfect, fork-free `Q_6` pair and test
   whether (6.2) can be preserved.
2. Enlarge the lift move beyond independent modes on fixed parents, allowing
   chain splices between different parent chains.  Such a splice must break
   the forced singleton/depth-two relationship in a lift fork.

Continuing to vary only one bit independently on each chain of any of the
current `24` seeds cannot work.

## 7. Correct ledger

**Proved mathematically**

* one-stage per-chain lift orthogonality is an exact 2-SAT problem;
* the two-stage full problem has a bounded-width exact SAT encoding;
* the lift-fork lemma gives a three-to-two Hall obstruction;
* any seed containing a lift fork is impossible regardless of
  orthogonality.

**Verified exhaustively**

* the original global search has `24` union-perfect `Q_6` seeds;
* all `24` contain the displayed lift fork;
* all `24` relaxed candidate graphs have matching number `55`, not `56`;
* the exact 110-variable SAT instances are UNSAT even with orthogonality
  omitted.

**Open**

* existence of a union-perfect fork-free OSCD pair on `Q_6` outside these
  `24` lift seeds;
* sufficiency or inductive preservation of fork-freeness;
* a nonlocal chain-splicing lift that avoids the Hall fork.
