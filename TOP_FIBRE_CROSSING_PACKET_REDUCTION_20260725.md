# The crossing-scale top-fibre promotion reduction

Date: 2026-07-25

Pure mathematics only.  No computation, web search, solver, or probabilistic
rounding assertion is used.

## 0. Verdict

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q},
\]

and

\[
 \lambda_q=\frac{W}{N_q}.
\]

Let \(H\) be the least positive integer for which

\[
 \lambda_H\ge m+H,
 \qquad M:=m+H.                                      \tag{0.1}
\]

This is the unique useful scale for the following top-fibre construction.
One has

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 N_H=(1+o(1))\frac Wm.                               \tag{0.2}
\]

For every top \(U\in\binom{[2m]}M\), choose one oriented cyclic order of
\(U\).  Its \(M\) sliding \(m\)-windows, equipped with their natural full
radius-\(H\) flags, form one bridge-one promotion cycle with frozen top
\(U\).  Cutting one edge gives one path of \(M\) owners.

The crossing definition (0.1) has three exact consequences.

1. The aggregate middle capacity of one packet per top is
   \[
      T:=MN_H=W-o(W).                                  \tag{0.3}
   \]
2. The total path-reset toll is
   \[
      2HN_H=o(W).                                      \tag{0.4}
   \]
3. If the packet shadows could be made floor/ceiling balanced at every
   controlled rank, their *entire forced hole ledger*, summed over all
   depths, would be \(o(W)\).

Thus promotion, which fails at fixed \(H=A\sqrt m\) because there are
\(\Theta_A(W)\) frozen tops, becomes quantitatively viable exactly at the
crossing scale: here there are only \((1+o(1))W/m=o(W/H)\) top fibres.

The remaining statement is a single integral cyclic-packet resolution.
Choose one cyclic order per top so that

* the \(M\) middle windows from different tops are disjoint; and
* at every length \(m-q\) and \(m+q\), the aggregate cyclic-interval
  histogram is floor/ceiling balanced (or has only \(o(W)\) total holes).

An exact augmented hypergraph for this statement is given below.  It has a
fully symmetric fractional solution.  Its middle-only relaxation has an
exact integral Hall solution.  What is not proved is the simultaneous
cyclic-order constraint.  The sharp local statistics are:

\[
 \frac{\Delta_2^{\rm middle}}D=\frac2{m^2},             \tag{0.5}
\]

but adjacent nested shadow constraints have relative codegree

\[
 \Theta(1/m).                                          \tag{0.6}
\]

The latter is the precise high-order clustering which prevents this note
from invoking an ordinary growing-uniformity nibble as a black box.

## 1. The crossing scale

The exact ratio is

\[
 \lambda_h
 =\prod_{i=0}^{h-1}\frac{m+i+1}{m-i}.                   \tag{1.1}
\]

### Lemma 1.1 (location and overshoot of the crossing)

For the least \(H\) satisfying (0.1),

\[
 H=(1+o(1))\sqrt{m\log m},                              \tag{1.2}
\]

and

\[
 1\le \frac{\lambda_H}{M}
 <\frac{m+H-1}{m-H+1}
 =1+O\!\left(\frac Hm\right).                          \tag{1.3}
\]

Consequently, with \(T=MN_H\) and \(D=W-T\),

\[
 0\le \frac DW=O\!\left(\frac Hm\right)=o(1),         \tag{1.4}
\]

and

\[
 N_H=(1+o(1))\frac WM.                                 \tag{1.5}
\]

#### Proof

First take \(h=2\sqrt{m\log m}\).  The elementary lower bound

\[
 \log\lambda_h
 \ge \sum_{i=0}^{h-1}\frac{2i+1}{m+i+1}
 \ge \frac{h^2}{m+h}
\]

shows that \(\lambda_h>m+h\) for all sufficiently large \(m\).  Hence the
minimal crossing has \(H=o(m)\).  Uniform Taylor expansion in (1.1) now
gives

\[
 \log\lambda_H
 =\frac{H^2}{m}+O\!\left(\frac Hm+\frac{H^3}{m^2}\right).
                                                               \tag{1.6}
\]

