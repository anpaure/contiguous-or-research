# Good cuts, cyclic Hall barriers, and the scope of the bulk compiler

Date: 2026-07-27

## 1. Executive conclusion

For the fixed bulk sandwich graph, the good-cut question has an exact answer:
a cut adds `d` duplicate right resources, and it repairs Hall precisely when
each cyclic Hall barrier sees enough of those `d` positions.  In a free
`Z_p`-equivariant graph every invariant deficiency is a multiple of `p`.
Consequently, when `p>d`, **no cut can repair a cyclic Hall failure** in the
duplicate-only bulk architecture.

Thus the successful `k=11` quotient Hall audit is not merely one convenient
choice of cut.  In that architecture it is the gate itself.  Rotation
averaging cannot substitute for it.

The exact `k=7` computation supplies the complementary warning: without the
free symmetry, cyclic Hall can fail and the boundary can repair it, but only
at some safe cuts.  Complete shadows, residence, cap 2, and exterior safety
do not make every cut good.

Finally, the literal bulk compiler is a special finite-regime tool.  It
cannot be the general exact construction because eventually there are more
low-rank targets than entries.  The minimal general replacement is a
multi-row pin-compatible compiler.

## 2. Exact rotation criterion

Let `G=(L,R;E)` be a bipartite graph with

\[
R=\mathbb Z_W.
\]

For a cut `t`, let

\[
B_t=\{t,t+1,\ldots,t+d-1\}\subseteq\mathbb Z_W
\]

and form `G_t` by adding one duplicate copy of every right vertex in `B_t`,
with the same neighbourhood as the original.  For `A subseteq L`, put

\[
\delta(A)=|A|-|N_G(A)|.
\]

### Theorem 1 (exact good-cut criterion)

The extended graph `G_t` has a matching saturating `L` if and only if

\[
\boxed{
\delta(A)\le |N_G(A)\cap B_t|
\quad\text{for every }A\subseteq L.
}
\tag{2.1}
\]

#### Proof

The new neighbourhood has exactly one additional vertex for every old
neighbour lying in `B_t`.  Hence

\[
|N_{G_t}(A)|=|N_G(A)|+|N_G(A)\cap B_t|.
\]

Hall's inequality in `G_t` is therefore exactly (2.1).  □

Only cyclically deficient sets need be considered.  If `mathcal S` is the
set of exterior-safe cuts and

\[
b(A)=\#\{t\in\mathcal S:
|N_G(A)\cap B_t|<\delta(A)\},
\]

then the following union-bound criterion is immediate.

### Corollary 2 (rotation covering criterion)

If

\[
\sum_{\substack{A\subseteq L\\\delta(A)>0}}b(A)<|\mathcal S|,
\tag{2.2}
\]

then some exterior-safe cut is Hall-good.

This is a genuine sufficient theorem, but it also shows what averaging must
control: not merely the sizes of barrier neighbourhoods, but their circular
gap distribution.  Complete shadow counts alone do not contain that
information.

## 3. Symmetry gives a rigidity theorem, not an averaging theorem

Assume a group `Gamma` of order `p` acts freely on both shores of `G`, and
that it acts by automorphisms.  If Hall fails, the invariant-witness theorem
in `MATH_SYMMETRIC_HALL_UNCROSSING_20260727.md` gives an invariant deficient
set `A`.  Both `A` and `N(A)` are unions of free orbits, so

\[
\delta(A)\in p\mathbb Z_{>0},
\qquad\delta(A)\ge p.
\tag{3.1}
\]

### Theorem 3 (boundary-rigidity threshold)

In the duplicate-window model, if `p>d`, then the following are equivalent:

1. the cyclic graph `G` satisfies Hall;
2. `G_t` satisfies Hall for one cut `t`;
3. `G_t` satisfies Hall for every cut `t`.

#### Proof

The implications (1) to (3) to (2) are immediate.  If cyclic Hall fails,
choose the invariant witness from (3.1).  A length-`d` duplicate window adds
at most `d` neighbours, while its deficiency is at least `p>d`.  Equation
(2.1) fails for every cut.  □

If, while keeping the cyclic core and all nonboundary sandwiches fixed,
linearization is allowed both to add `d` positions and to enlarge the
allowed sets at the `d` old boundary positions, the neighbourhood of a fixed
target family can grow by at most `2d`.  The same proof gives threshold
`p>2d`.  This statement does not cover a global reoptimization of the core;
that is the multi-row PCSH problem of Section 6.

For the `k=11` translation-equivariant certificate, `p=11` and `d=3`, so
both thresholds hold.  This explains why the 63 quotient surplus-Hall
inequalities in `MATH_BULK_PCSH_COMPILER_20260727.md` are the correct
statewise gate: a failed invariant inequality could not have been repaired
by choosing another cut.

## 4. Exact `k=7` boundary counterexample

The certificate

