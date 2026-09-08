# Lane U: Gaussian tight segments, exact local overlap, and the greedy gate

Date: 2026-07-25

## 0. Verdict

The proposed rank-dependent designation removes the unequal-rank degree
problem exactly, and the proposed local-overlap estimate is true.

Let

\[
 n=2m+1,\qquad H=\lfloor A\sqrt m\rfloor,
 \qquad H=o(b),\qquad b+H<m,
\]

where \(A>0\) is fixed.  In the tight-segment template defined below,
condition on one interval slot carrying a prescribed target \(A_0\).  For
every distinct prescribed target \(B_0\), the sum over all compatible second
slots of the exact conditional probabilities is at most

\[
 \boxed{\frac4m}
 \tag{0.1}
\]

for all sufficiently large \(m\).  The constant is independent of \(b\),
\(H\), the two ranks, and the designated-start subsets.  The hypothesis
\(b+H<m\) is decisive; it prevents disjoint complementary position
intervals.

Put \(N_q=\binom n{m+q}\), \(W=N_0=N_1\),

\[
 p=\left\lfloor\frac Wb\right\rfloor,
 \qquad
 b_q=\left\lfloor\frac{N_q}{p}\right\rfloor
 \quad(-H\le q\le H+1).
 \tag{0.2}
\]

An atom designating \(b_q\) starts in rank \(m+q\) has degrees

\[
 d_q=\frac{b_q|\mathcal E|}{N_q}
     =\left(1+O_A(1/b)\right)\frac{|\mathcal E|}{p}.
 \tag{0.3}
\]

Thus no clones or unequal capacities are needed.  If this actual-target
hypergraph has a matching of size

\[
 \boxed{p-o(p/H),}
 \tag{0.4}
\]

then the selected atoms and literal singleton repairs give a word of length
\(W+o(W)\) covering the entire fixed Gaussian band.  The frozen
diagonalization would then give the constant-one theorem.

However, (0.4) does **not** follow from (0.1)--(0.3).  Two rigorous facts
separate the proved result from the missing theorem.

1. Balanced partite degrees and normalized pair overlap \(O(1/m)\) admit
   simple hypergraphs whose matching number is only one; a projective-plane
   construction is given in Section 6.
2. In the actual tight-segment hypergraph, an independently thinned or
   quasirandom residual of density even a fixed \(\varepsilon<1\) contains
   no atom with high probability.  At the required residual density
   \(o(1/H)\), the entropy deficit is overwhelming.  Hence ordinary
   quasirandom random greedy cannot prove (0.4); a structured reservoir,
   absorber, or global expansion theorem is necessary.

Accordingly, the local-overlap and constant-one implication are proved, but
the near-resolution matching theorem (0.4) remains explicitly unproved.  No
constant-one conclusion is claimed in this report.

---

## 1. The rank-balanced designated atom

Let

\[
 \mathcal Q=[-H,H+1]\cap\mathbb Z,
 \qquad R=|\mathcal Q|=2H+2,
 \qquad L=m+b+H<n.
 \tag{1.1}
\]

For every \(q\in\mathcal Q\), choose an arbitrary designated-start set

\[
 I_q\subseteq\{0,1,\ldots,b-1\},
 \qquad |I_q|=b_q.
 \tag{1.2}
\]

The prefix choice \(I_q=\{0,\ldots,b_q-1\}\) is sufficient, but none of
the overlap estimates requires it.

For an injective word

\[
 x=(x_0,x_1,\ldots,x_{L-1})\in[n]^L_{\ne}
\]

and \(i\in I_q\), define

\[
 A_{i,q}(x)
 =\{x_i,x_{i+1},\ldots,x_{i+m+q-1}\}.
 \tag{1.3}
\]

The largest possible final position is

\[
 (b-1)+(m+H+1)-1=L-1,
\]

so every slot is legal.  Within one fixed rank, different starts give
different targets because the word is injective.  Targets in different
ranks have different cardinalities.  Hence every atom has exact size

