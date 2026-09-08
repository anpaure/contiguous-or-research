# Exact age-flag run criterion and full-flag refinement

**Date:** 2026-08-02  
**Status:** unconditional.  This closes the literal age-state realization
problem for a fixed rainbow Johnson cycle when no deeper marked chains are
prescribed, and gives a linear-time exact test when every prescribed chain
uses all `d` suffix levels.  It does **not** construct the required
coatom-rooted lower-chain partition, a suitable rainbow cycle, the upper
deck, or a terminal word.

## 0. Setting

Let

\[
 Q_0,Q_1,\ldots,Q_{N-1}
\]

be a cyclic simple walk in `J(k,r-1)`.  Write

\[
 Q_{i+1}=Q_i-\{\alpha_i\}+\{\beta_i\},
 \qquad T_{i+1}=Q_i\cup Q_{i+1}.                 \tag{0.1}
\]

When the `Q_i` run through the complete rank-`(r-1)` layer and the `T_i`
run through the complete rank-`r` layer, this is the contracted rainbow
Middle Levels cycle of Corollary 3.1 in
`MATH_THEOREM_ODD_ONECOPY_COATOM_MIDDLELEVELS_PATH_NORMAL_FORM_20260802.md`.

Recall that a depth-`d` age flag on `Q_i` is an ordered partition

\[
 Q_i=C^i_0\mathbin{\dot\cup}\cdots
          \mathbin{\dot\cup}C^i_{d-1}.            \tag{0.2}
\]

The literal shift equations are

\[
 \alpha_i\in C^i_{d-1},\qquad
 C^{i+1}_{t+1}\subseteq C^i_t\quad(0\le t<d-1),   \tag{0.3}
\]

together with the refresh/newborn identity for `C^(i+1)_0`.  These
equations are necessary and sufficient for a literal cyclic source
spelling.

## 1. Coordinate runs contain the whole age holonomy

For a coordinate `x`, a **positive `Q`-run** is a maximal cyclic interval

\[
             Q_a,Q_{a+1},\ldots,Q_b
\]

all containing `x`.  Its length is `ell=b-a+1`.  Since the walk visits more
than one coatom, every run has an entry and a departure.

### Theorem 1.1 (exact cyclic run criterion)

The cycle `(Q_i)` admits labelled age flags satisfying all oldest-departure,
survivor, refresh and newborn equations if and only if

\[
 \boxed{\text{every positive coordinate run in }(Q_i)
                    \text{ has length at least }d.}            \tag{1.1}
\]

There is no further global age holonomy and no interaction between
different coordinates.

#### Proof

Fix a positive run of `x` and number its positions `0,...,ell-1`.  At its
first position `x` is the newborn `beta`, so its age is zero.  At its last
position it is the departing `alpha`, so its age is `d-1`.  At an internal
survival step its age either increases by one or is reset to zero.  It can
never increase past `d-1`.

Starting from zero, reaching age `d-1` needs at least `d-1` transitions.
Thus `ell>=d`, proving necessity.

Conversely, suppose `ell>=d`.  Choose refresh positions in the run as
follows.  The entry position is a refresh.  The final refresh is at position
`ell-d`; before it, insert refreshes so that every two successive refreshes
are at distance at most `d`.  For example, take

\[
 \{0\}\cup\{\ell-d-jd:j\ge0,\ \ell-d-jd>0\}.       \tag{1.2}
\]

Give `x` age zero at these positions and increase its age by one at every
other position.  The final `d` positions then have ages
`0,1,...,d-1`, so departure is legal.  Every earlier age is also at most
`d-1`.

Do this independently on every positive run of every coordinate.  At state
`Q_i`, let `C^i_t` be the set of present coordinates of age `t`.  Entry,
departure and survival have exactly the alternatives in (0.3).  Every old
coordinate not chosen as a survivor is refreshed, and the unique new
coordinate is born, so the refresh/newborn identity follows coordinate by
coordinate.  The resulting `C^i_t` partition `Q_i`.  This constructs the
required cyclic spelling.  \(\square\)

### Corollary 1.2 (exact number of spellings)

Let `f_d(0)=1`, and for `n>0` put

\[
 f_d(n)=\sum_{j=1}^{\min(d,n)}f_d(n-j).              \tag{1.3}
\]

If the run condition holds, the number of labelled age-flag spellings is

\[
 \boxed{\prod_{x}\ \prod_{R\in\mathcal R_x}
                    f_d\bigl(|R|-d\bigr),}           \tag{1.4}
\]

