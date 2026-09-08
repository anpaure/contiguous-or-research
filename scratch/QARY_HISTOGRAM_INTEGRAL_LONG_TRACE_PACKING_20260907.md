# Integral long traces inside q-ary histogram classes

Date: 2026-09-07. Coordinator proof, prompted by chats 02 and 04.

Status: a constructive central-rank packing lemma, not an all-rank q-ary
cover and not a proof of the coefficient-one OR conjecture. No mathematical
computation was run for this note. Chat04 supplied the Boolean
incidence/minimum-degree mechanism; chat02 supplied the histogram-preserving
chain-pair interpretation. The extension below combines those mechanisms.

## 1. A finite induced-degree inequality

Fix q>=2, n>=2, and a histogram h=(h_0,...,h_(q-1)) of nonnegative integers
with sum n. Let Omega_h be the words x in {0,...,q-1}^n with this histogram,
and v=|Omega_h|. Join two words when one is obtained from the other by
swapping a coordinate of value a with a coordinate of value a+1, for some
0<=a<q-1. Put

    D = sum_(a=0)^(q-2) h_a h_(a+1),
    L = sum_(a=0)^(q-2) h_(a+1) = n-h_0.

The graph is simple and D-regular. For U subseteq Omega_h of density
rho=|U|/v, its induced average degree satisfies

    avgdeg(U) >= (D+L)rho-L.                         (1)

Proof. For color a, lower a coordinate of value a+1 to a. These incidence
objects have histogram h+e_a-e_(a+1), hence there are
v*h_(a+1)/(h_a+1) of them when h_(a+1)>0. Each member of U is incident
with h_(a+1) objects. Two different members of U share a color-a object
exactly when they form a color-a edge, and then the object is unique.
Writing d_y for the incidence degree,

    2e_a(U) = sum_y d_y(d_y-1)
            >= (h_a+1)h_(a+1)|U|^2/v-h_(a+1)|U|.

This is Cauchy--Schwarz. When h_(a+1)=0 the corresponding inequality is
zero and needs no division. Summing over a and dividing by |U| proves
(1). The empty U case is omitted. QED.

## 2. Long traces with no coordinate reused

Let 2<=ell<=floor(n/2)+1 and D+L>0. Define

    theta = (4n*ell+L)/(D+L).                       (2)

There is a vertex-disjoint collection of ell-vertex paths in Omega_h
leaving at most min(1,theta)v vertices uncovered, such that along each
path every coordinate is changed at most once.

Proof. Start with U=Omega_h. Whenever |U|>theta*v, (1) gives average
degree greater than 4n*ell. Every finite graph of average degree A has a
nonempty induced subgraph of minimum degree at least A/2: delete vertices
of degree less than A/2, and note that deleting every vertex would account
for fewer than A|U|/2 edges. Thus U contains a subgraph of minimum degree
greater than 2n*ell.

Start at any vertex of this subgraph. After j steps that have not reused
coordinates, exactly 2j coordinates have changed. At the present vertex
each coordinate is incident with at most n graph edges, because it can be
swapped only with a coordinate whose value differs by one. Hence at most
2jn edges touch an already changed coordinate. For j<=ell-2 this is less
than the minimum degree. Choose an edge touching no changed coordinate
and continue. The resulting ell vertices are distinct: after each step
the number of coordinates different from the first vertex increases by
two.

Remove these ell vertices from U and repeat. The finite process terminates,
and its stopping condition gives the claimed uncovered bound. The
algorithm uses only induced-graph deletion and path extension; no
matching theorem or probabilistic existence result is a premise. QED.

The constant in (2) is deliberately loose. It is sufficient for the
asymptotic application; no claim of an optimal leftover fraction is made.

## 3. Every such trace is a literal chain-pair rectangle

Write a selected path as x^0,...,x^(ell-1), and let R=sum_a a*h_a.
Put every coordinate that increases along the path on a left shore P,
and every coordinate that decreases on a right shore Q. No coordinate
was reused, so these assignments are consistent and disjoint. Each shore
has ell-1 assigned coordinates. Because ell-1<=floor(n/2), extend them
arbitrarily to complementary shores of sizes floor(n/2),ceil(n/2).
In particular both shores are nonempty.

Define

    C_i = x^i restricted to P,
    E_j = x^(ell-1-j) restricted to Q,  0<=i,j<ell.

Both C and E are saturated coordinatewise increasing chains: one
coordinate increases by one at every successive step. If the initial
left rank is s_0, then

    rank(C_i)=s_0+i,
    rank(E_j)=R-s_0-(ell-1)+j.

Consequently the rank-R elements of the full product C x E are precisely
the ell points with i+j=ell-1, namely the original trace x^i. The
rectangle has principal cost |C|+|E|=2ell. Products at other ranks are
real targets too, but their distinct coverage is not controlled by this
lemma.

Distinct packed traces have disjoint rank-R supports. Their rectangles
may, and in general must, overlap at other ranks.

## 4. Integral near-complete packing of a largest rank

Fix q and let n tend to infinity. Choose integers ell with ell=o(n) and
ell>=2. Let R be a rank attaining the largest coefficient W_q(n) of
(1+z+...+z^(q-1))^n. Call a histogram typical if every h_a>=n/(2q).
For typical histograms,

    D >= (q-1)n^2/(4q^2),   L<=n,

so (2) is at most C_q(ell+1)/n.

Atypical words are exponentially rare even after restricting to this
largest rank. Here is an elementary bound. For a uniform point of [q]^n,
the count X_a of one value is Bin(n,1/q). Markov's inequality gives

    Pr(X_a<n/(2q))
      <= 2^(n/(2q)) E[2^(-X_a)]
       = 2^(n/(2q))(1-1/(2q))^n
      <= exp(-(1-log 2)n/(2q)).

