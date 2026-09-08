# Variable-band factorization for the four-box fans

## 1. Outcome

This note gives an exact nonuniform replacement for the fixed-delay erosion
criterion and applies it to the full radius-transfer fan row.

There are two main results.

1. For prescribed monotone middle-witness intervals
   \[
      I_i=[i+\alpha_i,i+\beta_i],
   \]
   central factorability and translation of every nested lower meet have
   exact coordinatewise pin criteria.  The physical window naturally
   assigned to a meet over row indices `[u,v]` is
   \[
      J_{u,v}=\bigcap_{i=u}^{v}I_i
             =[v+\alpha_v,u+\beta_u].
   \]
   It realizes the meet precisely when every common atom has a legal pin in
   this interval.  Atoms absent from the meet are excluded automatically.

2. Nonuniform intervals do **not** reduce the factor slack of the literal
   combined full-fan row to `O(m^2)`.  For every fan of radius `r>=2`, its
   peak-only atom closes the monotone band, while its canonical deepest lower
   meet forces the band to reopen by `2r-1`.  Summing these disjoint offset
   increases over all fans and both orientations gives
   \[
      \boxed{
      d\ge {m(2m^2+3m-5)\over3}=\Omega(m^3).
      }
   \]

Grouping peaks by their common threshold `c=m-H+r` does not repair the
literal construction.  At fixed `c`, a depth-one upper-tail target for
radius `r` can contain only the two peaks of radii `r-1` and `r`.  Therefore
one common `(2,c)`-run can service at most four canonical depth-one
witnesses, and the sum over `c` of the required atom-run counts is
`Omega(m^2)`.  Runs for different threshold atoms can physically overlap,
so this latter count alone is not an `Omega(m^3)` length lower bound.  The
cubic lower bound for the literal row is instead the close/reopen theorem
above.

The obstruction is architectural.  It applies when the canonical combined
fans remain ordered blocks and their lower meets are translated by the
natural intersection windows.  It does not rule out a genuinely global
interleaving that replaces the canonical depth-one upper witnesses and uses
non-core physical windows for the lower targets.

## 2. Monotone interval systems

Let

\[
                  T_1,T_2,\ldots,T_L\subseteq\mathcal B
\]

be prescribed row labels on a finite atom set `mathcal B`.  Let the physical
word have positions `[N]`, where `N=L+d`, and prescribe

\[
 I_i=[\ell_i,r_i]=[i+\alpha_i,i+\beta_i],             \tag{2.1}
\]

with

\[
 \begin{split}
 0&\le\alpha_1\le\cdots\le\alpha_L\le d,\\
 0&\le\beta_1\le\cdots\le\beta_L\le d,\\
 &\alpha_i\le\beta_i.
 \end{split}                                           \tag{2.2}
\]

Both endpoint sequences are strictly increasing, because the base index
increases by one.  We ask for a word `A_1,...,A_N` satisfying

\[
                       \bigvee_{p\in I_i}A_p=T_i
                       \qquad(1\le i\le L).             \tag{2.3}
\]

For an atom `b`, define its central legal positions by

\[
 Z_b=[N]\setminus\bigcup_{i:b\notin T_i}I_i.           \tag{2.4}
\]

No occurrence of `b` can be placed outside `Z_b` without contaminating a
target which excludes it.

### Theorem 1 (exact variable-band factorization)

There is a word satisfying (2.3) if and only if

\[
                 I_i\cap Z_b\ne\varnothing
                 \quad\text{for every }b\in T_i.       \tag{2.5}
\]

When (2.5) holds, the coordinatewise maximal factor

\[
                 A_p^{\max}=\{b:p\in Z_b\}             \tag{2.6}
\]

satisfies (2.3).  Every other factor is obtained by independently choosing,
for each atom `b`, a subset `H_b subseteq Z_b` which hits every positive
interval `I_i` with `b in T_i`, and declaring

\[
                         b\in A_p\iff p\in H_b.          \tag{2.7}
\]

#### Proof

If `b notin T_i`, equality in (2.3) forbids `b` from every position of
`I_i`; hence every occurrence lies in `Z_b`.  If `b in T_i`, at least one
occurrence in `I_i cap Z_b` is necessary.  This proves necessity.