\[
 K=\sum_{q=-H}^{H+1}b_q.
 \tag{1.4}
\]

Let \(\widetilde{\mathcal H}\) be the labelled multihypergraph whose edge
occurrences are the injective words \(x\), and whose vertices are the
**actual target subsets** in the ranks \(m+q\).  Parallel word occurrences
representing the same target set system are retained for counting.  A
matching in this multihypergraph projects to a literal matching of simple
atoms because parallel edges share every vertex.

Let \(\mathcal H\) denote the simple quotient obtained by identifying
parallel word occurrences.

### Lemma 1.1 — exact degrees

Put

\[
 c=n-L=m+1-b-H.
 \tag{1.5}
\]

For a target \(X\in\binom{[n]}{m+q}\), its exact labelled-word degree is

\[
 \boxed{
 \widetilde d_q
 =b_q\frac{(m+q)!(m+1-q)!}{c!}
 =\frac{(n)_L b_q}{N_q}.}
 \tag{1.6}
\]

Writing

\[
 \rho_q=N_q-pb_q,
 \qquad 0\le\rho_q<p,
 \tag{1.7}
\]

this becomes

\[
 \boxed{
 \widetilde d_q
 =\frac{(n)_L}{p}
   \left(1-\frac{\rho_q}{N_q}\right).}
 \tag{1.8}
\]

Uniformly in \(q\in\mathcal Q\),

\[
 \widetilde d_q
 =\left(1+O_A(1/b)\right)\frac{(n)_L}{p}.
 \tag{1.9}
\]

#### Proof

Fix a start \(i\) and a target \(X\) of size \(r=m+q\).  The letters in
the interval slot can be ordered in \(r!\) ways.  The remaining \(L-r\)
word positions receive distinct letters from \([n]\setminus X\) in

\[
 (n-r)_{L-r}=\frac{(n-r)!}{(n-L)!}
\]

ways.  Thus one slot contributes \(r!(n-r)!/c!\) words.  The events that
the same \(X\) occupies two different equal-length slots are disjoint,
because two shifted intervals in an injective word have different letter
sets.  Multiplication by \(b_q\) proves (1.6).

Since \(b_q=(N_q-\rho_q)/p\), (1.8) is exact.  For fixed \(A\), the central
binomial ratios give \(N_q\ge c_AW\) uniformly on \(\mathcal Q\), for some
constant \(c_A>0\).  Also \(p\le W/b\).  Therefore

\[
 0\le\frac{\rho_q}{N_q}<\frac p{N_q}=O_A(1/b),
\]

which proves (1.9). \(\square\)

### Lemma 1.2 — simple quotient multiplicity is uniform

Every simple atom in \(\mathcal H\) has the same number \(\mu\) of
injective-word representatives.  Consequently all labelled degrees and all
labelled pair-codegrees are \(\mu\) times their simple-quotient values, and
every normalized overlap ratio transfers exactly to \(\mathcal H\).

#### Proof

Let \(\mathcal F\) be the fixed rank-coloured interval set system on the
position set \([0,L-1]\) given by (1.2)--(1.3), and let
\(U_0=\bigcup_{F\in\mathcal F}F\).  If two injective labellings have the
same image atom, their restrictions to \(U_0\) differ by an automorphism of
the abstract rank-coloured set system \(\mathcal F\).  Conversely every
such automorphism preserves the image atom.  Positions outside \(U_0\) are
invisible and may be filled by any injection from the unused coordinates.
Hence

\[
 \mu=|\operatorname{Aut}(\mathcal F)|
      (n-|U_0|)_{L-|U_0|},
 \tag{1.10}
\]

which depends only on the fixed slot template, not on the image atom.
Dividing incidence counts by \(\mu\) proves the claim. \(\square\)

No assertion that \(\mu\) is merely a core factorial times a reversal
factor is needed; the rank-coloured prefix families may destroy reversal
symmetry.

---

## 2. Exact conditional interval probability

For position intervals

