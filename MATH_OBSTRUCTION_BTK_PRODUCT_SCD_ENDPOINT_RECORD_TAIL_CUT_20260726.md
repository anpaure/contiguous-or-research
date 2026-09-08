# BTK product-SCD endpoints have an exact record-tail forbidden-set cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Fix the standard Greene--Kleitman/de Bruijn--Tengbergen--Kruyswijk
symmetric-chain decomposition of the Boolean lattice on each half of a
split (A\mathbin{\dot\cup}B), with (|A|=|B|=m), and take the usual
rank-(m) product diagonals.  This is a concrete complement-reversal
symmetric product SCD.

For a high endpoint (X), let (h=2|X\cap A|-m) be the length of its
product diagonal and let (I_A(X)) be the set of (A)-coordinates inserted
while that diagonal is traversed from low to high.  If (Y) is any
Johnson-adjacent high endpoint, with corresponding length (h'), then

\[
 \boxed{|I_A(X)\cap I_A(Y)|\ge h-4.}                 \tag{0.1}
\]

The point is that (I_A(X)) is exactly the last (h) strict ascending
record times of the (\{\pm1\})-walk encoded by (X\cap A).  A Johnson
move changes that record-time set in at most four positions; a cross-half
move changes it in at most two positions and changes (h) by two.

Consequently, for every product path of length

\[
                         5\le h\le H,               \tag{0.2}
\]

the endpoint-dependent forbidden set

\[
                         Z_X:=I_A(X)                 \tag{0.3}
\]

has size at most (H), yet the number of Johnson-adjacent product-path
endpoints whose active physical direction alphabet avoids (Z_X) is
exactly zero.  This remains true if the active alphabet means the union
(I_A(Y)\cup I_B(Y)), since it contains (I_A(Y)).

Thus this concrete complement-symmetric SCD does **not** have polynomial
robust endpoint degree uniformly over arbitrary forbidden coordinate sets.
It has robust minimum degree zero.  At

\[
                  H=\sqrt m\log\log m,              \tag{0.4}
\]

one may take (h=\sqrt m+O(1)), with the parity of (m).  The obstruction
then uses only (\sqrt m+O(1)=o(H)) forbidden coordinates.

The number of product diagonals of any admissible exact length
(h=m-2r>0) is

\[
 P_h=\binom mr^2-\binom m{r-1}^2.                  \tag{0.5}
\]

Hence, for (h=c\sqrt m+O(1)), (c>0) fixed,

\[
 P_h=\left(\frac{8c e^{-c^2}}{\sqrt\pi}+o(1)\right)
                  \frac{\binom{2m}{m}}m.           \tag{0.6}
\]

Every one of these high endpoints admits its own cut (0.3).  The
complement-reversal symmetry gives the identical low-end statement.

This is a counter-cut for the BTK/product choice, not a no-go for a
different SCD.  It says that endpoint mixing cannot be obtained merely by
choosing the standard explicit complement-symmetric chains and hoping that
Johnson adjacency randomizes their active alphabets.

## 1. The concrete complement-reversal symmetric SCD

Write a subset of ([m]) as a binary word

\[
                         w=w_1\cdots w_m.            \tag{1.1}
\]

Scan from left to right, keeping a stack of unpaired zeroes.  Each one is
paired with the most recent zero on the stack, when such a zero exists.
After the scan, erase the paired positions and list the unpaired positions

\[
                         u_1<\cdots<u_s.             \tag{1.2}
\]

Their values necessarily have the form

\[
                         1^p0^{s-p}.                 \tag{1.3}
\]

Indeed, an unpaired zero before an unpaired one would have been available
to pair with that one.

Fix the paired positions and their values.  Replacing (1.3) successively
by

\[
 0^s, 10^{s-1}, 1^20^{s-2},\ldots,1^s             \tag{1.4}
\]

gives a saturated symmetric chain.  The canonical pairing is unchanged
throughout (1.4), and every word has a unique canonical pairing, so these
chains partition (2^{[m]}).  This is the BTK SCD, denoted
(\mathcal G_m).

Let (\iota(i)=m+1-i) and define the complementing anti-automorphism

\[
 \vartheta(w)_i=1-w_{m+1-i}.                        \tag{1.5}
\]

A canonical pair (0\cdots1) is sent to a canonical pair
(0\cdots1), with its two positions reflected.  The unpaired word
(1^p0^{s-p}) is sent to (1^{s-p}0^p).  Therefore

\[
                         \vartheta(\mathcal G_m)=\mathcal G_m,  \tag{1.6}
\]

and (\vartheta) reverses every chain after sending it to its reflected
partner.

Literal complementation alone cannot preserve an SCD when (m\ge2): the
unique chain containing (\varnothing) would have to be setwise
complement-invariant, but its rank-one member ({i}) and rank-((m-1))
member are comparable, whereas the complement of ({i}) omits (i).
Thus (1.5) is the natural exact meaning of a complement-symmetric labelled
SCD.  Equivalently, on (A\dot\cup B), identify the two halves in reverse
order and combine (1.5) with the swap (A\leftrightarrow B).  It sends
each product diagonal to another product diagonal with reversed
orientation.

There is a tempting but invalid literal-symmetry shortcut.  For an arbitrary
SCD (\mathcal D), its literal complement image

\[
 \mathcal D^*=\{\{[m]\setminus X:X\in C\}:C\in\mathcal D\}       \tag{1.7}
\]

is another SCD after every chain is read upward.  But
(\mathcal D\cup\mathcal D^*) is a twofold owner multicover: every Boolean
set lies once in a chain of each decomposition.  It is not an
owner-disjoint SCD or path resolution.  Since (\mathcal D=\mathcal D^*) is
impossible by the preceding paragraph, a literal-complement two-frame atlas
requires a genuine integral choice between the two copies; simply adjoining
the complement frame duplicates every owner.

## 2. Active coordinates are terminal strict records

For a word (w), put

\[
 D_w(t)=\sum_{i=1}^t(2w_i-1),\qquad D_w(0)=0,       \tag{2.1}
\]

and let

\[
 \mathcal R(w)=
 \{t: D_w(t)>\max_{0\le s<t}D_w(s)}               \tag{2.2}
\]

be its strict ascending record-time set.  Write its elements in increasing
order as

\[
                         \tau_1<\cdots<\tau_M.       \tag{2.3}
\]

Here (D_w(\tau_j)=j) and (M=\max_tD_w(t)).

### Lemma 2.1 (unpaired-one record lemma)

The unpaired one-positions in the BTK pairing of (w) are exactly
(\mathcal R(w)).

#### Proof

After cancellation of all (01)-pairs in a prefix, the uncancelled word
is (1^a0^b).  A new one is unpaired precisely when (b=0), namely when
the new height exceeds every previous prefix height.  This is exactly the
condition in (2.2).  Successive such events first hit the levels
(1,2,\ldots,M).  \(\square\)

Suppose now that (w) has weight (k\ge m/2), and put

\[
                         h=2k-m.                    \tag{2.4}
\]

Let (a) be the minimum rank of the BTK chain containing (w).  By Lemma
2.1, (M) of the (k) one-positions are unpaired, so

\[
                         a=k-M.                     \tag{2.5}
\]

The member (w) is the rank-(k) member of its chain, hence it uses the
first (k-a=M) unpaired positions.  Its symmetric rank-((m-k)) ancestor
uses the first

\[
 (m-k)-a=m-k-(k-M)=M-h                             \tag{2.6}
\]

unpaired positions.  We have therefore proved the following exact formula.

### Proposition 2.2 (record-tail formula)

The set of coordinates inserted between the symmetric rank-((m-k)) and
rank-(k) members of the BTK chain is

\[
 I_h(w)=\{\tau_{M-h+1},\ldots,\tau_M\},             \tag{2.7}
\]

the last (h) strict ascending record times of (w).

Notice that (M\ge D_w(m)=h), so (2.7) always has exactly (h)
elements.

## 3. Record times are stable under one Johnson move

We need an exact deterministic stability statement, not a probabilistic
estimate.

### Lemma 3.1 (interval perturbation)

Let (w,w') have the same weight and differ by exchanging one zero and one
one.  Then

\[
                         |\mathcal R(w)\mathbin\triangle
                           \mathcal R(w')|\le4.       \tag{3.1}
\]

If (w,w') differ in one bit, then

\[
                         |\mathcal R(w)\mathbin\triangle
                           \mathcal R(w')|\le2.       \tag{3.2}
\]

#### Proof

First suppose the exchanged positions are (u<v), with
(w_u=0,w_v=1) and (w'_u=1,w'_v=0).  Then

\[
 D_{w'}(t)=
 \begin{cases}
 D_w(t)+2,&u\le t<v,\\
 D_w(t),&t<u\text{ or }t\ge v.
 \end{cases}                                        \tag{3.3}
\]

Put (P=\max_{t<u}D_w(t)).  Inside ([u,v)), a record time for (w)
is a local record whose level is at least (P+1).  A record time for
(w') is a local record whose old level is at least (P-1).  Thus the
lift in (3.3) can add only the first local visits to the two levels
(P-1,P): at most two record times.

At time (v), the two walks meet again.  Their accumulated pre-(v)
maxima differ by an integer in ({0,1,2}).  Beyond (v), their paths are
identical, so the walk with the larger accumulated maximum can omit at
most the first two suffix record levels of the other.  This contributes at
most two further record times.  Hence (3.1).  If the signs at (u,v) are
opposite, interchange (w,w'); the same argument applies.

For a one-bit change, the two height walks agree before the changed
position and differ by the constant (2) or (-2) thereafter.  Relative
to the common prefix maximum, lowering the suffix suppresses at most its
first two record levels, while raising it adds at most two.  This proves
(3.2).  \(\square\)

We also use the elementary ordered-tail estimate below.

### Lemma 3.2 (tail edit bound)

Let (E,E') be finite subsets of a linearly ordered set, with
(|E\triangle E'|\le d).  If (T_s(E)) and (T_t(E')) denote their last
(s) and last (t) elements, respectively, and the indicated tails
exist, then

\[
 |T_s(E)\setminus T_t(E')|\le d+(s-t)_+.            \tag{3.4}
\]

#### Proof

Put (a=|E\setminus E'|) and (b=|E'\setminus E|), so (a+b\le d).
Deleting (E\setminus E') removes at most (a) elements from (T_s(E)).
The surviving part

\[
                         T_s(E)\cap E'               \tag{3.5a}
\]

is a terminal segment of (E\cap E') and has size at most (s).  Before
the (b) new elements of (E'\setminus E) are inserted, passing to a
terminal (t)-set can discard at most ((s-t)_+) elements of (3.5a).
Each inserted element can displace at most one further old element from
that terminal (t)-set.  The total loss is at most
(a+(s-t)_++b\le d+(s-t)_+), proving (3.4).  This argument does not
require (T_t(E)) to exist when (t>s).  \(\square\)

### Corollary 3.3 (active-tail stability)

Let (w) have weight (k\ge m/2), let (h=2k-m), and let (w') arise
as the (A)-restriction of a Johnson neighbor on
(A\dot\cup B).  Put (k'=|w'|) and (h'=2k'-m).  Provided (h'>0),

\[
                         |I_h(w)\cap I_{h'}(w')|
                         \ge h-4.                   \tag{3.5}
\]

#### Proof

There are three cases.

* An edge internal to (A) exchanges one zero and one one.  Lemma 3.1
  gives (d\le4), while (h'=h).  Apply Lemma 3.2.
* An edge internal to (B) leaves (w) and (h) unchanged.
* A cross-half edge changes one bit of (w).  Then (d\le2) and
  (h'=h\pm2).  Lemma 3.2 gives a loss of at most (2+2=4).

Formula (2.7) identifies the tails with the active sets.  \(\square\)

## 4. Product paths and the zero-degree cut

Take (\mathcal G_m) on each of (A) and (B).  If

\[
 C_a\subset\cdots\subset C_{m-a},\qquad
 D_b\subset\cdots\subset D_{m-b}                  \tag{4.1}
\]

are two chains, their rank-(m) product diagonal is

\[
 C_i\cup D_{m-i},qquad
 \max(a,b)\le i\le m-\max(a,b).                   \tag{4.2}
\]

Put (r=\max(a,b)).  The path length is

\[
                         h=m-2r,                    \tag{4.3}
\]

and its high endpoint has (A)-rank (m-r=(m+h)/2).  Its (A)-active
insertion alphabet is

\[
                         I_A=C_{m-r}\setminus C_r.  \tag{4.4}
\]

By Proposition 2.2, (4.4) is exactly (I_h(w)) for the high endpoint's
(A)-word (w).

Fix a high endpoint (X) with (h\ge5), and define (Z_X=I_A(X)).
If a Johnson neighbor (Y) is a product-path endpoint, then its (A)-rank
differs from that of (X) by at most one.  Since (h\ge5), this rank is
still strictly above (m/2); consequently (Y) cannot be a low endpoint
and must be a high endpoint.  Corollary 3.3 now gives

\[
                         |I_A(Y)\cap Z_X|\ge h-4>0. \tag{4.5}
\]

Thus, with

\[
 d_Z^+(X)=|{Y:XY\in E(J(2m,m)),\ Y\text{ is a product-path endpoint},
                     \ I_A(Y)\cap Z=\varnothing}|,             \tag{4.6}
\]

we have the exact identity

\[
                         \boxed{d_{Z_X}^+(X)=0.}     \tag{4.7}
\]

The same conclusion holds if eligibility asks the full carrier alphabet
(I_A(Y)\cup I_B(Y)) to avoid (Z_X).  Applying the anti-automorphism
from Section 1, together with the half swap, gives the low-end version.

### 4.1 Double-boundary endpoints and all neighbor types

The obstruction is especially transparent at the endpoint requested by a
natural raw-degree test.  Take both half chains to have minimum rank

\[
                         a=b=r,                     \tag{4.8}
\]

so the high endpoint is simultaneously the top of its (A)-chain and the
bottom of its (B)-chain.  Put (k=m-r) and (h=k-r).  Its (A)-word has
final height and maximum both equal to (h), so

\[
                         I_A(X)=\mathcal R(X\cap A). \tag{4.9}
\]

Every Johnson neighbor belongs to exactly one of the following four
classes.

1. **Internal (A) exchange.**  There are exactly (kr) such neighbors.
   The unchanged (B)-word is still a bottom chain member of minimum (r),
   so every one is a high product-path endpoint of length (h).
2. **Internal (B) exchange.**  There are exactly (rk) such neighbors.
   The unchanged (A)-word is still a top member of minimum (r), so every
   one is again a high endpoint of length (h).
3. **Cross move (B\to A).**  There are exactly (r^2) such neighbors.
   Adding a one to the top (A)-word raises a suffix of its height walk by
   two.  Its new final height is (h+2), and its maximum is at most the old
   maximum plus two, hence is exactly (h+2).  Thus its new (A)-word is
   automatically a top chain member of minimum (r-1).  Every one of these
   neighbors is a high endpoint of length (h+2).
4. **Cross move (A\to B).**  There are (k^2) Johnson neighbors before the
   endpoint condition is imposed.  Such a neighbor is a high endpoint of
   length (h-2) exactly when at least one of its two new half-chain minima
   equals (r+1).  We do not need to enumerate that subset.

Thus the unrestricted endpoint degree at this vertex is at least

\[
                         2rk+r^2=\Theta(m^2)         \tag{4.10}
\]

when (h=O(\sqrt m)).  The zero in (4.7) is therefore a genuine forbidden-set
collapse of polynomial raw degree, not an isolated endpoint with no
Johnson neighbors.

There is also exact nesting on the two cross-half classes.  If a one of the
top (A)-word is changed to zero, the new walk is the old walk lowered by two
on a suffix.  Every new strict record time was already an old strict record
time, so

\[
                         I_A(Y)\subseteq I_A(X)       \tag{4.11}
\]

for every endpoint in class 4.  If a zero is changed to one, the walk is
raised by two on a suffix; every old strict record remains a new strict
record, and the new maximum is (h+2).  Hence

\[
                         I_A(X)\subseteq I_A(Y)       \tag{4.12}
\]

throughout class 3.  Internal (B) exchanges give equality, while internal
(A) exchanges give the (h-4) overlap from Lemma 3.1.  This proves the cut
after a complete classification of neighbor types.

If one prefers the visibly complement-symmetric forbidden set

\[
                         Z_X^{\rm two}=I_A(X)\cup I_B(X),        \tag{4.13}
\]

then (|Z_X^{\rm two}|=2h) and the same proof applies a fortiori.  The
one-alphabet choice (Z_X=I_A(X)) is the sharper statement.

## 5. Exact census and the (H=\sqrt m\log\log m) scale

Every SCD of (2^{[m]}) has exactly

\[
 \binom mr-\binom m{r-1}                           \tag{5.1}
\]

chains of minimum rank (r), and exactly (\binom mr) chains of minimum
rank at most (r).  Therefore the number of ordered chain pairs with
(\max(a,b)=r), equivalently product paths of length (h=m-2r), is

\[
\begin{aligned}
 P_h
 &=\binom mr^2-\binom m{r-1}^2\\
 &=\binom mr^2
   \frac{4(h+1)(m+1)}{(m+h+2)^2}.                  \tag{5.2}
\end{aligned}
\]

This proves (0.5).  If (h=c\sqrt m+O(1)), the central local estimate

\[
 \binom m{(m-h)/2}
 =\left(\sqrt{\frac2{\pi m}}+o(m^{-1/2})\right)
       2^m e^{-c^2/2}                               \tag{5.3}
\]

and (\binom{2m}{m}\sim4^m/\sqrt{\pi m}) turn (5.2) into (0.6).

Finally choose an integer (h_m=\sqrt m+O(1)) having the parity of (m).
For all sufficiently large (m),

\[
 5\le h_m\le\sqrt m\log\log m.                    \tag{5.4}
\]

There are (P_{h_m}=\Theta(\binom{2m}{m}/m)) such paths, and for every
one of their high endpoints the set (Z_X) has only
(h_m=\sqrt m+O(1)) coordinates but gives degree zero.  Therefore no
uniform lower bound (m^{-C}\deg(X)), nor even a lower bound of one, can
hold for this product SCD at the requested scale.

## 6. Exact boundary of the obstruction

The obstruction uses two special BTK facts:

1. an endpoint's active alphabet is a terminal interval of a canonical
   record set; and
2. a one-edge perturbation changes that record set in boundedly many
   places.

It does not show that every complement-symmetric SCD has poor endpoint
mixing.  A positive construction must violate this bounded-edit property:
for most endpoints, one Johnson move must be able to replace a positive
fraction of the (h)-coordinate active alphabet.  In particular, any SCD
whose endpoint active map (I) obeys

\[
 \sup_{XY\in E(J(2m,m))}|I(X)\triangle I(Y)|=O(1)  \tag{6.1}
\]

on paths with (h\to\infty) has the same adversarial cut
(Z=I(X)) and cannot satisfy robust endpoint degree.
