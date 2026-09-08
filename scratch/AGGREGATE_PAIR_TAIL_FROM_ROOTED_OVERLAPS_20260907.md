# Aggregate pair-codegree tails from one-root overlap bounds

Date: 2026-09-07. Pure proof; no computation. This lemma controls the
total edge mass incident to overlarge pairs without a separate kernel
for every possible pair distance. It does not itself maintain an
adaptive packing process.

## 1. Finite rooted setup

Let H be a finite simple r-uniform hypergraph. Fix a vertex v of
degree D>0, put s=r-1, and sample incident edges uniformly. For u!=v let

    p_u=deg(v,u)/D,             p_u<=delta,

where 0<delta<=1. Assume the full rooted overlap bounds

    E_Q[sigma^(-(|E intersect Q|-1))-1] <= Xi_sigma

hold for every reference edge E containing v, at each parameter used
below. All Xi are nonnegative. Condition on retaining v and retain
every other vertex independently with probability rho in (0,1).
Let Y_vu count retained edges containing both v and u, including the
retention indicator of u. Put mu=D rho^s.

Fix an integer m>=2 and Holder conjugates q,q'>1,
1/q+1/q'=1. Define

    R_m=product_{j=1}^{m-1}(1+Xi_{rho^(q'j)}).

Then

    sum_{u!=v} E Y_vu^m
      <= mu^m s delta^((m-1)/q) R_m^(1/q').             (1)

Consequently, for any L>0 and A=L delta mu,

    sum_{u!=v} E[Y_vu 1{Y_vu>A}]
      <= mu s R_m^(1/q')
                (L delta^(1/q'))^(-(m-1)).             (2)

The sums may range over the entire ground vertex set; vertices of
zero pair degree contribute zero. No bound on the number of such
vertices is needed.

## 2. Proof

Choose E_1,...,E_m independently and uniformly from the D edges through
v, with repetitions allowed. Write E_i^-=E_i minus {v}, and set

    I=|intersection_i E_i^-|,
    J=ms-|union_i E_i^-|.

Expanding the powers and then summing over u gives the exact identity

    sum_u E Y_vu^m / mu^m = E[I rho^(-J)].               (3)

The intersection multiplicity has

    E I=sum_u p_u^m <= delta^(m-1) sum_u p_u
                       =s delta^(m-1).

Since 0<=I<=s, E I^q<=s^q delta^(m-1).

The other Holder factor is controlled by the full rooted kernel.
Revealing E_j after its predecessors, the new overlap with their
union is at most sum_{i<j}|E_i^- intersect E_j^-|. Holder over these
j-1 factors, followed by the uniform reference-edge bound, gives

    E rho^(-q' J) <= product_{j=1}^{m-1}
                                  (1+Xi_{rho^(q'j)})=R_m.

Thus Holder applied to (3) proves (1). The pointwise inequality
Y 1{Y>A}<=Y^m/A^(m-1) proves (2).

## 3. Expected total pruning charge

Suppose now H is D-regular on N vertices and the same delta and Xi
work at every anchor. In the independently retained hypergraph delete
every edge containing a pair with codegree greater than A=L delta mu.
Counting ordered anchors (and therefore allowing harmless double
counting), the expected number of deleted edges is at most

    N rho mu s R_m^(1/q')
                       (L delta^(1/q'))^(-(m-1)).        (4)

The expected number of all retained edges is N rho mu/r. Hence the
ratio of these EXPECTATIONS is at most

    r s R_m^(1/q') (L delta^(1/q'))^(-(m-1)).             (5)

This does not assert concentration of the random denominator.

## 4. Transfer to a proved dependent survival upper law

Suppose a different random retained set has positive probability of v
surviving and, conditional on that event, the following inequality for
every union U of an ordered m-tuple of original incident edges, with
repetitions allowed and v removed:

    P(U survives | v survives) <= C_m rho^|U|.           (6)

Then (1) and (2) hold with the additional factor C_m. This follows
term by term in the nonnegative expansion (3). It does not require
independent retention, conditional pair laws, or subtracting moments.
Here mu=D rho^s is a reference scale, not necessarily the actual mean.
The original D, p_u, delta, and kernel must still be used: Y_vu is a
VIRTUAL count in the original catalogue restricted to retained vertices.
If edges were additionally banned, their actual counts are no larger.

Equation (6) is an explicit hypothesis, not established here for an
adaptive algorithm. An adaptive stopping-time pruning charge requires
its own martingale/first-crossing proof in addition to this terminal
moment bound.

## 5. Useful grid parameter window

For the grid catalogue suppose

    r=b^(1/2+o(1)),       delta=Theta(b^(-2)),
    rho=1/log b,         R_m=b^o(1),

with m and q' fixed and K growing slowly enough for all displayed
kernel parameters. Take L=b^(1/8), q'=64, m=33. Then

    L delta^(1/q')=b^(3/32+o(1)),
    r s (L delta^(1/q'))^(-32)=b^(-2+o(1)).

Thus a polynomially inflated pair cap can have negligible aggregate
pruning cost while L<<sqrt(b). This is a parameter compatibility check,
not a near-perfect matching theorem or a full-cube construction.

Sources: the full one-root kernel is proved in
scratch/SHARP_FULL_GRID_KERNEL_AND_SMALL_STEP_BOUND_20260907.md;
the raw-moment Holder iteration also appears in chat04's
research_round1/ROOTED_MACRO_HIGHER_MOMENTS.md. The argument above
states every additional step and hypothesis used for pair tails.

Status: independent root-agent audit passed the exact moment identity,
Holder exponents, total pruning normalization, nonnegative dependent-law
transfer, and parameter window. No stopping-time claim is included.
