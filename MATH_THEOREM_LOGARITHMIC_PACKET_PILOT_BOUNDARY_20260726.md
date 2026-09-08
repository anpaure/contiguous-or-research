# The logarithmic pair-packet pilot: exact mixed codegrees and the correlated matching gate

Date: 2026-07-26

Method: pure mathematics only.  No finite search, solver, computation, or
web input is used.

## 0. Verdict

Fix constants \(0<\alpha<1\) and \(c>0\), and take

\[
 r=\alpha\log_2m+O(1),\qquad
 H=c\log m+O(1)\le r/4,\qquad
 R=2^r=m^{\alpha+o(1)}.                                \tag{0.1}
\]

The logarithmic packet pilot clears the complete time-zero mixed-codegree
test.  For the owner-and-all-signed-target packet lift,

\[
 K=(1+2H)R=m^{\alpha+o(1)}O(\log m),                    \tag{0.2}
\]

and the maximum normalized pair codegree is

\[
 {\Delta_2\over D}\le(1+o(1)){r\over m}.                \tag{0.3}
\]

The dominant pair is not owner--target: it is a same-sign adjacent-depth
nested target pair.  Nevertheless,

\[
 \boxed{
 K{\Delta_2\over D}
 =O(m^{\alpha-1}(\log m)^2)=o(1).}                      \tag{0.4}
\]

Thus there is no projective-plane or pair-codegree obstruction to a fresh
packet bite.

This does **not** prove a \(c\log m\)-band matching.  Three further facts
are unconditional.

1. One isolated random bite covers
   \((e^{-1}+o(1))/K\) of every resource part.
2. The audited quantitative growing-uniformity matching theorem is
   inapplicable: even after using every physical local cube state,
   \(\log D=o(K)\), while that theorem requires
   \(K\le\frac12\log D\); its exponential codegree hypothesis and its
   displayed leave bound also fail.
3. Product-like residuals do not regenerate.  After independently deleting
   only \(\omega((\log m)^2/m^\alpha)\) of the owners, all but \(o(1)\) of
   the retained owners lie in no surviving physical \(Q_r\)-packet.

Hence the proposed \(c\log m\) theorem remains open, but its minimum form
is now exact: a one-shot colored matching or a deliberately
packet-correlated residual theorem.  Marginal regularity,
\(K\Delta_2/D=o(1)\), and the existence of many surviving packets
globally do not supply it.

## 1. Why the logarithmic quotas are almost unthinned

Put

\[
 W=\binom{2m}m,\qquad
 N_q=\binom{2m}{m-q},\qquad p_q={N_q\over W}.
\]

Uniformly for \(q\le H=O(\log m)\),

\[
 p_q
 =\prod_{i=0}^{q-1}{m-i\over m+i+1}
 =1-{q^2\over m}
  +O\left({q^3+q^4\over m^2}\right).                   \tag{1.1}
\]

Consequently,

\[
 R(1-p_q)=O(m^{\alpha-1}\log^2m)=o(1).                 \tag{1.2}
\]

The floor/ceiling hard quota in one packet is therefore \(R-1\) or \(R\)
at every signed depth.  Across the complete band, the mean number of
dumped occurrences in one balanced column is

\[
 2R\sum_{q\le H}(1-p_q)
 =O(RH^3/m)=o(1).                                      \tag{1.3}
\]

Since this is a nonnegative integer, a \(1-o(1)\) fraction of the indexed
columns have no dump at any depth.  Such a column must have \(R\) distinct
literal lower traces and \(R\) distinct literal upper traces
simultaneously at every \(q\le H\).  Thus quota marking cannot repair a
local trace collision in this pilot; an almost-everywhere exact local
multidepth-rainbow catalogue is a logically prior requirement.

For the global matching calculation it is therefore convenient to use
the strict unthinned packet edge: all \(R\) owners and all \(R\) distinct
targets in every signed part.  The part sizes are \(W,N_1,N_1,\ldots,
N_H,N_H\), and their degree ratios are

\[
 {D_q^\pm\over D_0}={W\over N_q}=1+O(H^2/m).            \tag{1.4}
\]

