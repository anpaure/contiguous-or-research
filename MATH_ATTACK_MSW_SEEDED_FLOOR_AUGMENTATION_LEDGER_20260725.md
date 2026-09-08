# Exact floor-calibrated MSW-seeded augmentation ledger

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let

\[
 n=2m+1,
 \qquad
 W=\binom{n}{m},
 \qquad
 T=\frac Wn=\operatorname {Cat}_m,
\]

and fix an exact Mütze--Standke--Wiechert middle wreath factor with
\(T\) wreaths.  Augment a seed wreath by designating, in each lower rank
\(m-q\) and complementary upper rank \(m+1+q\), exactly

\[
 c_q=\left\lfloor\frac{N_q}{T}\right\rfloor
 =\left\lfloor\frac{nN_q}{W}\right\rfloor,
 \qquad
 N_q=\binom n{m-q}.
\]

If conflict-free legal augmentations can be selected for \(T-L\) seed
wreaths, then the exact certified number of holes in either signed
depth-\(q\) row is

\[
 \boxed{H_q=\delta_q+Lc_q,\qquad
 \delta_q=N_q-Tc_q.}
\]

For

\[
 Q=\left\lceil\sqrt{m\log m}\right\rceil,
\]

the total floor defect is \(o(W)\), and

\[
 \sum_{q=1}^Qc_q
 =(1+o(1))\frac{n\sqrt{\pi m}}2.
\]

Consequently the exact floor-template leave criterion is

\[
 \boxed{
 \sum_{q=1}^Q(H_q^-+H_q^+)=o(W)
 \iff
 L=o\!\left(\frac{T}{\sqrt m}\right).}
\]

This is sharper by a factor \(\sqrt{\log m}\) than the crude requirement
\(L=o(T/Q)\).  The reason is that the calibrated quotas have a Gaussian
profile: their sum is \(\Theta(n\sqrt m)\), not \(\Theta(nQ)\).

The matching statement still remains open.  The note identifies exactly
what it must preserve and separates genuine literal compatibility from
priority/nesting conditions used only as a construction device.

There are two different matching targets.  The common-tag target above is
convenient for one augmented-hyperedge construction, but literalization
itself permits independent row-specific selections.  In that weaker and
more exact formulation, row \((q,\pm)\) may have its own leave
\(L_q^\pm\), and the sharp ledger is

\[
 2\sum_q\delta_q+
 \sum_qc_q(L_q^-+L_q^+)=o(W).
\]

No common set of discarded seeds is physically required.

## 1. The seed factor and its symmetric ranks

Fix cyclic orders \(\pi_1,\ldots,\pi_T\) whose length-\(m\) intervals
partition \(\binom{[n]}m\).  Complements of those intervals are the
length-\((m+1)\) intervals in the reversed/shifted cyclic orders, so the
same seeds also partition \(\binom{[n]}{m+1}\).

For \(q\ge0\), put

\[
 \mathcal L_q=\binom{[n]}{m-q},
 \qquad
 \mathcal U_q=\binom{[n]}{m+1+q}.
\]

Complementation gives

\[
 |\mathcal L_q|=|\mathcal U_q|=N_q.
 \tag{1.1}
\]

The two central rows \(q=0\) are already covered exactly by the seed
factor.  Only \(q\ge1\) enters the augmentation matching.

## 2. Exact floor calibration

Define

\[
 \lambda_q=\frac{N_q}{T}=\frac{nN_q}{W},
 \qquad
 c_q=\lfloor\lambda_q\rfloor,
 \qquad
 \delta_q=N_q-Tc_q.
 \tag{2.1}
\]

Then

\[
 \boxed{0\le\delta_q<T,\qquad
 \delta_q=T\{\lambda_q\}.}
 \tag{2.2}
\]

The number \(c_q\) is the largest constant per-seed quota compatible
with a target-disjoint selection of all \(T\) seeds.  Indeed,

\[
 Tc_q\le N_q<T(c_q+1).
 \tag{2.3}
\]

Thus a uniform template cannot designate \(c_q+1\) targets at this row on
every seed.  Conversely, \(c_q\) leaves exactly \(\delta_q\) forced holes.

If one wants zero floor holes, the exact alternative is a heterogeneous
floor/ceiling menu: precisely \(\delta_q\) seeds receive quota \(c_q+1\)
and the remaining \(T-\delta_q\) receive quota \(c_q\).  That is a
strictly stronger simultaneous bonus-placement problem and is not assumed
below.

## 3. Exact matching-leave formula

Form the seeded augmentation hypergraph as follows.