Conversely, choose any hitting subset `H_b` as in (2.7).  A negative target
interval contains no legal occurrence, while a positive target interval is
hit.  The union on every `I_i` is therefore exactly `T_i`.  Taking
`H_b=Z_b` gives (2.6).  QED.

Positions belonging to no prescribed interval permit every atom in the
maximal factor.  They may instead be assigned the empty set unless a later
output witness deliberately uses them.

## 3. Exact run form of central factorability

Fix an atom `b` and write

\[
                       \epsilon_i=1_{b\in T_i}.
\]

Let `[u,v]` be a maximal internal run of ones, so `u>1`, `v<L`, and
`epsilon_(u-1)=epsilon_(v+1)=0`.

### Lemma 2 (exact nonuniform run criterion)

The positive intervals indexed by `[u,v]` retain a legal `b`-position if and
only if

\[
             r_{u-1}+1\le\ell_{v+1}-1,                \tag{3.1}
\]

or equivalently

\[
             \boxed{
             \beta_{u-1}-\alpha_{v+1}\le v-u.
             }                                        \tag{3.2}
\]

When this holds, every positive interval in the run meets the common clean
gap

\[
             G_b(u,v)=[r_{u-1}+1,\ell_{v+1}-1].        \tag{3.3}
\]

Runs touching either end of the row impose no condition.

#### Proof

Take `i in [u,v]`.  If a point `p in I_i` satisfies `p<=r_(u-1)`, then
`ell_i>ell_(u-1)` and hence `p in I_(u-1)`, a negative interval.  Similarly,
if `p>=ell_(v+1)`, then `r_i<r_(v+1)` and `p in I_(v+1)`.  Thus every legal
point of every positive interval lies strictly between the two adjacent
negative intervals.

Conversely, if (3.1) holds, then for every `u<=i<=v`,

\[
 \ell_i\le\ell_v\le\ell_{v+1}-1,
 \qquad
 r_i\ge r_u\ge r_{u-1}+1.
\]

Therefore `I_i` meets (3.3).  Negative intervals farther left or right have
smaller right endpoints or larger left endpoints, so they do not remove this
gap.  This proves the exact criterion.

Substituting (2.1) into (3.1) gives (3.2).  At a left boundary run, the
strict increase `ell_v<ell_(v+1)` supplies a legal point on the left; the
right boundary is dual.  QED.

Combining Lemma 2 over every atom and every internal one-run is equivalent
to Theorem 1.  For a singleton one-run at position `p`, the condition is the
particularly rigid inequality

\[
                         \boxed{\beta_{p-1}\le\alpha_{p+1}.}
                                                               \tag{3.4}
\]

Thus a peak-only atom closes whatever band width was open immediately before
the peak.

## 4. Translating nested meets

Suppose a lower target is supplied as a consecutive meet

\[
                  S_{u,v}=\bigcap_{i=u}^{v}T_i.         \tag{4.1}
\]

The natural physical core of the central witness intervals is