\[
 P=[a,a+r-1],\qquad Q=[y,y+t-1],
 \tag{2.1}
\]

condition on the set of letters in \(P\) being a prescribed set \(A_0\) of
size \(r\).  Put \(u=|P\cap Q|\).  For a prescribed \(t\)-set \(B_0\), the
event that the letters of \(Q\) form \(B_0\) is impossible unless

\[
 |A_0\cap B_0|=u.
\]

When this equality holds, the exact conditional probability is

\[
 \boxed{
 \Pr(Q=B_0\mid P=A_0)
 =\frac1{\binom r u\binom{n-r}{t-u}}.}
 \tag{2.2}
\]

Indeed, the \(u\) common letters form a uniformly random \(u\)-subset of
\(A_0\), and the \(t-u\) new letters form a uniformly random subset of its
complement.  This is the labelled-word probability; unseen word positions
do not alter it.

---

## 3. The local-overlap sum

### Theorem 3.1 — uniform \(4/m\) overlap

Fix a first designated interval \(P=[a,a+r-1]\), a distinct pair of target
sets \(A_0,B_0\), and a second rank of interval length \(t\).  Let
\(T\subseteq\{0,\ldots,b-1\}\) be any designated-start set for that rank.
Then, for all sufficiently large \(m\),

\[
 \boxed{
 \sum_{\substack{y\in T:\\
 |P\cap[y,y+t-1]|=|A_0\cap B_0|}}
 \frac1{
 \binom r{|A_0\cap B_0|}
 \binom{n-r}{t-|A_0\cap B_0|}}
 \le\frac4m.}
 \tag{3.1}
\]

This is uniform for all

\[
 m-H\le r,t\le m+H+1.
\]

#### Proof

Put \(u=|A_0\cap B_0|\), and let

\[
 k_u=|\{y\in T:|P\cap[y,y+t-1]|=u\}|.
\]

The sum in (3.1) is exactly

\[
 \frac{k_u}{\binom r u\binom{n-r}{t-u}}.
 \tag{3.2}
\]

First, every two legal position intervals overlap.  Indeed,

\[
 |a-y|\le b-1,
 \qquad
 \min(r,t)\ge m-H,
\]

and therefore

\[
 |P\cap[y,y+t-1]|
 \ge m-H-b+1>0.
 \tag{3.3}
\]

This removes the dangerous disjoint-complement case.

Suppose first that

\[
 0<u<\min(r,t).
\]

There are at most two possible starts with overlap \(u\):

\[
 y_-=a-t+u,
 \qquad
 y_+=a+r-u.
\]

Hence \(k_u\le2\).  Also \(1\le u\le r-1\), so

\[
 \binom r u\ge r\ge m-H.
\]

Thus (3.2) is at most

\[
 \frac2{m-H}\le\frac4m
\]

eventually.

It remains to consider \(u=\min(r,t)\).  If \(t<r\), put \(d=r-t\ge1\).
The second interval is contained in the first, and

\[
 k_u\le d+1,
 \qquad
 \binom r u\binom{n-r}{t-u}=\binom r d.
 \tag{3.4}
\]

If \(r<t\), put \(d=t-r\ge1\).  The first interval is contained in the
second, and

\[
 k_u\le d+1,
 \qquad
 \binom r u\binom{n-r}{t-u}=\binom{n-r}d.
 \tag{3.5}
\]

If \(r=t\), then \(u=r\) would force \(A_0=B_0\), contrary to the
hypothesis.

In (3.4)--(3.5), the binomial top \(M\) is at least \(m-H\), while

\[
 1\le d\le2H+1.
\]

For \(d=1\), the ratio is at most \(2/(m-H)\).  For \(d\ge2\), the fixed
Gaussian assumption gives \(d\le M-2\) eventually, and hence

\[
 \frac{d+1}{\binom Md}
 \le\frac{2(d+1)}{M(M-1)}
 =O_A(m^{-3/2})
 \le\frac4m.
\]

This proves (3.1). \(\square\)

