# Audit of the unrestricted rank-depth majorization claims

## Verdict

The three displayed inequalities are valid, subject to their stated range
conditions and one localization detail in the full-core proof.

1. The width-profile majorization is correct and genuinely useful.
   Distinct selected rank-`r` right endpoints make its suffix regions
   disjoint, so neither witnesses nor holes are counted twice.
2. The endpoint scalar bound is correct, but it is strictly weaker than a
   simple majorization obtained by using all right endpoints of the short
   band.  It should not be advertised as the sharp consequence.
3. The full-core prefix/suffix bound is correct when `C=M-sigma>=d`.  The
   overlap calculation applies because the certified labels can be chosen in
   the `q` shortest physical cells of each prefix/suffix chain.  Since every
   lower target has one fixed selected witness, the two label families can
   overlap only at identical physical cells.
4. At `sigma=0` one obtains a completely filled short band and an exact
   fixed-delay central row.  This does not by itself force a one-rank-per-row
   grading or any upper-shadow theorem.
5. In odd dimension, conditional on `sigma>=d-1`, the proposed endpoint
   substitution misses equality by exactly `d^2` at both `q=d` and `q=d-1`.
   The condition is essential: `k=9,r=5,d=2` has `sigma=0`.

An arithmetic and finite-geometry checker is
`scratch/check_rank_depth_majorisation.py`.

## 1. Setup and conventions

Fix `k,r` and put

\[
 M=\binom{k}{r},\qquad n=M+d,
\]

\[
 \Lambda_s=\sum_{a=1}^{s}\binom{k}{a}
 \quad(s\ge1),\qquad \Lambda_s=0\quad(s\le0).
\tag{1.1}
\]

The short band is

\[
 \mathcal B_{n,d}=\{[a,b]:1\le a\le b\le n,\ b-a+1\le d\}.
\]

Its size is

\[
 |\mathcal B_{n,d}|=dn-\binom d2
 =dM+\binom{d+1}{2}.
\tag{1.2}
\]

Choose one short witness for every nonempty target of rank below `r`.
There are `Lambda_{r-1}` chosen cells.  Define the holes to be all remaining
short cells.  Then

\[
 \sigma=dM+\binom{d+1}{2}-\Lambda_{r-1}
\tag{1.3}
\]

is exactly the number of holes.

Independently choose one witness interval for every rank-`r` target.  Equal
rank targets are incomparable, so their selected intervals are pairwise
nonnested.  Their left endpoints are distinct, their right endpoints are
distinct, and the two endpoint orders agree.  Every selected rank-`r`
witness has physical width at most `d`, where

\[
 \operatorname{width}[a,b]=b-a.
\]

Let `x_j` be the number of selected rank-`r` witnesses of width `j`,
`0<=j<=d`.  Thus

\[
 \sum_{j=0}^{d}x_j=M.
\tag{1.4}
\]

## 2. Audit of the width-profile theorem

### Theorem 2.1

For every integer `u>=1`,

\[
 \boxed{
 \Lambda_{r-u}\ge
 \sum_{j=u}^{d}(j-u+1)x_j-\sigma.
 }
\tag{2.1}
\]

### Proof

Let `I=[a,b]` be one selected rank-`r` interval of width `j`.  Its `j`
proper suffix cells are

\[
 [a+1,b],[a+2,b],\ldots,[b,b].
\tag{2.2}
\]

They all lie in the short band.  Let `h_I` of them be holes.  Every nonhole
is the distinguished witness of one lower target.  These `j-h_I` selected
values form a strict inclusion chain: the physical suffixes are nested, and
two chosen lower targets are different.

In any strict chain below a rank-`r` set, at most `u-1` members can have rank
strictly above `r-u`, because only the ranks

\[
 r-u+1,\ldots,r-1
\]

are available.  Hence the suffixes of `I` certify at least

\[
 \max\{j-h_I-u+1,0\}
\tag{2.3}
\]

selected targets of rank at most `r-u`.

Different selected rank-`r` intervals have different right endpoints.
Therefore their suffix-cell families (2.2) are disjoint as sets of physical
cells.  It follows that

