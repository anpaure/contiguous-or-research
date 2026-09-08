# OCR transported overlap: exact bridge parsing and a cap-valid critical family

Date: 2026-07-25

Method: pure mathematics only; no computation, finite search, solver, or web
search.

## 0. Outcome

Fix two phases (0\le t<u<s), put

\[
 d=u-t,
 \qquad \sigma=s-d-1,
\]

and retain the transported terminal equation

\[
 \mathcal A_{t,u}R_t=R_u\mathcal C_{t,u},
 \tag{0.1}
\]

where

\[
 \mathcal A_{t,u}
 = (\overline T_{u-1}0)\cdots(\overline T_t0),
 \qquad
 \mathcal C_{t,u}
 = (0S_u)\cdots(0S_{t+1}).
 \tag{0.2}
\]

The free-monoid overlap alternative says that, when

\[
 |R_u|<|\mathcal A_{t,u}|,
\]

there is a unique word (H) such that

\[
 \mathcal A_{t,u}=R_uH,
 \qquad
 \mathcal C_{t,u}=HR_t,
 \qquad
 \operatorname {net}(H)=\sigma.
 \tag{0.3}
\]

This report proves two new facts about that alternative.

1.  The bridge has a unique two-sided block parse.  The original PBBS
    caps then force

    \[
       \ell\ge t,
       \qquad \ell\ge s-u-1,
       \qquad \sigma\le2\ell,
       \tag{0.4}
    \]

    where (2\ell) is the endpoint excess.  They also force the bridge
    to start in a dual block of index at most ((u-1)/2) and to end in a
    forward block of index at least ((s+t)/2).  Thus overlap is confined
    to a genuinely cross-corridor phase pair.

2.  Those restrictions do **not** produce a vanishing transported-
    compatibility factor.  There is an explicit family of genuine first
    zero-winding PBBS returns, satisfying the exact caps and chronology,
    parameterized by every strip path (Y:0\to K) in ([0,K]).  Its
    common bridge is

    \[
       H=0Y0,
    \]

    and, after deterministic collars are removed and this common word is
    counted once, its generating function is exactly

    \[
       \boxed{
       G_K(x)={x^K\over Q_{K+1}(x^2)}.}
       \tag{0.5}
    \]

    This is the full top-to-bottom strip kernel, coefficient by
    coefficient.  At the critical point,

    \[
       G_K(1/2)={2\over K+2}.
       \tag{0.6}
    \]

    Hence the overlapping transported equation has no uniform
    coefficientwise (o(1)) penalty relative to the corresponding free
    corridor kernel.  The example is an actual PBBS family, not merely a
    formal word-equation family.

For (s=3q,t=q-1,u=2q), one has (K=2q\asymp s).  Under the normalized
critical law, the variable semilength in (0.5) is of order (K^2), and a
fixed positive fraction of (0.6) lies on that scale.  Thus this critical
overlap obstruction occurs in a fixed Gaussian height window.

This does not disprove `OCR_s`: the deterministic collars in this family
can still make its global Catalan density small.  It rigorously closes the
more local lane in which an (o(1)) gain is supposed to follow from the
transported overlap equation, the PBBS caps, and first-return chronology
alone.  Any successful overlap estimate must charge additional global
rarity or packing information.

## 1. Canonical parsing of every positive-net overlap bridge

Every word (overline T_j) has net zero and
(operatorname {rev}(\overline T_j)) is Dyck.  Every (S_j) is Dyck.
Consequently a whole suffix of (mathcal A_{t,u}) beginning at a block
boundary has negative net, while a whole prefix of
(mathcal C_{t,u}) ending at a block boundary has negative net.  Since
(operatorname {net}(H)=\sigma\ge0), and the genuinely overlapping case
used below has (sigma>0), both endpoints of (H) lie strictly inside
blocks.

### Theorem 1.1 (unique two-sided bridge parse)

Assume (sigma>0).  There are unique indices

\[
 t\le j\le u-1,
 \qquad
 t+1\le k\le u,
\]

and unique words (X,Y) such that

\[
 H=X0(\overline T_{j-1}0)\cdots(\overline T_t0),
 \tag{1.1}
\]

where (X) is a proper suffix of (overline T_j), and

\[
 H=(0S_u)\cdots(0S_{k+1})0Y,
 \tag{1.2}
\]

where (Y) is a proper prefix of (S_k).  Moreover

\[
 \boxed{
 \operatorname {net}(X)=s-u+j,
 \qquad
 \operatorname {net}(Y)=s+t-k.}
 \tag{1.3}
\]