\[
 \begin{split}
 J_{u,v}
   &=\bigcap_{i=u}^{v}I_i\\
   &=[\ell_v,r_u]
    =[v+\alpha_v,u+\beta_u].                           \tag{4.2}
 \end{split}

It is nonempty exactly when

\[
                    \boxed{\beta_u-\alpha_v\ge v-u.}  \tag{4.3}

### Theorem 3 (exact core-pinning theorem)

Assume the central interval system is factorable and `J_(u,v)` is nonempty.
For the maximal factor (2.6),

\[
                  \bigvee_{p\in J_{u,v}}A_p^{\max}
                  =S_{u,v}                              \tag{4.4}

if and only if

\[
                  J_{u,v}\cap Z_b\ne\varnothing
                  \quad\text{for every }b\in S_{u,v}.  \tag{4.5}

For an arbitrary factor with pin sets `H_b`, the corresponding exact
condition is

\[
                  J_{u,v}\cap H_b\ne\varnothing
                  \quad\text{for every }b\in S_{u,v}.  \tag{4.6}

No separate exclusion condition is needed for atoms outside `S_(u,v)`.

#### Proof

Every `J_(u,v)` is contained in every `I_i`, `u<=i<=v`.  If an atom `b` is
absent from `S_(u,v)`, it is absent from at least one `T_i` in this range.
The entire interval `I_i`, and hence its subset `J_(u,v)`, contains no
occurrence of `b` in any central factor.  Thus the OR over the core is always
contained in the meet.

For an atom in the meet, equality holds precisely when its chosen pin set
hits the core.  Taking the maximal pin set gives (4.5), and arbitrary pin
sets give (4.6).  QED.

This condition is simultaneous: if (4.5) holds for every prescribed lower
meet, the one maximal factor realizes all of them at once.

### Corollary 4 (run-local form of the meet pins)

Let `[a,c]` be the maximal `b`-support run containing `[u,v]`, where
`b in S_(u,v)`.  Put

\[
 L_b=\begin{cases}r_{a-1}+1,&a>1,\\1,&a=1,\end{cases}
 \qquad
 R_b=\begin{cases}\ell_{c+1}-1,&c<L,\\N,&c=L.\end{cases} \tag{4.7}
\]

Then the exact maximal-factor pin condition for this target-bit pair is

\[
 \boxed{
   \max(\ell_v,L_b)\le\min(r_u,R_b).
 }                                                        \tag{4.8}

#### Proof

Inside every positive interval of this support run, the legal positions are
exactly the trace of the gap `[L_b,R_b]`: the adjacent negative intervals
dominate every negative interval farther away by endpoint monotonicity.
Intersecting this gap with `J_(u,v)=[ell_v,r_u]` gives (4.8).  QED.

Conditions (4.3) and (4.8) separate two obstructions:

* the chosen central intervals must have a nonempty common core; and
* every atom of the lower meet must survive the neighboring negative
  barriers inside that core.

The fixed-delay erosion identity is the special case
`alpha_i=0,beta_i=D`, where `J_(u,v)=[v,u+D]`.

## 5. General assigned lower windows

The core construction is contamination-free automatically, but it is not
the only possible assignment.  For completeness, prescribe arbitrary
physical intervals `Q_s` for lower labels `S_s`.  For each atom define

\[
 Z_b^*=[N]\setminus
 \left(
   \bigcup_{i:b\notin T_i}I_i
   \ \cup\
   \bigcup_{s:b\notin S_s}Q_s
 \right).                                               \tag{5.1}

### Theorem 5 (exact simultaneous central/lower pinning)

There is one word realizing every central equation

\[
 \bigvee_{p\in I_i}A_p=T_i
\]

and every assigned lower equation

\[
 \bigvee_{p\in Q_s}A_p=S_s
\]

if and only if

\[
 I_i\cap Z_b^*\ne\varnothing\quad(b\in T_i),
 \qquad
 Q_s\cap Z_b^*\ne\varnothing\quad(b\in S_s).          \tag{5.2}

When these conditions hold, putting `b` at every position of `Z_b^*`
realizes all equations.

#### Proof

Every interval whose label excludes `b` forbids `b` at all of its positions;
these are exactly the positions removed in (5.1).  Every interval whose
label includes `b` must retain at least one legal position.  These conditions
are necessary and, independently for each atom, sufficient.  QED.

Thus using a non-core lower window may be beneficial geometrically, but it
adds new negative barriers and can destroy central or other lower pins.  The
core theorem avoids that interaction because `J_(u,v)` is contained in a
central negative interval for every atom absent from the meet.

## 6. Automatic translation of upper joins

If the central intervals are linked in index order,

\[
                         \ell_{i+1}\le r_i+1
                         \quad(1\le i<L),              \tag{6.1}

or equivalently

\[
                         \alpha_{i+1}\le\beta_i,       \tag{6.2}

then for every consecutive row interval `[u,v]`,

\[
                 \bigcup_{i=u}^{v}I_i=[\ell_u,r_v].    \tag{6.3}

Every central factor consequently satisfies

\[
 \bigvee_{p=\ell_u}^{r_v}A_p
   =\bigvee_{i=u}^{v}T_i.                               \tag{6.4}

Hence a linked variable band automatically translates all upper fan joins.
Without (6.1), upper translation is not automatic: the interval hull may
contain physical gap positions unconstrained by the selected central
targets.

## 7. The literal combined fan row

Return to the equal four-box hook geometry.  For every

\[
                         1\le r\le H\le m,
\]

the full combined fan has order

\[
 \begin{split}
  &U_{r-1},\ldots,U_1,U_0,V_1,\ldots,V_{r-1},V_r=A_0,\\
  &A_1,\ldots,A_r,B_{r-1},\ldots,B_1.                 \tag{7.1}
 \end{split}

It has `4r-1` positions.  Include one such block for every `(H,r)` and its
transpose for the second orientation, exactly as in the all-depth shadow
walk.

Let `p_(H,r)` be the position of `U_0`, let `u_(H,r)` be the shared position
`V_r=A_0`, and let `v_(H,r)` be the position of `B_1`.

For `r>=2`, the atom

\[
                     b_{H,r}=(2,m-H+r)                \tag{7.2}

occurs at `U_0` but at neither immediate neighbour `U_1,V_1`.  Its incidence
word therefore has the internal singleton run `[p_(H,r),p_(H,r)]`, regardless
of all other blocks in the row.  Lemma 2 forces

\[
             \beta_{p_{H,r}-1}\le\alpha_{p_{H,r}+1}.  \tag{7.3}

The canonical lower witness from `A_0` through `B_1` has `2r` terms and
lower depth `2r-1`.  If it is translated by its natural core, even mere
nonemptiness of that core requires

\[
             \beta_{u_{H,r}}-\alpha_{v_{H,r}}
             \ge2r-1.                                  \tag{7.4}

Since

\[
 p_{H,r}+1\le u_{H,r}\le v_{H,r},
\]

monotonicity and (7.3)--(7.4) give

\[
 \begin{split}
 \beta_{u_{H,r}}
 &\ge\alpha_{v_{H,r}}+(2r-1)\\
 &\ge\alpha_{p_{H,r}+1}+(2r-1)\\
 &\ge\beta_{p_{H,r}-1}+(2r-1).                       \tag{7.5}
 \end{split}

Thus `beta` must increase by at least `2r-1` between the left neighbour of
the peak and the start of the deep lower witness.

### Theorem 6 (cubic variable-slack obstruction)

Let a row contain pairwise position-disjoint, contiguous literal copies of
the full combined fan blocks (7.1), with no insertions inside a copy and no
physical occurrence shared by two copies.  The copies may be placed in any
block order, for every `1<=r<=H<=m` and both coordinate-pair orientations.
Suppose monotone intervals (2.1)--(2.2)

1. factor every middle occurrence in the row, and
2. translate in each fan the canonical deepest lower meet
   `A_0,...,A_r,B_(r-1),...,B_1` by its core interval.

Then its total slack satisfies

\[
 \boxed{
 d\ge
 2\sum_{H=1}^{m}\sum_{r=2}^{H}(2r-1)
 =\frac{m(2m^2+3m-5)}3.
 }                                                       \tag{7.6}

#### Proof

For every fan, (7.5) gives an increase of at least `2r-1` in the monotone
sequence `beta`.  The index intervals

\[
          [p_{H,r}-1,u_{H,r}]
\]

belong to disjoint row blocks and hence are pairwise disjoint, regardless of
the block order.  The sum of increases of one monotone sequence over
pairwise disjoint ordered intervals is at most its total increase, which is
at most `d`.  There are two orientations.  Finally,

\[
 \sum_{r=2}^{H}(2r-1)=H^2-1,
\]

and

\[
 2\sum_{H=1}^{m}(H^2-1)
 =2\left(\frac{m(m+1)(2m+1)}6-m\right)
 =\frac{m(2m^2+3m-5)}3.
\]

This proves (7.6).  QED.

The obstruction uses only core nonemptiness, not the stronger atom-pin
conditions (4.8).  Hall conflicts or failed pins can only make the
factorization harder.

## 8. Why grouping peaks by `c` does not preserve the fans

For one orientation, put

\[
                         c=m-H+r.
\]

At fixed `c`, write `delta=m-c`.  The admissible fans have

\[
 H=\delta+r,\qquad1\le r\le c,
\]

and their peaks are

\[
 P_{c,r}=U_0=(\delta+r,c,0,m-r).                      \tag{8.1}

All `c` peaks contain the common atom `(2,c)`.  This suggests moving them
into one long run and paying for one plateau instead of `c` plateaus.

The depth-one upper target in fan `r` is

\[
 Y_{c,r}=U_0\vee V_1
        =(\delta+r,c,0,m-r+1).                         \tag{8.2}

Among the other peaks in this `c`-family,

\[
 P_{c,s}\le Y_{c,r}
 \quad\Longleftrightarrow\quad
 s\le r\text{ and }s\ge r-1.                         \tag{8.3}

Thus only `P_(c,r)` and, when it exists, `P_(c,r-1)` may occur inside any
OR witness for `Y_(c,r)`.

### Proposition 7 (peak-grouping obstruction)

Suppose the canonical peak occurrence `P_(c,r)` and the corresponding
`V_1` occurrence are retained as endpoints of a contiguous witness for
every `Y_(c,r)`.  Here a run means a maximal atom-positive run in the full
row.  In any such run containing consecutive `(2,c)`-positive peaks, at most
four distinct radii can use that run for their canonical depth-one witness.
Consequently the fixed-`c` family needs at least `ceil(c/4)` distinct runs
of the atom `(2,c)`.  Summed over all `c` and both orientations, the number
of **atom-run incidences** is `Omega(m^2)`.

#### Proof

The term `V_1` omits `(2,c)`, so it lies outside the positive peak run.  The
witness interval from `P_(c,r)` to `V_1` must travel from that peak to one of
the two boundaries of the run.  Every peak encountered on the way belongs
to the witness and must be coordinatewise at most `Y_(c,r)`.  By (8.3), at
most `P_(c,r)` and `P_(c,r-1)` are allowed.  Therefore `P_(c,r)` must be one
of the first two or last two distinct peaks in its run.  A run has at most
four such radii.

There are `c` required radii, hence at least `ceil(c/4)` `(2,c)`-runs.
Summing `c=1,...,m` and doubling for the two orientations gives

\[
 2\sum_{c=1}^{m}\left\lceil\frac c4\right\rceil
 =\Omega(m^2).
\]

QED.

The sum here is over different threshold atoms.  A physical row segment can
be a positive run for many atoms `(2,c)` simultaneously, and repeating one
point can pad all those atom runs at once.  Therefore Proposition 7 by itself
does **not** turn the `Omega(m^2)` atom-run incidence count into
`Omega(m^3)` physical length.  If a proposed construction isolates the
different `c`-groups in disjoint physical regions, then the runs are
physically disjoint and fixed delay `h=Theta(m)` does cost `Omega(m^3)`;
a nested global grouping across different `c` is not excluded by this
proposition alone.

What Proposition 7 does prove unconditionally is that grouping all `c`
peaks into one common run destroys all but `O(1)` of the canonical
depth-one upper witnesses.  Any more efficient global grouping must replace
most of those witnesses or exploit additional nonpeak terms.

For a genuinely variable band, run length and offset slack trade against one
another through (3.2).  Proposition 7 alone is not a universal cubic lower
bound for every reordered row: one could place all peak runs in a narrow
initial band and open the band only later.  The cubic lower bound for the
literal combined row is instead Theorem 6, where each peak is followed in
the same block by its deep lower witness and the close/reopen costs cannot be
reordered away.

## 9. Exact scope and remaining escape routes

Theorems 1--5 are general exact interval-factorization statements.  Theorem
6 and Proposition 7 have narrower architectural hypotheses.

The cubic obstruction can be escaped only by changing at least one of the
following features.

1. **Break the combined fan blocks.**  Separate peak runs from their deep
   lower witnesses so that the close/reopen increments in (7.5) are no
   longer disjointly charged once per fan.
2. **Replace canonical depth-one upper witnesses.**  Proposition 7 prevents
   large `c`-groups only because every `Y_(c,r)` is still witnessed through
   `P_(c,r)` and its canonical `V_1`.
3. **Use non-core lower windows.**  Theorem 6 charges the necessary core
   width (4.3).  Arbitrary lower windows are governed instead by Theorem 5
   and introduce their own negative-barrier pin constraints.
4. **Reuse middle occurrences globally.**  The literal all-depth fan row
   already has leading length about `3M_m`; even a hypothetical
   `O(m^2)` factor slack would not make it a width-plus-surface word.

Accordingly, grouping peak-only runs by `c` is not the missing local repair.
Within the full literal fan architecture, nonuniform monotone endpoints still
cost `Omega(m^3)`.  A possible surface-error theorem must globally interleave
fan arms, peaks, and lower witnesses and must be checked against the exact
pin conditions (4.8) or the fully general conditions (5.2).
