# Audit of the translation-orbit exploration

Date: 2026-07-25

Source audited:
`/Users/amir.nuriyev/.codex/attachments/20348553-ec9f-41d1-b242-f79faf89efa4/pasted-text.txt`.

Pure mathematics only.  No computation or web input is used.

## 0. Verdict

The attachment does not prove coefficient one and does not solve the
critical top-packet theorem.  Most of its valid calculations reproduce
already calibrated wreath means, the independent Poisson barrier, and the
outer-depth threshold.

There is one useful exact lemma which can be salvaged and strengthened:
for prime $n=2m+1$, every translation-fixed wreath is an arithmetic-
progression wreath.  It gives a congruence obstruction to a fully
translation-invariant exact factor, ruling one out at $n=7$.

There is also a definite counting error: a fixed $r$-set lies in

\[
 r!(n-r)!
 \]

cyclic orders modulo rotation, not $r!(n-r-1)!$.  At
$r=m-q$, the missing factor is $m+q+1$.

## 1. Exact shadow means

Let

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 N_q=\binom n{m-q}.
\]

The attachment's mean calculation is correct:

\[
 \lambda_q={W\over N_q}
 =\prod_{i=0}^{q-1}{m+2+i\over m-i},
 \tag{1.1}
\]

and, uniformly for $q=o(m^{2/3})$,

\[
 \log\lambda_q={q(q+1)\over m}
 +O(q^3/m^2+q/m).
 \tag{1.2}
\]

In particular

\[
 \lambda_1={m+2\over m},\qquad
 W-N_1={2W\over m+2}.
 \tag{1.3}
\]

The statement that shallow ranks must be nearly rainbow is therefore
correct.  The sum

\[
 \sum_{q\le H}(W-N_q)
 =(1+o(1)){WH^3\over3m}
 \tag{1.4}
\]

is also correct for $H=o(m^{2/3})$.  It is an arithmetic forced-duplicate
baseline, not by itself a construction or an available error budget.

## 2. Translation-fixed wreaths

The attachment proves only the constant-step AP implication as written;
its assertion that varying steps are "overly restrictive" is not a proof.
For prime ground size, however, the desired classification follows by a
different exact argument.

### Theorem 2.1 (prime translation-fixed wreath classification)

Let $n=2m+1$ be prime, identify the ground set with $\mathbb Z_n$, and let
$\mathcal W(\pi)$ be the family of the $n$ cyclic length-$m$ intervals of
a cyclic order $\pi$.  If

\[
 \mathcal W(\pi)+1=\mathcal W(\pi),
 \tag{2.1}
\]

then $\pi$ is an arithmetic-progression cyclic order.  Consequently the
translation-fixed un-oriented wreaths are exactly

\[
 \pi_d=(0,d,2d,\ldots,(n-1)d),
 \qquad d\in\mathbb Z_n^*/\{\pm1\},
 \tag{2.2}
\]

and there are $(n-1)/2=m$ of them.

#### Proof

Write the interval sets as $I_j$, with starts indexed cyclically.  Two
distinct length-$m$ intervals have intersection size $m-1$ exactly when
their starts differ by $1$ or $-1$: a shift by $t\le m$ gives intersection
size $m-t$, and the other shifts are symmetric.  Thus the graph on the
$I_j$ joining pairs with intersection $m-1$ is the cycle $C_n$.

No nonempty proper subset of $\mathbb Z_n$ is fixed by translation by one.
Therefore translation acts freely, hence transitively, on the $n$ members
of the invariant wreath.  It acts as an order-$n$ automorphism of the
cycle $C_n$, so it is a rotation

\[
 I_j+1=I_{j+c}
 \tag{2.3}
\]

with $c\ne0$.  Let $x_j$ be the coordinate which leaves when passing from
$I_j$ to $I_{j+1}$.  Translation of that oriented edge gives

\[
 x_{j+c}=x_j+1.
 \tag{2.4}
\]

Since $c$ is invertible modulo the prime $n$, (2.4) gives

\[
 x_j=x_0+jc^{-1}.
\]

The leaving sequence is the underlying cyclic coordinate order, proving
the AP form.  Reversal identifies $d$ with $-d$, and no other two
differences give the same wreath. \(\square\)

### Corollary 2.2 (invariant-factor congruence)

If an exact wreath factor is invariant under translation, then

\[
 \operatorname{Cat}_m=k+n\ell
 \tag{2.5}
\]

