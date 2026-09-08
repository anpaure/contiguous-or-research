# Critical weighted transported unions: the anchor cocycle and the external shoulder shield

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Result and exact boundary

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r.
\]

Fix \(A>0\) and \(\varepsilon>0\).  Work in the compact critical sector of
zero-winding first-return profiles satisfying

\[
 s=p+q\le A\sqrt r,\qquad
 b=2q-p+1,\qquad
 \varepsilon\sqrt r\le p,q,b,
 \qquad y_p=1.                                    \tag{0.1}
\]

The terminal inverse fibre is the audited one-defect rotor.  Its admissible
top phases form an interval

\[
 I=\{0,1,\ldots,b-1\}.
\]

Transporting all actual duration-\(s\) top-start sets to one reference
fibre gives \(\mathcal A_x\), \(x\in I\).  The still desired estimate is

\[
 \sum_{\text{critical fibres}}
 \left|\bigcup_{x\in I}\mathcal A_x\right|
 =o_A(4^r/r^2).                                    \tag{TU}
\]

This report does **not** prove (TU).  It proves the following exact
reduction and obstruction classification.

1.  There is an integer anchor cocycle \(F_s(t)\) whose zero set is exactly
    the transported phase set.  A low-multiplicity zero set either has many
    primal--dual deficit mismatches or contains a long nonzero plateau on
    which the two separated deficit itineraries agree term by term.  The
    smallest such plateau has residual \(\pm2\).

2.  Choosing the rightmost accepted phase injects every element of every
    transported union into one actual canonical run exit.  The terminal
    rotor recovers the chosen phase, so this loses no factor \(b\).

3.  At the endpoint of an exit there are two disjoint possibilities.  A
    later primitive component can tie the global maximum; the aggregate of
    all such ambient endpoints in a fixed Gaussian window is

    \[
      O_\varepsilon(4^r/r^{5/2})=o(4^r/r^2).       \tag{0.2}
    \]

    In the fixed terminal-mountain profile this branch is actually empty.

    Otherwise the endpoint contains a unique literal external dual
    shoulder

    \[
      T_s\ne\varnothing,\qquad
      d(\phi\tau^sD)=|T_s|+1.                     \tag{0.3}
    \]

    The minimal exit is exactly

    \[
      T_s=10,\qquad d(\phi\tau^sD)=3.             \tag{0.4}
    \]

4.  If the critical profile terminates at
    \(\partial^p(\tau^sD)=M_{s-p}\), then

    \[
      \boxed{\operatorname {ht}(T_s)\le p.}       \tag{0.5}
    \]

    More precisely, \(\operatorname {ht}(T_s)\) is the largest index of a
    forward staircase block which saturates its Dyck height cap.

5.  The shoulder \(T_s\) is not one of the blocks in the previously
    audited internal corner atlas, which stops at
    \(T_{s-1}\).  A genuine buffered \(y_p=1\) family has the same two
    internal axis-corner coordinates and the same common boundary for every
    filler, while its external \(T_s\) varies.  Thus the coarse P/B/I type,
    corner coordinates, and internal block-length ledger do not determine
    the external shield.  The complete charged roots can retain the filler,
    so no stronger independence is claimed.

6.  The buffered family nevertheless satisfies the desired weighted-union
    saving internally:

    \[
      U_{\rm buf}\le {C\over p}S_{\rm buf}
      =o(S_{\rm buf}).                             \tag{0.6}
    \]

    Hence it is a structural stress test, not a counterexample to (TU).

The exact remaining theorem, for every fixed \(A,\varepsilon\), is a joint
predecessor/profile incidence bound
for the external shoulders in (0.3).  Endpoint marginals, the terminal
profile, and the internal corner atlas separately do not provide it.

## 1. The exact anchor-carry cocycle

Along one actual quotient orbit write

\[
 D_t=\tau^tD=P_t1R_t0S_t
\]

and put

\[
 a_t=\delta(D_t),\qquad
 c_t=d(D_t)=|S_t|+1,\qquad
 \widehat c_t=d(\phi D_t).
\]

The one-step PBBS identities give

\[
 \boxed{a_{t+1}-a_t=c_t-\widehat c_t.}             \tag{1.1}
\]

For a fixed duration \(s\), define

\[
 F_s(t)=a_{t+s}-\sum_{i=0}^{s-1}c_{t+i}.           \tag{1.2}
\]

### Theorem 1.1 (zero-set and carry formula)

A phase \(t\) is a genuine first zero-winding duration-\(s\) start if and
only if

\[
 F_s(t)=0.                                         \tag{1.3}
\]

Moreover, for every \(k\ge0\),

\[
 \boxed{
 F_s(t+k)-F_s(t)
 =\sum_{i=0}^{k-1}
   \bigl(c_{t+i}-\widehat c_{t+s+i}\bigr).}        \tag{1.4}
\]

