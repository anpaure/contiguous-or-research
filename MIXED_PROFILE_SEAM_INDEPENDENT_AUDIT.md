# Independent audit of `MIXED_PROFILE_SEAM_NEXT.md`

## 1. Verdict

**PASS WITH LOCAL REPAIRS AND A STRICT SCOPE QUALIFICATION.**

The main mathematical advances in the source are sound, conditional on the
inherited three-box setup and, where invoked, the selected-middle-order
hypothesis `D=o(a^2)`:

1. the aggregate absorption resource is `3 dt`;
2. a nonabsorbing seam has the guaranteed saving density
   \[
   \phi(p,s,z)=\min\{p,(4-s-z)_+\}(s-z)_+;
   \]
3. optimizing the coarse atomic ledger gives `4/9` at `x=4/3`;
4. one uniform neighbourhood of the atomic segment
   `2 delta_x`, `4/3<=x<=3/2`, is excluded, even when the mass inside the
   neighbourhood is non-atomic; and
5. the adversarial fixed-threshold value is concave in the retained plateau
   measure.

The broad density `2 1_[1,2](x) dx` also really does pass the reduced
fixed-threshold seam ledger.  The source explicitly proves this only for
`1<c<=4/3`; Section 9 below gives the short continuation through every
`1<c<2`.

None of this proves that the broad ledger, or any one of its threshold
couplings, comes from a permutation of the three-box points.  The functional
is an exact accounting of what the repaired seam move can guarantee after
projecting to lengths, gaps, and aggregate line capacity; it is only a
**necessary relaxation of realizable word geometry**.  It omits precisely the
direction labels, cross-line placement, and compatibility between different
threshold deletions emphasized in `MATHEMATICAL_HANDOFF.md`, Sections 148,
152, 160, and 162.

Two literal statements need repair:

* The first gap is at source equations (2.2) and (2.7).  A weak limit of
  plateaux satisfying `lambda/a>c` may have an atom at `c`.  Hence the demand
  mass in (2.7) is `||mu||=rho_ps(total)`, not `mu((c,2])`, unless `c` is a
  continuity point.  All later applications in the note either have no atom
  at `c` or are finite, so this does not invalidate them.
* Source equation (2.6) is the valid aggregate inequality
  `kappa(t in B)<=3|B|`.  It is **not equivalent** to one unit in each named
  direction.  The direction-labelled necessary inequalities are
  `kappa(d=d0,t in B)<=|B|` for each `d0`.  The aggregate version is the
  intended relaxation and is sufficient for every exclusion and static
  obstruction claimed in the note.

The audit therefore does not support an unqualified phrase such as “exact
fixed-threshold characterization of words.”  It does support “exact
fixed-threshold seam-repair functional under an aggregate necessary
relaxation.”

## 2. Authoritative inputs and normalization

The source audited here has SHA-256

```text
01d863d66cf2a0a2e0fdc13f8b4e1b52d109de96c1c798819dc3e8a4cf4abd60
```

The principal inherited sources used in this audit are:

```text
75483123b4425561847bd00f607a545545af0a0ae2661ce9f3fb41e322bfbde6  FABLE_QUANTITATIVE_SEAM_TRACE_AUDIT.md
1b612fceabb25089060a59282a613ff01ae581e2fccab11e95cae843ce17113a  FABLE_QUANTITATIVE_SEAM_REPAIR_INDEPENDENT_AUDIT.md
492ccbddaf05fa2671d9dec5cfae7225ca3cf8d1e0cbe780bf609d9b455ce3a1  FIRST_DANGEROUS_GLOBAL_SERVICE.md
e23b123cacad01f4d1b4bbf3d095bf0fb9dec4aa077eaabf04de3c736ceec772  FIRST_DANGEROUS_GLOBAL_SERVICE_AUDIT.md
ae96c591b036233dd8a9250917e70b1b7c0425b38a20f3a1d97383cfa8493a31  POSITIVE_SEAM_CROSSLINE_COUPLING.md
3b16ee5b2e5d851090895c4c18d2d20da7daaabedb9943de65d19e81409875e3  POSITIVE_SEAM_CROSSLINE_COUPLING_AUDIT.md
3259f21ae5bcd5887fca19875f2f28301f7fec6f24f8bcdb0c2351e850df422e  FABLE_RUN_SPECTRUM_AUDIT.md
```