Thus this strict lift is already near-regular.  The total imbalance of
its target parts is

\[
 2\sum_{q\le H}(W-N_q)=O(WH^3/m)=o(W).                  \tag{1.5}
\]

## 2. Complete mixed-codegree census

All ratios below are in the fully coordinate-symmetrized catalogue, with
the degree of the first displayed resource type in the denominator.  They
become literal common-\(D\) ratios after exact hard-quota regularization.
In the strict unthinned lift the type degrees differ by only
\(1+O(H^2/m)\), so normalization by its maximum degree changes every
bound by \(1+o(1)\).  Trace selection and acceptance can only decrease
the target--target upper bounds.

### 2.1 Owner--owner

For middle owners at Johnson distance \(d\),

\[
 {d(X,Y)\over D}
 ={1\over\binom rd}
  \left({(r)_{\underline d}\over(m)_{\underline d}}\right)^2,
 \qquad
 \max_{X\ne Y}{d(X,Y)\over D}={r\over m^2}.             \tag{2.1}
\]

### 2.2 Owner--target, including nonincident pairs

Let \(T\) be a lower depth-\(q\) target and put \(j=|T\setminus X|\).
Then exactly

\[
 \boxed{
 {d(T,X)\over D}
 ={2^q\binom{r-q}{j}\over
   \binom{m-q}{j}\binom{m+q}{q+j}}.}                    \tag{2.2}
\]

Complementation gives the upper formula.  The maximum is the incident
depth-one value

\[
                         {2\over m+1}.                  \tag{2.3}
\]

### 2.3 Same-sign targets

Let \(T,S\) be lower targets at depths \(q,p\), and put

\[
 a=|T\setminus S|,\qquad b=|S\setminus T|=a+q-p.
\]

The ambient shell about \(T\) has size

\[
 M^-_{q,p}(a)=\binom{m-q}{a}\binom{m+q}{b}.             \tag{2.4}
\]

The exact number of physical lower \(p\)-faces in one pair frame with
this relation to a fixed lower \(q\)-face is

\[
 f^-_{q,p}(a)
 =\sum_t
   \binom{r-q}{t}\binom q{t+q-p}2^{t+q-p}
   \binom{r-q-t}{a-t}.                                  \tag{2.5}
\]

Hence

\[
 {d(T,S)\over D}
 \le {f^-_{q,p}(a)\over M^-_{q,p}(a)}
 \le\left({2r\over m-r}\right)^{a+b}.                  \tag{2.6}
\]

The only one-power shells are adjacent and nested:

\[
 {f^-_{q,q+1}(1)\over M^-_{q,q+1}(1)}
 ={r-q\over m-q},\qquad
 {f^-_{q,q-1}(0)\over M^-_{q,q-1}(0)}
 ={2q\over m+q}.                                       \tag{2.7}
\]

Upper--upper pairs follow by complementation.

### 2.4 Opposite signs

If \(T\) is lower at depth \(q\), \(U\) is upper at depth \(p\), and
\(a=|T\setminus U|\), then

\[
 f^{-+}_{q,p}(a)
 =\sum_u\binom qu\binom{r-q}{p-u}2^{q-u}
   \binom{r-q-p+u}{a},                                  \tag{2.8}
\]

while the ambient shell is

\[
 M^{-+}_{q,p}(a)
 =\binom{m-q}{a}\binom{m+q}{p+q+a}.
\]

Therefore

\[
 {d(T,U)\over D}
 \le {f^{-+}_{q,p}(a)\over M^{-+}_{q,p}(a)}
 \le\left({2r\over m-r}\right)^{p+q+2a}.               \tag{2.9}
\]

Every opposite-sign pair pays at least two powers of \(r/m\).

### 2.5 Dump resources

Under full independent label symmetrization,

\[
 {d(z,X)\over D}={R\over W},\qquad
 {d(z,T)\over D}\le(1+o(1)){R\over W}.                 \tag{2.10}
\]

Since (1.2) permits at most one dump in a signed part, two distinct dump
tokens from the same part have codegree zero.  Dump codegrees are
exponentially below (2.7).

