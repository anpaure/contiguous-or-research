# Canonical predecessor boundaries have a tight Gaussian-window count

2026-09-08. Pure proof; no computation. Root full-file proof review and
independent cover-selectors full audit passed. The theorem concerns successive C clocks of the original D_1
started at time zero. It does not concern every physical phase, nor the
exposed feasibility count J.

## 1. Setting and exact finite-depth clock expansion

Use the actual base-c incidence law and notation of
`PBBS_TWO_ROW_VIRTUAL_ZERO_CLOCK_REDUCTION_20260908.md`. Fix c>0 and
C>=c, let R=sqrt(r), H_c=floor(cR), H_C=floor(CR), and G_C=2H_C+1.
The base has top gap zero and actual physical endpoint at most 2H_c+1.
At every fixed depth S, its safe original zero triangle has incidence
probability 1-o(1). Conditional on the entire profile, original rows
s>=S and the sampled offset, rows s<S are independent uniform
compositions with their original slots 0,-1,...,-s forced zero. Their
free finite-query limit has independent geometric values of ratio

    q_s=1/(s+2)^2.

These are the accepted exact fibre and finite adaptive query theorem.
The environment always retains its actual incidence law.

At level u, consider an endpoint-started chronological word with a C
nodes and b T nodes. Let z_1,...,z_(a+b) be its chronological incoming
gap queries. The exact one-level partition is

    C -> C T^(2z),       T -> C T^(2z+1).

Every parent node contains one child C; its completion therefore
decrements the next-level original selected label by one. If the word
begins at original phase zero, its row-u queries are exactly the
original prefix 0,-1,...,-(a+b-1). Child endpoint maps C and T commute
by the accepted adjacent-selection alternation argument. Consequently
the expanded endpoint is that of

    C^(a+b) T^(b+2 sum z_i).                         (1)

The count identity is valid for any chronological ordering of the
parent nodes. It does not replace the actual leaf trajectory by
independent clocks. Endpoint commutation preserves its endpoint, and
the displayed original query prefix comes from the chronological
partition before commuting.

For a word expanded through rows u,...,S-1, write a_s,b_s for its C
and T counts at level s, n_s=a_s+b_s, and

    W_s=sum_(i=0)^(n_s-1) Z_(s,-i).

Then the exact count recursion is

    a_(s+1)=a_s+b_s,
    b_(s+1)=b_s+2W_s.                               (2)

For cutoff use, (1)-(2) are invoked physically only inside a horizon
G_C satisfying G_C+1<min_(u<=s<S) p_s. An actual word finishing by
G_C has exactly this expansion. Conversely a candidate expansion
finishing by G_C can be grouped back into the parent word; all groups
are inside the safe horizon. These are the accepted forward/reverse
no-wrap implications. The recursion can also be run as a formal
original-prefix query algorithm after a candidate has become too long;
no physical identity is then asserted for its unrestricted endpoint.

## 2. The finite zero corridor for C_1^k

Let tau_k be the physical endpoint of k consecutive C_1 clocks from
time zero, with tau_0=0. These times increase strictly and are even.
Fix the positive integer k before taking any limit. Start (2) at

    a_1=k,       b_1=0.

Define the original-coordinate event

    A_k={Z_(s,-i)=0 for 1<=s<=k-2,
                         s+1<=i<=k-1}.             (3)

An empty condition is true. Thus A_1=A_2 is the sure event on the safe
base fibre. These are precisely the free entries needed to make the
first k coordinates zero at every row s>=1: for s>=k-1 the base
triangle already forces all k coordinates zero. Consequently, for
S>=k, the formal recursion has b_S=0 if and only if A_k holds.
On A_k it consists of C_S^k, with no T nodes.

The original base top return, on its depth-S zero triangle, expands
to C_S^S T_S. Its first k C endpoints are therefore inside the actual
base return when k<=S. If A_k holds, reverse grouping of the first k
of those C_S clocks gives exactly C_1^k. Hence, on the safe event,

    A_k => tau_k<=2H_c+1<=G_C.                     (4)

This is a physical endpoint assertion. It does not use an arbitrary
reached-root distribution or a raw shifted original cone.

## 3. A T seed grows without bound in the infinite-row oracle

For this section only, construct independent original geometric rows,
with ratio q_s and the first s+1 slots forced zero, on infinite labels.
Run (2) with a_1=k,b_1=0 using the same chronological prefixes. Each
finite depth is well defined: each queried value and each resulting
finite prefix length is finite almost surely. The next prefix length
is measurable before its row is read.

On A_k^c, some W_s is positive, so b subsequently is an even integer
at least two. We claim

    b_S -> infinity almost surely on A_k^c.        (5)

The sequence b_s is nondecreasing. If it were bounded after a seed,
it would eventually be a constant B>=2, since it is integer valued.
Thus for some N all later W_s would vanish and

    n_s=n_N+B(s-N),       s>=N.

The number of free coordinates queried in row s would be

    e_s=max(n_s-(s+1),0)=(B-1)s+O(1).