For one fixed threshold `1<c<2`, every dangerous plateau has more than `a`
edges.  The total number of dangerous plateaux is therefore `O(a)`.  Deleting
the first predecessor and final successor changes either empirical marginal
by `O(1/a)`.  Thus the predecessor-successor measure has equal limiting
`p`- and `s`-marginals.

Dangerous plateau edge intervals are disjoint, while the discrepancy between
edge mass and the vertex-union convention is only `O(a)`.  Consequently

\[
  \int x\,d\mu(x)\le 3,
  \qquad
  \int z\,d\rho(p,s,z)\le 3-\int x\,d\mu(x).
\]

The first moment bound makes the `z`-measures tight.  Both the seam integrand
and the saving integrand are bounded after clipping, so truncation followed by
monotone removal of the truncation handles a vanishing family of macroscopic
gaps.

### Threshold-boundary repair

Although every finite dangerous length satisfies `s_j>c`, weak convergence
does not imply `mu({c})=0`; for example `s_j=c+1/a` can carry positive limiting
mass at `c`.  Therefore equations involving the total seam count must use

\[
                 f=\|\mu\|=\rho_{ps}([c,2]^2),
\]

or one must explicitly assume `mu({c})=0` before replacing this by open-tail
mass.  The source already invokes continuity thresholds when it
turns the functional into an exclusion certificate.  The atoms used in
Section 3 have `x>c`, the broad density is absolutely continuous, and Theorem
4.1 is a direct finite argument.  Hence the repair is local.

## 3. Absorption interval and the `3 dt` resource

Let the predecessor and successor edge lengths be `pa+o(a)` and `sa+o(a)`.
The predecessor's rising cross-coordinate finishes at normalized level at
least `p-1`.  If the successor absorbs that cross-coordinate as its fixed
coordinate at level `t`, then the line has at most `(2-t)a+O(1)` edges, so

\[
                         p-1\le t\le 2-s.
\]

In particular `p+s>3` forbids absorption.  Since `p,s>c>1`, two dangerous
successors cannot occupy one geometric coordinate line: their disjoint
vertex sets would contain more than the at-most `2a+1` vertices of that line.
For each of the three coordinate directions and each integer positive level,
there is therefore capacity for at most one absorbed successor.  On scaling
levels by `a`, every actual weak limit satisfies

\[
 \kappa\{d=d_0,\ t\in B\}\le |B|,
 \qquad d_0=1,2,3.
\]

Summing gives the aggregate relaxation

\[
                         \kappa\{t\in B\}\le3|B|.
\]

Thus `3 dt` is correct as the unlabelled fractional resource.  For prescribed
length coupling, the fractional Hall deficiency formula

\[
 A_{\max}=f-\sup_{\mathcal U}
       \big(\rho_{ps}(\mathcal U)-3|N(\mathcal U)|\big)_+
\]

is correct after replacing `f` by the total demand mass as above.  It is the
maximum in the aggregate fractional relaxation.  If predecessor rising
directions are retained, the three separate `dt` resources, not merely their
sum, must be used.

This distinction is consistent with Handoff Section 148: line capacity alone
does not place the clipped predecessor gaps in the cross-line desert, and it
does not determine which direction a particular seam demands.

## 4. Saving integrand

For a nonabsorbing seam, the audited local-maximum lemma gives an internal
threshold run inside the predecessor gap of cost at most `za+O(1)`.  The
exact safe-start interval has cardinality

\[
 \min\{pa+o(a),\ (4-s-z)a+O(1)\}_+.
\]

