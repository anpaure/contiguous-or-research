# Transverse `Q_4` mosaics: an exact Gaussian cut, a dyadic XOR escape, and the remaining CPM gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Write

\[
                         W=\binom{2m}{m}.
\tag{0.1}
\]

The corrected fixed-quartet theorem shows that potential reachability is
not source capacity: for the rank-two mosaic

\[
 \{12,13\},\qquad \{14,24\},\qquad \{23,34\},
\tag{0.2}
\]

the exact type ratio

\[
 R_q(g,u)={2^q\binom gq\over\binom{u+q}q}
\tag{0.3}
\]

tends to \(e^{-6A^2}\) at \(q=A\sqrt m\) on a positive-density
Gaussian type box.  This report does not reprove (0.3).  It proves a
different, factor-independent cut which survives after the rank-one and
rank-three local layers are also activated.

The conclusions are as follows.

1.  There is an exact all-rank tensor tiling over fixed four-blocks.  It
    gives an owner-disjoint \(Q_r\) near-factor with exponentially small
    leave for every \(r\le (7/8-\varepsilon)m/2\).  Nevertheless every
    one of its directions is internal to a fixed block.
2.  Let \(F_4(S)\) count full four-blocks.  At
    \(q=\lfloor A\sqrt m\rfloor\), every owner-disjoint or owner-partial
    family (at most one start per middle owner) whose depth-\(q\) windows
    stay inside the fixed blocks has at least

    \[
       (\delta_4(A)-o(1))W
    \tag{0.4}
    \]

    lower holes, and the same upper deficit holds by complementation,
    where

    \[
    \boxed{
    \begin{aligned}
     c&=\sqrt{8/11},\\
     \delta_4(A)
       &=e^{-A^2}\Phi\!\left[-A\left({1\over c}-{c\over2}\right)\right]
        -\Phi\!\left[-A\left({1\over c}+{c\over2}\right)\right]>0.
    \end{aligned}}
    \tag{0.5}
    \]

3.  More sharply, if \(B_q\) is the set of starts whose actual
    \(q\)-window uses a cross-block direction, then

    \[
       M_q^-\ge (\delta_4(A)-o(1))W-|B_q|.
    \tag{0.6}
    \]

    Thus a positive-density number of the *actual chronological
    windows*, not merely a large option catalogue, must cross the old
    blocks.  For a doubled-permutation factor on a \(Q_r\)-packet with
    \(t\) transverse axes, at most

    \[
                         \min\{1,qt/r\}
    \tag{0.7}
    \]

    of its starts see a transverse axis.  Consequently a bounded-axis
    hierarchy fails whenever \(qt/r=o(1)\).
4.  A literal orientation cube has pairwise disjoint coordinate-swap
    axes.  Hence a sorting network which reuses wires is not itself a
    cubical tiling.  Exact uniform full-layer tilings have the additional
    arithmetic obstruction

    \[
                   r\le v_2\binom{2m}{m}=s_2(m).
    \tag{0.8}
    \]

    This closes an exact full-layer uniform recursion at Gaussian-scale
    dimension, but not a near-factor.
5.  The natural two-quartet promotion is not wholly impossible.  There is
    an explicit \(Q_2\cup Q_2=Q_3\) transverse seed.  However, for the
    particular star mosaic (0.2), the nine directed balanced branches
    have a common-owner clique, so at most one branch can be promoted in
    a fixed direction without cutting the old cells.  An aligned
    \(L,M,U\) cylinder has an odd number of base cells, giving a sharp
    parity obstruction to promoting the whole cylinder even once.
6.  There is nevertheless a genuine invariant-removing exact mosaic on
    dyadic ground sets.  If

    \[
                         [2m]=G=\mathbb F_2^\ell,
                         \qquad 2m=2^\ell,
    \tag{0.9}
    \]

    an XOR hash chooses, owner by owner but cell-consistently, one of the
    translation matchings

    \[
                         M_a=\{\{x,x+a\}:x\in G\}/2.
    \tag{0.10}
    \]

    The chosen status cells are equal or disjoint and partition the
    middle layer exactly into variable-dimensional orientation cubes.
    For every fixed old four-block decomposition and every
    \(2\le r\le m/4\), they can be trimmed and subdivided into
    owner-disjoint \(Q_r\)-packets with

    \[
                         L=O(W/m)+e^{-\Omega(m)}W,
    \tag{0.11}
    \]

    all of whose retained axes cross the old four-blocks.  Thus
    \(L=o(W/H)\) for every \(H=o(m)\), and the obstruction (0.6) is
    genuinely escaped rather than hidden.
7.  The XOR trace ledger is exact, and target hash fibres are exactly
    uniform at odd ranks and exponentially close to uniform throughout
    the central band.  Thus raw hash-fibre cardinalities create no linear
    imbalance.  A chronological hash-level cut is not excluded and would
    have to use the trace map itself rather than fibre sizes alone.
8.  The exact packet-local obstruction is the \(q\)-subset XOR spectrum
    \(K_{P,q}\).  Reversal leaves every target multiset unchanged,
    complement only exchanges signs, antipodal inverse coupling is
    impossible, and translations cannot move even-depth hash defects.
9.  Conditional only on the stated certified literal context-array
    factor at the chosen dimension, these limitations do not create a
    Gaussian hash obstruction.  There is an integral
    translation-equivariant choice balancing every odd hash depth, and a
    second single common factor choice saturating every exact hash bin on
    both signs throughout \(40\log m\le q\le H=o(m)\).  This is still
    weaker than literal target coverage inside each hash fibre.
10. Under the same explicit factor hypothesis, high-dimensional cells
    admit a deterministic selector-array
    deployment of their entire active-set/affine-factor catalogue.  It
    is owner-exact and target-injective inside each selected status cell;
    all unresolved literal collisions occur between different cells.

What is not proved is the simultaneous literal target selection required
by `CPM`.  A clean sufficient route is to choose one legal factor state
in every retained packet so that the all-depth floor energy is \(o(W)\),
but `CPM` could in principle hold without that stronger floor balance.
The XOR mosaic proves a real owner-side escape and a substantial
chronological/hash-level completion.  It does not yet control literal
within-fibre collisions between different status cells.  It is also
presently restricted to dyadic \(2m\).

## 1. Literal orientation packets and nested gluing

Let \(M\) be an \(r\)-edge matching on the ground coordinates.  Let
\(F,E\) be disjoint from \(V(M)\), with

\[
                         |F|=|E|=m-r.
\tag{1.1}
\]

Define

\[
 \mathcal Q(F,E;M)
 =\{X:F\subseteq X,\ X\cap E=\varnothing,
       \ |X\cap e|=1\text{ for every }e\in M\}.
\tag{1.2}
\]

This is a literal middle-layer orientation \(Q_r\), of size \(2^r\).

### Lemma 1.1 (opposite-facet criterion)

Two literal \(Q_R\)-packets are opposite facets of one literal
\(Q_{R+1}\) if and only if, after exchanging their names, there are a
common matching \(M\), common pins \(F,E\), and a fresh pair
\(\{u,v\}\) such that

\[
\begin{aligned}
 P_0&=\mathcal Q(F\cup\{u\},E\cup\{v\};M),\\
 P_1&=\mathcal Q(F\cup\{v\},E\cup\{u\};M).
\end{aligned}
\tag{1.3}
\]

#### Proof

The two displayed packets are the two facets of
\(\mathcal Q(F,E;M\cup\{uv\})\), proving sufficiency.

Conversely, every Johnson edge inside an orientation cube flips one
member of its ground-coordinate matching.  A connected \(Q_R\) contained
in a \(Q_{R+1}\) uses exactly \(R\) of those axes and fixes the last
orientation.  It is therefore a facet.  The opposite facet has the same
old \(R\)-edge matching and the opposite status on the one unused pair,
which is exactly (1.3).  \(\square\)

### Lemma 1.2 (comparator-axis obstruction)

Independent axes of a literal Johnson cube use disjoint ground
coordinates.  In particular, two sorting-network comparators sharing a
wire cannot both survive as axes of one final orientation packet.

#### Proof

At a state \(X\), simultaneous legality forces a shared support
coordinate to have the same status in both swaps: selected in both or
unselected in both.  (A selected/unselected cross-role would require the
coordinate to lie both in and outside \(X\).)  In the selected case,
write the swaps as \(x\mapsto a\) and \(x\mapsto b\).  The two neighboring states

\[
                         X-x+a,\qquad X-x+b
\tag{1.4}
\]

are at Johnson distance one.  In a square obtained by applying two
independent cube axes they would be at distance two.  Sharing an
unselected endpoint is identical.  Thus the swap supports are disjoint.
Four-face propagation then keeps the same swap label on every parallel
edge of the cube.  \(\square\)

This does not forbid a comparator network as a routing device.  It says
that every leaf which is still a literal \(Q_r\) must reduce to a matching
of disjoint ground-coordinate pairs.  Reusing a wire requires cutting and
retiling, or a new path-factor theorem; network depth is not cube
dimension.

## 2. Exact arithmetic and statewise cylinder obstructions

Write \(s_2(n)\) for the number of ones in the binary expansion of
\(n\).

