# Zero-budget PBBS returns: renewal clusters and small physical packing

2026-09-07. Root derivation. Independent exact-product, renewal,
physical-incidence, packing and two-tail/diagonal audits all PASS.
Pure proof, no computation. All conclusions concern ZERO-BUDGET runs,
not all short PBBS runs.

Later positive-budget extensions are in
PBBS_NEAR_GAUSSIAN_BUDGET_SHARED_REPAIR_20260907.md: together with this
zero-budget theorem, they handle all budgets through an explicit cutoff
of order sqrt(r/log r). Larger budgets remain open.

Main result: the union of repair edges for ALL births with T=height is
o(W), and their actual maximum edge-disjoint packing is o(W/sqrt(r)).
For some H_r with H_r/sqrt(r) tending to infinity and H_r=o(r), the
zero-budget contribution to the O(H_r)-per-cut compiler ledger is o(W).
Positive-budget returns T>height remain uncontrolled.

Fix constants 0<a<b. On the full physical complement-projected PBBS
factor at semilength r, retain precisely births whose normalized root D
satisfies

    T(D)=height(D)=h,   a sqrt(r)<=h<=b sqrt(r).

Here T includes the consuming update. Their complement residences have
h+1 owners and their full repair intervals have h+2 edges. Let W be the
total number of physical edges, W=(2r+1)Cat_r. Let K_e count retained
repair intervals containing edge e, and let nu_0(r;a,b) be the maximum
number of pairwise edge-disjoint retained intervals.

The fixed-band claim proved first, using the accepted exact forest
identities explicitly specified below, is

    #{e:K_e>0}=o(W),
    nu_0(r;a,b)=o(W/sqrt(r)).                         (1)

This coexists with sum_e K_e=Theta(W) and E_edge K_e^2 tending to
infinity. The decisive extra fact is that K_e tends to infinity in
probability under UNIFORM INCIDENCE sampling. Second-moment divergence
by itself would not prove (1).

## 1. Exact multi-time partition from original forest coordinates

Write chi_h(D)=1{T(D)=height(D)=h}, and let tau be the normalized
step-two PBBS map. The original forest bijection supplies terminal
forests with caps ceil(j/2), and suffix forests U_i with universal caps
M_i=h-ceil(i/2), for 0<=i,j<h. Zero budget is exactly height(U_i)<=i.
On chi_h(D)=1, for 3d<=h the exact time-shift equivalence is

    chi_h(tau^dD)=1 iff height(U_i)<=i-d for d<=i<h.  (2)

This uses the ORIGINAL forests of D. It does not sample new forests at
reached roots. The complete derivation and physical phase convention
are in task05's
`research_round1/pbbs_zero_budget_pair_product_and_overlap_divergence.md`.

Take fixed times 0=d_0<d_1<...<d_k with 3d_k<=h, and set
g_j=d_j-d_(j-1). Intersecting the conditions (2) gives, on the index
block d_(j-1)<=i<d_j, the cap i-d_(j-1), together with the universal
cap. These early indices lie below h/3, so their universal caps do not
bind. The terminal block i>=d_k has cap min(i-d_k,M_i).

Let F_0=F_1=1 and F_m=F_(m-1)-xF_(m-2). Forest height cap s has series
C_s=F_s/F_(s+1). The pair partition at d_k has the early factor
product_(i=0)^(d_k-1)C_i=1/F_(d_k). The multi-time event replaces this
by product_(j=1)^k 1/F_(g_j); everything else is unchanged. Consequently

    sum_(D: chi_h(tau^(d_j)D)=1 for j=0..k)
          x^{semilength(D)}
       = x^h/[ (product_(j=1)^k F_(g_j)) F_A F_B F_C ], (3)

where A,B,C are balanced integers with sum 2h+1-d_k. This is a graded
combinatorial identity, not an independence claim at fixed semilength.

The accepted one-point series G_h has three balanced F factors whose
indices sum to 2h+1. Since F_m(1/4)=(m+1)/2^m, the ratio of the critical
values in (3) and G_h tends to

    product_(j=1)^k 1/(g_j+1).                       (4)

The same ratio holds for their x^r coefficients, uniformly when
a<=h/sqrt(r)<=b. Indeed all g_j are FIXED, so their positive geometric
factors add only fixed finite-mean random variables to the auxiliary
critical size law. The three large factors still have indices/h tending
to2/3. The same two-large-mode Fourier bound C/(1+t^2) therefore gives
the same uniform lattice local limit and positive density on the compact
size-ratio interval. Combining that limit with (4) gives

    Pr(chi_h(tau^(d_j)D)=1 for j=1..k | chi_h(D)=1)
       -> product_(j=1)^k 1/(g_j+1).                 (5)

Uniformity is for each FIXED finite collection of times and over the
whole fixed positive Gaussian height band. No growing-time estimate is
claimed or needed.

## 2. The limiting process is a proper recurrent renewal process

Put u_n=1/(n+1), n>=0. Its generating function is

    U(z)=sum_(n>=0)u_n z^n=-log(1-z)/z,  0<=z<1.

