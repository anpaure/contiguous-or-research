# Calibrated top packets: augmented near-factor audit

Date: 2026-07-25

Pure mathematics only.  No computation, web input, solver, or unproved
generic rounding theorem is used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \lambda_q=\frac W{N_q}.                                                   \tag{0.1}
\]

Choose \(H\) to be the **least** positive integer such that

\[
 \lambda_H\ge M,\qquad M:=m+H.                                             \tag{0.2}
\]

This is the calibrated sign needed for one full length-\(M\) promotion
packet at every rank-\((m+H)\) top.  The exact estimates are

\[
 H=(1+o(1))\sqrt{m\log m},                                                  \tag{0.3}
\]

\[
 1\le\frac{\lambda_H}{M}
 <\frac{M-1}{m-H+1}=1+O(H/m),                                              \tag{0.4}
\]

and therefore, with

\[
 S:=MN_H,
\]

\[
 \boxed{S=W-O(WH/m)=W-o(W),}                                               \tag{0.5}
\]

\[
 \boxed{HN_H=o(W).}                                                        \tag{0.6}
\]

For every top \(U\in\binom{[2m]}M\), an oriented cyclic order of \(U\)
gives one exact promotion cycle with \(M\) distinct middle owners.  At
every lower or upper depth \(q<H\), it gives \(M\) distinct cyclic-interval
targets; at upper depth \(H\), all states give the common top \(U\).

The scalar ledger is stronger than merely rankwise \(o(W)\).  If \(S\)
collision-free occurrences were available at every signed rank, the total
unavoidable holes over the whole band would be

\[
 (W-S)+2\sum_{q=1}^{H-1}(N_q-S)_+=o(W).                                    \tag{0.7}
\]

Thus no hidden sum over \(H\) ranks destroys the proposal.

The middle-owner packet hypergraph has excellent exact local statistics.
Its owner degree is

\[
 D_0=\frac{m!^2}{(m-H)!},                                                   \tag{0.8}
\]

and two owners at Johnson distance \(t<H\) have relative codegree

\[
 \boxed{\frac{D_2(t)}{D_0}=
 \frac{2(t!)^2}{(m)_t^2}.}                                                 \tag{0.9}
\]

The maximum is \(2/m^2\), attained at \(t=1\).  Moreover the normalized
pair-codegree sum inside any one packet is only \(O(1/m)\).  This is much
sparser than a projective-plane overlap pattern.

These facts do not by themselves prove an integral near-factor.  The packet
rank \(M\) grows with \(m\), independent one-packet-per-top selection has
Poisson-scale owner collisions, and the all-ranks augmentation has strong
but structured vertical codegrees between nested interval targets.  The
exact sufficient statement left by the audit is the augmented top-packet
near-factor \((\mathrm{ATPNF})\) in Section 7:

* choose one packet at each top;
* make their middle-owner sets disjoint; and
* keep the aggregate excess above balanced target quotas through all
  signed depths \(q<H\) equal to \(o(W)\).

The proved scalar estimate (0.7) then turns quota excess \(o(W)\) into
aggregate flag holes \(o(W)\), while (0.6) pays every packet reset.  Hence
\((\mathrm{ATPNF})\) implies coefficient one.

No sharp obstruction to \((\mathrm{ATPNF})\) is found.  What is ruled out
is an uncorrelated topwise choice and a black-box argument using only the
maximum codegree of the raw all-ranks hypergraph.  The remaining integral
problem must use the top tags and the nested interval-column quotient.

## 1. The calibrated threshold

The exact adjacent ratio is

\[
 \frac{\lambda_q}{\lambda_{q-1}}
 =\frac{m+q}{m-q+1}.                                                       \tag{1.1}
\]

### Proposition 1.1 (threshold and overshoot)

The least \(H\) satisfying (0.2) obeys (0.3)--(0.4).

#### Proof

For \(q=o(m^{2/3})\), uniformly,

\[
 \log\lambda_q
 =\sum_{i=0}^{q-1}\log\frac{m+i+1}{m-i}
 =\frac{q^2}{m}
  +O\!\left(\frac qm+\frac{q^3}{m^2}\right).                              \tag{1.2}
\]

Substitution of
\(q_\pm=(1\pm\varepsilon)\sqrt{m\log m}\) shows, for every fixed
\(\varepsilon>0\), that