### Theorem 2.1 (uniform full-layer divisibility)

If the whole middle layer is partitioned into literal \(Q_r\)-packets,
then

\[
                         2^r\mid\binom{2m}{m},
                         \qquad r\le s_2(m).
\tag{2.1}
\]

#### Proof

Every packet has \(2^r\) vertices, proving the divisibility.  Legendre's
identity \(v_2(n!)=n-s_2(n)\) gives

\[
\begin{aligned}
 v_2\binom{2m}{m}
 &=2s_2(m)-s_2(2m)\\
 &=s_2(m).
\end{aligned}
\tag{2.2}
\]

This proves (2.1).  \(\square\)

There are useful statewise versions.  Let \(A,B\) be disjoint and assume
the following cylinder is nonempty.  If

\[
 \mathcal C(A,B)=\{X\in\tbinom{[2m]}m:A\subseteq X,
                                      \ X\cap B=\varnothing\}
\tag{2.3}
\]

is a union of whole \(Q_r\)-packets, then

\[
 r\le
 s_2(m-|A|)+s_2(m-|B|)-s_2(2m-|A|-|B|),
\tag{2.4}
\]

because the cylinder has size
\(\binom{2m-|A|-|B|}{m-|A|}\).  If \((B_i)_i\) partitions the ground
set and a nonempty block-occupancy cylinder

\[
 \mathcal C_{\boldsymbol\kappa}
 =\{X:|X\cap B_i|=\kappa_i\text{ for every }i\}
\tag{2.5}
\]

is a union of whole packets, then

\[
                         r\le
 \sum_i v_2\binom{|B_i|}{\kappa_i}.
\tag{2.6}
\]

For \(b\) four-blocks, the balanced cylinder
\(J(4,2)^b\) has size \(6^b\) and its tensor mosaic into \(Q_b\)'s
saturates valuation \(b\).  The full middle layer on \(4b\) coordinates,
however, has

\[
             v_2\binom{4b}{2b}=s_2(2b)=s_2(b)<b
             \qquad(b\ge2).
\tag{2.7}
\]

Thus no exact transverse reblocking can end in a full-layer partition by
\(Q_b\)-packets.  More generally, an exact uniform full-layer endpoint
has only \(r=O(\log m)\), far below a Gaussian compiler dimension.

The scope is important.  For a near-factor with leave \(L\), divisibility
only says

\[
                         L\equiv W\pmod {2^r}.
\tag{2.8}
\]

This permits an asymptotically negligible leave and does not refute
`CPM`.

## 3. The exact all-rank fixed-quartet near-factor

For this section write \(2m=4b\) and fix four-blocks
\(B_1,\ldots,B_b\).  On every block use the local partition

\[
\begin{array}{c|c}
\text{local rank}&\text{local cells}\\ \hline
0,4&Q_0\text{ singletons},\\
1&\{1,2\},\ \{3,4\},\\
2&\{12,13\},\ \{14,24\},\ \{23,34\},\\
3&\text{complements of the two rank-one edges}.
\end{array}
\tag{3.1}
\]

Each nonsingleton is a literal \(Q_1\), and (3.1) partitions all
sixteen local states.  Tensor over the \(b\) blocks and restrict to total
rank \(2b=m\).

### Proposition 3.1 (owner near-factor)

The tensor cell containing \(X\) is a literal \(Q_{D(X)}\), where

\[
                         D(X)=\#\{i:1\le|X\cap B_i|\le3\}.
\tag{3.2}
\]

For every cell with \(D\ge r\), fixing \(D-r\) orientations partitions
it exactly into \(Q_r\)'s.  The leave from cells with \(D<r\) obeys

\[
                         L_r\le
 2^b\sum_{d<r}\binom bd7^d.
\tag{3.3}
\]

In particular, if \(r=o(m)\), then

\[
                         L_r\le2^{m/2+o(m)}=o(W/H)
\tag{3.4}
\]

for every \(H\le m\).  More generally, for each fixed
\(\varepsilon>0\),

\[
 r\le(7/8-\varepsilon)b
 \quad\Longrightarrow\quad
                         L_r\le e^{-\Omega_\varepsilon(m)}W.
\tag{3.5}
\]

#### Proof

The tensor statement and subdivision are immediate from the local
partition.  Ignoring the global rank constraint, choose the \(d\)
eligible blocks, one of their fourteen nonempty nonfull states, and one
of the two empty/full states in every other block.  This gives

\[
 \binom bd14^d2^{b-d}=2^b\binom bd7^d,
\tag{3.6}
\]

and proves (3.3).  For \(r=o(m)\), its logarithm is
\(m/2+o(m)\), whereas \(W=2^{2m-o(m)}\), proving (3.4).

Under independent fair coordinate bits, the eligible-block indicators
are independent Bernoulli variables of mean \(14/16=7/8\).  A Chernoff
bound makes the event in (3.5) exponentially unlikely.  Conditioning on
total rank \(2b\) costs only a polynomial factor, since
\(2^{-4b}\binom{4b}{2b}\ge(4b+1)^{-1}\).  This proves (3.5).
\(\square\)

Every direction in this construction lies inside one fixed block, so the
full occupancy vector remains invariant.  The next section shows that
this is a genuine Gaussian capacity obstruction even though the owner
leave is exponentially small.

## 4. A factor-independent Gaussian full-block cut

For a set \(S\subseteq[4b]\), put

\[
                         F_4(S)=\#\{i:B_i\subseteq S\}.
\tag{4.1}
\]

For \(f\ge0\), define the owner and lower-target type sizes

\[
\begin{aligned}
 V_f&=\#\{X\in\tbinom{[4b]}{2b}:F_4(X)=f\},\\
 T_{f,q}&=\#\{T\in\tbinom{[4b]}{2b-q}:F_4(T)=f\}.
\end{aligned}
\tag{4.2}
\]

### Lemma 4.1 (exact Hall cut)

Suppose every middle owner is used at most once as the start of a
depth-\(q\) lower window, and every transition in every such window swaps
two coordinates in the same fixed four-block.  Then the number of absent
lower targets satisfies

\[
                         M_q^-\ge
 \sum_f(T_{f,q}-V_f)_+.
\tag{4.3}
\]

#### Proof

An internal swap preserves every block occupancy.  A block which is full
in one state is full in every state of the window, and a nonfull block
cannot become full in the intersection.  Therefore the lower intersection
has the same \(F_4\)-value as its source owner.  There are at most \(V_f\)
source starts of type \(f\), so at most \(V_f\) distinct targets of that
type can be covered.  Sum the positive deficits.  \(\square\)

We now evaluate (4.3) at Gaussian distance.  Let \(\phi,\Phi\) be the
standard normal density and distribution function.

### Lemma 4.2 (conditional local limit with audited constants)

Fix \(A>0\), put

\[
                         q=\lfloor A\sqrt m\rfloor,
                         \qquad m=2b,
\tag{4.4}
\]

and set

\[
                         \sigma_m^2={11m\over512},
                         \qquad c=\sqrt{8/11}.
\tag{4.5}
\]

There are centering constants

\[
                         \mu_0={b\over16}+O(1),
                         \qquad
                         \mu_q=\mu_0-{q\over8}+O_A(1)
\tag{4.6}
\]

such that, uniformly on every fixed \(O(\sqrt m)\) central window,

\[
\begin{aligned}
 {V_f\over W}
  &={1\over\sigma_m}\phi\!\left({f-\mu_0\over\sigma_m}\right)
    +o(m^{-1/2}),\\
 {T_{f,q}\over W}
  &=e^{-A^2}{1\over\sigma_m}
     \phi\!\left({f-\mu_q\over\sigma_m}\right)
    +o(m^{-1/2}).
\end{aligned}
\tag{4.7}
\]

The mass outside growing central windows is uniformly negligible.

#### Proof

Use independent Bernoulli-\(p\) coordinates, grouped into blocks.  For
one block let

\[
                         S=\text{its number of selected coordinates},
                         \qquad Y=\mathbf1_{\{S=4\}}.
\tag{4.8}
\]

Conditioning \(\sum_iS_i=k\) makes the selected set uniform on the
rank-\(k\) layer.  At \(p=1/2\),

\[
\begin{aligned}
 \operatorname{Var}S&=1,\\
 \operatorname{Var}Y&={15\over256},\\
 \operatorname{Cov}(S,Y)&={1\over8}.
\end{aligned}
\tag{4.9}
\]

Hence the conditional Schur-complement variance per block is

\[
 {15\over256}-{(1/8)^2\over1}={11\over256}.
\tag{4.10}
\]

Multiplication by \(b=m/2\) proves (4.5).  For the target layer use

\[
                         p_q={2b-q\over4b}
                             ={1\over2}-{q\over4b}.
\tag{4.11}
\]

Its conditional centre is \(bp_q^4+O(1)\), and therefore

\[
                         bp_q^4={b\over16}-{q\over8}+O_A(1),
\tag{4.12}
\]

which gives (4.6).  The variance changes by only \(o(m)\).

For completeness, the required lattice local limit follows directly by
two-dimensional Fourier inversion for \((S,Y)\).  Its support

\[
                         (0,0),(1,0),(2,0),(3,0),(4,1)
\tag{4.13}
\]

