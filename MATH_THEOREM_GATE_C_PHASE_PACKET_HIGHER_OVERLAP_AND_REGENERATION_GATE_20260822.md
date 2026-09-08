# Gate C: phase-packet higher overlaps and the exact regeneration gate

**Status (2026-08-22).**  The positional enumeration, the rooted
all-overlap bound, and the product-residual concentration theorem below are
proved.  They do **not** prove a near-perfect phase-packet matching.  Their
logical content is exact:

1. regularity and the pair bound
   \(\Delta _2/D=2/[b(b+1)]\) do not constitute a growing-rank matching
   theorem;
2. the actual phase-packet orbit has much stronger all-order local
   structure than that pair bound records;
3. this structure gives product-residual regeneration down to every density
   \(\rho\) with \(b\rho\to\infty\); but
4. a matching residual is not a product residual.  The remaining matching
   assertion is a correlated-regeneration theorem (or a one-shot
   edge-colouring/absorption theorem), not another time-zero codegree count.

This note is self-contained.  It uses labelled packets for enumeration and
then passes explicitly to the simple support hypergraph.  No
fixed-uniformity nibble theorem is invoked.

Throughout, \(b\ge5\) is odd,

\[
 q=b+1,\qquad \Omega=[2b],\qquad
 V={\Omega\choose b},\qquad W=|V|.
\tag{0.1}
\]

## 1. Packet labels, supports, and their metric

A packet label is a pair consisting of an omitted coordinate \(v\in\Omega\)
and a cyclic word with marked origin

\[
 z=(z_0,z_1,\ldots,z_{2b-2})
\tag{1.1}
\]

on \(\Omega\setminus\{v\}\).  Put \(N=2b-1\) and

\[
 C_i(z)=\{z_i,z_{i+1},\ldots,z_{i+b-1}\},
 \qquad 0\le i\le b,
\tag{1.2}
\]

where subscripts of \(z\) are read modulo \(N\).  The packet support is

\[
                         P(z)=\{C_0(z),\ldots,C_b(z)\}.
\tag{1.3}
\]

There are \((2b)!\) labels.  The middle-layer Johnson distance satisfies

\[
 d_J(C_i,C_j)=
 \begin{cases}
 |i-j|,&\{i,j\}\ne\{0,b\},\\
 b-1,&\{i,j\}=\{0,b\}.
 \end{cases}
\tag{1.4}
\]

Thus the distance-one graph induced by a support is the path
\(C_0C_1\cdots C_b\).

### Lemma 1.1 (support multiplicity two)

Every simple packet support has exactly two labels, corresponding to the two
orientations of the path in (1.4).  Consequently the simple packet
hypergraph is \(q\)-uniform and regular of degree

\[
                         d={q(b!)^2\over2}.
\tag{1.5}
\]

#### Proof

The support determines its distance-one path, up to reversal.  In one
orientation, the transition \(C_{i-1}\to C_i\) determines the removed
coordinate \(z_{i-1}\) and the entered coordinate \(z_{i+b-1}\).  The
first \(b\) removals recover \(z_0,\ldots,z_{b-1}\), the first \(b-1\)
entries recover \(z_b,\ldots,z_{2b-2}\), and the final entry repeats
\(z_0\).  The unique coordinate outside
\(C_0\cup C_b\) is \(v\).  Hence an oriented support has one label and an
unoriented support has two.

For a fixed target and a fixed position, its \(b\) coordinates can be
ordered in \(b!\) ways; the other \(b\) coordinates can be assigned to the
omitted position and ordered outside slots in another \(b!\) ways.  There
are \(q\) positions.  Labelled degree is therefore \(q(b!)^2\), and
division by two proves (1.5). \(\square\)

## 2. Exact prescribed-position tuple counts

Let

\[
 K=\{k_0<k_1<\cdots<k_{t-1}\}\subseteq\{0,1,\ldots,b\},
 \qquad g_j=k_j-k_{j-1}\quad(1\le j<t),
\tag{2.1}
\]

and write \(S=k_{t-1}-k_0\).  Suppose distinct prescribed targets
\(A_0,\ldots,A_{t-1}\) are compatible with the assignments
\(C_{k_j}=A_j\).  Let \(L(K)\) be the number of packet labels realizing
all these assignments.