Minimality and (0.1) place \(\log\lambda_H\) between
\(\log(m+H-1)+o(1)\) and \(\log(m+H)+o(1)\), proving (1.2).

Also

\[
 \lambda_H
 =\lambda_{H-1}\frac{m+H}{m-H+1}
 <(m+H-1)\frac{m+H}{m-H+1}.
\]

Division by \(M=m+H\) proves (1.3).  Since
\(T/W=M/\lambda_H\), (1.4)--(1.5) follow. \(\square\)

### Corollary 1.2 (the reset ledger)

One promotion path per top has

\[
 p=N_H=(1+o(1))\frac Wm=o(W/H)                          \tag{1.7}
\]

components, and its total full-flag initialization toll is

\[
 2Hp=2HN_H=o(W).                                       \tag{1.8}
\]

This is the first regime in which a promotion-only top-fibre construction
has the correct coefficient-one path scale.

## 2. One top supplies one exact promotion packet

Fix \(U\in\binom{[2m]}M\) and an oriented cyclic order

\[
 \pi=(u_0,u_1,\ldots,u_{M-1})
\]

modulo rotation.  Write \(I_\pi(j,r)\) for its cyclic interval of length
\(r\), and put

\[
 X_j=I_\pi(j,m),\qquad j\in\mathbb Z_M.                \tag{2.1}
\]

The Johnson step \(X_j\to X_{j+1}\) deletes \(u_j\) and adds \(u_{j+m}\).
The deleted coordinate returns after exactly \(H\) steps.  Define

\[
 \alpha(X_j)=(u_j,u_{j+1},\ldots,u_{j+H-1}),           \tag{2.2}
\]

\[
 \beta(X_j)=(u_{j-1},u_{j-2},\ldots,u_{j-H}).          \tag{2.3}
\]

These are valid lower-deletion and upper-addition queues.  Every arc is the
last-position promotion, and

\[
 L_q(X_j)=I_\pi(j+q,m-q),                              \tag{2.4}
\]

\[
 U_q(X_j)=I_\pi(j-q,m+q)                               \tag{2.5}
\]

for \(0\le q\le H\).  At \(q=H\), (2.5) is the common top \(U\).

Thus the \(M\) states form one bridge-one cycle.  Cutting one arc gives a
path whose literal word has length

\[
 M+2H.                                                  \tag{2.6}
\]

For every \(q<H\), the packet exposes \(M\) *distinct* lower targets and
\(M\) distinct upper targets at depth \(q\).  At lower depth \(H\), it
again exposes \(M\) distinct bottoms.  Its upper depth-\(H\) target is the
single set \(U\), repeated by all owners but covered once.

## 3. Exact coefficient-one transfer from balanced packets

For every top \(U\), choose one packet \(P_U\).  Assume first that their
middle supports are pairwise disjoint.  They use exactly \(T=MN_H\) middle
owners, leaving \(D=W-T\).

For \(1\le q\le H\), let \(M_q^-\) be the number of rank-\((m-q)\)
targets missing from all packet lower flags.  For \(1\le q<H\), define
\(M_q^+\) analogously above the middle.  There is no upper depth-\(H\)
defect because every top \(U\) is represented.

Concatenate the cut packet paths, append the \(D\) missing middle owners,
append every missing controlled shadow target literally, and use the proved
outer product-SCD tail.  The resulting word has length at most

\[
 W+2HN_H
 +\sum_{q=1}^{H}M_q^-
 +\sum_{q=1}^{H-1}M_q^+
 +o(W).                                                    \tag{3.1}
\]

Here the tail is \(o(W)\) because \(H/\sqrt m\to\infty\) and \(H=o(m)\).

Put

\[
 \bar\lambda_q=\frac{T}{N_q},\qquad
 a_q=\lfloor\bar\lambda_q\rfloor,\qquad
 b_q=T-a_qN_q.                                           \tag{3.2}
\]

If every lower histogram, and every upper histogram for \(q<H\), has
values in \(\{a_q,a_q+1\}\), then its number of holes is exactly

\[
 (N_q-T)_+.                                               \tag{3.3}
\]

At lower depth \(H\), \(\bar\lambda_H=M\), so there are no holes.

### Lemma 3.1 (the total forced packet deficit is negligible)