generates the full lattice \(\mathbb Z^2\), and the covariance is
nonsingular.  Uniformly for \(p=1/2+O(m^{-1/2})\), the characteristic
function has modulus strictly below one off a fixed neighborhood of the
origin.  Inside that neighborhood,

\[
 \log\mathbb E e^{i\langle\theta,(S,Y)-\mathbb E(S,Y)\rangle}
 =-{1\over2}\theta^T\Sigma_p\theta+O(\|\theta\|^3).
\tag{4.14}
\]

Split the inversion integral at \(\|\theta\|=b^{-2/5}\).  On the inner
part (4.14), after scaling by \(b^{-1/2}\), converges uniformly to the
bivariate Gaussian integral; on the complement the aperiodicity bound
and the quadratic real part give \(o(b^{-1})\).  Dividing this joint local
limit by the one-dimensional local limit for \(\sum S_i=k\) gives
(4.7), with error \(o(m^{-1/2})\).  The same conditional Gaussian limit
is tight.  Hence, first choosing a fixed standardized radius and then
letting that radius tend to infinity, the conditional mass outside every
growing central window is negligible.  This is the tail statement used
below; no polynomial-loss division of a slowly growing Chernoff bound is
being invoked.

Finally,

\[
 {\binom{2m}{m-q}\over\binom{2m}{m}}
 =\prod_{j=0}^{q-1}{m-j\over m+j+1}
 =e^{-A^2+o(1)},
\tag{4.15}
\]

which supplies the factor \(e^{-A^2}\) in the second line of (4.7).
\(\square\)

### Theorem 4.3 (explicit fixed-block Gaussian deficit)

Under the hypotheses of Lemma 4.1 and (4.4),

\[
                         M_q^-\ge
 (\delta_4(A)-o(1))W,
\tag{4.16}
\]

where \(\delta_4(A)\) is (0.5).  In particular,
\(\delta_4(A)>0\) for every fixed \(A>0\).

#### Proof

Put \(z=(f-\mu_0)/\sigma_m\).  The normalized target and source
densities in Lemma 4.2 cross where

\[
 e^{-A^2}\phi(z+cA)=\phi(z),
\tag{4.17}
\]

namely at

\[
                         z_0=-A\left({1\over c}+{c\over2}\right).
\tag{4.18}
\]

The target density is larger on \(( -\infty,z_0)\).  Summing the positive
part in (4.3), using (4.7) and then letting the central-window radius tend
to infinity, gives

\[
\begin{aligned}
 \lim_{m\to\infty}{1\over W}\sum_f(T_{f,q}-V_f)_+
 &=e^{-A^2}\Phi(z_0+cA)-\Phi(z_0)\\
 &=e^{-A^2}\Phi\!\left[-A\left({1\over c}-{c\over2}\right)\right]
   -\Phi\!\left[-A\left({1\over c}+{c\over2}\right)\right].
\end{aligned}
\tag{4.19}
\]

This is positive because it is the integral of the strictly positive
density difference on a nonempty interval.  Lemma 4.1 proves (4.16).
\(\square\)

Complementation replaces full blocks in a lower target by empty blocks
in an upper target and proves the identical upper deficit.  Thus the
all-rank construction of Section 3, despite its exponentially small owner
leave, cannot satisfy `CPM` by subdivision, factor choice, or internal
chronology.

## 5. How much transverse chronology is necessary

Allow arbitrary windows, and call a start *transverse* if at least one of
its next \(q\) transitions swaps coordinates in different fixed
four-blocks.  Let \(B_q\) be the number of transverse starts.

### Theorem 5.1 (positive-density transverse-window requirement)

At \(q=\lfloor A\sqrt m\rfloor\), every owner-disjoint or owner-partial
cycle family satisfies

\[
                         M_q^-\ge
 (\delta_4(A)-o(1))W-B_q.
\tag{5.1}
\]

Consequently \(M_q^-=o(W)\) requires

\[
                         B_q\ge(\delta_4(A)-o(1))W.
\tag{5.2}
\]

#### Proof

The nontransverse starts retain \(F_4\), so their distinct images of type
\(f\) are at most \(V_f\).  The transverse starts can cover at most
\(B_q\) additional distinct targets in total.  For nonnegative numbers,

\[
                         (x-y-z)_+\ge(x-y)_+-z.
\tag{5.3}
\]

Apply (5.3) type by type and sum.  Theorem 4.3 gives (5.1), and (5.2)
follows.  Notice that deleting owners cannot improve the internal type
capacity, so no owner-leave correction is needed on the right side.
\(\square\)

### Corollary 5.2 (transverse-axis requirement)

Suppose a selected \(Q_r\)-packet \(P\) has \(t(P)\) cross-block axes and
uses a doubled-permutation factor: on each \(2r\)-cycle every direction
occurs once in each of two laps.  Then, for \(q\le r\),

\[
 \#\{\text{transverse starts in }P\}
 \le |P|\min\left\{1,{q\,t(P)\over r}\right\}.
\tag{5.4}
\]

Hence every such near-factor with \(o(W)\) lower holes must satisfy

\[
 \boxed{
 \sum_P |P|\min\left\{1,{q\,t(P)\over r}\right\}
 \ge(\delta_4(A)-o(1))W.}
\tag{5.5}
\]

#### Proof

On a \(2r\)-cycle, a fixed direction occurs twice.  Each occurrence lies
in at most \(q\) cyclic \(q\)-windows, so the union bound over the
\(t(P)\) transverse directions gives at most \(2qt(P)\) of the \(2r\)
starts.  Sum over the cycles in \(P\), cap the fraction by one, and apply
Theorem 5.1.  \(\square\)

In particular, if \(t(P)\le L\) for every packet and \(qL/r=o(1)\), the
left side of (5.5) is \(o(W)\).  Equivalently, the owner-weighted average
transverse dimension must be at least

\[
                         (\delta_4(A)-o(1)){r\over q}.
\tag{5.6}
\]

This is the exact quantitative reason a bounded number of local seams or
sorting comparators cannot repair the fixed mosaic.

## 6. The natural two-block promotion: seed and obstruction

For the particular mosaic (0.2), write its three cells as

\[
 E_c=\mathcal Q(\{u_c\},\{v_c\};\{e_c\}),
\tag{6.1}
\]

where

\[
\begin{array}{c|ccc}
c&e_c&u_c&v_c\\ \hline
1&23&1&4\\
2&12&4&3\\
3&24&3&1.
\end{array}
\tag{6.2}
\]

Thus every active edge in this particular mosaic contains the hub
coordinate \(2\).  This hub assertion is not claimed for every perfect
matching of \(J(4,2)\); it is a property of (0.2) and its coordinate
conjugates.

### Proposition 6.1 (a genuine transverse seed)

Align rank-one, rank-two, and rank-three local cells on the common swap
\(12\):

\[
\begin{aligned}
 L&=\mathcal Q(\varnothing,\{3,4\};\{12\}),\\
 M&=\mathcal Q(\{4\},\{3\};\{12\})=\{14,24\},\\
 U&=\mathcal Q(\{3,4\},\varnothing;\{12\}).
\end{aligned}
\tag{6.3}
\]

On disjoint blocks \(A,B\),

\[
                         (M_A\times M_B)\ \dot\cup\
                         (L_A\times U_B)
\tag{6.4}
\]

is exactly the \(Q_3\)

\[
 \mathcal Q\bigl(\{4_B\},\{3_A\};
          \{12_A,12_B,\{4_A,3_B\}\}\bigr).
\tag{6.5}
\]

#### Proof

The two \(Q_2\)'s in (6.4) have the identical old active matching
\(\{12_A,12_B\}\).  Their frozen statuses differ only by exchanging
\(4_A\) and \(3_B\).  Lemma 1.1 gives (6.5).  \(\square\)

So block occupancy is not an absolute geometric invariant.  The issue is
simultaneous disjoint promotion of all mosaic branches.

### Theorem 6.2 (nine-branch common-owner clique)

For \(c,d\in\{1,2,3\}\), the unique \(Q_3\) which contains
\(E_c^A\times E_d^B\) as its balanced facet, retains its two old axes,
and transfers one selected coordinate from \(A\) to \(B\), is

\[
 R_{cd}^{A\to B}
 =\mathcal Q\bigl(\{u_d^B\},\{v_c^A\};
   \{e_c^A,e_d^B,\{u_c^A,v_d^B\}\}\bigr).
\tag{6.6}
\]

All nine packets (6.6) contain the same owner

\[
                         \boxed{\{2_A\}\cup(B\setminus\{2_B\}).}
\tag{6.7}
\]

The nine reverse promotions similarly contain

\[
                         \boxed{(A\setminus\{2_A\})\cup\{2_B\}.}
\tag{6.8}
\]

Thus an owner-disjoint monotone promotion can use at most one of the nine
branches in each direction.  In particular it can retain and promote at
most \(1/9\) of the old balanced-sector owners in one fixed direction,
or at most \(2/9\) even if both directions are admitted.

#### Proof

