# Uniform cyclic middle windows require a growing compiler width

2026-09-09. Pure-proof audit by `exact_b_induction`, proposed by root.
No mathematical computation or literature search was run. This is a
necessary condition for extending the successful flat triple architecture,
not an all-dimensional construction or an obstruction to general OR words.

## 1. Precise hypotheses and middle-window rigidity

Let n=2r+1 with r>=1, M=binom(n,r)=binom(n,r+1), and let C be a cyclic
universal word of exactly M nonempty letters. Suppose every cyclic window
of q consecutive letters has rank r, where q>=1. Necessarily q<M:
a window of at least one full period has union [n], of rank n>r.
Thus the degenerate q=M case cannot satisfy the hypotheses; M=1 does
not occur for r>=1.

At a fixed cyclic endpoint the unions of suffix windows of lengths1,...,M
form a chain, which contains at most one distinct target of rank r.
Cyclic universality requires M distinct rank-r targets from M endpoints.
Hence every endpoint serves one, and no two endpoints serve the same one.
The q-window already has rank r, so **the M q-windows are precisely the
rank-r targets, once each**.

Any shorter window is contained in two adjacent q-windows. If its union
had rank r, both q-windows would equal that union, contradicting their
distinctness. Therefore every window shorter than q has rank below r.
Any window longer than q contains two distinct adjacent q-windows, so
its rank exceeds r. In particular, every rank-r witness has length
exactly q.

The same endpoint budget applies at rank r+1, which also has M targets.
Every endpoint must serve such a target. Its q-window has rank r, and
its (q+1)-window has rank greater than r. If the latter had rank greater
than r+1, all subsequent suffix unions would skip rank r+1 at that
endpoint, a contradiction. Thus **all (q+1)-windows have rank r+1 and
are precisely that rank's targets, once each**. In particular q+1<M,
since a full period has rank n>r+1 when r>=2. For r=1 the full-period
issue does not affect the argument: q=1 and q+1=2<M=3.

Consequently the q- and (q+1)-window rows form a middle-levels Hamilton
cycle after interleaving them. This is a consequence of an already
universal width-sized cyclic word, not a method for constructing one.

## 2. Lower-target capacity and the triple limitation

Every target of positive rank below r must have a cyclic witness of
length at most q-1. There are at most (q-1)M indexed windows of those
lengths. Therefore

    Lambda_<r := sum_(j=1)^(r-1) binom(2r+1,j)
                 <=(q-1)M.                            (2.1)

Odd-dimensional symmetry gives Lambda_<r=2^(2r)-M-1. Equivalently,

    q M>=2^(2r)-1,
    q>=ceil((2^(2r)-1)/M).                            (2.2)

For q=3 this is exactly

    3 binom(2r+1,r)>=2^(2r)-1.                        (2.3)

It is only a necessary scalar capacity check. Passing it does not supply
a simultaneous lower-target assignment, residence-compatible middle
ordering, upper coverage, or a usable opening.

Using the standard central-binomial asymptotic,

    M=((2r+1)/(r+1)) binom(2r,r)
      =(2+O(1/r)) 4^r/sqrt(pi r),

equation (2.2) gives

    liminf_(r->infinity) q/sqrt(r)>=sqrt(pi)/2.         (2.4)

In particular q=Omega(sqrt(r)); a fixed q, including q=3, cannot persist
through arbitrarily large odd dimensions in this architecture. No new
finite threshold or numerical test is asserted here.

## 3. Literal openings and the endpoint lower bound

Choose any cyclic phase and form a linear prefix opening

    A=C followed by the next d periodic letters,

of length M+d. Assume this A is universal. Its first q positions cannot
be endpoints of rank-(r+1) witnesses: every suffix there has length at
most q and rank at most r. The M distinct rank-(r+1) targets need M
distinct ordinary endpoints, so

    M+d-q>=M,      hence d>=q.                        (3.1)

Combining this with (2.2) yields the architecture-specific condition

    d>=q>=ceil((2^(2r)-1)/M).                         (3.2)

This is stronger in form than the general endpoint bound, which only
requires

    2^(2r)-1<=d M+d(d+1)/2.                           (3.3)

The triangular allowance in (3.3) is available to general linear words;
the periodic uniform-window architecture obeys the additional restriction
(3.2). Both force the same leading scale sqrt(pi r)/2, but they need not
have identical integer thresholds.

If d=q, all cyclic windows of length at most q+1 are present as ordinary
windows in A. Hence all targets of rank at most r+1 survive automatically
under these hypotheses. Higher targets may require longer windows, whose
only witnesses can cross the opening; they still need a separate safe-cut
proof. Thus d>=q is necessary, not sufficient for full linear universality.
A universal unqualified safe collar is M-1, because it retains every
cyclic window of length at most M; the exact goal requires much less.

No claim in this section applies to an arbitrary word merely because its
length is B(n). Such a word need not be a prefix opening, need not have
uniform middle-witness length, and need not obey d>=q for a globally
defined q. The scope is the explicit cyclic-core architecture above.

## 4. Attribution and the surviving construction requirement

The counting principle is already implicit in MASTER_HANDOFF Section2.1
and explicit in
`MATH_THEOREM_NEAROPTIMAL_WORD_FORCES_UNIFORM_ENDPOINT_CHAINS_20260801.md`.
The earlier
`PBBS_CAPPED_APERTURE_EXACT_MIDDLE_AND_LOWER_PIN_INTERFACE_20260908.md`,
Sections1--2, proves corresponding fixed-window rank and endpoint
obstructions for capped PBBS sources. This note specializes those
necessary capacity ideas to a cyclic universal core of exactly M
positions; it is not credited as a new general lower-bound method.

The useful current conclusion is that extending the successful triple
compiler requires changing its fixed window width. A possible all-r
construction must provide a growing q, a simultaneous short-target
compiler, and an opening with d>=q whose longer upper witnesses survive.
No such construction, matching sufficiency, or induction is proved here.
