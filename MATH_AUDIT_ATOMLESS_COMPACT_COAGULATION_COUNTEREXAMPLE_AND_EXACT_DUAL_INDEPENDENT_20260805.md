# Independent audit: atomless compact coagulation counterexample and exact dual

**Date:** 2026-08-05  
**Method:** pure mathematical replay; no computation, search, or solver  
**Audited source:**
`MATH_THEOREM_ATOMLESS_COMPACT_COAGULATION_COUNTEREXAMPLE_AND_EXACT_DUAL_20260805.md`  
**Audited source SHA-256:**
`85adad66000c546e14bb155317dcab1ffcea59247a412a823bc95303cd013daa`  
**Verdict:** **GO after exact clarifications.**  The counterexample, its
continuous covering-price separator, the generic closed-upward-cone theorem,
the interval-flow equivalence, the product-renewal corollary, the compact
finite-arity signed dual, and the open-interval representability gate are all
correct.  The source was clarified at four proof boundaries: tightness is now
carried out in the actual open configuration space; the zero-source
interval-flow case is explicit; Theorem 5.1 explicitly assumes pointwise job
representability; and the signed constant tests are described as occurrence
count bounds rather than an equality.  No Rayleigh price inequality or
integral/literal rounding follows.

## 1. Definitions and universal cuts

For one exact configuration with socket count `n`, strict socket support
`y_i<b` gives

\[
                         x=\sum_i y_i<nb.
\]

Thus `n>x/b`, whose least integer solution is

\[
                    \left\lfloor{x\over b}\right\rfloor+1.
\]

This proves (2.1), including the case in which `x/b` is an integer.

For a threshold `0<t<b`, if exactly `k` sockets exceed `t`, then

\[
                              kt<x.
\]

The greatest integer strictly below `x/t` is
`ceil(x/t)-1`, proving (2.2).  The strict/open endpoint conventions are
therefore correct.  Atomlessness is used only when replacing one threshold
representative by another in the stated applications; it is not needed for
either cut itself.

## 2. Counterexample ledger

The job measure in (3.1) has mass one and mean

\[
 50\int_1^{51/50}x\,dx={101\over100}.
\]

The two beta densities in (3.3) each have mass one and respective means
`19/20` and `1/20`.  Hence

\[
 \nu(0,1)={1\over10}+{43+47\over45}={21\over10}
\]

and

\[
 \int y\,d\nu
 ={1\over20}+{43\over45}{19\over20}
                +{47\over45}{1\over20}
 ={101\over100}.
\]

Thus exact work and the strict count window `2<21/10<3` both hold.

At `t=51/100`, the beta-tail formula is

\[
 \nu((t,1))={1\over10}(1-t)
  +{43\over45}(1-t^{19})+{47\over45}(1-t)^{19}.
\]

The elementary estimate `t^19<1/1000` is safe (already
`t^16<(7/100)^4<1/1000`).  Dropping the last positive term gives

\[
 \nu((t,1))>{49\over1000}+{43\over45}{999\over1000}
 ={45162\over45000}>1.
\]

Two sockets strictly above `t` have sum strictly above `2t=51/50`, while
every job is at most `51/50`.  Therefore the threshold capacity is exactly
one per job, contradicting the displayed tail mass.  There is no endpoint
loophole at the maximal job.

## 3. Continuous covering-price witness

The tail map is continuous because `nu` has a density.  Since its value at
`51/100` is strictly above one, one may choose

\[
                         {51\over100}<s<1,
 \qquad \nu((s,1))>1.
\]

A continuous ramp `w`, zero through `s`, bounded by one, and converging
monotonically to `1_(s,1)` can consequently be chosen with
`int w dnu>1`.  Since `2s-L>0`, the constant

\[
 C\ge\max\{1/s,1/(2s-L)\}
\]

is finite.  The price `a(y)=Cy-w(y)` is nonnegative: below `s` this is
immediate, and above `s` it follows from `Cy>=Cs>=1>=w(y)`.

For a cover, let `k` be the number of pieces on which `w` is positive.  If
`k<=1`, then

\[
                       \sum_i a(y_i)\ge Cx-1.
\]

If `k>=2`, all those pieces exceed `s`, and

\[
 \sum_i a(y_i)-(Cx-1)
 \ge C(ks-L)-k+1.
\]

The last expression is nondecreasing in `k` because `Cs>=1`; at `k=2` it
is nonnegative because `C(2s-L)>=1`.  Hence

\[
                         a^\star(x)\ge Cx-1
\]

throughout the job support.  Exact work yields

