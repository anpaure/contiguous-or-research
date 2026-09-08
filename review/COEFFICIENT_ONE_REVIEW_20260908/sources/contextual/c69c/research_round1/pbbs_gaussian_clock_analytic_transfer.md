# Gaussian PBBS lifetime vanishing from the original clock triangle

Date: 2026-09-07. Pure proof; no computation or original-project edits.
Local review record: an independent recency-gate full audit passed the
profile law, all counting formulas, conditioning, spectral constant, and
order of limits, with no corrections. The coordinator's separate
structural and analytic audits both passed, and the theorem was accepted
on 2026-09-07.

This is the separate analytic transfer for
pbbs_gaussian_clock_genealogy_structural_audit.md. The structural proof
has passed both the local independent audit and the coordinator's
separate review.
No distribution is reset at a reached root. All independent variables
below are coordinates in the exact ORIGINAL inverse-pruning bijection.

The accepted conclusion is

    P_(uniform Dyck_r)(T(D)<=c sqrt(r)) -> 0
                    for every fixed c>0.                (1)

Here T includes the consuming update. This is a raw lifetime count;
it does not by itself establish a sharper packing or coefficient-one
statement. The argument supplies no rate uniform in a growing c.

## 1. Structural input, with every conditioning specified

Put D_s=partial^s D, r_s=|D_s|_up and h=ht(D). At each nonempty-core
level s, the original inverse-pruning vector Z_s is a uniform weak
composition of

    ell_s=r_s-2r_(s+1)+r_(s+2)

into

    p_s=2r_(s+1)+1

parts. Conditional on the ENTIRE feasible pruning profile, these vectors
are independent. This is the finite Cartesian-fibre bijection in the
structural note, not a conditional independence assertion about dynamics.
Particle labels are persistent, and label zero is fixed at the original
root at every level.

The proved clock implication is as follows. For any integer L with h>L,
if the physical horizon G=2T+1 is below every queried circumference, then

    sum_(s=0)^(L-1) sum_(j=0)^s Z_(s,-j)
      <= ( G/[2(h-L)+1]-1 )/2,                         (2)

provided p_s>G at every s<L. Indices in each row are reduced modulo p_s;
under the displayed condition they are distinct. Height h-L at the
reached depth-L phases follows from invariance of the whole pruning
profile, as now made explicit before (8) in the structural note.

Fix a,c>0 and set K=ceil(c/a)+1. For every FIXED L, on

    h>=a sqrt(r),       T<=c sqrt(r),                   (3)

the right side of (2) is at most K for sufficiently large r. The required
size and circumference conditions hold with probability tending to one
by the fixed-depth profile law proved next.

## 2. Elementary fixed-depth Catalan pruning law

We prove, jointly for every fixed finite list of depths,

    r_s/r -> 1/(s+1) in probability.                   (4)

Regard a uniform Dyck word of semilength r as a uniform plane tree with
n=r+1 vertices. List its offspring numbers in preorder. The resulting
sequence of n nonnegative integers has sum n-1 and satisfies the usual
prefix condition. Conversely this condition reconstructs the tree.

Start instead with a uniform weak composition (X_1,...,X_n) of n-1 into
n parts. The cycle lemma says exactly one of its n cyclic shifts has the
preorder prefix condition. There is no nontrivial periodicity, since a
period repeated d>1 times would require d to divide both n and n-1.
Taking the unique valid shift therefore gives the uniform plane tree.
Any statistic defined by counting cyclic windows is unchanged by that
shift.

Fix a finite plane tree A with k vertices, with offspring sequence
(a_1,...,a_k), whose sum is k-1. At any prescribed cyclic position, the
probability that the next k entries equal this sequence is

    binom(2n-2k-1,n-k-1) / binom(2n-2,n-1)
      -> 2^(-(2k-1))=:mu(A).                           (5)

This is direct stars and bars on the remaining n-k entries. The formula
is used for n>k, which suffices for the limit. For two disjoint windows
of fixed tree sequences A,B with total length m, the same calculation is

    binom(2n-2m,n-m-1) / binom(2n-2,n-1)
      -> 2^(-(2m-2))=mu(A)mu(B).                       (6)

There are only O(n) overlapping pairs of fixed-length windows, compared
with n^2 pairs in total. Equations (5)-(6) imply that the normalized
number of occurrences of each fixed sequence converges to mu(A) in L^2.
A non-wrapping occurrence of a tree's complete preorder sequence is
exactly a fringe subtree: its prefix sums specify the first completion
of that descendant block. Cyclic windows crossing the end contribute at
most k-1 discrepancies. Thus the same limit holds for fringe counts,
jointly for any finite collection of finite trees.

The numbers mu(A) form the fringe law of a critical Galton-Watson tree
with offspring probabilities P(X=d)=2^(-(d+1)). Indeed their product
over the k vertices is 2^(-(2k-1)). Extinction has probability one:
the offspring generating function is 1/(2-t), and its smallest fixed
point in [0,1] is one. Hence sum_A mu(A)=1.