#### Proof

Telescoping (1.1) gives

\[
 \begin{aligned}
 F_s(t)
 &=a_t-\sum_{i=0}^{s-1}\widehat c_{t+i}\\
 &=a_t-s-\sum_{i=0}^{s-1}(\widehat c_{t+i}-1).
                                                               \tag{1.5}
 \end{aligned}
\]

Thus (1.3) is exactly the ordinary zero-winding ledger.  If it holds, then
for \(0\le h<s\), another application of (1.1) gives

\[
 \begin{aligned}
 a_{t+h}-\sum_{i=0}^{h-1}c_{t+i}
 &=a_t-\sum_{i=0}^{h-1}\widehat c_{t+i}\\
 &=(s-h)+\sum_{i=h}^{s-1}(\widehat c_{t+i}-1)>0.   \tag{1.6}
 \end{aligned}
\]

The expression is also strictly below \(N\), since its first term before
subtraction is \(a_{t+h}<N\).  Hence no earlier ordinary or positive-winding
congruence is possible: the hit is first.  Conversely every first
zero-winding start satisfies its ledger and hence (1.3).

Finally, subtract (1.2) at \(t+1\) and \(t\).  Equation (1.1) cancels the
new terminal \(c_{t+s}\) term and leaves

\[
 F_s(t+1)-F_s(t)=c_t-\widehat c_{t+s}.
\]

Summation proves (1.4). \(\square\)

Both \(c_t\) and \(\widehat c_t\) are positive odd integers.  Once one
phase in a window is accepted, every value of \(F_s\) in that window is
therefore even.

### Corollary 1.2 (exact plateau dichotomy)

Let \(J\subseteq\{0,\ldots,b-1\}\) be the accepted phases for one
transported object, put \(\mu=|J|\), and let

\[
 \mathcal C
 =\{0\le k<b-1:c_{t+k}\ne\widehat c_{t+s+k}\},
 \qquad c=|\mathcal C|.
\]

If \(\mu<b\), the rejected phases contain a consecutive interval on which
\(F_s\) is one fixed nonzero even integer and whose length is at least

\[
 \boxed{\left\lceil{b-\mu\over c+1}\right\rceil.} \tag{1.7}
\]

On this interval one has the literal separated-time identities

\[
 c_{t+k}=\widehat c_{t+s+k}                       \tag{1.8}
\]

at every step.

#### Proof

By (1.4), \(F_s\) is constant between consecutive members of
\(\mathcal C\).  There are at most \(c+1\) constant intervals.  Their
nonzero parts contain \(b-\mu\) positions in total, so one has length at
least (1.7).  Equation (1.8) is precisely the vanishing of the increment
in (1.4). \(\square\)

This has a weighted consequence.  If

\[
 U=\#\{E:\mu(E)>0\},\qquad S=\sum_E\mu(E),
\]

and \(U\ge\eta S\), then at least \(U/2\) objects satisfy

\[
 \mu(E)\le2/\eta.                                  \tag{1.9}
\]

Indeed the number with \(\mu>2/\eta\) is at most \(\eta S/2\le U/2\).
Consequently any failure of a weighted-union little-oh is supported either
by many mismatch indices or by long exact-match plateaux with bounded live
phase multiplicity.  The smallest nonzero plateau residual is \(\pm2\).

This can be stated with the exact asymptotic quantifiers needed here.  The
audited critical capacity envelope gives

\[
 S_{\rm crit}le C_{A,\varepsilon}{4^r\over r^2}. \tag{1.9a}
\]

Let \(K=K(r)\to\infty\) with \(K=o(\sqrt r)\).  The union elements with
\(\mu(E)\ge K\) contribute at most

\[
 {S_{\rm crit}\over K}=o_{A,\varepsilon}(4^r/r^2). \tag{1.9b}
\]

Now let \(L=L(r)\to\infty\) with \(L=o(\sqrt r)\).  For every remaining
element \(1\le\mu(E)<K\), either

\[
 |\mathcal C(E)|>{b\over L},                      \tag{1.9c}
\]

or (1.7) supplies a nonzero paired-deficit plateau of length at least

\[
 {b-K\over b/L+1}=(1-o(1))L,                     \tag{1.9d}
\]

provided, for example, \(K=o(b)\).  Thus the weighted-union gate has the
following exhaustive residual form: a mismatch-rich branch with at least
\(b/L\) separated anchor discrepancies, and a long exact-match shield
branch.  No estimate making either branch little-oh is proved here.

There is also a literal identification when a dead plateau begins
immediately after a start.  If

\[
 F_s(t)=0,\qquad
 F_s(t+1)=\cdots=F_s(t+L)=-2a,qquad a\ge1,
\]

then \(c_t=1\) and (1.4) give

