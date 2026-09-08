# Second independent audit of the corner-period collar barrier

2026-09-08. Pure-proof review by `exact_b_induction`. I read
`PBBS_CORNER_PERIOD_UPPER_BOUND_AND_EXPONENTIAL_COLLAR_BARRIER_AUDIT_20260908.md`
in full, using the separately proved exact translated-return formula.
No computation was run. Verdict: **PASS; no correction required**.

On a constant peak-count block with value a, the exact identity

    1/(n_s n_(s+1))=(1/n_(s+1)-1/n_s)/(2a)

telescopes to the block length divided by its two endpoint
circumferences. Thus the lcm of adjacent corner products clears every
boundary sigma. At an interior depth t, the preceding row has zero
mass and therefore least period1, so its repetition factor is n_t.
Multiplication changes the remaining partial-block contribution to
(t-b)/x, which is also cleared by that same corner lcm. This proves
the asserted upper divisor for every row signature, including
nonprimitive rows and the one-site bottom.

Each adjacent corner product divides the product of all corners, so
their lcm does as well; no coprimality assumption is present. With q
distinct positive peak counts, q(q+1)/2<=r and therefore

    v<=n^q,   q<=Q_n=floor((sqrt(4n-3)-1)/2).

For n>=3, the sequence (2q-1)/n^q is nonincreasing because its
successive ratio is (2q+1)/(n(2q-1))<=1. The exact state average of
(2h-1)/v consequently yields the integer lower bound

    C_n>=ceil((2Q_n-1)W(n)/n^Q_n).

This is a lower bound on the collar overhead of the UNCHANGED native
height-adaptive compiler. For example the weaker elementary estimate
W(n)>=2^n/(n+1), together with Q_n<sqrt(n), already gives

    C_n>=2^n/[(n+1)n^(sqrt(n))],

which has the asserted exponential logarithmic scale. Since the
endpoint-bound excess B(n)-W(n) is only O(sqrt(n)), that particular
compiler cannot attain B(n) eventually. For the exact odd-to-even
doubling, W(n+1)=2W(n), so doubling the same word doubles its collar
overhead as well.

None of these steps gives a positive lower bound on nu(n)-W(n) or
nu(n)-B(n). Shortening collars, recoding source states, capping,
fusion with separately checked coverage, or another construction is
outside the barrier. The root note states that limitation correctly.
This is an internal independent mathematical review, not external or
proof-assistant certification.