Conditional on the countable finite history through row N-1, the
probability that all these later sums vanish is

    product_(s>=N) (1-q_s)^(e_s)=0,                (6)

because sum e_s q_s diverges and log(1-q_s)<=-q_s. This argument is
applied separately to each possible N,B,n_N and finite history; their
countable union still has probability zero. It proves (5).

In particular, for every fixed integer M,

    lim_(S->infinity) Pr_oracle(A_k^c,b_S<=M)=0.    (7)

The threshold two is material: the forced triangle grows by one slot
per row. A seed from an all-C word creates at least two T nodes, so
its expanding queried prefix eventually extends linearly beyond that
triangle. Equation (5) is not a general statement about every initial
word with one T node.

## 4. Transfer to actual Gaussian-time C boundaries

Fix epsilon>0, k, and S>=k, and then send r to infinity. All relevant
circumferences exceed G_C+1 with incidence probability 1-o(1). If
tau_k<=G_C, its depth-S T intervals are disjoint within that horizon.
Every reached depth-S root has height h-S. Therefore

    b_S [2(h-S)+1] <= G_C.                          (8)

On h>=epsilon R and sufficiently large r, (8) implies b_S<=M for a
fixed integer M>2C/epsilon.

The event {A_k^c,b_S<=M} is an event of a bounded legal query algorithm
for fixed k,S,M: stop the recursion as soon as b exceeds M. Before
this stop, a_s<=k+(s-1)M and n_s<=k+sM. Query individual original
prefix entries and stop within a row when its partial sum already
forces b_(s+1)>M. Thus there is a deterministic finite query bound
depending only on k,S,M; no aggregate or trajectory oracle is used.
The accepted finite adaptive freshness theorem transfers its law to
the oracle in Section 3 while preserving the actual environment law.

It follows that

    limsup_(r->infinity)
      Pr_inc,c(tau_k<=G_C,A_k^c,h>=epsilon R)
       <= Pr_oracle(A_k^c,b_S<=M).                  (9)

First let S tend to infinity, using (7). Then let epsilon decrease
to zero. The accepted actual-incidence small-height limsup, derived
in Section 6 of the J note, is at most
C_c exp(-b_c/epsilon^2). Therefore

    Pr_inc,c(tau_k<=G_C,A_k^c) -> 0.                (10)

Together with (4), this proves the stronger event comparison

    Pr_inc,c({tau_k<=G_C} symmetric-difference A_k)
                               ->0.               (11)

Only fixed-depth limits were used: epsilon,k,S and the query cap are
fixed before r tends to infinity; S then tends to infinity; epsilon
is removed last. There is no fresh law at a dynamically reached root.

## 5. Explicit tight boundary-count law

The finite-coordinate fibre limit applied to (3) gives

    p_k:=lim_(r->infinity) Pr_inc,c(A_k)
       =product_(s=1)^(k-2) (1-q_s)^(k-s-1).

For k>=2, p_2=1 and

    p_(k+1)/p_k
       =product_(s=1)^(k-1) [(s+1)(s+3)/(s+2)^2]
       =2(k+2)/[3(k+1)].

The last product telescopes by separating its two linear factors.
Hence

    p_1=p_2=1,
    p_k=(k+1)/3 * (2/3)^(k-2),       k>=2.          (12)

Let B_(r,C)=#{k>=1:tau_k<=G_C}. Strict positivity of clock lengths
makes this finite for every r, and {B_(r,C)>=k}={tau_k<=G_C}.
Equations (11)-(12) show convergence in distribution to a finite
integer B with

    Pr(B>=k)=p_k,
    Pr(B=2+m)=(m+1)/9 * (2/3)^m,     m>=0.          (13)

The masses in (13) sum to one, for example by differentiating the
geometric-series identity. In particular B_(r,C) is asymptotically
tight, for every fixed C>=c. No claim about convergence of its means
is needed. The limit is the same for every such fixed C.

For a concrete positive-probability obstruction, A_3 is just
{Z_(1,-2)=0}. Thus

    lim_(r->infinity) Pr_inc,c(tau_3>G_C)=1/9.       (14)

On its complement the third canonical boundary lies inside the base
clock; on the limiting positive-gap event it exceeds every fixed
Gaussian cutoff in the sense of (10), separately for each fixed C.

## 6. Consequence and exact scope

Increasing the number of consecutive original D_1 predecessor clocks
cannot supply a diverging number of physical candidate phases in a
fixed Gaussian window. Their available number has the explicit tight
law (13), even when the window is enlarged by an arbitrary fixed
factor. This closes that particular canonical-endpoint construction.

The common deep C_S boundaries of the base C_S^S T_S word are different
objects. They need not be endpoints of successive upper-level C_1
clocks: lower gaps can move the physical labels, as the accepted
fixed-gap misalignment example already shows. The theorem neither
bounds their number nor determines which of their virtual intervals
are short and overlap the sampled edge. It does not imply tightness
of J, failure of occupied-support decay, or failure of coefficient one.
Abundance among those other actual physical phases remains open.