Any \(Q_3\) containing the old \(Q_2\) facet must retain the axes
\(e_c^A,e_d^B\), by Lemma 1.1.  Outside those axes, the selected and
unselected coordinates in block \(A\) are \(u_c^A,v_c^A\), and in
block \(B\) they are \(u_d^B,v_d^B\).  A new axis decreasing the
\(A\)-occupancy and increasing the \(B\)-occupancy is therefore uniquely
\(\{u_c^A,v_d^B\}\), proving (6.6).

In (6.6), choose the hub \(2_A\) on \(e_c^A\), choose \(v_d^B\) on the
cross axis, and choose the nonhub endpoint of \(e_d^B\).  Together with
the frozen \(u_d^B\), the three selected coordinates in \(B\) are
exactly \(B\setminus\{2_B\}\), independently of \(c,d\).  This proves
(6.7).  The reverse calculation proves (6.8).

The nine old cells partition the \(36\) balanced owners into nine groups
of four.  At most one old group can be the balanced facet of a selected
forward promotion, and similarly in reverse, proving the fractions.
\(\square\)

The fractions refer only to a monotone layer which retains old cells as
facets.  A trade which cuts and retiles those cells is outside the theorem
and is the surviving route.

### Proposition 6.3 (odd aligned-cylinder obstruction)

Across \(b\) blocks, consider only the aligned cells \(L,M,U\) from
(6.3).  Middle cells are indexed by

\[
 (t_1,\ldots,t_b)\in\{0,1,2\}^b,
                         \qquad \sum_i t_i=b,
\tag{6.9}
\]

and every such base cell is a \(Q_b\) with the same internal matching.
Their number

\[
                         T_b=[x^b](1+x+x^2)^b
\tag{6.10}
\]

is odd.  Hence their union has \(2\)-adic valuation exactly \(b\) and
cannot be partitioned into \(Q_{b+1}\)'s.

#### Proof

The involution \(t_i\mapsto2-t_i\) preserves (6.9) and pairs every word
except \((1,\ldots,1)\).  Thus \(T_b\) is odd.  The base cells are
disjoint and each has \(2^b\) owners, so the union has size \(2^bT_b\),
not divisible by \(2^{b+1}\).  \(\square\)

Proposition 6.1 is therefore a real seed, but no coarsening confined to
this cylinder can promote every base packet even once.  Importing cells
from outside the cylinder may evade this parity cut; that is again a
cut-and-retile problem rather than monotone recursion.

## 7. The dyadic XOR-addressed translation mosaic

We now give a construction which genuinely changes frames on the owner
partition itself.  Assume

\[
                         G=\mathbb F_2^\ell,
                         \qquad |G|=2m=2^\ell,
                         \qquad \ell\ge4.
\tag{7.1}
\]

For \(a\ne0\), let \(M_a\) be the translation perfect matching (0.10).
For a middle owner \(X\), let \(\mathcal C_a(X)\) be its full
\(M_a\)-status cell: on every edge of \(M_a\), retain whether it is full,
empty, or split, and freely orient every split edge.  Thus

\[
                         \mathcal C_a(X)\cong Q_{D_a(X)},
\tag{7.2}
\]

where \(D_a(X)\) is the number of split \(M_a\)-edges.

Define the XOR hash

\[
                         \sigma(X)=\bigoplus_{x\in X}x\in G.
\tag{7.3}
\]

Let \(\tau:G\to G\) be a fixed-point-free involution and put

\[
                         a(s)=s+\tau(s).
\tag{7.4}
\]

### Theorem 7.1 (exact XOR cell partition)

The selected cells

\[
                         \mathscr C(X)
                         =\mathcal C_{a(\sigma(X))}(X)
\tag{7.5}
\]

are equal or disjoint and partition \(\binom Gm\) exactly into literal
variable-dimensional orientation cubes.

#### Proof

Put \(s=\sigma(X)\) and \(a=a(s)\).  Flipping one split edge
\(\{x,x+a\}\) changes the XOR by exactly \(a\).  Hence every
\(Y\in\mathcal C_a(X)\) satisfies

\[
                         \sigma(Y)\in\{s,s+a\}
                                      =\{s,\tau(s)\}.
\tag{7.6}
\]

Since \(a(\tau(s))=\tau(s)+s=a(s)\), the owner \(Y\) chooses the same
frame \(M_a\), and it plainly has the same full/empty/split status.
Therefore

\[
                         Y\in\mathscr C(X)
                         \quad\Longrightarrow\quad
                         \mathscr C(Y)=\mathscr C(X).
\tag{7.7}
\]

If two selected cells intersect, apply (7.7) to an owner in their
intersection to see that they are equal.  Every owner belongs to its own
selected cell, proving exhaustion.  \(\square\)

This is the crucial cell-stability identity.  The frame address is not a
frozen external selector: the hash changes inside the cell, but only
between the two endpoints of one \(\tau\)-edge, on which the selected
frame label is constant.

The partition is also complement-symmetric.  Since every coordinate of
\(G\) occurs in exactly \(2^{\ell-1}\) ground elements,

\[
                         \bigoplus_{x\in G}x=0,
                         \qquad
                         \sigma(G\setminus X)=\sigma(X).
\tag{7.8}
\]

Thus complementation preserves the selected frame and exchanges the full
and empty statuses of its cell.  No separate upper-frame mosaic is
needed.

## 8. A spanning family of hash labels

Write

\[
                         G=K\times\mathbb F_2,
                         \qquad K=\mathbb F_{2^{\ell-1}}.
\tag{8.1}
\]

Choose \(\alpha\in K\setminus\{0,1\}\) and define

\[
\begin{aligned}
 \tau(u,0)&=(\alpha u,1),\\
 \tau(v,1)&=(\alpha^{-1}v,0).
\end{aligned}
\tag{8.2}
\]

This is a fixed-point-free involution.  Its edge indexed by \(u\) has
label

\[
                         a_u=((1+\alpha)u,1).
\tag{8.3}
\]

As \(u\) ranges over \(K\), the labels are exactly

\[
                         \mathcal A=K\times\{1\}.
\tag{8.4}
\]

They span \(G\), and the union of the translation matchings
\(M_a\), \(a\in\mathcal A\), is the complete bipartite graph between
\(K\times\{0\}\) and \(K\times\{1\}\).

One must also check that these frame edges are genuinely active in
selected cells; occurrence of a hash label alone would not suffice.

### Lemma 8.1 (prescribed active edges)

Fix a \(\tau\)-edge \(\{s,s+a\}\), and let \(R\subseteq M_a\) have
\(|R|<m/2\).  There is a middle owner \(X\) such that

\[
                         \sigma(X)=s,
                         \qquad D_a(X)\ge m-2,
\tag{8.5}
\]

and every edge of \(R\) is split in \(X\).  Thus every prescribed
coordinate edge of every selected translation frame occurs actively in a
high-dimensional selected cell.

#### Proof

Choose a linear functional \(\lambda:G\to\mathbb F_2\) with

\[
                         \lambda(a)=1,
\tag{8.6}
\]

and, if \(s\ne0\), also \(\lambda(s)=1\).  The two requirements are
consistent: over \(\mathbb F_2\), either \(s=a\) or the two nonzero
vectors are independent.  Put \(H=\ker\lambda\).  Then \(|H|=m\),
\(H\) is a transversal of \(M_a\), and

\[
                         \bigoplus_{x\in H}x=0
\tag{8.7}
\]

because \(\dim H=\ell-1\ge3\).

If \(s=0\), take \(X=H\).  If \(s\ne0\), choose \(y\in H\) so that
neither the \(M_a\)-edge containing \(y\) nor the one containing
\(y+s\) lies in \(R\), and put

\[
                         X=(H\setminus\{y\})\cup\{y+s\}.
\tag{8.8}
\]

There are at most \(2|R|<m\) forbidden values of \(y\), so such a choice
exists.  Since \(\lambda(s)=1\), the new point is outside \(H\), and
\(|X|=m\).  Equation (8.7) gives \(\sigma(X)=s\).  Starting from the
full transversal \(H\), (8.8) changes the status of at most two
\(M_a\)-edges, none in \(R\).  Hence (8.5) holds.  By Theorem 7.1 this
is a selected cell of frame \(a\).  \(\square\)

It follows that the union of the active coordinate edges of the
variable-cell mosaic contains the connected Cayley graph generated by
\(\mathcal A\).  No nontrivial partition of the ground coordinates into
fixed blocks can contain all selected active edges.

## 9. Exact hash-fibre sizes

The hash distribution can be computed without an asymptotic theorem.
For \(0\le k\le2m\), let

\[
                         H_k(s)=\#\{X\in\tbinom Gk:\sigma(X)=s\}.
\tag{9.1}
\]

Put

\[
 B_k=[x^k](1-x^2)^m
 =\begin{cases}
   0,&k\text{ odd},\\
   (-1)^{k/2}\binom m{k/2},&k\text{ even}.
  \end{cases}
\tag{9.2}
\]

### Lemma 9.1 (exact XOR fibres)

\[
\boxed{
\begin{aligned}
 H_k(0)&={1\over2m}\left[\binom{2m}k+(2m-1)B_k\right],\\
 H_k(s)&={1\over2m}\left[\binom{2m}k-B_k\right]
                         \qquad(s\ne0).
\end{aligned}}
\tag{9.3}
\]