\[
 \lambda_{q_-}<m+q_-,\qquad \lambda_{q_+}>m+q_+                            \tag{1.3}
\]

for all sufficiently large \(m\).  Minimality then gives (0.3).

Also \(\lambda_{H-1}<m+H-1=M-1\).  By (1.1),

\[
 \lambda_H
 =\lambda_{H-1}\frac{m+H}{m-H+1}
 <(M-1)\frac{M}{m-H+1}.                                                    \tag{1.4}
\]

Divide by \(M\) and combine with (0.2) to obtain (0.4). \(\square\)

Define

\[
 \rho=\frac{S}{W}=\frac{M}{\lambda_H},\qquad
 \delta=1-\rho.                                                           \tag{1.5}
\]

Proposition 1.1 gives

\[
 0\le\delta=O(H/m)=o(1).                                                   \tag{1.6}
\]

Equations (0.5)--(0.6) follow immediately:

\[
 W-S=\delta W=O(WH/m),                                                     \tag{1.7}
\]

\[
 HN_H=\frac{HW}{\lambda_H}\le\frac{HW}{M}=o(W).                           \tag{1.8}
\]

The outer tails are also negligible.  Since

\[
 \frac{N_{q+1}}{N_q}=\frac{m-q}{m+q+1},
\]

one has

\[
 \sum_{q=H+1}^mN_q
 \le N_H\frac{m-H}{2H+1}
 \le\frac{W}{M}\frac{m-H}{2H+1}
 =O(W/H).                                                                 \tag{1.9}
\]

The complemented tail has the same size.

## 2. One full promotion packet at a top

Fix \(U\in\binom{[2m]}M\) and an oriented cyclic order

\[
 \pi=(u_0,u_1,\ldots,u_{M-1}).
\]

Indices are cyclic modulo \(M\).  Define

\[
 X_i=\{u_i,u_{i+1},\ldots,u_{i+m-1}\}.                                    \tag{2.1}
\]

At \(X_i\), use the lower and upper words

\[
 \alpha_i=(u_i,u_{i+1},\ldots,u_{i+H-1}),                                  \tag{2.2}
\]

\[
 \beta_i=(u_{i-1},u_{i-2},\ldots,u_{i-H}).                                 \tag{2.3}
\]

The next owner is

\[
 X_{i+1}=X_i-u_i+u_{i-H},                                                  \tag{2.4}
\]

and \(u_{i-H}=\beta_H(X_i)\).  Hence (2.4) is exactly last-position
singleton promotion.  The \(M\) states form a bridge-one cycle; cut one arc
to obtain one useful-prefix path.

For \(0\le q\le H\), its flags are

\[
 L_q(X_i)=\{u_{i+q},\ldots,u_{i+m-1}\},                                   \tag{2.5}
\]

\[
 U_q(X_i)=\{u_{i-q},\ldots,u_{i+m-1}\}.                                   \tag{2.6}
\]

Thus the lower length is \(m-q\), the upper length is \(m+q\), and all
\(M\) starts are distinct at every proper interval length.  At \(q=H\),
the upper interval is all of \(U\).

Call the support arising from one cyclic order a **top packet**.  We retain
oriented cyclic orders modulo rotation, so each top has

\[
 (M-1)!                                                                  \tag{2.7}
\]

indexed packets.  Reversal may identify two un-oriented supports, but
retaining both orientations makes all incidence counts exact and harmless.

## 3. The aggregate scalar-hole lemma

Suppose, provisionally, that one packet is chosen at each of the \(N_H\)
tops and that the \(S=MN_H\) target occurrences at every proper interval
rank can be placed without avoidable collision.  The middle rank then has
\(W-S=\delta W\) holes.  At either signed depth \(q\ge1\), the unavoidable
count is \((N_q-S)_+\).

### Proposition 3.1 (all scalar holes sum to \(o(W)\))

At the calibrated depth,

\[
 (W-S)+2\sum_{q=1}^{H-1}(N_q-S)_+=o(W).                                   \tag{3.1}
\]

#### Proof

The product defining \(\lambda_q\) has positive factors, so

\[
 \lambda_q
 =\prod_{i=0}^{q-1}\left(1+\frac{2i+1}{m-i}\right)
 \ge1+\sum_{i=0}^{q-1}\frac{2i+1}{m}
 =1+\frac{q^2}{m}.                                                        \tag{3.2}
\]