The reversed word (operatorname {rev}X) is a nonnegative prefix of
the Dyck word (operatorname {rev}(\overline T_j)), and (Y) is a
nonnegative prefix of the Dyck word (S_k).

#### Proof

The first letter of (H) has a unique physical location in the block
array (mathcal A_{t,u}).  If it were at the beginning of a block,
then the suffix from that point would contain only complete net-zero
(overline T)-words and at least one delimiter zero, and hence would
have negative net.  Thus it lies strictly inside one
(overline T_j), giving (1.1) uniquely.

Put (a=j-t+1), the number of delimiter zeroes in (1.1).  Since all
complete (overline T)-words have net zero,

\[
 \operatorname {net}(H)=\operatorname {net}(X)-a.
\]

Using

\[
 \sigma=s-(u-t)-1
\]

gives

\[
 \operatorname {net}(X)
 =\sigma+j-t+1=s-u+j.
\]

Because (X) is a suffix, (operatorname {rev}X) is a prefix of
(operatorname {rev}(\overline T_j)); reversal preserves net height.

The ending location of (H) is likewise unique in
(mathcal C_{t,u}).  Ending at a block boundary would give a prefix
made from complete net-zero (S)-words and delimiter zeroes, hence
negative net.  Thus it ends strictly inside one (S_k), giving (1.2).
There are (b=u-k+1) delimiter zeroes in (1.2), so

\[
 \operatorname {net}(Y)=\sigma+b=s+t-k.
\]

As a prefix of the Dyck word (S_k), the word (Y) is nonnegative.
This proves all assertions. (square)

### Corollary 1.2 (exact cap consequences)

For a genuine zero-winding return of endpoint excess (2\ell), every
overlap bridge with (sigma>0) satisfies

\[
 \boxed{
  2j\le u-1,
  \qquad
  2k\ge s+t,
  \qquad
  \ell\ge s-u-1,
  \qquad
  \ell\ge t.}
 \tag{1.4}
\]

In particular

\[
 \boxed{
 u\ge2t+1,
 \qquad
 2u\ge s+t,
 \qquad
 \sigma=t+(s-u-1)\le2\ell.}
 \tag{1.5}
\]

#### Proof

The shifted PBBS caps are

\[
 \operatorname {ht}(T_j)
 \le\min\{s-1-j,j+1+\ell\},
 \tag{1.6}
\]

and

\[
 \operatorname {ht}(S_k)
 \le\min\{k,s-k+\ell\}.
 \tag{1.7}
\]

Theorem 1.1 gives

\[
 s-u+j\le\operatorname {ht}(T_j),
 \qquad
 s+t-k\le\operatorname {ht}(S_k).
\]

Comparison with the two terms of (1.6) yields respectively

\[
 2j\le u-1,
 \qquad
 \ell\ge s-u-1.
\]

Comparison with the two terms of (1.7) yields

\[
 2k\ge s+t,
 \qquad
 \ell\ge t.
\]

Since (j\ge t) and (k\le u), the first two necessary phase
inequalities in (1.5) follow.  Finally

\[
 \sigma=s-u+t-1=t+(s-u-1),
\]

and both summands are at most (ell). (square)

Thus if (ell=o(s)), every overlap pair has

\[
 t=o(s),
 \qquad s-u=o(s),
 \qquad d=s-o(s),
 \qquad \sigma=o(s).
 \tag{1.8}
\]

Conversely, a bridge of height (sigma\asymp s) is possible only in a
macroscopic endpoint-overlap sector (ell\ge\sigma/2).

## 2. An exact cap-valid PBBS family carrying the full strip kernel

Let integers (s,t,u) satisfy

\[
 0\le t<u<s,
 \tag{2.1}
\]

and put

\[
 d=u-t,
 \qquad
 K=s-d+1=s-u+t+1.
 \tag{2.2}
\]

Assume

\[
 \boxed{
 K\le s-1-t,
 \qquad
 K\le u.}
 \tag{2.3}
\]

Equivalently,

\[
 u\ge2t+2,
 \qquad
 2u\ge s+t+1.
 \tag{2.4}
\]

Let (mathscr Y_K) be the set of all zero-one walks (Y) which start
at zero, end at (K), and stay in the strip ([0,K]).  Thus every
(Y\inmathscr Y_K) has