#### Proof

For a character \(\chi_y(s)=(-1)^{\langle y,s\rangle}\),

\[
 \sum_{|X|=k}\chi_y(\sigma(X))
 =[x^k]\prod_{g\in G}(1+x\chi_y(g)).
\tag{9.4}
\]

For \(y=0\), this is \(\binom{2m}k\).  For \(y\ne0\), exactly half of
the elements of \(G\) have each character sign, so (9.4) is
\([x^k](1+x)^m(1-x)^m=B_k\).  Fourier inversion on \(G\), together with

\[
 \sum_{y\ne0}\chi_y(s)=
 \begin{cases}2m-1,&s=0,\\-1,&s\ne0,
 \end{cases}
\tag{9.5}
\]

proves (9.3).  \(\square\)

For the middle layer, \(m\) is divisible by four under (7.1), so, with
\(C_m=\binom m{m/2}\),

\[
\begin{aligned}
 H_m(0)&={W+(2m-1)C_m\over2m},\\
 H_m(s)&={W-C_m\over2m}\qquad(s\ne0).
\end{aligned}
\tag{9.6}
\]

Thus every selected frame label, which owns two hash fibres, has owner
mass

\[
                         {W\over m}+O(C_m),
\tag{9.7}
\]

uniformly in the label.  Since \(mC_m/W=e^{-\Omega(m)}\), the frame masses
are exponentially close to equal.

For \(k=m\pm q\) with \(q=o(m)\), (9.3) says more: if \(q\) is odd the
target hash fibres are exactly equal, and if \(q\) is even their relative
discrepancy is \(e^{-\Omega(m)}\), uniformly in every fixed Gaussian
window.  Hence the XOR address introduces no positive-density hash-fibre
Hall cut.

## 10. Concentration, transverse subdivision, and the owner near-factor

For a fixed translation matching \(M_a\), under independent fair ground
bits the number \(D_a\) of split edges is \(\operatorname{Bin}(m,1/2)\).
Hoeffding's inequality gives

\[
                         \Pr(D_a<m/3)\le e^{-m/18}.
\tag{10.1}
\]

Since

\[
                         2^{-2m}\binom{2m}m\ge(2m+1)^{-1},
\tag{10.2}
\]

conditioning on the middle layer gives

\[
 \Pr_{X\in\binom Gm}(D_a(X)<m/3)
 \le(2m+1)e^{-m/18}.
\tag{10.3}
\]

The selected frame depends on \(\sigma(X)\), but a union bound over the
\(2m\) hash values gives

\[
 \#\{X:D_{a(\sigma(X))}(X)<m/3\}
 \le2m(2m+1)e^{-m/18}W.
\tag{10.4}
\]

Now fix any old partition of \(G\) into four-blocks.  For
\(a\in\mathcal A\), let \(i(a)\) be the number of edges of \(M_a\)
whose endpoints lie in one old four-block.  Every internal coordinate
pair has a unique nonzero difference, so

\[
                         \sum_{a\in\mathcal A}i(a)\le
 {m\over2}\binom42=3m.
\tag{10.5}
\]

Therefore fewer than \(36\) labels have \(i(a)>m/12\).  By (9.7), all
owners using those exceptional labels have total mass

\[
                         O(W/m)+e^{-\Omega(m)}W.
\tag{10.6}
\]

Discard the exceptional-label cells and the low-dimensional cells from
(10.4).  In every retained cell,

\[
 \#\{\text{split edges crossing old blocks}\}
 \ge D_a-i(a)\ge {m\over3}-{m\over12}={m\over4}.
\tag{10.7}
\]

### Theorem 10.1 (dyadic all-transverse owner near-factor)

For every \(2\le r\le m/4\), each retained cell can be partitioned into
literal \(Q_r\)-packets by choosing \(r\) of the transverse split axes
and fixing every other split orientation.  The resulting packets are
owner-disjoint, all of their axes cross the old four-block partition, and
their owner leave satisfies

\[
 \boxed{
 L\le O(W/m)+2m(2m+1)e^{-m/18}W
       =O(W/m)+e^{-\Omega(m)}W.}
\tag{10.8}
\]

Consequently, for every \(H=o(m)\),

\[
                         HL=o(W).
\tag{10.9}
\]

#### Proof

The selected variable cells partition the middle layer by Theorem 7.1.
The discarded cells contribute (10.4) and (10.6).  Equation (10.7)
allows the stated parallel subdivision of each remaining orientation
cube.  Subdivisions of disjoint cells remain disjoint.  Finally,
\(H/m=o(1)\) and the exponential term is negligible, proving (10.9).
\(\square\)

If the doubled-permutation compiler is installed, every nontrivial
window in every retained packet now sees only cross-block axes.  Thus the
left side of the necessary inequality (5.5) is \(W-L\): the dyadic
mosaic really clears the full-block Hall cut.

For example, one may take an admissible power of two

\[
                         m^{2/3}\le r<2m^{2/3},
                         \qquad
                         H=\left\lceil\sqrt{m\log m}\right\rceil.
\tag{10.10}
\]

Then \(H/\sqrt m\to\infty\), \(H/r\to0\), \(r=o(m)\), and (10.9)
holds.  Thus the owner geometry and the usual collar scale are
simultaneously compatible; only target selection remains.

The construction is an algebraic finite substitute for a transverse
sorting hierarchy.  On an affine two-flat the three nonzero translation
directions give its three pair frames, matching the local source of the
\(J(4,2)\) phenomenon.  What is not proved is a decomposition of the XOR
mosaic into a prescribed sequence of disjoint local four-point switches.

## 11. Exact lower/upper trace hashes

There is a useful exact ledger for the remaining chronological problem.
Fix one retained packet of frame label \(a\).  Write its active axes as

\[
                         e_j=\{x_j,x_j+a\},
                         \qquad 1\le j\le r,
\tag{11.1}
\]

and encode an owner by \(z\in\mathbb F_2^r\), choosing
\(x_j+z_ja\) on axis \(j\).  Absorb the frozen coordinates and the
canonical \(x_j\)'s into a constant \(\gamma\).  Then

\[
                         \sigma(X_z)
 =\gamma+\left(\sum_{j=1}^rz_j\right)a.
\tag{11.2}
\]

If a return-free \(q\)-window, with \(q\le r\), uses the axis set \(J\),
put

\[
                         x_J=\bigoplus_{j\in J}x_j.
\tag{11.3}
\]

Its lower intersection \(T^-\) and upper union \(T^+\) satisfy

\[
\boxed{
\begin{aligned}
 \sigma(T^-)
   &=\gamma+x_J+\left(\sum_{j\notin J}z_j\right)a,\\
 \sigma(T^+)
   &=\gamma+x_J+\left(q+\sum_{j\notin J}z_j\right)a.
\end{aligned}}
\tag{11.4}
\]

In particular,

\[
                         \sigma(T^+)=\sigma(T^-)+(q\bmod2)a.
\tag{11.5}
\]

#### Proof

The lower target is obtained from \(X_z\) by deleting the selected
endpoint \(x_j+z_ja\) on every \(j\in J\).  XOR this deletion with
(11.2); the \(z_j\)-terms on \(J\) cancel and give the first line of
(11.4).  The upper target instead adjoins the unselected endpoints
\(x_j+(1-z_j)a\); this adds \(x_J+(q+\sum_{j\in J}z_j)a\) to (11.2)
and proves the second line.  \(\square\)

Together, Lemma 9.1 and (11.4) prove that raw address-fibre sizes are
balanced on every protected rank and give the exact formula any
chronological hash cut must use.  They do not prove that a selected
factor distributes its emissions evenly among those fibres, and they do
not prove literal target disjointness: many different packets with the
correct target hash may still emit the same set.

### Theorem 11.1 (exact packet-local quotient-hash census)

Let

\[
                         V_a=G/\langle a\rangle
\tag{11.6}
\]

and write a bar for the quotient map.  The active matching edges of the
packet are indexed by distinct quotient points

\[
                         v_j=\overline{x_j}\in V_a,
                         \qquad 1\le j\le r.
\tag{11.7}
\]

For \(1\le q<r\) and \(w\in V_a\), put

\[
 K_{P,q}(w)
 =\#\left\{J\in\binom{[r]}q:
                  \bigoplus_{j\in J}v_j=w\right\}.
\tag{11.8}
\]

Fix one of the packet's two middle hash values, denoted \(s\), and an
exact target hash \(t\in G\).  The number of pairs \((X,J)\), where
\(\sigma(X)=s\), \(|J|=q\), and the lower \(J\)-face below \(X\) has
hash \(t\), is

\[
                         2^{r-2}
 K_{P,q}(\bar s+\bar t).
\tag{11.9}
\]

The number of distinct lower target faces of exact hash \(t\) in the
packet is

\[
                         2^{r-q-1}
 K_{P,q}(\bar s+\bar t),
\tag{11.10}
\]

and each is incident with exactly \(2^{q-1}\) sources on the hash shore
\(s\).  The upper formulas are identical; only the lift of \(t\) inside
its \(a\)-coset is shifted by \((q\bmod2)a\).

#### Proof

Modulo \(\langle a\rangle\), (11.4) becomes