If \(N_q>S=(1-\delta)W\), then

\[
 \frac1{1+q^2/m}\ge\frac1{\lambda_q}
 =\frac{N_q}{W}>1-\delta.
\]

Hence

\[
 q^2<\frac{m\delta}{1-\delta}.                                           \tag{3.3}
\]

There are only \(O(\sqrt{m\delta})=O(\sqrt H)\) such positive depths,
and every summand is at most \(W-S=\delta W\).  Therefore

\[
 \sum_{q=1}^{H-1}(N_q-S)_+
 =O\bigl(W\delta\sqrt{m\delta}\bigr)
 =O\left(W\frac{H^{3/2}}m\right)=o(W),                                   \tag{3.4}
\]

because \(H=(1+o(1))\sqrt{m\log m}\).  Add the middle deficit and the two
signs. \(\square\)

This proposition is essential.  A merely rankwise statement
\(N_q-S=o(W)\) would not justify summing over \(H\) ranks; (3.4) does.

## 4. The packet degrees

Let \(\mathcal E\) be the indexed family of all top packets over all tops.
Its size is

\[
 |\mathcal E|=N_H(M-1)!.                                                   \tag{4.1}
\]

### Proposition 4.1 (exact one-row degrees)

1. A fixed top tag \(U\) belongs to exactly
   \[
      D_{\rm top}=(M-1)!                                                   \tag{4.2}
   \]
   packets.
2. For every \(0\le q<H\), a fixed lower or upper rank-\((m\mp q)\)
   target belongs to exactly
   \[
      \boxed{D_q=\frac{(m-q)!(m+q)!}{(m-H)!}}                              \tag{4.3}
   \]
   packets.  At \(q=0\), this is the middle-owner degree
   \[
      D_0=\frac{m!^2}{(m-H)!}.                                             \tag{4.4}
   \]

#### Proof

For a lower target \(T\) of size \(m-q\), choose its top by adjoining
\(H+q\) elements from its complement.  There are

\[
 \binom{m+q}{H+q}
\]

choices.  In a fixed top, the number of oriented cyclic orders in which
\(T\) is an interval is

\[
 (m-q)!(H+q)!.
\]

Their product is (4.3).  For an upper target of size \(m+q\), there are
\(\binom{m-q}{H-q}\) containing tops and
\((m+q)!(H-q)!\) interval orders in each, giving the same expression.
The top and middle cases follow. \(\square\)

The degree ratio is

\[
 \frac{D_q}{D_0}=\frac{(m-q)!(m+q)!}{m!^2}=\lambda_q.                      \tag{4.5}
\]

This is exactly the required rank load.  Also

\[
 WD_0=|\mathcal E|M,                                                       \tag{4.6}
\]

and

\[
 SD_{\rm top}=|\mathcal E|M.                                              \tag{4.7}
\]

Hence

\[
 \frac{D_0}{D_{\rm top}}=\frac SW=\rho=1-o(1).                            \tag{4.8}
\]

This near-equality is the top-tag balance behind the calibrated choice.
If every top tag is regarded as a private cluster of mass \(M\), the top
mass and owner mass have asymptotically equal degrees.  The cluster must be
kept contracted: expanding it into \(M\) twins creates codegree one inside
the cluster and destroys a raw small-codegree hypothesis.

### Proposition 4.2 (exact one-per-top fractional point)

At every top, distribute total weight one uniformly over its \((M-1)!\)
indexed packets.  Then every top tag has load one, every owner has load

\[
 \rho=\frac SW=\frac{M}{\lambda_H}\le1,                                  \tag{4.9}
\]

and every lower or upper target at a proper depth \(q<H\) has load

\[
 \frac{S}{N_q}=\rho\lambda_q.                                             \tag{4.10}
\]

The total packet weight is exactly \(N_H\).

#### Proof

The top assertion is the normalization.  The construction is invariant
under all coordinate permutations and contains total owner mass
\(MN_H=S\), so every one of the \(W\) owners has load \(S/W=\rho\).
At a proper signed depth, each packet has \(M\) distinct targets and hence
the total target mass is again \(S\); transitivity on that rank gives
(4.10).  Summing one unit over all tops gives total weight \(N_H\).
\(\square\)