It lies in the word-edge interior of the predecessor plateau.  Distinct seams
therefore have disjoint safe-start intervals.  Every reassigned start
previously paid `sa+o(a)` and now pays at most `za+O(1)`.  Selecting only the
guaranteed number of starts gives the lower saving

\[
 \min\{p,(4-s-z)_+\}(s-z)_+a^2-o(a^2)
\]

at that seam.  Summing `O(a)` seams and accounting once for the global word
boundary gives only `o(a^3)` loss.  Hence

\[
 \phi(p,s,z)=\min\{p,(4-s-z)_+\}(s-z)_+
\]

is correct as the exact asymptotic **guaranteed** saving integrand.  It is not
an assertion that no larger saving is available.

The first-dangerous seam charge is likewise

\[
 H_c(\rho)=\int(s-c)\min\{z,4-s\}\,d\rho,
\]

and the inherited cyclic-secant charge is `2e_c`.  An actual word therefore
produces a feasible ledger with

\[
 {Q_{\rm mod}\over a^3}
 \le 3c+2e_c+H_c-\int\phi\,d(\rho-\alpha)+o(1).
\]

Taking the supremum over the relaxed feasible ledgers is safe for an
exclusion: if even this supremum is below four, every realizable ledger is
below four and contradicts the capped-run lower bound.

## 5. Optimized atomic constant

For `mu=2 delta_x`, `4/3<=x<=3/2`, the aggregate absorption capacity and gap
mass are

\[
 A\le3(3-2x),\qquad G=3-2x.
\]

After declaring gaps larger than `r` expensive, the cheap nonabsorbed mass is
at least

\[
 \left[6x-7-{3-2x\over r}\right]_+.
\]

On the optimizing interval the safe-start factor is `x`, and the per-start
saving is `x-r`.  Differentiation gives

\[
 r_*(x)=\sqrt{{x(3-2x)\over6x-7}},
\]

and substitution gives

\[
 S_*(x)=x\left(\sqrt{x(6x-7)}-\sqrt{3-2x}\right)^2.
\]

At `x=4/3`, `r_*=2/3` and

\[
                         S_*(4/3)=4/9.
\]

The support inequalities `0<r_*<x` and
`r_*<=4-2x` hold for `4/3<=x<3/2`.  At `x=3/2`, the displayed optimizer is
the boundary limit `r_*=0`, rather than an interior maximizer.  This is only a
wording repair.  The old choice `r=1` gave `8/27`, so `4/9` is the correctly
optimized benchmark.

## 6. Uniform mixed-band stability

Theorem 4.1 is valid.  Here is the complete count audit.

If `R` regular and `E` exceptional dangerous plateaux occur in one linear
list, the regular vertices form at most `E+1` blocks.  Hence the number of
regular-to-regular seams is at least

\[
                         R-E-1\ge(2-2\epsilon-o(1))a.
\]

Absorption of such a seam requires a line level in

\[
 [x-1-\epsilon,\ 2-x+\epsilon],
\]

so the three-direction line capacity removes at most
`3(3-2x+2epsilon)a+O(1)` seams.  The regular plateaux consume at least

\[
                  (2-\epsilon)(x-\epsilon)a^2
\]

word edges.  Therefore the number of predecessor gaps longer than `a` is at
most

\[
 \big(3-(2-\epsilon)(x-\epsilon)+o(1)\big)a.
\]

Subtracting these two exceptional classes leaves normalized cheap-seam count

\[
 C_\epsilon(x)
 =8x-10-(10+x)\epsilon+\epsilon^2-o(1),
\]

exactly as in the source.  Every such seam supplies at least
`(x-epsilon)a-O(1)` disjoint starts and saves at least
`(x-1-epsilon)a-O(1)` at each.

With `c=x-2epsilon`, every regular excess is at most `3epsilon a`; the at
most `epsilon a` exceptional dangerous plateaux each have excess at most
`(2-c)a`.  Since `c>1` after choosing a small uniform `epsilon`,

