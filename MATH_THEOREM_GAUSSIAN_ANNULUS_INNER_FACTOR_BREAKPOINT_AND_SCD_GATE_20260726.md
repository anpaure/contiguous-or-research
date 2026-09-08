# Gaussian annulus packets: the inner tight-cycle factor, the all-codegree formula, and the SCD endpoint gate

Date: 2026-07-26

## 0. Verdict

Put

\[
 n=2m,\qquad q_0=\lceil a\sqrt m\rceil,\qquad
 r=m-q_0,\qquad s=n-r=m+q_0,
\]

where \(0<a<b\) are fixed, and put

\[
 N_u=\binom n{m-u},\qquad W=\binom n m,
 \qquad H=\lfloor b\sqrt m\rfloor.
\]

The proposed first-annulus selection has two genuinely different parts.

1.  At rank \(r\), it asks for an almost decomposition of
    \(K_n^{(r)}\) into tight Hamilton cycles.  The auxiliary packet
    hypergraph is exactly regular and has

    \[
      \frac{\Delta _2}{D}=\frac{2}{rs}=(2+o(1))m^{-2}.
    \]

    This lies at the constant boundary, rather than below the boundary,
    of the known variable-rank Grable nibble criterion.

2.  A rank-\(r\) near-factor alone does not cover the deeper annulus.
    The exact extra datum is an endpoint/deque flag at every owned
    rank-\(r\) interval.  An SCD whose flags are compatible with those
    deques would give **zero holes at every deeper rank simultaneously**.
    PBBS supplies a correct-rank Johnson chronology, while an SCD supplies
    a bijective nested target assignment; neither supplies cyclic
    residence/deque compatibility.

There is one new useful exact reduction for the first part.  Every
\(j\)-codegree is given by a finite circular-breakpoint factorial formula
(Theorem 3.1 below).  Thus the full-codegree hypothesis in the 2025
Gould--Kelly nibble is no longer an unspecified geometric question: it is
one explicit one-dimensional profile optimization.  What is not proved
here is the uniform lower bound on its bottleneck \(B_m\), nor the
diagonal uniformity needed to apply a theorem stated with fixed packet
rank.

## 1. The inner-rank packet hypergraph

Let \(\mathcal H_r\) have vertex set \(\binom{[n]}r\).  Its edges are
the sets

\[
 e_r(\pi)=\{I_\pi(t,r):t\in\mathbb Z_n\},
\]

where cyclic orders are taken modulo rotation and reversal.  In the
present range \(2\le r\le n-2\), the \(n\) intervals are distinct and
their intersection-\((r-1)\) graph recovers the coordinate cycle.  Hence
there are \((n-1)!/2\) distinct packet edges, each of size \(n\).

### Proposition 1.1 (degree and all pair-codegrees)

Every vertex has degree

\[
 \boxed{D=\frac{r!s!}{2}.}                                      \tag{1.1}
\]

For distinct \(A,B\in\binom{[n]}r\), write
\(d=|A\setminus B|=|B\setminus A|\).  If \(1\le d<r\), then

\[
 \boxed{
 D(A,B)=d!^2(r-d)!(s-d)!,\qquad
 \frac{D(A,B)}D=
 \frac{2}{\binom rd\binom sd}.}                 \tag{1.2}
\]

If \(d=r\), then

\[
 \boxed{
 D(A,B)=\frac{r!^2(s-r+1)!}{2},\qquad
 \frac{D(A,B)}D=
 \frac{s-r+1}{\binom sr}.}                       \tag{1.3}
\]

Consequently, for fixed \(a>0\) and all sufficiently large \(m\),

\[
 \boxed{
 \Delta _2=\frac{2D}{rs},\qquad
 \frac{\Delta _2}{D}=\frac2{m^2-q_0^2}
 =(2+o(1))m^{-2}.}                                \tag{1.4}
\]

#### Proof

Contracting a prescribed \(r\)-interval to one block gives
\(r!s!\) directed cyclic orders modulo rotation.  Reversal pairs them,
which proves (1.1).