Thus the colored owner-matching LP is feasible with exactly the desired
leave, and every rank has the correct uniform mean.  What is not supplied
is integral polarization: when \(S/N_q\) is nonintegral, the uniform load
lies strictly between the two balanced integral quotas at every target.
The augmented rounding must choose which targets receive the high quota
while choosing the packets themselves.

## 5. Exact same-rank codegrees

We first give the middle-owner formula, which controls disjoint packet
packing.

Let distinct owners \(X,Y\) have Johnson distance

\[
 t=|X-Y|=|Y-X|.                                                           \tag{5.1}
\]

They lie in a common top only when \(t\le H\).

### Theorem 5.1 (owner pair degrees)

For \(1\le t<H\),

\[
 \boxed{
 \frac{\operatorname{codeg}(X,Y)}{D_0}
 =\frac{2(t!)^2}{(m)_t^2}.}                                               \tag{5.2}
\]

For \(t=H\),

\[
 \boxed{
 \frac{\operatorname{codeg}(X,Y)}{D_0}
 =\frac{m-H+1}{\binom mH^2}.}                                             \tag{5.3}
\]

For \(t>H\), the codegree is zero.  In particular,

\[
 \max_{X\ne Y}\frac{\operatorname{codeg}(X,Y)}{D_0}
 =\frac2{m^2}.                                                            \tag{5.4}
\]

#### Proof

Assume \(t<H\).  There are

\[
 \binom{m-t}{H-t}                                                         \tag{5.5}
\]

common tops.  In a fixed common top, put

\[
 B=U-X,\qquad C=U-Y.
\]

These are \(H\)-sets with \(|B\cap C|=H-t\).  Since \(2H<M\) for large
\(m\), two such short cyclic intervals must appear in one of the two block
orders

\[
 (B-C),(B\cap C),(C-B)
\]

or its reverse.  The remaining block has size \(m-t\).  Thus the number of
oriented cyclic orders is

\[
 2(t!)^2(H-t)!(m-t)!.                                                      \tag{5.6}
\]

Multiplying (5.5)--(5.6) and dividing by (4.4) gives (5.2).

If \(t=H\), the top is forced to be \(U=X\cup Y\), and \(B,C\) are
disjoint \(H\)-intervals.  Contracting them gives a cyclic order on
\(m-H+2\) objects.  Hence the number of orders is

\[
 (H!)^2(m-H+1)!,                                                          \tag{5.7}
\]

which divided by (4.4) is (5.3).  The remaining assertions follow.
\(\square\)

The maximum-codegree statistic conceals an additional gain.

### Proposition 5.2 (sparse owner-overlap profile)

For every packet \(P\),

\[
 \boxed{
 \sum_{\{X,Y\}\subseteq M(P)}
 \frac{\operatorname{codeg}(X,Y)}{D_0}=O(1/m).}                           \tag{5.8}
\]

#### Proof

For each cyclic separation \(1\le t<H\), there are at most \(M\) owner
pairs in \(P\) with Johnson distance \(t\).  All remaining pairs have
distance \(H\).  Theorem 5.1 gives

\[
 \begin{split}
 \sum_{\{X,Y\}\subseteq M(P)}
 \frac{\operatorname{codeg}(X,Y)}{D_0}
 &\le M\sum_{t=1}^{H-1}\frac{2(t!)^2}{(m)_t^2}
  +M^2\frac{m-H+1}{\binom mH^2}\\
 &=O(1/m).
 \end{split}                                                              \tag{5.9}
\]

The first term is dominated by \(2M/m^2\), and the second is
superpolynomially smaller. \(\square\)

There is an analogous exact formula at every one signed rank.  Let
\(A,B\) be distinct targets of the same rank \(m\mp q\), and put
\(t=|A-B|=|B-A|\).  Let

\[
 s=M-|A|=
 \begin{cases}
 H+q,&|A|=m-q,\\
 H-q,&|A|=m+q.
 \end{cases}                                                             \tag{5.10}
\]

For \(1\le t<s\), the same four-block count gives

\[
 \boxed{
 \frac{\operatorname{codeg}_q(A,B)}{D_q}
 =\frac{2(t!)^2}{(m-q)_t(m+q)_t}.}                                        \tag{5.11}
\]