\[
 \widehat c_{t+s}=2a+1.                            \tag{1.10}
\]

Thus the first mismatch is an external endpoint shoulder of semilength
\(a\), while (1.8) is the exact paired-deficit itinerary along the rest of
the shield.  The irreducible unit shield has \(a=1\).

## 2. No loss in passing from transported unions to exits

Fix one full profile in (0.1).  Let \(X_x\), \(x\in\mathbb Z_{2q+1}\), be
the one-defect terminal rotor, indexed so that \(\tau X_x=X_{x+1}\), and
let

\[
 \mathcal T_x
 =\{D:\partial^{p-1}D=X_x\text{ and }D
       \text{ has the fixed full profile}\}.
\]

Let \(\mathcal R_x\subseteq\mathcal T_x\) be the actual duration-\(s\)
top starts and

\[
 \mathcal A_x=\tau^{-x}\mathcal R_x\subseteq\mathcal T_0.
\]

The terminal rotor makes \(\mathcal R_x=\varnothing\) outside the lifted
interval \(I=\{0,\ldots,b-1\}\).  At phase \(b\), the required terminal
block contains the unique bad rotor state.

### Theorem 2.1 (rightmost-phase exit injection)

For each

\[
 E\in\bigcup_{x=0}^{b-1}\mathcal A_x,
\]

let

\[
 x(E)=\max\{x:E\in\mathcal A_x\},
 \qquad D(E)=\tau^{x(E)}E.                         \tag{2.1}
\]

Then \(D(E)\) is a genuine duration-\(s\) start and \(\tau D(E)\) is not.
The map \(E\mapsto D(E)\) is injective, both inside one profile and after
summing over all profiles.  Therefore

\[
 \boxed{
 \sum_{\text{critical fibres}}
 \left|\bigcup_x\mathcal A_x\right|
 \le \#\{\text{actual critical }y_p=1
          \text{ duration-}s\text{ run exits}\}.} \tag{2.2}
\]

#### Proof

By definition, \(D(E)\) starts the return.  If \(x(E)<b-1\), maximality
makes the next phase fail.  If \(x(E)=b-1\), the next terminal block
contains the unique bad rotor state, so it fails before any upper-level
condition is considered.

Moreover

\[
 \partial^{p-1}D(E)=X_{x(E)}.
\]

The rotor states \(X_0,\ldots,X_{b-1}\) are distinct because
\(b<2q+1\).  Hence \(D(E)\) recovers \(x(E)\), and then
\(E=\tau^{-x(E)}D(E)\).  This proves injectivity in a fixed profile.  The
successive pruning ranks of \(D(E)\) recover its full profile, so images
from distinct profiles cannot create an additional multiplicity. \(\square\)

Thus (TU) is reduced without a factor \(b\) to an actual-root exit
incidence.  This is stronger than merely bounding the number of distinct
transported set values.

## 3. Exact endpoint split

Let \(Y\) be a height-\(s\) Dyck root and use its canonical
first-highest-component factorization

\[
 Y=P1R0S.                                           \tag{3.1}
\]

Let \(\alpha(P)\) be the least prefix length at which \(P\) reaches
height \(s-1\).  If \(S\) reaches height \(s\), let \(\sigma(S)\) be
its first such prefix length.

### Lemma 3.1 (exit dichotomy)

One has

\[
 \delta(\tau Y)=
 \begin{cases}
  \sigma(S),&\operatorname {ht}(S)=s,\\
  |S|+1+\alpha(P),&\operatorname {ht}(S)<s,
 \end{cases}                                       \tag{3.2}
\]

and

\[
 d(\phi Y)=\delta(Y)+d(Y)-\delta(\tau Y).          \tag{3.3}
\]

Consequently

\[
 d(\phi Y)\ge3                                    \tag{3.4}
\]

if and only if exactly one of the following disjoint alternatives holds:

* **suffix tie:** \(\operatorname {ht}(S)=s\);
* **internal top shoulder:** \(\operatorname {ht}(S)<s\) and
  \(\alpha(P)<|P|\).

In the second case there is a unique factorization

\[
 P=A\overline F,                                   \tag{3.5}
\]

where \(A\) first reaches height \(s-1\) at its final bit and \(F\) is a
nonempty Dyck word.  For an endpoint \(Y=\tau^sD\), this word is literally
the external dual staircase block:

\[
 \boxed{F=T_s,\qquad d(\phi\tau^sD)=|T_s|+1.}      \tag{3.6}
\]

#### Proof

The block rotation is

\[
 \tau Y=S1P0R.
\]

If \(S\) reaches height \(s\), its first such step is the first maximum
of \(\tau Y\).  Otherwise \(S\) returns to height zero, the displayed one
raises the baseline to one, and the first maximum occurs when \(P\) first
reaches \(s-1\).  This proves (3.2).