If \(d<r\), the four nonempty Venn cells of \(A,B\) have to occur as
four consecutive blocks.  The two possible directions are identified by
reversal, leaving the product of the four internal factorials in (1.2).
If \(A,B\) are disjoint, contract both to blocks.  There are
\(s-r+2\) circular objects; ordering those, ordering the two blocks, and
dividing by reversal gives (1.3).

For \(1\le d<r\), both binomial coefficients in (1.2) are minimized at
\(d=1\) among the nontrivial endpoint values in the present asymptotic
range.  The disjoint ratio in (1.3) is

\[
 \frac{2q_0+1}{\binom{m+q_0}{2q_0}},
\]

which is superpolynomially smaller than \(m^{-2}\).  This proves (1.4).
\(\square\)

The exact incidence identity

\[
 \sum_{B:\,|A\setminus B|=1}D(A,B)=2D             \tag{1.5}
\]

shows that the critical distance-one codegree cannot be removed by a
regular sparsification: every packet through \(A\) has exactly two
rank-\(r\) cyclic neighbours of \(A\).

The natural packet count is

\[
 K=\left\lfloor\frac{N_{q_0}}n\right\rfloor
 =\left(e^{-a^2}+o(1)\right)\frac W{2m}.            \tag{1.6}
\]

The floor is necessary: \(n\mid N_{q_0}\) need not hold.  It costs fewer
than \(n=o(W)\) inner targets.

## 2. The known growing-rank nibble is exactly critical

Here

\[
 \log N_{q_0}=2m\log2+O(\log m),
\]

and therefore

\[
 \boxed{
 \frac{n\Delta _2\log N_{q_0}}D
 =8\log2+o(1).}                                     \tag{2.1}
\]

Grable's variable-rank sufficient hypothesis is

\[
 \Delta _2=o\!\left(\frac D{n\log N_{q_0}}\right).
\]

Thus (2.1) misses it by a fixed factor, not by a hidden logarithm.
Fixed-uniformity Pippenger--Frankl--Rödl theorems cannot be applied after
letting \(n=2m\) grow.  The recent Gould--Kelly theorem can exploit all
higher codegrees, so it is the relevant possible improvement; the next
section gives the exact input needed for that test.

## 3. Exact all-codegree breakpoint formula

Let \(F=(S_1,\ldots,S_j)\) be distinct labeled rank-\(r\) targets.  Its
coordinate-membership profile is

\[
 a_J(F)=\#\{x\in[n]:\{i:x\in S_i\}=J\},
 \qquad J\subseteq[j].                               \tag{3.1}
\]

For a labeled start vector

\[
 t=(t_1,\ldots,t_j)\in\mathbb Z_n^j,
 \qquad t_1=0,quad t_i\ne t_h\ (i\ne h),
\]

put

\[
 c_J(t)=\#\{z\in\mathbb Z_n:
       \{i:z\in[t_i,t_i+r)\}=J\}.                  \tag{3.2}
\]

### Theorem 3.1 (breakpoint factorial formula)

The number of **directed** cyclic orders modulo rotation containing every
\(S_i\), with the orientation of the order retained, is

\[
 \boxed{
 D_j^+(F)=
 \sum_{\substack{t_1=0,\ t_2,\ldots,t_j\ {\rm distinct}}}
 \mathbf1_{\{a_J(F)=c_J(t)\ \forall J\}}
 \prod_{J\subseteq[j]}a_J(F)!.}                    \tag{3.3}
\]

The unoriented codegree is \(D_j(F)=D_j^+(F)/2\).
Consequently, if \(C_j=\max_{|F|=j}D_j(F)\), then