### Theorem 2.1 (exact tuple-label formula)

For one prescribed target, \(L(K)=(b!)^2\).  For \(t\ge2\),

\[
 \boxed{
 L(K)=
 \begin{cases}
 \displaystyle
 \left((b-S)!\prod_{j=1}^{t-1}g_j!\right)^2,&S<b,\\[3mm]
 \displaystyle
 {\prod_{j=1}^{t-1}(g_j!)^2\over g_1g_{t-1}},&S=b.
 \end{cases}}
\tag{2.2}
\]

If the assignments are incompatible, their label count is zero.

#### Proof

Assume first \(S<b\).  Moving between consecutive prescribed starts fixes
the set, but not the internal order, of each removed block of size \(g_j\)
and each entered block of the same size.  These blocks contribute
\(\prod g_j!\) on each side.  The \(b-S\) initial-window coordinates that
never cross a prescribed boundary may be ordered arbitrarily.  On the
outside, the \(b-S\) coordinates not yet entered may be assigned to the
omitted coordinate and the remaining cyclic slots in \((b-S)!\) ways.
This gives the first line of (2.2).

If \(S=b\), necessarily \(k_0=0,k_{t-1}=b\).  The common endpoint
coordinate \(C_0\cap C_b=\{z_0\}\) is fixed.  In the first transition
block, it is the first removed coordinate; in the last transition block,
it is the last entered coordinate.  Hence those two sides contribute
\((g_1-1)!g_1!\) and \(g_{t-1}!(g_{t-1}-1)!\), respectively.  Every
interior block contributes \((g_j!)^2\).  Their product is the second line
of (2.2).  The one-target count is the argument used in Lemma 1.1.
\(\square\)

Formula (2.2) contains the pair-codegree calculation as its \(t=2\)
case, but it retains information that the maximum pair codegree discards:
many close checkpoints force successive positions in both coordinate
orders.

### Corollary 2.2 (exact Johnson pair profile)

If \(A,B\in V\) have Johnson distance \(r\), then their codegree divided
by the degree in (1.5) is

\[
 {d(A,B)\over d}=
 \begin{cases}
 \displaystyle {2(b+1-r)\over
 (b+1)\binom br^2},&1\le r\le b-2,\\[3mm]
 \displaystyle {6\over(b+1)b^2},&r=b-1,\\[2mm]
 0,&r=b.
 \end{cases}
\tag{2.3}
\]

In particular,

\[
                         {\Delta_2\over d}={2\over b(b+1)}.
\tag{2.4}
\]

#### Proof

For \(r\le b-2\), there are \(2(b+1-r)\) ordered position pairs at
separation \(r\).  For each, (2.2) gives
\((r!(b-r)!)^2=(b!)^2/\binom br^2\) labels.  At distance \(b-1\), the
two unordered position pairs at separation \(b-1\), together with the
endpoint pair \(\{0,b\}\), give six ordered assignments, each with
\(((b-1)!)^2\) labels.  Divide by the labelled degree
\((b+1)(b!)^2\); support multiplicity two cancels from numerator and
denominator.  Complementary targets never occur together.  The first line
is maximal at \(r=1\), proving (2.4). \(\square\)

### Corollary 2.3 (complete higher-codegree formula)

For a finite set \(\mathcal A\) of distinct middle targets, let
\(\operatorname {Emb}(\mathcal A)\) be the injective assignments
\(\phi:\mathcal A\to\{0,\ldots,b\}\) compatible with a packet label.
If \(K_\phi=\phi(\mathcal A)\), then the simple normalized codegree is

\[
 {d(\mathcal A)\over d}
 ={1\over(b+1)(b!)^2}
   \sum_{\phi\in\operatorname {Emb}(\mathcal A)}L(K_\phi),
\tag{2.5}
\]

where \(L\) is given by (2.2).  Thus the full higher-codegree hierarchy is
an explicit finite metric-embedding sum, not merely a maximum bound.

#### Proof

Every label containing \(\mathcal A\) assigns its distinct targets to
unique packet positions and hence contributes to one compatible injection.
Conversely, Theorem 2.1 counts exactly the labels for each compatible
injection.  Sum and divide by the labelled degree; the common support
multiplicity two again cancels. \(\square\)