Equations (2.1)--(2.10) prove (0.3)--(0.4).  In particular, checking only
the forced owner--target ratio \(2/(m+1)\) misses the genuine dominant
adjacent-depth target fibre, but the corrected scale remains favorable.

## 3. The exact strict-rainbow pilot theorem still needed

Let \(\mathcal G^\star_{m,r,H}\) be the simple hypergraph whose edges are
valid strict-rainbow packet states: one whole \(Q_r\) owner packet and all
of its \(R\) distinct signed traces through depth \(H\).

### Definition 3.1 (logarithmic colored packet matching)

\(\operatorname{LCPM}(\alpha,c)\) is the assertion that
\(\mathcal G^\star_{m,r,H}\) has a matching of \(t\) packet edges such
that

\[
                         N_H-Rt=o(W/H).                \tag{3.1}
\]

### Theorem 3.2 (LCPM gives the complete \(c\log m\) band)

If \(\operatorname{LCPM}(\alpha,c)\) holds, then the selected literal
packet factors have owner leave \(o(W/H)\) and aggregate signed-target
leave \(o(W)\) through depth \(H\).

#### Proof

Since \(N_q\) decreases with \(q\), write
\(\ell=N_H-Rt=o(W/H)\).  The owner leave is

\[
 W-Rt=(W-N_H)+\ell
 =O(WH^2/m)+o(W/H)=o(W/H),                             \tag{3.2}
\]

because \(H^3/m=o(1)\).  At signed depth \(q\), the leave is

\[
 N_q-Rt=(N_q-N_H)+\ell.
\]

Therefore the aggregate target leave is at most

\[
 2H(W-N_H)+2H\ell
 =O(WH^3/m)+o(W)=o(W).                                 \tag{3.3}
\]

All selected traces are literal and packet edges are owner-disjoint, so
there is no further recoding or integrality loss. \(\square\)

Thus (3.1), not a vague near-perfect matching statement, is the precise
pilot target.

## 4. What one fresh nibble proves

Let a simple \(K\)-uniform hypergraph have degrees
\((1\pm\eta)D\).  For an edge \(E\), put

\[
 \sigma(E)={1\over KD}
 \sum_{\{u,v\}\subset E}d(u,v),\qquad
 \sigma=\max_E\sigma(E).                               \tag{4.1}
\]

If \(\Delta_2\le\delta D\), then
\(\sigma\le(K-1)\delta/2\).  Mark every edge independently with
probability \(1/(KD)\), and retain it when no intersecting marked edge
exists.  Bonferroni gives

\[
 |\Gamma(E)|=KD\bigl(1+O(\eta+\sigma+D^{-1})\bigr).
\]

Consequently

\[
 \Pr(E\text{ retained})
 ={e^{-1}+o(1)\over KD},                                \tag{4.2}
\]

and every resource is covered with probability

\[
                         {e^{-1}+o(1)\over K}.          \tag{4.3}
\]

By (0.4), this is a rigorous growing-\(K\) one-bite theorem for the
logarithmic packet lift.  It covers only \(\Theta(1/K)\), so iteration or
a one-shot global theorem is unavoidable.

There is also an exact conditional iteration in the equal-part
mandatory-plus-dump lift.  If every matching residual down to common part
density \(\varepsilon\) remains \((1+o(1))\)-regular and has
\(\sigma=o(1)\), then repeated applications of (4.3) give density
\(\varepsilon\) after

\[
                         O(K\log(1/\varepsilon))        \tag{4.4}
\]

bites.  Taking \(\varepsilon=1/(H\log H)\) gives common part leave
\(W/(H\log H)=o(W/H)\), and hence proves the hard-quota \(c\log m\)
band by the mandatory-plus-dump ledger.  This hereditary
packet-regeneration hypothesis is sufficient, but it is not a consequence
of (0.4).

## 5. Two quantitative failures of generic matching machinery

### 5.1 The audited growing-uniformity theorem

Through one owner there are

\[
 D_r=\binom mr^2r!
\]

