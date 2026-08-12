# Audit of the recursive rectangle chronology cut, including all three shores

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is used.

**Scale extension audited subsequently.** The fixed-slice prefix argument in
MATH_OBSTRUCTION_RECTANGLE_ADAPTIVE_CHRONOLOGY_HALL_CUT_20260726.md
extends the conclusion below from the phase choice \(q\le r<2q\) to every
\[
 q=A\sqrt m+O(1),\qquad q\le r=o(m).
\]
For the maximal all-shore alphabet it gives
\(\widehat n\le2r-3q/2\) with probability \(1-o(1)\), and hence the exact
capacity ratio is at most \(\exp(-q^2/(4r))=o(1)\). I independently
audited the fixed-slice variance, the two prefix means, and this product
inequality; all pass. Thus the stronger conclusion is
\(M_q^+=(e^{-A^2}-o(1))W\) throughout the full sublinear range.

## 0. Verdict

The canonical first-\(r\) chronology gives a genuine global Hall
obstruction to tensor rectangles equipped with arbitrary context-dependent
recursive block orders.

The fixed-shore calculation is correct. It has the following stronger
all-shore form.

Partition \(2m\) coordinates into ordered six-blocks, up to a bounded
remainder. In one block put

\[
 P=\{u,v\},\qquad A=\{a,b,c,d\},\qquad
 \mathcal E=P*A.                                                   \tag{0.1}
\]

Thus \(|\mathcal E|=8\), at local rank two. Allow all three perfect
matchings of \(A\). The union of their upper edge traces is

\[
 \mathcal C^+
 =
 \{P\cup\{a\}:a\in A\}
 \ \dot\cup\
 \{\{p,x,y\}:p\in P,\ \{x,y\}\in\tbinom A2\},                    \tag{0.2}
\]

so \(|\mathcal C^+|=4+12=16\). Every member of \(\mathcal C^+\)
determines one literal physical edge of \(\mathcal E\), and any collection
of such edges in distinct blocks can be placed simultaneously in a tensor
rectangle resolution by choosing a matching separately in each block.

For a rank-\((m+q)\) target \(T\), erase all block letters except
\(E\), meaning a restriction in \(\mathcal E\), and \(C\), meaning a
restriction in \(\mathcal C^+\). Put

\[
                         k=r-q+1.                                  \tag{0.3}
\]

Let \(b(T)\) be the \(k\)-th \(E\)-block, and let \(n(T)\) be the number
of \(C\)-blocks strictly before \(b(T)\). Then:

1. the number of canonical first-\(r\) rectangle macrocells in which
   \(T\) is an upper block-simple \(q\)-face is exactly
   \[
                              \binom{n(T)}q;                         \tag{0.4}
   \]
2. if \(\mathcal T_n\) is the target stratum \(n(T)=n\), then every
   exact owner-one choice of rectangle shores and recursive context orders
   reaches at most the fraction
   \[
      \boxed{
      {R(\mathcal T_n)\over|\mathcal T_n|}
      \le {\,\binom nq\,\over 2^q\binom rq};}                       \tag{0.5}
   \]
3. if \(q=A\sqrt m+O(1)\), \(A>0\), and
   \[
                              q\le r<2q,                            \tag{0.6}
   \]
   then a constant \(c_A>0\) of all rank-\((m+q)\) targets satisfy
   \[
                              n(T)\le r-1.                          \tag{0.7}
   \]

On (0.7), (0.5) is at most

\[
 {1\over2^q}{\binom{r-1}q\over\binom rq}
 ={r-q\over r\,2^q}
 <2^{-q-1}.                                                       \tag{0.8}
\]

The canonical bad-middle leave is \(e^{-\Omega(m)}W\). Consequently the
number of upper holes obeys

\[
 \boxed{
 M_q^+\ge
 (c_A-o(1))\binom{2m}{m+q}
 =\bigl(c_Ae^{-A^2}-o(1)\bigr)W.}                                 \tag{0.9}
\]

This closes the proposed single-atlas A/S combination at coefficient one:
arbitrary cycle-dependent block orders, arbitrary affine phases, and all
three local rectangle shores still leave \(\Theta_A(W)\) upper targets at
one Gaussian depth.

