# Independent audit: one-depth shift and the freed-singleton absorber

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ONE_DEPTH_SHIFT_FREED_SINGLETON_ABSORBER_20260805.md`  
**Audited self-audit:**
`MATH_AUDIT_ONE_DEPTH_SHIFT_FREED_SINGLETON_ABSORBER_20260805.md`  
**Method:** independent pure-mathematical reconstruction; no computation,
search, or solver  
**Verdict:** **INDEPENDENT GO** for the complete anonymous even-dimensional
two-SCD system and the explicitly coherent boundary variant.  The source
was tightened by stating `D>=1,t>=2`, which is automatic asymptotically and
excludes the punctured bottom-zero counting degeneracy.  Duplicate equation
numbers in the asymptotic corollary were also corrected.  No substantive
claim changed.

## 1. Exact adjacent-depth identities

At depth `D`, the collar threshold is

\[
                         t=r-D.
\]

For a residual SCD chain with bottom `b<t`, the unpunctured portion has
ranks `b,...,t-1` and hence length `t-b`.  At depth `D+1`, the threshold is
`t-1`, so a surviving bottom `b<t-1` has ranks `b,...,t-2` and length

\[
                         t-1-b=L_D(b)-1.
\]

The bottom-`t-1` chains have old length one and disappear.  When `t>=2`
their multiplicity is exactly

\[
                         H_{t-1}=C_{t-1}-C_{t-2};
\]

none is the punctured bottom-zero chain.  The unique bottom-zero job loses
the rank-`t-1` terminal cell at the same time as every other surviving job;
deleting the empty set therefore commutes with the shift.

For a collar-SCD chain with bottom `t+u`, its old short-collar length is

\[
                         r-(t+u)=D-u,
\]

so its residual socket capacity is `D-(D-u)=u`.  At new depth `D+1`, the
same occurrence has capacity

\[
                         (D+1)-(D-u)=u+1.
\]

Chains beginning at `t` had no old socket and become the new capacity-one
collar sockets.  The proof does not use them.  These calculations verify
(0.4)--(0.5) occurrence by occurrence on the same collar SCD.

## 2. Terminal deletion of configurations

Take an old consecutive fragmentation of a job of length `L>=2`.  Removing
the rightmost job cell affects only its rightmost piece.  A piece of length
at least two shortens by one; a singleton piece disappears together with
its socket assignment.  Every retained piece stays positive, remains
consecutive, and does not increase in length.  On a genuine collar
occurrence its capacity rises by one, so the same labelled assignment is
valid after the shift.

Applying this deterministic operation to every integer configuration in a
fractional mixture is affine.  The main proof, however, needs it only after
the integral configurations have been selected and injected.

## 3. Extreme-point and endpoint isolation

The correct old configuration LP mixes integer whole-job fragmentations.
Its basic-support theorem yields a feasible extreme point in which at most
`D` jobs have more than one positive configuration; call them `F`.  Every
other job has a unique coefficient-one integer configuration.  The
aggregate tail use of those configurations is bounded by the old socket
tails, so the Ferrers injection theorem assigns all their pieces to
distinct labelled old socket occurrences.

The old endpoint triangle has exactly `D` occurrences, one of each
capacity `1,...,D`.  Let `G` contain every integrally selected job touching
at least one endpoint occurrence.  Since the selected packing is injective,
choosing one touched endpoint for each member of `G` gives an injection
`G` into the endpoint bank.  Therefore

\[
                         |F|\le D,
 \qquad
                         |G|\le D,
 \qquad
                         |F\cup G|\le2D.
\]

After discarding `F union G`, every retained assignment lies on a genuine
collar-SCD occurrence, where the `+1` capacity identity is literal.  This
step is essential: the endpoint occurrences are abstract boundary cells
and no occurrencewise lift for them is assumed.

## 4. The freed bank is physical and has capacity at least two

An integral job of total length one has exactly one positive piece of
length one and occupies exactly one socket.  Distinct singleton jobs in the
fixed injection occupy distinct occurrences.  Among the `H_(t-1)` old
singleton jobs, at most `D` can lie in `F` and at most `D` in `G`.  Thus at
least

\[
                         H_{t-1}-2D
\]

singleton jobs are integral, nonendpoint jobs.

When those jobs disappear, their labelled collar occurrences are free.
They are disjoint from every transported retained assignment because the
old injection was injective.  Each had old capacity at least one, since it
carried a positive singleton, and the same occurrence has new capacity one
larger.  Hence every member of this bank has actual capacity at least two;
this is not a scalar-capacity inference.

The proof does not count sockets freed by discarded jobs, does not use the
old or new endpoint triangles, and does not use the newly born
capacity-one collar sockets.  All of those omissions are conservative.

## 5. Absorbing the residual jobs

The only unpacked new jobs are the members of `F union G` whose old length
was at least two.  There are at most `2D`.  In the complete nonempty
histogram the largest old job has length `t-1`: the unpunctured bottom-one
jobs and the punctured bottom-zero job both have that length.  Therefore
every unpacked new job has length at most `t-2`.

Splitting a length `L'<=t-2` into twos and at most one final singleton uses