### Corollary 3.2 — actual-target pair-codegrees

For distinct actual targets \(A_0,B_0\),

\[
 \boxed{
 \frac{\operatorname{codeg}_{\widetilde{\mathcal H}}(A_0,B_0)}
      {\deg_{\widetilde{\mathcal H}}(A_0)}
 \le\frac4m.}
 \tag{3.6}
\]

The same inequality holds in the simple quotient.  Since all degrees are
\(1+O_A(1/b)\) comparable,

\[
 \frac{\operatorname{codeg}(A_0,B_0)}
      {\min(\deg A_0,\deg B_0)}
 \le\frac{4+o_A(1)}m.
 \tag{3.7}
\]

#### Proof

Condition on which of the \(b_q\) first slots contains \(A_0\).  These
events have equal size and are disjoint.  For a fixed first slot, the events
that \(B_0\) occupies different equal-rank slots are also disjoint.  Their
conditional probabilities sum to the left side of (3.1).  Average over the
first slots.  Lemma 1.2 transfers the ratio to the simple quotient.
\(\square\)

The restriction \(A_0\ne B_0\) is necessary: the identical slot gives
conditional probability one.  Allowing position intervals far enough apart
to be complementary also destroys the conclusion.  Notice that \(H=o(b)\)
was not used in Theorem 3.1; only \(b+H<m\) and \(H=o(m)\) were needed.

---

## 4. Exact literal word ledger

For a labelled atom \(x\), define the base windows

\[
 E_j(x)=\{x_j,x_{j+1},\ldots,x_{j+m-H-1}\},
 \qquad 0\le j\le b+2H.
 \tag{4.1}
\]

This is a literal word of exact length \(b+2H+1\).  For every designated
slot \(i\in I_q\),

\[
 \boxed{
 \bigvee_{j=i}^{i+H+q}E_j(x)=A_{i,q}(x).}
 \tag{4.2}
\]

The last coordinate on the right is \(x_{i+m+q-1}\), so there is no
off-by-one or virtual-window convention.

### Theorem 4.1 — conditional Gaussian-band implication

Suppose \(\mathcal H\) has a matching of size

\[
 M=p-\delta.
\]

Emit (4.1) for every selected atom and append every target missed by the
matching once as its literal mask.  Put

\[
 B=\sum_{q\in\mathcal Q}b_q,
 \qquad
 R_0=\sum_{q\in\mathcal Q}\rho_q.
\]

The exact number of uncovered targets is

\[
 U=R_0+\delta B,
 \tag{4.3}
\]

and the exact word length is

\[
 \boxed{
 N_{\rm word}
 =(p-\delta)(b+2H+1)+R_0+\delta B.}
 \tag{4.4}
\]

For all sufficiently large \(m\), \(b_0=b_1=b\).  If
\(\rho_0=W-pb\), then

\[
 \boxed{
 N_{\rm word}-W
 =p(2H+1)+(R_0-\rho_0)
  +\delta(B-b-2H-1).}
 \tag{4.5}
\]

Consequently,

\[
 \boxed{
 N_{\rm word}-W
 \le(4H+2)p+(2H+2)b\delta.}
 \tag{4.6}
\]

In particular,

\[
 H=o(b),qquad \delta=o(p/H)
 \tag{4.7}
\]

imply \(N_{\rm word}=W+o(W)\).

#### Proof

A matching atom covers exactly \(b_q\) distinct actual targets in rank
\(m+q\).  Thus that rank leaves

\[
 N_q-(p-\delta)b_q=\rho_q+\delta b_q
\]

targets, proving (4.3).  Add the module and repair lengths to obtain (4.4).

Since \(p=\lfloor W/b\rfloor\) and \(p>b\) eventually, writing
\(W=pb+\rho_0\), \(0\le\rho_0<b<p\), gives
\(b_0=b_1=b\).  Expanding (4.4) around \(pb=W-\rho_0\) proves (4.5).

