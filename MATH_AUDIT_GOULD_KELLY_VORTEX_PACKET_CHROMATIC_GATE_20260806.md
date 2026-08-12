# Gould--Kelly does not close the vortex packet chromatic gate

## Status

This note audits the primary statement and proof of Gould--Kelly,
*Advancing the Rodl Nibble: New bounds on matchings and the list chromatic
index of hypergraphs*, arXiv:2511.11375 (version dated 14 November 2025),
against the `D+2` two-hole packet hypergraph.

The conclusion is negative and quantitative.

Even granting the best possible higher-codegree input, so that the theorem's
parameter `B` reaches its sharp pair-codegree ceiling `Theta(sqrt r)`, the
published list-colouring error

\[
                         B^{-1+\gamma}\log^A D_0
\]

diverges for the literal packet degree `D_0`.  Sparsifying the packet family
cannot repair this within the same theorem: its additional uniformity bound
`B<=D^(1/K)` forces every useful sparsified degree to retain
`log D=Theta(sqrt r log r)`.  Independently, the theorem is a fixed-rank
result.  An explicit inequality used in its proof fails by an exponential
margin when the packet rank is `K=Theta(sqrt r)`.

Therefore Gould--Kelly neither proves

\[
          \chi'(G)=D_0+o(D_0|\mathcal H|/W)
\]

nor supplies an `o(halo)` packet matching through the chromatic reduction.
No claim about the truth of that bound is made here.

## 1. The exact primary theorem

Write `C_j(G)` for maximum `j`-codegree.  Gould--Kelly's list-chromatic
theorem states the following.  If

\[
 {1\over D}\ll {1\over A}\ll\gamma\ll {1\over k}\le1,  \tag{1.1}
\]

`G` is `(k+1)`-bounded with maximum degree at most `D`, and
`C_j(G)<=D_j`, then for every

\[
 1\le B\le
 \min\left\{
 D^{1/(k+1)},
 \sqrt{D/D_2},
 \min_{4\le j\le k+1}(D/D_j)^{1/(j-1)}
 \right\},                                               \tag{1.2}
\]

one has

\[
 \boxed{
       \chi'_\ell(G)\le
       \bigl(1+B^{-1+\gamma}\log^A D\bigr)D.}           \tag{1.3}
\]

These are the parameters in Theorem 1.7 of the primary TeX source (the
theorem labelled `maincolourtheorem`).  In particular, `A` is not a
disposable negative log power: the hierarchy requires it to be a
sufficiently large positive integer after `k,gamma` have been fixed.

The hierarchy has its standard fixed-parameter meaning.  The paper defines
`1/A,b << c` by first fixing `c`, then choosing thresholds `A_0(c),b_0(c)`.
Thus (1.1) does not assert a uniform theorem for `k=k(D)` tending to
infinity.

## 2. Literal packet parameters

Let `G_full` be the full owner/root packet hypergraph and let `G` be the
slice-avoiding packet hypergraph used in the chromatic gate.  Deleting
packets cannot increase a degree or codegree.  For the upper-rich two-hole
packets put

\[
 K=2L=2D_*+4,\qquad L=D_*+2,                             \tag{2.1}
\]

where `D_*=d+1=Theta(sqrt r)` is the source-window length.  To avoid a
collision of notation, `D_*` is the deadline parameter and `D_0` is the
packet degree.  The owner/root packet hypergraph is `K`-uniform, so the
Gould--Kelly parameter is

\[
                         k=K-1=2D_*+3=\Theta(\sqrt r).    \tag{2.2}
\]

The exact degree formula simplifies to

