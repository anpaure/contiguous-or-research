# The nested alternating-pair broad ledger has no partial line realization

## 1. Outcome

`MULTISCALE_DIRECTION_COUPLING_NEXT.md` constructs one common contracted
scalar process with broad length measure

\[
\mu(ds)=2\mathbf 1_{[1,2]}(s)\,ds
\]

and modified seam value strictly above four at every threshold.  Its original
direction-labelled lift was shown non-realizable only in the lifetime-
saturating case, where essentially every reflected seam is absorbed.

This note removes that qualification for this process.  Even after choosing
an arbitrary *partial* absorbed subfamily and arbitrary directions for it,
the positive-line geometry forces

\[
\limsup_{c\downarrow1}U(c)
\le {1525\over384}
=3.97135416\ldots<4.                                      \tag{1.1}
\]

Thus no actual marked-line realization of the alternating-pair process can
meet the necessary condition `U(c)>=4` at every threshold.

This is not yet a proof for every broad or mixed profile.  It eliminates the
single explicit nested scalar survivor which previously showed that threshold
contraction alone was insufficient.

## 2. A positive-line coverage inequality

Let `nu_x,nu_y,nu_z` be submeasures of Lebesgue measure on `[0,1]`.  Put

\[
A=\sum_i\nu_i([0,1]),\qquad
\tau=\sum_i\int_0^1t\,d\nu_i(t),
\]

and

\[
I=\sum_{i<j}\iint_{t+u\le1}d\nu_i(t)d\nu_j(u).               \tag{2.1}
\]

### Lemma 2.1

Every such triple satisfies

\[
\boxed{\tau+I\ge A-{1\over2}.}                               \tag{2.2}
\]

The right side may of course be replaced by zero when `A<1/2`.

### Proof

For every direction define the complementary level measure, reflected about
`1/2`, by

\[
d\bar\nu_i(x)=dx-d\nu_i(1-x).                                \tag{2.3}
\]

It is nonnegative because `nu_i<=dt`.  Put

\[
L=\sum_i\int_0^1x\,d\bar\nu_i(x)
\]

and

\[
J=\sum_{i<j}\iint_{x+y\ge1}d\bar\nu_i(x)d\bar\nu_j(y).       \tag{2.4}
\]

Expanding the three complementary products gives

\[
L={3\over2}-A+\tau,
\qquad
J={3\over2}-2A+2\tau+I,                                     \tag{2.5}
\]

and hence

\[
L-J=A-(\tau+I).                                               \tag{2.6}
\]

It remains to show `L-J<=1/2`.  Use the unit triangle

\[
\Delta=\{(x,y):x\ge0,\ y\ge0,\ x+y\le1\},
\qquad |\Delta|={1\over2}.                                   \tag{2.7}
\]

Its three families of lines parallel to the sides may be indexed by
`x in [0,1]` so that a line of index `x` has normalized length `x`, and two
lines in different directions intersect precisely when their indices sum to
at least one.  At finite mesh, select in direction `i` the lines represented
by `bar(nu)_i`.  Inclusion--exclusion for their union inside `Delta` gives

\[
L-J+T=|\text{selected-line union}|\le{1\over2},               \tag{2.8}
\]

where `T>=0` is the number/measure of actual three-line concurrence points.
Thus `L-J<=1/2`.  Approximate dominated measures by the finite level sets (or
apply the same identity to their layer-cake sets) and pass monotonically to
the limit.  Combining with (2.6) proves (2.2).  QED.

The triple term has the favorable sign: additive concurrence only strengthens
the inequality.

## 3. Apply the inequality to absorbed reflected seams

In the alternating-pair process, at thresholds `c downarrow 1` all but
vanishing seam mass has

\[
p=3-s,\qquad z=0,\qquad1\le s\le2.                            \tag{3.1}
\]

If such a seam is absorbed, its allowed level interval collapses to

\[
[p-1,2-s]=\{2-s\}.                                            \tag{3.2}
\]