The missing primitive is therefore external to a first-\(r\) rectangle
macrocell: it must change the chronology boundary itself, for example by a
phase-compatible adjacent-block transposition or by an owner trade joining
different canonical macrocells. Merely enlarging the within-block shore
menu cannot evade (0.9).

## 1. Local upper edges

Fix a perfect matching \(M=\{E_0,E_1\}\) of \(A\). The two cells

\[
                              P*E_0,\qquad P*E_1                    \tag{1.1}
\]

partition \(\mathcal E\) into physical squares.

An edge in the \(P\)-direction has union \(P\cup\{a\}\), for one
\(a\in A\). An edge in the \(E_j\)-direction has union
\(\{p\}\cup E_j\), for one \(p\in P\). Hence a fixed shore has eight
upper traces:

\[
 \{P\cup\{a\}:a\in A\}
 \ \dot\cup\
 \{\{p\}\cup E:p\in P,\ E\in M\}.                                \tag{1.2}
\]

As \(M\) ranges over the three matchings, every two-set of \(A\) occurs
once, giving (0.2).

Every triple in (0.2) determines its edge uniquely. For \(P\cup\{a\}\)
the edge is

\[
                              \{\{u,a\},\{v,a\}\}.                  \tag{1.3}
\]

For \(\{p,x,y\}\) the edge is

\[
                              \{\{p,x\},\{p,y\}\}.                  \tag{1.4}
\]

Given one such edge in each of several distinct blocks, choose in a block
of type (1.4) the unique matching containing \(xy\), and choose an
arbitrary matching in a block of type (1.3). The product of these local
resolutions contains all prescribed edges simultaneously. Thus no hidden
shore-compatibility loss occurs in the all-shore face count below.

## 2. The exact chronology parsing

For a middle owner \(X\), call a block eligible when its restriction lies
in \(\mathcal E\). Its canonical macrocell varies the first \(r\)
eligible blocks independently over \(\mathcal E\), while freezing every
other block.

Take an upper target \(T\) and suppose it is a block-simple \(q\)-face of
one canonical macrocell. In the \(q\) touched selected blocks, the local
restriction changes from \(E\) at middle rank to \(C\) at target rank. In
the other \(r-q\) selected blocks it remains \(E\). All blocks outside the
macrocell are frozen.

Let \(b(T)\) be the \((r-q+1)\)-st \(E\)-block of \(T\). The \(q\)
touched \(C\)-blocks all occur before \(b(T)\): otherwise the candidate
middle owner would already have \(r\) eligible blocks before that touched
block, contradicting the first-\(r\) rule.

Conversely, choose any \(q\) of the \(n(T)\) convertible \(C\)-blocks
before \(b(T)\), and replace each chosen triple by either endpoint of its
unique edge from Section 1. The chosen blocks become eligible. Together
with the first \(r-q\) pre-existing \(E\)-blocks, they are exactly the
first \(r\) eligible blocks of every corner of the resulting \(q\)-face.
The block \(b(T)\) is the next eligible block and is excluded. Thus the
face lies in one canonical macrocell.

Different choices of \(q\) converted blocks give different first-\(r\)
index sets, hence different macrocells. The \(2^q\) endpoint choices are
the corners of the same physical face and do not create additional
macrocells. This proves (0.4), including the convention
\(\binom nq=0\) for \(n<q\).

## 3. Exact stratum double count

For a canonical macrocell \(\mathcal P\), let its selected eligible blocks
be \(i_1<\cdots<i_r\), and let \(b\) be the next eligible block after
\(i_r\). Define its all-shore gap \(g(\mathcal P)\) to be the number of
blocks of type \(C\) strictly between the selected chronology and \(b\),
including all frozen positions before \(b\) but excluding the selected
blocks themselves.

If a block-simple upper \(q\)-face touches any \(q\) selected blocks, those
blocks become \(C\), the other \(r-q\) selected blocks stay \(E\), and
\(b\) becomes the \((r-q+1)\)-st \(E\)-block of the target. Therefore

\[
                              n(T)=q+g(\mathcal P)                  \tag{3.1}
\]

for every such target from \(\mathcal P\), independent of the touched
set, shore choices, direction order, affine phase, or starting owner.

Let \(M_g\) be the number of canonical macrocells with gap \(g\), and let
\(\mathcal T_{q+g}\) be the corresponding target stratum. We count
incidences