physical frames.  A directed cube factor on one frame is specified, with
a generous overcount, by one of \(r\) outgoing directions at each of its
\(R\) owners.  Thus the maximum simple degree over every possible local
state satisfies

\[
 D\le(1+o(1))D_r r^R,\qquad
 \log D=O(r\log m+R\log r)=o(K).                       \tag{5.1}
\]

The audited Alon--Bollobas--Kim--Vu matching theorem used elsewhere in
this project requires

\[
 K\le\tfrac12\log D,\qquad
 e^{2K}{\Delta_2\log D\over D}=o(1).                   \tag{5.2}
\]

The first condition contradicts (5.1).  The exact owner--depth-one ratio
also gives \(\Delta_2/D\ge(2+o(1))/m\), so the second expression in
(5.2) diverges.  Finally its displayed leave factor,

\[
 K\left({\Delta_2\log(1+\Delta_2)\over D}\right)^{1/(K-1)},
\]

is at least \((1-o(1))K\), since \(\Delta_2\ge1\) and
\(\log D=o(K)\).  That theorem is quantitatively vacuous here.

### 5.2 Product residuals

Retain owners independently with density \(\rho\), conditioning on a
retained owner \(X\).  A physical frame through \(X\) survives only when
its other \(R-1\) owners survive, so exactly

\[
 \mathbb E[d_{\rm frame}(X)\mid X\text{ retained}]
 =D_r\rho^{R-1}.                                       \tag{5.3}
\]

Since

\[
 \log D_r=\Theta((\log m)^2),                           \tag{5.4}
\]

the exact link-death criterion is

\[
 (R-1)\log(1/\rho)-\log D_r\longrightarrow+\infty.
\]

In particular, the expectation in (5.3) is \(o(1)\) whenever

\[
 (1-\rho)R\gg(\log m)^2.                                \tag{5.5}
\]

Thus a product-like trajectory destroys the typical owner link after
deleting only

\[
 \omega((\log m)^2/m^\alpha)=o(1)                      \tag{5.6}
\]

of the layer.  In particular it cannot approach density
\(1/(H\log H)\).

There may nevertheless be exponentially many surviving packets globally:

\[
 \mathbb E|\mathscr P_r[U]|={WD_r\over R}\rho^R.
\]

For fixed \(\rho\), its logarithm is
\(\Theta(m)-\Theta(m^\alpha)>0\).  But their average degree at a retained
owner is (5.3), so they are concentrated on an \(o(1)\)-fraction of
owners.  Global packet count is not hereditary expansion.

## 6. Exact remaining hypothesis

The logarithmic pilot has passed:

* literal local trace injectivity, assuming the audited packet compiler;
* exact fractional regularity;
* every owner--owner, owner--target, target--target, and dump codegree;
* the natural one-bite condition \(K\Delta_2/D=o(1)\); and
* the exact loss implication (3.2)--(3.3).

It has not passed either of the following alternative constructive gates:

1. the one-shot matching assertion \(\operatorname{LCPM}(\alpha,c)\);
2. a packet-correlated residual/absorber theorem which preserves complete
   owner cubes and the mixed target ledgers down to leave \(o(W/H)\).

A convenient explicit one-shot theorem would be any fixed-power leave
bound.  Put

\[
 \Gamma_m=K\Delta_2/D
 =O(m^{\alpha-1}(\log m)^2).
\]

If a matching theorem specific to this packet lift gave common part leave

\[
                         \ell\le C\Gamma_m^\gamma W    \tag{6.1}
\]

for fixed \(C,\gamma>0\), then

\[
 {H\ell\over W}
 \le C H\,m^{-\gamma(1-\alpha)}
       (\log m)^{2\gamma}=o(1).                        \tag{6.2}
\]

Thus (6.1) would prove the pilot immediately.  Neither the one-bite lemma
nor the audited ABKV theorem yields such a bound; (6.1) is an explicit
form of the missing one-shot result, not a conclusion of the present
work.

Ordinary product regeneration is rigorously impossible, and the available
audited growing-uniformity theorem is quantitatively unavailable.  Thus
the \(c\log m\) band is a valid pilot toward CPM, but it is not yet a
proved simultaneous-band colored packet matching.