\[
 \int a^\star\,d\mu\ge C{101\over100}-1
 > C{101\over100}-\int w\,d\nu=\int a\,d\nu.
\]

The strict comparison is exactly `int w dnu>1`, so the source's violation
has the correct direction.  The separator is bounded, continuous, and
nonnegative, and hence lies in the literal test class of Theorem 4.1.

## 4. Closed upward cone and separation

Let `F_mu` be the available-capacity cone from the source.  Convexity and
upward closure are immediate by mixing cover kernels and by adding unused
capacity.

For closedness, suppose `B_n -> B` narrowly and let `rho_n` witness
`B_n in F_mu`.  Narrow convergence on the Polish socket space `(0,b)` gives
a uniform mass bound and uniform tightness.  Since

\[
 \int N\,d\rho_n=\lambda_n(0,b)\le B_n(0,b),
\]

the mass on configurations with `N>R` is `O(1/R)`.  For a compact
`K` contained in `(0,b)`, domination gives

\[
 \rho_n\{\hbox{some }y_i\notin K\}
 \le\lambda_n((0,b)\setminus K)
 \le B_n((0,b)\setminus K).
\]

Taking `K` from uniform tightness and then `R` large proves tightness in the
actual countable disjoint union; no socket mass is allowed to disappear at
zero or at `b`.  The cover inequality is closed on each finite-arity
component.  For nonnegative `f in C_c((0,b))`, Portmanteau gives

\[
 \int\sum_i f(y_i)\,d\rho
 \le\liminf_n\int\sum_i f(y_i)\,d\rho_n
 \le\int f\,dB.
\]

Therefore the limiting used marginal is at most `B`.  The finite-positive-
measure narrow topology on a Polish space is metrizable, so this sequential
argument is the closedness required by separation.

If `nu` lies outside the cone, strong separation supplies a bounded
continuous price.  Upward closure forces it to be nonnegative: a negative
value at one socket would let one add arbitrarily much capacity there and
drive the separating functional downward.

For a fixed nonnegative price, the infimum over cover kernels separates by
job.  To justify the exact identity, restrict sockets to
`[1/M,b-1/M]`.  An inclusion-minimal cover has total size below `L+b` and
therefore uses at most `M(L+b)` pieces.  The restricted configuration space
is compact and admits measurable near-minimizers.  These restricted values
decrease pointwise to the literal covering closure, because every finite
socket list is eventually contained in one restriction.  Repetitions of one
fixed interior socket give a uniform finite dominator on `[b,L]`.
Dominated convergence proves

\[
 \inf_{B\in F_\mu}\int a\,dB
       =\int a^\star(x)\,d\mu(x).
\]

No lower-semicontinuity of `a^star` is asserted or needed; at strict socket
endpoints such closures can have jumps.

Finally, for a relaxed witness with used marginal `lambda<=nu`, exact work
gives

\[
 0\le
 \int(\sum_i y_i-x)\,d\rho
 +\int y\,d(\nu-\lambda)=0.
\]

Both terms vanish.  The first makes every cover exact.  For the second,
positivity of `y` implies `nu-lambda=0` (apply the zero integral on each
`[1/m,b)`).  This verifies exact zero trimming even though the socket support
is not bounded away from zero.

## 5. Interval-flow equivalence

Ordering each finite socket list and placing its pieces consecutively on
`[0,x)` preserves the length occurrence marginal and gives occupation
`1_(t<x)`.  Averaging produces

\[
                         G(t)=\mu((t,\infty)).
\]

Conversely, if `sigma_0,sigma_1` are the start and end marginals, then

\[
 \int f\,d(\sigma_1-\sigma_0)
 =\int f'(t)G(t)\,dt
 =\int f\,d\mu-\mu([b,L])f(0).
\]

Thus the sign is correct: the interval flow has source
`mu([b,L]) delta_0` and sink `mu`.  At every positive endpoint, the outgoing
mass is a submeasure of incoming mass; regular conditional probabilities
pair the continuing part and terminate the complementary `mu` part.
Ionescu--Tulcea iteration from zero produces a measure on directed paths.

Any edge flow not reached by those paths has equal start and end marginals.
Its occupation density has zero distributional derivative and is therefore
constant almost everywhere.  Its integral is the residual total interval
work, which is finite.  A nonzero constant on `[0,infinity)` is impossible,
so the occupation is zero; positive edge lengths then force the residual
edge measure to vanish.

If the source mass is zero, positivity and (4.12) already force `eta=0`.
Otherwise

\[
 {\eta(\mathcal E)\over\mu([b,L])}
 ={\nu(0,b)\over\mu([b,L])}<\infty
\]

