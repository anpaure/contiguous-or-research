# Exact forward-prefix engine: one r=163 certificate attempt

2026-09-08. Prepared by `exact_b_finite_frontier`. **Status: the single reviewed run and its complete priority-free replay PASS.** It independently certifies nu(327)<1.0001W(327), and the established even lift gives nu(328)<1.0001W(328). No other new dimension or uniform band was computed.

The purpose is to implement and independently replay the finite method proved in [the forward-prefix audit](PBBS_FORWARD_PREFIX_PERIOD_COMPLETION_AND_UNIFORM_BAND_AUDIT_20260908.md). This task is restricted to complete small-r validation at r=1,...,8 and one fixed r=163 attempt at `10000*U<Cat_r`. It does not enumerate or certify the user-reported 713-case band.

Source: [census_pbbs_forward_prefix_integer_frontier_20260908.py](census_pbbs_forward_prefix_integer_frontier_20260908.py). Mathematical execution was restricted to `ssh h100`, hostname `arboghast`. Root and `exact_b_induction` independently read and approved the entire source before the sole run; see [the independent source audit](PBBS_FORWARD_PREFIX_INTEGER_FRONTIER_CODE_INDEPENDENT_AUDIT_20260908.md).

## State and exact charge

A live prefix node records

    (id,s,a,b,w,P,beta_num,beta_den),

where a=a_s>0, b=a_(s+1) satisfies 0≤b<a, w is the product of the already fixed ordered-row least-period multiplicities, beta is the reduced fraction beta_s, and P is the least common multiple of n=2r+1 and all processed denominator factors. Its exact root mass and height cap are

    M=w*K(a,b),   K(a,b)=binom(a,b)*binom(a,b+1)/a,
    H=s+b+1.

For b>0 its charge period is P. For b=0 the engine first computes

    beta_final=(1+beta_s)/(2a+1),
    P_final=lcm(P,den(beta_final)),

and uses P_final in the charge. This includes the unique final one-slot row, whose least period and multiplicity both equal one. The stored beta_s and P_s remain unchanged so the transcript's incoming-prefix convention is uniform; the separate `charge_period` field records the completed terminal period. The terminal height H=s+1 is exact.

Every node contributes the integer

    ceil_charge=ceil(M*(2H-1)/charge_period).

All fractions use exact integer numerators and denominators. There is no floating-point priority or probability estimate.

## Complete initialization and splits

The initial frontier has all r nodes `(s,a,b,w,P,beta)=(0,r,b,1,n,0)`, b=0,...,r-1. The engine checks that their masses sum exactly to Cat_r.

For a nonterminal parent, c ranges over every integer from max(0,2b-a) through b-1. Its incoming row has p=2b+1 positions and ell=a-2b+c units. For each divisor d of p, the number of ordered rows with period dividing d is the exact weak-composition count when p/d divides ell, and zero otherwise. Divisor subtraction gives the exact least-period count chi(p,ell;d). All positive classes are retained. Their sum is independently checked against binom(ell+p-1,p-1), including zero rows and p=1.

The next fraction is

    beta_next=(1+(2b+1)*beta)/(2a+1),

and every child has

    s'=s+1, a'=b, b'=c, w'=w*chi,
    P'=lcm(P,den(beta_next/d)).

Thus each split includes every possible next size and ordered-row period class exactly once. The program checks that child masses sum exactly to the parent mass. It also checks that each child's charge period is a multiple of the parent's and its height cap does not increase. The consequent unrounded charge domination is checked by integer cross multiplication. The total rounded U is updated by subtracting the parent's ceiling and adding every child ceiling; an increase is allowed and counted.

## Priority and stopping do not enter the proof

The selected parent has the largest integer ceiling charge, with the smallest node id breaking ties. Priority is only an efficiency choice. The graph of prefixes is not pruned by a heuristic, and no incomplete child collection replaces a parent.

The r=163 driver stops at the first strict integer certificate `10000*U<Cat_163`, or at a fixed cap. The caps are 10,000 successful refinements and 1,000,000 generated prefix nodes. It may stop sooner at a soft CPU/wall reserve threshold so the current complete frontier can be written and replayed before the overall hard limits of 120 CPU seconds, 150 wall seconds, and 2 GiB address space. If a proposed complete split would exceed the node cap, that parent remains a live leaf. No root mass is discarded.

Every stopping frontier is a valid upper bound, even if the requested inequality does not pass. A capped failure to achieve the target is not a proof that the target inequality is false. Rounded U is never assumed monotone under splitting.

## Complete log and priority-free replay

Each run directory contains:

* `splits.jsonl`: initialization and every split's parent id, deterministic child-id interval/count, exact child mass, child ceiling sum, and updated frontier totals.
* `final_leaves.jsonl`: every remaining leaf, using the explicit column schema in the transcript header. It records the incoming state and freshly derived mass, height cap, charge period, and ceiling.
* `summary.json`: exact integer U, Cat_r, the strict target margin when applicable, frontier sizes, limits, and replay status.