\[
 e_c\le 3\epsilon(2+\epsilon)+\epsilon(2-c)
      \le7\epsilon+3\epsilon^2.
\]

The inherited bound `H_c<=(4-c+o(1))e_c` then yields

\[
 {Q_{\rm fd}\over a^3}
 \le3x+29\epsilon+15\epsilon^2+o(1).
\]

At `epsilon=0`, the saving margin over the amount needed below four is

\[
 (8x-10)x(x-1)-(3x-4)\ge8/27
\]

uniformly on the compact interval.  Every displayed function is continuous
there, and the cheap-seam coefficient is uniformly positive at
`epsilon=0`.  One numerical `epsilon_0>0` therefore works simultaneously for
all `x` in the interval.  This proves a genuine non-atomic neighbourhood
exclusion under `D=o(a^2)`.

The theorem does **not** reduce an arbitrary mixed survivor to this
neighbourhood.  It strengthens Handoff Section 162 but does not close the
mixed-profile case.

## 7. Concavity

For fixed `c`, take feasible relaxed ledgers for `mu_1` and `mu_2`.  Their
convex mixture has the required mixed marginals; its gap moment is at most

\[
 \theta(3-\ell_1)+(1-\theta)(3-\ell_2)
 =3-\big(\theta\ell_1+(1-\theta)\ell_2\big);
\]

its aggregate line demand remains at most `3 dt`; and its objective is the
same convex mixture of the two objective values.  Taking suprema proves

\[
 \mathcal U_c(\theta\mu_1+(1-\theta)\mu_2)
 \ge \theta\mathcal U_c(\mu_1)
 +(1-\theta)\mathcal U_c(\mu_2).
\]

Thus the value function is concave.  The same proof works if the three
direction capacities are retained separately.

Concavity shows only that an extreme-point/Dirac reduction is unavailable;
it does **not** prove that no atom can be an optimizer.  The source's section
title “why atoms are not extremizers” is stronger than its proof and should be
read as “why atoms need not be extremizers.”

## 8. The broad thresholdwise ledger on `1<c<=4/3`

For the full measure

\[
                       \mu(dx)=2\mathbf1_{[1,2]}(x)\,dx,
\]

the dangerous tail has

\[
 e_c=(2-c)^2,\qquad \ell_c=4-c^2,\qquad G_c=c^2-1.
\]

On `[c,3-c]`, reflection `p=3-s` preserves the density.  Absorption occurs
at the unique allowed level `t=2-s=p-1`; its pushforward has density two on
`[c-1,2-c]`, below aggregate capacity three.  On `[3-c,2]`, the identity
coupling preserves the remaining density.  With

\[
 r_c=\sqrt{2(c^2-3c+4)},
\]

setting `z=s` on `[3-c,r_c]` and `z=0` on `[r_c,2]` uses exactly

\[
 2\int_{3-c}^{r_c}s\,ds=c^2-1
\]

gap mass.  Every marginal, support, absorption, and gap constraint is
satisfied.

The resulting value is

\[
 \Psi(c)=\frac43[2(c^2-3c+4)]^{3/2}
          -\frac13c^3-4c^2+14c-\frac{46}{3}.
\]

Direct differentiation verifies that it decreases on `[1,4/3]`, and

\[
 \Psi(4/3)={512\sqrt2-370\over81}=4.371325\ldots>4.
\]

This part of the source is correct.

## 9. “All fixed thresholds”: what is proved and how it extends

Literally, the source proves the broad ledger only for `1<c<=4/3`.  Thus the
phrase “survives all fixed thresholds” would exceed the written proof.  The
claim is nevertheless repairable within the same static relaxation.

### 9.1 `1<c<=3/2`

The source construction remains feasible unchanged until `c=3/2`, because
the reflected low block `[c,3-c]` remains nonempty.  The same `Psi(c)` is
decreasing on `[1,3/2]`.  At the endpoint