\[
 \begin{aligned}
 D_0
 &=\binom{r-1}{2}\binom r{r-D_*}(L-2)!\\
 &=\binom{r-1}{2}\binom r{D_*}D_*!\\
 &=\binom{r-1}{2}(r)_{D_*}.                              \tag{2.3}
 \end{aligned}

Since `D_*=Theta(sqrt r)=o(r)`, this gives

\[
               \log D_0=\Theta(D_*\log r)
                         =\Theta(\sqrt r\log r),          \tag{2.4}
\]

and

\[
                       D_0^{1/K}=r^{1/2+o(1)}.            \tag{2.5}
\]

The exact pair ledger for `G_full` gives

\[
                C_2(G)\le C_2(G_{\rm full})={2D_0\over r}.\tag{2.6}
\]

Consequently the proved pair input allows the term

\[
                         \sqrt{D_0/D_2}=\sqrt{r/2}.       \tag{2.7}
\]

The actual pair codegree after deletion might be smaller, but the
uniformity term (2.5) is independent of that deletion.  Thus even if every
pair and higher-codegree term in (1.2) is favourable, one can have at best

\[
                              B=\Theta(\sqrt r).          \tag{2.8}
\]

## 3. The published error is already too large

Assume optimistically that (2.8) is allowed by every uncomputed
higher-codegree.  Take any fixed `0<gamma<1`.  From (2.4), for every
integer `A>=1`,

\[
 \begin{aligned}
 B^{-1+\gamma}\log^A D_0
 &\ge
  c\,r^{-(1-\gamma)/2}
       (\sqrt r\log r)^A\\
 &=c\,r^{(A-1+\gamma)/2}(\log r)^A.                     \tag{3.1}
 \end{aligned}

This tends to infinity.  In contrast, the chromatic reduction for the
critical radius-three vortex needs relative excess

\[
             o(|\mathcal H|/W)
             =o(a^5/\sqrt r),
 \qquad a={1\over4}\log_2r+O(1).                         \tag{3.2}
\]

Thus (1.3) is quantitatively vacuous for the desired purpose even under
the fictitious assumptions that the fixed-rank hierarchy applies and all
higher codegrees permit the maximum `B`.

Nor may one repair the hierarchy by feeding the theorem a vastly inflated
degree parameter `D=lambda D_0`.  Its conclusion is multiplied by `D`
itself.  A conclusion of the required form permits only

\[
                  \lambda-1=o(|\mathcal H|/W),           \tag{3.3}
\]

in which case `log(lambda D_0)=(1+o(1))log D_0` and none of the estimates
above or in Section 5 changes.  An inflation large enough to meet a
fixed-rank threshold would already spend far more colours than the vortex
budget.

This failure comes from the logarithm of the **packet degree**, not from a
missing power of `log r` in the halo estimate:

\[
                         \log D_0=\Theta(\sqrt r\log r).  \tag{3.4}
\]

## 4. Degree sparsification cannot rescue Theorem 1.7

One might randomly partition the packets into nearly degree-`d`
subhypergraphs, colour each separately using a disjoint palette, and sum
the colour counts.  Even granting perfect degree and codegree control in
that partition, Theorem 1.7 retains the first term in (1.2):

\[
                              B\le d^{1/K}.               \tag{4.1}
\]

To reach the only useful scale

\[
                         B\ge {\sqrt r\over g(r)},        \tag{4.2}
\]

where `g(r)=r^{o(1)}`, equations (4.1)--(4.2) force

\[
 \log d\ge K\left({1\over2}\log r-\log g(r)\right)
          =\Theta(\sqrt r\log r).                        \tag{4.3}
\]

Hence `log^A d` has exactly the same fatal polynomial-in-`r` scale as in
(3.1).  Conversely, sparsifying to `d=r^{O(1)}` makes

\[
                         d^{1/K}=1+o(1),                  \tag{4.4}
\]

so the theorem returns no near-`D_0` colouring.  There is no intermediate
choice of `d` which keeps both a square-root `B` and a harmless logarithmic
factor.

This is specific to the colouring theorem.  The matching theorem in the
same paper has no `D^{1/K}` term, but it does not colour the regular
multicover, does not force a prescribed vortex leave, and still has the
fixed-rank hierarchy and the error `B^{-1+gamma}log^A D`.

## 5. The fixed-rank quantifier fails explicitly

It is not proof-safe to set `k=Theta(sqrt r)` inside (1.1).  This is more
than a formal objection: the primary proof explicitly uses, among its
hierarchy consequences,

\[
                   \log^5 D\ge2^k(k+1)^{2k+2}.           \tag{5.1}
\]

(This appears in the proof's codegree-family bound immediately before the
display labelled `hypothesis:degratio`.)

For the packet values `D=D_0` and `k=Theta(sqrt r)`,

\[
 \log(\log^5D_0)=O(\log r),                              \tag{5.2}
\]

whereas

\[
 \log\bigl(2^k(k+1)^{2k+2}\bigr)
       =\Theta(k\log k)=\Theta(\sqrt r\log r).           \tag{5.3}
\]

Thus (5.1) fails by an exponential margin.  Equivalently, that proof would
require roughly

\[
                 \log D\ge\exp(\Omega(k\log k)),         \tag{5.4}
\]

while the packet degree has only

\[
                 \log D_0=\Theta(k\log k).               \tag{5.5}
\]

The same fixed-uniformity issue applies to classical
Pippenger--Spencer/Kahn asymptotic edge-colouring statements.  Their
quantifiers do not become growing-rank theorems merely because `D_0` tends
to infinity.

## 6. Other pair-codegree-only bounds are still farther away

A theorem using only `C_2` through the classical exponent

\[
                 (D_0/C_2)^{-1/K}
                 =(r/2)^{-1/K}                           \tag{6.1}
\]

has relative error

\[
                 \exp\left(-{\log(r/2)\over K}\right)
                    =1-o(1),                             \tag{6.2}
\]

because `K=Theta(sqrt r)`.  Thus the Molloy--Reed form and the
pair-codegree Pippenger--Spencer/Kostochka--Rodl scale do not even give an
`o(W)` leave here.  Exploiting the full codegree/cluster structure is
essential.

## 7. The exact missing estimates

There are two logically separate missing inputs.

### 7.1 A packet higher-codegree bound

To make the numerical parameter in a Gould--Kelly-shaped theorem reach

\[
                           B={\sqrt r\over g(r)},          \tag{7.1}
\]

it is sufficient to prove, in addition to the known pair row,

\[
 \boxed{
 C_j(G)\le D_0\left({g(r)\over\sqrt r}\right)^{j-1}
       \quad(4\le j\le K),}                              \tag{7.2}
\]

together with `D_0>=B^K`.  The latter already follows at the right scale
from (2.5).  The theorem deliberately has no `j=3` term in its definition
of `B`; forced triples inside a packet therefore need not satisfy (7.2).

No estimate proved in the current packet ledger implies (7.2): the ledger
determines all pairs and a rare special triple class, not the maximum
codegree of every larger resource configuration.

### 7.2 A growing-rank, log-light colouring theorem

Even (7.2) is not sufficient for the published theorem, by Sections 3--5.
What the vortex reduction actually needs is a theorem uniform for
`K=Theta(sqrt r)` with a conclusion of the form

\[
 \boxed{
     \chi'(G)\le
       D_0\left(1+{g_0(r)\over B}\right),
       \qquad g_0(r)=o(a^5),}                            \tag{7.3}
\]

or any direct packet-specific estimate

\[
                 \chi'(G)=D_0+o(D_0a^5/\sqrt r).         \tag{7.4}
\]

An especially natural cluster formulation would replace the full
codegree sequence by the already proved aggregate overlap parameter

\[
                         \Xi=O(1/\sqrt r)                 \tag{7.5}
\]

and prove

\[
                         \chi'(G)\le D_0(1+O(\Xi)).       \tag{7.6}
\]

Equation (7.6) would be more than enough, since
`Xi=O(1/sqrt r)=o(a^5/sqrt r)`.  It is a proposed packet-specific
edge-colouring theorem, not a consequence of any cited black box.

## 8. Verdict

The exact audit is:

* the proved pair input and, independently, the unavoidable uniformity cap
  both put the useful scale at `B<=Theta(sqrt r)`;
* direct Gould--Kelly has an error which diverges even at that optimistic
  ceiling;
* degree sparsification cannot lower its log term without activating the
  uniformity cap and collapsing `B`;
* the fixed-rank hierarchy is genuinely violated, with the explicit proof
  inequality (5.1) failing exponentially;
* classical pair-only matching/colouring theorems are quantitatively much
  weaker;
* the weakest credible next input is the combination of the full packet
  bound (7.2) and a growing-rank log-light theorem such as (7.3), or the
  direct aggregate-cluster estimate (7.6).

Therefore the exact chromatic gate in
`MATH_THEOREM_VORTEX_BULK_INTEGRAL_MULTICOVER_COPRIME_PERIOD_AND_CHROMATIC_GATE_20260806.md`
remains open.  Gould--Kelly 2025 does not close it.
