# Mixed SCDs: exact fixed-stratum flow rounding and the dynamic integral boundary

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Audited verdict

Let \(A\dot\cup B\) be two \(m\)-sets, let

\[
  h=m-2r>0,
  \qquad
  N_r=\binom mr^2,
\]

and let \({\cal V}_t\) be the rank-\(m\) owners having \(r+t\)
coordinates in \(A\), for \(0\le t\le h\). The complete independently
labelled coordinate orbit of any pair of SCDs contains every monotone
Johnson geodesic

\[
  X_0\longrightarrow X_1\longrightarrow\cdots\longrightarrow X_h,
  \qquad X_t\in{\cal V}_t.                              \tag{0.1}
\]

The following positive statement is exact.

> **Fixed-stratum integral theorem.** The complete path catalogue (0.1)
> contains \(N_r\) pairwise owner-disjoint paths. They use every owner in
> \({\cal V}_0\cup{\cal V}_h\). More generally, every arc-local deletion
> of this catalogue has no fractional-to-integral gap: its maximum path
> packing equals its integral vertex-capacitated max flow.

Thus the bare full orbit needs no nibble at one radius. Prefix/suffix
splicing makes it a single-commodity network, and max-flow integrality is
stronger than an almost-perfect matching theorem.

There are two essential qualifications.

1. The natural number of length-\(h\) paths in a product-SCD resolution is

   \[
      P_h=N_r-N_{r-1},                                  \tag{0.2}
   \]

   not \(N_r\). The fixed-stratum theorem is therefore an overcomplete
   band packing, not a simultaneous all-radius SCD and not a partition of
   the whole middle layer.

2. Queue legality is attached to an incoming history. Safe prefixes for
   one history and safe suffixes for another need not splice. Once this
   state label is retained while all copies of one physical owner share
   capacity one, the problem is a coloured multicommodity packing, not an
   ordinary flow.

The exact direction-transport identity proved below exposes the first
dynamic cut. If an \(N_r\)-path packing misses only \(\ell_0,\ell_h\)
owners at its two endpoint layers, then every \(z\in A\) is inserted

\[
  {h\over m}N_r+O(\ell_0+\ell_h)                       \tag{0.3}
\]

times, and every \(z\in B\) is removed the same number of times. Forbidding
one common coordinate on every path leaves exactly

\[
  {h\over m}N_r                                           \tag{0.4}
\]

endpoint paths uncovered. At \(h=C\sqrt m\) and
\(H=\sqrt m\log\log m\), (0.4) is \(C\log\log m\) times the
fixed-stratum target \(N_r/H\).

This cut can be imposed by individually reachable one-step dynamic states
while every local option fibre remains asymptotically complete. At a high
endpoint choose the inserted label to be \(z\) when \(z\) is present and
any present \(A\)-label otherwise; also choose one removed \(B\)-label.
Every endpoint then has the same one-step queue type and retains the exact
safe fraction

\[
  \left(1-{h\over m-r}\right)^2
  =1-O(m^{-1/2}),                                     \tag{0.5}
\]

and every fixed history type retains the normalized empty-rectangle Hall
inequality. Globally, however, no safe path changes \(z\), so (0.4) is
unavoidable. This is a coefficient-scale fixed-stratum counterexample to
deducing integral grouping from local dynamic Hall. It is not yet a
coherent-predecessor-route counterexample.

Finally, separate endpoint biregularity cannot by itself round a dynamic
filter. A literal \(C_3\)-invariant subcatalogue of a full labelled SCD
orbit has an exact fractional cover and perfect Hall in every separate
rank, but a \(\mathbb Z/3\mathbb Z\) character forbids an integral cover.
A disjoint union of Johnson triangles similarly has perfect fractional
owner incidence but a \((1/4+o(1))W\) blossom leave. These are obstructions
to the proposed *deduction from orbit marginals*. They are not claimed to
be realized by the actual \(O(H)\)-queue filter; the unrestricted full
orbit contains an original integral resolution.

There is also a genuine queue-compatible odd cut. If one common live
support \(Z\) is forbidden, every safe path preserves \(X\cap Z\). On an
infinite subsequence one can make all \(2^{|Z|}\) resulting sectors odd
while every admissible product path has even order. Exact integral
rounding then leaves at least \(2^{|Z|}\) owners although every sector has
a regular fractional perfect matching. This gap is real but cheap:
\(2^{|Z|}=o(W/H)\) for \(|Z|=O(H)=o(m)\).

