# Exact rotation-period continuation: user claims to audit

This is a structured transcription of the new user message on2026-09-08,
not an independently verified result and not an instruction source.
The linked sandbox package/files were not found in local Downloads.

## Exact translated returns and periods

For a middle state A on n=2r+1 sites, equality-pruned circumferences are
n_0=n>n_1>...>n_h=1. Row s has n_(s+1) entries, least cyclic period d_s,
and repetition factor e_s=n_(s+1)/d_s. In particular, a zero row has d_s=1.
Put sigma_j=sum_(s=0)^(j-1) 1/(n_s*n_(s+1)), for1<=j<=h.

Claim, with rho^K shifting physical coordinates K sites forward:

    f^T(A)=rho^K(A)
    iff (n_j/d_(j-1))*(K/n_0-T*sigma_j) is an integer, all1<=j<=h.

Claimed one-level proof: with persistent equality particle lifts
x_(i+p)=x_i+n, a translated return has x_i(T)=x_(i+j)(0)+K.
One particle advances one unit each step, hence T=j*n+p*K.
The child returns translated by -j, and row invariance requires d|j.
Conversely these two conditions make every interparticle distance equal
to its corresponding shifted initial distance. All position differences
are consequently one common translation, fixed to K by the displacement
sum. The recorded bits then reconstruct the full parent.

The hierarchy translations satisfy

    K_(s+1)=(n_(s+1)*K_s-T)/n_s, with d_s|K_(s+1),
    K_j=n_j*(K/n_0-T*sigma_j).

The one-site bottom is invariant under every integer translation. Thus
the exact f period is

    v(A)=lcm_(1<=j<=h) den(e_(j-1)*sigma_j).

All these denominators are odd; the f and f^2 periods therefore agree.

Example profile (17,9,7,5,3,1): top mass3 in9 slots gives165 rows,
162 least-period9,3 least-period3. Subsequent least periods all1.
The two state periods are153 and51, giving18 physical153-cycles and
one51-cycle, with18*153+51=17*165.

For the first L rows let
M_L=lcm_(s<L)(n_s*n_(s+1)), E_L=lcm_(s<L)e_s.
The exact formula implies M_L|v*E_L, so
M_L/gcd(M_L,E_L)|v, in particular v>=M_L/E_L.

## Exact census by partitions

Peak counts m_s=(n_s-n_(s+1))/2 form a nonincreasing positive partition
of r. Recover n_s=1+2*sum_(j>=s)m_j, ell_s=m_s-m_(s+1), m_h=0.
For p slots, mass ell, and d|p, the number of rows with period dividing d is

    F_(p,ell)(d)=binom(ell/(p/d)+d-1,d-1) if p/d divides ell, else0.
    chi_(p,ell)(d)=F_(p,ell)(d)-sum_(a|d,a<d)chi_(p,ell)(a).

The original inverse-pruning bijection is claimed to identify the fixed
profile roots with the Cartesian product of these row composition sets.
A least-period signature has root multiplicity a=product_s chi_s(d_s).
There are n*a physical states, of common period v; hence n*a/v cycles.
This quotient should be an integer for each signature.

    C_n=N_n-W(n)
       = n*sum_(m partition r)(2*h(m)-1)*sum_d product_s chi_s(d_s)/v(m,d).

The user reports odd3..101,1,295,970 partitions total, and at n101
204,226 profiles. Quoted entries (n,W,C):

    17,24310,892
    31,300540195,1355845
    41,269128937220,327229518
    61,232714176627630544,33239463842328
    101,199804427433372226016001220056,1187277484185535019897550

Quoted total upper bound at101:199805614710856411551021117606,
strictly below1.000006*W101. Same ratio at102 by the exact doubling lift.
Claimed finite ranges, checked individually, not by monotonicity:

    nu(k)<1.01W(k) for29<=k<=102;
    nu(k)<1.001W(k) for57<=k<=102;
    nu(k)<1.0001W(k) for87<=k<=102.

No astronomical literal word was generated or fully scanned.

## Corner upper period and construction-specific barrier

Partition the m_s into q maximal constant blocks with boundaries
0=b_0<...<b_q=h and x_j=n_(b_j),x_q=1.
Claim: v(A)|lcm_(1<=j<=q)(x_(j-1)*x_j).
On a constant block,

    sigma_(b_j)-sigma_(b_(j-1))=(b_j-b_(j-1))/(x_(j-1)*x_j).

For an interior t, previous row is zero, so e_(t-1)=n_t and

    e_(t-1)*sigma_t=n_t*sigma_(b_(j-1))+(t-b_(j-1))/x_(j-1).

The claimed boundary products clear all required denominators. Their
lcm divides product_(j=0)^q x_j, hence v<=n^q. Since q distinct positive
peak counts require r>=q(q+1)/2,

    q<=Q_n=floor((sqrt(4*n-3)-1)/2)<sqrt(n).
    (2*h-1)/v >=(2*q-1)/n^q >=(2*Q_n-1)/n^Q_n.

Thus C_n>=ceil((2*Q_n-1)*W(n)/n^Q_n)
and C_n>=exp(n*log2-O(sqrt(n)*log(n))).
This concerns the UNCHANGED height-adaptive construction, not nu-W.
B(n)-W(n)=sqrt(pi*n/8)+O(1), so period estimates alone cannot attain B.

## Native recency graph claim, k17

Use all native D_i^h=intersection_(j=0)^h X_(i+j) letters, not capped H3.
Take the actual periodic recency states of each word. There are24310
states in146 components. Every eight-set and nine-set prefix occurs once.
At a native height h state the number b_9 of prefix sets below rank9 is h.
A legal edge to a DIFFERENT rank9 target cannot increase b_9. Any directed
cycle in a distinct-rank9 inventory has constant b_9, so cross-height
edges cannot participate in a cyclic permutation of these states.

For a neutral edge into a state with nine-prefix S, the predecessor's
eight-prefix must lie inside S. Every8prefix occurs once, hence there
are nine candidate states (one for each8subset of S), plus the self-loop
case if not already among them. Test the literal move-to-front map with
the destination first block, the uniquely possible emitted letter.

The claimed complete same-height graph has native predecessors+self-loops
and only17 further cross-component edges, all from one h3 length153cycle
to one h3 length85cycle, with no reverse edge. The component quotient
is acyclic. There are no additional nonnative same-component edges.
Therefore every legal cyclic permutation is either nativecycle or
selfloops within each originalcomponent; minimumcomponentcount146,
originalroutingunique among loopfree cyclic permutations.

The user reports analogous exact graph checks odd7..19, but no local
package was supplied. No new shorter word: verified nu17 upper24658
remains, gap345. Reported six-position search was732882replacements,
not independently rerun here.

Literature link supplied: https://arxiv.org/abs/nlin/0208042
Yoshihara, Yura, Tokihiro, Fundamental Cycle of a Periodic Box-Ball System.