## 3. Rooted factorial overlap moments

Fix a simple packet support \(F\) and a target \(A\in F\).  For a uniformly
random simple packet \(E\ni A\), put

\[
                         J=|(E\cap F)\setminus\{A\}|,
 \qquad M_s(F,A)={\mathbb E}{J\choose s}.
\tag{3.1}
\]

The distribution is unchanged if packet labels are sampled instead,
because every support has multiplicity two.

For \(r\ge0\), put

\[
 (b)_r=b(b-1)\cdots(b-r+1),\qquad
 A_r={\binom{b-1}{r}\over (b)_r^2},
\tag{3.2}
\]

with \(A_0=1\) and \(A_b=0\).

### Lemma 3.1 (metric embedding bound)

Let \(\mathcal Q=\{0,1,\ldots,b\}\) carry the metric in (1.4).  Every
metric sphere in \(\mathcal Q\) has at most two points.  If a distinguished
point of a \((s+1)\)-point subspace is required to map to a specified
point, there are at most \(2^s\) isometric embeddings into \(\mathcal Q\).

#### Proof

The ordinary path metric has spheres of size at most two.  The sole change
in (1.4) moves the distance between \(0\) and \(b\) from \(b\) to
\(b-1\); for a sphere about either endpoint it replaces a missing/extreme
possibility without raising the size above two.  After the image of the
distinguished point is fixed, each other point has at most two possible
images even if all mutual-distance and injectivity constraints are ignored.
\(\square\)

### Theorem 3.2 (all rooted factorial moments)

Uniformly in \(F,A\),

\[
                         M_1(F,A)\le {12\over b^2},
\tag{3.3}
\]

and, for \(2\le s\le b\),

\[
 \boxed{
 M_s(F,A)
 \le 2^s(s+1)\left(A_s+{A_{s-1}\over b+1}\right).}
\tag{3.4}
\]

In particular, if \(2\le s\le b/2\), then

\[
 M_s(F,A)
 \le {8^s(s+1)^2\over b^s s!}.
\tag{3.5}
\]

#### Proof

For (3.3), sum the exact normalized pair-codegrees over the other targets
of \(F\).  At most two of them occur at any Johnson distance.  At distance
one the normalized codegree is at most \(2/b^2\).  For
\(2\le r\le b-2\), it is at most

\[
 {2\over\binom br^2}
 \le {8\over b^2(b-1)^2},
\tag{3.6}
\]

and at distance \(b-1\) it is at most \(6/b^3\).  Summation gives
(3.3) for \(b\ge5\).

For (3.4), expand \(\binom Js\) by choosing the other \(s\) targets of
\(F\).  Equality of targets preserves Johnson distance, so their source
positions and their positions in \(E\) form an isometric map in
\(\mathcal Q\).  Reverse the map and use Lemma 3.1.  For every image
position set \(K\), and for each of its \(s+1\) choices for the image of
\(A\), at most \(2^s\) source tuples can contribute.

It remains to sum (2.2) over image position sets.  For span below \(b\),
write

\[
 h_0=b-S,\qquad h_j=g_j\ (1\le j\le s).
\tag{3.7}
\]

The positive integers \(h_0,\ldots,h_s\) sum to \(b\), and there are
\(h_0+1\) choices for the leftmost position.  Moving mass from a smaller
part greater than one into a largest part increases the product of the
factorials.  Hence

\[
 {b!\over\prod_{j=0}^s h_j!}\ge (b)_s.
\tag{3.8}
\]

There are \(\binom{b-1}s\) positive compositions, so the sum of
\(L(K)/(b!)^2\) over all non-full spans is at most

\[
                         (b+1)A_s.
\tag{3.9}
\]

For full span, the \(s\) positive gaps sum to \(b\).  Dropping the helpful
factor \(g_1g_s\) from the denominator in (2.2), the same argument bounds
the corresponding sum by

\[
                         A_{s-1}.
\tag{3.10}
\]

Divide \(2^s(s+1)\) times the sum of (3.9)--(3.10) by the labelled degree
\((b+1)(b!)^2\).  This is (3.4).

Finally, for \(r\le b/2\),

\[
 A_r\le {b^r/r!\over(b/2)^{2r}}
       ={4^r\over b^r r!}.
\tag{3.11}
\]