for some $0\le k\le m$, where $k$ is the number of fixed AP wreaths in the
factor.  In particular no translation-invariant exact factor exists for
$m=3,n=7$, because

\[
 \operatorname{Cat}_3=5
 \]

is neither $0,1,2,$ nor $3$ modulo $7$.

#### Proof

For prime $n$, every orbit of wreaths has size one or $n$.  The fixed
orbits are the $m$ AP wreaths from Theorem 2.1, and an exact factor cannot
repeat one. \(\square\)

The attachment's $n=7$ gap-pattern discussion is consistent with this
corollary: the five translation orbits of triples consist of the three AP
types and two non-AP reverse types.  The gap-pattern enumeration is an
illustration, not needed for the proof.

This obstruction is only to **fully translation-invariant exact** factors.
An approximate construction may alter $O(n)=o(W/n)$ orders to repair orbit
congruences, so it is not an obstruction to coefficient one.

## 3. Correct cyclic-order incidence degree

The attachment states that a fixed rank-$(m-q)$ set belongs to
$(m-q)!(m+q)!$ cyclic orders.  This is false by one factor.

### Proposition 3.1

Among the $(n-1)!$ oriented cyclic orders modulo rotation, a fixed
$r$-set is a cyclic interval in exactly

\[
 \boxed{r!(n-r)!}
 \tag{3.1}
\]

orders.  Hence at $r=m-q$ the degree is

\[
 \boxed{(m-q)!(m+q+1)!}. 
 \tag{3.2}
\]

#### Proof

Contract the prescribed interval to one cyclic object.  Together with the
$n-r$ outside singletons this gives $n-r+1$ cyclic objects, with
$(n-r)!$ cyclic arrangements.  Order the interval internally in $r!$
ways. \(\square\)

The incidence check is

\[
 \binom nr r!(n-r)!=n!=(n-1)!\,n,
\]

as required because every cyclic order supplies $n$ intervals.

## 4. Orbit reduction and random-cover barrier

Taking complete translation orbits of seed orders does shrink the number
of labels by a factor $n$, but the attachment correctly observes that it
does not improve the load ratio (1.1).  A generic seed orbit covers at most
$n$ translation orbits of rank-$r$ targets, and the normalized mean remains
$\lambda_q$.

The independent-order calculation is also valid.  If $Nn=CW$ with fixed
$C>0$, then a fixed rank-$(m-q)$ target is missed with probability

\[
 \left(1-{n\over N_q}\right)^N
 =\exp(-C\lambda_q+o(1)).
 \tag{4.1}
\]

For $q=u\sqrt m$ its expected missed contribution is

\[
 W e^{-u^2}e^{-Ce^{u^2}}(1+o(1)).
\]

Summation over $\Theta(\sqrt m)$ shallow depths gives
$\Theta_C(W\sqrt m)$.  This is a valid no-go for iid-like selection, not a
no-go for correlated packet/segment constructions.

The outer random threshold is likewise correctly located by

\[
 \lambda_q\asymp\log m,
 \]

namely

\[
 q\asymp\sqrt{m\log\log m}.
 \tag{4.2}
\]

The attachment's claim about a particular unconditional strip depth
mixes incompatible scales -- it mentions both a cube-root expression and
"roughly $(\log m)^{1/2-o(1)}$" without a proof.  It should not be used as
a theorem.

## 5. Product-box discussion

The final product-box paragraphs are exploratory.  They supply no new
construction, no proved estimate for growing dimension, and no implication
for coefficient one.  The fixed-dimensional obstructions quoted there may
be valid results from the handoff, but they are not reproved in the
attachment.  The proposed escape by letting the number of blocks grow is
only a question; no bound on the corresponding local word $g_d$ is given.

## 6. Relation to the current promotion-packet frontier

The exact prime translation theorem rules out one overly symmetric source
of factors.  It does not affect the critical top-fibre construction, whose
tops and cyclic orders are deliberately allowed to vary non-equivariantly.

Nothing in the attachment supplies the missing positive vertical
selection for the promotion packets.  In particular:

* orbit averaging is another exact fractional solution;
* independent seed orbits retain the Poisson hole barrier;
* AP wreaths furnish only $O(n)$ orders;
* no integral absorber, rank-isolating trade, or low-switch descaling is
  constructed.

The theorem-level net contribution of the attachment is therefore
Theorem 2.1 and its congruence corollary, together with the correction
(3.2).  The coefficient-one gate remains the positive simultaneous
vertical rounding of the calibrated packet/segment-rectangle system.
