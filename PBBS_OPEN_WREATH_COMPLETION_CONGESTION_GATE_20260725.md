# PBBS simple returns: exact random-completion congestion formula

Date: 2026-07-25

Method: pure mathematics only. No computation or external input is used.

## 0. Purpose and outcome

The minimal-return theorem reduces the Catalan packing problem, within a
factor two, to simple PBBS returns.  A simple return of gap \(2s+1\) has
cores \(K,K'\) of size

\[
 q=r-s
\]

and an active set

\[
 Z=\{a_0,\ldots,a_s,b_0,\ldots,b_{s-1}\}.
\]

It has \((q!)^2\) explicit ambient wreath completions.  This note computes
the vertex law of a uniformly random such completion exactly.

The result turns the proposed bounded-overlap completion idea into one
explicit inequality.  For every middle vertex \(X\), one must bound a
weighted sum over those packed sectors whose active labels alternate
perfectly across the cut \((X,X^c)\).  The weights are reciprocal products
of binomial coefficients.  A uniform \(O(1)\) bound proves the physical
Catalan packing theorem immediately.

The inequality is not established here.  In particular, edge-disjointness
alone gives no immediate pointwise bound on the alternating-sector sum.
Thus ambient completion is a clean reformulation, not yet a proof of
\((\mathrm{CP}_A)\).

## 1. The completion tail

Use the omitted-label order

\[
 \begin{aligned}
 z={}&(a_0,b_0,a_1,b_1,\ldots,a_{s-1},b_{s-1},a_s,\\
     &k_1,k'_1,k_2,k'_2,\ldots,k_q,k'_q),
 \end{aligned}                                      \tag{1.1}
\]

where \((k_1,\ldots,k_q)\) and \((k'_1,\ldots,k'_q)\) are independent
orders of \(K\) and \(K'\).  The ambient wreath vertices are

\[
 W_t=\{z_{t+1},z_{t+3},\ldots,z_{t+2r-1}\}.
 \tag{1.2}
\]

Put

\[
 A=\{a_0,\ldots,a_s\},\qquad
 U=\{b_0,\ldots,b_{s-1}\}.                         \tag{1.3}
\]

The vertices \(W_0,\ldots,W_{2s+1}\) are the prescribed open PBBS
segment.  The remaining \(2q-1\) vertices split into

\[
 E_i=W_{2s+2i}\quad(1\le i\le q)
\]

and

\[
 O_i=W_{2s+1+2i}\quad(1\le i\le q-1).
\]

### Proposition 1.1 (exact completion-tail states)

One has

\[
 \boxed{
 E_i=
 (K\setminus\{k_1,\ldots,k_i\})
 \cup A\cup\{k'_1,\ldots,k'_{i-1}\}}
 \qquad(1\le i\le q),                              \tag{1.4}
\]

and

\[
 \boxed{
 O_i=
 (K'\setminus\{k'_1,\ldots,k'_i\})
 \cup U\cup\{k_1,\ldots,k_i\}}
 \qquad(1\le i\le q-1).                           \tag{1.5}
\]

### Proof

The wreath recurrence is

\[
 W_{t+2}=W_t-\{z_{t+1}\}+\{z_t\}.                 \tag{1.6}
\]

At the first even tail step it removes \(k_1\) and inserts \(a_s\).
Every subsequent even tail step removes \(k_i\) and inserts
\(k'_{i-1}\).  This proves (1.4) by induction.  On the odd parity, the
first tail step removes \(k'_1\) and inserts \(k_1\), and subsequent
steps continue the same exchange, proving (1.5). \(\square\)

## 2. Exact inclusion probabilities

Choose the two core orders independently and uniformly.  For a fixed
middle vertex \(X\in\binom{[N]}r\), define

\[
 \pi_I(X)=\Pr\{X\text{ is a vertex of the random completion of }I\}.
\]

The prescribed vertices are present with probability one.  Away from the
prescribed segment, Proposition 1.1 gives the following exact law.

### Theorem 2.1 (random completion law)

For the even tail, \(X=E_i\) is possible exactly when

\[
 X\cap Z=A,qquad |X\cap K|=q-i,qquad
 |X\cap K'|=i-1.                                   \tag{2.1}
\]

Under these conditions,

\[
 \boxed{
 \Pr(X=E_i)=
 {1\over\binom qi\binom q{i-1}}.}                 \tag{2.2}
\]

For the odd tail, \(X=O_i\) is possible exactly when

\[
 X\cap Z=U,qquad |X\cap K|=i,qquad
 |X\cap K'|=q-i,                                   \tag{2.3}
\]

and then

\[
 \boxed{
 \Pr(X=O_i)= {1\over\binom qi^2}.}                \tag{2.4}
\]

For a fixed sector and fixed \(X\), at most one even-tail index and at
most one odd-tail index can contribute.

### Proof

In (1.4), the retained part of \(K\) is a uniform \((q-i)\)-subset and
the inserted part of \(K'\) is an independent uniform \((i-1)\)-subset.
This proves (2.1)--(2.2).  The same argument applied to (1.5) proves
(2.3)--(2.4).  The intersection sizes determine \(i\), proving the last
statement. \(\square\)

The active condition has a useful direct interpretation:

\[
 X\cap Z=A
 \quad\Longleftrightarrow\quad
 a_0,\ldots,a_s\in X,quad b_0,\ldots,b_{s-1}\notin X,
 \tag{2.5}
\]

while \(X\cap Z=U\) is the reverse alternation.  Thus a completion can hit
\(X\) outside the prescribed segment only if the half-open omitted-label
word alternates perfectly between \(X\) and its complement.

## 3. The exact fractional-congestion gate

Let \(\mathcal P\) be a physical edge-disjoint family of simple returns.
For a middle vertex \(X\), put

\[
 \begin{aligned}
 \Lambda_X(\mathcal P)
 ={}&\#\{I\in\mathcal P:X\text{ lies in the prescribed open segment of }I\}\\
 &+\sum_{I\in\mathcal P}\sum_{i=1}^{q_I}
 {\mathbf1_{\{X\text{ satisfies }(2.1)\}}
  \over\binom{q_I}i\binom{q_I}{i-1}}\\
 &+\sum_{I\in\mathcal P}\sum_{i=1}^{q_I-1}
 {\mathbf1_{\{X\text{ satisfies }(2.3)\}}
  \over\binom{q_I}i^2}.
 \end{aligned}                                    \tag{3.1}
\]

This is exactly the expected number of chosen random completions which
contain \(X\).

### Theorem 3.1 (bounded fractional completion congestion implies CP)

If

\[
 \boxed{
 \sup_{X\in\binom{[N]}r}\Lambda_X(\mathcal P)\le C} \tag{3.2}
\]

for an absolute constant \(C\), then

\[
 \boxed{
 |\mathcal P|N\le C\binom Nr.}                    \tag{3.3}
\]

In particular,

\[
 |\mathcal P|=O(B_r).
\]

After the exact factor-two minimal-return reduction, (3.2), uniformly for
all Gaussian-window simple-return packings, proves the physical form of
\((\mathrm{CP}_A)\).

### Proof

Every ambient completion contains exactly \(N\) middle vertices.  Hence,
for independently chosen uniform completions,

\[
 |\mathcal P|N
 =\sum_X\mathbb E[\text{number of completions containing }X]
 =\sum_X\Lambda_X(\mathcal P).
\]

Apply (3.2) and use
\(\binom Nr=NB_r\). \(\square\)

Notice that no integral simultaneous choice of completions is required for
this counting argument.  A bounded *fractional* congestion estimate is
already enough.

## 4. What remains

The prescribed open PBBS segments themselves have bounded vertex overlap
when the corresponding ordinary edge supports are disjoint; the only new
term is the alternating-sector sum in (3.1).  The exact remaining
completion theorem is therefore:

> For every physical edge-disjoint family of Gaussian-length simple PBBS
> returns and every middle vertex \(X\), the reciprocal-binomial weighted
> number of sectors whose simple omitted-label word alternates across
> \((X,X^c)\) is \(O_A(1)\).

The endpoint cases of (2.2) have weight \(1/q\), while the interior
weights decay as reciprocal products of two binomial coefficients.  This
is favorable, but edge-disjointness by itself does not presently bound the
number of perfectly alternating sectors at each endpoint index.  A proof
must use the fact that all the sectors lie in the single canonical PBBS
factor, or an equivalent first-return restriction on the alternating
label words.

Thus the ambient-wreath route has been reduced to the explicit scalar gate
(3.2); it has not yet been closed.

## 5. Equivalent monotone-staircase form for a fixed target

The alternation condition has an exact interpretation inside the original
PBBS owner factor.  Fix (X\in\binom{[N]}r), and for an owner (Y) put

\[
 h_X(Y)=|X\cap Y|.
\]

If an omitted label at the edge (Y_tY_{t+1}) is (z_t), the Kneser
recurrence gives

\[
 \boxed{
 h_X(Y_{t+1})=r-h_X(Y_t)-\mathbf1_{\{z_t\in X\}}.}
 \tag{5.1}
\]

Consequently

\[
 h_X(Y_{t+2})-h_X(Y_t)
 =\mathbf1_{\{z_t\in X\}}-
  \mathbf1_{\{z_{t+1}\in X\}}.                    \tag{5.2}
\]

### Proposition 5.1 (paired monotone staircases)

For a simple sector satisfying the even-tail condition (2.1), the two
owner parities obey

\[
 \boxed{
 h_X(A_{2j})=q-i+j,
 \qquad
 h_X(A_{2j+1})=s+i-j-1
 \quad(0\le j\le s),}                              \tag{5.3}
\]

with the evident endpoint interpretation in the second formula.  Thus the
even parity rises by one at every step-two edge while the odd parity falls
by one.

For a sector satisfying the odd-tail condition (2.3),

\[
 \boxed{
 h_X(A_{2j})=s+i-j,
 \qquad
 h_X(A_{2j+1})=q-i+j
 \quad(0\le j\le s),}                              \tag{5.4}
\]

so the directions are reversed.

### Proof

Under (2.1), (X) contains all (a)-labels and no (b)-labels,
while

\[
 |X\cap K|=q-i,qquad |X\cap K'|=i-1.
\]

Substitution in the exact owner formulas

\[
 A_{2j}=K\cup\{a_0,\ldots,a_{j-1}\}
             \cup\{b_j,\ldots,b_{s-1}\}
\]

and

\[
 A_{2j+1}=K'\cup\{b_0,\ldots,b_{j-1}\}
               \cup\{a_{j+1},\ldots,a_s\}
\]

gives (5.3).  The same substitution with (X\cap Z=U),

\[
 |X\cap K|=i,qquad |X\cap K'|=q-i,
\]

gives (5.4). \(\square\)

Hence (3.2) is equivalently a weighted packing theorem for **paired
oppositely directed monotone staircases** of length (s) in the scalar
intersection process (h_X) along the two parity factors.  The weights
are exactly

\[
 {1\over\binom qi\binom q{i-1}}
 \quad\hbox{or}\quad
 {1\over\binom qi^2}.                              \tag{5.5}
\]

This uses all of the fixed-core normal form.  A generic level-counting
argument is still too weak: at the endpoint (i=1), the first weight in
(5.5) is (1/q), whereas there are

\[
 \binom r1\binom{r+1}1=r(r+1)
\]

middle vertices at Johnson distance one from (X).  Thus the desired
constant cannot follow merely by charging the endpoint of each staircase
to its Johnson level.  One must use a restriction on which paired
staircases the canonical PBBS factor can contain, or a genuinely
two-parity nonreuse theorem.

There is nevertheless a clean bounded-index consequence.  Let
\(\mathcal P^E_i(X)\) be the sectors contributing to the even-tail term at
index (i).  Their terminal odd owners (A_{2s+1}) are distinct and have
intersection (i-1) with (X).  Hence

\[
 |\mathcal P^E_i(X)|
 \le \binom r{i-1}\binom{r+1}i.                    \tag{5.6}
\]

Similarly, sectors contributing to the odd-tail term at index (i) have
distinct terminal owners at Johnson distance (i) from (X), and

\[
 |\mathcal P^O_i(X)|
 \le \binom ri\binom{r+1}i.                        \tag{5.7}
\]

Consequently their weighted contributions are at most

\[
 \boxed{
 R^E_i(r,q)=
 {\binom r{i-1}\binom{r+1}i
  \over\binom q{i-1}\binom qi},
 \qquad
 R^O_i(r,q)=
 {\binom ri\binom{r+1}i
  \over\binom qi^2}.}                              \tag{5.8}
\]

For every fixed (i) and (s=o(r)), both ratios in (5.8) are (O_i(1))
(indeed they tend to one).  Thus every fixed number of completion layers
at either core boundary already has bounded congestion.  The unresolved
loss is genuinely a growing-index accumulation; it is not caused by the
first or last completion step.