\[
 \sum_Ih_I\le\sigma.
\tag{2.4}
\]

There is also no cross-endpoint label collision: one distinguished witness
was chosen for each lower target, so different selected physical cells have
different target labels.

For `j>=u`,

\[
 \max\{j-h_I-u+1,0\}\ge j-u+1-h_I.
\]

Summing over all selected central intervals of width at least `u`, and then
using (2.4), proves (2.1).  QED.

### Audit notes

The proof does not assume that every proper suffix has a lower-rank OR.  A
suffix with the same rank-`r` value, a duplicate value, or an unselected
lower value is simply a hole relative to the distinguished lower-witness
packing.  This is exactly what makes the `-sigma` charge sound.

The right-endpoint uniqueness is indispensable.  It holds for selected
equal-rank witnesses by noncontainment; it would not hold for an arbitrary
multiset of central intervals.

Theorem 2.1 is a real profile-sensitive refinement of the scalar rank count.

## 3. Audit of the selected-endpoint bound

Number physical positions from `1` to `n`.  For a right endpoint `b`, put

\[
 c_b=\min(d,b).
\tag{3.1}
\]

This is the number of short cells ending at `b`.  Let `E` be the `M` selected
rank-`r` right endpoints.  If the selected central interval ending at `b`
has width `w_b`, let `h_b` be the number of holes among its `w_b` proper
suffixes.

Every short interval ending at `b` which is not a proper suffix either is
the selected central interval itself or contains it.  Its OR has rank at
least `r`, so it cannot be a chosen lower witness.  Therefore at least

\[
 \delta_b=c_b-w_b+h_b
\tag{3.2}
\]

holes end at `b`.  The selected endpoints are distinct, so

\[
 \sum_{b\in E}\delta_b\le\sigma.
\tag{3.3}
\]

Put

\[
 f_u(z)=\max(z-u+1,0).
\]

The chain argument gives `f_u(w_b-h_b)` low-depth labels at endpoint `b`,
and the one-Lipschitz property of `f_u` gives

\[
 f_u(w_b-h_b)=f_u(c_b-\delta_b)
 \ge f_u(c_b)-\delta_b.
\tag{3.4}
\]

For `b<d`, physical width satisfies `w_b<=b-1`, so `delta_b>=1`.  Thus at
most `sigma` selected endpoints can lie among the useful early positions
`1,...,d-1`.

Define

\[
 t=\min(\sigma,d-1,M),\qquad
 v=\max(0,t-d+q).
\tag{3.5}
\]

To minimize the sum of `f_u(c_b)` over `M` selected endpoints, use the `t`
smallest early endpoints `1,...,t`, and take the other `M-t` endpoints where
`c_b=d`.  With

\[
 u=d-q+1,
\]

the positive early contributions are `1+...+v`.  Equations (3.3)--(3.4)
therefore prove

