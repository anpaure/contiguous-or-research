# Audit of the PBBS first-shadow theorem and the centered Johnson factor

Date: 2026-07-26

Scope: independent line-by-line audit of Theorem 3.1 and the centered-edge
claims in `MATH_ATTACK_O2_FIRST_SHADOW_FACTOR_20260724.md`.

## 0. Verdict

The PBBS multiplicity theorem is valid:

\[
 \boxed{1\le \mu_P(S)\le3
 \quad\text{for every }S\in\binom{[2m+1]}{m-1},\ m\ge2.}
 \tag{0.1}
\]

No cyclic-parenthesis boundary case invalidates either inequality.

Centering every PBBS odd-graph vertex also does give a genuine spanning
Johnson 2-factor.  Its union colors are exactly all \((m+1)\)-sets, once
each, and its intersection-color histogram is exactly \(\mu_P\).

There is, however, an important ownership distinction.  If the PBBS
permutation has orbit lengths

\[
                         L_j=\ell_j(2m+1),                    \tag{0.2}
\]

then its centered Johnson graph has exactly

\[
 \boxed{
 c_J=\sum_j\gcd(2,L_j)
    =\sum_j\gcd(2,\ell_j)
    \le\sum_j\ell_j
    ={W\over2m+1}=B}
 \tag{0.3}
\]

components.  This improves the `at most \(2B\)` estimate in Proposition
6.1 of the source file.  Each centered component has length

\[
                         {L_j\over\gcd(2,L_j)}.                \tag{0.4}
\]

Consequently \(c_J=o(W/H)\) whenever \(H=o(m)\).

But (0.4) is **not** an exact-wreath conclusion.  When \(\ell_j=2\), for
example, the centered graph splits the PBBS \(2n\)-orbit into two
Johnson \(n\)-cycles, and the edges of each cycle are owned by the vertices
of the other cycle.  The original reciprocal odd-graph factor is still one
cycle of length \(2n\), not two wreaths.  Centered component length and
self-owned wreath packaging must not be conflated.

## 1. Parenthesis conventions and the clean-label lemma

Write \(1\) as an up-step and \(0\) as a down-step.  In a cyclic word with
\(d>0\) more zeros than ones, iterative noncrossing forward matching leaves
exactly \(d\) zeros.  Cutting immediately before those zeros gives a unique
cyclic decomposition

\[
 0_{z_0}D_0\,0_{z_1}D_1\cdots0_{z_{d-1}}D_{d-1},             \tag{1.1}
\]

where every \(D_i\) is a Dyck word, possibly empty.

The specialized clean-label fact needed in Theorem 3.1 is the following.

### Lemma 1.1 (deficit-three clean labels)

Let \(S\) have three more zeros than ones, and let \(U_+(S)\) be its three
forward-unmatched zeros.  If any zero \(u\) is changed to one, then the
unique forward-unmatched zero of the resulting word belongs to \(U_+(S)\).
The analogous statement holds for reverse matching and \(U_-(S)\).

#### Proof

Use (1.1) with \(d=3\).

* If \(u=z_i\), the new open at \(z_i\) consumes the next old unmatched
  zero \(z_{i+1}\), leaving \(z_{i+2}\).
* If \(u\) is a down-step in \(D_i\), the modified block has final height
  two.  Its two excess opens consume \(z_{i+1}\) and \(z_{i+2}\), leaving
  \(z_i\).

Thus the surviving forward mark is old in both cases.  Reverse physical
orientation gives the reverse assertion. \(\square\)

This proves the inclusions used in the source file,

\[
 \alpha_S(T)\subseteq U_+(S),
 \qquad
 \beta_S(T)\subseteq U_-(S).                                 \tag{1.2}
\]

Empty Dyck blocks and flipping one of the displayed unmatched zeros are
explicitly covered by the first case.  There is no hidden genericity
assumption in (1.2).

## 2. Audit of the lower bound

Fix

\[
                         S\in\binom{[n]}{m-1},
 \qquad n=2m+1,quad m\ge2.                                  \tag{2.1}
\]

Its word has \(m-1\) ones and \(m+2\) zeros, hence exactly three forward
unmatched zeros.  Write

\[
                         0_{z_0}D_0\,0_{z_1}D_1\,0_{z_2}D_2. \tag{2.2}
\]

