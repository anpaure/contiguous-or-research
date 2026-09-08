# Dong--Mao fixed-core diamond banks and the exact two-bank fusion gate

Date: 2026-08-02  
Status: primary-source audit; unconditional five-coordinate-fibre bank
occupying asymptotically three quarters of the central packing capacity;
exact two-bank equivalence; the central maximum-bank and correlated two-bank
existence statements are explicitly **UNPROVED**

## 0. Verdict

Dong and Mao prove that the consecutive-rank interval poset

\[
 {\cal P}_{n;\ell,\ell+r}
 =\{X\subseteq[n]:\ell\le |X|\le\ell+r\}
\]

has \(\binom n\ell\) pairwise vertex-disjoint maximal intervals whenever

\[
                    n\ge (\ell+1)r+\ell .             \tag{0.1}
\]

For \(r=2\), every interval is one Boolean diamond.  Their critical-case
construction is the cycle-lemma construction in Section 2; Section 3 extends
it recursively to every parameter satisfying (0.1).

This does **not** settle the central Catalan three-level instance

\[
              (n,\ell,r)=(2m,m-1,2),\qquad m\ge2,      \tag{0.2}
\]

because (0.1) would read \(2m\ge3m-1\).  In fact (0.2) lies strictly in
the central range left open in their Problem 4.2.  Thus the paper must not be
cited for a full central diamond bank.

It nevertheless gives an unconditional **large partial central bank**.
Stratifying by all patterns on a fixed \((2m-5)\)-coordinate core and
applying the critical five-coordinate construction fibrewise gives a bank
whose size is asymptotically three quarters of the elementary central
packing upper bound.  More importantly, two correlated vertex-disjoint
diamond banks give an exact normal form for the ordered four-transversal:
the only cross-bank topological condition is that their middle-overlap graph
be a forest.

