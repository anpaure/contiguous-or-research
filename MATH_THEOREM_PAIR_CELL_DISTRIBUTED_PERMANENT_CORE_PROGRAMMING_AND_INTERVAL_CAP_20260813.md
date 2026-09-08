# Pair-cell clocks have a distributed permanent-core programming face

**Date:** 2026-08-13  
**Status:** unconditional local programming theorem and exact simultaneous cap.  A
long-run pair-cell cycle has a large permanent owner core.  Redistributing those core
coordinates among source phases preserves every middle owner and programs arbitrary
core masks on one short source cell.  For many cells, feasibility is exactly one cyclic
hit/avoid problem per core coordinate.  The theorem does not select a global target-to-
cell atlas or join different pair cells.

## 1. General permanent-core redistribution

Let

\[
                         T=(T_i)_{i\in\mathbb Z_L}          \tag{1.1}
\]

be a cyclic rank-`R` owner trace whose coordinate-positive runs are either constant or
have at least `q` owner positions.  Assume `L>=2q` and put

\[
 P_t=\bigcap_{u=0}^{q-1}T_{t-u},
 \qquad C=\bigcap_iT_i,
 \qquad B_t=P_t-C.                                        \tag{1.2}
\]

Then

\[
                         \bigcup_{t=i}^{i+q-1}P_t=T_i,     \tag{1.3}
\]

and hence

\[
                         \bigcup_{t=i}^{i+q-1}B_t=T_i-C.   \tag{1.4}
\]

For every permanent coordinate `c in C`, choose an emission set
`E_c subseteq Z_L` meeting every cyclic interval of `q` source positions.  Define

\[
 A_t=B_t\cup\{c\in C:t\in E_c\}.                          \tag{1.5}
\]

### Theorem 1.1 (owner-transparent core redistribution)

Every choice of the emission sets gives

\[
                         \bigcup_{t=i}^{i+q-1}A_t=T_i      \tag{1.6}
\]

for all `i`.  Thus all owner values, their chronology, and every resource determined
solely by that owner trace remain unchanged.

#### Proof

Equation (1.4) supplies exactly the nonpermanent part of `T_i`.  The hitting condition
puts every coordinate of `C` into every `q`-window, and no source letter contains a
coordinate outside `P_t subseteq T_i` for a window using it.  This proves (1.6).
\(\square\)

### Corollary 1.2 (immediate-lower-preserving face)

If every `E_c` meets every cyclic interval of `q-1` source positions, then in addition
every width-`q-1` source union remains equal to the consecutive owner intersection

\[
 \bigcup_{t=i+1}^{i+q-1}A_t=T_i\cap T_{i+1}.              \tag{1.7}
\]

Thus the literal immediate-lower source row, the owner row, and all longer source rows
are preserved simultaneously.  This stronger hitting condition is required whenever
the immediate-lower palette must remain a literal source deck, rather than merely a
resource derived abstractly from the unchanged owners.

## 2. Exact one-cell programming

Fix a cyclic source interval `I` of length at most `q-1`, and put

\[
                         U_I=\bigcup_{t\in I}B_t.           \tag{2.1}
\]

### Lemma 2.1 (a `q`-hitting schedule can hit or avoid one short interval)

There are cyclic `q`-interval hitting sets `E^+` and `E^-` such that

\[
                         E^+\cap I\ne\varnothing,
 \qquad                  E^-\cap I=\varnothing.            \tag{2.2}
\]

#### Proof

Write `I=[a,a+ell-1]`, `ell<=q-1`.  Put selected positions immediately before and
after it, at `a-1` and `a+ell`; their cyclic distance through `I` is `ell+1<=q`.
Continue in both directions around the complementary arc, inserting a selected
position whenever the next gap would exceed `q`.  The resulting cyclic gaps are all at
most `q`, which is equivalent to meeting every cyclic `q`-interval, and the set avoids
`I`.  This is `E^-`; adding any point of `I` gives `E^+`. \(\square\)

### Theorem 2.2 (arbitrary permanent-core mask on one cell)

For every `H subseteq C`, there is a redistributed antecedent with

\[
                         \bigcup_{t\in I}A_t=U_I\cup H.    \tag{2.3}
\]

Choose `E_c=E^+` for `c in H` and `E_c=E^-` otherwise.

Consequently a target `S` is realizable on the fixed cell `I` inside this face if and
only if

\[
                         \boxed{U_I\subseteq S\subseteq U_I\cup C.} \tag{2.4}
\]

