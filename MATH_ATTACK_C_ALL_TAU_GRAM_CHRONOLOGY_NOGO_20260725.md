# All-transposition Gram locality: an exact-middle chronology no-go

Date: 2026-07-25

Method: pure mathematics only.  No search, computation, solver, or
probabilistic experiment is used.

## 0. Result and precise boundary

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\frac Wn=\operatorname{Cat}_m,
\qquad H=\lceil L\sqrt m\rceil,
\]

where \(L>0\) is fixed.  At depth \(q\), put

\[
r_q=m-q,\qquad N_q=\binom n{r_q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\]

and for an integral load vector \(\mu_q\) define its exact floor energy by

\[
Q_q(\mu_q)=
\sum_{S\in\binom{[n]}{r_q}}
(\mu_q(S)-c_q)(\mu_q(S)-c_q-1),
\qquad
\mathcal Q_H=\sum_{q=1}^H\frac{Q_q}{c_q}.
\tag{0.1}
\]

The theorem below is an all-transposition obstruction with the same local
quantifiers as the surviving local-minimum gate.  It is not a genuine
lower-shadow counterexample, and the one datum it omits is stated exactly.

### Theorem 0.1 (simultaneous chronology-free local minimum)

Fix \(L>0\).  Along the infinite sequence for which \(n=2m+1\) is prime,
and for all sufficiently large \(m\), there is a decorated exact-middle
wreath system with the following properties.

1.  Its middle rows are the rows of a genuine integral exact wreath factor.
    Every component switch in the ownership overlay with any transposition
    therefore has a genuine integral exact middle factor as its child.

2.  Every decorated row has, at every \(q\le H\), exactly \(n\) distinct
    rank-\(r_q\) targets, and every coordinate occurs in exactly \(r_q\) of
    them.  Thus every integral component-switch child has exact rank mass
    \(W\) and exact point margins \(r_qW/n\).

3.  The initial rank loads \(\mu_q\) are nonnegative integral and satisfy

    \[
    |\mu_q(S)-\mu_q(T)|\le1
    \quad\text{for every edge }ST\text{ of }J(n,r_q).
    \tag{0.2}
    \]

4.  For every coordinate transposition \(\tau\), and for every subset of
    the genuine intrinsic \(\tau\)-ownership components, switching that
    subset does not decrease \(Q_q\) at any depth \(q\le H\).  In
    particular, it does not decrease \(\mathcal Q_H\).  Equivalently, for
    every \(\tau\), its genuine component Gram weights satisfy

    \[
    \sum_{K\in I,\,J\notin I}
    \langle d_K,d_J\rangle_H\le0
    \qquad\text{for every component subset }I.
    \tag{0.3}
    \]

5.  Nevertheless,

    \[
    \liminf_{m\to\infty}\frac{\mathcal Q_H}{W}\ge\frac14,
    \tag{0.4}
    \]

    and hence

    \[
    \frac{\mathcal Q_H}{H\operatorname{Cat}_m}
    \ge
    \left(\frac1{2L}+o(1)\right)\sqrt m
    \longrightarrow\infty.
    \tag{0.5}
    \]

The lower-rank decorations in this theorem are actual labelled subsets and
have all the rowwise and factorwise occurrence counts above.  What is not
asserted is

\[
\mathcal T_q(C)=\mathcal I_{m-q}(C)
\quad\text{simultaneously for all }q,
\tag{0.6}
\]

where the right side is the family of genuine cyclic intervals of the same
owning wreath \(C\).  The decorations are cyclic-orbit designs attached to
the rows, but need not be consecutive intervals in the row's cyclic order,
and the designs at different depths need not be nested.

Consequently, simultaneous signed Gram cut inequalities, exact middle
ownership, nonnegative integral occurrence counts, componentwise
transposition pair-sum preservation, exact row and point margins, and the
integer floor do not imply the local-minimum bound.  Any proof of the
genuine theorem must use the common cyclic-prefix chronology (0.6), or a
consequence which is not already contained in those data.

The rest of the report proves Theorem 0.1.

## 1. The exact occurrence-pair form of local Gram inequalities

Fix a transposition \(\tau\) and one intrinsic ownership component \(K\).
At depth \(q\), let \(a_{K,q}\) be the old-side target histogram and put

\[
d_{K,q}=a_{K,q}-\tau a_{K,q}.
\tag{1.1}
\]

The new side has histogram \(\tau a_{K,q}\).  For a moved target orbit
\(p=\{S,T=\tau S\}\), orient \(p\) and write

\[
x_{K,p}=a_{K,q}(S),\qquad
y_{K,p}=a_{K,q}(T),\qquad
z_{K,p}=x_{K,p}-y_{K,p}.
\tag{1.2}
\]

Switching \(K\) interchanges \(x_{K,p}\) and \(y_{K,p}\).  Therefore every
common component signing preserves the pair total

\[
\ell_p=\mu_q(S)+\mu_q(T).
\tag{1.3}
\]

If the signed difference after switching is \(u_p\), its two loads are
\((\ell_p+u_p)/2\) and \((\ell_p-u_p)/2\).  For any integer \(c\), direct
expansion gives

\[
\begin{aligned}
&(a-c)(a-c-1)+(b-c)(b-c-1)\\
&\qquad =a^2+b^2-(2c+1)(a+b)+2c(c+1).
\end{aligned}
\tag{1.4}
\]

Thus, at fixed \(a+b=\ell\), the floor energy is minimized exactly by the
two balanced integer loads, equivalently by

\[
|a-b|=\ell\bmod2.
\tag{1.5}
\]

If the old difference is \(z_p\), the exact pair-energy increment is

\[
\frac{u_p^2-z_p^2}{2}.
\tag{1.6}
\]

It follows at once that if

\[
|\mu_q(S)-\mu_q(\tau S)|\le1
\tag{1.7}
\]

for every moved pair, no component signing can decrease the depth-\(q\)
energy.  Notice that this conclusion is pointwise in \(q\), so there is no
multirank cancellation issue.

For completeness, this is also precisely the signed Gram condition.  With

\[
\langle u,v\rangle_H
=\sum_{q\le H}\frac{\langle u_q,v_q\rangle_2}{c_q},
\qquad d_I=\sum_{K\in I}d_K,
\tag{1.8}
\]

switching \(I\) changes the load by \(-d_I\).  The invariant midpoint is
orthogonal to every anti-invariant \(d_K\), and hence

\[
\boxed{
\mathcal Q_H(F^I)-\mathcal Q_H(F)
=-\langle d_I,d_{I^c}\rangle_H.}
\tag{1.9}
\]

Thus all-subset local minimality is exactly (0.3).  Equations
(1.3)--(1.7) show that Johnson \(1\)-Lipschitz loads force every one of
these cut inequalities, regardless of the number, sizes, or holonomy of the
components.

## 2. A cyclic-invariant high-energy Johnson \(1\)-Lipschitz load

We now work at depth one.  Identify the coordinates with \(\mathbb Z/n\mathbb
Z\), put

\[
r=m-1=\frac{n-3}{2},\qquad N=\binom nr,
\tag{2.1}
\]

and let \(g:i\mapsto i+1\) be the cyclic shift.

For an \(r\)-set \(S\), write \(b_i=\mathbf1_{\{i\in S\}}\).  Let

\[
P=001011,\qquad P^{\rm rev}=110100,
\tag{2.2}
\]

and define the integer chiral statistic

\[
h(S)=\sum_{i\in\mathbb Z/n\mathbb Z}
\left(
\mathbf1_{\{(b_i,\ldots,b_{i+5})=P\}}
-\mathbf1_{\{(b_i,\ldots,b_{i+5})=P^{\rm rev}\}}
\right).
\tag{2.3}
\]

It has three elementary properties.

First, it is shift-invariant:

\[
h(gS)=h(S).
\tag{2.4}
\]

Second, reflection \(\iota:i\mapsto-i\) reverses every six-window, so

\[
h(\iota S)=-h(S).
\tag{2.5}
\]

Third, a Johnson edge changes one \(1\) to \(0\) and one \(0\) to \(1\).
Each changed coordinate lies in six windows.  In one affected window the
summand in (2.3) changes by at most one: the two words in (2.2) have Hamming
distance six, so a two-bit exchange cannot turn one directly into the
other.  Consequently

\[
\boxed{|h(S)-h(T)|\le12\quad(ST\in E(J(n,r))).}
\tag{2.6}
\]

### Lemma 2.1 (two macroscopic chiral tails)

For every fixed integer \(M\ge0\), as \(n\to\infty\) through odd values
and \(r=(n-3)/2\),

\[
\frac1N\#\{S:h(S)>M\}\ge\frac18-o(1),
\qquad
\frac1N\#\{S:h(S)<-M\}\ge\frac18-o(1).
\tag{2.7}
\]

#### Proof

Choose \(k=\lfloor n/16\rfloor\) disjoint consecutive blocks of length
sixteen.  Call a block active if it is one of

\[
A=00000\,001011\,00000,
\qquad
D=00000\,110100\,00000.
\tag{2.8}
\]

Both words have weight three.  For a uniformly chosen rank-\(r\) binary
word, if \(X\) is the number of active blocks, then

\[
\mathbb E X
=2k\frac{\binom{n-16}{r-3}}{\binom nr}
=\left(2^{-19}+o(1)\right)n,
\tag{2.9}
\]

because a specified weight-three word on sixteen fixed positions has
asymptotic probability \(2^{-16}\).  For two specified blocks,

\[
\mathbb P(\text{both active})
=4\frac{\binom{n-32}{r-6}}{\binom nr}
=2^{-30}+o(1).
\tag{2.10}
\]

The square of the one-block limiting probability is also \(2^{-30}\).
It follows from (2.9)--(2.10) that

\[
\frac{\mathbb E X^2}{(\mathbb E X)^2}\longrightarrow1.
\tag{2.11}
\]

Paley--Zygmund with parameter \(1/2\) therefore gives

\[
\mathbb P\left(X\ge\tfrac12\mathbb EX\right)
\ge\frac14-o(1).
\tag{2.12}
\]

Partition the rank-\(r\) words into classes by allowing every active block
to be flipped independently between \(A\) and \(D\).  This preserves the
rank and the active-block set.  The five zeroes on both ends of a block
ensure that every six-window affected by the flip stays inside that block.
A direct inspection shows that \(A\) contains exactly one occurrence of
\(P\) and no occurrence of \(P^{\rm rev}\), while \(D\) contributes exactly
the reverse.  Hence on a class with \(a\) active blocks,

\[
h=h_0+\varepsilon_1+\cdots+\varepsilon_a,
\qquad \varepsilon_j\in\{-1,1\},
\tag{2.13}
\]

and all \(2^a\) sign choices occur equally often.

For any real translate \(h_0\), the number of sign choices for which
\(|h|\le M\) is at most

\[
(2M+1)\binom a{\lfloor a/2\rfloor}
=O_M(2^a a^{-1/2}).
\tag{2.14}
\]

On the classes counted by (2.12), one has \(a=\Omega(n)\).  Thus the
proportion of their elements with \(|h|\le M\) is \(o(1)\).  Combining
this with (2.12) gives

\[
\mathbb P(|h|>M)\ge\frac14-o(1).
\tag{2.15}
\]

Reflection (2.5) is a rank-preserving bijection between the two tails, so
each has at least half the mass in (2.15).  This proves (2.7). \(\square\)

Define

\[
x(S)=
\begin{cases}
-1,&h(S)\le-13,\\
0,&-12\le h(S)\le12,\\
1,&h(S)\ge13.
\end{cases}
\tag{2.16}
\]

By (2.4), \(x\) is constant on every \(g\)-orbit.  By (2.5), its positive
and negative supports have exactly the same size, so

\[
\sum_Sx(S)=0.
\tag{2.17}
\]

Moreover, (2.6) implies

\[
|x(S)-x(T)|\le1
\qquad(ST\in E(J(n,r))).
\tag{2.18}
\]

Indeed, an edge cannot join the regions \(h\le-13\) and \(h\ge13\).

At depth one,

\[
\frac WN=\frac{m+2}{m},\qquad c_1=1,
\qquad R:=W-N=\frac{2N}{m}.
\tag{2.19}
\]

Assume now that \(n\) is prime.  Every nonempty proper subset of
\(\mathbb Z/n\mathbb Z\) has a \(g\)-orbit of length \(n\).  Thus \(N\),
\(W\), and \(R\) are divisible by \(n\).

Apply Lemma 2.1 with \(M=24\).  There are at least
\((1/8-o(1))N\) targets with \(h\ge25\), whereas \(R/N=2/m\).  We may
therefore choose a union \(\mathcal U\) of exactly \(R/n\) full \(g\)-orbits
inside \(\{h\ge25\}\).  Define

\[
\boxed{\mu_1(S)=1+x(S)+\mathbf1_{\mathcal U}(S).}
\tag{2.20}
\]

This vector has exact mass \(W\) by (2.17) and \(|\mathcal U|=R\).  It is
shift-invariant, so all point degrees are equal; their sum is \(rW\), and
hence every point degree is exactly \(rW/n\).

Its values are \(0,1,2,3\).  It remains Johnson \(1\)-Lipschitz.  The only
new case is a target in \(\mathcal U\), whose load is three.  Such a target
has \(h\ge25\), so every Johnson neighbor has \(h\ge13\) by (2.6), and
therefore has load two or three.

Finally, if

\[
\mathcal H_-:=\{S:h(S)\le-13\},
\tag{2.21}
\]

then (2.20) has load zero on \(\mathcal H_-\), load three on \(\mathcal U\),
and balanced load one or two elsewhere.  Since \(c_1=1\),

\[
\boxed{Q_1(\mu_1)=2|\mathcal H_-|+2R.}
\tag{2.22}
\]

Lemma 2.1 with \(M=12\) and \(N/W=m/(m+2)\) give the exact asymptotic lower
bound

\[
\boxed{\liminf_{m\to\infty}\frac{Q_1(\mu_1)}W\ge\frac14.}
\tag{2.23}
\]

## 3. Exact balanced orbit loads at every other depth

For \(2\le q\le H\), write

\[
W=c_qN_q+\rho_q,\qquad0\le\rho_q<N_q.
\tag{3.1}
\]

Since \(n\) is prime and \(1\le r_q<n\), every \(g\)-orbit in
\(\binom{[n]}{r_q}\) has length \(n\).  Therefore both \(W\) and \(N_q\)
are divisible by \(n\), and so is \(\rho_q\).  Choose any union
\(\mathcal U_q\) of \(\rho_q/n\) full orbits and put

\[
\boxed{\mu_q(S)=c_q+\mathbf1_{\mathcal U_q}(S).}
\tag{3.2}
\]

Then \(\mu_q\) has exact mass \(W\), exact point margin \(r_qW/n\), and

\[
|\mu_q(S)-\mu_q(T)|\le1
\quad(ST\in E(J(n,r_q))).
\tag{3.3}
\]

More strongly, it is exactly at the integer floor:

\[
\boxed{Q_q(\mu_q)=0\qquad(2\le q\le H).}
\tag{3.4}
\]

Thus (2.23) is the entire initial corrected energy; there is no hidden
positive contribution or floor error at the other depths.

## 4. Attaching the orbit profiles to a genuine exact middle factor

Let \(F^0\) be any genuine exact middle wreath factor, for example the
canonical MSW factor.  It has exactly \(B=W/n\) wreath rows.

Every full \(g\)-orbit \(\mathcal O\subseteq\binom{[n]}{r_q}\) contains
\(n\) distinct targets.  Since \(g\) is transitive on coordinates and

\[
\sum_{S\in\mathcal O}|S|=nr_q,
\]

each coordinate belongs to exactly \(r_q\) members of \(\mathcal O\).
Thus \(\mathcal O\) is a legitimate point-regular row profile.

At depth one, take \(\mu_1(\mathcal O)\) copies of each orbit
\(\mathcal O\).  At depth \(q\ge2\), take \(c_q\) copies of every orbit and
one additional copy of every orbit in \(\mathcal U_q\).  In either case the
number of orbit copies is

\[
\frac1n\sum_S\mu_q(S)=\frac Wn=B.
\tag{4.1}
\]

For every \(q\), pair these \(B\) orbit copies bijectively with the \(B\)
genuine wreath rows of \(F^0\).  Denote the profile attached to row \(C\) by
\(\mathcal T_q(C)\).  Under a coordinate permutation \(\pi\), decorate the
row \(\pi C\) by \(\pi\mathcal T_q(C)\).  Write \(\widetilde F\) for this
decorated system.  Its middle projection is \(F^0\), but its lower profiles
are the attached orbit designs and are not being identified with the genuine
lower intervals of \(F^0\).

Rows here are colored by their decoration: even if a permutation stabilizes
the underlying unoriented wreath, it carries \((C,\mathcal T_\bullet(C))\)
to the well-defined colored row
\((C,\pi\mathcal T_\bullet(C))\).  Forgetting the color gives the genuine
middle wreath row.  Thus the coordinate action and every two-factor overlay
are unambiguous, while no false equivariance of the attached profiles is
being assumed.

The middle ownership of the decorated system is still exactly the genuine
middle ownership of \(F^0\).  Also, every decorated row has exactly \(n\)
distinct targets and point degree \(r_q\) at rank \(r_q\).

### Lemma 4.1 (every transposition component is invariant)

Fix a transposition \(\tau=(a\ b)\).  In the ownership overlay of \(F^0\)
and \(\tau F^0\), every connected component is carried to itself by \(\tau\),
with its two shores interchanged.

#### Proof

Take one wreath row \(C\).  Among its \(n\) cyclic middle intervals, label
an interval by zero, one, or two according to how many of \(a,b\) it
contains.  If every interval contained exactly one of the two labels, the
sum of these counts over the \(n=2m+1\) intervals would be \(n\).  On the
other hand, each label belongs to exactly \(m\) cyclic middle intervals, so
the same sum is \(2m=n-1\), a contradiction.  Hence \(C\) owns a middle
interval \(X\) containing both labels or neither.  Then \(\tau X=X\), and
both the old row \(C\) and the new row \(\tau C\) own \(X\).  They are
therefore adjacent in the overlay.

Thus every old row and its \(\tau\)-image lie in the same connected
component.  The involution \(\tau\) consequently maps each component to
itself and swaps its old and new shores. \(\square\)

If \(K\) has old-side row set \(L_K\), Lemma 4.1 says that its new-side row
set is exactly \(\tau L_K\).  Hence, at every depth,

\[
a^{\rm new}_{K,q}=\tau a^{\rm old}_{K,q}.
\tag{4.2}
\]

This proves the componentwise pair-sum preservation (1.3) for the decorated
profiles, not merely for their aggregate.

Choosing either complete shore of every component is a genuine exact middle
factor, since the two shores partition the same middle-root union.  The two
shores contain the same number of rows: every row owns \(n\) roots, and both
shores partition the same union.  Since each decorated row has point degree
\(r_q\), every child has exactly \(B\) rows, rank mass \(nB=W\), and point
margin \(r_qB=r_qW/n\).

## 5. Simultaneous local minimality and the Gram conclusion

Fix an arbitrary transposition \(\tau\).  If it moves a rank-\(r_q\) target
\(S\), then \(S\) and \(\tau S\) are adjacent in the Johnson graph.  By
(2.20), (3.2), and their \(1\)-Lipschitz properties,

\[
|\mu_q(S)-\mu_q(\tau S)|\le1
\qquad(q\le H).
\tag{5.1}
\]

Every common component signing preserves the pair total by (4.2).  Equations
(1.4)--(1.6) now show, separately for every moved target pair and every
depth, that the signed child cannot have lower floor energy.  Fixed targets
are unchanged.  Therefore

\[
Q_q(\widetilde F_\varepsilon)\ge Q_q(\widetilde F)
\qquad\text{for every }q\le H
\tag{5.2}
\]

for every signing of the intrinsic \(\tau\)-components.

The transposition was arbitrary.  Hence (5.2) holds simultaneously for
every transposition, with its freshly recomputed genuine ownership
components.  Summing with the positive weights \(1/c_q\), and using (1.9),
proves both all-transposition local minimality and every signed Gram cut
inequality (0.3).

Finally, (3.4) and (2.23) give

\[
\liminf\frac{\mathcal Q_H}{W}
=\liminf\frac{Q_1}{W}\ge\frac14.
\tag{5.3}
\]

Since \(B=W/n\) and \(H=(L+o(1))\sqrt m\),

\[
\frac{W}{HB}=\frac nH
=\left(\frac2L+o(1)\right)\sqrt m.
\tag{5.4}
\]

Combining (5.3)--(5.4) proves (0.4)--(0.5), and Theorem 0.1 follows.

There are infinitely many admissible \(m\), because every odd prime
\(n\) gives the integer \(m=(n-1)/2\), and there are infinitely many odd
primes.

## 6. What this closes and the next exact statement

The obstruction has the all-transposition quantifier

\[
\forall\tau\ \forall I
\quad
\mathcal Q_H(F^I)\ge\mathcal Q_H(F),
\tag{6.1}
\]

not the prescribed-transposition quantifier closed by AB7.  It also uses
the freshly recomputed intrinsic components for each \(\tau\), rather than
one fixed overlay.  Thus no theorem deduced solely from the following list
can prove the genuine local-minimum gate:

* positive-semidefinite component Gram structure and all signed cut
  inequalities;
* exact integral middle ownership and exact component-switch children;
* nonnegative integral labelled occurrence arrays;
* exactly \(n\) distinct rank targets and exact point degree per row;
* componentwise transposition pair-sum preservation and parity;
* the exact floor values \(c_q\), including a zero floor excess at every
  \(q\ge2\);
* simultaneous locality for every coordinate transposition.

The construction does not disprove the genuine local-minimum lemma, because
it deliberately severs the implication

\[
\text{middle wreath row }C
\quad\Longrightarrow\quad
\bigl(\mathcal I_{m-q}(C)\bigr)_{q\le H}
\tag{6.2}
\]

and replaces the right side by independently attached point-regular orbit
profiles.

Accordingly, the next exact positive statement cannot be another abstract
Gram, discrepancy, parity, or occurrence-marginal inequality.  It must be a
**cyclic-chronology exclusion theorem**.  One concrete necessary special
case is:

> A genuine exact wreath factor cannot have every lower load
> \(\mu_q\), \(q\le H\), Johnson \(1\)-Lipschitz while
> \(Q_1=\Omega(W)\).

Proving this special case would exclude the ideal-gain-zero obstruction
above, but would not by itself settle general bundling holonomy.  The full
surviving statement remains that common cyclic-prefix chronology must force
either \(\mathcal Q_H=O_L(H\operatorname{Cat}_m)\) or a positive component
cut for some transposition.  The present theorem proves rigorously that the
word "common" in that statement carries indispensable content.