There are \(2H+2\) parts, \(b_q\le b\), and \(\rho_q<p\).  Dropping the
negative terms in (4.5) yields (4.6).  Finally \(p=(1+o(1))W/b\), so (4.7)
makes both terms in (4.6) \(o(W)\). \(\square\)

Uniformly on a fixed Gaussian band, \(b_q=\Theta_A(b)\), and therefore

\[
 B=\Theta_A(Hb).
 \tag{4.8}
\]

Thus \(\delta=o(p/H)\) is also the correct deficit scale for this
append-all-misses implementation: a larger matching deficit creates
\(\Theta_A(\delta Hb)\) literal repairs.

### Corollary 4.2 — exact missing matching theorem

The following statement would imply the coefficient-one conjecture.

> **Tight-segment near-resolution (TSNR).**  For every fixed \(A>0\), with
> \(H=\lfloor A\sqrt m\rfloor\), there is a choice
> \(H=o(b)\), \(b+H<m\), for which the actual-target hypergraph
> \(\mathcal H\) has a matching of size \(p-o(p/H)\).

Indeed, Theorem 4.1 would give a \(W+o(W)\) literal word for every fixed
Gaussian band.  The already frozen fixed-window diagonalization then gives
constant one.

**TSNR is unproved.**

---

## 5. Why ordinary quasirandom greedy cannot prove TSNR

The local-overlap theorem is strong but is not a near-resolution theorem.
The tight-segment family has very low entropy compared with its edge size.

### Lemma 5.1 — simple-atom entropy bound

Every designated interval contains the common position core

\[
 J=\{b-1,b,\ldots,m-H-1\},
 \qquad |J|=c=m+1-b-H.
 \tag{5.1}
\]

Consequently the number \(M_{\rm simp}\) of distinct simple atoms satisfies

\[
 \boxed{
 M_{\rm simp}\le\frac{n!}{(c!)^2}.}
 \tag{5.2}
\]

Moreover,

\[
 \log M_{\rm simp}
 =O\bigl(m+(b+H)\log m\bigr).
 \tag{5.3}
\]

On the other hand,

\[
 \boxed{K=\Theta_A(bH),}
 \tag{5.4}
\]

and hence

\[
 \boxed{\frac{\log M_{\rm simp}}K=o(1).}
 \tag{5.5}
\]

#### Proof

Permuting the \(c\) letters in the common core changes the injective word
but no target in the atom.  Since the total labelled-word count is

\[
 (n)_L=\frac{n!}{c!},
\]

every simple atom has at least \(c!\) representatives, proving (5.2).

Put \(r=m-c=b+H-1\).  Using

\[
 \frac{n!}{m!(m+1)!}=W\le2^n
\]

and bounding the two factorial quotients from \(c!\) to \(m!\) and
\((m+1)!\) by \(n^{2r+1}\) gives (5.3).

For fixed \(A\), \(N_q\ge c_AW\) throughout \(\mathcal Q\).  Since
\(p\le W/b\),

\[
 b_q\ge c_Ab-1\ge\frac{c_A}2b
\]

eventually.  Summing over \(2H+2\) parts proves the lower half of (5.4),
while \(b_q\le b\) proves the upper half.  Finally

\[
 \frac{m}{bH}=O_A(H/b)=o(1),
 \qquad
 \frac{(b+H)\log m}{bH}=O(\log m/H)=o(1),
\]

which proves (5.5). \(\square\)

### Theorem 5.2 — a random residual contains no atom

Independently retain every actual target vertex with probability
\(\varepsilon\in(0,1)\).  If \(\varepsilon\) is any fixed constant smaller
than one, then the probability that the retained hypergraph contains even
one complete simple atom tends to zero.  The conclusion is stronger at
\(\varepsilon=O(1/H)\).

#### Proof

Every simple atom contains exactly \(K\) distinct vertices, so its survival
probability is \(\varepsilon^K\).  By the union bound and Lemma 5.1,