\[
 D+2\sum_{q=1}^{H-1}(N_q-T)_+=o(W).                     \tag{3.4}
\]

#### Proof

By Lemma 1.1, \(D\le CWH/m\) for an absolute constant \(C\).  Also

\[
 \frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+i+1}
 \le \exp\!\left(-\frac{q^2}{m+q}\right).              \tag{3.5}
\]

If \(N_q>T=W-D\), then (3.5) and \(D/W=O(H/m)=o(1)\)
force \(q^2=O(H)\).  Hence only \(O(\sqrt H)\) summands in (3.4) can be
positive.  Each is at most \(D\), and therefore

\[
 \sum_q(N_q-T)_+
 =O(D\sqrt H)
 =O\!\left(W\frac{H^{3/2}}m\right)
 =o(W),
\]

because \(H=(1+o(1))\sqrt{m\log m}\). \(\square\)

### Theorem 3.2 (balanced top packets imply coefficient one)

If one can choose one packet per top so that

1. the packet middle supports are pairwise disjoint; and
2. all the histograms in (3.2) are floor/ceiling balanced,

then

\[
 \nu(2m)\le W+o(W).                                      \tag{3.6}
\]

The odd-dimensional result follows by the trimmed one-bit lift.

#### Proof

Substitute (1.8), (3.3), and Lemma 3.1 into (3.1). \(\square\)

The exact floor/ceiling requirement may be weakened: Theorem 3.2 still
holds if the aggregate number of additional holes above (3.3) is \(o(W)\).

## 4. The packet hypergraph and its exact local statistics

Let \({\cal E}\) be the set of pairs \((U,\pi)\), where
\(U\in\binom{[2m]}M\) and \(\pi\) is an oriented cyclic order of \(U\)
modulo rotation.  Thus

\[
 |{\cal E}|=N_H(M-1)!.                                   \tag{4.1}
\]

The packet \((U,\pi)\) contains the \(M\) cyclic intervals of each rank
\(r\), \(1\le r<M\).  In the application only
\(m-H\le r\le M-1\) is used.

### Lemma 4.1 (one-target degree)

Every fixed \(r\)-set \(S\), with \(1\le r<M\), lies in exactly

\[
 d_r
 =\binom{2m-r}{M-r}r!(M-r)!
 =\frac{r!(2m-r)!}{(m-H)!}                              \tag{4.2}
\]

packets as a cyclic \(r\)-interval.

#### Proof

Choose the top \(U\supset S\), and then cyclically arrange \(S\) as one
block.  There are \(r!(M-r)!\) oriented cycles for each top. \(\square\)

In particular, the middle degree is

\[
 D=d_m=\frac{(m!)^2}{(m-H)!}.                            \tag{4.3}
\]

The lower and upper depth-\(q\) degrees agree and satisfy

\[
 d_{m-q}=d_{m+q}=\lambda_qD.                             \tag{4.4}
\]

### Lemma 4.2 (middle-pair codegrees)

Let \(X,Y\in\binom{[2m]}m\), and put
\(|X-Y|=|Y-X|=d\).  If \(1\le d<H\), then

\[
 d(X,Y)
 =\frac{2(d!)^2(m-d)!^2}{(m-H)!},                        \tag{4.5}
\]

and hence

\[
 \frac{d(X,Y)}D=\frac2{\binom md^2}.                    \tag{4.6}
\]

If \(d=H\), then

\[
 d(X,Y)=(H!)^2(m-H+1)!,                                  \tag{4.7}
\]

while if \(d>H\), the codegree is zero.  Consequently

\[
 \max_{X\ne Y}\frac{d(X,Y)}D=\frac2{m^2}.              \tag{4.8}
\]

#### Proof

For \(d<H\), choose the top in
\(\binom{m-d}{H-d}\) ways.  Inside it, the complementary \(H\)-sets of
\(X\) and \(Y\) are overlapping cyclic intervals shifted by \(d\).  The
number of cycles is

\[
 2(d!)^2(H-d)!(m-d)!.
\]

Multiplication and cancellation give (4.5).  If \(d=H\), the two
complementary \(H\)-sets are disjoint and determine the unique top.  Treat
them as two cyclic blocks; this gives (4.7).  The remaining assertions are
immediate. \(\square\)