Define

    F(z)=1-1/U(z)=1-integral_0^1(1-z)^t dt.

For n>=1 its coefficient is

    f_n=-integral_0^1 (-1)^n binom(t,n) dt >=0,

because binom(t,n) has sign (-1)^(n-1) for 0<t<1. Also f_0=0 and
F(1-)=1 by dominated convergence. Thus (f_n)_(n>=1) is a probability
distribution on positive finite integers.

Take independent interarrival times with this distribution and begin a
renewal at time0. The renewal mass generating function is
1/(1-F(z))=U(z), so the probability of a renewal at time n is u_n.
Regeneration gives the joint probability of renewals at d_1,...,d_k as
product_j u_(g_j), exactly (5). The number R_L of renewals in {0,...,L}
tends to infinity almost surely as L tends to infinity: every finite
number of the almost-surely finite interarrival times has a finite sum.
Their mean need not be finite.

For fixed L, (5) for every subset of {1,...,L}, followed by finite
inclusion-exclusion, proves convergence of the WHOLE binary vector
(chi_h(tau^dD))_(d=0)^L conditional on chi_h(D)=1 to these renewal
indicators. The convergence is uniform over h in the Gaussian band.
In particular, for each fixed integer M,

    lim_(L->infinity) limsup_(r->infinity)
      sup_(h in band) Pr(sum_(d=0)^L chi_h(tau^dD)<=M
                         | chi_h(D)=1) =0.           (6)

## 3. From the birth law to the incidence-biased edge law

Choose uniformly one pair (I,e), where I is a retained physical repair
interval and e one of its h+2 edges. Conditional on h and the birth
root, the offset j of e from the birth edge is uniform on {0,...,h+1}.
The birth root conditional on h is uniform in its exact chi_h class;
the physical deck and the common complement-birth phase change do not
alter (5), since that phase map is bijective and commutes with tau.

Fix L. If j>=L, each retained birth at times d=0,...,L after this birth
has its repair interval containing e: all have the same invariant
height h and hence length h+2, while d<=j<=h+1. Moreover

    Pr_incidence(j<L)<=L/(a sqrt(r)+1)=o(1).

The physical periods are at least 2r+1, so these O(sqrt(r))-length
intervals do not traverse a full period for sufficiently large r.
Consequently K_e is at least the count in (6), except on the stated
vanishing-offset event. Since (6) is uniform in the height, the
height mixture under incidence weighting is harmless. Thus

    K_e -> infinity in probability under uniform incidence. (7)

This is a size-biased statement about existing overlaps, not a reset of
the rooted dynamics and not a conclusion from its second moment.

## 4. Occupied edges and the physical packing bound

Let mu_r=(1/W)sum_e K_e. The audited one-point Gaussian-band local limit
gives mu_r->I_(a,b), with 0<I_(a,b)<infinity. Exact incidence counting
gives

    #{e:K_e>0}/W = mu_r E_incidence[1/K_e].            (8)

On the incidence sample K_e>=1, so 0<1/K_e<=1. Equation (7) implies
E_incidence[1/K_e]->0. Hence the occupied-edge fraction in (8) tends to
zero. Every retained interval has at least a sqrt(r) edges, so any
edge-disjoint subfamily has at most

    #{e:K_e>0}/(a sqrt(r))=o(W/sqrt(r))

members. This proves (1).

The circular-interval transversal theorem gives cuts meeting this
subfamily using at most nu_0 plus one opening per physical cycle. There
are at most Cat_r=W/(2r+1) such cycles, which is o(W/sqrt(r)). Thus this
subfamily can be met by o(W/sqrt(r)) cuts. Charging O(sqrt(r)) per such
cut contributes o(W) to the existing ledger.

## 5. Scope of the fixed-band theorem

So far only the ZERO-BUDGET class T=height in one FIXED POSITIVE Gaussian
band has been treated. Arbitrarily small scaled heights and growing
cutoffs are added separately below; positive-budget lifetimes are not.
A word compiler requiring a transversal for ALL short
residences cannot yet be invoked merely with these cuts. The result
removes the raw-incidence obstruction for this specified subfamily by
proving actual sharing; it does not prove coefficient one.

Sources used: task05's exact original forest product, Gaussian-band
local limit, pair-product/time-shift proof, and physical age/incidence
dictionary, all in worktree c69c/research_round1. Separate root-agent
audits pass the time-shift and multi-time extension, renewal law, and
complete size-bias/packing transfer. Task05 and its two independent
readers also checked the complete argument. One may additionally infer
that owners belonging to the retained positive runs are o(W), by mapping
each affected owner to its immediately preceding repair edge. This is
only the q=0 contribution from this same retained subfamily.

## 6. The ALL-HEIGHT zero-budget family

The previously accepted uniform positive-coefficient bound is

    [x^r]G_h(x) <= C*4^r*(h+1)^(-5)
                  *exp[-(r-h)/(2(h+1)^2)],           (9)

