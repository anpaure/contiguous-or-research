# Kupavskii--Zakharov spread approximation at the physical-port high-cover gate

Date: 2026-07-26

Status: theorem-grade audit. The published spread-approximation method does
**not** close the high-cover EKR gate.

Primary reference: A. Kupavskii and D. Zakharov, *Spread approximations for
forbidden intersections problems*, Adv. Math. 445 (2024), 109653;
[arXiv:2203.13379](https://arxiv.org/abs/2203.13379).

## 0. Verdict

Use the physical cyclic-strip catalogue on a \(2m\)-element ground set and
the exact target-regular ports from the laminar-port note. Put

\[
 H=\sqrt{m\log m}\,m^{o(1)},\qquad
 h=\sqrt m\,\log m\,L_m,\qquad
 L_m\to\infty,\quad L_m=m^{o(1)},\quad H=o(h).                    \tag{0.1}
\]

Write \(D_1\) for the exact degree of every signed nonmiddle target,
\(D_0=(N_1/W)D_1\) for the middle degree, and \(e_C^\#\) for the
selected port edge of a strip \(C\).

Two complementary facts are proved below.

1. The independent exact target-regular ports admit a full all-order
   codegree profile. For any co-occurring target set \(A\), its codegree
   is controlled by

   \[
   \operatorname{sp}(A)=\left|\bigcup A\right|-\left|\bigcap A\right|,
   \]

   and every member of a nested comparable subflag costs \(O(1/m)\).

2. Ordinary relative spreadness nevertheless fails. Two crossing nested
   flags form an \(s\times s\) interval grid. Every exact target-regular
   port system contains a grid of \((s+1)^2\) targets having conditional
   density at least

   \[
   \frac{c}{s(m)_s^2}                                               \tag{0.2}
   \]

   inside a middle target star. For \(s=m^{1/5}\), \(r\)-spreadness
   would force

   \[
   \log r\le \frac{2\log m+o(\log m)}s=o(1).                        \tag{0.3}
   \]

Thus the ambient family is not \((r,1)\)-spread for any fixed \(r>1\),
whereas Kupavskii--Zakharov require
\(r>2^{12}\tau\log_2(2k_{\rm port})=\Omega(\log m)\).
The grid has \(m^{2/5+o(1)}\) vertices, below the high-cover scale

\[
q_*\asymp\frac1{\widehat\rho_m\sqrt m}
 =\frac{\sqrt m}{(\log m)L_m}\,m^{o(1)}.                           \tag{0.4}
\]

So even a version testing conditional codegrees only through order \(q_*\)
would fail. The desired high-cover bound remains open. A successful
replacement must charge a flag rectangle by its boundary complexity
\(O(s)\), not by its \((s+1)^2\) implied targets.

## 1. Setup

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}.
\]

A physical strip has a core \(K\), \(|K|=m-h\), and an active cyclic
order \(z_0,\ldots,z_{2h-1}\). Its targets are

\[
K\cup I_z(t,h+a),\qquad -H\le a\le H,\quad t\in\mathbb Z_{2h}.     \tag{1.1}
\]

The raw degree of a rank-\((m+a)\) target is

\[
D_a=\frac{(m+a)!(m-a)!}{2(m-h)!^2}.                                \tag{1.2}
\]

At every signed nonmiddle target of depth \(q=|a|\), independently choose
a uniform \(D_1\)-subset of its \(D_q\) incident strips. Therefore

\[
\theta_q=\frac{D_1}{D_q}=\frac{N_q}{N_1},                           \tag{1.3}
\]

while all middle incidences are retained. If \(M\) is the strip count,

\[
2hM=N_1D_1=WD_0.                                                    \tag{1.4}
\]

For a target set \(A\), write
\[
d^\#(A)=\#\{C:A\subseteq e_C^\#\}.                                 \tag{1.5}
\]

## 2. Raw span and comparable flags

### Lemma 2.1 (Boolean-span multicodegree)

If a nonempty target set \(A\) occurs in one raw strip, then, with

\[
\alpha_m=\frac{h+H}{m-H}=m^{-1/2+o(1)},                             \tag{2.1}
\]

