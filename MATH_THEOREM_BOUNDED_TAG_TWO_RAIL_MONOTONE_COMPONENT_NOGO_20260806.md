# Bounded-tag two-rail charts cannot occur at positive density

**Date:** 2026-08-06  
**Method:** overlap-forced signature monotonicity, component spacing, and a
hypergeometric second-moment bound  
**Status:** unconditional obstruction to physically gluing the
multiseparator SCD chart bank when all separators lie in \(O(d)\)
coordinates.  Its target matching and piece census are exact, but any
literal word of length \(O(W)\) contains only \(o(W)\) such chart
occurrences.  A positive-density realization of this packet form needs a
separator/tag bank of order \(d^2=\Theta(n)\), or a different history
interface.

## 1. Abstract tagged chart bank

Let \(D\subseteq[n]\) be a fixed tag/separator bank of size

\[
                         |D|=T.                            \tag{1.1}
\]

Consider a bank of two-rail charts indexed injectively by rank-\(q\)
cores \(K\).  For one chart choose a separator

\[
                         b\in D\setminus K                  \tag{1.2}
\]

and put

\[
                         E=K\cap D.                         \tag{1.3}
\]

Assume its two marked rails have tag signatures

\[
 T_{0,j}\cap D=E,
 \qquad
 T_{1,j}\cap D=E\cup\{b\}
 \qquad(1\le j\le d).                                    \tag{1.4}
\]

The multiseparator hypercube--SCD construction has exactly this form: all
SCD additions lie in the bulk outside \(D\), and each core supports one
chart.

Let

\[
                         A=(A_1,\ldots,A_L)                 \tag{1.5}
\]

be a cyclic literal word.  A chart occurs at terminal position \(e\) when
its first rail is the suffix chain at endpoint \(e-1\) and its second rail
is the suffix chain at endpoint \(e\).

## 2. Overlap forces strict signature growth

### Lemma 2.1 (overlap monotonicity)

