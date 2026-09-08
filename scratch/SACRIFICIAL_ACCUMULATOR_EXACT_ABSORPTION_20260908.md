# Exact sacrificial absorption and legal continuation

This note concerns the principal paired-rectangle charge in MASTER_HANDOFF.md, Appendix A.7. It does not claim a new full-cube coefficient. All eight principal factors and the sacrificial factor are strict ascending set chains on disjoint physical supports. Every product-SCD child is retained. The inequalities below do not assert that finite compiler overhead is nonincreasing; A.7's fixed-factor, lower-degree overhead argument remains necessary.

## 1. Exact absorption for eight equal principal chains

Let the eight principal chains have common length a=2s, and let the ninth chain have arbitrary length r. The sacrificial chain need not be shortest. In each of the fourteen template rows, either four-axis staircase has

    R=s^3 chains,       V=5s^4 total membership.

Its chain indexed by j_2,j_3,j_4 in {0,...,s-1} has length

    L_j=8s-3-2(j_2+j_3+j_4).

Thus min L_j=2s+3, max L_j=8s-3, and the average chain length is exactly 5s. After absorbing the ninth factor into the left staircase, its membership is rV and its exact product-SCD chain count is sum_j min(r,L_j). Pairing with the right staircase therefore gives the principal upper charge

    P_ref = 14 V [ rR + sum_j min(r,L_j) ].

Normalization is by actual volume r a^8. Writing alpha=35/32, this becomes

    P_ref/(r a^8)
      = alpha/(2a) [ 1 + (1/R) sum_j min(1,L_j/r) ].

This equality describes the indexed rectangle charge of the specified construction, not the optimal word length. All overlap and template multiplicities remain charged.

With r/a -> t and s -> infinity, L_j/a tends to

    T = 4-U_1-U_2-U_3,

where the U_i are independent uniform variables on [0,1]. By symmetry this is also the law of 1+U_1+U_2+U_3. The limiting normalized charge is

    F(a,r) = alpha/(2a) [1 + E min(1,T/t)],       t=r/a.

It equals alpha/a for t<=1, and is strictly smaller for t>1. For t>=4 it equals

    alpha/(2a) [1 + 5/(2t)].

An explicit formula usable without numerical integration is

    E min(1,T/t)
      = 1 - (1/(24t)) sum_{j=0}^3 (-1)^j C(3,j)(t-1-j)_+^4.

For large t, the preceding 5/(2t) formula avoids subtracting nearly equal fourth-degree terms.

## 2. Exact discrete supermartingale under sacrificial merges

Fix a strict principal staircase image-chain length L and set

    g_L(r)=min(r,L)/r.

A complete product SCD of sacrificial length r with an unread length b has children

    c=|r-b|+1, |r-b|+3, ..., r+b-1.

There are min(r,b) children and their lengths sum to rb. Under the exact volume-biased law, a child c has probability c/(rb). Consequently

    E[g_L(c) | r,b] = (1/(rb)) sum_c min(c,L)
                    <= min(r,L)/r.

The proof has two exhaustive cases. If r<=L, use sum_c min(c,L)<=sum_c c=rb. If r>L, there are at most b children and every summand is at most L, giving sum_c min(c,L)<=bL. No stochastic limit or distributional assumption on b is involved.

For fixed principal chain families, let the left family have lengths L_i, total membership V_L, and the right family have R_R chains and total membership V_R. If P is the actual volume of the principal product, its normalized principal absorption charge is

    R_R V_L/P + (V_R/P) sum_i g_{L_i}(r).

It is therefore a supermartingale under every complete merge into the sacrificial slot. Equivalently, the sum of principal charges over all new children is at most b times the old principal charge. This proves the deterministic normalized-charge inequality while retaining every child.

The unread slot is selected before inspecting its length. Since the displayed inequality holds separately for every b, it remains valid under any unread-length distribution and at adapted stopping decisions. It does not permit dropping unsuccessful children, restoring an ancestor chain after a failed merge, or substituting a past historical radius for a current factor.

The continuum interpretation agrees: min(1,L/|x|) is the Newton potential of a uniformly charged sphere in three dimensions, hence is superharmonic. The discrete proof above is stronger for the actual compiler because it directly addresses the exact SCD child law.

## 3. Bounded freeze-and-dump diagnostic

The tested legal policy runs nine shortest-slot clocks for a deterministic fraction theta of the available variance, freezes the eight largest slots, and puts every remaining factor into the ninth slot. Its terminal charge uses the preceding refined absorption factor and permits the existing line-cover upper bound as an alternative.

All computations ran through ssh h100. A bounded test used 32,768 independent paths and 2,048 mesh updates, torch seed 83172, and independent continuation normals from NumPy seed 91823. Prefix paths and continuation normals were reused across theta for paired comparisons. The retained eight radii were not artificially equalized: the numerical charge included the finite-mesh padding multiplier alpha*A^7/product(a_i), with A their maximum.