Because the total Dyck-block semilength is \(m-1>0\), at least one block
is nonempty and has positive height.  Choose \(D_i\) of maximal height and
let \(u\) be the down-step immediately following the **rightmost** maximum
of \(D_i\).

### Lemma 2.1

\[
 r_+(S\cup\{u\})=z_i,
 \qquad
 r_-(S\cup\{z_i\})=u.                                       \tag{2.3}
\]

#### Proof

The first equality is Lemma 1.1: among the three old forward marks, the
unique mark strictly preceding the internal step \(u\) is \(z_i\).

For the second, change \(z_i\) to one and rotate the word to

\[
                         1D_i\,0D_{i+1}\,0D_{i+2}.            \tag{2.4}
\]

Its total height is \(-1\).  If \(H_j\) is the maximum height of \(D_j\),
the maxima in the three displayed regions are bounded by

\[
                         1+H_i,\qquad H_{i+1},\qquad H_{i+2}-1.
 \tag{2.5}
\]

The first is strictly largest even when the \(H_j\)'s tie.  Its rightmost
occurrence is, by construction, immediately before \(u\).  The standard
cycle lemma for a word of total height \(-1\) identifies the
reverse-unmatched zero as the down-step following the rightmost global
maximum.  Hence it is \(u\). \(\square\)

Put \(T=[n]\setminus S\) and

\[
                         X=T\setminus\{u,z_i\}.                \tag{2.6}
\]

The two elements are distinct and outside \(S\).  From the definitions of
the PBBS map and its inverse,

\[
 f(S\cup\{u\})=X,
 \qquad
 f^{-1}(S\cup\{z_i\})=X.                                    \tag{2.7}
\]

Thus

\[
 S\cup\{u\}\longrightarrow X\longrightarrow S\cup\{z_i\}
 \tag{2.8}
\]

is a directed PBBS two-path centered at \(X\), and its endpoint
intersection is exactly \(S\).  This proves \(\mu_P(S)\ge1\).

For \(m=2\), the three blocks in (2.2) have total semilength one, so one
of them is exactly `10` and the same proof applies literally.  This is the
only small-rank edge case in the argument.

## 3. Audit of the upper bound

For \(u\in T=[n]\setminus S\), define

\[
 \alpha(u)=r_+(S\cup\{u\}),
 \qquad
 \beta(u)=r_-(S\cup\{u\}).                                  \tag{3.1}
\]

Lemma 1.1 gives

\[
                         \alpha(T)\subseteq U_+(S),
 \qquad
                         \beta(T)\subseteq U_-(S),            \tag{3.2}
\]

and both sets on the right have size three.

### Lemma 3.1 (fixed-point dictionary)

Angle occurrences with color \(S\) are in bijection with fixed points of

\[
                         \beta\circ\alpha:T\longrightarrow T.\tag{3.3}
\]

#### Proof

Suppose an occurrence has directed form

\[
 S\cup\{u\}\longrightarrow X\longrightarrow S\cup\{v\}.
 \tag{3.4}
\]

The two endpoint sets are distinct: otherwise the PBBS permutation would
have a two-cycle, whereas every PBBS orbit length is divisible by the odd
number \(n\ge5\).  The definitions give

\[
 X=T\setminus\{u,\alpha(u)\}
  =T\setminus\{v,\beta(v)\}.                                 \tag{3.5}
\]

Equality of the two deleted unordered pairs, together with \(u\ne v\),
forces

\[
                         v=\alpha(u),
 \qquad
                         u=\beta(v).                           \tag{3.6}
\]

Thus \(u\) is fixed by \(\beta\alpha\).

Conversely, a fixed point \(u\), with \(v=\alpha(u)\), satisfies
\(u\ne v\) and (3.5), so it gives (3.4).  Two different fixed points
cannot encode the same directed occurrence, because its PBBS predecessor
is unique. \(\square\)

Every fixed point \(u\) lies in \(\beta(T)\subseteq U_-(S)\), since
\(u=\beta(\alpha(u))\).  Hence there are at most three, proving

\[
                         \mu_P(S)\le3.                         \tag{3.7}
\]

This also confirms that no factor of two is lost by orienting the PBBS
cycle: the predecessor, not the unordered endpoint pair, parametrizes the
occurrence.

## 4. The centered Johnson 2-factor

Let \(P\) be the PBBS odd-graph 2-factor and, for every center \(X\), put

\[
                         e_X=\{f^{-1}(X),f(X)\}.               \tag{4.1}
\]