The replay starts again from all r initial leaves. It reads only the recorded parent choices; it has no priority queue and does not infer any property from the original selection order. It regenerates every possible child of each selected parent, including all ordered-row period classes. It uses `Fraction` for the beta update and denominator of beta_next/d, independently of the integer update helper in the generator. It checks all split mass identities and period/height inequalities.

Finally, replay pops every listed final leaf exactly once from its reconstructed live frontier. It recomputes its mass, terminal denominator when needed, and integer ceiling directly. Duplicate final records, omitted leaves, extra leaves, wrong states, or wrong derived fields fail. Only after this does it freshly sum final mass and U and check that the mass is Cat_r and U matches the reported value. No enormous global rational denominator or rounded-charge monotonicity is needed.

The generator is released before replay so their complete live frontiers do not coexist in memory. The source's `replay_frontier` function can also replay a saved transcript without constructing a new priority traversal.

## Small-r validation and numerical interpretation

Before r=163, the same engine refines every leaf to a terminal for r=1,...,8. The exact reference is the existing full rotation-period census, pinned by SHA-256

    43b52c9d3ed72b9901dc7c6aca96a4ce8f46a12e322fc01c181da1a3412869b2.

At each terminal, n*M/v must be an integer cycle count. The engine checks total root mass, signature count, total cycles, height sum, every period histogram, every height histogram, and the native collar overhead against that reference. In particular, it computes the **unrounded** terminal fraction and checks exactly

    n*sum(M*(2h-1)/v)=C_reference.

It does not compare rounded U to C/n as if they had to be equal. Every small-r transcript is then replayed without priority as above.

At r=163 the certified construction bound represented by any complete frontier is

    N≤W(327)+327U,   W(327)=327*Cat_163.

A passing strict test proves nu(327)<1.0001W(327); the established doubled literal lift gives the same relative bound at dimension 328. A nonpassing but fully replayed frontier would still supply the stated exact rational upper bound U/Cat_163. Neither outcome by itself establishes the complete claimed uniform band or all-dimensional exact equality.

## Completed exact result

The sole run passed every complete small-r validation and every priority-free replay. The small-r native overheads for r=1,...,8 were exactly

    1,4,9,22,52,128,409,892,

and their cycle counts were exactly

    1,2,3,6,12,26,73,146.

Every full period histogram, height histogram, terminal signature count, and unrounded charge matched the SHA-pinned independent partition census.

At r=163 the requested strict integer test passed after **395 refinements**, **14,342 generated nodes**, and **13,947 retained final leaves**. Of the final leaves, 13,924 remain nonterminal and all their root mass is explicitly retained; 23 are terminal. The maximum processed prefix depth was three. No rounded-U increase happened in this particular traversal, but no proof step or stopping test assumes that property.

The exact integers are

    Cat_163 = 36807214530352423207683103791586102953744012679838920659909415950802761947893119968555926155300
    U       = 3659269505275277758600286890594857530514283537895747540917474187169465457309453311181253834

The independent priority-free replay regenerates every one of the 395 complete splits, checks all 14,342 generated nodes through their split ancestry, and consumes all 13,947 final leaf records exactly once. Its freshly summed root mass is Cat_163 and its freshly summed integer ceiling charge is U. The exact positive margin is

    Cat_163-10000*U =
    214519477599645621680234885637527648601177300881445250734674079108107374798586856743387815300.

Integer division gives the outward enclosure

    0.000099417180896906105456651838
        <= U/Cat_163
        < 0.000099417180896906105456651839
        < 0.0001.

Thus the retained height-adaptive construction satisfies the claimed relative upper bound in this independently checked gap case. This is a constructive charge certificate; the enormous full 327-coordinate word was not materialized.

The entire run, including all eight small-r validations, all saved leaves, and all priority-free replays, used 0.3283 wall seconds and 0.3274 CPU seconds, far below every fixed cap. There was no retry, alternate priority, broader band, solver, or random selection.

Artifacts:

* [Complete report](pbbs_forward_prefix_r163_20260908/forward_prefix_r163_complete_certificate.json).
* [r163 summary and exact integer bound](pbbs_forward_prefix_r163_20260908/attempt_r163/summary.json).
* [Every r163 split](pbbs_forward_prefix_r163_20260908/attempt_r163/splits.jsonl).
* [All retained r163 leaves](pbbs_forward_prefix_r163_20260908/attempt_r163/final_leaves.jsonl).

The same bundle contains the complete split logs, final leaves, and independently replayed summaries for r=1,...,8. The remote directory is `/home/amodo/exact-b-pbbs-forward-prefix-r163-20260908/`; the sole command was `python3 /home/amodo/census_pbbs_forward_prefix_integer_frontier_20260908.py`.

The claimed 713-case finite band remains a separate evidence obligation. This successful implementation validates the method and one nontrivial missing numerical case; it does not substitute one case for the unprovided band-wide transcripts.