\[
 \boxed{
 C_j=\frac12\max_a
 \left(\#\{t:c(t)=a\}\right)\prod_Ja_J!,}         \tag{3.4}
\]

where the maximum is over profiles realized by \(j\) distinct
length-\(r\) circular arcs.

#### Proof

In a directed cyclic order containing \(S_i\), the start of \(S_i\) is
unique.  Rotate positions so that the start of \(S_1\) is zero.  Once the
remaining starts are fixed, position \(z\) has the membership pattern in
(3.2).  A label of coordinate type \(J\) may be assigned to precisely the
positions of type \(J\); hence a compatible profile admits exactly
\(\prod_Ja_J!\) labelings.  Conversely every such labeling gives a unique
directed cyclic order with the prescribed starts.  Summing proves (3.3).
Reversal acts freely and preserves the static packet, proving (3.4).
\(\square\)

There is also a rigorous envelope which avoids solving the profile
optimization.  Put

\[
 p_t=\frac2{\binom rt\binom st}\quad(1\le t<r),
 \qquad p_r=\frac{s-r+1}{\binom sr},
 \qquad d_j=\min\{r,\lfloor j/2\rfloor\}.
\]

### Proposition 3.2 (all-codegree distance envelope)

For \(2\le j\le n\),

\[
 \boxed{
 \frac{C_j}{D}\le\max_{d_j\le t\le r}p_t
 =\begin{cases}
   \max\{p_{d_j},p_r\},&d_j<r,\\
   p_r,&d_j=r.
  \end{cases}}                                      \tag{3.5a}
\]

Moreover \(C_n=1\).

#### Proof

The \(j\) starts of prescribed windows form a \(j\)-set on the coordinate
cycle.  Since a radius-\((d-1)\) cyclic ball has at most \(2d-1\)
positions, two starts have cyclic distance at least
\(\lfloor j/2\rfloor\).  For \(r<n/2\), the corresponding rank-\(r\)
windows have Johnson distance \(\min\{r,u\}\), where \(u\) is their
cyclic start distance in \([0,n/2]\).  The codegree of the whole family
is at most the codegree of this pair.  Finally
\(\binom rt\binom st\) is unimodal in \(t\), so its minimum on the
displayed interval occurs at an endpoint; the disjoint endpoint is
\(p_r\).  Simplicity gives \(C_n=1\). \(\square\)

Periodic closure is not a hidden exception.  If
\(g=\gcd(n,r)\), \(L=n/g\), and one prescribes the \(L\) windows whose
starts form a complete \(+r\) orbit, their exact codegree is

\[
 \boxed{(g!)^L.}                                    \tag{3.5b}
\]

Indeed those windows recover the cyclic order of the \(L\) consecutive
\(g\)-element chunks, leaving only the internal order of each chunk.
Here \(g\mid n-2r=2q_0\), so \(g=O(\sqrt m)\); this configuration has
rooted bottleneck
\(\exp(g\log(m/g)+O(g))\), never a bounded scale.

Formula (3.4) is useful because \(c(t)\) is obtained by walking around at
most \(2j\) start/end breakpoints and toggling one interval label at each
breakpoint (two labels at a coincident start/end).  The remaining
all-codegree question is now the explicit extremal quantity

\[
 \mathfrak B_m=\min\left\{
 \sqrt{D/C_2},
 \min_{4\le j\le n}\left(D/C_j\right)^{1/(j-1)}
 \right\}.                                          \tag{3.5c}
\]

The full-codegree bottleneck in Theorem 1.4 of Gould--Kelly is exactly
\(\mathfrak B_m\).  However, the **published theorem cannot yield a
nontrivial conclusion in the present diagonal even if
\(\mathfrak B_m\asymp m\)**.  Its leftover is

\[
 N_{q_0}\mathfrak B_m^{-1+\gamma}(\log D)^A,        \tag{3.6a}
\]

and its hierarchy is

\[
 1/D\ll1/A\ll\gamma\ll1/(n-1).
\]

This is a fixed-uniformity hierarchy, not a uniform statement.  More
decisively, the proof takes \(A=10/\gamma^4\) and observes that the result
is trivial unless

\[
 \mathfrak B_m\ge(\log D)^{10/\gamma^4}.            \tag{3.6b}
\]

Here \(\mathfrak B_m\le\sqrt{D/C_2}=\sqrt{rs/2}=O(m)\), while
\(\log D=\Theta(m\log m)\).  Condition (3.6b) is impossible even for a
fixed positive \(\gamma\), and a fortiori when
\(\gamma=o(1/m)\) as the displayed hierarchy would require on the
diagonal.  Thus the 2025 theorem identifies the right full-codegree
quantity but does **not** round this packet hypergraph.  A new uniform
nibble with radically smaller polylogarithmic loss would still be needed.

There is no evident geometric all-codegree obstruction.  For example, \(j\)
consecutive rank-\(r\) windows have codegree

\[
 (r-j+1)!(s-j+1)!\qquad(1\le j\le r+1),             \tag{3.6}
\]

and a full packet has codegree one.  Both profiles give a bottleneck of
polynomial order.  However, (3.6) has not been proved extremal; mixed
clusters of circular arcs must be controlled in (3.4).

References for this quantitative comparison are Gould--Kelly,
*Advancing the Rödl Nibble* (arXiv:2511.11375, Theorem 1.4), and the
Kostochka--Rödl/Grable variable-rank criterion quoted there.

## 4. Inner matching is not the whole packet theorem

Suppose \(\mathcal F\) is a rank-\(r\) packet matching.  Write

\[
 \mu_u(T)=\#\{\pi\in\mathcal F:T
       \text{ is a cyclic }(m-u)\text{-interval of }\pi\}.
\]

Its middle collision mass is

\[
 C_m(\mathcal F)=
 \sum_{X\in\binom{[n]}m}(\mu_0(X)-1)_+.             \tag{4.1}
\]

Rank-\(r\) disjointness does not control (4.1).  The exact annulus packet
theorem needs

\[
 C_m(\mathcal F)=o(W),
 \qquad
 \sum_{u=q_0}^{H}h_u(\mathcal F)=o(W),              \tag{4.2}
\]

where \(h_u=\#\{T:\mu_u(T)=0\}\).  The uniform fractional point has
middle load \(N_{q_0}/W=e^{-a^2+o(1)}<1\), but a diffuse integral choice
would still have linear collision mass.  Thus the middle shore is a real
conflict constraint, albeit one with constant fractional slack.

## 5. Exact extension and deficiency identities

Let \(d\ge1\), and let \(|T|=r-d\).  Define
\(\operatorname{Ext}_d(T)\) to count pairs \((S,\pi)\) such that

* \(S\supset T\), \(|S|=r\);
* \(S\) is owned by \(\pi\in\mathcal F\); and
* inside the same cyclic order, \(T\) is obtained from \(S\) by deleting
  a prefix and a suffix of total size \(d\).

### Proposition 5.1 (grouped extensions)

For every \(T\),

\[
 \boxed{
 \operatorname{Ext}_d(T)=(d+1)\mu_{q_0+d}(T).}       \tag{5.1}
\]

Furthermore, if \(n|\mathcal F|=N_{q_0}+o(W)\), then

\[
 \sum_T\operatorname{Ext}_d(T)
 =(d+1)N_{q_0}+o(Wd).                                \tag{5.2}
\]

#### Proof

One occurrence of \(T\) in a packet lies in exactly \(d+1\) of that
packet's rank-\(r\) windows, according to how the \(d\) deleted boundary
elements split between the left and right ends.  This is a bijection of
occurrences, proving (5.1).  Sum it and use that every packet has exactly
\(n\) targets at every rank to obtain (5.2).  \(\square\)

At depth \(d\), total load is \(n|\mathcal F|\), so the exact elementary
deficiency identity is

\[
 \boxed{
 h_{q_0+d}
 =\sum_T(\mu_{q_0+d}(T)-1)_+
   -\bigl(n|\mathcal F|-N_{q_0+d}\bigr).}            \tag{5.3}
\]

Thus deeper coverage asks for duplicate excess to sit at its forced
minimum, simultaneously at \(\Theta(\sqrt m)\) ranks.  Merely obtaining
the correct mean

\[
 \lambda_{d}=\frac{N_{q_0}}{N_{q_0+d}}
 =\exp\!\left(\frac{(q_0+d)^2-q_0^2}{m}+o(1)\right)
\]

does not imply (4.2).  This precisely identifies the extra correlation a
rank-\(r\) nibble would have to preserve.

The first deeper rank already changes the codegree scale.  If
\(T\subset S\), \(|S|=r\), \(|T|=r-1\), then

\[
 \boxed{
 D(S,T)=(r-1)!s!,\qquad
 \frac{D(S,T)}{D_r}=\frac2r,\qquad
 \frac{D(S,T)}{D_{r-1}}=\frac2{s+1}.}               \tag{5.4}
\]

Conditioned on \(S\) being an interval, this merely says that its omitted
element must be one of the two endpoints.  More generally, for
\(|T|=r-d\),

\[
 \boxed{
 \frac{D(S,T)}{D_r}=\frac{d+1}{\binom rd}.}         \tag{5.5}
\]

Thus the same-rank owner hypergraph has relative codegree
\(\Theta(m^{-2})\), but the first nested shore has the intrinsic scale
\(\Theta(m^{-1})\).  Treating the two ranks as one ordinary packet edge
of size \(2n\) gives ``edge size times relative codegree'' of constant
order, and putting all \(\Theta(\sqrt m)\) annular ranks into one edge
raises this product to order \(\sqrt m\).  This is the precise reason the
favorable inner-rank nibble parameters do not propagate to a naive
all-rank matching theorem.

## 6. An SCD would make the deeper correlation exact

Fix an SCD \(\mathscr C\) of \(2^{[n]}\).  Every rank-\(r\) set \(S\)
lies on a unique chain.  If that chain reaches rank \(r-d\), denote its
rank-\((r-d)\) member by \(P_d(S)\).  The map

\[
 S\longmapsto P_d(S)
\]

is a bijection from the \(N_{q_0+d}\) eligible rank-\(r\) sets onto
\(\binom{[n]}{r-d}\).

### Theorem 6.1 (SCD--packet endpoint criterion)

Suppose \(\mathcal F\) is a packet matching covering every eligible
rank-\(r\) set, and suppose that whenever \(P_d(S)\) is defined for
\(1\le d\le H-q_0\), the owner packet of \(S\) also contains
\(P_d(S)\) as a cyclic interval.  Then

\[
 \boxed{h_{q_0+d}(\mathcal F)=0
 \quad(1\le d\le H-q_0).}                            \tag{6.1}
\]

#### Proof

Every rank-\((r-d)\) target is \(P_d(S)\) for one eligible \(S\).
By hypothesis it occurs in the packet owning \(S\).  Hence no target is
missing.  \(\square\)

The approximate form is equally exact.  Let \(B_d\) be the number of
eligible \(S\)'s which are either not owned or whose owner packet does
not contain \(P_d(S)\).  Since \(P_d\) is a bijection,

\[
 \boxed{h_{q_0+d}(\mathcal F)\le B_d.}              \tag{6.1a}
\]

Consequently \(\sum_dB_d=o(W)\) is an SCD/deque certificate for the
desired aggregate annulus bound.  Missing inner targets may harmlessly
be chosen among chains whose minimum rank is \(r\); there are
\(N_{q_0}-N_{q_0+1}=\Theta_a(W/\sqrt m)\) such chains, much more than
the unavoidable divisibility leave of fewer than \(n\) targets.

The condition has a concrete local form.  Write the chain below \(S\) as

\[
 S=P_0(S)\supset P_1(S)\supset\cdots,
 \qquad P_i(S)\setminus P_{i+1}(S)=\{x_i\}.
\]

It is compatible with the owner cyclic order through depth \(L\) exactly
when \(x_i\) is a left or right endpoint of the current interval at every
step.  Equivalently, the deletion word is a deque deletion of the linear
order induced on \(S\).

For one prescribed flag of length \(L<r\), the exact fraction of cyclic
orders through \(S\) which realize it is

\[
 \boxed{\frac{2^L}{(r)_L}.}                          \tag{6.2}
\]

Indeed, choose left/right for each of the \(L\) deletions and order the
remaining \(r-L\) elements arbitrarily.  This gives
\(2^L(r-L)!\) of the \(r!\) internal orders of \(S\).

Equation (6.2) explains why an arbitrary preassigned SCD is not a free
addition to the inner nibble.  At Gaussian thickness
\(L=\Theta(\sqrt m)\), even one flag has density
\(\exp[-\Theta(\sqrt m\log m)]\), and the \(n\) flags in one packet are
strongly coupled.  A successful proof must construct the SCD and the
packet factor together, rather than first choosing either object.

### Proposition 6.2 (fixed-depth endpoint Hall is free once covered)

Let \(\mathcal F\) be a rank-\(r\) packet matching and fix \(d\ge1\).
There is an injection from the covered rank-\((r-d)\) targets to owned
rank-\(r\) targets such that every target is an aligned subinterval of
its assigned owner.  Consequently the number of omissions in a
compatible depth-\(d\) root assignment is exactly
\(h_{q_0+d}(\mathcal F)\); there is no additional Hall defect at any one
fixed depth.

#### Proof

Form a \((d+1)\)-uniform multihypergraph \(G_d\) whose vertices are
rank-\((r-d)\) targets.  An owned rank-\(r\) interval \(S\) is an edge
consisting of its \(d+1\) aligned subintervals of rank \(r-d\).
Rank-\(r\) packet disjointness makes these edges distinct.  Every
occurrence of a target \(T\) in a packet has exactly \(d+1\) containing
rank-\(r\) windows in that packet, so

\[
 \deg_{G_d}(T)=(d+1)\mu_{q_0+d}(T).                 \tag{6.3}
\]

Delete the isolated vertices.  The remaining multihypergraph has minimum
degree at least \(d+1\).  For any vertex set \(U\), if \(E(U)\) denotes
all edges incident with \(U\), then

\[
 (d+1)|U|\le\sum_{v\in U}\deg_{G_d}(v)
 \le(d+1)|E(U)|.
\]

Thus the vertex--hyperedge incidence bipartite graph satisfies Hall's
condition, and has a matching saturating every nonisolated vertex.  Read
the matched edge as the required distinct rank-\(r\) parent. \(\square\)

The assignments supplied for different \(d\)'s need not be nested inside
the same owner: a root \(S\) assigned a target at depth \(d\) and one at
depth \(d+1\) may receive two incompatible prefix--suffix splits.
Selecting the depthwise Hall matchings coherently is the coupled
multi-depth choice which Proposition 6.2 does not settle.

## 7. Why the current PBBS and SCD theorems do not supply the criterion

PBBS proves a powerful sibling statement: at every depth and for every
target there is a correct-rank consecutive Johnson path whose
intersection is that target.  This gives the target side of (6.1), but
not cyclic residence.

For a length-\(n\) Johnson cycle \((S_i)\) of rank \(r\), write

\[
 d_i=S_i\setminus S_{i+1},\qquad
 a_i=S_{i+1}\setminus S_i.
\]

If the deletions are all distinct, the cycle is the rank-\(r\) window
cycle of a cyclic order precisely when

\[
 \boxed{a_i=d_{i+r}\quad\text{for every }i\pmod n.} \tag{7.1}
\]

PBBS correct-shadow support does not imply (7.1), and its components need
not even have length \(n\).  Conversely, an SCD gives the bijections
\(S\mapsto P_d(S)\) but does not arrange its deletion words as the deques
of one common packet factor.

The positive PBBS morphological-preimage theorem has the same exact
boundary: it preserves the middle chronology and the entire upper
dilation tower, but necessarily destroys the canonical deepest lower
tower.  Its remaining open condition is precisely an SCD-quality lower
endpoint schedule.  Thus it does not independently prove Theorem 6.1's
hypothesis.

## 8. Precise remaining theorem

For every fixed \(0<a<b\), it is enough to construct cyclic orders
\(\mathcal F_m\) satisfying

1. their rank-\(r\) interval supports are pairwise disjoint and cover
   \(N_{q_0}-o(W)\) targets;
2. their middle collision mass is \(o(W)\); and
3. either directly
   \(\sum_{u=q_0}^{H}h_u=o(W)\), or, as a stronger sufficient route via
   Theorem 6.1, they admit an asymptotically complete SCD/deque endpoint
   assignment.

The first item is a growing-uniformity partial Bailey--Stevens theorem.
The exact higher-codegree input for the strongest current nibble is
(3.4).  The third item is the genuinely new all-depth correlation.  A
plain pseudorandom near-factor is not enough: it must be endpoint-rainbow
relative to one nested target assignment.