\[
                         \bar t=\bar s+
                         \bigoplus_{j\in J}v_j.
\tag{11.11}
\]

For a support \(J\) satisfying (11.11), the exact lift \(t\) fixes the
parity of the \(r-q\) outside orientations.  There are
\(2^{r-q-1}\) choices.  The condition \(\sigma(X)=s\) then fixes the
parity of the \(q\) inside orientations, leaving \(2^{q-1}\) choices.
Their product is \(2^{r-2}\), proving (11.9).  The lower face forgets
the inside orientations, so only the first factor counts distinct
targets, proving (11.10).  Different supports \(J\) have different sets
of empty active matching edges and hence cannot define the same literal
face.  The upper claim follows from the second line of (11.4).
\(\square\)

The census identifies a genuine packet-local restriction.  At depth one,

\[
                         K_{P,1}(w)=
                         \mathbf1_{\{w\in\{v_1,\ldots,v_r\}\}},
\tag{11.12}
\]

so one packet can reach only the two exact lifts of its \(r\) active
quotient labels.  More generally, a hash quotient with
\(K_{P,q}(w)=0\) is unreachable by every phase choice in that packet.

Under the uniform catalogue of all cube translations and axis
permutations of one fixed return-free factor, every \(q\)-support occurs
equally often at every fixed physical source.  Its multiplicity in the
catalogue is

\[
                         2^r q!(r-q)!.
\tag{11.13}
\]

Consequently, after summing over all owners on both middle hash shores,
the mean number of depth-\(q\) emissions of one packet to the exact hash
\(t\) is

\[
                         {2^{r-1}over\binom rq}
                         K_{P,q}(\bar s+\bar t).
\tag{11.14}
\]

Thus affine conjugation uniformizes the choice among supports but cannot
alter the subset-XOR spectrum \(K_{P,q}\).  In the packet aggregate, cube
translations balance the two lifts of a quotient point, but at a fixed
physical owner and support the literal target is forced.  Only
direction-order permutations can redistribute mass among quotient
points.  Proving raw target-fibre balance in Lemma 9.1 is therefore not
enough.

### Proposition 11.2 (mirror and translation couplings do not close the gate)

Let \(F\) be a successor permutation on a packet.

1. Reversal preserves every signed depth-\(q\) target multiset:

   \[
   L_q^{F^{-1}}(X)=L_q^F(F^{-q}X),
   \qquad
   U_q^{F^{-1}}(X)=U_q^F(F^{-q}X).
   \tag{11.15}
   \]

   Hence reversal leaves the selected target incidence vector unchanged.
   Under an aligned isomorphism, an inverse-coupled copy has precisely the
   transported same vector; reversal supplies no new negative covariance.
2. Ground complementation only exchanges the two signs.  If
   \(F^C=CFC\), then

   \[
                         U_q^{F^C}(CX)=C(L_q^F(X)).
   \tag{11.16}
   \]

   It synchronizes lower and upper profiles but, by itself, introduces no
   new same-sign choice or negative covariance.
3. For a doubled-permutation \(C_{2r}\)-factor, the cube antipode \(A\)
   satisfies

   \[
                         F^r=A,
                         \qquad AF=FA.
   \tag{11.17}
   \]

   Therefore an antipodal inverse rule \(AFA=F^{-1}\) would force
   \(F=F^{-1}\), impossible on cycles of length \(2r>2\).
4. A ground translation by \(h\in G\) changes the hash of a \(k\)-set by

   \[
                         \sigma(T+h)=\sigma(T)+(k\bmod2)h.
   \tag{11.18}
   \]

   Since \(m\) is even, translations can mix target hash fibres at odd
   protected depths but preserve every hash fibre at even depths.

#### Proof

For (11.15), reverse the list of the same \(q+1\) states and reindex the
start by \(F^{-q}\).  Intersections and unions are order-independent.
Equation (11.16) is De Morgan's law applied state by state.  In a
doubled-permutation cycle, the first \(r\) transitions flip every cube
axis exactly once, proving (11.17).  Finally, XORing \(h\) once for every
member of a \(k\)-set gives (11.18).  \(\square\)

These statements close the most direct symmetry completion.  Inverse
slabs have the same target multiset, complement slabs merely exchange
signs, and translations do not move even-depth hash defects.  Any
positive chronological theorem must coordinate direction orders across
different packets so that their subset-XOR spectra and their literal
within-fibre targets complement one another.

A necessary hash-level consequence of literal `CPM` is the following.
Write \(\varepsilon=-1\) for lower targets and \(\varepsilon=+1\) for
upper targets.  If

\[
 Z_{q,t}^{\varepsilon,\mathrm{hash}}
 =\sum_{\substack{T:\,\sigma(T)=t}}Z_{q,\varepsilon,T},
\tag{11.19}
\]

then

\[
 \sum_{t\in G}
 \left(H_{m+\varepsilon q}(t)
       -Z_{q,t}^{\varepsilon,\mathrm{hash}}\right)_+=o(W)
\tag{11.20}
\]

must hold in aggregate over the protected signed depths.  Equations
(11.8)--(11.14) give the exact finite packet data for this preliminary
transport problem.  Even (11.20) is weaker than literal `CPM`, because it
does not prevent collisions between distinct targets in the same hash
fibre.

There is one exact correlated choice which clears this preliminary gate
on every odd depth.

### Theorem 11.3 (translation-equivariant odd-depth hash balance)

Choose the old four-blocks to be the cosets of a fixed two-dimensional
subspace of \(G\).  Assume \(2\le r\le m/4\) is a certified literal
context-array factor dimension and \(H<r\) lies in its return-free trace
range.  Choose the exceptional-label, low-dimensional, and stabilizer
quarantines translation-invariantly.  After the resulting additional
discard of \(e^{-\Omega(m)}W\) owners, the all-transverse packet
near-factor and one legal factor state in every packet can be chosen
equivariantly under all ground translations.  Consequently, at every
odd protected depth \(q\le H\),

\[
                         Z_{q,t}^{\varepsilon,\mathrm{hash}}
                         ={S\over2m}
                         \qquad(t\in G,
                                \ \varepsilon\in\{-1,+1\}).
\tag{11.21}
\]

In particular, the aggregate odd-depth hash deficit is at most

\[
 \sum_{\substack{q\le H\\q\text{ odd}}}
 \sum_{\varepsilon,t}
 \left(H_{m+\varepsilon q}(t)
       -Z_{q,t}^{\varepsilon,\mathrm{hash}}\right)_+
 \le 2HL=o(W).
\tag{11.22}
\]

#### Proof

Ground translation preserves the XOR of a middle owner because \(m\) is
even.  It therefore preserves its hash-addressed frame, and it maps
selected status cells to selected status cells.  Translation by the
frame label \(a\) fixes every \(M_a\)-status cell, since it merely swaps
the two endpoints of each matching edge.

We first remove cells with any larger translation stabilizer.  Fix
\(h\notin\{0,a\}\).  On the \(m\) edges of \(M_a\), translation by
\(h\) has \(m/2\) two-edge orbits.  An \(h\)-stable status assigns the
same type to both edges of an orbit.  The empty, split, and full choices
contribute respectively

\[
                         1,\qquad4x^2,\qquad x^4
\tag{11.23}
\]

to the owner-rank generating polynomial.  Hence all middle owners in
such cells are at most

\[
                         [x^m](1+4x^2+x^4)^{m/2}
                         \le6^{m/2}.
\tag{11.24}
\]

There are fewer than \(2m^2\) pairs \((a,h)\).  Since
\(W\ge4^m/(2m+1)\), their union has size \(e^{-\Omega(m)}W\).
Every remaining cell has translation stabilizer exactly
\(\langle a\rangle\).

Choose packet subdivisions on representatives of the remaining cell
orbits and transport them by translation.  Because \(D-r>0\), translation
by \(a\) complements at least one frozen split orientation and therefore
pairs, rather than fixes, the resulting \(Q_r\)-subpackets.  Thus the
translation action on packets is free.  Choose a legal factor on every
packet-orbit representative and transport it by conjugacy.  The resulting
literal target loads satisfy

\[
                         Z_{q,\varepsilon}(T+h)
                         =Z_{q,\varepsilon}(T)
                         \qquad(h\in G).
\tag{11.25}
\]

If \(q\) is odd, the target rank \(m\pm q\) is odd.  A set of odd size
cannot be invariant under a nonzero translation, whose coordinate orbits
are pairs.  Every target translation orbit therefore has size \(2m\).
By (11.18), its hashes run through all of \(G\) exactly once.  The common
load on each target orbit then contributes equally to every hash, and
the total occurrence mass \(S\) proves (11.21).

Lemma 9.1 gives
\(H_{m\pm q}(t)=N_q/(2m)\) exactly at odd \(q\).  Summing the positive
hash deficit gives \(2(N_q-S)_+\le2L\) at that depth.  Summation over at
most \(H\) depths and (10.9) proves (11.22).  \(\square\)

For an odd depth, translation equivariance also reduces the floor energy
exactly to target-translation orbits.  If \(z_O\) is the common load on
the orbit \(O\), then

\[
                         Q_{q,\varepsilon}
 =2m\sum_O(z_O-c_q)(z_O-c_q-1).
\tag{11.26}
\]