Thus the middle-only packet system has the favorable relative codegree
\(2/m^2\).

If one adjoins the top marker \(U\) to every packet edge, the resulting
\((M+1)\)-uniform hypergraph is itself asymptotically regular.  The top
degree is

\[
 D_{\rm top}=(M-1)!,
\]

and

\[
 \frac{D_{\rm top}}D
 =\frac{\lambda_H}{M}
 =1+O(H/m).                                               \tag{4.8a}
\]

For \(X\subset U\), the top--middle codegree is \(m!H!\), whose ratio to
\(D\) is \(1/\binom mH\).  Hence this top--middle packet hypergraph has
maximum relative pair codegree \(2/m^2\).  These are precisely the local
statistics one would want for a growing-uniformity near-matching theorem;
no such theorem is invoked here.

### Lemma 4.3 (sharp adjacent-rank clustering)

Let \(S\subset T\), with \(|S|=r\), \(|T|=r+1\), and
\(1\le r\le M-2\).  The number of packets in which both are cyclic
intervals is

\[
 d(S,T)
 =\frac{2r!(2m-r-1)!}{(m-H)!}.                          \tag{4.9}
\]

Therefore

\[
 \frac{d(S,T)}{d_r}=\frac2{2m-r},\qquad
 \frac{d(S,T)}{d_{r+1}}=\frac2{r+1}.                    \tag{4.10}
\]

Across the central band this is \(\Theta(1/m)\), and the order is sharp.

#### Proof

Choose \(U\supset T\).  In the cyclic order, the extra point of \(T-S\)
must be attached at one of the two ends of the interval \(S\).  This gives
\(2r!(M-r-1)!\) cycles per top.  Multiplication by the number of tops and
cancellation give (4.9). \(\square\)

This adjacent-rank clustering is the main quantitative warning.  If all
controlled ranks are inserted as ordinary vertices of one augmented edge,
the edge size is \(\Theta(MH)\), while its largest relative cross-rank
codegree is only \(\Theta(1/m)\), not \(\Theta(1/m^2)\).  A standard
fixed-uniformity matching theorem therefore does not directly supply the
needed diagonal integral resolution.

There is a smaller exact near-rainbow core.  If there is a positive depth
with \(N_q>T\), let \(q_*\) be the largest such depth (otherwise put
\(q_*=0\)).  Lemma 3.1 shows

\[
 q_*=O(\sqrt H).                                          \tag{4.11}
\]

At every \(q\le q_*\), floor/ceiling balance means genuine injectivity of
the selected packet shadows: their loads are zero or one.  Thus the ranks
where the packet capacity itself is below the number of targets occupy only
\(O(\sqrt H)=O(m^{1/4}(\log m)^{1/4})\) depths.  Beyond this point repeated
colors are arithmetically necessary, and the problem is coverage/balance
rather than rainbowness.

## 5. What ordinary Hall already solves

Ignore cyclic order and ask only that every top choose \(M\) of its middle
subsets, with no middle owner chosen twice.  This relaxation is exactly
integral.

### Theorem 5.1 (unstructured top assignment)

There are sets

\[
 {cal A}_U\subseteq\binom Um,\qquad |{\cal A}_U|=M,
\]

one for every \(U\in\binom{[2m]}M\), such that the families
\({\cal A}_U\) are pairwise disjoint.

#### Proof

Use the bipartite inclusion graph between tops \(U\) and middle owners
\(X\subset U\).  Its two degrees are

\[
 d_L=\binom M m,\qquad d_R=\binom mH,
\]

and incidence counting gives

\[
 \frac{d_L}{d_R}=\frac W{N_H}=\lambda_H\ge M.            \tag{5.1}
\]

For any family \({\cal S}\) of tops,

\[
 d_L|{\cal S}|
 \le d_R|N({\cal S})|,
\]

so \(|N({\cal S})|\ge M|{\cal S}|\).  Clone every top \(M\) times and
apply Hall's theorem. \(\square\)

Thus neither middle capacity nor one-fold top ownership is an obstruction.
The missing local condition is exact:

> for every \(U\), the complementary family
> \(\{U-X:X\in{\cal A}_U\}\) must be the edge set of a tight Hamilton
> cycle in the complete \(H\)-uniform hypergraph on \(U\).