\[
 \boxed{
 \Lambda_{r-d+q-1}
 \ge q(M-t)+\binom{v+1}{2}-\sigma
 }
\tag{3.6}

for `1<=q<=d`.

So the proposed endpoint inequality is valid.

### It is not the strongest endpoint consequence

Apply the same chain argument to **all** right endpoints, without mentioning
the selected rank-`r` intervals.  If `z_b` is the number of holes among the
`c_b` short cells ending at `b`, then the occupied cells form a strict chain
of length `c_b-z_b`.  Hence they contain at least

\[
 f_{d-q+1}(c_b-z_b)
 \ge f_{d-q+1}(c_b)-z_b
\]

targets of rank at most `r-d+q-1`.  Summing `z_b=sigma` and evaluating the
complete endpoint profile gives the stronger bound

\[
 \boxed{
 \Lambda_{r-d+q-1}
 \ge qM+\binom{q+1}{2}-\sigma.
 }
\tag{3.7}

Indeed, the positions `b=d,...,M+d` contribute `q(M+1)`, while the early
positions contribute `1+...+(q-1)`.

Bound (3.7) dominates (3.6), since

\[
 \bigl[qM+\binom{q+1}{2}-\sigma\bigr]
 -\bigl[q(M-t)+\binom{v+1}{2}-\sigma\bigr]
 =qt+\binom{q+1}{2}-\binom{v+1}{2}>0.
\tag{3.8}

Here `v<=q-1`.  Thus (3.6) is correct but redundant as a scalar necessary
condition.  The genuinely new information remains the width-dependent
Theorem 2.1.

At `q=d`, (3.7) is exactly the defining identity

\[
 \Lambda_{r-1}=dM+\binom{d+1}{2}-\sigma,
\]

so no contradiction can occur there.

## 4. Audit of the full-core bound

Every selected central interval which is not a full width-`d` window forces
at least one hole at its selected right endpoint.  The standard monotone
endpoint normal form also shows that all full-width windows form one
contiguous core.  Hence, when

\[
 C=M-\sigma\ge d,
\tag{4.1}
\]

we may select `C` consecutive full central windows

\[
 I_i=[i,i+d]
\]

after translating the index interval.

Fix `1<=q<=d` and put

\[
 s_0=r-d+q-1.
\]

For each core window consider its `q` shortest proper prefixes and its `q`
shortest proper suffixes.

### Localization lemma

Suppose one proper-suffix chain has `h` holes among all of its `d` cells.
It has `d-h` occupied cells.  When `q-h>0`, in increasing-length order its
first `q-h` occupied cells have rank at most `s_0`: the `j`th member of a
strict chain of `d-h` ranks below `r` has rank at most

\[
 r-(d-h)+j-1,
\]

and setting `j=q-h` gives `s_0`.  Moreover, these first `q-h` occupied cells
lie among the `q` shortest physical suffixes, because at most `h` positions
can be missing before them.

Thus the fixed geometric strip of `q` shortest suffixes contains at least
`max(q-h,0)`, and hence at least `q-h`, certified labels of rank at most
`s_0`.  The same statement holds for prefixes.

Distinct core windows have distinct right endpoints and distinct left
endpoints.  Therefore the suffix-hole charges total at most `sigma`, and the
prefix-hole charges also total at most `sigma`.  The two geometric strips
contain label families of sizes at least

\[
 qC-\sigma
\tag{4.2}
\]

each.

### Exact geometric overlap

Let `F` be the interval of `C` core starts.  A length-`ell` prefix cell has
start in `F`.  A length-`ell` suffix cell has start in

\[
 F+(d-\ell+1).
\]

Because `C>=d`, their intersection has size

\[
 C-d+\ell-1.
\]

Summing over `1<=ell<=q`, the two full geometric strips overlap in exactly

\[
 \sum_{\ell=1}^{q}(C-d+\ell-1)
 =qC-qd+\binom q2
\tag{4.3}
\]

physical cells.

There is no larger hidden overlap at the label level.  A single
distinguished witness cell was fixed for every lower target.  Therefore the
same label can occur in the prefix and suffix selected families only when
its one physical witness cell lies in both geometric strips.

Inclusion--exclusion using (4.2)--(4.3) proves

\[
 \boxed{
 \Lambda_{r-d+q-1}
 \ge q(M-\sigma)+qd-\binom q2-2\sigma.
 }
\tag{4.4}

This verifies the proposed full-core bound.

The localization lemma is essential.  Merely saying that each chain
contains `q-h` low labels, without locating them in the `q` shortest cells,
would not justify the overlap number (4.3).

Compared with the all-endpoint bound (3.7), the gain of (4.4) is

\[
 q(d-q)-(q+1)\sigma.
\tag{4.5}

Hence (4.4) is strongest mainly in the zero- or very-small-defect regime.
It is nevertheless a valid new two-sided rank-depth refinement.

## 5. The zero-hole case

Suppose `sigma=0`.

Every short-band cell is then the selected witness of a different lower
target.  At a selected rank-`r` right endpoint `b`, equation (3.2) gives

\[
 c_b-w_b+h_b=0.
\]

No endpoint `b<=d` can be selected: physical width is at most `b-1<c_b`.
The only `M` possible selected endpoints are consequently

\[
 d+1,d+2,\ldots,M+d,
\]

and every selected width equals `d`.  Thus the rank-`r` witnesses are exactly

\[
 [1,d+1],[2,d+2],\ldots,[M,M+d].
\tag{5.1}
\]

This proves genuine fixed-delay rigidity:

* the entire short band is bijectively labelled by the lower ideal;
* every central witness has maximum width;
* the central witnesses form one complete contiguous row.

At `sigma=0`, (4.4) becomes

\[
 \Lambda_{r-d+q-1}
 \ge qM+qd-\binom q2.
\tag{5.2}

These conclusions do not force all cells of one physical length to have one
common rank, nor do they supply longer upper shadows.  Any stronger
“one-rank-per-row” or universal-braid statement remains an additional
construction theorem.

The zero-hole fixed-row conclusion was already implicit in the endpoint
saturation theorem; the new content here is the explicit rank-depth family
(5.2).

## 6. Odd-dimensional substitution

Let

\[
 k=2m+1,\qquad r=m+1,
\]

and

\[
 M=\binom{2m+1}{m+1}=\binom{2m+1}{m}.
\]

By symmetry,

\[
 \Lambda_{r-1}=\Lambda_m=2^{2m}-1,
\qquad
 \Lambda_{r-2}=\Lambda_{m-1}=\Lambda_m-M.
\tag{6.1}
\]

Also, by definition of `sigma`,

\[
 \Lambda_{r-1}=dM+\binom{d+1}{2}-\sigma.
\tag{6.2}
\]

Assume

\[
 \sigma\ge d-1
\tag{6.3}
\]

and `M>=d-1`.  Then the selected-endpoint parameters in (3.5) satisfy

\[
 t=d-1.
\]

At `q=d`, one has `v=d-1`, and the right side of (3.6) is

\[
 d(M-d+1)+\binom d2-\sigma.
\]

Subtracting it from (6.2) gives exactly

\[
 d^2.
\tag{6.4}
\]

For `d>=2`, at `q=d-1` one has `v=d-2`.  Using
`Lambda_{r-2}=Lambda_{r-1}-M`, the margin over (3.6) is again

\[
 d^2.
\tag{6.5}
\]

Thus the stated `d^2` margins are correct.  They show that the weaker
selected-endpoint inequality cannot decide the odd equality case at either
of its two deepest ranks.

They do **not** establish that one-sided counting has reached an absolute
“arithmetic limit.”  The calculation treats only this particular endpoint
functional, and only `q=d,d-1`, under (6.3).  A different endpoint weight,
the profile-sensitive inequalities (2.1), another value of `q`, or a
cross-rank coupling could still be stronger.  Moreover, Theorem 4.4 is
already genuinely two-sided inside the full core.  The defensible conclusion
is only that the displayed selected-endpoint corollary has an exact `d^2`
slack at those two tests.

Condition (6.3) must not be silently universalized.  The exact case

\[
 k=9,\quad r=5,\quad d=2,
\]

has `sigma=0<d-1`.  It belongs to the rigid regime of Section 5 instead.

## 7. Correct ledger

### Valid and genuinely informative

* The width-profile inequality (2.1).
* The localized two-sided full-core inequality (4.4), especially at very
  small `sigma`.
* The exact zero-hole fixed-delay rigidity.

### Valid but already dominated

* The selected-endpoint scalar inequality (3.6), which is strictly weaker
  than the all-endpoint band inequality (3.7).
* The `d^2` odd-dimensional margins; these are correct arithmetic checks,
  not new obstructions.

### Invalid if asserted without an extra hypothesis

* Applying the full-core formula when `M-sigma<d` without replacing the
  overlap calculation by positive parts.
* Treating the full-cycle component count as an ordinary path-run count.
* Claiming `sigma>=d-1` for every odd equality parameter; `k=9` is a direct
  exception.
* Claiming that `sigma=0` forces a one-rank-per-length grading or complete
  upper shadows.
* Claiming from the two `d^2` calculations that every possible one-sided or
  cross-rank counting refinement has been exhausted.

The majorization program is sound.  Its sharp part is the profile-sensitive
and two-sided geometry, not the weaker selected-endpoint scalar corollary.