\[
 \Psi(3/2)={14\over3}\sqrt{7\over2}-{107\over24}
           =4.272200\ldots>4.
\]

Hence every threshold in this range survives.

### 9.2 `3/2<=c<=sqrt(5/2)`

Use the identity coupling on the entire tail `[c,2]`, with no absorption.
Put

\[
 r=\sqrt{2c^2-1},\qquad
 z=s\ \text{on }[c,r],\qquad z=0\ \text{on }[r,2].
\]

Then `2 integral_c^r s ds=c^2-1`, exactly the gap budget.  The ledger value is

\[
 F_2(c)={4\over3}(2c^2-1)^{3/2}
        -{5\over3}c^3+2c^2-4c+{8\over3}.
\]

Since `r>=c`,

\[
 F_2'(c)=8cr-5c^2+4c-4
        \ge3c^2+4c-4>0.
\]

Thus `F_2(c)>=F_2(3/2)=Psi(3/2)>4`.

### 9.3 `sqrt(5/2)<=c<2`

Again use the identity coupling, but set `z=s` on the entire tail.  This is
feasible because

\[
 \int_c^2 2s\,ds=4-c^2\le c^2-1.
\]

There is no saving and the seam charge is nonnegative.  The exact value is

\[
 F_3(c)={40\over3}-9c+2c^2+{c^3\over3}.
\]

Its minimum on this interval occurs at `c=-2+sqrt(13)` and equals

\[
 {110-26\sqrt{13}\over3}=5.418\ldots>4.
\]

Therefore the broad measure passes the reduced static seam ledger at every
fixed threshold `1<c<2`.

This extension still chooses a different coupling and gap allocation for
different `c`.  It supplies no nested family of threshold deletions from one
ordering.

## 10. Static feasibility versus one realizable ordering

The broad calculation proves only this statement:

> For each threshold `c` separately, there exists a stationary
> predecessor-successor length coupling, gap allocation, and aggregate
> fractional line allocation satisfying the reduced ledger and having value
> at least four.

It does **not** prove any of the following:

1. that one linear or cyclic order induces all of those couplings after its
   shorter plateaux are deleted;
2. that an absorbed seam's predecessor rising direction equals the direction
   used by the aggregate fractional line allocation;
3. that the prescribed gap mass can be placed outside, or inside the unused
   part of, the selected coordinate-line union as required by Handoff Section
   148;
4. that line intersections and additive triples admit the proposed plateau
   family; or
5. that any permutation of `H_a` realizes the full measure.

This is not a technical afterthought.  The positive-seam theorem in Handoff
Section 148 shows that actual threshold ledgers inherit cross-line placement
constraints, and the failed argument audited in Section 152 shows why static
tail averages cannot be exactified into a word ordering.  Section 160 makes
the correction audits authoritative, while Section 162 certifies only the
atomic exclusion and explicitly leaves mixed profiles open.

The broad family is therefore a valid no-go example for a proof using only
independent fixed-threshold length/gap/aggregate-line ledgers.  It is not a
counterexample to the three-box conjecture and supplies no construction for
the original OR-array problem.

## 11. Final ledger

### Certified, under the inherited framework

* aggregate absorption capacity `3 dt`;
* the fractional Hall formulation after the threshold-boundary repair;
* the guaranteed saving integrand `phi`;
* the optimized atomic coefficient `4/9`;
* uniform non-atomic band stability near every excluded atom;
* concavity of the relaxed adversarial value;
* the broad fixed-threshold static ledger on the source's stated range; and
* by the explicit continuation in Section 9, broad static feasibility for
  every `1<c<2` in the reduced relaxation.

### Not certified

* direction-labelled feasibility from lengths alone;
* simultaneous compatibility of the ledgers across thresholds;
* cross-line-desert placement of the allocated gaps;
* realizability by one three-box ordering;
* exclusion of arbitrary mixed profiles;
* the three-box impossibility theorem; or
* the all-`k` OR-array conjecture.