This last fact permits bounded fringe statistics without a finite-size
restriction. For every M there are finitely many trees of size at most M,
and their total empirical proportion converges to their total mu-mass.
The remaining empirical proportion tends to at most the complementary
mass, which decreases to zero as M increases. Truncating any bounded
fringe statistic at size M, taking n to infinity, then M to infinity
therefore proves its law of large numbers. No growing-window estimate
or unproved concentration theorem is needed.

After s rounds of leaf pruning, a non-root vertex survives exactly when
its ORIGINAL fringe tree has height at least s. The root contributes at
most one discrepancy if all vertices are counted. Under the fringe law,
the probability of height at most s-1 is

    (1/2) C_(s-1)(1/4)=s/(s+1),       s>=1,

where C_j is the bounded-height Catalan series and
C_j(1/4)=2(j+1)/(j+2). Thus the survival probability is 1/(s+1);
for s=0 it is one. Applying the bounded-fringe law of large numbers gives
(4), including joint convergence at any fixed number of depths.

## 3. The original triangular coordinates have harmonic cost

For each fixed s, (4) gives

    ell_s/r -> 2/[(s+1)(s+2)(s+3)],
    p_s/r   -> 2/(s+2),
    ell_s/(ell_s+p_s) -> q_s=1/(s+2)^2.               (7)

For a uniform composition of ell into p parts, fixing k distinct
coordinates to values with total A leaves exactly

    binom(ell-A+p-k-1,p-k-1)

compositions, out of binom(ell+p-1,p-1). If ell,p tend to infinity with
ell/(ell+p)->q in (0,1), this ratio tends to

    (1-q)^k q^A.                                      (8)

Thus any fixed finite set of coordinates converges jointly to independent
geometric variables with P(Z=b)=(1-q)q^b, b>=0. The limiting probabilities
sum to one, so there is no missing mass at large coordinate values.

For a fixed L the triangular set in (2) is finite. Conditional on the
entire profile, apply (8) separately in each row, and use the exact
independence of the original row vectors. Since all row ratios converge
in probability to the deterministic values in (7), averaging over the
profile gives the same finite product limit UNCONDITIONALLY. In particular
we do not condition this limit further on (3).

Let S_(r,L) be the sum of the triangular coordinates, defined as zero
on the exceptional profiles with fewer than L+1 nonempty levels. Those
profiles have probability tending to zero by (4). Its limiting variables
have row-s positive probability q_s and occur s+1 times. For any fixed K,

    limsup_(r->infinity) P(S_(r,L)<=K)
      <= exp{K - (1-e^(-1)) A_L},
    A_L=sum_(s=0)^(L-1) (s+1)/(s+2)^2.                (9)

Indeed 1{S<=K}<=exp(K-S), and for every nonnegative integer variable Z,
E exp(-Z)<=1-(1-e^(-1))P(Z>0). Apply this to the finite independent
geometric limit and use 1-x<=exp(-x).

The sum A_L diverges logarithmically. For each fixed L, the regular
profiles in (4) have all p_s of order r, so p_s>2c sqrt(r)+1 and the
clock no-wrap assumptions hold for large r. Combining (2)-(3) with (9)
and then letting L tend to infinity proves

    P(h>=a sqrt(r), T<=c sqrt(r)) -> 0
                           for every fixed a,c>0.      (10)

The order of limits is essential: first fix a,c,L; next let r grow; then
let L grow. No assertion about L=L(r) is used.

## 4. Removing the low-height tail

For completeness, a direct spectral estimate supplies the required
small-height bound. Let m>=1. The adjacency matrix of the path with
vertices 0,...,m gives

    #{D in Dyck_r: ht(D)<=m}
      =2/(m+2) sum_(j=1)^(m+1) sin^2(theta_j)
                         [2 cos(theta_j)]^(2r),
    theta_j=pi*j/(m+2).                               (11)

Pair the modes at opposite ends of the spectrum. On 0<=theta<=pi/2,
sin(theta)<=theta and cos(theta)<=exp(-theta^2/2). Therefore

    #{ht(D)<=m}
      <= 4 pi^2 4^r/(m+2)^3
          sum_(j>=1) j^2 exp[-pi^2 r j^2/(m+2)^2].     (12)

Using Cat_r~4^r/(sqrt(pi) r^(3/2)) and m=floor(a sqrt(r)) yields

    limsup P(ht(D)<=a sqrt(r))
      <= 4 pi^(5/2) a^(-3)
           sum_(j>=1) j^2 exp[-pi^2 j^2/a^2].          (13)

The right side tends to zero as a decreases to zero. Combining (10)
and (13), and taking a down to zero AFTER the preceding limits, proves
(1). This completes the analytic passage from the original triangular
slot constraint to the actual full Gaussian lifetime event.

## 5. Audit and scope

The proof uses four exact inputs: the original profile-conditioned
Cartesian fibres, the clock triangle inequality, the fixed-depth Catalan
fringe law proved here, and the path spectral formula. Reached phases
enter only in deriving the deterministic clock partition. None are
sampled from a new birth law.

The separate coordinator audits have accepted this result. This note
does not assert a quantitative tail rate,
uniformity for growing c, a short-interval packing theorem, or a change
to the independent unconditional upper-bound coefficient.
