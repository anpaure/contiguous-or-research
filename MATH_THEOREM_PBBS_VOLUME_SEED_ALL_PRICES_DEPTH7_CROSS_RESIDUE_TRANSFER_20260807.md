# A $2+6$ cross-residue transfer makes the volume seed control every depth-seven min-plus price

**Date:** 2026-08-07  
**Status:** unconditional all-price theorem for the terminal even
depth-seven parent/child pair.  This repairs the exact residue-one failure
of the one-dimensional prefix certificate.  No depth-eight or all-depth
claim is made.

## 1. A cross-residue transfer lemma

Let $p_1,\ldots,p_h$ be a closed piece table for which size $h$ has
minimum density.  For its min-plus closure put

\[
 e_i=p_i-{i\over h}p_h\quad(1\le i<h),
 \qquad
 \delta(L)=\psi(L)-{L\over h}p_h.
 \tag{1.1}
\]

Then $e_i\ge0$, and for every $j\ge1$,

\[
 \delta(i+jh)\le e_i.
 \tag{1.2}
\]

If a vector $x=(x_1,\ldots,x_{h-1})\in\mathbb Z_{\ge0}^{h-1}$ satisfies

\[
                         \sum_{i=1}^{h-1}ix_i=h+a,
 \tag{1.3}
\]

then every positive length congruent to $a$ after the first one also
satisfies

\[
                         \delta(a+jh)\le x\cdot e
                         \qquad(j\ge1).
 \tag{1.4}
\]

Indeed, use the pieces in $x$, followed by $j-1$ size-$h$ pieces.

### Lemma 1.1 (single-deficit cyclic transfer)

Let a volume-balanced price functional have positive coefficients
$s_i>0$ at lengths $1\le i<h$, zero reduced cost on multiples of $h$,
and negative coefficients at all later lengths.  Put

\[
 d_i=-\sum_{j\ge1}\mu_{i+jh},
 \qquad
 S_i=s_i-d_i.
 \tag{1.5}
\]

Suppose exactly one residue $a$ has a deficit

\[
                         S_a=-\Delta<0,
 \tag{1.6}
\]

and suppose there is a vector $x$ satisfying (1.3), with $x_a=0$, such
that

\[
                         S_i\ge\Delta x_i
                         \quad(i\ne a).
 \tag{1.7}
\]

Then the functional is nonnegative on every min-plus price whose
minimum-density denomination is $h$.

#### Proof

For residues $i\ne a$, bound every negative job directly by (1.2), at
total cost at most $d_i e_i$.  On the deficit residue, (1.2) and (1.4)
give

\[
 \sum_{j\ge1}(-\mu_{a+jh})\delta(a+jh)
 \le d_a\min(e_a,x\cdot e).
 \tag{1.8}
\]

Since $d_a=s_a+\Delta$ and both arguments of the minimum are
nonnegative,

\[
 d_a\min(e_a,x\cdot e)
 \le s_ae_a+\Delta x\cdot e.
 \tag{1.9}
\]

After subtracting these job bounds from the positive supply price, the
coefficient left at $e_i$ is at least $S_i-\Delta x_i\ge0$.  Multiples
of $h$ have zero reduced cost, and volume balance cancels the linear
part. \(\square\)

This is the smallest cyclic-subadditivity extension of the residue-prefix
lemma: a deficit residue is rerouted through an alternative partition of
its first post-$h$ length.

## 2. The terminal depth-seven coefficient measure

Take the terminal even depth-seven pair

\[
 D=7,\qquad n=142,\qquad n-2=140.
 \tag{2.1}
\]

Its child and parent volume margins are

\[
\begin{aligned}
 V_{140,7}&=6758985279718335862903013333535935437613,\\
 V_{142,7}&=7214609492569109394262920676290298581449.
\end{aligned}
 \tag{2.2}
\]

Let

\[
 \widehat\mu_L=
 V_{140,7}\nu_{142,7}(L)-V_{142,7}\nu_{140,7}(L),
 \tag{2.3}
\]

where

\[
 \nu_{n,D}(L)=
 \mathbf1_{L\le D}H_{n/2-D+L}^{(n)}
 -\widetilde H_{n/2-D-L}^{(n)}.
 \tag{2.4}
\]

As before, $\widetilde H_1^{(n)}=n$ and all other births use
$H_s^{(n)}={n\choose s}-{n\choose s-1}$.  Then

\[
 V_{140,7}
 \left(M_{142,7}(\psi)-{V_{142,7}\over V_{140,7}}M_{140,7}(\psi)\right)
 =\sum_L\widehat\mu_L\psi(L).
 \tag{2.5}
\]

The coefficient sequence has one sign change:

\[
 \widehat\mu_1,\ldots,\widehat\mu_6>0,
 \qquad
 \widehat\mu_L<0\quad(7\le L\le63).
 \tag{2.6}
\]

An exact short-rank certificate is