The local voltage identity gives (3.3), while

\[
 \delta(Y)=|P|+1,\qquad d(Y)=|S|+1.
\]

If \(S\) reaches height \(s\), at least \(s\) down-steps remain after its
first such visit, so \(\sigma(S)\le|S|-s\).  Equations (3.2)--(3.3) then
give

\[
 d(\phi Y)=|P|+|S|+2-\sigma(S)
 \ge |P|+s+2\ge3.
\]

In the second line of (3.2), therefore,

\[
 d(\phi Y)=1+|P|-\alpha(P).                        \tag{3.7}
\]

The suffix of \(P\) following its first visit to height \(s-1\) is
balanced and every relative prefix has nonpositive height.  Its length is
even, so (3.7) equals one exactly when the suffix is empty and is at least
three otherwise.  Complementing a nonempty such suffix gives the unique
Dyck word \(F\) in (3.5).

For the word-level identification, write \(P=AB\), where \(A\) ends at
the first visit to height \(s-1\).  The exact one-step word is

\[
 \phi Y=\overline R\,1\,\overline S\,0\,
        \overline A\,\overline B.                 \tag{3.7a}
\]

After the displayed zero the path is at height \(s-1\).  Since every
proper prefix of \(A\) has height below \(s-1\), the word \(\overline A\)
first returns (3.7a) to zero at its final bit.  The remaining terminal
Dyck suffix is therefore \(\overline B\).  By definition this is the next
dual block \(T_s\).  Thus \(B=\overline {T_s}\), proving (3.6).
\(\square\)

In particular,

\[
 d(\phi\tau^sD)=3
 \iff T_s=10
 \iff P=A01.                                       \tag{3.8}
\]

The suffix-tie alternative is already negligible.

For the critical profile it is, in fact, empty.  If

\[
 \partial^pY=M_{s-p},\qquad p<s,                  \tag{3.8a}
\]

and the root-level suffix \(S\) had height \(s\), then
\(\partial^pS\ne\varnothing\).  More generally, peak deletion acts
componentwise across root-level Dyck concatenations, so (3.8a) forces

\[
 \boxed{\operatorname {ht}(S)\le p.}              \tag{3.8b}
\]

Otherwise \(\partial^pY\) would retain a nonempty terminal component and
could not be the primitive mountain \(M_{s-p}\).  Thus every critical run
exit is already in the internal-top-shoulder alternative.  The next
theorem records the stronger ambient estimate, which does not require the
profile hypothesis.

### Theorem 3.2 (suffix-tie enumeration)

Let \(G_s(z)\) count height-\(s\) Dyck roots whose canonical terminal
suffix contains a primitive component of height \(s\).  Then

\[
 \boxed{
 G_s(z)
 =C_s(z)\left({z^s\over Q_s(z)^2}\right)^2
 ={z^{2s}\over Q_s(z)^3Q_{s+1}(z)}.}              \tag{3.9}
\]

Uniformly in \(r,s\),

\[
 [z^r]G_s(z)\le C{4^r\over(s+1)^6}.               \tag{3.10}
\]

Hence, for every fixed \(\varepsilon>0\),

\[
 \sum_{s\ge\varepsilon\sqrt r}[z^r]G_s(z)
 =O_\varepsilon(4^r/r^{5/2}).                     \tag{3.11}
\]

#### Proof

A primitive component of exact height \(s\) has series

\[
 H_s(z)=z(C_{s-1}-C_{s-2})
       ={z^s\over Q_{s-1}Q_s}.
\]

The canonical suffix reaches height \(s\) exactly when the word has at
least two height-\(s\) primitive components.  Decomposing an ambient Dyck
root at its first two such components gives the unique product

\[
 C_{s-1}H_sC_{s-1}H_sC_s.
\]

Cassini's continuant identity yields

\[
 C_{s-1}H_s={z^s\over Q_s^2},
\]

which proves (3.9).

At \(z_0=1/4\),

\[
 G_s(z_0)={2\over(s+1)^3(s+2)}\le {2\over(s+1)^4}. \tag{3.12}
\]

We also need an atom estimate; (3.12) alone is insufficient.  The series
\(1/Q_s\) has nonnegative coefficients.  Under its \(z_0\)-normalized
coefficient law, Fourier inversion and the continuant roots

\[
 \rho_{s,k}=\left(4\cos^2{k\pi\over s+1}\right)^{-1}
\]

give

\[
 \sup_n
 {4^{-n}[z^n]Q_s^{-1}\over Q_s(1/4)^{-1}}
 \le {C\over(s+1)^2}.                             \tag{3.13}
\]

Indeed, in

\[
 \left|{Q_s(z_0)\over Q_s(z_0e^{it})}\right|,
\]