Let chart occurrences with lower signatures \(E,E'\) and separators
\(b,b'\) terminate at \(e<e'\), with cyclic forward distance

\[
                         1\le e'-e\le d.                   \tag{2.1}
\]

Then

\[
                         \boxed{E\cup\{b\}\subseteq E'.}  \tag{2.2}
\]

In particular,

\[
                         |E'|\ge|E|+1.                      \tag{2.3}
\]

#### Proof

The depth-one value at the first terminal position is the second rail's
bottom target, so

\[
                         A_e\cap D=E\cup\{b\}.              \tag{2.4}
\]

The next chart's first depth-\(d\) target is

\[
                         A_{e'-d}\cup\cdots\cup A_{e'-1},  \tag{2.5}
\]

whose intersection with \(D\) is \(E'\) by (1.4).  Condition (2.1) says
that \(A_e\) is one of the letters in (2.5).  Therefore its tag signature
is a subset of \(E'\), proving (2.2).  Since \(b\notin E\), (2.3)
follows. \(\square\)

## 3. Overlap components

Order all chart terminal positions cyclically.  Break the list whenever
the forward gap is greater than \(d\); call the resulting runs
**overlap components** and let their number be \(R\).

### Lemma 3.1

If at least one chart occurs, then

\[
                         R\le\left\lfloor{L\over d+1}\right\rfloor.
                                                                    \tag{3.1}
\]

Within one component, lower tag-signature sizes are strictly increasing.
Consequently one component contains at most one chart whose lower
signature has any prescribed size \(e\).

#### Proof

Lemma 2.1 gives strict increase along every unbroken gap.  Hence the whole
cyclic list cannot be one unbroken component: strict inclusion cannot
return to its starting signature.  Every break gap has length at least
\(d+1\), and the break gaps are disjoint arcs of the \(L\)-cycle.  This
proves (3.1).  Strict rank increase gives the final assertion. \(\square\)

## 4. Rank-slice capacity

Because cores index the chart bank injectively, the number of available
charts with lower signature size \(e\) is at most

\[
                         C_e={T\choose e}{n-T\choose q-e}.  \tag{4.1}
\]

If \(H_e\) such charts occur in the word, Lemma 3.1 and (4.1) give

\[
                         H_e\le\min\{R,C_e\}.               \tag{4.2}
\]

Put

\[
                         N_q={n\choose q}.                  \tag{4.3}
\]

Then \(C_e/N_q\) is the probability mass function of a hypergeometric
random variable

\[
                         X=|K\cap D|                        \tag{4.4}
\]

for a uniform rank-\(q\) core.  Its mean and variance satisfy

\[
 \mu={qT\over n},
 \qquad
 \operatorname {Var}X
  =T{q\over n}\left(1-{q\over n}\right){n-T\over n-1}
  \le {T\over4}.                                          \tag{4.5}
\]

### Theorem 4.1 (bounded-tag occurrence bound)

For every real \(a\ge1\), the total number \(H=\sum_eH_e\) of chart
occurrences satisfies

\[
 \boxed{
 H\le(2a+3)R+{N_qT\over4a^2}.}                            \tag{4.6}
\]

Consequently

\[
 \boxed{
 H=O\!\left((N_qT)^{1/3}R^{2/3}+R\right).}                \tag{4.7}
\]

#### Proof

There are at most \(2a+3\) integer ranks in
\([\mu-a,\mu+a]\), and each contributes at most \(R\) by (4.2).  Outside
that interval, discard the \(R\) bound and sum the available capacities:

\[
 \sum_{|e-\mu|>a}H_e
 \le\sum_{|e-\mu|>a}C_e
 =N_q\Pr(|X-\mu|>a)
 \le {N_qT\over4a^2},                                     \tag{4.8}
\]

where the last inequality is Chebyshev's inequality and (4.5).  This
proves (4.6).  Taking

\[
                         a=\max\left\{1,(N_qT/R)^{1/3}\right\}          \tag{4.9}
\]

gives (4.7). \(\square\)

## 5. PBBS asymptotic no-go

In the top PBBS slab,

\[
                         N_q=\Theta(W),
 \qquad L=O(W),
 \qquad d\to\infty.                                      \tag{5.1}
\]

Lemma 3.1 gives \(R=O(W/d)\).  Substitute this in (4.7):

\[
 \boxed{
 H=O\!\left(W{T^{1/3}\over d^{2/3}}+{W\over d}\right).}  \tag{5.2}
\]

### Corollary 5.1 (\(O(d)\) tags give zero density)

If

\[
                         T=O(d),                            \tag{5.3}
\]

then

\[
                         \boxed{H=O(Wd^{-1/3})=o(W).}       \tag{5.4}
\]

In particular, the balanced multiseparator hypercube--SCD bank with
\(T=p+r=\Theta(d)\) cannot supply the required
\((\eta+o(1))W\) literal shared joins, even though it has exact target
disjointness, exact piece count, and per-separator load below the individual
spacing bound.

### Corollary 5.2 (positive density requires a macroscopic tag bank)

For every fixed \(\eta>0\), if

\[
                         H\ge\eta W,                       \tag{5.5}
\]

then (5.2) forces

\[
                         \boxed{T=\Omega_\eta(d^2).}        \tag{5.6}
\]

At the optimal deadline \(d^2=\Theta(n)\).  Thus a positive-density
realization of this injective-core, tag-monotone packet form needs a
positive-order fraction of the coordinate bank, not merely the
\(\Theta(d)\) separators required by one-coordinate spacing.

## 6. Interpretation

The earlier fixed-separator obstruction said that one coordinate cannot
host enough chart births.  Balancing the charts over \(\Theta(d)\)
separators repairs that scalar count.  Theorem 4.1 exposes the next,
strictly stronger obstruction:

* histories of events closer than \(d+1\) overlap;
* overlap forces their complete tag signatures to increase strictly;
* an \(O(d)\)-tag hypercube has only \(O(\sqrt d)\) statistically abundant
  signature ranks;
* the remaining tail ranks contain too few named cores.

The obstruction is not that the warm-up positions must be empty.  They may
carry arbitrary other PBBS pieces.  It is the unavoidable inclusion order
on the signatures of the selected chart occurrences themselves.

## 7. Exact scope

Proved here:

* a source-word obstruction, not merely a target-count warning;
* an exact all-\(T\) upper bound (4.6)--(4.7);
* zero asymptotic density for the \(T=\Theta(d)\) hypercube--SCD bank;
* necessity of \(T=\Omega(d^2)\) for positive density in this packet form.

The theorem assumes:

1. chart cores are used injectively;
2. every rail has the fixed tag signatures (1.4); and
3. the charts occur literally as adjacent full endpoints in one word.

It does **not** refute:

* packets whose history interface can forget or recycle tags without a
  gap of length \(d\);
* a construction with a macroscopic \(\Theta(n)\) tag bank;
* noninjective-core packets with a separately proved target matching;
* a different PBBS support-first/Euler construction; or
* \(\nu(k)\le B(k)+O(1)\).

Thus the two-rail SCD bank completely solves the marked-target matching but
does not, even after balanced separator spreading, solve physical history
gluing.  A successful next packet must contain a genuine tag-reset or
tag-recycling mechanism.