Both endpoints are \(m\)-subsets of the \((m+1)\)-set \(X^c\).  They are
distinct because there are no PBBS two-cycles.  Therefore

\[
 f^{-1}(X)\cup f(X)=X^c,
 \qquad
 f^{-1}(X)\cap f(X)=\chi_P(X),                                \tag{4.2}
\]

and \(e_X\) is a Johnson edge.

### Theorem 4.1 (exact centered ledgers)

The graph

\[
                         J_P=\{e_X:X\in\tbinom{[n]}m\}        \tag{4.3}
\]

is a simple spanning 2-factor of \(J(n,m)\).  Its edge-union map is a
bijection onto \(\binom{[n]}{m+1}\), and its edge-intersection load vector
is exactly \(\mu_P\).

#### Proof

A vertex \(Y\) is an endpoint of \(e_X\) precisely when

\[
                         X=f(Y)\quad\text{or}\quad X=f^{-1}(Y).
 \tag{4.4}
\]

These are two distinct centers, and their edges are distinct, so every
vertex has degree two.  Equation (4.2) shows that the union color of
\(e_X\) is \(X^c\).  Complementation is a bijection from rank \(m\) to
rank \(m+1\), proving the upper ledger.  The second identity in (4.2) is
the definition of the angle at \(X\), proving the lower ledger. \(\square\)

No additional reciprocity assumption is being smuggled in here: (4.1) was
built from the already-existing permutation \(f\), so joining each center
to the endpoints of its edge reconstructs the original PBBS odd-graph
factor.

## 5. Exact centered component formula

Take one PBBS orbit

\[
                         C=(X_0,X_1,\ldots,X_{L-1}),
 \qquad f(X_i)=X_{i+1}.                                      \tag{5.1}
\]

On these vertices,

\[
                         e_{X_i}=X_{i-1}X_{i+1}.               \tag{5.2}
\]

Thus the centered graph is the step-two circulant on \(\mathbb Z/L\),
which has exactly \(\gcd(2,L)\) components, each of length
\(L/\gcd(2,L)\).

The imported PBBS orbit theorem gives \(L_j=\ell_jn\), where \(n=2m+1\)
is odd.  Hence

\[
 c_J=\sum_j\gcd(2,\ell_j),                                   \tag{5.3}
\]

and

\[
 \sum_j\ell_j={1\over n}\sum_jL_j={W\over n}=B.             \tag{5.4}
\]

Since \(\gcd(2,\ell)\le\ell\) for every positive integer \(\ell\),

\[
                         \boxed{c_J\le B={W\over n}.}         \tag{5.5}
\]

This is sharp at the level of the available length information: it is
attained when all \(\ell_j\in\{1,2\}\).  In particular, for every
\(H=o(m)\),

\[
                         c_J\le {W\over2m+1}=o(W/H).           \tag{5.6}
\]

### Ownership warning

If \(L=2n\), then (5.2) gives two centered Johnson \(n\)-cycles, one on
the even and one on the odd indices.  But edges on the odd-index cycle are
owned by even-index centers, and conversely.  The reciprocal odd graph
obtained from the centered edges is still the original single \(2n\)-cycle.
Therefore neither (5.5) nor the occurrence of length-\(n\) centered
components turns PBBS into an exact wreath factor.

For an odd PBBS orbit length \(L\), the centered graph has one component
on the same vertex set; for an even orbit it has two components exchanged
by \(f\).  This is the complete owner/component relation.

## 6. Correct conclusions

The following statements from the source file are validated:

1. every first-shadow target occurs;
2. every first-shadow load is at most three;
3. the number of load-three targets is at most \(W/(m+2)\), by mass
   conservation;
4. centered PBBS edges have perfect upper colors and the PBBS lower
   histogram;
5. the PBBS object itself remains a spanning odd-graph 2-factor whose
   orbit lengths are multiples of \(n\).

The following refinement should replace Proposition 6.1's coarse bound:

\[
 \boxed{
 \#\operatorname{comp}(J_P)
 =\sum_j\gcd(2,\ell_j)
 \le B,
 }
 \tag{6.1}
\]

not merely \(\le2B\).

What remains unproved is unchanged:

* PBBS odd components need not have length \(n\);
* centered Johnson components need not be self-owned physical wreath rows;
* the centered cycles have no established \(H\)-safe chronology for
  growing \(H\);
* rebundling into exact wreaths while retaining the first-shadow quality
  is a separate integral theorem.