\[
\begin{aligned}
 \min_{1\le L\le6}\widehat\mu_L
 &=19504198402658544341130165052397821042350502535823139333338283436617709063957640,\\
 \widehat\mu_7
 &=-14298514253001271161892276661428130046682181514414405525406205798440625678234130.
\end{aligned}
 \tag{2.7}

For $8\le L\le61$, put $s=64-L$, so $3\le s\le56$.  The exact ratio

\[
 {H_s^{(142)}\over H_{s-1}^{(140)}}
 ={20022\over s(143-s)}
 \ge {3337\over812}>4
 >{V_{142,7}\over V_{140,7}}
 \tag{2.8}
\]

proves the negative tail sign.  At $L=62$, the modified child rank-one
term still gives a negative coefficient because

\[
 -H_2^{(142)}+{V_{142,7}\over V_{140,7}}\,140
 <-9869+2\cdot140<0.
 \tag{2.9}
\]

At $L=63$ only the negative parent rank-one term remains.

## 3. Minimum-density denominations at most six

For $2\le h\le6$, let

\[
 S_{h,a}=\sum_{j\ge0}\widehat\mu_{a+jh}
 \qquad(1\le a<h).
 \tag{3.1}
\]

The exact minima over nonzero residues are

\[
\begin{array}{c|c|r}
h&\operatorname*{argmin}_{1\le a<h}S_{h,a}
 &\min_{1\le a<h}S_{h,a}\\ \hline
2&1&81714134227955409413484843815974810872755584539600666681094368059826024899015918\\
3&1&52358894744317013570601412569948720234777073992531367038064159387394192125535573\\
4&3&34215631853198462083312926359945072924002850497680052034411643752496931888746098\\
5&3&26495096960629936624686705369610161964429924162239815482450517253502286565539291\\
6&1& 8147621675597562481307241958536921211432659788852774177334909418034660050978140
\end{array}
 \tag{3.2}
\]

Because of the one-sign-change pattern (2.6), every nonzero-residue
prefix first increases and then decreases to the positive total in (3.2).
The residue-prefix lemma therefore proves the desired all-price inequality
whenever some minimum-density denomination satisfies $h\le6$.  If $h=1$,
the price is linear and the normalized margin is zero.

## 4. The critical denomination seven

It remains to treat $h=7$.  Put

\[
 s_i=\widehat\mu_i,
 \qquad
 d_i=-\sum_{j\ge1}\widehat\mu_{i+7j},
 \qquad
 S_i=s_i-d_i
 \quad(1\le i\le6).
 \tag{4.1}
\]

The exact residue totals are

\[
\begin{array}{c|r}
i&S_i\\ \hline
1&-3423325714954379686130249243233713709218759036643730386067200682046346277185673\\
2&26486377602638340256381425911311270297186598322566409083432790199748331566606302\\
3&44721021616072616968544691357549323423475683704743690630403100544510365330506743\\
4&49119766494404897596329761876438372793178066866734482603985404996908552893452106\\
5&39269589696379585819119607330527421591193220794765908146569727561078037332345783\\
6&16570083831876472380860058149672936004379101275145063631160858912375696022213939
\end{array}
 \tag{4.2}
\]

Thus residue one has the sole deficit

\[
 \Delta=3423325714954379686130249243233713709218759036643730386067200682046346277185673.
 \tag{4.3}
\]

Use the alternative residue-one partition

\[
                         8=2+6.
 \tag{4.4}
\]

The two required surplus checks are strictly positive:

\[
\begin{aligned}
 S_2-\Delta
 &=23063051887683960570251176668077556587967839285922678697365589517701985289420629,\\
 S_6-\Delta
 &=13146758116922092694729808906439222295160342238501333245093658230329349745028266.
\end{aligned}
 \tag{4.5}
\]

Lemma 1.1 applies with $a=1$ and $x_2=x_6=1$.  This proves the missing
$h=7$ case.

## 5. Exact theorem and invariant-cone consequence

### Theorem 5.1 (all depth-seven prices)

For every closed depth-seven piece table and its complete min-plus
closure,

\[
 \boxed{
 M_{142,7}(\psi)
 -{V_{142,7}\over V_{140,7}}M_{140,7}(\psi)\ge0.}
 \tag{5.1}
\]

Equivalently, the exact minimum central weight for a unit distance-one
pair is the volume value

\[
 \boxed{
 \rho^{\rm vol}_7
 =2-{V_{142,7}\over V_{140,7}}
 ={6303361066867562331543105990781572293777
   \over6758985279718335862903013333535935437613}.}
 \tag{5.2}
\]

The linear price is tight, so the weight is minimal.  Under the Pascal
transfer, its Laurent seed

\[
                         W_0(z)=\rho^{\rm vol}_7+z+z^{-1}
 \tag{5.3}
\]

generates the exact nonnegative invariant orbit

\[
 W_N(z)=z^{-N}(1+z)^{2N}
              (\rho^{\rm vol}_7+z+z^{-1}),
 \tag{5.4}
\]

and every depth-seven fan-ray aggregate margin remains nonnegative along
that orbit.

## 6. General finite cyclic-transfer target

The proof isolates a reusable finite LP.  After direct residue coverage,
let $S_a<0$ be the remaining deficits and $S_i>0$ the surpluses.  For
each deficit residue $a$, use partitions of $h+a$ into pieces below $h$.
If nonnegative amounts of those partitions route every deficit while
using at most the surplus of each piece size, Lemma 1.1 extends verbatim
with several deficit residues.  This is a finite transportation LP on the
cyclic Apéry residues.

At depth seven the LP has one demand and one route,
$1\mapsto2+6$.
The all-depth problem is now to prove feasibility of this cyclic
transportation LP from total positivity of the binomial coefficient
measure, or to find the first depth at which it is infeasible.