This is an integral reduction by a factor \(2m\), not a solution:
translation symmetry supplies no negative covariance between the orbit
loads.  At even depths it does not even mix hash fibres, by (11.18).

The even-depth hash issue can nevertheless be cleared throughout the
mesoscopic and Gaussian range by choosing spectrally balanced active
axes and then making one common random affine-conjugate choice per
packet.  The randomness is used only for a finite existence proof; the
result is one deterministic integral factor choice.

### Theorem 11.4 (integral hash-bin saturation above logarithmic depth)

For all sufficiently large dyadic instances satisfying (7.1), take

\[
                         r=m/4,
                         \qquad
                         q_0=\lceil40\log m\rceil,
                         \qquad
                         q_0\le H<r,
                         \qquad H/r\longrightarrow0,
\tag{11.27}
\]

where the logarithm is natural.  Assume explicitly that this dyadic
\(r=m/4\) belongs to the certified context-array dimension family and
that its literal return-free, two-sided trace-injectivity theorem holds
through \(H\).  After the owner discard already allowed in Theorem 10.1
and an additional \(e^{-\Omega(m)}W\) cell discard, the packets and one
common legal affine factor conjugate in every packet can be chosen so
that, simultaneously for

\[
                         q_0\le q\le H,
                         \quad t\in G,
                         \quad\varepsilon\in\{-1,+1\},
\tag{11.28}
\]

one has

\[
 \boxed{
 Z_{q,t}^{\varepsilon,\mathrm{hash}}
 \ge H_{m+\varepsilon q}(t).}
\tag{11.29}
\]

Thus the aggregate hash-bin occurrence deficit in (11.20) is exactly zero
throughout (11.28), for one simultaneous integral factor choice.  In
particular it vanishes at every fixed Gaussian depth
\(q=\lfloor A\sqrt m\rfloor\), \(A>0\).
Separately for each protected depth and sign, all occurrences emitted by
packets descending from the same original XOR-status cell are literal
distinct; any remaining collision is between different status cells.

#### Proof

Fix a nonexceptional frame \(a\) and identify its \(m\) matching edges
with \(V_a=G/\langle a\rangle\).  Under independent fair ground bits, the
split indicators of these edges are independent Bernoulli variables of
mean \(1/2\).  For every nontrivial character \(\chi\) of \(V_a\), each
of its two sign shores has \(m/2\) edge labels.  Chernoff bounds, followed
by a union bound over fewer than \(m^2\) pairs \((a,\chi)\), show that all
but \(e^{-\Omega(m)}W\) middle owners lie in selected cells whose
split-label set \(\mathcal S\) satisfies

\[
 {5m\over12}\le|\mathcal S|\le{7m\over12},
 \qquad
 {5m\over24}\le
 |\mathcal S\cap\chi^{-1}(\pm1)|
 \le{7m\over24}
\tag{11.30}
\]

for every nontrivial \(\chi\).  This is a whole-cell condition because
the split-label set is constant on a status cell.  Passing from all
subsets to the middle layer costs only a polynomial factor, by (10.2),
and is absorbed by the exponential bound.

For a nonexceptional frame, at most \(m/12\) matching edges lie inside
the old four-blocks.  Remove them from \(\mathcal S\), obtaining a
transverse pool \(P_{\mathcal S}\).  Equations (11.30) give

\[
 |P_{\mathcal S}|\ge m/3,
 \qquad
 |P_{\mathcal S}\cap\chi^{-1}(\pm1)|\ge m/8.
\tag{11.31}
\]

Hence each sign occupies at least a \(3/14\) fraction of
\(P_{\mathcal S}\).  A uniform \(r=m/4\) subset of
\(P_{\mathcal S}\) has at least \(r/10\) labels on
each sign shore of every nontrivial character, simultaneously with
positive probability: for one character this is a hypergeometric
Chernoff bound \(e^{-\Omega(r)}\), and there are only \(m-1\) characters.
Choose one such active set

\[
                         A_P=\{v_1,\ldots,v_r\}
\tag{11.32}
\]

in every retained cell and use the parallel subdivision into
\(Q_r\)-packets.  Every chosen axis is transverse.

Every frozen spectator orientation survives all packet trajectories.
Hence the certified within-packet trace injectivity also separates traces
from different parallel subpackets in the same selected cell, proving the
within-cell assertion in the theorem statement.

We next audit its subset-XOR spectrum.  For a nontrivial \(\chi\), let
\(r_+,r_-\) be its two sign counts on \(A_P\) and define

\[
 k_j(\chi)=
 { [z^j](1+z)^{r_+}(1-z)^{r_-}\over\binom rj}.
\tag{11.33}
\]

The logarithmic derivative of the numerator gives the exact recurrence

\[
 k_{j+1}
 ={r_+-r_-\over r-j}k_j
 -{j\over r-j}k_{j-1}.
\tag{11.34}
\]

By (11.32), \(|r_+-r_-|\le4r/5\).  Put \(\lambda=9/10\).  Starting
from \(k_0=1\), \(|k_1|\le4/5\), induction in (11.34) gives

\[
                         |k_j(\chi)|\le\lambda^j
                         \qquad(0\le j\le H)
\tag{11.35}
\]

for all large \(m\).  Indeed, after inserting the two preceding induction
bounds, the multiplier relative to \(\lambda^{j+1}\) is at most

\[
 {4r/5\over\lambda(r-H)}
 +{H\over\lambda^2(r-H)}<1,
\tag{11.36}
\]

because \(H/r\to0\).

Fourier inversion on \(V_a\), applied to (11.8), now yields uniformly in
the packet and \(w\in V_a\),

\[
 K_{P,q}(w)
 ={1\over m}\binom rq
  \left(1+O(m\lambda^q)\right).
\tag{11.37}
\]

For \(q\ge q_0\), the relative error in (11.37) is
\(o(q^2/m)\).  The exact packet census (11.14) therefore says that a
uniform affine factor conjugate has mean exact-hash emission

\[
                         {2^r\over2m}
                         \left(1+o(q^2/m)\right)
\tag{11.38}
\]

on each sign.  Summed over the \(S/2^r\) packets, this is
\(S/(2m)(1+o(q^2/m))\).

On the demand side, Lemma 9.1 gives

\[
                         H_{m\pm q}(t)
 ={N_q\over2m}\left(1+O(e^{-\Omega(m)})\right)
\tag{11.39}
\]

uniformly in \(t\), while

\[
 {W\over N_q}
 =\exp\left({q^2\over m}+O\left({q^3\over m^2}\right)\right),
 \qquad
                         {S\over W}=1-O(1/m).
\tag{11.40}
\]

Equations (11.38)--(11.40) leave a positive margin in every hash bin,
uniformly over (11.28).  The smallest margin, at \(q=q_0\), is
\(\Omega(Wq_0^2/m^2)\).

Finally choose the affine conjugate independently and uniformly in every
packet.  For a fixed triple \((q,t,\varepsilon)\), packet contributions
lie in \([0,2^r]\).  Hoeffding's inequality bounds failure to meet demand
by

\[
 \exp\left[-\Omega\left(
       {Wq_0^4\over m^4 2^r}
                    \right)\right].
\tag{11.41}
\]

Since \(r=m/4\), this dominates a union bound over fewer than
\(4mH\) triples.  Therefore one deterministic common choice avoids every
failure and proves (11.29).  \(\square\)

The logarithmic cutoff is genuine in this proof.  At \(q=1\), (11.12)
shows that a packet reaches only its \(r\) active quotient labels, and the
Fourier error in (11.37) is not small.  Depths
\(q<40\log m\), especially depth one, still require a separate
cross-packet discrepancy argument.  More importantly, (11.29) controls
only total occurrence supply in each hash fibre.  It permits all that
supply to collide on a small subset of literal targets, so literal `CPM`
remains open even on the interval (11.28).

## 12A. Deterministic deployment of the full local catalogue

The abundance of parallel subpackets inside one high-dimensional selected
cell can be used chronologically, without random independent choices.
This removes all within-cell collisions and realizes an almost perfectly
uniform catalogue of active-axis sets and affine factor conjugates.

Fix one retained selected cell \(\mathscr C\cong Q_D\).  Let \(E_\times\)
be its set of split axes crossing the old four-block partition.  By
(10.7),

\[
                         D\ge m/3,
                         \qquad |E_\times|\ge m/4.
\tag{12A.1}
\]

Let \(r\) be an admissible factor dimension satisfying

\[
                         r\log m=o(m),
\tag{12A.2}
\]

and let the established factor on \(Q_r\) be return-free through
\(H<r\), with literal rank-\((m-q)\) and rank-\((m+q)\) lower/upper
traces that are injective throughout that range.  Put

\[
                         \ell=
 \left\lceil4r\log_2(2em)\right\rceil.
\tag{12A.3}
\]

For all sufficiently large \(m\), \(\ell+r<D\).  Choose \(\ell\)
selector axes \(S\) from the split axes of the cell.  Even if all of them
belong to \(E_\times\), the remaining allowed set

\[
                         E'=E_\times\setminus S
\tag{12A.4}
\]