Substitution in (3.4) gives (3.5). \(\square\)

## 4. The complete rooted overlap kernel

For \(0<\rho\le1\), define

\[
 \mathcal K_{F,A}(\rho)
 ={1\over d}
   \sum_{\substack{E\ni A\\E\ne F}}
   \left(\rho^{-|(E\cap F)\setminus\{A\}|}-1\right).
\tag{4.1}
\]

This is the exact exponential statistic that replaces the maximum
pair-codegree in a deep residual.  Put \(z=\rho^{-1}-1\).

### Theorem 4.1 (uniform rooted-kernel bound)

If \(8(1+z)<b\), then, uniformly in \(F,A\),

\[
 \boxed{
 \mathcal K_{F,A}(\rho)
 \le {12z\over b^2}+{1280z^2\over b^2}
      +2b^3\left({8(1+z)\over b}\right)^b.}
\tag{4.2}
\]

Consequently,

\[
 b\rho\longrightarrow\infty
 \quad\Longrightarrow\quad
 \max_{F,A}\mathcal K_{F,A}(\rho)
 =O\!\left({1\over b^2\rho^2}\right)=o(1).
\tag{4.3}
\]

#### Proof

Since \((1+z)^J=\sum_s\binom Js z^s\), including the omitted nonnegative
term \(E=F\) gives

\[
 \mathcal K_{F,A}(\rho)
 \le\sum_{s=1}^b M_s(F,A)z^s.
\tag{4.4}
\]

The \(s=1\) term is bounded by (3.3).  For
\(2\le s\le b/2\), (3.5) and the elementary identity

\[
 \sum_{s\ge0}{(s+1)^2a^s\over s!}
 =(a^2+3a+1)e^a
\tag{4.5}
\]

show, for \(0\le a=8z/b<1\), that the sum of the remaining low-order
terms is at most \(20a^2\), which is the second term of (4.2).

For \(s>b/2\), both indices \(s,s-1\) in (3.4) are at least
\(n=(b-1)/2\).  Directly from (3.2),

\[
 {A_{r+1}\over A_r}
 ={b-1-r\over(r+1)(b-r)^2}<1\qquad(r\ge n),
\tag{4.6}
\]

so the high-order tail is maximized at \(r=n\).  Since \(b=2n+1\),

\[
 A_n={ (n+1)^2\over b^2(b-1)!}
 \le {1\over(b-1)!}
 \le \left({4\over b}\right)^{b-1}
 \le b\left({4\over b}\right)^b.
\tag{4.7}
\]

Here the penultimate inequality follows from
\((b-1)!\ge((b-1)/e)^{b-1}\ge(b/4)^{b-1}\) for \(b\ge5\); the first
factorial inequality follows, for example, by integrating \(\log x\).
Thus (3.4) bounds every high-order \(M_s\) by
\(2b^2(8/b)^b\).  Summing the at most \(b\) high-order terms and using
\(z^s\le(1+z)^b\) gives the last term of (4.2).  Equation (4.3) follows
as follows.  Put \(x=b\rho\).  Then \(x\to\infty\), \(x\le b\), and
\(1+z=1/\rho\).  The high-order term is
\(2b^3(8/x)^b=o(x^{-2})\): once \(x\ge16\), it is at most
\(2b^3 2^{-b}\), whereas \(x^{-2}\ge b^{-2}\).  The first two terms are
\(O(x^{-2})\) because \(z\le1/\rho\). \(\square\)

## 5. Product-residual regeneration

Retain each target of \(V\) independently with probability \(\rho\).
Condition on retaining a fixed target \(A\), and let \(Z_A\) be its degree
in the induced simple packet hypergraph.  Then

\[
                         \mu_A={\mathbb E}Z_A=d\rho^b.
\tag{5.1}
\]

### Theorem 5.1 (fixed-root and aggregate concentration)

For every \(A\),

\[
 {\operatorname {Var}Z_A\over\mu_A^2}
 \le {1\over\mu_A}
     +\max_{F\ni A}\mathcal K_{F,A}(\rho).
\tag{5.2}
\]

Hence, if \(b\rho\to\infty\), then