retain the two smallest positive roots.  Each contributes at most
\(C(s^{-2})/(s^{-2}+|t|)\); every omitted root-factor ratio is at most one.
The resulting product has integral \(O(s^{-2})\), proving (3.13).

Factor one positive \(1/Q_s\) from (3.9).  The normalized coefficient law
of the remaining positive product convolves with the law in (3.13), and
convolution cannot increase the largest atom.  Combining (3.12)--(3.13)
proves (3.10).  Finally,

\[
 \sum_{s\ge\varepsilon\sqrt r}s^{-6}
 \le C_\varepsilon r^{-5/2},
\]

which proves (3.11), and in particular its restriction to every fixed
Gaussian window. \(\square\)

Combining Theorem 2.1 with (3.8a), the critical transported-union problem
is reduced exactly to the internal-top-shoulder alternative
(3.5)--(3.6).  Theorem 3.2 independently controls suffix ties even without
using the terminal mountain.

## 4. The shoulder height is a saturated forward cap

For a zero-winding return \(D_0,\ldots,D_s\), the exact forward word
identity is

\[
 \boxed{
 P_s=S_{s-1}1S_{s-2}1\cdots S_1 1S_0,\qquad
 S_0=\varnothing.}                                \tag{4.1}
\]

Every \(S_j\) is Dyck and

\[
 \operatorname {ht}(S_j)\le j.                   \tag{4.2}
\]

Assume the suffix-tie alternative has been removed and the endpoint is an
exit.  Define

\[
 j_*=\max\{1\le j<s:\operatorname {ht}(S_j)=j\}. \tag{4.3}
\]

The set is nonempty by Lemma 3.1.

### Theorem 4.1 (exact cap location and profile bound)

The external shoulder in (3.6) satisfies

\[
 \boxed{\operatorname {ht}(T_s)=j_*.}             \tag{4.4}
\]

If, in addition,

\[
 \partial^pD=M_{s-p},                             \tag{4.5}
\]

then

\[
 \boxed{j_*\le p.}                                \tag{4.6}
\]

The same conclusion holds with (4.5) stated at the endpoint, because
\(\partial\tau=\tau\partial\) and \(\tau M_{s-p}=M_{s-p}\).

#### Proof

In (4.1), the block \(S_j\) begins at absolute height \(s-1-j\).  Since
the blocks occur in decreasing order of \(j\), all blocks preceding
\(S_{j_*}\) stay strictly below height \(s-1\), while \(S_{j_*}\) first
reaches it.  Thus the first early visit of \(P_s\) to height \(s-1\)
occurs inside \(S_{j_*}\).

After that visit, the remaining suffix of \(S_{j_*}\) returns to its
baseline \(s-1-j_*\), so the negative shoulder descends exactly \(j_*\)
levels.  Every later block \(S_k\), \(k<j_*\), is based at height
\(s-1-k>s-1-j_*\) and stays above its own baseline.  Hence the shoulder
never descends farther.  Complementation proves (4.4).

For (4.6), interpret simultaneous peak deletion as simultaneous leaf
pruning in the plane tree.  Put \(h=\operatorname {ht}(T_s)\).  At the
first visit to height \(s-1\), the negative contour loop
\(\overline {T_s}\) leaves a vertex \(v\), ascends \(h\) tree edges to its
lowest common ancestor \(w\), and later descends a distinct ordered branch
to a vertex \(v'\) at the same depth.  The marked next edge from \(v'\)
reaches depth \(s\).  Thus \(w\) has two distinct descendant branches of
heights at least \(h\) and \(h+1\).

If \(h>p\), both branches retain an edge incident with \(w\) after \(p\)
leaf-pruning rounds.  The pruned tree therefore still branches at \(w\),
contradicting (4.5), whose tree is a path.  Hence \(h\le p\).  Equation
(4.4) gives (4.6). \(\square\)

The cap restriction alone has no vanishing partition weight.  This can be
seen exactly in the independent forward-array relaxation.  With

\[
 D_j(z)=C_j(z)-C_{j-1}(z)
       ={z^j\over Q_j(z)Q_{j+1}(z)},
\]

one has

\[
 {D_j(1/4)\over C_j(1/4)}={1\over(j+1)^2}.         \tag{4.7}
\]

Thus, under the product Boltzmann law for blocks of caps
\(1,\ldots,p\),

\[
 \Pr(\text{no cap is saturated})
 =\prod_{j=1}^p\left(1-{1\over(j+1)^2}\right)
 ={p+2\over2(p+1)},                               \tag{4.8}
\]

and

\[
 \Pr(\text{at least one saturation})
 ={p\over2(p+1)}\longrightarrow{1\over2}.         \tag{4.9}
\]

More exactly, if

\[
 J=\max\bigl(\{j\ge1:\operatorname {ht}(S_j)=j\}\cup\{0\}\bigr),
\]

then