A union bound handles the q values. Also W_q(n)>=q^n/((q-1)n+1), since
there are (q-1)n+1 ranks. Thus the atypical fraction within rank R is at
most

    q((q-1)n+1) exp(-(1-log 2)n/(2q)) = o(1).        (3)

Apply Section2 separately to every typical rank-R histogram. The resulting
integral family of equal-side rectangles has t rows and covers at least

    (1-O_q((ell+1)/n)-o(1)) W_q(n)                  (4)

distinct rank-R targets, with

    ell*t <= W_q(n),   M=2ell*t<=2W_q(n).           (5)

One may add a singleton-chain rectangle for each remaining rank-R target.
Then the central rank is covered exactly once and the total principal
charge is exactly 2W_q(n). This remains a central-rank cover only.

Taking sqrt(n)<<ell<<n gives long integral rectangles of near-optimal
central charge. For the long rectangles alone their indexed volume is
ell^2*t=(1-o(1))*ell*W_q(n). No claim that this volume consists of distinct
targets is made.

## 5. The remaining research requirement

This removes a central integral-selection bottleneck in the q-ary
histogram mechanism: long literal traces can be packed without fixed
phases and without converting a fractional solution by fiat.

It does not show that the selected full rectangles cover the other ranks.
Even their rank R+1 and R-1 distinct supports are uncontrolled. Coordinate
symmetrization would restore fractional incidence regularity, not an
integral cover at the same cost. A successful continuation must choose,
modify or reassemble the packed traces so that their actual noncentral
targets cover the required ranks, with all added principal charge and
compilation overhead accounted for.

The full OR coefficient remains 1.180703803847...; coefficient one is open.


## 6. Stronger global-rank version: histogram confinement is unnecessary

The following second-round improvement allows a trace to change its value
histogram. Its extraction constants do not depend on q.

Let n be even, q>=2, R=n(q-1)/2 and W=|{x in [q]^n:rank(x)=R}|.
The central coefficient is maximal: convolution preserves symmetric
unimodality, as is seen by expressing a symmetric unimodal sequence as a
nonnegative sum of centered interval indicators and convolving two such
indicators to obtain symmetric trapezoids. Hence the rank R-1 has at most W
points.

On the entire rank-R layer join x to x-e_i+e_j whenever i!=j, x_i>0 and
x_j<q-1. For U in this layer of density rho, let d_U(y) be the number of
its members covering y at rank R-1. Every graph edge has a unique lower
meet, and every x has r(x)=#{i:x_i>0} lower neighbors. Since
rank(x)=n(q-1)/2 and each positive coordinate is at most q-1,

    n/2 <= r(x) <= n.

Therefore, writing N_-=|rank(R-1)|<=W, Cauchy--Schwarz gives

    2e(U)=sum_y d_U(y)(d_U(y)-1)
          >= n^2 |U|^2/(4N_-)-n|U|,

and consequently

    avgdeg(U) >= n^2 rho/4-n.                            (6)

This incidence graph is not restricted to adjacent-value interchanges.
Donor and recipient values may differ arbitrarily, provided the unit
transfer is legal. The value histogram can thus change at every step.

Choose 2<=L with 128L<n. Start from the whole rank and, while
rho>=128L/n, take

    ell=floor(n*rho/64).                                 (7)

A temporary core of half the average degree has minimum degree at least
n^2 rho/8-n/2. Each coordinate is incident with at most2(n-1) unit-transfer
edges. After j fresh-coordinate transfers, at most2j coordinates have
changed, so at most4nj edges touch a previously changed coordinate.
For j<=ell-2,

    n^2 rho/8-n/2-4nj
      >= n^2 rho/8-n/2-4n(ell-2)
      >= n^2 rho/16+15n/2 >0.

The positive-degree core exists because n*rho>=128L. Thus an ell-vertex
trace using every coordinate at most once can be extracted. Its increasing
and decreasing coordinates each number ell-1, so they extend to balanced
nonempty shores, exactly as in Section3. This gives a literal saturated
chain-pair rectangle whose central trace is exactly the chosen path.

Remove only that trace's ell vertices, not the vertices peeled while
finding the temporary core. During each accepted step,

    ell>=n*rho/128>=L,   ell<=n/64,

and the residual size falls by at least the fraction n/(128W). Iteration
therefore gives an integral family with central leave h and row count t
satisfying

    h<128L W/n,
    sum ell_j=W-h,
    M=2(W-h)<=2W,
    t<=1+(128W/n)log(n/(128L)).                           (8)

No histogram typicality or separate orbit summation is needed. The argument
is finite for every even n and every q>=2 satisfying the displayed length
conditions. As before, adding singleton-chain rectangles at the h central
holes makes the central charge exactly2W.

Every long row remains centered at R, so for |s|<L its total indexed
profile is still

    G(s)=W-h-|s|t.                                       (9)

For each fixed q, the rank-drop and tail estimates in chat02's
qary_adaptive_packing.md therefore apply without change. Choosing
sqrt(n log n)<<L<<n^(2/3) gives o(W) scalar band deficit, actual central/tail
coverage at charge(2+o(1))W, and no restriction that long rows stay in one
histogram. Actual noncentral collisions remain the sole unproved coverage
condition. The graph inequality (6) and extraction (8) are uniform in q;
the subsequent band choices and rank-curvature constants here are asserted
only for fixed q.

This is an integral construction, not a fractional averaging step. It
enlarges the available rows for coupled off-diagonal ownership, but it is
not an all-rank cover or an improvement of the OR coefficient by itself.