\[
                         Z_A=(1+o_{\mathbb P}(1))d\rho^b.
\tag{5.3}
\]

Moreover, some product residual has all but \(o(\rho W)\) of its retained
targets satisfying (5.3), with a common deterministic relative error
\(o(1)\).

#### Proof

For \(F\ni A\), let \(I_F\) indicate that every member of
\(F\setminus\{A\}\) survives.  Then

\[
 {\mathbb E(I_EI_F)\over(\mathbb E I_E)(\mathbb E I_F)}
 =\rho^{-|(E\cap F)\setminus\{A\}|}.
\tag{5.4}
\]

Expanding the variance, bounding the diagonal by \(\mu_A\), and averaging
(4.1) over \(F\ni A\) proves (5.2).  Theorem 4.1 makes its second term
\(o(1)\).  Also Stirling gives

\[
 \log(d\rho^b)
 =2b\log b-2b+b\log\rho+O(\log b)\longrightarrow\infty
\tag{5.5}
\]

when \(b\rho\to\infty\).  Chebyshev proves (5.3).

Choose a deterministic error tending to zero more slowly than the square
root of the right side of (5.2).  The expected number of retained targets
violating that error is \(o(\rho W)\).  Markov's inequality, together with
the ordinary binomial concentration of the residual size, supplies one
outcome with the aggregate assertion. \(\square\)

The theorem reaches, for example, every \(\rho=b^{-\alpha}\) with
\(0<\alpha<1\).  Thus neither degree exhaustion nor time-zero high-overlap
clusters obstruct an \(o(W)\) leave.

## 6. Why this is not yet a matching theorem

The pair hypotheses alone cannot be iterated.  Here is a self-contained
generic counterexample.  Put

\[
 D=r^2,\qquad Q=\log(2eDr),\qquad c={16Q\over r},
\tag{6.1}
\]

and take \(r\) large enough that \(r\ge64Q\).  Choose \(r\) independent
uniform random equipartitions of a set of size \(LD\) into \(L\) blocks
of size \(D\), with \(L\) sufficiently large.  With positive probability:

1. every two blocks from different partitions meet in at most two points
   (the expected number of triple intersections is
   \(O(r^2D^4/(LD))=o(1)\)); and
2. no set of \(s=\lceil cL\rceil\) points meets every block in at most
   one point.

For the second assertion, a fixed \(s\)-set is a partial transversal of
one random partition with probability

\[
 { (L)_sD^s\over(LD)_s}
 \le \exp\{-s(s-1)/(4L)\},
\tag{6.2}
\]

provided \(s\le L/2\), which follows from \(c\le1/4\) for large \(L\).
Indeed, using \(s-1\ge cL/2\) and
\(\log(eLD/s)\le\log(eD/c)<Q\), the expected number of common partial
transversals is at most

\[
 \binom{LD}s\exp\{-rs(s-1)/(4L)\}
 \le \exp\{s(Q-rc/8)\}=e^{-sQ}=o(1).
\tag{6.3}
\]

For the first assertion, two independently uniform \(D\)-blocks have
probability at most
\(\binom D3^2/\binom{LD}3\) of meeting in at least three points.  A union
bound over \(\binom r2L^2\) block pairs is
\(O(r^2D^3/L)=o(1)\).  Thus the two properties occur simultaneously for
all sufficiently large \(L\).

Make one hypergraph vertex for every block and one edge for every point,
using its containing block in each of the \(r\) partitions.  This is
\(r\)-uniform and \(D\)-regular, has

\[
                         {\Delta_2\over D}\le {2\over r^2},
\tag{6.4}
\]

but a matching is exactly a common partial transversal, so it covers only
at most \(2c=O(\log r/r)\) of the vertices for large \(L\).  Thus even
\(r\Delta_2/D\to0\) is not a parameter-only matching criterion.
Replacing every edge by a common number of labelled parallel copies makes
the absolute labelled degree arbitrarily large, with normalized codegrees
and matching number unchanged.  Hence an absolute-degree hypothesis alone
does not repair a labelled/multihypergraph theorem.  A theorem restricted
to simple hypergraphs may of course use simplicity and a quantitative
degree-versus-order hypothesis; neither is encoded by (2.4).