\[
 (\mathcal P,T):
 T\text{ is an all-shore block-simple upper \(q\)-face of }\mathcal P.
                                                                    \tag{3.2}
\]

In one macrocell:

* choose the touched blocks in \(\binom rq\) ways;
* choose one of the \(16\) physical upper edges in every touched block;
* choose one of the \(8\) middle owner states in every untouched block.

Upper traces determine these data uniquely. Hence one macrocell has

\[
 \binom rq16^q8^{r-q}
 =\binom rq\,2^q\,8^r                                  \tag{3.3}
\]

all-shore candidate targets.

By (0.4), every \(T\in\mathcal T_{q+g}\) occurs in exactly
\(\binom{q+g}q\) candidate macrocells. Double counting (3.2) gives

\[
 \boxed{
 M_g\binom rq\,2^q\,8^r
 =|\mathcal T_{q+g}|\binom{q+g}q.}                    \tag{3.4}
\]

An owner-one factor on one macrocell has only \(8^r\) starts. Therefore,
regardless of its shores or recursive orders, it supplies at most \(8^r\)
distinct targets in its stratum. Summing over the \(M_g\) macrocells and
using (3.4) proves

\[
 {R(\mathcal T_{q+g})\over|\mathcal T_{q+g}|}
 \le {M_g8^r\over|\mathcal T_{q+g}|}
 ={\,\binom{q+g}q\,\over2^q\binom rq},
                                                                    \tag{3.5}
\]

which is (0.5). Collisions between different macrocells only decrease the
left side.

For comparison, if one fixes one matching shore \(M\) in advance, the
local upper alphabet has size eight rather than sixteen. The same proof
then gives

\[
 {R_M(\mathcal T_{n,M})\over|\mathcal T_{n,M}|}
 \le {\binom nq\over\binom rq}.                                    \tag{3.6}
\]

Thus the proposed fixed-shore ratio is correct. Formula (3.5) shows that
allowing all three shores strengthens rather than weakens the owner-count
cut after the target universe is enlarged accordingly.

## 4. Positive mass of the low-chronology strata

Put

\[
 p={m+q\over2m}.                                                   \tag{4.1}
\]

Choose every coordinate independently with probability \(p\). Conditioning
on total size \(m+q\) gives the uniform law on the upper target layer.

For one complete six-block,

\[
 e:=\Pr(E)=8p^2(1-p)^4,\qquad
 c:=\Pr(C)=16p^3(1-p)^3.                                          \tag{4.2}
\]

After neutral letters are erased, the successive \(E/C\) letters are
i.i.d., with

\[
 \Pr(C\mid E\text{ or }C)
 ={c\over c+e}={2p\over1+p},\qquad
 a:=\Pr(E\mid E\text{ or }C)={1-p\over1+p}.                        \tag{4.3}
\]

Let \(N_k\) be the number of \(C\)'s before the \(k\)-th \(E\). Then
\(N_k\) has the negative-binomial law determined by (4.3), and

\[
 \{N_k\le r-1\}
 =
 \left\{
 \operatorname{Bin}(r-1+k,a)\ge k
 \right\}.                                                         \tag{4.4}
\]

Since \(k=r-q+1\), write \(r=q+k-1\). The number of trials in (4.4) is

\[
                         r-1+k=q+2k-2.                             \tag{4.5}
\]

For \(q\le r<2q\), one has \(1\le k\le q\). Also, when
\(q=A\sqrt m+O(1)\),

\[
 a={1-p\over1+p}
 ={1\over3}+O_A(m^{-1/2}).                                        \tag{4.6}
\]

We claim that, under the product law,

\[
                         \Pr(N_k\le r-1)\ge c_0                     \tag{4.7}
\]

for an absolute \(c_0>0\) and all sufficiently large \(m\).

If \(k<q/2\), the mean in (4.4) exceeds \(k\) by
\(\Omega(q)\), so a Chernoff bound makes the probability tend to one.
If \(q/2\le k\le q\), its variance is \(\Theta(q)\), while

\[
 (q+2k-2)a-k
 ={q-k-2\over3}+O_A(1).                                           \tag{4.8}
\]

The threshold is therefore at most \(O_A(1)\) above the mean in the
worst case \(k=q\), and is below it otherwise. The Berry--Esseen theorem
for a binomial variable gives a lower bound tending to \(1/2\) in the
worst case, uniformly on this interval. This proves (4.7), for example
with \(c_0=1/4\) after increasing \(m\).

