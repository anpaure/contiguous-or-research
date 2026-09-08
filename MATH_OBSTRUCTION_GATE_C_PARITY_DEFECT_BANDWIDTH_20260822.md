# Gate C: the parity-defect bandwidth obstruction

**Status (2026-08-22).** Every assertion below is proved.  For the
Catalan-switched non-GK central factor, any coherent tour with only \(L\)
missing flags has all its middle windows in \(O(1+L/b)\) parity-split
layers.  Those layers contain only
\[
 O\!\left({1+L/b\over\sqrt b}\right)N
\]
middle targets.  In particular, no collection of \(q-O(b)\) coherent
partial tours can cover a fixed positive fraction of the factor, regardless
of how many candidates exist or how favorable their codegrees are.

Exactly parity-alternating Hamilton cycles are the case \(L\)-bandwidth
zero: all their windows lie in two middle split layers, of total size
\((4/\sqrt{\pi b}+o(b^{-1/2}))N\).  The obstruction does not rule out a
coefficient-one architecture with mesoscopic loss
\(\Omega(b^{3/2})=o(q)\) per tour.

Throughout,
\[
 n=2b,\quad b\ge3\ {\rm odd},\quad
 E=\{0,2,\ldots,2b-2\},\quad O=\{1,3,\ldots,2b-1\},
\quad h={b-1\over2},\quad q=b(b-1),\quad
 N=\binom{2b}{b-1}.                                      \tag{0.1}
\]

## 1. Two exact inputs