for h>=2 and r>=h, with an absolute C. For r>1 the h=1 zero-budget
class is empty. This bound, with its amplitude retained, is proved in
task05's `pbbs_zero_budget_uniform_bound.md`, Section3; it bounds the
complete true zero-budget class, not just a protected subclass.

For every fixed a>0 and sufficiently large r, all h<=a sqrt(r) lie
below r/2. Dropping constants in (9) gives the summand

    f_r(h+1)=(h+1)^(-5)exp[-r/(4(h+1)^2)].

This is a nonnegative unimodal function of h+1. Its sum up to
a sqrt(r)+1 is bounded by its integral up to that endpoint plus twice
its global maximum O(r^(-5/2)). With x=u sqrt(r), the integral is

    r^(-2) integral_0^(a+1/sqrt(r))
                    u^(-5)exp[-1/(4u^2)] du.

After Catalan normalization this proves

    limsup_(r->infinity) sqrt(r)
      *Pr(T=height<=a sqrt(r)) <= epsilon(a),         (10)

where epsilon(a) tends to zero as a decreases to zero. Finiteness and
this limit follow directly from the exponential at u=0. The low-height
repair incidence, normalized by W, has limsup at most a epsilon(a),
since each such trace has at most a sqrt(r)+2 edges.

For the HIGH-height tail, drop the exponential in (9). If p_(r,h)
denotes the probability of T=height=h, then

    p_(r,h)<=C r^(3/2)(h+1)^(-5).

Summing h>B sqrt(r) gives, with absolute constants,

    limsup sqrt(r)*Pr(T=height>B sqrt(r))<=C B^(-4),
    limsup E[(T+2)1_{T=height>B sqrt(r)}]<=C B^(-3).   (11)

Let nu_all(r) be the maximum edge-disjoint packing of ALL zero-budget
repair intervals, with no height cutoff. Partition any packing into
heights below a sqrt(r), in [a sqrt(r),B sqrt(r)], and above B sqrt(r).
Bound the two tails by their RAW birth counts, and the central part
by (1). For every fixed 0<a<B,

    limsup sqrt(r)*nu_all(r)/W <= epsilon(a)+C B^(-4).

First take r to infinity with a,B fixed; then let a decrease to zero
and B increase to infinity. This proves

    nu_all(r)=o(W/sqrt(r)).                           (12)

For the UNION of occupied edges, bound the two tail supports by their
raw length incidences instead. The same splitting gives

    limsup #{all zero-budget occupied edges}/W
       <=a epsilon(a)+C B^(-3),

so that entire union is o(W) as well. All traces have distinct physical
edges: h+2<=r+2<=2r+1, and each physical cycle has length at least2r+1.

Distinct owners belonging to any zero-budget positive run also number
o(W). If a run starts at edge e_s, its owners are X_(s+1),...,X_(s+h+1)
and its trace contains e_s,...,e_(s+h+1). Map any affected owner X_i to
its preceding edge e_(i-1); this is globally injective into the occupied
edge union. This counts DISTINCT owner states, not owner-coordinate
incidences, which can still have order-W total mass.

## 7. A slowly widening cutoff with negligible zero-budget cut charge

There is a finite, computable choice of the cutoff, not only an
existential diagonal. Enumerate the finite physical factor and its
zero-budget intervals, and determine nu_all(r) by a finite interval
packing algorithm (even exhaustive enumeration suffices). Let c_r be
the largest positive integer c satisfying BOTH integer inequalities

    c^4*r*nu_all(r)^2 <= W^2,       c^8<=r.

Use c_r=1 if this finite set is empty. Put
H_r=isqrt(c_r^2*r)=floor(c_r sqrt(r)), where isqrt is the integer square
root. No efficient complexity bound is asserted for this finite recipe.

With delta_r=sqrt(r)*nu_all(r)/W tending to zero by (12), every fixed
positive integer c is admissible for all sufficiently large r. Hence
the fallback occurs only finitely often and c_r tends to infinity.
The first integer inequality gives c_r^2 delta_r<=1. Consequently

    c_r -> infinity,   H_r/sqrt(r)->infinity,
    H_r<=r^(5/8)=o(r),
    H_r*nu_all(r)/W <=1/c_r ->0.                     (13)

The displayed r^(5/8) is an upper bound on the chosen cutoff, NOT a
claim that setting H_r=r^(5/8) works. Neither monotonicity of c_r nor an
unproved growing-lag estimate is used. The recipe handles nu_all(r)=0
without division by that quantity.

Circular transversals add at most Cat_r openings. Their charge also
vanishes because H_r Cat_r/W=H_r/(2r+1)=o(1). In particular all zero-budget
returns with T+1<=H_r can be met by cuts whose O(H_r)-per-cut ledger
charge is o(W).

This cutoff is wide enough in scale for the accepted negligible far-rank
repair. Nevertheless positive-budget returns T>height must still be
handled before the full PBBS compiler or coefficient-one conclusion can
be invoked. Equation(13) resolves the ZERO-BUDGET contribution to that
packing requirement, not the full requirement.