The all-order packet result above rules out this particular latent-partition
mechanism at product scale, but it still does not justify conditioning on a
long matching history.  Indeed arbitrary dense residuals cannot satisfy a
hereditary phase-packet theorem.  For a coordinate \(x\), the star

\[
                         \mathcal S_x=\{A\in V:x\in A\}
\tag{6.5}
\]

has density \(1/2\) and contains no packet support: the intersection of all
\(q\) targets of every packet is empty.  Hence the induced packet
hypergraph on \(\mathcal S_x\) has degree zero.

For completeness, the iteration that this failure interrupts is elementary.

### Lemma 6.1 (isolated bite with growing \(q\))

Let \(\mathcal G\) be a \(q\)-uniform hypergraph with all degrees
\((1\pm\eta)D_0\), and put

\[
 \sigma(\mathcal G)
 ={1\over qD_0}\max_{F\in E(\mathcal G)}
   \sum_{\{A,B\}\in\binom F2}d_{\mathcal G}(A,B).
\tag{6.6}
\]

If \(\eta+\sigma+D_0^{-1}=o(1)\), then \(\mathcal G\) has a matching
covering

\[
                         {e^{-1}+o(1)\over q}|V(\mathcal G)|
\tag{6.7}
\]

vertices.

#### Proof

Mark every edge independently with probability \(p=1/(qD_0)\), and keep
a marked edge exactly when no intersecting edge is marked.  If \(N(F)\)
is the number of other edges meeting \(F\), the union bound and the first
Bonferroni inequality give

\[
 q(1-\eta)D_0-q-qD_0\sigma
 \le N(F)\le q(1+\eta)D_0.
\tag{6.8}
\]

Thus

\[
 \Pr(F\text{ is kept})
 =p(1-p)^{N(F)}={e^{-1}+o(1)\over qD_0}.
\tag{6.9}
\]

Kept edges through one vertex are mutually exclusive.  Summing (6.9) over
its incident edges gives coverage probability
\((e^{-1}+o(1))/q\); summing over vertices and choosing an outcome at least
as large as its expectation proves (6.7). \(\square\)

At time zero, (3.3) gives

\[
 \sigma(\mathcal H_b)
 \le {1\over2q}\sum_{A\in F}M_1(F,A)
 \le {6\over b^2}.
\tag{6.10}
\]

The exact remaining sufficient input is therefore **matching-correlated
regeneration**, not regeneration for every vertex subset:

> Starting from the full orbit, construct the successive isolated bites
> so that, until the uncovered density is some \(\rho_b=o(1)\) with
> \(b\rho_b\to\infty\), the available packet degrees and rooted overlap
> factorial moments remain within the bounds needed for
> \(\eta+\sigma=o(1)\), apart from an aggregate \(o(W)\) quarantined target
> set.  At every stage there must be at least one isolated-bite outcome
> preserving these conditions for the next stage.

Under that statement, the elementary isolated-bite calculation removes
\((e^{-1}+o(1))/q\) of the current targets per bite; after
\(O(q\log(1/\rho_b))\) regenerated bites it leaves \(o(W)\) targets.
Theorems 4.1 and 5.1 verify the time-zero rooted overlap kernel and
product-thinned degree regeneration for this program, for every sequence
\(\rho_b\) satisfying \(b\rho_b\to\infty\).  They do **not** verify the
displayed stage-uniform condition: product thinning is independent, whereas
an isolated bite is selected from and conditioned on the current packet
catalogue.  What is still unproved is preservation under that
future-selected matching filtration, or a one-shot construction that
bypasses it.

Accordingly, the rigorous verdict is

\[
 \boxed{
 \begin{array}{c}
 \text{the phase-packet orbit crosses the all-order product-regeneration
 test,}\\
 \text{but no self-contained near-perfect matching theorem has yet been
 derived from it.}
 \end{array}}
\tag{6.11}
\]

## 7. Finite audit

The companion checker

`scratch/verify_gate_c_phase_packet_higher_overlap_20260822.py`

exhaustively checks for \(b=3,5\):

1. support multiplicity two;
2. every prescribed-position instance of (2.2);
3. the exact rooted intersection histograms for every position of a
   canonical packet; and
4. inequalities (3.3), (3.4), and (4.2).

The checker is confirmatory; every asymptotic assertion is proved above.