\[
 \Pr(J=j)
 ={p+2\over(p+1)(j+1)(j+2)}\quad(1\le j\le p),  \tag{4.9a}
\]

and

\[
 \Pr(J\ge j)
 ={p-j+1\over(p+1)(j+1)}.                         \tag{4.9b}
\]

Thus only shoulders whose height tends to infinity have a formal
\(O(1/j)\) tail.  Even the sparse one-shield event has constant limiting
weight: the probability that exactly one cap is saturated tends to
\(3/8\).  Moreover,
the event

\[
 S_1=10,qquad \operatorname {ht}(S_j)<j\quad(2\le j\le p)
\]

has probability

\[
 {3\over16}
 \prod_{j=2}^p\left(1-{1\over(j+1)^2}\right)
 ={1\over4}{p+2\over2(p+1)}\longrightarrow{1\over8}. \tag{4.10}
\]

This is an obstruction only for the independent cap-product relaxation;
it is not a lower bound for actual closed PBBS returns.  It proves that a
successful estimate must use the predecessor return/common-boundary
incidence, not merely the fact that a cap is saturated or that
\(\operatorname {ht}(T_s)\le p\).

There is also an actual-word marginal obstruction.  Given a primitive
Dyck word of height exactly \(s\ge3\), insert \(01\) immediately before
its first up-step reaching height \(s\).  The insertion occurs at height
\(s-1\), drops only to \(s-2\), preserves primitivity and height, and
creates the shoulder \(P=A01\).  The map is injective: delete the two bits
immediately preceding the first height-\(s\) up-step.  Hence the hard
shoulder class has no endpoint-word entropy loss beyond exact-height
selection.

## 5. Coarse internal corner data do not determine the external shield

The P/B/I corner atlas uses

\[
 T_0,\ldots,T_{s-1},\qquad S_1,\ldots,S_{s-1}.
\]

The block \(T_s\) in (3.6) is not one of these listed dual blocks.  The
following genuine family shows that the coarse corner type, corner
coordinates, common boundary, and internal block **lengths** do not
determine it.  It does not show independence from the complete literal
charged roots.

Fix

\[
 s\ge2p-1,\qquad1\le h\le p-2,
\]

and a nonempty Dyck word \(F\) of semilength \(M\) and exact height \(h\).
Put

\[
 D(F)=1^{s-p+1}0^p1^{2p-1}0^{s-h}F0^h.           \tag{5.1}
\]

The direct block-rotation calculation gives

\[
 |S_h|=2M,\qquad |S_{s-1}|=2p,qquad
 |T_{p-2}|=2p,                                    \tag{5.2}
\]

with every other internal \(S_j,T_j\) empty.  Its endpoint excess is
\(\Lambda=2p\).  Therefore its nonoverlap ideal has exactly the two
minimal corners

\[
 \boxed{(p-1,0),\qquad(0,1),}                     \tag{5.3}
\]

both boundary-axis shields, and its common boundary word is always

\[
 \boxed{E=01^p0^{p-1}.}                           \tag{5.4}
\]

On the other hand,

\[
 D_s=1^p0^p1^{s-h-1}F1^{h+1}0^s.                 \tag{5.5}
\]

If \(\delta_F\) is the first position where \(F\) reaches height \(h\),
then the endpoint prefix before its marked height-\(s\) step is

\[
 P_s=1^p0^p1^{s-h-1}F1^h,
\]

and

\[
 |P_s|-\alpha(P_s)=2M+h-\delta_F.                 \tag{5.6}
\]

If \(F=F_1\cdots F_{2M}\), the negative shoulder is

\[
 F_{\delta_F+1}\cdots F_{2M}1^h,
\]

and hence

\[
 T_s=\overline{F_{\delta_F+1}\cdots F_{2M}}\,0^h. \tag{5.6a}
\]

In particular,

\[
 d(\phi D_s)=2M+h-\delta_F+1.                     \tag{5.7}
\]

With \(M,h\) fixed and \(F\) varying, this literal external shoulder
varies while the lengths in (5.2), the corner coordinates/type (5.3), and
the common boundary (5.4) remain fixed.  The literal block \(S_h=F\) and
the complete charged roots do vary and can recover the filler.  The proved
separation is therefore exactly from the coarse internal corner data, not
from the full internal words.

For an edge-disjoint critical-order family, the audited corner charge can
be made quantitative.  If \(\mathcal C(I)\) is the internal minimal-corner
set and \(|\mathcal P|\ge cB_r/\sqrt r\), then

\[
 \sum_{I\in\mathcal P}|\mathcal C(I)|
 \le R|\mathcal P|
 +CB_r\bigl(R^{-1/2}+r^{-1/4}\bigr).              \tag{5.8}
\]