When \(t=s\), the two short complements are disjoint and the exact
codegree is

\[
 (s!)^2(M-2s+1)!.                                                         \tag{5.12}
\]

For \(t>s\), it is zero.  Formula (5.11) is \(O(1/m^2)\), uniformly in the
band.  The boundary formula (5.12) is also much smaller except at the
upper depth \(H-1\), where \(s=1\) and the relative codegree is

\[
 \frac1{m-H+1}.                                                           \tag{5.13}
\]

This exception is a top quotient, not a diffuse collision: every packet at
\(U\) contains all \(M\) facets of \(U\), so the entire upper
depth-\((H-1)\) load is independent of the cyclic order and is already
exactly balanced when one packet is chosen at each top.

## 6. Why the raw all-ranks codegree is not small

Targets at different ranks are nested along the same cyclic interval
columns.  This creates larger but very structured codegrees.

For example, fix a top \(U\), an interval \(A\subset U\) of size \(k\),
and a set \(B\supset A\) of size \(k+d<M\).  Conditional on \(A\) being
an interval in a uniformly indexed cyclic order of \(U\), the exact
probability that \(B\) is also an interval is

\[
 \boxed{
 \frac{(d+1)d!(M-k-d)!}{(M-k)!}
 =\frac{d+1}{\binom{M-k}{d}}.}                                            \tag{6.1}
\]

Indeed, the \(d\) new elements may be split in \(d+1\) ways between the
two ends of \(A\); their total internal order contributes \(d!\), and the
complement of \(B\) is the remaining interval block.  When \(B=U\), the
conditional probability is one.

At adjacent ranks, (6.1) is \(2/(M-k)\).  Near the middle this is
\(\Theta(1/H)\), much larger than the \(O(1/m^2)\) same-rank codegree; at
the top boundary it becomes deterministic.  Therefore a black-box matching
claim applied to a hyperedge containing all \((2H-1)M\) proper-rank
resources has not been justified by Theorem 5.1.

The large cross-rank pairs form only the \(M\) nested interval columns of
one packet.  They should be contracted or handled as a bounded-width
vertical conflict system.  Similarly, the \(M\) private copies of a top tag
must be contracted to one tag of weight \(M\).  These two quotients are the
specific structure absent from a generic growing-uniformity hypergraph.

Independent choices do not exploit it.  If one packet is chosen uniformly
and independently at every top, a fixed owner lies in \(\binom mH\) tops,
and its inclusion probability within any one containing top is

\[
 \frac{M}{\binom MH}.
\]

Its mean load is

\[
 \binom mH\frac{M}{\binom MH}
 =\frac{M}{\lambda_H}=\rho=1-o(1),                                        \tag{6.2}
\]

while the individual probability tends to zero.  Hence its uncovered
probability is

\[
 \left(1-\frac{M}{\binom MH}\right)^{\binom mH}
 =e^{-1}+o(1).                                                            \tag{6.3}
\]

So uncorrelated topwise selection leaves \((e^{-1}+o(1))W\) expected owner
holes.  Correlated near-factor selection is essential.

## 7. The augmented packet gate

For a selected packet family \(\mathcal M\) containing one packet at every
top, let

\[
 \mu_0(X)=|\{P\in\mathcal M:X\in M(P)\}|                                  \tag{7.1}
\]

be the owner load.  For \(1\le q<H\), let \(\mu_q^-\) and \(\mu_q^+\)
be its two target-load vectors.  Each of these signed rows has total mass
exactly \(S\).

For each signed row, choose an integral balanced quota vector

\[
 b_q^\pm(T)\in
 \left\{\left\lfloor\frac{S}{N_q}\right\rfloor,
             \left\lceil\frac{S}{N_q}\right\rceil\right\},
 \qquad
 \sum_Tb_q^\pm(T)=S.                                                      \tag{7.2}
\]

Define the aggregate quota excess

\[
 \mathsf E(\mathcal M,b)
 =\sum_{q=1}^{H-1}
 \left[
  \sum_T(\mu_q^-(T)-b_q^-(T))_+
  +\sum_T(\mu_q^+(T)-b_q^+(T))_+
 \right].                                                                \tag{7.3}
\]

The precise sufficient statement is:

