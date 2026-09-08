# Forward period-prefix bounds: proved method, finite band pending

The new pruning-prefix upper-bound method passes a pure-proof audit on
the retained finite PBBS construction, particle-return and rooted-fibre
inputs. The submitted uniform thresholds of 57 and 87 depend on 713
finite certificates that were not supplied with the text. They are not
yet independently verified numerical results in this repository.

The [user claims](scratch/FORWARD_PREFIX_PERIOD_UNIFORM_USER_CLAIMS_20260908.md)
and [complete method audit](scratch/PBBS_FORWARD_PREFIX_PERIOD_COMPLETION_AND_UNIFORM_BAND_AUDIT_20260908.md)
are preserved separately.

For pruning circumferences `n_s=2a_s+1`, set

    beta_0=0, beta_(s+1)=(1+n_(s+1)*beta_s)/n_s.

The exact period is `lcm_s den(beta_(s+1)/d_s)`, including nonprimitive
rows. This is equivalent to the previously proved translated-return
formula. After a prefix, the least common multiple of the original n
and processed denominators divides every completion's actual period.

A leaf ending in `(a_s,a_(s+1))=(a,b)` represents exactly

    M=w*K(a,b), K(a,b)=binom(a,b)*binom(a,b+1)/a

roots, where w is the product of processed ordered-row multiplicities.
Its height is at most `H=s+b+1`. All possible next sizes and least-period
row classes conserve this exact mass. The unrounded charge
`M*(2H-1)/P` cannot increase when a leaf is refined.

With every unfinished branch retained, the integer certificate

    U=sum_leaves ceil(M*(2H-1)/P)

gives `N_r<=W_r+(2r+1)*U`. Thus `D*U<Cat_r` proves relative excess below
`1/D`. Independently rounded charges need not decrease on refinement;
their validity does not require such monotonicity. A terminal b=0 leaf
must process its last one-slot denominator before its period is called
exact.

The supplied claims are `1000*U_r<Cat_r` for r=28 through42 and
`10000*U_r<Cat_r` for r=43 through740. Together with the already verified
decreasing analytic envelope from r=741, these would give the uniform
starting dimensions57 and87. The reported refinement counts and partial
replay statistics remain attributed to the user until the finite data
are obtained and checked.

The presently verified [uniform thresholds](HEIGHT_ADAPTIVE_UNIFORM_FINITE_THRESHOLDS_20260908.md)
remain29,327,1483,6849 for relative errors1%,0.1%,0.01%,0.001%.
The exact earlier census separately certifies0.1% on57–102 and0.01%
on87–102. A finite band must not be extrapolated to all larger k.

An [independent bounded implementation and complete replay](scratch/PBBS_FORWARD_PREFIX_R163_ENGINE_AND_REPLAY_SPECIFICATION_20260908.md)
now pass. Fully refined casesr=1 through8 agree with the existing exact
period/height/cycle census, including unrounded collar costs. A single
case at r=163 gives

    U/Cat_163 < 0.000099417180896906105456651839 < 0.0001.

This independently certifies nu(k)<1.0001W(k) at k=327 and328. The
395refinements produce14342nodes and retain13947final leaves, including
13924unfinished leaves. A priority-free replay reconstructs every split,
preserves total Catalan mass and freshly sums all integer ceilings.
The [exact report](scratch/pbbs_forward_prefix_r163_20260908/attempt_r163/summary.json)
and complete transcripts are retained. Root and a second agent read the
entire implementation before its sole h100 run, which took0.33seconds.

No713-case enumeration has been run for this record. This successful
dimension pair is not a uniform threshold. It does not change the exact18
certificate or settle the all-dimensional equality goal.