Consequently the precise surviving theorem is history-state recoupling
with shared physical-owner capacities and all-coordinate transport. No
coefficient-one conclusion follows here.

## 1. The complete geodesic orbit

For \(0\le t\le h\), put

\[
 {\cal V}_t=\left\{S\dot\cup T:
 S\subseteq A,\ |S|=r+t,\ 
 T\subseteq B,\ |T|=m-r-t\right\}.                    \tag{1.1}
\]

An arc from phase \(t\) to phase \(t+1\) has the form

\[
 S\dot\cup T
 \longmapsto
 (S\cup\{a\})\dot\cup(T\setminus\{b\}),
 \quad a\in A\setminus S,\quad b\in T.                \tag{1.2}
\]

A source-to-sink path is uniquely specified by a low owner, an ordered
\(h\)-tuple of distinct insertions from \(A\), and an ordered \(h\)-tuple
of distinct removals from \(B\).

### Lemma 1.1 (orbit completeness)

The independently labelled
\(\mathfrak S_A\times\mathfrak S_B\)-orbit of any pair of SCDs contains
every path (1.2).

#### Proof

Every SCD of \(B_m\) has

\[
  \binom mr-\binom m{r-1}>0
\]

chains of minimum rank \(r\). Such a chain is an ordered partition of its
coordinates into an \(r\)-element bottom, an ordered active word of length
\(h\), and an \(r\)-element outside set. The symmetric group is transitive
on these ordered partitions. Hence the \(A\)-orbit realizes any prescribed
low \(r\)-set and ordered insertion word. Applying the same argument to a
\(B\)-chain and traversing it backwards realizes any prescribed ordered
removal word. Their rank-\(m\) product diagonal is the desired path.
\(\square\)

This proof uses labelled occurrences. Stabilizers may create parallel
occurrences, but every physical path asserted above is literal.

## 2. Exact incidence census

Write \((u)_j=u(u-1)\cdots(u-j+1)\).

### Proposition 2.1 (one-point degrees)

Every \(X\in{\cal V}_t\) lies on exactly

\[
 D_t=\left((r+t)_t(r+h-t)_{h-t}\right)^2             \tag{2.1}
\]

directed paths. Moreover

\[
 |{\cal V}_t|D_t
 =\left({m!\over(r!)^2}\right)^2,                    \tag{2.2}
\]

independently of \(t\).

#### Proof

At \(X\in{\cal V}_t\), the \(t\) already inserted \(A\)-labels form an
ordered \(t\)-tuple among the \(r+t\) present labels, and the \(h-t\)
future insertions form an ordered tuple among the \(r+h-t\) absent labels.
This gives \((r+t)_t(r+h-t)_{h-t}\) choices. The already removed and future
removed \(B\)-labels give the same factor. This proves (2.1). Finally,

\[
 \binom m{r+t}(r+t)_t(r+h-t)_{h-t}={m!\over(r!)^2},
\]

which proves (2.2). \(\square\)

### Proposition 2.2 (two-point codegrees)

Let \(X\in{\cal V}_s\), \(Y\in{\cal V}_t\), \(s<t\), and \(d=t-s\).
Their codegree is zero unless the \(A\)-part of \(X\) is contained in the
\(A\)-part of \(Y\) and the \(B\)-part of \(Y\) is contained in the
\(B\)-part of \(X\). In the compatible case it is

\[
 \lambda_{s,t}
 =\left((r+s)_s\,d!\,(r+h-t)_{h-t}\right)^2.          \tag{2.3}
\]

Consequently

\[
 {\lambda_{s,t}\over D_s}
 ={1\over\binom{r+h-s}{d}^{\,2}},
 \qquad
 {\lambda_{s,t}\over D_t}
 ={1\over\binom{r+t}{d}^{\,2}}.                      \tag{2.4}
\]

In particular every nonzero relative codegree is at most
\((r+1)^{-2}=O(m^{-2})\) in a Gaussian radius stratum.

#### Proof