> **Augmented top-packet near-factor \((\mathrm{ATPNF})\).**  There are
> one packet \(P_U\) for every top \(U\), and balanced quotas (7.2), such
> that
> \[
>    \mu_0(X)\le1\quad\text{for every owner }X,                            \tag{7.4}
> \]
> and
> \[
>    \mathsf E(\mathcal M,b)=o(W).                                        \tag{7.5}
> \]

### Theorem 7.1 (\(\mathrm{ATPNF}\) implies coefficient one)

If \((\mathrm{ATPNF})\) holds, then there is a contiguous-OR word of length
\(W+o(W)\) covering every nonempty subset of \([2m]\).

#### Proof

Condition (7.4) makes the \(S\) packet owners distinct, leaving exactly
\(W-S=o(W)\) middle owners.  Cut every promotion cycle once.  The selected
packets compile with length

\[
 S+O(HN_H)=S+o(W)                                                         \tag{7.6}
\]

by (0.6).  Append the \(W-S\) uncovered middle masks literally.

At a fixed signed depth, the load vector and quota vector both have total
mass \(S\).  Hence their total deficit below quota equals their total excess
above quota.  Every positive quota is at least one, so the number of missed
targets is at most

\[
 (N_q-S)_++\sum_T(\mu_q(T)-b_q(T))_+.                                     \tag{7.7}
\]

Sum (7.7) over both signs and all proper depths.  Proposition 3.1 and
(7.5) give \(o(W)\) missing band masks.  Append them literally.  Upper
depth \(H\) has no holes because one packet was selected at every top.
Finally append the two outer tails, whose size is \(O(W/H)=o(W)\) by
(1.9).  The total length is \(W+o(W)\). \(\square\)

### 7.1 Exact augmented hypergraph form

For fixed quotas \(b\), replace every signed target \(T\) by
\(b_q^\pm(T)\) capacity clones.  Expand a packet column by assigning each
of its \(M\) distinct targets at that row to one clone.  Keep middle owners
as capacity-one vertices and keep each top as one contracted tag of weight
\(M\).  A selection satisfying all capacities has zero excess in (7.3).

When \(S<N_q\), the balanced vector has \(S\) targets of quota one and the
remaining targets quota zero; the latter are exactly the unavoidable scalar
holes.  When \(S\ge N_q\), every target has positive quota.  This is the
exact augmented packet hypergraph whose integral near-factor would prove
\((\mathrm{ATPNF})\).

Theorem 4.1 gives its one-row degrees, Theorem 5.1 gives the diffuse
same-rank codegrees, Proposition 5.2 gives the stronger owner overlap
profile, and (6.1) identifies the vertical nested backbone that must be
quotiented.  No theorem rounding this clustered, growing-uniformity system
is proved here.

## 8. Final audit

The calibrated route passes the following checks.

1. **Correct crossing direction:** minimal \(\lambda_H\ge M\) gives
   \(MN_H\le W\), not an overfull owner ledger.
2. **Asymptotic calibration:** \(\lambda_H/M=1+O(H/m)\) and
   \(H\sim\sqrt{m\log m}\).
3. **Owner leave:** \(W-MN_H=O(WH/m)=o(W)\).
4. **Reset toll:** one cut per top costs \(O(HN_H)=o(W)\).
5. **All-rank scalar holes:** their aggregate, not merely each row, is
   \(o(W)\).
6. **Local validity:** every packet is a genuine promotion path after one
   cut and exposes all cyclic interval ranks simultaneously.
7. **Owner incidence:** exact degree (0.8), maximum relative codegree
   \(2/m^2\), and packetwise overlap profile \(O(1/m)\).
8. **Top quotient:** top tags have the calibrated degree ratio
   \(D_0/D_{\rm top}=1-o(1)\).
9. **Failure of independence:** uncorrelated choices leave an
   \(e^{-1}\)-fraction of owners uncovered.
10. **Remaining issue:** correlated integral selection with aggregate
    all-ranks quota excess \(o(W)\), exactly \((\mathrm{ATPNF})\).

Thus there is no count, capacity, fixed-frame, or local-codegree
refutation.  The sharp unresolved object is a clustered augmented
near-factor: contract top tags and vertical interval columns, then round the
nearly regular packet orbit while preserving the sparse owner-overlap
profile.  A claim based only on ordinary maximum codegree would omit the
nested cross-rank correlations in (6.1).