\[
 |Y|=K+2n
 \tag{2.5}

for a unique (n\ge0).

For such a word define

\[
 \overline T=0^K Y,
 \qquad
 S=Y0^K.
 \tag{2.6}
\]

The word (overline T) has nonpositive prefixes, net zero, and depth
(K), so its bit-complement (T) is Dyck of height (K).  The word
(S) is Dyck of height (K).  The key literal identity is

\[
 \boxed{
 \overline T,0^K=0^K S.}
 \tag{2.7}
\]

Set

\[
 T_t=T,
 \qquad S_u=S,
 \tag{2.8}
\]

and let every other (T_j,S_j), including (S_s), be empty.

### Theorem 2.1 (actual first zero-winding realization)

For every (Y\inmathscr Y_K), the Dyck word

\[
 \boxed{
 D_0=1^{s-1-t}0^K Y1^{t+1}0^s}
 \tag{2.9}

starts a genuine first zero-winding PBBS return of duration (s), with
the staircase data (2.8).

If

\[
 L=|\overline T|=K+|Y|=2K+2n,
 \tag{2.10}
\]

then its semilength, endpoint excess, and endpoint first-maximum
positions are

\[
 \boxed{
 m=s+{L\over2}=s+K+n,
 \qquad
 \Lambda=L=2(m-s),}
 \tag{2.11}
\]

and

\[
 \boxed{
 \delta(D_0)=\delta(D_s)=s+L.}
 \tag{2.12}
\]

#### Proof

Define prefixes (P_j) by

\[
 P_j=
 \begin{cases}
  1^{s-1-t+j}\overline T1^{t-j},&0\le j\le t,\\
  1^{s-1},&t+1\le j\le u,\\
  1^{k-1}S1^{s-k},&j=u+k, 1\le k\le s-u,
 \end{cases}
 \tag{2.13}
\]

and terminal corridors (R_j) by

\[
 R_j=
 \begin{cases}
  0^{s-1},&0\le j\le t,\\
  0^{k-1}\overline T0^{s-k},
       &j=t+k, 1\le k\le d-1,\\
  0^{s-1},&u\le j\le s.
 \end{cases}
 \tag{2.14}
\]

Let the terminal suffix at phase (j) be the word (S_j) from (2.8),
and put

\[
 D_j=P_j1R_j0S_j.
 \tag{2.15}
\]

First check legality.  In the first line of (2.13), the copy of
(overline T) is based at height

\[
 s-1-t+j\ge s-1-t\ge K.
\]

It never rises above that base and descends by at most (K).  The final
ones take the endpoint to height (s-1).  Hence (P_j) stays in
([0,s-1]).  In the last line, the (S)-excursion is based at (k-1).
Since (k\le s-u), (2.3) gives

\[
 k-1+K\le s-u-1+K\le s-1,
\]

so these prefixes are legal as well.

For the middle line of (2.14), start at height (s).  After the first
(k-1) zeroes and the initial (0^K) in (overline T), the height is

\[
 s-(k-1)-K=d-k\ge1.
\]

During (Y) it stays between (d-k) and

\[
 d-k+K=s-k+1\le s.
\]

The final (s-k) zeroes end at height one.  Thus every (R_j) stays in
([1,s]) and has net (1-s).

The literal local identities are

\[
 S_j1P_j=P_{j+1}1\overline T_j,
 \tag{2.16}
\]

and

\[
 \overline T_j0R_j=R_{j+1}0S_{j+1}.
 \tag{2.17}
\]

Away from (j=t,u-1,u), these identities merely move one terminal
one or zero across an empty block.  At (j=t), (2.16) reads

\[
 1(1^{s-1}\overline T)=1^{s-1}1\overline T,
\]

and (2.17) reads

\[
 \overline T0^s=(\overline T0^{s-1})0.
\]

At (j=u-1), (2.17) is exactly

\[
 0^{d-1}\overline T0^K=0^sS,
\]

which follows from (2.7) and (d-1+K=s).  At (j=u), (2.16) reads

\[
 S1^s=(S1^{s-1})1.
\]

Thus (2.16)--(2.17) hold at every phase.  Concatenating them gives

\[
 P_{j+1}1R_{j+1}0S_{j+1}=S_j1P_j0R_j.
\]

The right side is the exact canonical block rotation of
(D_j=P_j1R_j0S_j).  Hence (D_{j+1}=\tau D_j) for every (j<s).
All displayed factorizations are canonical by the prefix and corridor
legality just proved.

Now put (L=|T|=|S|).  Formula (2.13) gives

\[
 \delta(D_j)=|P_j|+1
 =\begin{cases}
   s+L,&0\le j\le t,\\
   s,&t+1\le j\le u,\\
   s+L,&u+1\le j\le s.
  \end{cases}
 \tag{2.18}
\]

The chronological deficits are

\[
 c_j=|S_j|+1
 =\begin{cases}
   L+1,&j=u,\\
   1,&j\ne u.
  \end{cases}
 \tag{2.19}
\]

Therefore

\[
 \sum_{i<j}c_i
 =\begin{cases}
   j,&j\le u,\\
   j+L,&j\ge u+1.
  \end{cases}
 \tag{2.20}
\]

For every (1\le j<s), (2.18)--(2.20) give the strict first-return
inequality

\[
 \sum_{i<j}c_i<\delta(D_j).
 \tag{2.21}
\]

At (j=s) there is equality:

\[
 \sum_{i<s}c_i=s+L=\delta(D_s).
 \tag{2.22}
\]

The exact PBBS zero-winding first-passage criterion now proves that this
is a genuine first return of duration (s).

Finally, (2.9) has length (2s+L), proving
(m=s+L/2).  Equations (2.18) and the endpoint identity

\[
 \Lambda=\delta(D_0)+\delta(D_s)-2m
\]

give (Lambda=L). (square)

## 3. The common carrier and transported bridge are counted once

For the family of Theorem 2.1, the full endpoint certificates are

\[
 \begin{aligned}
 \mathcal A_{m full}
 &=0^{s-1-t}\overline T0^{t+1},\\
 \mathcal C_{m full}
 &=0^{s-u+1}S0^{u-1}.
 \end{aligned}
 \tag{3.1}
\]

Since (R_0=R_s=0^{s-1}), both have the exact common-carrier form

\[
 \boxed{
 \mathcal A_{m full}=R_sO,
 \qquad
 \mathcal C_{m full}=OR_0,}
 \tag{3.2}
\]

with

\[
 \boxed{
 O=0^{s-u+1}Y0^{t+1}.}
 \tag{3.3}
\]

Indeed (s-1-t+K-(s-1)=s-u+1), while
(K+u-1=s+t=(t+1)+(s-1)).  Also

\[
 \operatorname {net}(O)=-1,
 \qquad
 |O|=K+1+|Y|=L+1=\Lambda+1,
 \tag{3.4}
\]

as required because (S_s) is empty.  In particular the word (Y) is
one literal piece of the outer carrier; it is not two independent array
words.

At phases (t,u), the shorter transported collars are

\[
 \begin{aligned}
 \mathcal A_{t,u}
 &=0^{d-1}\overline T0=0^sY0,\\
 \mathcal C_{t,u}
 &=0S0^{d-1}=0Y0^s.
 \end{aligned}
 \tag{3.5}
\]

Consequently

\[
 \boxed{
 \mathcal A_{t,u}=R_uH,
 \qquad
 \mathcal C_{t,u}=HR_t,
 \qquad
 H=0Y0,}
 \tag{3.6}
\]

where (R_t=R_u=0^{s-1}).  Its net is

\[
 \operatorname {net}(H)=K-2=s-d-1=\sigma.
 \tag{3.7}
\]

This verifies the overlap alternative literally, with no duplicate copy
of (O) or (H).

## 4. Exact generating function and coefficientwise no-go

Let (a_{K,n}) be the number of paths (Y\inmathscr Y_K) of length
(K+2n).  Put

\[
 Q_0(z)=Q_1(z)=1,
 \qquad
 Q_{j+1}(z)=Q_j(z)-zQ_{j-1}(z).
 \tag{4.1}
\]

### Lemma 4.1 (full strip kernel)

One has

\[
 \boxed{
 \sum_{n\ge0}a_{K,n}x^{K+2n}
 ={x^K\over Q_{K+1}(x^2)}.}
 \tag{4.2}
\]

#### Proof

Let (A_K) be the adjacency matrix of the path on vertices
(0,1,\ldots,K).  The left side is the ((0,K))-entry of
((I-xA_K)^{-1}).  Expanding the determinant along the last vertex gives

\[
 \det(I-xA_K)=Q_{K+1}(x^2).
\]

The ((K,0))-cofactor is the unique monotone chain product (x^K).
Cramer's rule proves (4.2). (square)

The map (Y\mapsto D_0) in (2.9) is injective, and Theorem 2.1 gives

\[
 \boxed{
 \sum_{Y\in\mathscr Y_K}z^{m(D_0)}
 ={z^{s+K}\over Q_{K+1}(z)}.}
 \tag{4.3}
\]

For every (n\ge0), the coefficient at (z^{s+K+n}) is exactly
(a_{K,n}).  After deleting the deterministic rank (s+K), this is the
same coefficient (a_{K,n}) as the unrestricted strip corridor.  Hence
there cannot exist numbers (arepsilon_s\to0) for which transported
overlap compatibility, even together with the exact caps and first-return
chronology used above, gives the coefficientwise estimate

\[
 [x^{K+2n}]\mathscr L_{m overlap}(x)
 \le\varepsilon_s
 [x^{K+2n}]G_K(x)
 \tag{4.4}
\]

uniformly in (n): the family above already contributes the entire
right side.

At (z=1/4), the recurrence gives

\[
 Q_j(1/4)={j+1\over2^j}.
 \tag{4.5}
\]

Thus (4.2) has exact critical mass

\[
 G_K(1/2)
 ={2^{-K}\over Q_{K+1}(1/4)}
 ={2\over K+2}.
 \tag{4.6}
\]

For (K\asymp s), this is (Theta(1/s)), with the exact constant
visible.  It is the ordinary corridor scale, not (o(1/s)).

## 5. Exact Gaussian-scale accounting

Normalize the critical weights in (4.2), and let (M) be the extra
semilength:

\[
 \Pr(M=n)
 ={a_{K,n}4^{-n}\over Q_{K+1}(1/4)^{-1}}.
 \tag{5.1}
\]

Put (N=K+1).  The exact critical expansion is

\[
 Q_N(z)
 =2^{-N}\sum_{r\ge0}
   {N+1\choose2r+1}(1-4z)^r.
 \tag{5.2}
\]

It follows that

\[
 {Q_N'(1/4)\over Q_N(1/4)}
 =-{2N(N-1)\over3},
 \tag{5.3}
\]

and

\[
 {Q_N''(1/4)\over Q_N(1/4)}
 ={4N(N-1)(N-2)(N-3)\over15}.
 \tag{5.4}
\]

Since the probability generating function of (M) is the normalized
reciprocal of (Q_N), logarithmic differentiation gives

\[
 \boxed{
 \mathbb EM={K(K+1)\over6},}
 \tag{5.5}
\]

and

\[
 \boxed{
 \operatorname {Var}(M)
 ={K(K+1)(K+3)(K+4)\over90}.}
 \tag{5.6}
\]

For completeness, (5.6) follows from

\[
 \operatorname {Var}(M)
 =-z{Q_N'\over Q_N}
  -z^2\left({Q_N''\over Q_N}
             -\left({Q_N'\over Q_N}\right)^2\right)
 \quad(z=1/4).
\]

For (K\ge5), (5.5)--(5.6) imply

\[
 \mathbb E M^2\le2(\mathbb EM)^2.
\]

Paley--Zygmund and Markov therefore give

\[
 \Pr\left({\mathbb EM\over2}\le M\le16\mathbb EM\right)
 \ge {1\over8}-{1\over16}={1\over16}.
 \tag{5.7}
\]

Consequently the portion of the bit-series (4.2) with

\[
 {K(K+1)\over12}
 \le n\le
 {8K(K+1)\over3}
 \tag{5.8}
\]

has critical mass at least

\[
 \boxed{{1\over8(K+2)}.}
 \tag{5.9}
\]

Now specialize to

\[
 s=3q,
 \qquad t=q-1,
 \qquad u=2q.
 \tag{5.10}
\]

Then (2.3) holds with equality and

\[
 d=q+1,
 \qquad K=2q={2s\over3},
 \qquad \sigma=2q-2.
 \tag{5.11}
\]

For the mass in (5.8), Theorem 2.1 gives

\[
 m=s+K+n=\Theta(q^2)=\Theta(s^2).
 \tag{5.12}
\]

Thus (s=\Theta(\sqrt m)), and the lower mass (5.9) is
(Theta(1/s)).  This is the exact Gaussian-scale critical obstruction
promised in Section 0.

## 6. Precise proved boundary

Theorem 1.1 and Corollary 1.2 are universal for the overlap alternative:
they identify its unique two-sided partial-block parse and force
(sigma\le2\ell).

Theorem 2.1 is a genuine PBBS realization of a broad sublanguage.  On
that sublanguage, the bridge word, the full outer carrier, both endpoint
collars, every intermediate terminal corridor, all shifted height caps,
and the strict first-return inequalities are literal and exact.  Its
remaining degree of freedom is the entire strip path (Y), with no loss
relative to the scalar strip kernel.

Therefore a proof of `OCR_s` cannot obtain its vanishing factor from any
uniform assertion that overlapping transported compatibility is itself
subcritical after the deterministic pieces have been fixed.  The possible
next statements are strictly more global:

* charge the deterministic cross-corridor collars of this critical family;
* prove that their fixed-rank aggregate is Catalan-negligible;
* or use quotient-edge packing to show that few of these full strip fibres
  can coexist.

No coefficient-one conclusion is claimed.