Indeed, there are at most \(R\) antichain corners with \(a+b<R\), while
all larger corners inject into the two-coloured suffix tail.  Choosing
\(R=\lfloor r^{1/3}\rfloor\) gives

\[
 {1\over|\mathcal P|}
 \sum_{I\in\mathcal P}|\mathcal C(I)|
 =O_c(r^{1/3}).                                    \tag{5.9}
\]

Thus all but \(o(|\mathcal P|)\) intervals have, for example, at most
\(r^{5/12}=o(\sqrt r)\) internal corners.  Equations (5.3)--(5.7) show why
this strengthened sparsity still does not control the external shoulder.

## 6. The buffered family has weighted union saving

The separation example is not a transported-union obstruction.  We prove
this for the more general height-capped family in which
\(H=\operatorname {ht}(F)\le h\).

Put \(q=s-p\).  Direct simultaneous peak deletion gives, for
\(0\le j\le p-1\),

\[
 \partial^jD(F)
 =1^{q+1-j}0^{p-j}1^{2p-1-j}0^{s-h-j}
   (\partial^jF)0^h.                               \tag{6.1}
\]

Since \(H\le h\le p-2\), at \(j=p-1\) this becomes

\[
 \partial^{p-1}D(F)
 =1^{q-p+2}0\,1^p0^{q+1},                         \tag{6.2}
\]

which deletes once to \(M_q\).  Hence

\[
 r_{p-1}=q+2,\qquad r_p=q,\qquad r_{p+1}=q-1,
\]

and therefore

\[
 \boxed{y_p=1.}                                    \tag{6.3}
\]

For \(0\le i\le h-H\), literal first-maximum rotation gives

\[
 \boxed{
 D_{s+i}
 =1^{p+i}0^p1^{s-h-1}F1^{h+1-i}0^s.}             \tag{6.4}
\]

Before \(F\), the current height is \(s-h-1+i\), so \(F\) remains below
\(s\) exactly throughout this range; the final displayed up-run first
reaches \(s\) at its last step.  This proves (6.4) inductively.

For completeness, the first-maximum positions \(a_j=\delta(D_j)\) before
this continuation are

\[
 a_j=
 \begin{cases}
  s+2p,&0\le j\le h,\\
  2M+s+2p,&h<j<p-1,\\
  2M+s,&p-1\le j<s,\\
  2M+s+2p,&j=s.
 \end{cases}                                      \tag{6.4a}
\]

The only nonempty primal suffixes in \(0\le j<s\) have

\[
 |S_h|=2M,\qquad |S_{s-1}|=2p.
\]

Substitution in

\[
 a_{j+1}-a_j=|S_j|-|T_j|
\]

shows that the internal dual array has exactly one nonempty block before
the endpoint:

\[
 |T_{p-2}|=2p.                                     \tag{6.5}
\]

At the first excluded continuation, the new external drop occurs at

\[
 j_*=s+h-H
\]

and has

\[
 |T_{j_*}|=2M+H-\delta_F\ge2H>0,                  \tag{6.6}
\]

because at least \(H\) down-steps remain after the first height-\(H\) hit
in \(F\).  Every duration-\(s\) window starting at
\(0\le k\le h-H\) contains (6.5) and excludes (6.6).  The cocycle (1.5)
therefore equals

\[
 F_s(k)=a_k-s-|T_{p-2}|=(s+2p)-s-2p=0.           \tag{6.6a}
\]

The next window includes both (6.5) and the positive block (6.6), while
its starting \(a_k\) is still \(s+2p\), so its cocycle is negative and it
does not vanish.
Thus

\[
 \boxed{\mu(F)\ge h-H+1.}                         \tag{6.7}
\]

Here \(h\le p-2<b\), so all displayed phases lie in the terminally
admissible window.  From (6.4a) and (6.4), with ambient semilength
\(R=M+s+p\), their endpoint excess is exactly

\[
 a_k+a_{s+k}-2R
 =(s+2p)+(2M+s+2p)-2(M+s+p)=2p.                  \tag{6.7a}
\]

Thus all these returns have positive endpoint excess, and
\(\partial\tau=\tau\partial\) preserves their full pruning profile.

Define \(U_{\rm buf}\) as the sum, over the distinct full pruning profiles
of the fillers, of the corresponding fibrewise transported unions, and
define \(S_{\rm buf}\) as the sum of their phase memberships.  The parse
of (5.1) is unique, phase zero is always valid, and \(\tau\) preserves each
profile.  Hence \(U_{\rm buf}\) is exactly the number of allowed fillers,
while \(S_{\rm buf}=\sum_F\mu(F)\).

Now assume compact critical scaling

\[
 \alpha\sqrt M\le h\le\beta\sqrt M               \tag{6.8}
\]