Write

\[
t=2-s.
\]

The total reflected seam supply becomes `2 dt` on `[0,1]`.  Let `nu_i` be
the absorbed successor-level measure in direction `i`.  Same-line uniqueness
gives

\[
\nu_i\le dt,\qquad \sum_i\nu_i\le2dt.                         \tag{3.3}
\]

The absorbed-line inequality from `ABSORBED_FLOW_COAREA.md` says

\[
\ell(c)\le2f(c)-\tau_A(c)-\iota_A(c).                         \tag{3.4}
\]

For the broad tail, `f(c)->2` and `ell(c)->3` as `c downarrow1`.
Consequently every subsequential absorbed limit obeys

\[
E:=\tau+I\le1.                                                \tag{3.5}
\]

Lemma 2.1 now yields

\[
\boxed{A\le{3\over2}.}                                       \tag{3.6}
\]

No direction-balance or off-diagonal-flow relaxation was used in obtaining
(3.6); imposing them can only reduce the feasible absorbed family.

## 4. Weighted value of the absorbed seams

For a reflected zero-gap seam, the saving lost when it is absorbed is

\[
\phi(p,s,0)=ps=(1+t)(2-t)=2+t-t^2
={9\over4}-\left(t-{1\over2}\right)^2.                        \tag{4.1}
\]

Let

\[
B=\sum_i\int_0^1(2+t-t^2)\,d\nu_i(t)                         \tag{4.2}
\]

be the total saving value protected by absorption.  From (3.3), the total
density is at most two.  Among measures of mass `A` and density at most two,
the centered second moment is minimized by density two on the interval of
length `A/2` centered at `1/2`.  Therefore

\[
\sum_i\int\left(t-{1\over2}\right)^2d\nu_i(t)
\ge {A^3\over48}.                                             \tag{4.3}
\]

Equations (3.6), (4.1), and (4.3) give

\[
B\le {9A\over4}-{A^3\over48}
\le {27\over8}-{27\over384}
={423\over128}.                                               \tag{4.4}
\]

The scalar function is increasing throughout `0<=A<=3/2`, so the last
substitution is valid.

## 5. Strict-sub-four conclusion

At `c downarrow1`, the broad process has

\[
3c+2e_c\longrightarrow5,
\qquad H_c\longrightarrow0.                                  \tag{5.1}
\]

If every reflected seam were nonabsorbed, its total saving would be

\[
2\int_0^1(2+t-t^2)\,dt={13\over3}.                            \tag{5.2}
\]

Absorption can protect at most the amount `B` in (4.4).  Hence

\[
\begin{aligned}
\limsup_{c\downarrow1}U(c)
&\le5-\left({13\over3}-{423\over128}\right)\\
&={1525\over384}
=4-{11\over384}.                                             \tag{5.3}
\end{aligned}
\]

For all sufficiently small fixed continuity thresholds, the modified
first-dangerous assignment therefore has value below four by a fixed margin
(for example `11/768` after absorbing approximation errors).  The
run-spectrum/large-defect transfer then excludes a line-realizable lift of
this nested alternating-pair process from the subquadratic-defect regime.

## 6. Exact scope

Proved here:

1. the universal positive-line inequality (2.2);
2. the sharp-enough absorbed mass bound `A<=3/2` for the paired broad limit;
3. the weighted absorption bound `B<=423/128`; and
4. strict exclusion of every partial actual-line lift of the one nested
   alternating-pair scalar survivor.

Not proved here:

1. that every broad profile has the paired coupling `p=3-s,z=0` near one;
2. that every mixed profile has a strict-sub-four threshold;
3. the three-box OR lemma or its negation; or
4. the original all-`k` OR conjecture.

The remaining mixed-profile problem can no longer cite the alternating-pair
ledger as a physically viable survivor.  A counterprocess must change its
length coupling and/or retain positive gap mass near threshold one while
satisfying the same line-union inequality.