* There is one tag for each seed wreath.
* A legal augmentation of seed \(i\) contains its tag and, for every
  \(1\le q\le Q\), exactly \(c_q\) actual cyclic intervals from
  \(\mathcal L_q\) and \(c_q\) actual cyclic intervals from
  \(\mathcal U_q\), all belonging to the same cyclic order \(\pi_i\).

Let \(M\) be a matching of augmentations of size \(T-L\).  Since \(M\)
is target-disjoint, it certifies exactly \((T-L)c_q\) distinct targets in
each signed depth-\(q\) row.  Therefore

\[
 \begin{aligned}
 H_q^-=H_q^+
 &=N_q-(T-L)c_q\\
 &=\boxed{\delta_q+Lc_q}.
 \end{aligned}
 \tag{3.1}
\]

The unaugmented \(L\) seed wreaths are still emitted in their middle-only
form, so they create no central-rank holes.  Consequently the complete
certified band-hole count is exactly

\[
 \boxed{
 \mathcal H_Q(L)
 =2\sum_{q=1}^Q\delta_q
  +2L\sum_{q=1}^Qc_q.}
 \tag{3.2}
\]

If instead one uses an unseeded augmented matching and discards its
unmatched tags entirely, there are an additional \(2nL\) central holes.
This changes none of the asymptotic leave thresholds below.

## 4. Gaussian quota sum

The exact rank ratio is

\[
 r_q:=\frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+2+i}.
 \tag{4.1}
\]

Uniformly for \(q=o(m^{2/3})\),

\[
 \log r_q
 =-\frac{q(q+1)}m
 +O\!\left(\frac{q^3}{m^2}+\frac qm\right).
 \tag{4.2}
\]

Our choice \(Q=\lceil\sqrt{m\log m}\rceil\) lies in this range.  Gaussian
summation and the negligible tail beyond \(Q\) give

\[
 \sum_{q=1}^Qr_q
 =\frac{\sqrt{\pi m}}2+O(1).
 \tag{4.3}
\]

Since \(c_q=nr_q+O(1)\),

\[
 \boxed{
 C_Q:=\sum_{q=1}^Qc_q
 =(1+o(1))\frac{n\sqrt{\pi m}}2.}
 \tag{4.4}
\]

Notice that (4.4) is independent, to first order, of the extra
\(\sqrt{\log m}\) in \(Q\).  Rows beyond the Gaussian window carry
negligible calibrated quota.

## 5. The floor ledger is automatically small

By (2.2),

\[
 \Delta_Q:=2\sum_{q=1}^Q\delta_q<2QT.
 \tag{5.1}
\]

As \(T=W/n\),

\[
 \frac{\Delta_Q}{W}
 <\frac{2Q}{n}
 =O\!\left(\sqrt{\frac{\log m}{m}}\right)
 =o(1).
 \tag{5.2}
\]

Thus all arithmetic floor defects are coefficient-safe without a bonus
construction.

## 6. Sharp leave threshold for the floor template

Combining (3.2), (4.4), and (5.2),

\[
 \mathcal H_Q(L)=o(W)
 \quad\Longleftrightarrow\quad
 LC_Q=o(W).
 \tag{6.1}
\]

Since \(W=nT\), equation (4.4) turns this into

\[
 \boxed{
 L=o\!\left(\frac{W}{n\sqrt m}\right)
 =o\!\left(\frac{T}{\sqrt m}\right).}
 \tag{6.2}
\]

This is exact for the certified floor-template ledger: if (6.2) fails,
the leave term in (3.2) is not \(o(W)\); if (6.2) holds, it is.

The often-used bound \(c_q\le n\) gives only

\[
 \mathcal H_Q(L)\le2QT+2nQL,
\]

and hence the unnecessarily strong condition \(L=o(T/Q)\).  Gaussian
summation recovers the factor \(Q/\sqrt m\asymp\sqrt{\log m}\).

### 6.1 The weaker row-specific criterion

At signed row \((q,\varepsilon)\), suppose a target-disjoint phase
selection fully supplies the quota \(c_q\) on exactly
\(T-L_q^\varepsilon\) seed wreaths.  Choices made in different ranks do
not conflict, because their physical target vertices lie in disjoint
Boolean ranks.  The exact certified holes are

\[
 H_q^\varepsilon=\delta_q+L_q^\varepsilon c_q.
 \tag{6.3}
\]

Thus the weakest floor-ledger condition is

\[
 \boxed{
 \sum_{q=1}^Qc_q(L_q^-+L_q^+)=o(W).}
 \tag{6.4}
\]