```text
scratch/sigma_calibration_k7_full_nonsym43.certificate.json
```

has delay 2, complete two-sided shadows through depth 2, residence at least
3, q1 upper load at most 2, and 28 exterior-safe cuts.

The exact compiler SAT audit gives:

* cyclic PCSH: UNSAT;
* linear PCSH: SAT on 24 safe cuts and UNSAT on cuts `0,1,14,29`.

This is a statewise counterexample to both stronger claims

\[
\text{complete shadows + residence + cap 2}
\Longrightarrow\text{cyclic PCSH}
\]

and

\[
\text{exterior-safe cut}
\Longrightarrow\text{that cut is PCSH-good}.
\]

It is **not** a counterexample to existence of some good cut.  A bounded
portfolio of 121 independently generated cycles had successful-cut
histogram

\[
15^8\;24^{13}\;28^{100};
\]

no all-cut failure was found.

This is the smallest informative regime found: the analogous fully
constrained `k=5`, delay-2 middle-cycle instance is itself UNSAT.

## 5. Necessary scope correction for the literal bulk compiler

Put

\[
s=r-d.
\]

The bulk compiler in `MATH_BULK_PCSH_COMPILER_20260727.md` asks every target
of rank at most `s` to occur literally in row `D^0`.  A necessary capacity
condition is therefore

\[
\boxed{
\sum_{j=1}^{s}\binom{k}{j}\le W+d.
}
\tag{5.1}
\]

It already fails at `k=9`:

\[
\sum_{j=1}^{3}\binom9j=9+36+84=129>128=W+d.
\]

Indeed the known exact `k=9` word places one rank-3 target in `D^1` rather
than literally.  Numerically the low-target/entry ratio is about 1.25 at
`k=30` and 1.70 at `k=100`; asymptotically it is `Theta(sqrt(k))` in the
deadline regime.  Hence the first-derivative bulk theorem is a powerful
finite/special-regime compiler, not a uniform proof of the exact formula.

## 6. Minimal multi-row generalization

Let the lower targets be partitioned into row families

\[
\mathcal L_0\sqcup\mathcal L_1\sqcup\cdots
\sqcup\mathcal L_{d-1}.
\]

For every `S in mathcal L_t`, choose a start `i=phi_t(S)` and impose the pin

\[
(D^tA)_i=S.
\tag{6.1}
\]

For fixed `t`, the starts must be injective because one derivative cell has
one value.  Starts at different depths may overlap.

Intersect the top envelopes with every pin containing each entry position,
obtaining allowed sets `P_j`.  For every coordinate, demand a witness in
each top or pinned interval in which that coordinate is required.  A core
`C_j subseteq P_j` hitting all these coordinate intervals has the property

\[
C\subseteq A\subseteq P
\Longrightarrow
D^dA=T\text{ and every pin (6.1) holds}.
\tag{6.2}
\]

This is the minimal row-graded PCSH condition.  It reduces to the literal
bulk compiler when `mathcal L_0` contains all ranks at most `s`, and to the
selected-pin theorem in `scratch/sigma_calibration_compiler_theorem.md` for
the `k=11` rank split.

For a fixed cyclic row assignment, cutting and appending `d` entries creates

\[
\sum_{t=0}^{d-1}(d-t)=\frac{d(d+1)}2
\tag{6.3}
\]

additional derivative cells across rows `0,...,d-1`.  Thus a free
`Z_p`-invariant layered Hall deficit larger than this cannot be repaired by
duplicate boundary cells.  The general deadline has `p` and `d^2` of the
same order, so unlike the special `k=11` bulk case this does not by itself
settle the asymptotic gate.

## 7. Reproducible audits

Bulk quotient Hall and exact `k=11` compilation:

```sh
python3 scratch/sigma_calibration_bulk_surplus_hall.py \
  scratch/sigma_sat_k11_allcentral_cap2.certificate.json \
  --k 11 --delay 3 \
  --output-word scratch/sigma_calibration_bulk_k11_465.word
```

Exact cyclic and cut-by-cut `k=7` PCSH:

```sh
python3 scratch/sigma_calibration_exact_pcsh.py \
  scratch/sigma_calibration_k7_full_nonsym43.certificate.json \
  --k 7 --delay 2 --cyclic

python3 scratch/sigma_calibration_exact_pcsh.py \
  scratch/sigma_calibration_k7_full_nonsym43.certificate.json \
  --k 7 --delay 2
```

## 8. Remaining theorem

The strongest honest good-cut target is now:

> In the multi-row compiler, prove that complete shadows and residence force
> either cyclic row-graded Hall, or a family of cyclic barriers whose
> circular gap profiles satisfy the rotation covering inequality (2.2) on
> the exterior-safe cuts.

Counts, loads, and uncrossing identify the barriers but do not control their
position around the cycle.  That positional statement is the irreducible
content still missing from a general good-cut theorem.