Compatibility is necessary by monotonicity. The \(d\) forced insertions
and \(d\) forced removals can each be ordered in \(d!\) ways. Before \(X\),
each half contributes \((r+s)_s\) choices; after \(Y\), each half
contributes \((r+h-t)_{h-t}\). This proves (2.3). Dividing by (2.1) and
using

\[
 {d!(r+h-t)_{h-t}\over(r+h-s)_{h-s}}
 ={1\over\binom{r+h-s}d},
 \qquad
 {(r+s)_s d!\over(r+t)_t}
 ={1\over\binom{r+t}d}
\]

proves (2.4). \(\square\)

The codegree scale is favourable. It is nevertheless not the reason
integrality holds: integrality comes from network closure.

## 3. Exact integral rounding by flow

Split every physical owner into an entrance and exit joined by a
capacity-one arc. Give every source, sink, and owner capacity one.

### Theorem 3.1 (fixed-stratum exact path packing)

The resulting layered network has an integral flow of value \(N_r\).
Equivalently, it contains \(N_r\) pairwise owner-disjoint paths from
\({\cal V}_0\) to \({\cal V}_h\).

#### Proof

Put \(v_t=|{\cal V}_t|=\binom m{r+t}^2\) and
\(\theta_t=N_r/v_t\le1\). Every phase-\(t\) vertex has forward degree

\[
 d_t^+=(r+h-t)^2,
\]

and every phase-\((t+1)\) vertex has backward degree

\[
 d_{t+1}^-=(r+t+1)^2.
\]

Send \(\theta_t/d_t^+\) units through every arc from phase \(t\) to
phase \(t+1\). At a phase-\((t+1)\) vertex the incoming load is

\[
 {d_{t+1}^-\theta_t\over d_t^+}
 =\theta_{t+1},                                      \tag{3.1}
\]

because

\[
 {v_{t+1}\over v_t}={d_t^+\over d_{t+1}^-}.
\]

Thus this is a conserved fractional flow, every owner load is at most one,
and the endpoint loads are one. Its value is \(N_r\). The vertex-split
network has integral capacities, so the augmenting-path proof of max-flow
integrality gives an integral flow of the same value. Acyclic flow
decomposition yields the asserted paths. \(\square\)

### Corollary 3.2 (arc-local filters)

After deleting an arbitrary set of network arcs, a fractional flow of
value \(M\) rounds to an owner-disjoint path family of size
\(\lfloor M\rfloor\).

#### Proof

The filtered object remains one vertex-capacitated directed network with
integral capacities. Apply max-flow integrality. \(\square\)

This is the exact group-design rounding theorem available here. It applies
to path restrictions determined locally by a physical arc. It does not
apply when legality depends on the identity of the incoming history and
that identity must survive a shared physical-owner capacity gate.

## 4. Common forbidden coordinates and the sharp quota cut

Let \(F_A\subseteq A\), \(F_B\subseteq B\), with sizes \(f,g\), and retain
only paths that never change a coordinate in \(F_A\cup F_B\). Along such a
path the signatures

\[
 P=X\cap F_A,
 \qquad
 Q=X\cap F_B
\]

are constant. If \(i=|P|\), \(j=|Q|\), the phase-\(t\) population in this
signature is

\[
 v_t(i,j)=
 \binom{m-f}{r+t-i}
 \binom{m-g}{m-r-t-j}.                               \tag{4.1}
\]

### Theorem 4.1 (exact common-forbidden formula)

The maximum number of owner-disjoint length-\(h\) paths avoiding all of
\(F_A\cup F_B\) is

\[
 M(F_A,F_B)=
 \sum_{P\subseteq F_A}\sum_{Q\subseteq F_B}
 \min\{v_0(|P|,|Q|),v_h(|P|,|Q|)\}.                  \tag{4.2}
\]

#### Proof

Every path stays in one signature, so its number there is at most the
smaller endpoint population. This proves the upper bound.

For a fixed signature, \(v_t(i,j)\) is a product of two binomial sequences
and is log-concave, hence its minimum over \(0\le t\le h\) occurs at an
endpoint. Put \(M_{P,Q}=\min(v_0,v_h)\), load every phase-\(t\) vertex by
\(M_{P,Q}/v_t\le1\), and divide this load uniformly among its outgoing
arcs. The exact successive-degree ratio makes the flow conserved, exactly
as in (3.1). Corollary 3.2 rounds it to \(M_{P,Q}\) paths. Distinct
signatures are owner-disjoint, so summing proves (4.2). \(\square\)