It remains to justify fixed-rank conditioning. The stopping position of
the \(k\)-th \(E\) among the original six-blocks is \(O(q)\) with
probability \(1-e^{-\Omega(q)}\), because \(e\) in (4.2) is bounded away
from zero. Truncate at \(Dq\) blocks for a sufficiently large absolute
\(D\). The event in (4.7), together with this truncation, still has
product probability at least \(c_0/2\) and is measurable on \(6Dq\)
coordinates.

For any realization on those coordinates, the displacement of its local
cardinality from its product mean is at most \(6Dq=O_A(\sqrt m)\).
Stirling's formula, uniformly for a binomial point displaced by
\(O_A(\sqrt m)\) from its mean, gives

\[
 \Pr\!\left(
  |\mathbf S_{\rm rest}|=m+q-y
 \right)
 \ge c_A\Pr(|\mathbf S|=m+q)                                      \tag{4.9}
\]

for every possible local cardinality \(y\), with \(c_A>0\). Averaging
(4.9) over the truncated event proves

\[
 \Pr\{n(T)\le r-1\mid |T|=m+q\}\ge c_A.                           \tag{4.10}
\]

The bounded coordinate remainder changes only the constant. This proves
(0.7).

## 5. The global Hall obstruction

Sum (3.5) over all strata with \(n\le r-1\). For \(n<q\) the candidate
degree is zero. For \(q\le n\le r-1\),

\[
 {\binom nq\over2^q\binom rq}
 \le
 {1\over2^q}{\binom{r-1}q\over\binom rq}
 ={r-q\over r\,2^q}
 <2^{-q-1},                                                       \tag{5.1}
\]

where the last inequality uses \(r<2q\).

Let \(L_q^+\) be the set in (4.10). The good canonical macrocells therefore
hit at most \(2^{-q-1}|L_q^+|\) of its targets. The set of middle owners
with fewer than \(r\) eligible blocks has size

\[
                              u=e^{-\Omega(m)}W,                    \tag{5.2}
\]

because \(r=O(\sqrt m)\) while the expected eligible-block count is
\(\Theta(m)\). Even an arbitrary completion on those owners can add at
most \(u\) distinct targets. Hence

\[
 M_q^+
 \ge(1-2^{-q-1})|L_q^+|-u
 \ge(c_A-o(1))\binom{2m}{m+q}.                                    \tag{5.3}
\]

Finally,

\[
 {\binom{2m}{m+q}\over\binom{2m}{m}}
 =\exp\!\left(
 -{q^2\over m}
 +O\!\left({q\over m}+{q^3\over m^2}\right)
 \right)
 =e^{-A^2+o(1)},                                                  \tag{5.4}
\]

which proves (0.9).

## 6. Exact boundary

The obstruction permits:

* all three rectangle shores, independently by selected block;
* arbitrary context-dependent block permutations and affine phases;
* arbitrary cycle-dependent orders inside every product cell;
* arbitrary correlations among different cell choices; and
* an arbitrary completion of the exponentially small bad-owner leave.

It uses only:

1. the canonical first-\(r\)-eligible chronology;
2. block-simple windows through depth \(q\);
3. owner-one supply \(8^r\) per macrocell; and
4. the local fact that every upper rectangle edge has trace in (0.2).

The block-simple hypothesis is robust to a sparse violation. If \(B_q\)
starts in the global factor have a depth-\(q\) window which uses both
directions of some rectangle block, discard those starts. The remaining
starts obey the chronology cut, while the discarded starts can supply at
most \(B_q\) additional distinct targets. Combining this observation with
the audited full-sublinear estimate gives

\[
 M_q^+\ge(e^{-A^2}-o(1))W-B_q.                                  \tag{6.1}
\]

Consequently any escape based on arbitrary non-sibling-preserving cube
conjugations must create \(\Omega_A(W)\) non-block-simple windows at the
Gaussian depth. An \(o(W)\)-start perturbation of the A/S factor cannot
evade the theorem.

Therefore the lane can escape only by violating one of those four facts.
The smallest constructive escape is a legal owner trade which changes the
first-\(r\) chronology across macrocells, equivalently a phase-compatible
block-transposition primitive. A new within-block carrier, shore, or
recursive order does not address the proved cut.