is the mean path length.  Infinite paths therefore have zero path measure.
The finite paths terminate with marginal `mu`, use length occurrences `nu`,
and have total length equal to their terminal coordinate.  This proves the
converse without a hidden finite-path assumption.

## 6. Product-renewal corollary

For `eta=q tensor nu` with `q` a probability measure, the length marginal is
exactly `nu`.  At time `t`, Fubini gives occupation

\[
 \int_{[0,t]}\nu((t-a,b))\,dq(a)
 =\int_{[0,t]}\overline\nu(t-a)\,dq(a).
\]

Therefore (4.15) is precisely the occupation identity in Theorem 4.2.  The
corollary is sufficient only; it does not claim that start and length can be
made independent in every flow.

## 7. Compact finite-arity dual

Theorem 5.1 needs one support hypothesis and no separate mass hypothesis.
The source now states it exactly: `S` is nonempty compact with
`min S>=q>0`, `J` is nonempty compact, and every `x in J` is representable
as a finite sum of members of `S`.  Then every representation has

\[
 n q\le x\le\max J,
 \qquad
 n\le N=\left\lfloor{\max J\over q}\right\rfloor.
\]

Hence the exact configuration space is a finite union of compact fibres and
projects onto all of `J`.  Measures on it with fixed job marginal `gamma`
form a nonempty compact convex set.  The aggregate occurrence map is weakly
continuous, so its image `K` in the finite-measure space on `S` is compact
and convex.

Membership in `K` is equivalent to

\[
 \int\phi\,d\lambda
 \ge\inf_{\kappa\in K}\int\phi\,d\kappa
 \qquad(\phi\in C(S)).
\]

For fixed `x`, the fibre minimum is exactly `m_phi(x)`.  Compact measurable
selection gives

\[
 \inf_{\kappa\in K}\int\phi\,d\kappa
 =\int_Jm_\phi(x)\,d\gamma(x),
\]

which is (5.3).  This also verifies the converse separation direction.

No additional work equation is needed: `phi(y)=y` and `-y` make the two
dual inequalities exact opposites and force

\[
                    \int y\,d\lambda=\int x\,d\gamma.
\]

The tests `phi=1` and `-1` analogously enforce the feasible minimum- and
maximum-arity bounds on total occurrence mass; they do not assert that job
mass and occurrence mass are equal.

If jobs outside the representable semigroup were permitted, the fibre in
(5.2) would be empty there and the displayed finite minimum would be
undefined.  One could instead use the extended value `+infinity`, but the
source's explicit representability assumption is the clean exact form.

## 8. Open-interval remainder gate

For actual sockets in `(q,b)`, a remainder represented by exactly `n`
pieces lies in `(nq,nb)`.  Conversely, every `z` in that interval is the sum
of `n` equal allowed values `z/n`.  Therefore

\[
                 \mathcal R(q,b)=\bigcup_{n\ge1}(nq,nb)
\]

is exact.

Successive intervals overlap precisely when

\[
                    (n+1)q<nb
 \quad\Longleftrightarrow\quad n(b-q)>q.
\]

If `q<b/2`, this already holds at `n=1` and hence at every later `n`, giving
`R(q,b)=(q,infinity)`.  If `q=b/2`, the first two intervals meet only at the
excluded point `b`, while every later pair overlaps; the only additional
missing point is `b`.  If `q>b/2`, the inequality eventually holds and is
then permanent, so only finitely many genuine interval or singleton gaps
remain.  This proves the primary-coupling representability warning exactly.

Satisfying this pointwise gate and every threshold cut remains only
necessary; the full signed dual or covering-price family is stronger.

## 9. Scope

The audited source proves an anonymous continuum theorem.  In particular it
proves:

1. count/work/atomlessness/continuous positivity do not imply coagulation;
2. the counterexample violates both an explicit tail cut and a continuous
   covering price;
3. all nonnegative bounded-continuous covering prices are an exact generic
   criterion under equal work;
4. interval flows are equivalent to finite exact coagulations;
5. a product renewal identity is a concrete sufficient face;
6. the compact gapped remainder has the exact signed finite-arity dual; and
7. an open socket interval imposes the exact union-of-sum-intervals gate.

It does **not** prove that the Rayleigh residual passes any nontrivial price,
construct the adaptive Rayleigh kernel, round a continuum solution to one
copy of each discrete job/socket, preserve named Boolean containment, or
provide literal serialization and upper/residence coverage.  It therefore
does not prove `nu(k)=B(k)+O(1)`.