The common-leave condition (6.2) is the specialization
\(L_q^-=L_q^+=L\).  Requiring that specialization is useful only when the
selection theorem packages all ranks into one common augmented edge.

## 7. Literal contiguous-OR realization

For one seed order \(\pi\), put

\[
 E_t=I_\pi(t,m-Q).
\]

Emit

\[
 E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2Q}.
 \tag{7.1}
\]

Every union of \(s\) consecutive entries in the legal range is the cyclic
interval

\[
 E_t\cup\cdots\cup E_{t+s-1}
 =I_\pi(t,m-Q+s-1).
 \tag{7.2}
\]

Hence (7.1) covers every designated interval in every rank from \(m-Q\)
through \(m+Q+1\).  Concatenating (7.1) over all \(T\) seed wreaths costs

\[
 T(n+2Q+1)
 =W+O(QT)
 =W+o(W).
 \tag{7.3}
\]

Append the holes counted in (3.2) literally.  The ranks outside the band
also have total size \(o(W)\) at
\(Q=\lceil\sqrt{m\log m}\rceil\), by the central-binomial Gaussian tail.
Thus (6.2) gives a literal word of length \(W+o(W)\).

### Minimal compatibility conditions

For this literalization, the augmentation needs only the following.

1. **Seed preservation.**  Every augmentation tagged by seed \(i\) uses
   one cyclic order whose length-\(m\) wreath is exactly the \(i\)-th MSW
   seed wreath.  Rotation and reversal are harmless.
2. **Physical incidence.**  Every designated lower or upper target is an
   actual cyclic interval of that same order at the stated rank and phase.
3. **Target disjointness.**  The selected augmentations are disjoint in
   every protected target row.  This is precisely the matching condition.
4. **One augmentation per seed.**  Tag disjointness enforces this.

No separate factorability, pin-survival, or row-by-row gluing theorem is
needed after these four conditions: (7.2) is the literal factorization.

A common priority order with nested phase sets is a useful sufficient
encoding for constructing the matching, but it is **not** required by
literalization itself.  Arbitrary phase subsets at different depths are
legal provided they are actual intervals of the same seed order.  If one
uses the heterogeneous floor/ceiling bonus menu, the additional global
condition is exactly that \(\delta_q\) seeds receive the bonus at signed
depth \(q\); any plateau-nesting restriction belongs to the chosen
priority algorithm, not to the OR identity.

For one fixed seed factor there is a further limitation.  Its collection
of middle intervals determines each seed cyclic order up to dihedral
symmetry, so phase selection cannot create a lower target absent from the
seed's existing interval rows.  At one signed depth the selection problem
is just a bipartite \(c_q\)-star matching between seed wreaths and their
actual rank targets.  Its exact Hall condition on a proposed seed set
\(I\) is

\[
 \boxed{|N_q(A)|\ge c_q|A|\quad(A\subseteq I).}
 \tag{7.4}
\]

Consequently a fixed factor with a macroscopic row-support hole cannot be
repaired by re-prioritizing its phases.  One must change the exact wreath
factor, use a broader trajectory catalogue, or pay the holes.

## 8. Exact remaining theorem and the canonical-seed obstruction

The canonical MSW factor is not a viable fixed seed for the theorem below.
Its audited first-shadow support has \(\Theta(W)\) holes (equivalently, the
recorded \(\operatorname {Cat}_{m-4}\)-scale packet obstruction persists
with macroscopic total defect).  Since a wreath support fixes its cyclic
order up to dihedral symmetry, no designation or priority choice can add
one of those missing intervals.  Therefore one must first perform global
exact-factor trades replacing \(\Omega(T)\) canonical wreaths, or quantify
over an as-yet-unknown exact wreath factor \(F_m\) with the required row
support.

For such a variable exact factor, the coefficient-one target is:

The coefficient-one target in the MSW-seeded lane is now:

> Construct, from the legal augmentation menus of the \(T\) seed
> wreaths, a target-disjoint matching covering
> \[
>  T-o(T/\sqrt m)
> \]
> seed tags simultaneously through
> \(Q=\lceil\sqrt{m\log m}\rceil\).

This theorem is weaker than the previously stated
\(T-o(T/Q)\) target by a factor \(\sqrt{\log m}\), and it is exactly sharp
for the floor-calibrated literal-repair ledger.  It is not proved here.

For literal OR coverage alone, the still weaker alternative is to prove
the row-specific weighted-leave condition (6.4).  Any claim that a common
all-depth tag matching is logically necessary must therefore include the
extra priority/trajectory constraint which makes the row choices
inseparable.