has \(|E'|\ge m/5>r\).

Consider the complete local catalogue

\[
 \mathfrak C
 =\left\{(R,\eta,\pi):
 R\in\binom{E'}r,
 \ \eta\in\mathbb F_2^r,
 \ \pi\in S_r\right\}.
\tag{12A.5}
\]

Here \(R\) is the physical active-axis set, while \((\eta,\pi)\) is a
cube phase translation and direction permutation of the certified base
factor.  Its size \(M=|\mathfrak C|\) satisfies

\[
 M=\binom{|E'|}r2^rr!
 \le(2e|E'|)^r
 \le(2em)^r,
 \qquad
                         {M\over2^\ell}\le M^{-3}.
\tag{12A.6}
\]

### Theorem 12A.1 (selector-array chronological symmetrization)

The cell \(\mathscr C\) has an exact partition into physical
\(Q_r\)-packets, with one complete legal factor state installed in every
packet, such that:

1. every active packet axis belongs to \(E_\times\);
2. separately for every depth \(q\le H\) and each sign, all target
   occurrences emitted by the whole cell are pairwise distinct;
3. the frequencies of the catalogue labels in (12A.5), measured by owner
   mass, differ from the uniform distribution by total variation at most

   \[
                            {M\over2^{\ell+1}};
   \tag{12A.7}
   \]

4. after forgetting the phase and order labels, the induced normalized
   owner-occurrence distribution of abstract \(q\)-supports differs by
   the same error from the uniform distribution on \(\binom{E'}q\),
   simultaneously for every \(q\le H\).

#### Proof

Fix the orientations of the selector axes \(S\).  This partitions the
cell into \(2^\ell\) equal branches, each a \(Q_{D-\ell}\).  Assign the
\(M\) catalogue labels to the branches as evenly as possible, so every
label is used either

\[
                         \left\lfloor{2^\ell\over M}\right\rfloor
 \quad\text{or}\quad
                         \left\lceil{2^\ell\over M}\right\rceil
\tag{12A.8}
\]

times.  In a branch assigned \((R,\eta,\pi)\), partition its cube into
parallel \(Q_r\)-subcubes with active set \(R\), by fixing every other
orientation.  Install the \((\eta,\pi)\)-conjugate factor in all those
subcubes.  This is an exact owner partition and every active axis lies in
\(E'\subseteq E_\times\).

Within one \(Q_r\)-subcube, signed trace injectivity is the certified
factor theorem.  Two different parallel subcubes in one selector branch
differ on a fixed split axis outside \(R\); its selected endpoint survives
both every intersection and every union.  Two different selector
branches differ on an axis in \(S\), which survives for the same reason.
Thus no two target occurrences emitted by the cell coincide, proving
Item 2.

All selector branches have the same owner mass.  From (12A.8), the
frequency error of each catalogue label is at most \(2^{-\ell}\); summing
and dividing by two gives (12A.7).

Finally, under the uniform catalogue a fixed \(q\)-set
\(J\subseteq E'\) is contained in
\(\binom{|E'|-q}{r-q}\) choices of \(R\), and the uniform direction
permutations make every \(q\)-support inside \(R\) equally frequent.
The identity

\[
 {\binom{|E'|-q}{r-q}\over
  \binom{|E'|}r\binom rq}
 ={1\over\binom{|E'|}q}
\tag{12A.9}
\]

proves Item 4.  \(\square\)

For example, take an admissible power of two
\(m^{2/3}\le r<2m^{2/3}\) and the \(H\) in (10.10).  Then
\(r\log m=o(m)\), \(H/r\to0\), and Theorem 12A.1 applies in every
retained cell without any additional owner leave.

This is an actual deterministic chronological deployment, not an option
union or an independent random choice.  It proves that packet-option
scarcity and within-cell collisions are not the remaining obstruction.
The unresolved collisions are exclusively between different selected
XOR-status cells.  Moreover, their quotient-hash marginals are governed
by the \(q\)-subset XOR spectrum of the larger allowed set \(E'\); uniform
catalogue deployment does not by itself make that spectrum uniform.

## 12. An exact sufficient CPM gate

Let \(\mathcal P\) be the owner-disjoint dyadic near-factor from Theorem
10.1, with covered owner mass

\[
                         S=W-L.
\tag{12.1}
\]

Assume that \(r\) is an admissible compiler dimension (in particular, the
established exact doubled-permutation/context-array factor exists on
\(Q_r\)).  Fix a protected range \(1\le H<r\) and choose one complete
legal factor state in each packet.  The strict inequality is the safe
cyclic return-free range.  Theorem 10.1 by itself is only an owner-packet
statement for arbitrary \(r\); this additional factor hypothesis is
essential.

At signed depth \(a=(q,\varepsilon)\), let \(Z_{a,T}\) be the resulting
literal target load and put

\[
                         N_q=\binom{2m}{m-q},
                         \qquad c_a=\left\lfloor{S\over N_q}\right\rfloor,
\tag{12.2}
\]

\[
                         Q_a=\sum_T
 (Z_{a,T}-c_a)(Z_{a,T}-c_a-1).
\tag{12.3}
\]

Every summand in (12.3) is a nonnegative even integer.  The exact
floor-balanced inequality gives

\[
 \sum_{q\le H,\varepsilon}
        \#\{T:Z_{q,\varepsilon,T}=0\}
 \le 2HL+{1\over2}\sum_{q\le H,\varepsilon}Q_{q,\varepsilon}.
\tag{12.4}
\]

Theorem 10.1 proves that the first term is \(o(W)\).  Therefore the
following is a rigorous sufficient target statement for this mosaic:

\[
 \boxed{
 \text{Choose one common all-depth factor state in every packet so that}
 \quad
 \sum_{q\le H,\varepsilon}Q_{q,\varepsilon}=o(W).}
\tag{12.5}
\]

Potential path abundance, target-side hash-fibre balance, the connected
support of the untrimmed frame atlas, and the fact that every protected
window in the retained packets is transverse do not imply (12.5).
Independent packet choices generally retain linear floor
energy; (12.5) needs a linear negative overlap covariance or an exact
augmenting circulation.  Separate choices for different depths or signs
do not define one successor factor and are inadmissible.  Conversely,
small literal hole mass does not force \(Q=o(W)\), so (12.5) is not
claimed necessary.

## 13. Audited boundary

Proved here:

* an exact all-rank fixed-quartet \(Q_r\) owner near-factor;
* the explicit Gaussian full-block deficit (0.5), including its variance,
  mean-shift, and normalization constants;
* the positive-density transverse-window requirement (5.5);
* the exact uniform-tiling divisibility and comparator-axis obstructions;
* a valid two-block transverse seed, the corrected nine-branch
  common-owner obstruction for the specific star mosaic, and the odd
  aligned-cylinder obstruction;
* an exact XOR-addressed variable-cube partition for dyadic ground sets;
* an explicit spanning-label involution and prescribed-active-edge
  realization;
* an all-transverse \(Q_r\) owner near-factor with leave
  \(O(W/m)+e^{-\Omega(m)}W\);
* exact XOR fibre counts at every rank and the complete lower/upper
  target-hash ledger (11.4);
* the exact packet-local subset-XOR census (11.8)--(11.14);
* the reversal, complement, antipodal-inverse, and translation-parity
  symmetry audits;
* a translation-equivariant integral choice with exact odd-depth hash
  balance;
* under the certified literal context-array factor hypothesis, one
  simultaneous integral factor choice saturating every hash bin on both
  signs for \(40\log m\le q\le H\); and
* under that same hypothesis, deterministic full-catalogue deployment
  with literal trace injectivity throughout each individual selected
  status cell.

Not proved here:

* a literal all-depth factor choice satisfying (12.5);
* `CPM` for the XOR mosaic by any weaker non-floor-balanced route;
* control of the short-depth \(q<40\log m\) subset-XOR discrepancy by the
  same factor choice;
* suppression of literal collisions between different selected status
  cells, even when their aggregate hash bins are saturated;
* a conversion of the XOR mosaic into a prescribed finite sequence of
  local `J(4,2)` switches;
* a non-dyadic version with the same exact cell-stability identity; or
* the coefficient-one theorem.

Thus the fixed-block lane and the analyzed old-facet-preserving star
hierarchy are rigorously closed.
For the dyadic transverse mosaic, owner packing, transverse chronology,
within-cell injectivity, and all mesoscopic/Gaussian hash-bin capacities
are proved.  The unresolved literal problem is cross-cell collision
suppression (plus the short-depth hash discrepancy if one insists on the
same construction at every depth).  Equation (12.5) is an explicit
sufficient colored target-anticorrelation gate, not an equivalent
reformulation of `CPM`.  This is a strictly smaller and correctly integral
boundary than the original fixed-product compiler problem.

The decisive constructive steps were independently audited.  One audit
checked the translation-stabilizer quarantine, normalized Krawtchouk
recurrence, logarithmic cutoff, supply--demand margin, and Hoeffding
exponent in Theorems 11.3--11.4.  A separate audit checked selector
cardinality, total variation, literal spectator separation, and the
support pushforward in Theorem 12A.1.  Neither audit found a mathematical
defect after the factor hypotheses and quantifier scopes stated above
were made explicit.