For \(F_A=\{z\}\), \(F_B=\varnothing\), (4.2) gives

\[
 M(\{z\},\varnothing)
 =2\binom{m-1}{r-1}\binom mr
 ={2r\over m}N_r
 =\left(1-{h\over m}\right)N_r.                     \tag{4.3}
\]

### Theorem 4.2 (mandatory coordinate transport)

Let an arbitrary owner-disjoint length-\(h\) family miss
\(\ell_0,\ell_h\) owners in \({\cal V}_0,{\cal V}_h\). If \(n_z\) is the
number of its paths that insert \(z\in A\), then

\[
 \left|n_z-{h\over m}N_r\right|
 \le \ell_0+\ell_h.                                  \tag{4.4}
\]

The corresponding removal count for every \(z\in B\) satisfies the same
bound.

#### Proof

An \(A\)-coordinate changes at most once along a monotone path. Therefore

\[
 n_z
 =|\{Y\in{\cal V}_h\setminus L_h:z\in Y\}|
  -|\{X\in{\cal V}_0\setminus L_0:z\in X\}|.
\]

Before deleting the leave sets, these populations are respectively
\((m-r)N_r/m\) and \(rN_r/m\), whose difference is \(hN_r/m\). Removing
\(L_0,L_h\) changes the difference by at most
\(\ell_0+\ell_h\). The \(B\)-statement is identical after reversing the
change. \(\square\)

### Corollary 4.3 (near-complete local Hall can have a global cut)

Assume \(r\ge1\).
Orient every path from its high endpoint to its low endpoint, so its
\(A\)-active alphabet is removed and its \(B\)-active alphabet is inserted.
Fix \(z\in A\). At a high endpoint \(X=S\dot\cup T\), choose

\[
 i_X=
 \begin{cases}
   z,&z\in S,\\
   \text{any element of }S,&z\notin S,
 \end{cases}
 \qquad b_X\in B\setminus T.                           \tag{4.5}
\]

The edge \(X-i_X+b_X\to X\) is a literal one-step predecessor, with
insertion support \(\{i_X\}\) and removal support \(\{b_X\}\). The full
orbit independently realizes every \(h\)-subset of \(S\) as an active
removal alphabet and every \(h\)-subset of \(B\setminus T\) as an active
insertion alphabet. Therefore every endpoint retains the exact fraction

\[
 \left({\binom{m-r-1}h\over\binom{m-r}h}\right)^2
 =\left(1-{h\over m-r}\right)^2,                       \tag{4.6}
\]

and all endpoints have one common queue-size type. The complete typed
history-option block is a product of two biregular disjointness incidences.
Thus every history subfamily, including this prescribed field, satisfies
the normalized empty-rectangle inequality relative to the full typed
shores. This is not ordinary one-to-one Hall after collapsing histories by
physical endpoint.

Nevertheless no allowed path changes \(z\): when \(z\) is present it is
forbidden to be removed, and when absent it cannot be removed on the
high-to-low path. Thus every allowed path lies in one of the two
\(z\)-status fibres and belongs to the common-\(z\) subnetwork. Formula
(4.3) gives the upper bound

\[
 \left(1-{h\over m}\right)N_r.                         \tag{4.7}
\]

At \(h=C\sqrt m\), local survival tends to one, whereas the global deficit
\((h/m)N_r\) is \(C\log\log m\) times \(N_r/H\). Hence local dynamic Hall
does not imply owner-disjoint grouping even at the required additive
scale. The predecessor field (4.5) is not proved to arise simultaneously
from one owner-disjoint coherent preceding atlas. \(\square\)

For a set \(F\subseteq A\), the full endpoint histograms give a stronger
monotone transport condition. A path sends

\[
 j=|X_0\cap F|
 \quad\hbox{to}\quad
 j'=j+|U_A\cap F|\ge j,                               \tag{4.8}
\]

and must couple the exact low and high hypergeometric histograms. Equation
(4.4) is only the first-moment projection of these simultaneous cuts.

## 5. The natural-radius correction

The exact fixed-stratum result must not be substituted directly into the
product-SCD ledger. In a product of two \(m\)-cube SCDs, the number of
paths whose length is exactly \(h=m-2r\) is