\[
\boxed{\mathbb E d^\#(A)\le D_1\alpha_m^{\operatorname{sp}(A)}.}    \tag{2.2}
\]

#### Proof

Fix \(S_0\in A\), \(|S_0|=m+a_0\), and put
\(I=\bigcap A\), \(U=\bigcup A\). A strip containing \(A\) has its core
inside \(I\) and its excluded \((m-h)\)-set inside \([2m]\setminus U\).
Ignoring all interval constraints except that for \(S_0\) gives

\[
\frac{d_{\rm raw}(A)}{D_{a_0}}
\le
\frac{\binom{|I|}{m-h}}{\binom{m+a_0}{m-h}}
\frac{\binom{2m-|U|}{m-h}}{\binom{m-a_0}{m-h}}.                    \tag{2.3}
\]

For \(u=|S_0\setminus I|\), \(v=|U\setminus S_0|\), the two ratios are

\[
\frac{(h+a_0)_u}{(m+a_0)_u},\qquad
\frac{(h-a_0)_v}{(m-a_0)_v}.                                      \tag{2.4}
\]

Every factor is at most \(\alpha_m\), and \(u+v=\operatorname{sp}(A)\).
If \(S_0\) is nonmiddle, its selection probability changes \(D_{a_0}\)
to \(D_1\). If all members of \(A\) are middle, use \(D_0\le D_1\).
\(\square\)

### Lemma 2.2 (nested flags pay \(m^{-1}\) per member)

If

\[
S_0\subsetneq S_1\subsetneq\cdots\subsetneq S_\ell\subseteq A,     \tag{2.5}
\]

then

\[
\boxed{\mathbb E d^\#(A)\le D_1(C/m)^\ell}                         \tag{2.6}
\]

for an absolute \(C\).

#### Proof

Put \(g_i=|S_i\setminus S_{i-1}|\) and \(d=\sum_i g_i\le2H\).
First fix a saturated chain of all \(d+1\) ranks between the endpoints.
Writing \(N=2m-|S_0|=m-a_0\), the endpoint-pair formula is

\[
\frac{d_{\rm raw}(S_0,S_\ell)}{D_{a_0}}
 =\frac{d+1}{\binom Nd}.                                            \tag{2.7}
\]

For a split with \(u\) new elements on one side and \(d-u\) on the
other, a strip supports \(\binom du\) saturated interval chains. The
\(d+1\) splits have equal multiplicity, and the symmetric group on
\(S_\ell\setminus S_0\) is transitive on the \(d!\) saturated set
chains. Double counting gives

\[
\frac{d_{\rm raw}(\text{saturated chain})}{D_{a_0}}
 =\frac{2^d}{(N)_d}.                                                 \tag{2.8}
\]

The prescribed chain has at most \(\prod_i g_i!\) saturated refinements,
so

\[
\frac{d_{\rm raw}(S_0,\ldots,S_\ell)}{D_{a_0}}
\le \frac{2^d\prod_i g_i!}{(m-H)_d}.                               \tag{2.9}
\]

Since \(d\le2H=o(m)\), \((m-H)_d\ge(m-3H)^d\), and uniformly for
\(1\le g\le2H\),

\[
\frac{2^g g!}{(m-3H)^g}\le\frac Cm.                                \tag{2.10}
\]

Factor (2.9) over the gaps and then apply port selection as in Lemma 2.1.
\(\square\)

Thus adjacent comparable codegrees iterate at the correct
\((C/m)^\ell\) scale. Pure nested flags are not the obstruction.

### Lemma 2.3 (span versus cardinality)

If \(A\) consists of \(t\) distinct targets of one strip, then

\[
\operatorname{sp}(A)\ge\frac{\sqrt t-1}{2}.                         \tag{2.11}
\]

#### Proof

Fix \(S_0\in A\), and let \(s=\operatorname{sp}(A)\). Every \(T\in A\)
has \(|S_0\triangle T|\le s\). For \(s<h-H\), the two active intervals
overlap and have a unique common lift; both the rank difference and
start displacement are at most \(s\). Hence there are at most
\((2s+1)^2\) possibilities. If \(s\ge h-H\), the conclusion follows
from \(t\le2h(2H+1)=o(h^2)\). \(\square\)

## 3. Simultaneous all-order selected codegrees

### Theorem 3.1

The independent exact target-regular ports can be chosen simultaneously
with the earlier width, off-edge-star, and pair bounds and so that every
nonempty co-occurring target set \(A\) satisfies

\[
\boxed{
d^\#(A)\le
2D_1\min\left\{
 \alpha_m^{\operatorname{sp}(A)},(C/m)^{\ell(A)-1}
\right\}+\Lambda_m,}                                                \tag{3.1}
\]

where \(\ell(A)\) is its largest comparable-chain size and

\[
\Lambda_m=C_0(\log M+hH).                                           \tag{3.2}
\]

#### Proof

For fixed \(A\), the indicators that candidate strips were selected at
every target of \(A\) are negatively associated: fixed-size sampling at
one target is negatively associated; independent target blocks preserve
this; and increasing products on disjoint strip-coordinate blocks
preserve it. Lemmas 2.1--2.2 bound the mean. The Chernoff--Bernstein
bound gives

\[
\Pr[d^\#(A)>2\mathbb E d^\#(A)+\Lambda_m]
\le e^{-c\Lambda_m}.                                                \tag{3.3}
\]

Every \(A\) with nonzero raw codegree is a subset of the
\(2h(2H+1)\)-target raw edge of some strip. Thus there are at most

\[
M\,2^{2h(2H+1)}                                                     \tag{3.4}
\]

sets to check. A sufficiently large \(C_0\) makes (3.3) summable over
(3.4), simultaneously with all earlier port events. \(\square\)

Equation (3.1) is a full higher-codegree **profile**, not ordinary
\(r\)-spreadness: its exponent is boundary/span complexity and need not
be proportional to \(|A|\).

## 4. A deterministic crossing-flag grid

The failure of cardinality-based spreadness is forced by exact target
regularity and occurs well below the high-cover scale.

### Theorem 4.1 (dense selected interval grid)

Let any port system have degree \(D_1\) at every signed nonmiddle target
and retain every middle incidence. If

\[
s\to\infty,\qquad s=o(m^{1/4}),\qquad s\le H,                       \tag{4.1}
\]

then there are a middle target \(S\), ordered distinct elements

\[
a_1,\ldots,a_s\in S,\qquad b_1,\ldots,b_s\notin S,                 \tag{4.2}
\]

and the target grid

\[
\mathcal G(S;\mathbf a,\mathbf b)=
\left\{
(S\setminus\{a_1,\ldots,a_i\})\cup\{b_1,\ldots,b_j\}:
0\le i,j\le s
\right\}                                                          \tag{4.3}
\]

such that

\[
\boxed{
d^\#\bigl(\mathcal G(S;\mathbf a,\mathbf b)\bigr)
\ge\frac{cD_0}{s(m)_s^2}.}                                        \tag{4.4}
\]

#### Proof

Choose an oriented representative \(z_0,\ldots,z_{2h-1}\) for every
strip. For a phase \(t\), define

\[
T_{i,j}^{(t)}=K\cup I_z(t+i,h-i+j),\qquad0\le i,j\le s.             \tag{4.5}
\]

This is (4.3) with \(S=T_{0,0}^{(t)}\),
\(a_r=z_{t+r-1}\), and \(b_r=z_{t+h+r-1}\). Choose base phases

\[
t=0,s+1,2(s+1),\ldots,(g-1)(s+1),\qquad
g=\left\lfloor\frac{2h}{s+1}\right\rfloor.                          \tag{4.6}
\]

The start-index ranges are disjoint, so these \(g\ge ch/s\) grids have
pairwise disjoint target sets inside the strip.

At signed depth \(q\), exactly a fraction \(1-\theta_q\) of all raw
incidences is omitted. Across both signs and all strips, the omissions
through depth \(s\) number

\[
4hM\sum_{q=2}^{s}(1-\theta_q).                                     \tag{4.7}
\]

For \(q=o(\sqrt m)\),

\[
1-\theta_q\le\log\frac{N_1}{N_q}\le Cq^2/m.                        \tag{4.8}
\]

Thus (4.7) is at most \(ChMs^3/m\). Because the selected grids in one
strip are target-disjoint, one omitted incidence destroys at most one.
Relative to the \(Mg\) chosen strip--grid pairs, the destroyed fraction
is

\[
\frac{ChMs^3/m}{Mg}=O(s^4/m)=o(1).                                 \tag{4.9}
\]

There are at most \(W(m)_s^2\) coordinate grids of the form (4.3).
Pigeonholing the surviving pairs and using \(2hM=WD_0\) gives

\[
d^\#(\mathcal G)
\ge\frac{(1-o(1))Mg}{W(m)_s^2}
=\frac{(1-o(1))D_0g}{2h(m)_s^2}
\ge\frac{cD_0}{s(m)_s^2}.                                         \tag{4.10}
\]

\(\square\)

The grid is the Cartesian closure of two nested endpoint flags. Each
flag separately has the favorable behavior of Lemma 2.2, but the
\((s+1)^2\) target vertices encode only \(2s\) ordered boundary elements.

### Corollary 4.2 (relative spread fails below \(q_*\))

Condition the labelled ambient port family \(\mathcal A\) on the middle
target \(S\) from Theorem 4.1. If \(\mathcal A(S)\) were \(r\)-spread,
then

\[
\frac{c}{s(m)_s^2}\le r^{-((s+1)^2-1)}.                             \tag{4.11}
\]

Consequently

\[
\boxed{
\log r\le
\frac{2s\log m+O(s^2/m+\log s)}{s^2+2s}
=\frac{2\log m+o(\log m)}s.}                                      \tag{4.12}
\]

Taking \(s=\lfloor m^{1/5}\rfloor\) gives \(r=1+o(1)\), while the
test set has

\[
(s+1)^2-1=m^{2/5+o(1)}=o(q_*).                                    \tag{4.13}
\]

Thus even a hypothetical relative-spread definition testing only target
sets of size at most \(q_*\) would fail.

## 5. Exact failure of the published hypotheses

Kupavskii--Zakharov call \(\mathcal A\) \((r_0,q)\)-spread if
\(\mathcal A(B)\) is \(r_0\)-spread for every \(|B|\le q\).
Their Theorem 11, specialized to ordinary intersection, assumes

\[
r_0\ge2\tau q,\qquad
r_0>2^{12}\tau\log_2(2k),                                          \tag{5.1}
\]

where \(k\) is the maximum ambient edge size. Their Theorem 12, which
makes a nontrivial intersecting approximation quantitatively small,
assumes

\[
\varepsilon r\ge2^{17}q\log_2q.                                   \tag{5.2}
\]

Here

\[
k=k_{\rm port}=\Theta(h\sqrt m)=m^{1+o(1)},                        \tag{5.3}
\]

so (5.1) requires \(r_0=\Omega(\log m)\). Corollary 4.2 gives
\(r\le1+o(1)\) already after conditioning on one middle target.
Therefore the required \((r_0,q)\)-spread hypothesis fails for every
\(q\ge1\), by an unbounded factor.

There is also a simpler atom obstruction. Exact target regularity fixes
the average edge size at

\[
2h+4h\sum_{q=1}^{H}\frac{N_q}{N_1}=\Theta(h\sqrt m).                \tag{5.4}
\]

The independent ports may be chosen, by lower-tail Chernoff and a union
bound, so that every edge has this order of size. Moreover

\[
\log M=(2\log2+o(1))m,\qquad h\sqrt m=m\log m\,L_m.                 \tag{5.5}
\]

Any \(r\)-spread probability measure supported on at most \(M\) sets of
size at least \(ch\sqrt m\) has an atom of mass at least \(1/M\).
Testing spreadness on that atom's full set yields

\[
\log r\le\frac{\log M}{ch\sqrt m}
=O\left(\frac1{(\log m)L_m}\right).                                \tag{5.6}
\]

The grid obstruction is stronger: it survives one-target conditioning
and uses only \(o(q_*)\) further targets.

The robust-sunflower random-bipartition step also visibly fails. A
uniform random half of the target universe contains some complete port
edge with probability at most

\[
M\,2^{-ch\sqrt m}=o(1),                                             \tag{5.7}
\]

whereas the spread lemma needs this probability bounded away from zero.
This is a failed structural hypothesis, not a constant loss.

## 6. Why the numerical conclusion would otherwise have sufficed

At the optimized width,

\[
\widehat\rho_m=O((\log m)L_m/m),\qquad
q_*\asymp\sqrt m/((\log m)L_m).                                    \tag{6.1}
\]

If a flag-aware theorem supplied effective spread \(r\asymp m\), take

\[
\varepsilon_m=\frac1{\sqrt m\sqrt{L_m}}=o(m^{-1/2}).                \tag{6.2}
\]

Then

\[
\frac{q_*\log q_*}{\varepsilon_m}
=O(m/\sqrt{L_m})=o(m),                                              \tag{6.3}
\]

so (5.2) would hold with room. The required
\(o(D_1/\sqrt m)\) precision is therefore compatible with the physical
\(D_1/m\) adjacent-flag scale. What fails is converting laminar local
sparsity into ordinary target-cardinality spreadness.

The exact missing replacement is:

> **Flag-compressed high-cover theorem (open).** In the physical
> cyclic-strip port hypergraph, every intersecting family of target-cover
> number at least \(q_*\) has size \(o(D_1/\sqrt m)\), with interval
> rectangles charged by endpoint-boundary complexity rather than by the
> number of implied target vertices.

## 7. Final status

Proved here:

1. the all-order selected codegree profile (3.1);
2. the \(O(1/m)\)-per-member bound for nested comparable flags;
3. a deterministic selected \(s\times s\) crossing-flag grid in every
   exact target-regular port system;
4. failure of relative spreadness through
   \(m^{2/5+o(1)}=o(q_*)\) targets; and
5. the exact Kupavskii--Zakharov hypothesis and random-containment step
   that fail.

Not proved:

\[
\tau(\mathcal F)\ge q_*
\quad\Longrightarrow\quad
|\mathcal F|=o(D_1/\sqrt m).
\]

The published spread-approximation/sunflower method cannot prove this
without a new flag-compressed variant.

