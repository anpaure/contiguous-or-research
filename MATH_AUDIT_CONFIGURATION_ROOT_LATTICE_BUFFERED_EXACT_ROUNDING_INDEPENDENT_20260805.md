# Independent audit: configuration root-lattice buffered exact rounding

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Audited source:**
`MATH_THEOREM_CONFIGURATION_ROOT_LATTICE_BUFFERED_EXACT_ROUNDING_20260805.md`  
**Verdict:** **GO after two material scope corrections.**  The finite
root-lattice rounding theorem is correct as an anonymous aggregate-tail
statement.  The original named-collar corollary did not follow at zero
reserve, and the original dual-margin display used the wrong functional.
Both have been corrected in the audited source.

## 1. Tail-vector and exchange audit

For a fragmentation with part lengths `lambda_1,...,lambda_m<=D`, its
conjugate tail is

\[
 p_q=\#\{i:\lambda_i\ge q\}.
\]

It is nonnegative, nonincreasing, integral, and

\[
 \sum_{q=1}^Dp_q=\sum_i\lambda_i=L.
\]

The one-part length-`j` configuration has

\[
 u^{(j)}=(1^j,0^{D-j}),
\]

while `(j-1,1)` has

\[
 v^{(j)}=u^{(j-1)}+u^{(1)}.
\]

Therefore

\[
 v^{(j)}-u^{(j)}=e_1-e_j.
\]

The vectors `(e_1-e_j)_(2<=j<=D)` are a `Z`-basis of

\[
 A_{D-1}=\{z\in\mathbb Z^D:\sum_qz_q=0\},
\]

because

\[
 z=\sum_{j=2}^D(-z_j)(e_1-e_j).
\]

Thus the elementary exchange and complete zero-work lattice claim are
exact.

## 2. Exact-work hypothesis

The residual LP has tail inequalities `A_q<=K'_q`.  Every convex
configuration choice has total coordinate sum equal to the total residual
job work.  Hence, when

\[
 \sum_aL_a=\sum_qK'_q,
\]

the nonnegative gaps `K'_q-A_q` sum to zero and all tail rows are exact.
The corrected source now states this quantifier explicitly.  Without this
work identity, the later error vector need not lie in `A_(D-1)` and the
root-lattice correction would not apply.

## 3. Extreme-point split count

The bound of at most `D` split jobs is valid.  For every split job choose two
positive configurations and take their within-job difference direction.
Every such direction annihilates all job-equality rows.  If there are more
than `D` split jobs, a nonzero linear combination annihilates the at most
`D` independent active aggregate tail rows.  A sufficiently small positive
or negative perturbation preserves all positive support entries and every
inactive inequality, contradicting extremality.

More precisely, the number of split jobs is bounded by the rank of the
active non-job rows.  The theorem's bound `D` is safe, even though the work
identity can make one aggregate row redundant in particular formulations.

## 4. Error bound and switch supply

For a length-`L` job,

\[
 0\le p_j\le L/j,
\]

since its `p_j` counted pieces use at least `j p_j` work.  A chosen integral
configuration and the fractional mean both lie in this interval, so one
split job changes coordinate `j` by at most `L/j`.  With at most `E` split
jobs,

\[
 |e_j|\le E L_{\max}/j.
\]

The aggregate error is integral because both the chosen tail and `K'` are
integral, and it has coordinate sum zero by the exact-work identity.

For `e_j>0`, changing `e_j` base-`u^(j)` jobs to `v^(j)` changes the buffer
by `e_j(e_1-e_j)`.  For `e_j<0`, changing `-e_j` base-`v^(j)` jobs to
`u^(j)` produces the same signed formula.  Summing gives

\[
 \Delta=\sum_{j=2}^De_j(e_1-e_j)=-e.
\]

The supply `R_j>=ceil(E L_max/j)` is therefore sufficient independently in
every sign.  There is no hidden parity or divisibility condition.

## 5. Anonymous physical interpretation

If `K` is the conjugate tail of the physical socket-capacity multiset, tail
equality determines each exact multiplicity:

\[
 \#\{\hbox{pieces of length }q\}=K_q-K_{q+1}
 =\#\{\hbox{sockets of capacity }q\}.
\]

Thus an equal-length bijection exists.  This is the strongest physical
statement implied by aggregate tails alone.

It does not assign a named piece to a containing Boolean socket bottom.  A
two-by-two example already separates the assertions: let the two piece tops
be `{1}` and `{2}`, and the two candidate socket bottoms be `{1,2}` and
`{3,4}`.  The anonymous counts agree, but both tops see only the first
socket, so Hall fails.  Therefore the original claim that the usual
MLD-at-birth and named-top step follows automatically from exact aggregate
rounding was not proof-safe.

