# Every legal screen schedule in the unplanted common-order fibre obeys the reflected law

Date: 2026-08-01  
Status: unconditional finite-active / symbolic-filler classification  
Scope: all sixteen owner-simple common-palette schedules on the three
authenticated ECO connector rows **before endpoint planting**, with one
common coatom order in every block.  No screen schedule in this restricted
fibre supplies an independent quadratic routing direction.  Endpoint
planting and variable block orders are outside the theorem and do break the
reflection law.

## 0. Outcome

There are exactly sixteen choices of intersection/union screens for which
the old and new active paths have the same simple selected screen palettes.
All sixteen are owner-simple, upper-OR transparent and residence neutral.
Among them:

* ten also preserve the immediate lower and upper palettes;
* eight retain an intersection screen at transition zero and are therefore
  compatible with the current endpoint planting;
* six have both properties;
* three minimize the deeper lower exchange to two values in each direction
  at every depth; and
* **zero** break the reflected pair-current invariant.

The six immediate-palette-exact endpoint-plantable schedules are

```text
[1,3,5,7]
[1,3,5,7,9]
[2,5,8,10]
[2,3,5,8,10]
[1,2,5,7,8,10]
[1,2,3,5,7,8,10].
```

The three minimum-deeper-damage schedules are

```text
[1,3,5,7]
[0,2,4,5,6,8,10]
[0,2,3,4,5,6,8,10].
```

Thus the canonical schedule `[1,3,5,7]` is the unique schedule which is
simultaneously endpoint-plantable, immediate-palette exact, and
minimum-damage.  Changing only the screen schedule cannot escape the
quadratic reflection fibre.  This is not a no-go for the actual planted
catalogue: a label-attached adjacent coatom-order twist escapes it while
preserving the repaired endpoint planting.

## 1. General one-sided screen formula

Let

\[
        V_0^\epsilon,V_1^\epsilon,\ldots,V_{11}^\epsilon,
        \qquad \epsilon\in\{0,1\},
\]

be one authenticated old/new active pair.  The two words have the same
owner set and endpoints.  Let `E` be the set of transitions at which the
union screen is used; the complement uses intersection screens.

For `2<=q<=d`, put `t=d+1-q` and

\[
 P_t=\{f_1,\ldots,f_t\},\qquad
 S_t=\{f_{d-t+1},\ldots,f_d\}.
\]

Every `(q+1)`-window lies inside a block or crosses exactly one screen.
The inside-block contributions cancel because the active owner multisets
agree.  At an intersection screen, the two one-sided active bases are both
`V_j^epsilon cap V_(j+1)^epsilon`; the selected intersection palettes
cancel in aggregate.  At a union screen the two one-sided values are

\[
                 J\cup V_j^\epsilon\cup P_t,
       \qquad    J\cup V_{j+1}^\epsilon\cup S_t,      \tag{1.1}
\]

where the fixed core `J` is common to both phases.  Two-sided crossing
windows again depend only on the common active intersection and cancel.

Consequently the entire signed lower change is the sum over `j in E` of
the old/new differences of the two terms in (1.1).  The canonical schedule
collapses this sum to one flag rectangle; other schedules can give the sum
of two flag rectangles.

## 2. Endpoint current identity

For an active coordinate `x`, define

\[
\begin{aligned}
 \alpha_x&=\sum_{j\in E}
   \bigl({\bf1}_{x\in V_j^1}-{\bf1}_{x\in V_j^0}\bigr),\\
 \beta_x&=\sum_{j\in E}
   \bigl({\bf1}_{x\in V_{j+1}^1}-{\bf1}_{x\in V_{j+1}^0}\bigr).
                                                               \tag{2.1}
\end{aligned}
\]

### Lemma 2.1

Every simple common-palette schedule satisfies

\[
                              \boxed{\beta_x=-\alpha_x}          \tag{2.2}
\]

for every active coordinate `x`.

#### Proof

For one Johnson edge,

\[
 {\bf1}_{V_j}+{\bf1}_{V_{j+1}}
 ={f1}_{V_j\cap V_{j+1}}+{\bf1}_{V_j\cup V_{j+1}}             \tag{2.3}
\]