Equivalently, the selected owners must be the \(m\)-windows of one cyclic
order.  Theorem 5.1 does not enforce that condition.

## 6. Exact augmented matching formulation

For every controlled rank \(m\pm q\), except the common top at upper depth
\(H\), define \(a_q,b_q\) by (3.2).  For every target \(S\), make

* \(a_q\) mandatory core clones \((S,1),\ldots,(S,a_q)\); and
* one optional bonus clone \((S,+)\).

At middle rank there are no mandatory clones because \(T<W\); the middle
sets themselves are optional vertices of capacity one.  At lower depth
\(H\), one has \(a_H=M,b_H=0\).  Also make one mandatory marker for every
top \(U\).

Decorate a packet by assigning every one of its interval occurrences to a
clone of the corresponding target.  A matching of \(N_H\) decorated
packets which

1. covers every top marker;
2. covers every mandatory core clone; and
3. uses every optional clone at most once

is exactly a packet family satisfying Theorem 3.2.  Indeed, after the core
clones are covered, the remaining \(b_q\) occurrences at rank \(q\) must
occupy distinct bonus clones.

### Proposition 6.1 (exact fractional feasibility)

The decorated augmented hypergraph has a rational fractional matching which
covers every top marker and every mandatory core clone exactly once, and
loads every optional clone by at most one.

#### Proof

Give every cyclic order inside every top equal total packet weight, so every
top has weight one.  Coordinate transitivity and Lemma 4.1 give total
occurrence weight \(T/N_q=a_q+b_q/N_q\) at every rank-\(q\) target.
Split that occurrence weight symmetrically: one unit to each core clone and
the remaining \(b_q/N_q\) to its bonus clone.  This can be implemented by
finite decorated copies, independently over the finitely many occurrences
in a packet.  Middle vertices receive weight \(T/W<1\). \(\square\)

This proves that there is no divisibility, capacity, marginal, or fractional
obstruction.  The unresolved theorem is the integral rounding of this one
highly clustered packet system.

## 7. Additional exact invariants and one solved shadow

Every cyclic packet on \(U\) contains each coordinate of \(U\) in exactly
\(m\) of its \(M\) middle owners.  Hence any one-packet-per-top selection
has the forced point marginal

\[
 \#\{\text{selected owners containing }x\}
 =m\binom{2m-1}{M-1}=\frac T2                         \tag{7.1}
\]

for every coordinate \(x\), provided the packet owners are globally
distinct.  In fact the displayed identity also proves automatically that
\(T\) is even, since its left side is an integer.  Thus the forced point
marginal creates no parity obstruction.

The upper shadow at depth \(H-1\) is already balanced for *every* choice of
cyclic orders.  A packet on \(U\) contains all \(M\) subsets \(U-\{x\}\).
Therefore every rank-\((M-1)\) target occurs in exactly

\[
 2m-(M-1)=m-H+1                                      \tag{7.2}
\]

packets, and

\[
 \frac{T}{N_{H-1}}=m-H+1.                            \tag{7.3}
\]

So the deepest upper shadow costs no alignment at all.  The unresolved
alignment lies in the genuinely cyclic interval lengths.

## 8. Exact remaining theorem

The crossing-scale packet resolution theorem is:

> With \(H\) defined by (0.1), choose one oriented cyclic order \(\pi_U\)
> for every \(U\in\binom{[2m]}{m+H}\) such that the \(m\)-interval
> families are pairwise disjoint and the aggregate interval histograms at
> every length \(m-q\) and \(m+q\), \(1\le q\le H\), have only \(o(W)\)
> total holes.

Theorem 3.2 proves that this statement implies the coefficient-one
contiguous-OR theorem.  Sections 5--7 show exactly what is already solved:

* the top-fibre promotion paths themselves are explicit;
* their total capacity and reset toll have the correct asymptotics;
* arbitrary integral top-to-middle assignment follows from Hall;
* all desired clone marginals have an exact rational solution;
* middle-pair codegrees are only \(2/m^2\); and
* the common top and the next upper shadow are automatic.

What remains is not portal cost or path construction.  It is the integral
multi-length cyclic-order resolution inside the top fibres.