\[
                         \left\lceil{L'\over2}\right\rceil
 \le
                         \left\lceil{t-2\over2}\right\rceil
\]

distinct capacity-at-least-two occurrences.  Consequently the displayed
condition

\[
 H_{t-1}-2D
 \ge
 2D\left\lceil{t-2\over2}\right\rceil
\]

is sufficient.  Together with the transported integral jobs, this packs
the complete new job histogram.  Overlap between `F` and `G` only lowers
the true demand, so using `2D` is safe.

## 6. The `H_(t-1)` asymptotic

For `s=t-1=r-D-1`, the exact adjacent-binomial identity gives

\[
\begin{aligned}
 H_s
 &=C_s\left(1-{s\over2r-s+1}\right)\\
 &=C_s,{2D+3\over r+D+2}.
\end{aligned}
\tag{6.1}
\]

The coefficient-one depth has `D=Theta(sqrt(r))`.  Moreover

\[
 {C_{r-D-1}\over C_r}
 =\prod_{j=0}^{D}{r-j\over r+j+1}
 =\Theta(1),
\tag{6.2}
\]

because the logarithm of the product is `-Theta(D^2/r)=-Theta(1)`.
Equations (6.1)--(6.2) yield

\[
                         H_{t-1}=\Theta(W/\sqrt r).
\]

This is exponential in `r`, while

\[
 2D\left\lceil{t-2\over2}\right\rceil=O(r^{3/2}).
\]

Hence the finite absorber inequality holds for all sufficiently large
`r`.

## 7. Boundary, parity, and conclusion scope

The unconditional statement is for the complete nonempty histogram in
even dimension `2r`, using the same fixed residual and collar SCDs at the
two adjacent depths.  The source's boundary variant correctly requires:

1. every surviving new job to be the old job with its terminal cell
   deleted;
2. enough old singleton jobs to survive after the conservative `2D` loss;
3. the same labelled collar occurrences to realize the old fractional
   socket types and the new lifted capacities.

Independently chosen old and new triangular deletions need not meet these
conditions.  No odd-dimensional analogue is asserted.

The theorem proves only

\[
 \text{fractional anonymous depth-}D\text{ fragmentation}
 \Longrightarrow
 \text{integral anonymous depth-}(D+1)\text{ fragmentation}
\]

for sufficiently large even dimensions.  It does not prove the old
fractional configuration inequalities, named containment of a fragment in
its socket, one literal chronology, residence, upper shadows, a safe cut,
or an actual universal OR word of length `B+1`.  Subject to those explicit
boundaries, the theorem and self-audit are correct.  **INDEPENDENT GO.**