### Corollary 2.3 (programming while preserving the immediate-lower row)

If `|I|<=q-2`, Theorem 2.2 remains true with every emission set required to meet every
`(q-1)`-interval.  In Lemma 2.1, the two positions bracketing `I` then have distance
`|I|+1<=q-1`; fill the complementary arc with gaps at most `q-1`.  Conversely, a
`(q-1)`-interval cannot avoid a `(q-1)`-hitting schedule.  Hence a width-`q-1` cell can
omit no permanent-core coordinate on this three-shore-preserving face.

## 3. Exact simultaneous interval cap

Now choose a family of marked source intervals `(I_alpha)` and desired target values
`(S_alpha)`.  Keep the variable letters `B_t` fixed.

### Theorem 3.1 (coordinatewise cyclic hit/avoid criterion)

The marked targets are simultaneously realizable by one redistribution (1.5) if and
only if:

1. for every `alpha`,
   \[
             U_{I_\alpha}\subseteq S_\alpha
             \subseteq U_{I_\alpha}\cup C;                 \tag{3.1}
   \]
2. for every `c in C`, there exists a cyclic `q`-interval hitting set `E_c` satisfying
   \[
   E_c\cap I_\alpha\ne\varnothing
       \quad\text{when }c\in S_\alpha,                      \tag{3.2}
   \]
   \[
   E_c\cap I_\alpha=\varnothing
       \quad\text{when }c\notin S_\alpha.                  \tag{3.3}
   \]

#### Proof

The fixed variable contribution to a marked cell is exactly `U_(I_alpha)`, giving
(3.1).  A permanent coordinate occurs in that cell precisely when its emission set
meets the interval, giving (3.2)--(3.3).  The owner equations are equivalent to every
`E_c` meeting every `q`-window by Theorem 1.1.  These conditions are independent for
different core coordinates and are plainly sufficient. \(\square\)

On the immediate-lower-preserving face, replace “`q`-interval hitting” everywhere in
Theorem 3.1 by “`(q-1)`-interval hitting.”  This is again necessary and sufficient.
Any marked cell of width `q-1` must then contain the whole core; arbitrary core masks
remain locally available at widths at most `q-2`.

This is a finite circular-interval constraint system, not a scalar rank or Hall row.
One-cell programmability does not imply simultaneous programmability: negative intervals
for one core coordinate can cover an entire `q`-window, or a positive interval can be
contained in the forced-negative union.

## 4. Specialization to a long-run pair cell

Use the pair-cell notation of
`MATH_THEOREM_PAIR_CELL_LONG_RUN_Q_WINDOW_CLOCK_EXPLICIT_LEAVE_AND_EXACT_SPLICE_CAP_20260813.md`.
Let the cube dimension be `m`, and let its Hamilton Gray cycle have repeated-direction
separation at least `q`.  The permanent owner core consists of all elements in double
pairs together with the sentinel when present, and has rank

\[
                         |C|=R-m.                         \tag{4.1}
\]

Among `q` consecutive owner states, the `q-1` transition directions are distinct.  On
each of those pairs neither physical member lies in the intersection; every untouched
singleton pair contributes its common selected member.  Therefore

\[
                         |B_t|=m-q+1.                     \tag{4.2}
\]

In particular every source-letter cell has the exact programmable rank interval

\[
 \boxed{
 m-q+1\ \le |A_t|\le\ R-q+1.}                             \tag{4.3}
\]

and realizes every set between its fixed `(m-q+1)`-set `B_t` and `B_t union C`.

As `m` varies from `q` to `R-1`, these local rank intervals collectively span the entire
range `1,...,R-q+1`.  If only the Goddyn--Gvozdjak good cells
`m>=q+ceil(3 log_2(R-1))` are retained, the lowest singleton-letter rank supplied this
way is only `Theta(log R)`; the lower ranks and the exponentially many excluded owners
still require a cross-stratum absorber or another clock family.

## 5. Scope and next exact gate

The theorem supplies a large exact source design space inside every good pair-cell
cycle without changing its long-run owner chronology.  It improves the componentwise
clock from one fixed maximal antecedent to a Cartesian product of cyclic hitting-set
choices.

It does not show that every named target has an eligible pair `(cell,I)` satisfying
(3.1), nor that eligible choices can be made occurrence-injectively across all targets,
nor that the resulting per-coordinate interval systems (3.2)--(3.3) pass.  Those three
requirements, coupled to the cross-cell splice ports, are the precise product-group
lower-atlas gate.