The Catalan-switched factor \(\mathfrak F^*\) is obtained from the ordered
Greene--Kleitman central factor by replacing every source \(0D'1\), with
\(D'\) Dyck, by the alternate primitive-Dyck middle \(1D'0\).  Every arc
of \(\mathfrak F^*\) joins opposite coordinate parities.  Indeed, an
unchanged GK flag has arc \(p\to q\), where \(q<p\) are consecutive among
the unpaired positions.  All positions strictly between them are paired
internally, so \(p-q-1\) is even.  The only new arc is
\(0\to2b-1\), which also joins opposite parities.

We also need the exact coherent template.  Let
\(H=(h_0,\ldots,h_{2b-1})\) be a directed Hamilton cycle, let
\(\delta\in\{0,1\}\) be one of its two coherent phases, and index
cyclically modulo \(2b\).  For \(0\le s<b,\ 1\le t<b\), put
\[
\begin{aligned}
 d_s&=s(b+1),\\
 J_{s,t}^{\delta}
 &=\delta+d_s+\bigl([t,b-1]\cup[b+1,b+t]\bigr)\\
 &=\delta+d_s+\bigl([t,b+t]\setminus\{b\}\bigr),\\
 r_{s,t}^{\delta}&=\delta+d_s+b+t.                       \tag{1.1}
\end{aligned}
\]
The corresponding internal flag has middle and arc
\[
 C_{s,t}^{\delta}(H)=\{h_j:j\in J_{s,t}^{\delta}\},
 \qquad h_{r_{s,t}^{\delta}}\longrightarrow
        h_{r_{s,t}^{\delta}+1}.                           \tag{1.2}
\]
To verify this, use antipodal pairs
\(\{h_{\delta+j},h_{\delta+b+j}\}\).  At stage zero, after \(t\) FIFO
replacements, the H-index set is
\([t,b-1]\cup[b+1,b+t]\), and the current/next entrants have indices
\(b+t,b+t+1\).  Advancing one packet translates every index by \(b+1\),
giving (1.1)--(1.2).  The \(b\) packets close because
\(b(b+1)\equiv0\pmod{2b}\).

Every Hamilton edge occurs in exactly \(h\) internal flags.  In (1.1),
the arc-start index is \(\delta+s(b+1)+b+t\).
Since \(\gcd(b+1,2b)=2\), each allowed parity of \(t\) determines one
\(s\), and each parity occurs \(h\) times among \(1\le t<b\).

## 2. Cyclic parity discrepancy

For the Hamilton listing define
\[
 \sigma_i=
 \begin{cases}1,&h_i\in E,\\-1,&h_i\in O,\end{cases}
 \qquad
 k(H)=|\{i:\sigma_{i+1}=\sigma_i\}|.                     \tag{2.1}
\]
Thus \(k(H)\) is the number of same-parity Hamilton edges.

### Lemma 2.1 (interval-minus-point discrepancy)

For every cyclic interval \(I\) of H-indices,
\[
                         \left|\sum_{i\in I}\sigma_i\right|
 \le k(H)+1.                                             \tag{2.2}
\]
Consequently every coherent middle window satisfies
\[
 \boxed{\left|\,2|C_{s,t}^{\delta}(H)\cap E|-b\,\right|
 \le k(H)+2.}                                            \tag{2.3}
\]

#### Proof

Put \(\tau_i=(-1)^i\sigma_i\).  If the Hamilton edge \(i\to i+1\)
crosses parity, then \(\tau_{i+1}=\tau_i\); at a same-parity edge,
\(\tau_{i+1}=-\tau_i\).  Thus the cyclic word \(\tau\) changes sign
exactly \(k(H)\) times.  Any cyclic interval meets at most \(k(H)+1\)
constant-\(\tau\) pieces.  On one such piece,
\(\sum\sigma_i=\sum(-1)^i\tau_i\) has absolute value at most one.
Summing the pieces proves (2.2).

By (1.1), \(J_{s,t}^{\delta}\) is an interval of length \(b+1\) with one
index deleted.  Apply (2.2) and pay at most one for the deleted index.
The resulting sum is
\(|C\cap E|-|C\cap O|=2|C\cap E|-b\), proving (2.3).
\(\square\)

### Lemma 2.2 (overlap forces small bandwidth)

If
\[
 M(H,\delta):=|\mathcal T(H,\delta)\cap\mathfrak F^*|,
\]
then
\[
                         M(H,\delta)\le q-hk(H).          \tag{2.4}
\]

#### Proof

Every same-parity Hamilton edge supports \(h\) distinct tour flags, while
no flag of \(\mathfrak F^*\) has such an arc.  The edge classes are
disjoint, so all \(hk(H)\) flags are missing. \(\square\)

## 3. Universal middle-band capacity

For an integer \(K\ge0\), define the parity band
\[
 \mathcal B_K=
 \left\{C\in{\Omega\choose b}:
       \left|2|C\cap E|-b\right|\le K+2\right\}.          \tag{3.1}
\]

### Theorem 3.1 (near-tour bandwidth obstruction)

Fix \(L\ge0\), put \(K=\lfloor L/h\rfloor\), and let \(\mathscr T\) be
any collection of coherent phase supports satisfying
\[
                         M(H,\delta)\ge q-L              \tag{3.2}
\]
for every member.  Every flag in
\[
 \mathfrak F^*\cap\bigcup_{\mathcal T\in\mathscr T}\mathcal T
\]
has its middle target in \(\mathcal B_K\).  Hence the total number of
distinct retained flags is at most
\[
\begin{aligned}
 |\mathcal B_K|
 &=\sum_{\substack{0\le a\le b\\|2a-b|\le K+2}}
      \binom ba^2\\
 &\le (K+3)\binom bh^2.                                  \tag{3.3}
\end{aligned}
\]

#### Proof

By (2.4), (3.2) implies \(k(H)\le L/h\), hence
\(k(H)\le K\).  Equation (2.3) places every middle window of every
selected tour in \(\mathcal B_K\).  A central factor uses each middle
target at most once, giving the first bound in (3.3).  There are at most
\(K+3\) permitted integers \(a\), and
\(\binom ba\le\binom bh\), proving the second. \(\square\)

Stirling's formula gives
\[
 \binom bh^2={2\over\pi b}\,4^b(1+O(b^{-1})),\qquad
 N={4^b\over\sqrt{\pi b}}(1+O(b^{-1})).
\]
Therefore
\[
 \boxed{{|\mathcal B_K|\over N}
 \le {2(K+3)\over\sqrt{\pi b}}\,(1+O(b^{-1})).}          \tag{3.4}
\]

For every fixed \(C\), taking \(L=Cb\) gives \(K\le3C\), so all
\(q-Cb\) partial tours together cover only \(O_C(N/\sqrt b)=o(N)\)
flags.  More quantitatively, covering at least \(\alpha N\) flags by
tours with a common loss cap \(L\) requires
\[
 L\ge\left({\alpha\sqrt\pi\over4}+o(1)\right)b^{3/2}.     \tag{3.5}
\]
Indeed (3.4) forces
\(K\ge(\alpha\sqrt{\pi b}/2)-3+o(\sqrt b)\), and \(L\ge hK\).
Thus the \(O(b)\)-repair target is impossible in the fixed factor, but
the necessary \(\Omega(b^{3/2})\) loss remains \(o(q)\).

## 4. The exactly alternating orbit

Suppose \(k(H)=0\).  Root the cycle at coordinate \(0\).  It has the
unique form
\[
 H=(0,o_0,e_1,o_1,\ldots,e_{b-1},o_{b-1}),               \tag{4.1}
\]
where \((o_0,\ldots,o_{b-1})\) is a permutation of \(O\) and
\((e_1,\ldots,e_{b-1})\) a permutation of \(E\setminus\{0\}\).  Hence
there are
\[
                         S=b!(b-1)!                      \tag{4.2}
\]
directed cycles and \(2S\) phase supports.

The split statement is exact.  Before the shift in (1.1),
\[
 J_{s,t}^0=[t,b+t]\setminus\{b\}.
\]
The interval has even length \(b+1\), hence equally many even and odd
indices; the deleted index \(b\) is odd.  Since \(d_s=s(b+1)\) is even,
phase zero has \(h+1\) even and \(h\) odd indices in every middle.
The additional phase-one shift swaps them.  Thus
\[
 |C_{s,t}^{0}\cap E|=h+1,\qquad
 |C_{s,t}^{1}\cap E|=h.                                  \tag{4.3}
\]
Conversely, \(S_E\times S_O\) preserves the alternating-cycle family and
is transitive on each of these two split layers.  Since each phase
contains a middle target, its orbit fills the corresponding layer.  The
total accessible middle layer therefore has exact size
\[
 2\binom bh^2,\qquad
 {2\binom bh^2\over N}
 ={4\over\sqrt{\pi b}}\,(1+O(b^{-1}))=o(1).              \tag{4.4}
\]
This proves directly that no collection of exactly alternating tours can
cover a fixed fraction of any central flag factor.

For completeness, the orbit degrees and first moment are also exact.
Let \(\mathfrak F_{a,\epsilon}\) be the complete flags whose arc crosses
parity, whose middle has \(a\) even coordinates, and whose
\(p=C\setminus L\) coordinate has parity \(\epsilon\in\{0,1\}\).  Then
\[
 |\mathfrak F_{a,0}|=\binom ba^2a^2,\qquad
 |\mathfrak F_{a,1}|=\binom ba^2(b-a)^2.                 \tag{4.5}
\]
Put \(a_\delta=h+1-\delta\).  Each phase-\(\delta\) support has \(q/2\)
flags of each \(p\)-coordinate parity.  The group \(S_E\times S_O\) is transitive
on the unrooted cycles and on each flag type; rerooting at \(0\) uses an
even cyclic shift and preserves the phase.  Thus incidence counting gives
degree
\[
 D_{\delta,0}={S(q/2)\over\binom b{a_\delta}^2a_\delta^2},
 \qquad
 D_{\delta,1}={S(q/2)\over
   \binom b{a_\delta}^2(b-a_\delta)^2}.                  \tag{4.6}
\]

Let \(\mathfrak A\) be any central factor and put
\(g_{a,\epsilon}=|\mathfrak A\cap\mathfrak F_{a,\epsilon}|\).
A uniformly random choice among all \(2S\) phase supports has
\[
 \mathbb E|\mathcal T\cap\mathfrak A|
 ={q\over4}\sum_{\delta=0}^1
 \left[
 {g_{a_\delta,0}\over\binom b{a_\delta}^2a_\delta^2}
 +{g_{a_\delta,1}\over
   \binom b{a_\delta}^2(b-a_\delta)^2}
 \right]
 \le {2b\over b-1}.                                      \tag{4.7}
\]
For the inequality, a central factor uses each middle once, so
\(g_{a,0}+g_{a,1}\le\binom ba^2\); both denominators are at least
\(\binom ba^2h^2\), and \(q/(2h^2)=2b/(b-1)\).
Thus a random alternating support has bounded mean overlap even though
the orbit is factorially large.

## 5. Scope

Theorem 3.1 is universal over all \(q-L\) intersections with the fixed
Catalan-switched factor; it is not restricted to one-ascent or exactly
alternating cycles.  It proves that \(L=O(b)\) cannot support fixed-fraction
coverage and that a successful fixed-factor route cannot impose a uniform
per-tour loss cap below the \(b^{3/2}\) scale.

It does not rule out coefficient one: \(b^{3/2}=o(q)\), so a wider
parity-band construction could still have total repair \(o(N)\).  The
new frontier is to construct and match tours with
\(k(H)=\Theta(\sqrt b)\) or larger while controlling the associated
packet and deeper-chain defects, or to prove a stronger obstruction than
the parity bandwidth.

## 6. Finite audit

The companion checker is
scratch/verify_gate_c_parity_defect_bandwidth_20260822.py.  It verifies
the interval discrepancy and coherent-window bounds, the exact alternating
parameterization and layer identities, the orbit degrees, and the first
moment.  It is confirmatory; all general proofs are above.