At zero aggregate slack, the existing MLD--Holder theorem has no positive
deviation reserve.  The corrected corollary consequently asserts only
anonymous integrality.  A named result additionally needs either an exact
zero-slack containment theorem or a separately proved unused physical
reserve.

## 6. Bank scaling

The displayed upper bound on bank size is valid only when the minimal
choice

\[
 R_j=\lceil D L_{\max}/j\rceil
\]

is made.  The source now says so.  Then

\[
 2\sum_{j=2}^DR_j=O(DL_{\max}\log D)
\]

jobs and

\[
 2\sum_{j=2}^DjR_j=O(D^2L_{\max})
\]

total work suffice.  With `D=Theta(sqrt(k))` and `L_max=O(k)`, these are
`O(k^(3/2)log k)` jobs and `O(k^2)` work.  The relevant short-job Boolean
cohorts are near-central and exponentially larger, but this numerical
abundance does not imply that the designated removal stays inside every
configuration facet.

## 7. Exact BFI dual

Let `J=R disjoint_union G`, with `G` the designated bank, and let

\[
 m_a(\theta)=\min_{p\in P_a}\langle\theta,p\rangle.
\]

The complete-instance slack and the cost of forcing the bank to its
designated configurations are

\[
 \begin{aligned}
 S_J(\theta)&=\langle\theta,K\rangle-
                    \sum_{a\in J}m_a(\theta),\\
 \Pi_G(\theta)&=\sum_{a\in G}
   (\langle\theta,\bar p_a\rangle-m_a(\theta)).
 \end{aligned}
\]

The residual feasibility slack is identically

\[
 \langle\theta,K-B\rangle-sum_{a\in R}m_a(\theta)
 =S_J(\theta)-\Pi_G(\theta).
\]

Separation of the compact Minkowski sum of residual configuration
polytopes from the down-set below `K-B` shows that the residual LP is
feasible exactly when

\[
 S_J(\theta)\ge\Pi_G(\theta)
 \quad\hbox{for every }\theta\in\mathbb R_{\ge0}^D.
\]

This is the correct BFI criterion.  The former
`|<theta,B>|` expression was not invariant under workload-price shifts and
omitted the bank jobs' alternative configuration values.

Because complete and residual work balance, both `S_J` and `Pi_G` are
invariant under adding a constant all-ones price.  Normalize a nonconstant
price by `min theta=0`, `max theta=1`.  Each forced length-`j` job then has
opportunity cost at most `j`, so

\[
 \Pi_G(\theta)\le2\sum_{j=2}^DjR_j.
\]

Thus the corrected uniform sufficient margin is

\[
 \inf_{\min\theta=0,\max\theta=1}S_J(\theta)
 \ge2\sum_{j=2}^DjR_j.
\]

A positive normalized slack density of order `W` would dominate this
polynomial quantity.  Bare all-price nonnegativity does not.

## 8. Precise implication for coefficient zero

The audited theorem proves the following conditional row:

\[
 \boxed{
 \mathrm{BFI}_D
 \Longrightarrow
 \text{exact same-depth anonymous integral fragmentation}.}
\]

This removes the `D` extreme-point exceptions without an adjacent-depth
absorber.  It does not prove

\[
 \mathrm{BFI}_D
 \Longrightarrow
 \text{named lower collar},
\]

and therefore does not yet imply `C=0`.  A coefficient-zero proof still
needs all of the following on one object:

1. the exact bank inequality `S_J>=Pi_G` for the Boolean instance;
2. actual labelled bank jobs and actual socket occurrences;
3. zero-slack named containment Hall, or a separately priced empty reserve;
4. the separately priced boundary targets;
5. protected owner-once upper-complete residence serialization.

Accordingly this theorem is a genuine same-depth anonymous rounding
advance, but not evidence that exact equality becomes a routine corollary
of `B(k)+O(1)`.

## 9. Final audit verdict

The algebraic root-lattice mechanism, the extreme-point split bound, the
coordinate error estimate, and the switch construction all pass.  The
source was corrected in three places:

* the socket conclusion is explicitly anonymous;
* the named zero-reserve implication was removed;
* the exact bank opportunity-cost dual replaced the informal price-of-`B`
  condition.

No all-price inequality, BFI bank, physical occurrence bank, named Hall
matching, protected serializer, `B(k)+O(1)`, or `nu(k)=B(k)` is claimed.