\[
 \mathbb E[\#\text{ surviving atoms}]
 \le M_{\rm simp}\varepsilon^K.
\]

For fixed \(\varepsilon<1\), its logarithm is

\[
 o(K)-K\log(1/\varepsilon)\longrightarrow-\infty.
\]

Markov's inequality proves the first statement.  Taking
\(\varepsilon=O(1/H)\) only increases the negative term to
\(-(1+o(1))K\log H\). \(\square\)

If a matching has size \(p-\delta\), the residual density in rank \(q\) is

\[
 \frac{\rho_q+\delta b_q}{N_q}
 =O_A\left(\frac1b+\frac\delta p\right).
 \tag{5.6}
\]

Under the desired hypotheses this is \(o(1/H)\).  Theorem 5.2 therefore
shows that a proof which keeps the residual close to independent or
quasirandom thinning must freeze long before the required endpoint.  This
does not prove TSNR false: a successful absorber could maintain a highly
structured residual containing prescribed atoms.  It does prove that
ordinary quasirandom random greedy is not the requested theorem.

---

## 6. Pair overlap alone is logically insufficient

There is no abstract capacitated matching theorem deriving TSNR solely from
balanced degrees and normalized pair-codegree \(O(1/m)\).

### Proposition 6.1 — projective-plane counterexample

Let \(\Pi\) be a projective plane of order \(Q\), and fix a point \(z\).
The \(Q+1\) lines through \(z\), with \(z\) deleted, form \(Q+1\) vertex
parts of size \(Q\).  Take as hyperedges all projective lines not through
\(z\).

Then:

* every edge meets every part exactly once;
* every vertex has degree \(D=Q\);
* every distinct vertex pair has codegree at most one, so
  \(\Delta_2/D=1/Q\);
* the fractional matching number is \(Q\); but
* every two edges intersect, so the integral matching number is one.

Taking \(Q\ge m\) gives normalized pair-codegree \(O(1/m)\) with a maximal
integrality gap.  Disjoint copies, with the copy permutation included in the
symmetry group, can make the vertex set and edge set arbitrarily large
without repairing the gap.

#### Proof

Every line not through \(z\) meets each line through \(z\) in one point, so
it is a transversal of the parts.  A point different from \(z\) lies on
\(Q+1\) lines, exactly one of which passes through \(z\); hence its degree
is \(Q\).  Two points determine at most one line.  Finally every two
projective lines meet, and two lines not through \(z\) cannot meet at
\(z\).  Thus no two hyperedges are disjoint. \(\square\)

This counterexample does not assert that the tight-segment hypergraph lacks
a large matching.  It proves that Theorem 3.1 cannot, by itself, be promoted
to the required matching theorem.

---

## 7. Precise proved/conditional boundary

### Proved

1. Rank-dependent start counts \(b_q=\lfloor N_q/p\rfloor\) make all
   actual-target degrees \(1+O_A(1/b)\) regular, without clones.
2. The exact conditional local-overlap sum is at most \(4/m\), uniformly
   through every fixed Gaussian window.
3. Parallel injective-word representations have uniform multiplicity, so
   all normalized degree/codegree statements transfer to the simple atom
   hypergraph.
4. A matching deficit \(\delta=o(p/H)\) gives an exact literal
   \(W+o(W)\) Gaussian-band word.
5. Balanced degrees plus the local-overlap estimate do not imply that
   matching, and a quasirandom random-greedy residual provably contains no
   atom at the required density.

### Unproved

TSNR: an actual-target matching of size \(p-o(p/H)\), or an absorber/global
expansion theorem yielding one while maintaining a structured residual.

This is now the only missing step in the designated tight-segment route.
The capacity gradient, clone balancing, literal chronology, rounding loss,
and local interval overlap are no longer gaps.

### Independent audits

The interval case split, constant \(4/m\), degree formula, uniform quotient
multiplicity, exact word length, and deficit scale \(o(p/H)\) were checked
independently.  A separate audit confirmed the entropy obstruction and the
projective-plane counterexample.  No audit found a route from local overlap
alone to TSNR.