for fixed \(0<\alpha\le\beta<\infty\).  Let
\(C_a(M)=[z^M]C_a(z)\) be the number of semilength-\(M\) Dyck paths of
height at most \(a\).  Summing (6.7) over the fillers gives the exact
layer-cake lower bound

\[
 S_{\rm buf}
 \ge\sum_{F:\operatorname {ht}(F)\le h}
       (h-\operatorname {ht}(F)+1)
 =\sum_{a=0}^h C_a(M).                             \tag{6.9}
\]

For \(h/2\le a\le h\), the first path-graph eigenmode yields

\[
 C_a(M)
 \ge {2\over a+2}\sin^2{\pi\over a+2}
       \left(2\cos{\pi\over a+2}\right)^{2M}
 \ge c_{\alpha,\beta}{4^M\over h^3}.             \tag{6.10}
\]

There are \(\Theta(h)\) such indices, so

\[
 S_{\rm buf}\ge c_{\alpha,\beta}{4^M\over h^2}.  \tag{6.11}
\]

On the other hand,

\[
 U_{\rm buf}=C_h(M)
 \le\operatorname {Cat}_M
 \le C{4^M\over M^{3/2}}
 \le C_\beta{4^M\over h^3}.                       \tag{6.12}
\]

Division proves

\[
 \boxed{
 U_{\rm buf}\le {C_{\alpha,\beta}\over h}S_{\rm buf}
 =o(S_{\rm buf}).}                                \tag{6.13}
\]

This is a genuine actual-PBBS transported-union theorem, but only for the
buffered subclass.  Its deterministic collars already make the whole
subclass stretched-exponentially sparse relative to the ambient rank, so
(6.13) does not prove a new global sector estimate.

## 7. Exact remaining lemma and adversarial audit

For a critical profile \(\pi\), let \(\mathcal E_\pi^{\rm sh}\) be the
set of actual roots \(D\) such that

1. \(D\) starts a duration-\(s\) zero-winding return and \(\tau D\) does
   not;
2. \(s=p+q\le A\sqrt r\), \(\varepsilon\sqrt r\le p,q,b\),
   \(y_p=1\), and
   \(\partial^pD=M_{s-p}\);
3. at \(Y=\tau^sD=P1R0S\), one has
   \(\operatorname {ht}(S)\le p<s\) and
   \(P=A\overline F\) with
   \(\varnothing\ne F=T_s\), \(\operatorname {ht}(F)\le p\).

The smallest sufficient replacement for (TU) is

\[
 \boxed{
 \sum_{\pi}|\mathcal E_\pi^{\rm sh}|
 =o_{A,\varepsilon}(4^r/r^2).}                    \tag{ES_{A,\varepsilon}}
\]

Theorem 2.1 and the suffix-tie exclusion prove that
\((ES_{A,\varepsilon})\) implies
(TU).  The literal smallest unsolved atom inside
\((ES_{A,\varepsilon})\) is

\[
 T_s=10,\qquad d(\phi\tau^sD)=3,                  \tag{7.1}
\]

possibly followed by a long paired-deficit plateau (1.8).  No theorem in
this report makes the sectors \(|T_s|\ge4\) negligible, so they remain in
\((ES_{A,\varepsilon})\).

### Adversarial audit

1. **Actual chronology versus envelopes.**  The cocycle, exit injection,
   endpoint split, height bound, and buffered theorem concern actual PBBS
   roots.  Equations (4.7)--(4.10) are explicitly only a cap-product
   relaxation and are not used as an actual lower bound.

2. **No hidden factor \(b\).**  In Theorem 2.1 the one-defect rotor state
   recovers the rightmost phase before the reference root is recovered.

3. **Disjoint endpoint alternatives.**  A suffix tie and an internal top
   shoulder are separated by \(\operatorname {ht}(S)=s\) versus
   \(\operatorname {ht}(S)<s\).  Both may have a nonempty next dual block;
   nonemptiness of \(T_s\) alone is not the dichotomy.

4. **Coefficient extraction.**  The point value \(G_s(1/4)=O(s^{-4})\)
   is supplemented by the independent \(O(s^{-2})\) largest-atom factor.
   No coefficientwise conclusion is inferred from a point value alone.

5. **Profile scope of (0.5).**  The proof uses the exact mountain endpoint
   \(\partial^pY=M_{s-p}\).  It is not asserted for an arbitrary dual
   block or an arbitrary zero return.

6. **External versus internal corners.**  The existing dual-block list
   stops at \(T_{s-1}\).  The buffered family proves only that its P/B/I
   type, corner coordinates, common boundary, and internal block lengths do
   not determine \(T_s\).  Its literal \(S_h\) and charged roots retain the
   filler, so complete-word independence is not asserted.

7. **No coefficient-one claim.**  Neither (TU),
   \((ES_{A,\varepsilon})\), the full
   critical packing little-oh, nor the contiguous-OR constant-one theorem
   is proved here.