\[
 P_h=N_r-N_{r-1}.                                      \tag{5.1}
\]

Indeed \(N_r\) counts pairs of child chains whose minimum ranks are both at
most \(r\), while \(N_{r-1}\) counts those for which both are at most
\(r-1\). At Gaussian radius,

\[
 {P_h\over N_r}
 =1-\left({r\over m-r+1}\right)^2
 ={(h+1)(m+1)\over(m-r+1)^2}
 ={4h\over m}(1+o(1)).                                \tag{5.2}
\]

Furthermore, if \(h=C\sqrt m+O(1)\), Stirling gives

\[
 N_r=\left({2\over\sqrt\pi}e^{-C^2}+o(1)\right)
       {W\over\sqrt m}.                               \tag{5.3}
\]

Thus the exact flow in Theorem 3.1 contains about
\(\sqrt m/(4C)\) times the natural number of radius-\(h\) SCD paths. It
uses \(N_r\) vertices in every phase but does not cover the remaining
\(|{\cal V}_t|-N_r\) interior owners. Flows for different \(r\)'s compete
for those same owners.

The unresolved global problem is therefore a nested, shared-capacity
all-radius flow. The one-radius theorem is a decisive integrality lemma,
but it is not a global atlas by itself.

There is an exact recursive direction invariant. For every SCD of \(B_m\)
and every coordinate \(z\), exactly

\[
 {h\over m}\binom mr                                      \tag{5.4}
\]

of the chains of minimum rank at most \(r\) insert \(z\) between ranks
\(r\) and \(m-r\). Indeed this number is the upper-minus-lower
\(z\)-incidence difference

\[
 \binom{m-1}r-\binom{m-1}{r-1}
 ={h\over m}\binom mr.
\]

Consequently every product-SCD resolution, not only the averaged orbit,
uses each \(A\)-coordinate exactly \((h/m)N_r\) times while its cumulative
length-at-least-\(h\) paths cross the radius-\(r\) slab.

Suppose \(N_{r-1}\) longer paths have already been selected, and let
\(u_z^{\rm long}(r)\) count their uses of \(z\) inside this slab. If the
exact-length-\(h\) child family leaves \(\ell_0,\ell_h\) residual boundary
owners and uses \(z\) exactly \(n_z^{(h)}\) times, then

\[
 \left|
 n_z^{(h)}
 -\left({h\over m}N_r-u_z^{\rm long}(r)\right)
 \right|
 \le\ell_0+\ell_h,                                      \tag{5.5}
\]

while

\[
 \sum_{z\in A}u_z^{\rm long}(r)=hN_{r-1}.              \tag{5.6}
\]

Thus the average residual demand is \(hP_h/m\). Requiring every child
coordinate demand to be within \(o(P_h/H)\) of that symmetric value is
equivalent to the parent-scale dispersion

\[
 u_z^{\rm long}(r)
 ={h\over m}N_{r-1}+o(P_h/H)                           \tag{5.7}
\]

uniformly in every coordinate, with the analogous condition in \(B\).
More generally, the exact requirement is that the child safe-capacity
polytope contain the residual demand vector in (5.5); (5.7) is the precise
condition for a symmetric child library. It is not sufficient:
multicoordinate histogram cuts can remain after all first moments (5.7)
are balanced.

The one-coordinate part has an exact positive rounding theorem. Put
\(k=m-r\), let \({\cal X}={\cal V}_h\), and prescribe
\(I_X\subseteq X\cap A\) so that

\[
 |I_X|=f\quad(X\in{\cal X}),\qquad
 |\{X:z\in I_X\}|={fN_r\over m}\quad(z\in A),          \tag{5.8}
\]

where \(f\le k-h=r\). Then there are safe active alphabets

\[
 U_X\subseteq (X\cap A)\setminus I_X,\qquad |U_X|=h,   \tag{5.9}
\]

such that every \(z\in A\) occurs in exactly

\[
 {hN_r\over m}                                        \tag{5.10}
\]

of them. Indeed, join \(X\) to the eligible coordinates in
\((X\cap A)\setminus I_X\). The resulting bipartite graph has left degree
\(k-f\) and right degree \((k-f)N_r/m\). Weight every edge by
\(h/(k-f)\). This is a fractional \(b\)-matching of left degree \(h\) and
right degree \(hN_r/m\); integral bipartite max flow rounds it exactly.
The same argument applies to \(B\).