where `R_x` is the family of positive runs of `x`.

Indeed, the refresh positions before the forced final `d`-block are exactly
a composition of `ell-d` into parts in `{1,...,d}`.  The choices are
independent for different coordinate runs.

### Corollary 1.3 (residence and an explicit source word)

The construction is algorithmic in `O(kN)`.  If `a_i(x)` is the constructed
age, take the source letter appended at the turn into `Q_i` to be

\[
                 B_i=\{x\in Q_i:a_i(x)=0\}.          \tag{1.5}
\]

It is nonempty because it contains the newborn coordinate.  The union of
the last `d` source letters is `Q_i`, and the next `(d+1)`-window union is
`Q_i union Q_(i+1)=T_(i+1)`.

Moreover a `Q`-run of length `ell` supplies an owner interval of length
`ell+1`.  Hence (1.1) automatically gives owner-coordinate residence at
least `d+1`.  (The converse need not hold when two `Q`-runs are separated
by a single absent state, because their owner intervals then merge.)

Thus, for the unmarked lower-side spelling, a resident contracted
Middle-Levels cycle has no hidden age-state obstruction: residence is the
whole literal gate.

## 2. Prescribed full flags have an exact local transition test

Suppose the chain assigned to `Q_i` has exactly `d` distinct members

\[
 S^i_0\subset S^i_1\subset\cdots
       \subset S^i_{d-1}=Q_i.                       \tag{2.1}
\]

Since there are exactly `d` suffix thresholds, their positions are forced.
Put

\[
 D^i_0=S^i_0,\qquad
 D^i_t=S^i_t\setminus S^i_{t-1}\quad(1\le t<d).     \tag{2.2}
\]

### Theorem 2.1 (full-flag transition criterion)

The prescribed full flags are literally spellable around the fixed cycle
if and only if, for every `i`,

\[
 \boxed{
 \alpha_i\in D^i_{d-1},\qquad
 D^{i+1}_{t+1}\subseteq D^i_t
                 \quad(0\le t<d-1).}                \tag{2.3}
\]

This is a linear-time check in the size of the displayed flags.

#### Proof

Necessity is (0.3), because the full chain forces `C^i_t=D^i_t`.

Conversely, the survivor inclusions in (2.3) place every positive-age class
of the next state inside the corresponding previous-age class.  Their union
therefore contains neither the newborn `beta_i` nor the departing
`alpha_i`.  Since the `D` classes partition `Q_i` and `Q_(i+1)`, their
complement in `Q_(i+1)` is exactly

\[
 \{\beta_i\}\mathbin{\dot\cup}
 (D^i_{d-1}\setminus\{\alpha_i\})
 \mathbin{\dot\cup}
 \mathop{\dot\bigcup}_{t=0}^{d-2}
       (D^i_t\setminus D^{i+1}_{t+1}).               \tag{2.4}
\]

This complement is `D^(i+1)_0`, so (2.4) is precisely the missing
refresh/newborn equation.  The age-flag spelling equivalence now gives the
literal source.  \(\square\)

### Corollary 2.2 (partial-chain refinement criterion)

Let each prescribed coatom-rooted chain have at most `d` members.  It is
spellable around the fixed cycle if and only if it admits a weak length-`d`
refinement

\[
 F^i_0\subseteq F^i_1\subseteq\cdots
          \subseteq F^i_{d-1}=Q_i                 \tag{2.5}
\]

which contains every prescribed chain member as one of its values and whose
difference classes satisfy (2.3).  Empty difference classes are allowed.

This is an exact flag-refinement formulation.  In particular, for a fixed
full chain table and a fixed cycle the literal realization problem is not a
de Bruijn search; it is just the local containment replay (2.3).

## 3. Birth cores and departure apertures

For a prescribed chain `K_i`, let

\[
 A_i=\min K_i,
 \qquad
 Z_i=Q_i\setminus\max(K_i\setminus\{Q_i\}),          \tag{3.1}
\]

where `Z_i=Q_i` if the chain contains no proper member.

### Corollary 3.1 (forced endpoint labels)

Every compatible transition `Q_i -> Q_(i+1)` satisfies

\[
                   \boxed{\alpha_i\in Z_i,
                          \qquad\beta_i\in A_{i+1}.} \tag{3.2}
\]

The newborn has age zero and hence lies in every marked suffix threshold.
The departing coordinate has age `d-1` and hence lies in no proper marked
threshold.  Thus a jointly chosen owner cycle must be directed through the
departure apertures and birth cores of the static chain table.