coordinatewise.  The selected upper-union palettes agree between phases.
The complete all-edge intersection palettes agree, and the selected lower
intersection palettes agree, so the complementary selected-upper
intersection palettes agree as well.  Summing (2.3) over `j in E` and
subtracting the phases gives `alpha_x+beta_x=0`.  \(\square\)

## 3. Reflection theorem for the full sixteen-schedule fibre

For a signed depth-`q` occurrence vector `Delta_q`, write

\[
 \deg_q^{(1)}(x)=\sum_{R\ni x}\Delta_q(R),\qquad
 \deg_q^{(2)}(x,y)=\sum_{R\supseteq\{x,y\}}\Delta_q(R).
\]

### Theorem 3.1

For every one of the sixteen simple common-palette schedules, every
authenticated connector row, and every `d>=2`,

\[
                 \deg_q^{(1)}(x)=0                              \tag{3.1}
\]

at every depth and

\[
 \boxed{
   \deg_q^{(2)}(x,y)=\deg_{d+2-q}^{(2)}(x,y)
 }                                                              \tag{3.2}
\]

for every coordinate pair.

#### Proof

The fixed core and filler-only pair currents cancel phasewise.  An
active--active pair receives a signed contribution independent of `t`, so
it is automatically equal at reflected depths.

For an active--filler pair `{x,f_i}`, equations (1.1)--(2.2) give

\[
 \deg_q^{(2)}(x,f_i)
   =\alpha_x\bigl({\bf1}_{i\le t}
                   -{\bf1}_{i>d-t}\bigr).            \tag{3.3}
\]

At reflected depth `q'=d+2-q`, the prefix length is `d-t`, and

\[
 {\bf1}_{i\le t}-{\bf1}_{i>d-t}
  ={\bf1}_{i\le d-t}-{\bf1}_{i>t}.                   \tag{3.4}
\]

This proves (3.2).  Summing (1.1) coordinatewise and using (2.2) proves
(3.1).  \(\square\)

### Corollary 3.2 (screen changes alone do not escape)

Allowing a common-order unplanted search to choose a different legal screen
schedule at every step still preserves

\[
 \deg_q^{(2)}(x,y)-\deg_{d+2-q}^{(2)}(x,y).
\]

Hence schedule diversity alone cannot enlarge the quadratic multiplicity
space.  The authoritative repaired endpoint planting by itself remains
reflected, but label-attached internal adjacent swaps in the `Ica` block
give a complete reflection-odd quadratic basis.  Thus (3.2) is a
classification of the screen-only/common-order fibre, not an invariant of
the physical safe-carrier graph.

## 4. The finite classification

The active words live on six coordinates, so schedule validity is a finite
table.  Exhausting all `2^11` screen choices gives sixteen schedules for
which

1. the selected lower-intersection multisets agree and are simple; and
2. the selected upper-union multisets agree and are simple.

The standard filler case split then upgrades the finite table to every
`d`: two distinct coatoms already fill the filler union, leaving only a
single block letter, a single union screen, and its two adjacent exceptional
intervals.  Residence depends only on the common screen-type word and the
active boundary table.  Thus the owner, OR and residence conclusions are
symbolic in `d`, not an extrapolation from the audit.

Immediate-palette equality and endpoint planting are also finite active
conditions.  Their exhaustive counts are respectively ten, eight, and six
for the intersection.  The complete fixed-length lower deck calculation
shows three schedules with signed mass two per direction at every depth and
thirteen with mass four.

## 5. Audit

Run

```text
python3 scratch/audit_coatom_screen_schedule_reflection_classification_20260801.py
```

The audit independently re-enumerates all sixteen schedules and checks all
three connector rows for `2<=d<=24`.  It verifies owner simplicity and
equality, ordered prefix/suffix OR equality, full interval-OR support
equality, residence boundary equality, immediate palettes, exact signed
lower-deck masses, point balance, and reflected pair equality.

It reports

```text
simple common palette             16
q1 exact                          10
endpoint plantable                 8
q1 exact and endpoint plantable    6
minimum damage                     3
reflection breaking                0
```

with canonical payload SHA-256 recorded in the JSON audit.