Thus an exactly biregular queue design eliminates every one-coordinate
transport cut without a nibble. It does not pair the two chosen half
alphabets to distinct low endpoints, route their internal owners
disjointly, or enforce cross-radius compatibility. Those are precisely
the higher-order grouping gates left after (5.8)--(5.10).

In fact arbitrary queue fields also round exactly at the marginal level.
Let \(I_X\subseteq X\cap A\), put

\[
 a_X=k-|I_X|\ge h,
 \qquad
 L_z=\sum_{\substack{X\in{\cal X}\\z\in(X\cap A)\setminus I_X}}
          {h\over a_X}.                                  \tag{5.11}
\]

Then one can choose safe \(h\)-sets \(U_X\) whose multiplicities \(n_z\)
satisfy simultaneously

\[
 n_z\in\{\lfloor L_z\rfloor,\lceil L_z\rceil\}
 \qquad(z\in A).                                       \tag{5.12}
\]

To prove this, give every eligible incidence at \(X\) weight \(h/a_X\).
Left sums are exactly \(h\), and the right sum at \(z\) is \(L_z\).
Impose left lower and upper capacity \(h\), right lower/upper capacities
\(\lfloor L_z\rfloor,\lceil L_z\rceil\), and unit incidence capacities.
The displayed weights form a fractional feasible flow. Integral
lower-bound max flow gives an integral feasible flow, proving (5.12).

Therefore the complete one-coordinate rounding criterion is

\[
 \max_z\left|L_z-\text{required residual demand at }z\right|
 =o(P_h/H).                                            \tag{5.13}
\]

No nibble is needed after (5.13) is proved. The open work is to derive
(5.13) from coherent chronology and then couple the independently rounded
\(A\)- and \(B\)-alphabets to distinct low endpoints and internally
owner-disjoint paths.

## 6. Why biregular orbit incidence alone cannot finish the dynamic case

The complete unfiltered orbit contains the original SCD and hence has an
integral resolution. Any integral obstruction must be created by the
history-dependent admissibility filter or by coupling all ranks/radii.
Separate normalized Hall statements do not rule this out.

Two exact finite witnesses are recorded in
MATH_OBSTRUCTION_MIXED_SCD_ORBIT_INTEGRAL_GROUPING_AND_ODD_SECTOR_20260726.md.

### 6.1 A joint-rank lattice witness

Inside the full labelled \(S_3\)-orbit of

\[
 \varnothing\subset1\subset12\subset123,
 \qquad 2\subset23,
 \qquad 3\subset13,
\]

retain the three cyclic long chains and both labelled copies of the three
backward short chains. Every Boolean vertex then has degree three, so
weight \(1/3\) on every retained occurrence is an exact fractional SCD.
Every separate-rank owner/option projection has normalized Hall with
equality. Nevertheless the cover equations force

\[
 \ell_1=\ell_2=\ell_3,
 \qquad
 \ell_1+\ell_2+\ell_3=1,                              \tag{6.1}
\]

which has no integral solution. Equivalently, a displayed
\(\mathbb Z/3\mathbb Z\) row character annihilates every retained column
but not the all-one demand vector.

### 6.2 An owner blossom witness

A fixed coordinate triple partitions all middle owners meeting it in one
or two coordinates into disjoint Johnson triangles. Retaining the three
edge options in each triangle gives a \(C_6\) owner/option incidence with
the exact fractional cover \(x_e=1/2\). An integral matching selects at
most one edge per triangle. Its forced leave is

\[
 2\binom{2m-3}{m-1}
 ={m\over2(2m-1)}W
 =\left({1\over4}+o(1)\right)W.                       \tag{6.2}
\]

These witnesses prove that endpoint biregularity plus fractional balance
is not a sufficient hypothesis for a group-design/nibble rounding theorem.
They do **not** prove that an actual queue of size \(O(H)\) cuts the full
orbit down to either witness. In particular, they are a no-go for the
proposed inference, not a coefficient-one obstruction to all mixed SCDs.

### 6.3 The actual safe-orbit parity cut is exact but subcritical