These endpoint conditions are not sufficient.  For `d=2`, take

\[
 Q=\{1,2,4\},\quad R=\{1,3,4\},\quad
 S_Q=\{1\},\quad S_R=\{3\}.                          \tag{3.3}
\]

The transition removes `2` and inserts `3`, so (3.2) holds.  But the forced
old age-zero class is `{1}`, while the forced new age-one class is `{1,4}`;
the survivor inclusion `{1,4} subset {1}` fails.  Hence any cycle theorem
using only endpoint-labelled Middle Levels edges misses a real age-state
constraint.

## 4. Consequence for the `k=17` rooted flag programme

At `k=17`, `d=3`.  Every certified rank-eight-rooted static flag is a full
flag

\[
                     A\subset B\subset Q.            \tag{4.1}
\]

Put

\[
 D_0=A,\qquad D_1=B\setminus A,\qquad D_2=Q\setminus B.
\]

For two physical rooted flags `f=(A,B,Q)` and
`g=(A',B',Q')`, a Johnson turn

\[
 Q'=Q-\{\alpha\}+\{\beta\}
\]

is literally age-compatible if and only if

\[
 \boxed{\alpha\in Q\setminus B,\qquad
        B'\setminus A'\subseteq A,\qquad
        Q'\setminus B'\subseteq B\setminus A.}       \tag{4.2}
\]

The newborn condition `beta in A'` then follows automatically.  The
intervening rank-nine owner is not an independent attachment:

\[
                         T=Q\cup Q'.                  \tag{4.3}
\]

Therefore the exact lower-side joint object is:

1. choose one full rooted flag at every rank-eight root while covering the
   named lower targets;
2. choose a directed Hamilton cycle through those flags using only arcs
   (4.2); and
3. require the edge colours `Q union Q'` to use every rank-nine owner once.

In a cyclic quotient formulation one additionally retains the physical
phase and nonzero-voltage condition.  This is an exact reduction, not a
relaxation.  It explains both failed sequential strategies in the existing
record: an arbitrary static flag factor can have almost no compatible arcs,
while an arbitrary Middle Levels cycle can have short coordinate runs and
therefore no age spelling.

## 5. A tractable sufficient subclass

Given any rainbow Johnson cycle satisfying (1.1), choose the canonical
refresh schedules (1.2) and form all thresholds

\[
 F^i_t=C^i_0\cup\cdots\cup C^i_t.                   \tag{5.1}
\]

Any residual lower-target bank that is contained, with the required
multiplicities, in this literal threshold deck is carried by the resulting
source word: simply mark one matching occurrence of each target.  This can
be checked by independent multiplicity counts (or a bipartite matching if
occurrences carry additional admissibility labels), in polynomial time.

Thus one concrete sufficient route is

\[
 \boxed{
 \text{rainbow coatom cycle with minimum run }d
 +\text{canonical threshold-deck coverage}.}         \tag{5.2}
\]

The first term solves the complete moving-core spelling and residence row;
the second is the remaining named-target chainization/compiler row.

## 6. Scope

The new unconditional conclusions are:

* for a fixed contracted cycle with no prescribed deeper flags, minimum
  positive `Q`-run `d` is necessary and sufficient for a literal cyclic
  depth-`d` spelling;
* there is no extra cyclic age holonomy;
* all spellings factor independently over coordinate runs, with the exact
  count (1.4);
* a prescribed full flag table has the exact local compatibility test
  (2.3); and
* at `k=17`, the moving-core gate is exactly the full-flag Hamilton/rainbow
  selector (4.2)--(4.3).

What remains open is the correlated choice of the lower-palette-perfect
flag table and compatible rainbow Hamilton cycle, followed by upper shadows,
opening and the terminal compiler.  The theorem does not turn a stationary
owner-local rotor into a one-copy chronology and does not prove
`nu(17)=B(17)` or an all-`k` upper bound.

## 7. Independent finite replay of the coordinate calculation

The standalone source

```text
scratch/audit_age_flag_run_criterion_20260802.cpp
```

exhausts every legal reset/increment age sequence for
`1<=d<=7`, `1<=ell<=18`.  It independently checks both

* feasibility if and only if `ell>=d`; and
* the exact count `f_d(ell-d)` from (1.3)--(1.4).

Compiled and run with `g++ -O3` on the H100 CPU, it reports

```text
PASS_AGE_FLAG_RUN_CRITERION_AND_COUNT d=1..7 ell=1..18
```