The finite-mesh padded staircase baseline was 1.4863039746, with Monte Carlo standard error 0.00137318. This is substantially above the limiting c_9 and is not an estimate of c_9. The post-freeze cost minus that baseline was:

| theta | paired increase | Monte Carlo standard error |
| --- | ---: | ---: |
| 0.5 | 0.4384398824 | 0.00102697 |
| 0.8 | 0.1574301826 | 0.00025947 |
| 0.9 | 0.0763709524 | 0.00013256 |
| 0.95 | 0.0368637237 | 0.00011539 |

The comparison baseline used the padded staircase charge alone. Allowing its line alternative only lowers that baseline, so the positive increases remain conservative. These results diagnose this particular policy on this mesh; they are neither a continuum exclusion theorem nor a bound on all adapted policies. In particular they do not exclude state-dependent stopping rules.

The isolated remote data file is:

    /home/amodo/accumulator_policy_20260908.aSaz9v/radii_seed83172_m2048_n32768.npy

An initial GPU product reduction failed because the remote PyTorch JIT could not find libnvrtc-builtins.so.13.0. The successful bounded run evaluated products and the final charge on the h100 CPU after generating the radius paths on its GPU. No local computations were used.

## 4. Remaining constructive requirement

The supermartingale proves that sacrificial continuation is legal and can reduce a fixed principal family's normalized charge. It does not show that sacrificing time to create those principals is better than A.7's nine-clock balancing.

In particular, replacing the sum of nine exit times by eight is unjustified. Eight paths can reach a predetermined threshold earlier, but every branch that has not completed its threshold crossings before the factor deadline must still be charged. Choosing a retrospectively completed level would require an additional legal covering construction for already assigned factors.

No improved asymptotic coefficient is established here. A constructive improvement still requires an explicit adapted policy and an expectation bound including all branches and the compiler's prescribed order of limits.

## 5. A finite warm-up is washed out by subsequent minimum updates

There is a useful limitation on optimizing only the initial factors. Consider M scaled independent chi-three inputs, equivalently Gaussian radial updates of variance 1/M. After seeding the nine slots, permit any legal adapted warm-up using at most k_M updates, where k_M/M -> 0. Then use the ordinary nine-slot minimum-update rule for every remaining input and apply the existing terminal compiler, optionally with the refined absorption charge above.

For A.7's numerical terminal upper-charge functional, with the equal-principal absorption refinement used in this note, this modification has the same limiting coefficient alpha*sqrt(pi/8)*E sqrt(S_9) as A.7. Here S_9 is the sum of nine independent unit-ball exit times. This statement does not assert optimality among other terminal compilers or among finer evaluations of contracted unequal-principal staircase images.

For the radius limit, couple the entire legal process to nine independent Brownian paths with separate clocks. Every local clock during the warm-up is at most k_M/M. Brownian uniform continuity therefore makes the largest warm-up historical radius tend to zero almost surely. Subsequent minimum updates preserve their current maximum. Once their frontier exceeds the vanishing warm-up maximum, the same minimum-update balance argument and hitting-time sandwich as A.7.5 apply. They force the eight largest terminal radii to tend to the same inverse hitting-time level A, with A^(-2) distributed as S_9. No warm-up past maximum can survive at a positive limiting scale.

Uniform integrability does not require a rate of decay for k_M/M. The radial Gaussian transition kernel is stochastically increasing in its initial radius, by one-dimensional Bessel-process comparison. Couple two transitions by a common quantile. On sorted nine-vectors, replacing the minimum and sorting again preserves coordinatewise order: the changed coordinates remain ordered under this coupling and so do all untouched coordinates. Therefore, conditional on any nonnegative warm-start vector, at least M/2 subsequent minimum updates stochastically dominate the same number of fresh minimum updates from zero. The latter has A.7's reciprocal uniform integrability after the fixed time rescaling. Every terminal charge considered here is bounded by the line alternative 2/B, where B is the second smallest terminal radius. This yields the required uniform integrability, uniformly over the warm-up law.

At the limiting terminal state, eight radii equal a=A and the remaining radius is at most a. Absorbing that remaining factor gives exactly alpha/a: the refined absorption has no discount when r/a<=1. If one instead absorbs a large factor and uses the same formal padded staircase-length upper bound, its charge is alpha/r, while the line bound is 2/a; neither improves alpha/a. A finer exact evaluation after contracting the unequal principal's repetitions is outside this assertion. The equal-principal refinement proved above consequently does not change this limiting upper charge.

In particular, a fixed finite P-optimal initialization followed by indefinitely many minimum updates cannot improve the A.7 limit through this terminal bank. A policy with a nonvanishing allocation fraction, or a different limiting terminal geometry or compiler, is needed. This statement assumes the prescribed legal adapted Gaussian-kernel continuation; it does not authorize inspecting unread increments or discarding SCD children.