Primary source: Yuxian Dong and Jianxi Mao,
[*Engel's Interval Packing Problem in the Boolean Lattice*](https://arxiv.org/abs/2607.04794),
arXiv:2607.04794v1, Theorem 1.2, Proposition 2.5, and Problem 4.2.

## 1. What the source proves, and what it leaves open

Let \(\nu_{n;\ell,u}\) be the maximum number of pairwise disjoint maximal
intervals in \({\cal P}_{n;\ell,u}\).  Dong--Mao Theorem 1.2 states

\[
 n\ge(\ell+1)r+\ell
 \quad\Longrightarrow\quad
 \nu_{n;\ell,\ell+r}=\binom n\ell .                  \tag{1.1}
\]

For \(r=2\), a maximal interval

\[
 [A,A\cup\{a,b\}]
 =\{A,A+a,A+b,A+a+b\}                                \tag{1.2}
\]

is a Boolean diamond.  Pairwise disjointness of the intervals means
vertex-disjointness at all three ranks, not merely distinct lower and upper
endpoints.

At the critical value \(n=3\ell+2\), Section 2 assigns weights \(-2\) on
\(A\) and \(+1\) off \(A\).  If \(M\) is the maximum partial-sum height,
the cycle lemma identifies the two extension positions as the first
occurrences of heights \(M-1\) and \(M\).  Proposition 2.5 proves that the
resulting diamonds are pairwise disjoint.  The induction in Section 3
treats \(n>3\ell+2\).

For the central instance (0.2), Dong--Mao Problem 4.2 asks whether

\[
 \nu_{2m;m-1,m+1}
 =\min\left\{
     \binom{2m}{m-1},
     \left\lfloor\frac12\binom{2m}{m}\right\rfloor,
     \binom{2m}{m+1}
   \right\}
 =\left\lfloor\frac12\binom{2m}{m}\right\rfloor .   \tag{1.3}
\]

Indeed, for \(m\ge2\),

\[
 {3(m-1)+4\over2}<2m<3(m-1)+2,                       \tag{1.4}
\]

so this is strictly inside their unresolved central range.  Equation (1.3)
is **UNPROVED**.

## 2. An unconditional fixed-core central bank

Put

\[
 q=\left\lfloor {m\over2}\right\rfloor,\qquad
 \ell'=m-1-q,\qquad n'=2m-q .                         \tag{2.1}
\]

Fix \(R\subseteq[2m]\) with \(|R|=q\), and write
\(\Omega'=[2m]\setminus R\).  Directly,

\[
                         n'\ge3\ell'+2.               \tag{2.2}
\]

For \(m=2s+1\), equality holds:
\((q,\ell',n')=(s,s,3s+2)\).  For \(m=2s\),
\((q,\ell',n')=(s,s-1,3s)\), one above the critical value.

### Theorem 2.1 (fixed-core Dong--Mao bank)

There is a family \({\cal D}_R\) of

\[
 b_m=\binom{2m-\lfloor m/2\rfloor}
              {m-1-\lfloor m/2\rfloor}               \tag{2.3}
\]

pairwise vertex-disjoint Boolean diamonds in the three central ranks of
\({\cal B}_{2m}\).  Their lower endpoints are exactly

\[
       \{L\in\tbinom{[2m]}{m-1}:R\subseteq L\}.       \tag{2.4}
\]

#### Proof

Apply (1.1) with \((n,\ell,r)=(n',\ell',2)\) on
\(\Omega'\).  It gives one pairwise disjoint interval
\([A,B_A]\), \(|B_A\setminus A|=2\), for every
\(A\in\binom{\Omega'}{\ell'}\).  Send it to

\[
                         [R\cup A,R\cup B_A].          \tag{2.5}
\]

The three ranks in (2.5) are \(m-1,m,m+1\).  If two lifted intervals met,
deleting \(R\) would give a vertex in the intersection of the two original
intervals, impossible.  The number of choices of \(A\) is (2.3), and their
lower endpoints are precisely (2.4).  \(\square\)

Taking complements gives an equally large upper-anchored bank whose upper
endpoints are all rank-\((m+1)\) sets avoiding \(R\).

For reference,

\[
 b_m=\begin{cases}
       \binom{3s}{s-1},&m=2s,\\[2mm]
       \binom{3s+2}{s},&m=2s+1,
     \end{cases}                                      \tag{2.6}
\]

and Stirling's formula gives

\[
 b_m=\Theta\!\left({(3\sqrt3/2)^m\over\sqrt m}\right).
                                                               \tag{2.7}
\]

This is exponentially large but an exponentially small fraction of
\(N=\binom{2m}{m-1}\):

\[
                       {b_m\over N}
 =\Theta\!\left((3\sqrt3/8)^m\right).                \tag{2.8}
\]

In particular, two banks of the fixed-core size cannot by themselves cover
all \(N\) lower colours.  In fact \(2b_m<N\) for every \(m\ge2\).  For
\(m=2s\), already

\[
 \binom{3s}{2s-1}
   ={2(2s+1)\over s+1}\binom{3s}{s-1}
   >2b_m,
\]

and \(N\ge\binom{3s}{2s-1}\).  For \(m=2s+1\),

\[
 \binom{3s+2}{2s}
   ={2(2s+1)\over s+2}\binom{3s+2}{s};               \tag{2.9}
\]

the ratio is at least two when \(s\ge1\), and the strict enlargement from
\(3s+2\) to \(4s+2\) ground points gives \(N>2b_m\).

Thus Theorem 2.1 is a genuine partial absorber, not a two-bank completion of
the Catalan matching.

### Theorem 2.2 (five-coordinate stratified bank)

For every \(m\ge3\), the three central ranks of \({\cal B}_{2m}\) contain a
pairwise vertex-disjoint diamond bank of size

\[
 D_m
 =2\binom{2m-5}{m-1}+10\binom{2m-5}{m-2}.            \tag{2.10}
\]

Relative to the elementary middle-rank packing capacity, its exact density
is

\[
 {D_m\over \frac12\binom{2m}{m}}
 ={m(3m-4)\over(2m-1)(2m-3)}
 \longrightarrow {3\over4}.                         \tag{2.11}
\]

At \(m=3\), (2.10) has size \(10\) and attains the full capacity
\(\frac12\binom63=10\).

#### Proof

Split

\[
 [2m]=H\mathbin{\dot\cup}K,\qquad |H|=2m-5,\quad |K|=5.  \tag{2.12}
\]

For every \(P\subseteq H\), work inside the Boolean fibre

\[
                     {\cal F}_P=\{P\cup A:A\subseteq K\}. \tag{2.13}
\]

Different fibres are vertex-disjoint.  Put
\(j=m-1-|P|\).  A central diamond which stays in \({\cal F}_P\) is an
interval across levels \(j,j+1,j+2\) of \({\cal B}_5\), so only
\(j=0,1,2,3\) can occur.

For \(j=0\), take the trivial one-diamond interval packing of
\({\cal P}_{5;0,2}\).  For \(j=1\), apply Dong--Mao at its critical
parameter

\[
                       (n,\ell,r)=(5,1,2)             \tag{2.14}
\]

to obtain five pairwise disjoint diamonds.  Complementing these two
packings inside \(K\) gives respectively one packing at \(j=3\) and a
five-diamond packing at \(j=2\).  Lift the relevant packing by adjoining
the fixed pattern \(P\).  Thus the four fibre counts, in order
\(j=0,1,2,3\), are

\[
                              (1,5,5,1).              \tag{2.15}
\]

There is also a direct audit of the only nontrivial local packing.  Identify
\(K\) with \(\mathbb Z_5\) and take

\[
       [\,\{i\},\{i,i+1,i+2\}\,]\qquad(i\in\mathbb Z_5). \tag{2.15a}
\]

The ten middle vertices are the pairs
\(\{i,i+1\},\{i,i+2\}\); they enumerate every two-subset of
\(\mathbb Z_5\) exactly once.  The five lower singletons and five displayed
upper triples are also distinct.  Hence (2.15a) literally rechecks the
Dong--Mao \((5,1,2)\) output needed here.

The fibres (2.13) are disjoint, so all lifted diamonds form one bank.
Summing (2.15) over the possible \(H\)-patterns gives

\[
\begin{aligned}
 D_m
 &=\binom{2m-5}{m-1}
   +5\binom{2m-5}{m-2}
   +5\binom{2m-5}{m-3}
   +\binom{2m-5}{m-4}\\
 &=2\binom{2m-5}{m-1}
   +10\binom{2m-5}{m-2},
\end{aligned}                                         \tag{2.16}
\]

where the second line uses the symmetry of the \((2m-5)\)-row.

Finally,

\[
 {\binom{2m-5}{m-2}\over\binom{2m}{m}}
 ={m(m-1)\over8(2m-1)(2m-3)},\qquad
 {\binom{2m-5}{m-1}\over\binom{2m-5}{m-2}}
 ={m-3\over m-1}.                                    \tag{2.17}
\]

Substitution into (2.10) proves (2.11).  \(\square\)

### Corollary 2.3 (optimality on the frozen five-fibre face)

The bank in Theorem 2.2 is maximum among all central banks whose diamonds
preserve the \(H\)-intersection of every vertex.

#### Proof

In one fibre, the elementary lower/middle/upper rank bound is

\[
 \min\left\{\binom5j,\left\lfloor {1\over2}\binom5{j+1}\right\rfloor,
                    \binom5{j+2}\right\}.             \tag{2.18}
\]

For \(j=0,1,2,3\), these four values are \(1,5,5,1\), exactly (2.15).
No fibre-preserving diamond exists outside that range.  Since distinct
fibres have disjoint vertices, the four sharp bounds add.  \(\square\)

The exact relative deficit from the unrestricted capacity is

\[
 1-{D_m\over\frac12\binom{2m}{m}}
 ={(m-1)(m-3)\over(2m-1)(2m-3)}.                     \tag{2.19}
\]

Thus the cycle-lemma bank removes three quarters of the central packing
problem asymptotically, but leaves a genuine one-quarter bank-completion
problem.  Two such five-fibre banks do not even have enough total diamonds
to form a full Catalan matching once \(m\ge6\):

\[
 2D_m<\binom{2m}{m-1}\qquad(m\ge6).                  \tag{2.20}
\]

Indeed, after using (2.11) and
\(\binom{2m}{m-1}=\frac m{m+1}\binom{2m}{m}\),
(2.20) is equivalent to \(m^2-7m+7>0\), which holds for \(m\ge6\).
So Theorem 2.2 is a substantial one-bank absorber, not by itself a
two-bank route to the ordered four-transversal.

## 3. Exact two-bank normal form

In the central three levels, call a family of diamonds a **bank** if its
four-vertex intervals are pairwise disjoint.  Equivalently, inside one bank
all lower endpoints, all upper endpoints, and all physical middle vertices
are distinct.

Let \({\cal Q}_0,{\cal Q}_1\) be two banks.  Form their **cross-overlap
multigraph** \(H({\cal Q}_0,{\cal Q}_1)\): its vertices are the selected
diamonds, and for every middle-rank set used by one diamond in each bank,
join those two diamond vertices.  There are no within-bank edges.

### Theorem 3.1 (two-bank fusion equivalence)

The Catalan Linear Matching assertion at parameter \(m\) is equivalent to
the existence of two banks \({\cal Q}_0,{\cal Q}_1\) such that:

1. their union has every rank-\((m-1)\) lower endpoint exactly once;
2. their union has every rank-\((m+1)\) upper endpoint exactly once; and
3. \(H({\cal Q}_0,{\cal Q}_1)\) is a forest.             \tag{3.1}

Under Items 1--2 the overlap multigraph has no parallel pair, and every
vertex has degree at most two.  Thus Item 3 says exactly that it is a linear
forest.

#### Proof

Assume Items 1--3.  Items 1--2 make the selected diamonds a perfect matching
between the lower and upper colour shores.  Let \(F\) be their physical
Johnson lift on the middle rank.  Each bank is a matching in \(F\), so
\(\Delta(F)\le2\).  Two selected diamonds cannot have the same two middle
vertices: their lower endpoint would be the intersection of those vertices
and their upper endpoint their union, contradicting Items 1--2.  Hence
\(F\) is simple.

The cross-overlap graph is the line graph of \(F\), after isolated middle
vertices are ignored.  Since \(F\) has maximum degree two, it contains a
cycle if and only if its line graph contains the corresponding cycle.
Item 3 therefore makes \(F\) a linear forest.  Orient each path component.
The first and second middle endpoints of every diamond are then globally
injective tail and head maps, while Items 1--2 give the lower and upper
transversals.  This is the ordered four-transversal.

Conversely, start with a Catalan linear matching and alternately two-colour
the edges of every physical path component.  Each colour class is a matching
on the middle rank; global lower/upper injectivity makes its full Boolean
diamonds pairwise vertex-disjoint.  Hence the two colour classes are banks.
Their cross-overlap graph is the line graph of a linear forest and is again
a linear forest.  Items 1--3 follow.  \(\square\)

If orientations are part of the supplied data, the criterion for that
**oriented** union is instead: every cross-bank overlap is head-to-tail and
the resulting directed overlap graph has no directed cycle.  This can be
stronger than Item 3 for an arbitrarily frozen orientation.  If orientations
may be chosen after the banks, Item 3 is exactly what guarantees a valid
choice: orient every physical forest component consistently.

## 4. The exact remaining compatibility

Dong--Mao supplies one bank in its parameter range.  It does not correlate
two banks.  Even a positive solution of their central Problem 4.2 would
supply only one bank of size \(\lfloor M/2\rfloor\), where

\[
 M=\binom{2m}{m}=(m+1)\operatorname {Cat}_m,\qquad
 N=\binom{2m}{m-1}=m\operatorname {Cat}_m.            \tag{4.1}
\]

To infer the ordered four-transversal from two interval packings, one must
still choose subbanks of total size \(N\) whose lower and upper palettes are
both complementary and whose cross-overlap graph has no alternating cycle.
These are joint conditions; separate maximum size, separate endpoint
coverage, or separate vertex-disjointness inside each bank does not imply
them.

Accordingly the exact open statement exposed by this route is:

> **UNPROVED correlated two-bank theorem.**  There are two central
> vertex-disjoint diamond banks and subbanks satisfying Items 1--3 of
> Theorem 3.1.

This statement is equivalent to the Catalan Linear Matching Theorem, not a
consequence of Dong--Mao.  A weaker useful target would tile the lower and
upper colour layers by many fixed-core banks while keeping their aggregate
two-colouring internally vertex-disjoint and the final cross-overlap graph
acyclic.  No such cross-core compatibility theorem is proved here.

## 5. Proof audit

The primary-source checks used above are:

1. Theorem 1.2 has hypothesis \(n\ge(\ell+1)r+\ell\), not merely the
   rank-capacity inequality.
2. Proposition 2.5 proves pairwise disjoint **intervals**, so the two middle
   vertices of distinct diamonds are disjoint in the fixed-core lift.
3. Problem 4.2 explicitly leaves the central three-level range open; (1.4)
   puts every \(m\ge2\) Catalan instance in that range.
4. The fixed-core lift deletes the same core from a hypothetical collision,
   so it preserves literal vertex-disjointness, not only endpoint
   injectivity.
5. The five-coordinate bank is independently literalized by (2.15a).
   Different \(H\)-patterns are disjoint fibres, and the exact
   lower/middle/upper capacity in each fibre is (2.18).
6. The two-bank proof uses no unproved interval-packing assertion.  Its
   decisive identification is that, because each bank is a middle matching,
   the cross-overlap graph is exactly the line graph of the physical
   maximum-degree-two lift.  Outer-palette injectivity rules out parallel
   physical edges.

The central maximum-bank equation (1.3), correlated two-bank existence, and
any fibre aggregation closing the remaining deficit in (2.19) remain
**UNPROVED**.

The finite arithmetic and local \({\cal B}_5\) checks are replayed by

~~~text
python3 scratch/audit_dong_mao_five_fibre_bank_20260802.py
~~~