Fix queue supports \(I\subseteq X\), \(R\subseteq X^c\), with sizes
\(f,g\), and retain all length-\(h\) monotone paths whose active
coordinates avoid \(I\cup R\). The resulting sector design has exact
degree

\[
 D=(h+1)(m-f)_h(m-g)_h,                              \tag{6.3}
\]

and two owners at Johnson distance \(d\le h\) have relative codegree

\[
 {2(h-d+1)\over h+1}
 {1\over\binom{m-f}d\binom{m-g}d}.                   \tag{6.4}
\]

Thus, in the Gaussian core,

\[
 {\Delta_2\over D}\le {2\over(m-f)(m-g)},
 \qquad
 (h+1)^2{\Delta_2\over D}=m^{-1+o(1)}.               \tag{6.5}
\]

Moreover, when \(h\le\min(m-f,m-g)-1\), every owner function with values
in an abelian group whose sum is the same on every safe path is constant.
For every modulus \(q\), the left kernel consists exactly of
\(c\mathbf1\) with \((h+1)c=0\). In particular, over \(\mathbb F_2\)
the kernel is zero for even \(h\) and is generated by the all-one sector
vector for odd \(h\). Thus every owner-linear modular obstruction inside
one complete safe sector is only total-sector divisibility.

That parity can genuinely be activated by a common live support. Take

\[
 m=2^t+d,\qquad d\ {\rm odd},\qquad z=|Z|=2d+1.       \tag{6.6}
\]

Then \(2m-z=2^{t+1}-1\). Every binomial coefficient in that row is odd,
so all sectors

\[
 \Omega_Q=\{X:X\cap Z=Q\},\qquad Q\subseteq Z,
\]

have odd size. Since \(m\) and every product-SCD length
\(h\equiv m\pmod2\) are odd, every path contains \(h+1\) owners, an even
number. Any integral safe packing therefore obeys the \(2^z\) independent
cuts

\[
 \sum_{X\in\Omega_Q} e_X\ge1\qquad(Q\subseteq Z),     \tag{6.7}
\]

whereas regular orbit weights fractionally cover every sector exactly.

These states are pointwise chronological: for every endpoint \(X\), a
length-\(z\) geodesic history can insert a \(z\)-set in \(X\) and remove a
\(z\)-set in \(X^c\) whose union contains \(Z\). If \(z+h\le H\), all
labels of \(Z\) remain live throughout the following path. This does not
prove that all such predecessor histories form one owner-disjoint coherent
atlas. Also, the regular fractional point above belongs to the coarser
common-\(Z\) filter. Owner-dependent queue padding can delete additional
options; the parity inequalities persist, but fractional regularity of
that stricter physical family is not asserted.

Finally, for \(z=o(m)\) and \(H,h=\exp(o(m))\),

\[
 h2^z=o(W/H).                                         \tag{6.8}
\]

Thus the actual safe-orbit parity cut refutes exact rounding from
biregularity, but all of its repairs fit inside the permitted
\(o(W/H)\) reserve. Any coefficient-scale no-go must be a simultaneous
cross-history rank or transport cut, not sector parity.

## 7. Precise surviving statement

An adequate dynamic theorem must work with hyperedges

\[
  (\sigma,P),
\]

where \(\sigma\) is an actual incoming queue state, \(P\) is a safe orbit
path, and the edge consumes every physical owner of \(P\). It must select
these edges so that

1. every physical owner is consumed at most once across all state copies;
2. natural radius counts (5.1) are respected;
3. the endpoint Hall loss over all shelves is \(o(W/H)\);
4. every coordinate and every multicoordinate histogram satisfies the
   transport cuts (4.4), (4.8), and the exact residual-demand relation
   (5.5), with (5.7) when a symmetric child library is used; and
5. the joint all-rank column lattice is primitive after the allowed
   \(o(W/H)\) reserve.

If the safe catalogue can first be recoupled into one arc-local network,
Corollary 3.2 gives integrality for free. Without such recoupling, the
problem is a shared-capacity multicommodity path packing, and the
\(C_3/C_6\) witnesses show exactly which additional integral cuts a proof
must exclude.

This is the proved boundary: the bare fixed-radius full orbit rounds
exactly; fractional dynamic empty-rectangle expansion alone does not; the
missing gate is history-state recoupling simultaneously across the natural
radius ledger. No constant-one claim is made.
