# Fixed-lag positive cells: exact literal overlap and the surviving bridge-renewal obstruction

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome and exact scope

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,
 \qquad H=\lceil A\sqrt r\rceil .
\]

Consider one genuine PBBS trajectory

\[
 D_i=\tau^iD_0,
 \qquad D_i=P_i1R_i0S_i,
\]

with the canonical first-maximum factorization at every phase.  Let

\[
 c_i=d(D_i)=|S_i|+1,
 \qquad \widehat c_i=d(\phi D_i).
\]

For every transition there is a canonical Dyck word (T_i) such that

\[
 \widehat c_i=|T_i|+1,
 \qquad
 S_i1P_i=P_{i+1}1\overline {T_i}.
 \tag{0.1}
\]

For the bounded-winding residual of the source theorem, nondiffuseness
actually permits a selected cell with

\[
 \boxed{|E_j\cap O_k|>\frac{\varepsilon N}{4K}
        =\Omega_{K,\varepsilon}(r),}
 \tag{0.1a}
\]

not merely \(N/(4H)\).  Cells with \(k<j\) are identically empty, the
diagonal sector has size \(O(B_r/r^{3/4})\), and the adjacent sector has
size

\[
 O_\varepsilon\!\left(B_r/r^{3/4}
        +B_r(\log r)^4/r\right).
 \tag{0.1b}
\]

Thus all negative, zero, and one-step lags are
\(o(B_r/\sqrt r)\).  Only \(k-j\ge2\) remains.

The main proved result is an exact literalization of a positive
chronological cell.  If (j<k), then one iterated free-monoid word has
two factorizations

\[
 \boxed{
 (S_k1)(S_{k-1}1)\cdots(S_j1)P_j
 =P_{k+1}(1\overline T_k)(1\overline T_{k-1})
       \cdots(1\overline T_j).}
 \tag{0.2}
\]

After one explicit translation of coordinates, the ledger cell
(E_j\cap O_k) is exactly the coordinate overlap of the designated
blocks

\[
 S_j1
 \qquad\hbox{and}\qquad
 \overline T_k1
 \tag{0.3}
\]

inside (0.2).  Thus a residual cell of length (L\) gives a literal
common substring of (S_j) and \(\overline T_k\) of length at least
(L-1).  In particular, the threshold (L\ge N/(4H)) gives

\[
 |Z|\ge {N\over4H}-1=\Omega_A(\sqrt r).
 \tag{0.4}
\]

This is genuine simultaneous \(\tau\)-chronology, not a scalar profile.

An attempted same-label maximal-overlap argument formerly claimed a
fourth endpoint kernel here.  That argument is **retracted**: the unfolded
history word duplicates separator occurrences, and the required
same-token identification has not been proved in the accepted chronology
model.  None of its former fixed-lag or aggregate-lag estimates is used
below.  The unconditional lag conclusions of this report are exactly
the negative-lag impossibility and the lag-zero/lag-one estimates in
Section 8.

The decisive audit is negative for the proposed automatic extra-strip
step.  A long common word of a Dyck word and a complemented Dyck word is
a bridge, not a new Dyck excursion.  There are Catalan-critically many
such bridges of Gaussian height.  More precisely, for every balanced
word (Z), with prefix-sum minimum (-p) and maximum (q),

\[
 S_Z=1^pZ0^p,
 \qquad T_Z=1^q\overline Z0^q
 \tag{0.5}
\]

are Dyck words, and (Z) occurs literally in both (S_Z) and
\(\overline T_Z\).  A positive fraction of the
\(\binom{2n}{n}=\Theta(4^n/\sqrt n)\) balanced words of length (2n)
have (p,q=O(\sqrt n)).  Hence even a linear-length common word, with
both carrier lengths interior-macroscopic and both carrier heights
Gaussian, has full bridge entropy.  The synchronized common word carries
the diagonal Green/renewal mode; it is not an independent fifth strip.

Conditioning on the bridge and imposing matching on both carrier sides
does not by itself remove this mode: for fixed lag the right root is the
bijective image \(\phi\tau^\ell D\), and the local bridge language itself
admits a two-sided matching of order \(4^n/\sqrt n\).  This saturation is
proved only for the literal carrier language.  No Catalan-density family
of compatible fixed-lag PBBS orbit edges is constructed.  A proof for
\(\ell\ge2\) must therefore use the intervening canonical transition
history to show that the bridge-rich permutation edges have vanishing
aggregate mass.  That two-time correlation theorem remains unproved.  No
PBBS counterexample and no coefficient-one conclusion are claimed.

## 1. The local dual block is literal

The block rotation identity is

\[
 D_{i+1}=\tau D_i=S_i1P_i0R_i.
 \tag{1.1}
\]

In (D_{i+1}), the transported old deepest visit is the height-maximum
visit at the end of (S_i1P_i), while the new canonical first deepest
visit is the earlier height-maximum visit at the end of (P_{i+1}1).
The word between those two visits is a nonpositive excursion.  Its
complement is therefore a Dyck word (T_i), and this proves the first
identity in

\[
 \boxed{
 S_i1P_i=P_{i+1}1\overline T_i,
 \qquad
 \overline T_i0R_i=R_{i+1}0S_{i+1}.}
 \tag{1.2}
\]

The second identity follows by comparing the remaining suffixes in the
two displayed factorizations of (D_{i+1}).  The canonical deficit of
the half-shifted state is

\[
 d(\phi D_i)=|T_i|+1.
 \tag{1.3}
\]

Taking lengths in the first identity gives

\[
 a_{i+1}-a_i=c_i-\widehat c_i,
 \qquad a_i:=\delta(D_i),
 \tag{1.4}
\]

which is the exact two-ledger telescope.

## 2. Iterated chronology and exact coordinate alignment

### Theorem 2.1 (iterated two-factor word)

For every (j\le k), define

\[
 \mathcal W_{j,k}
 :=(S_k1)(S_{k-1}1)\cdots(S_j1)P_j.
 \tag{2.1}
\]

Then

\[
 \boxed{
 \mathcal W_{j,k}
 =P_{k+1}(1\overline T_k)(1\overline T_{k-1})
       \cdots(1\overline T_j).}
 \tag{2.2}
\]

#### Proof

For (k=j), equation (2.2) is the first identity in (1.2).  If it holds
through (k-1), prepend (S_k1) and use

\[
 S_k1P_k=P_{k+1}1\overline T_k.
\]

This gives (2.2) by induction.  Every cancellation and substitution is
inside the free word monoid; no length-only relaxation is used.  If the
symbols are labelled and those labels are propagated through each block
permutation, the same induction is label-preserving.  Thus two aligned
positions in (2.2) represent the same transported symbol occurrence, not
merely equal zero--one values. \(\square\)

Now put

\[
 C_{j,k}:=\sum_{i=j}^k c_i.
 \tag{2.3}
\]

Use boundary coordinates on the word (2.2), starting at zero on its
left.  In the left factorization, the designated block (S_j1) occupies

\[
 \boxed{(C_{j,k}-c_j,C_{j,k}].}
 \tag{2.4}
\]

Assume (j<k).  In the right factorization, the word immediately after
the leading separator in (1\overline T_k), together with the next
separator, is exactly \(\overline T_k1\).  It occupies

\[
 \boxed{(a_{k+1},a_{k+1}+\widehat c_k].}
 \tag{2.5}
\]

The strict inequality (j<k) is what supplies the trailing separator
from the next block (1\overline T_{k-1}).

### Theorem 2.2 (a ledger cell is a literal word overlap)

Let

\[
 C_t=\sum_{i<t}c_i,
 \qquad Y_t=a_t-C_t,
\]

and

\[
 E_j=(-C_{j+1},-C_j],
 \qquad O_k=(Y_{k+1},Y_k].
 \tag{2.6}
\]

Translation by

\[
 x\longmapsto x+C_j+C_{j,k}
 \tag{2.7}
\]

sends (E_j) to (2.4) and sends (O_k) to (2.5).  Consequently

\[
 \boxed{
 |E_j\cap O_k|
 =\bigl|\operatorname {coord}(S_j1)
       \cap\operatorname {coord}(\overline T_k1)\bigr|}
 \tag{2.8}
\]

inside the one literal word \(\mathcal W_{j,k}\).

#### Proof

For the even interval, (2.7) gives

\[
 (-C_j-c_j,-C_j]+C_j+C_{j,k}
 =(C_{j,k}-c_j,C_{j,k}].
\]

For the odd interval, its left endpoint becomes

\[
 a_{k+1}-C_{k+1}+C_j+C_{j,k}=a_{k+1},
\]

because (C_{k+1}=C_j+C_{j,k}).  Its right endpoint becomes

\[
 a_k-C_k+C_j+C_{j,k}=a_k+c_k.
\]

Equation (1.4) at phase (k) says

\[
 a_k+c_k=a_{k+1}+\widehat c_k,
\]

so the translated odd interval is exactly (2.5). \(\square\)

The intersection of two line intervals ends at the end of at least one
of them.  Hence its last symbol may be the appended separator (1) from
one or both blocks, but every earlier common symbol belongs to both
(S_j) and \(\overline T_k\).  Therefore:

### Corollary 2.3 (common carrier word)

If (L=|E_j\cap O_k|\ge1), there is a word (Z) of length at least

\[
 \boxed{|Z|\ge L-1}
 \tag{2.9}
\]

which occurs at the aligned coordinates both in (S_j) and in
\(\overline T_k\).  For the residual positive cell,

\[
 |Z|\ge {N\over4H}-1.
 \tag{2.10}
\]

This is the full unconditional literal consequence of the cell length.

There is no opposite nonempty-cell orientation.  If \(k<j\), then
monotonicity of the odd ledger gives

\[
 Y_{k+1}\ge Y_j=a_j-C_j>-C_j.
\]

Thus every point of \(O_k=(Y_{k+1},Y_k]\) lies strictly to the right of
\(-C_j\), whereas every point of
\(E_j=(-C_{j+1},-C_j]\) lies at or to its left.  Hence

\[
 \boxed{E_j\cap O_k=\varnothing\qquad(k<j).}
 \tag{2.11}
\]

All nonempty cells have \(j\le k\).  The literal overlap theorem is
needed only for \(j<k\); the diagonal is treated separately below.

## 3. Exact flank audit

Let (I) and (J) be the coordinate intervals of (S_j1) and
\(\overline T_k1), and let their intersection word be (Z_\ast).  There
are unique factorizations

\[
 S_j1=X_LZ_\ast X_R,
 \qquad
 \overline T_k1=Y_LZ_\ast Y_R,
 \tag{3.1}
\]

with

\[
 \boxed{
 \min\{|X_L|,|Y_L|\}=0,
 \qquad
 \min\{|X_R|,|Y_R|\}=0.}
 \tag{3.2}
\]

These are just the four possible relative orders of the two left and two
right endpoints: either interval may contain the other, or the two may
cross in either direction.

The interior-carrier assumptions say only

\[
 \varepsilon N<c_j,\widehat c_k\le N-U_r.
 \tag{3.3}
\]

Together with (|Z_\ast|\ge N/(4H)), they control the two total block
lengths and their intersection.  They give no positive lower bound on
the four individual flanks in (3.1); by (3.2), at least two of those
flanks are identically empty.  In particular, the cell itself is not an
additional independent strip.  Any four-strip theorem has to come from
the outer canonical restrictions in the intervening transitions, not
from four positive interval flanks.

## 3A. Retracted same-label maximal-overlap kernel

> **Retraction.**  The statements in this section are retained only to
> document the failed route and are not theorem claims.  The unfolded
> free-monoid word is not an injective physical-token history: canonical
> separator occurrences can be duplicated under iteration.  The proposed
> token-level invariant below is not part of the accepted PBBS chronology
> package.  Consequently formulas (3A.2)--(3A.10) are unsupported and are
> not used anywhere in the valid conclusions of this report.

The bridge obstruction applies to an arbitrary internal common word.
The cell, however, supplies the **maximal coordinate intersection** of
the two carrier intervals.  Its empty-flank alternatives force a much
stronger height conclusion once the actual symbol labels are transported.

The free-monoid word \(\mathcal W_{j,k}\) is not itself label-injective:
canonical separator labels can recur when successive transition words are
concatenated.  The token identification used below instead comes from the
physical skew product.

### Lemma 3A.0 (spatial labels of a chronological cell)

Fix one physical lift and let \(u_0\in\mathbb Z_N\) be its initial even
unmatched coordinate.  Then the even and odd unmatched coordinates at
phase \(i\) are

\[
 u_i=u_0-C_i,
 \qquad
 v_i=u_i+a_i=u_0+Y_i
 \pmod N.
 \tag{3A.0}
\]

The carrier-interior points of the directed arc \((u_{i+1},u_i]\) spell
\(S_i\); the appended endpoint in the history block gives the displayed
\(1\) in \(S_i1\).  Likewise the carrier-interior points of
\((v_{i+1},v_i]\), after the intervening complementation into the even
normalization, spell \(\overline T_i\).  Its appended history endpoint
is not asserted to be the actual bit \(1\) in \(D_{i+1}\).  After
discarding that one endpoint, an integer point of \(E_j\cap O_k\)
denotes the same physical coordinate label in the two carrier interiors.

#### Proof

The exact even skew product is

\[
 (u_i,D_i)\longmapsto(u_i-c_i,D_{i+1}),
\]

so induction gives \(u_i=u_0-C_i\).  The one-step displacement from the
even root is \(a_i\), giving \(v_i=u_i+a_i=u_0+Y_i\).  The odd two-step
deficit is \(\widehat c_i\), and
\(Y_{i+1}=Y_i-\widehat c_i\), so
\(v_{i+1}=v_i-\widehat c_i\).

For \(x\in E_i\), discard the appended right endpoint.  Its occurrence
in \(S_i\) has local offset \(x+C_{i+1}\) from \(u_{i+1}\), and hence
physical label

\[
 u_{i+1}+(x+C_{i+1})=u_0+x\pmod N.
\]

For \(x\in O_i\), again discard the appended history endpoint.  Its
occurrence in \(\overline T_i\) inside \(D_{i+1}\) has local offset
\(x-Y_{i+1}\) from \(v_{i+1}\), and hence label

\[
 v_{i+1}+(x-Y_{i+1})=u_0+x\pmod N.
\]

The ordinary carrier bits are complemented in passing from the odd root
to the displayed \(\overline T_i\) block.  No label-preserving claim is
made for the appended endpoint, or for the full unfolded word
\(\mathcal W_{j,k}\).

Finally, both ledger intervals use the same unwrapped origin \(u_0\).
Thus a common integer coordinate gives the same label modulo \(N\), in
the same directed order.  Each individual cell has length at most
\(\min(c_j,\widehat c_k)<N\) after the near-total deletion, so its labels
are pairwise distinct. \(\square\)

### Lemma 3A.1 (physical-site one-step height law)

For every physical site \(p\), let \(H_i(p)\) be its rooted path height
immediately before \(p\) in phase \(D_i\), with
\(H_i(u_i)=0\) at the omitted root.  Then

\[
 \boxed{|H_{i+1}(p)-H_i(p)|\le1\qquad\text{for every }p.}
 \tag{3A.1}
\]

#### Proof

Root the old phase as

\[
 0\,P_i1R_i0S_i.
\]

The new root is the displayed zero immediately before \(S_i\), and the
new rooted word is

\[
 0\,S_i1P_i0R_i.
\]

A direct block comparison gives height change zero on \(S_i\) and at the
old root, \(+1\) on \(P_i\) and at the old marked-maximum site, and
\(-1\) on \(R_i\) and at the new root.  These cases exhaust all physical
sites and prove (3A.1). \(\square\)

### Theorem 3A.2 (maximal-overlap flank dichotomy)

Let \(j<k\), put

\[
 \ell=k-j,qquad t=\ell+1,qquad
 L=|E_j\cap O_k|,
\]

and assume \(L\ge2\).  If \(h\) is the common orbit height, then

\[
 \boxed{
 \max\{\operatorname {ht}(S_j),\operatorname {ht}(T_k)\}
 \ge h-t.}
 \tag{3A.2}
\]

If neither carrier interval contains the other, then both heights are at
least \(h-t\).

#### Proof

By Lemma 3A.0 these are two occurrences of the same ordered physical
labels.  Delete the appended separator from the blocks \(S_j1\) and
\(\overline T_k1\), and call their coordinate intervals \(I,J\).  Their
intersection has length exactly \(L-1\ge1\): the right endpoint of
the shorter carrier interval is the single appended point removed from
the cell.  Choose any aligned physical site \(p\in I\cap J\).

The two occurrences of the common binary word have the same increments.
Consequently the difference

\[
 \Delta=(\hbox{absolute height in }\overline T_k)
        -(\hbox{absolute height in }S_j)
 \tag{3A.3}
\]

is constant throughout \(I\cap J\).  Iterating Lemma 3A.1 through the
\(t\) phases gives

\[
 |\Delta|=|H_{k+1}(p)-H_j(p)|\le t.
\]

There are four interval orders.

* If \(I\subseteq J\), the overlap contains both endpoints of \(S_j\),
  where its height is zero.  At either aligned point the
  \(\overline T_k\) occurrence has absolute height at most \(t\).
  Since \(\overline T_k\) starts at height \(h\), it descends by at least
  \(h-t\); hence \(\operatorname {ht}(T_k)\ge h-t\).
* If \(J\subseteq I\), the overlap contains an endpoint of
  \(\overline T_k\), at absolute height \(h\).  The aligned point of
  \(S_j\) has height at least \(h-t\).
* In either crossing order, one endpoint of the overlap is an endpoint of
  \(S_j\) and the other is an endpoint of \(\overline T_k\).  Applying
  the preceding two endpoint arguments separately shows that both carrier
  heights are at least \(h-t\).

This proves the theorem. \(\square\)

Let

\[
 \mathcal E_a(z)=C_a(z)-C_{a-1}(z),
 \qquad C_{-1}=0,
 \tag{3A.4}
\]

be the exact-height Dyck series.  Deleting \(S_j\) injects a root into a
height-\(h\) Dyck prefix and the recorded suffix.  Likewise, in
\(D_{k+1}\), deleting the balanced negative excursion
\(\overline T_k\) immediately after the canonical first maximum leaves a
height-\(h\) Dyck word; reinsertion is unique.  Rephasing by
\(\tau^{\ell+1}\) is bijective.  Therefore Theorem 3A.2 gives, with
\(t=\ell+1\),

\[
 \boxed{
 R_{r,h}^{(\ell)}
 \le2[z^r]\mathcal E_h(z)
       \bigl(C_h(z)-C_{h-t-1}(z)\bigr),}
 \tag{3A.5}
\]

where \(C_a=0\) for \(a<0\).

For \(h>2t\), expand the second factor as the \(t+1\) exact heights
\(h-t,\ldots,h\).  Since

\[
 \mathcal E_a(x^2)=A_a(x)G_a(x),
\]

each summand is a convolution of four endpoint kernels of widths
comparable to \(h\).  The audited endpoint masses and pointwise bounds
give

\[
 \boxed{
 R_{r,h}^{(\ell)}
 \le Ct,4^rh^{-6}\exp(-cr/h^2).}
 \tag{3A.6}
\]

For \(h\le2t\), the bounded-height estimate gives

\[
 \sum_{h\le2t}R_{r,h}^{(\ell)}
 \le C B_r\exp(-cr/t^2).
 \tag{3A.7}
\]

Since

\[
 \sum_{h\ge1}h^{-6}e^{-cr/h^2}=O(r^{-5/2}),
\]

we obtain the uniform fixed-gap estimate

\[
 \boxed{
 R_r^{(\ell)}
 \le C_A\left(\frac{tB_r}{r}
       +B_r e^{-cr/t^2}\right).}
 \tag{3A.8}
\]

In particular, for every fixed \(\ell\),

\[
 \boxed{R_r^{(\ell)}=O_{A,\ell}(B_r/r)
 =o(B_r/\sqrt r).}
 \tag{3A.9}
\]

More generally, summing (3A.8) over all \(1\le\ell\le G\) gives

\[
 \boxed{
 \sum_{1\le\ell\le G}R_r^{(\ell)}
 \le C_A\frac{B_rG^2}{r}
   +C B_rG\exp(-cr/G^2).}
 \tag{3A.10}
\]

Thus every range \(G=o(r^{1/4})\) is collectively
\(o(B_r/\sqrt r)\).  Every residual cell has \(L\ge2\) for all large
\(r\); the restriction \(G=o(r^{1/4})\) comes only from summing the
enumerative bound, not from label transport.

This theorem decides the fixed-lag question: the bridge entropy of
Section 4 is only an internal-substring saturation.  The maximal overlap
flanks plus genuine outer chronology restore the fourth endpoint kernel.

## 4. The common word has bridge, not Dyck, entropy

### Theorem 4.1 (Gaussian bridge collision family)

Let (Z) be a balanced binary word of length (2n).  Write

\[
 \sigma_Z(t)=\#1(Z[1,t])-\#0(Z[1,t]),
\]

and put

\[
 p=-\min_{0\le t\le2n}\sigma_Z(t),
 \qquad
 q=\max_{0\le t\le2n}\sigma_Z(t).
 \tag{4.1}
\]

Then

\[
 \boxed{
 S_Z=1^pZ0^p,
 \qquad
 T_Z=1^q\overline Z0^q}
 \tag{4.2}
\]

are Dyck words.  Both have height (p+q), and (Z) is a literal
substring of both (S_Z) and \(\overline T_Z\).

Moreover, there are absolute constants (C_0,c_0>0) such that at least

\[
 c_0\binom{2n}{n}
 \tag{4.3}
\]

balanced words (Z) satisfy

\[
 p,q\le C_0\sqrt n.
 \tag{4.4}
\]

Thus there are

\[
 \boxed{\Theta(4^n/\sqrt n)}
 \tag{4.5}
\]

marked common words of length (2n) whose two Dyck completions have
semilengths (n+O(\sqrt n)) and heights (O(\sqrt n)).

#### Proof

Starting (Z) at height (p) makes all its partial heights
nonnegative; it ends again at height (p), and the final (p) zeroes
return to zero.  Hence (S_Z) is Dyck.  The prefix sums of
\(\overline Z\) are (-\sigma_Z(t)).  Starting it at height (q) gives
the same proof for (T_Z).  Their maximum height is (p+q).

For the count, reflection at the first visit to height (M) maps a
balanced bridge which reaches (M) injectively to a walk ending at
(2M).  Therefore

\[
 \#\{Z:\max\sigma_Z\ge M\}
 \le\binom{2n}{n+M}.
 \tag{4.6}
\]

The analogous bound holds for (-\min\sigma_Z\).  The elementary product
ratio gives

\[
 {\binom{2n}{n+M}\over\binom{2n}{n}}
 \le \exp(-cM^2/n)
 \tag{4.7}
\]

for an absolute (c>0).  Taking (M=C_0\sqrt n) with (C_0)
sufficiently large and applying the union bound leaves a fixed positive
fraction of all balanced bridges.  Finally

\[
 \binom{2n}{n}=\Theta(4^n/\sqrt n),
\]

which proves (4.3)--(4.5). \(\square\)

Choose any fixed

\[
 \alpha\in(\varepsilon,1-2\varepsilon)
\]

and take (n=\lfloor\alpha r\rfloor).  Since (U_r=o(N)), the two
literal carrier lengths in (4.2) obey, for all large (r),

\[
 \varepsilon N<|S_Z|+1,|T_Z|+1<N-U_r,
 \tag{4.8}
\]

after shrinking the fixed interval for \(\alpha\), if necessary.  Their
common word has length

\[
 2n=\alpha N+O(1),
 \tag{4.9}
\]

which is much stronger than the residual threshold (N/(4H)).

The point is enumerative.  An independent Dyck excursion of semilength
(n) has only

\[
 \operatorname {Cat}_n=\Theta(4^n/n^{3/2})
\]

possibilities, whereas the synchronized common bridge has

\[
 \Theta(4^n/n^{1/2})
 =\Theta(n\operatorname {Cat}_n)
 \tag{4.10}
\]

possibilities.  The factor (n) in (4.10) is the diagonal
Green/renewal mode.  Treating the common cell as one more independent
Dyck strip loses exactly this mode and is not a valid coefficient bound.

Theorem 4.1 is a literal Dyck-word obstruction, not a scalar
pseudoprofile.  It is deliberately not claimed that every pair
((S_Z,T_Z)) occurs at a prescribed lag in one PBBS orbit.  Its exact
logical role is to show that the genuine consequence (2.9), even together
with the two Dyck conditions, does not imply an additional strip.  The
simultaneous outer orbit equations are the only remaining possible source
of a gain.

## 5. Why fixed lag has not yet supplied the missing factor

Fix a nonadjacent lag

\[
 \ell=k-j\ge1.
\]

The outer words in (2.2) retain all \(\ell+1\) local transitions.  But
equation (2.2) is obtained by iterating the local identities (1.2); it is
not an independent constraint which can be multiplied by them.  Once the
intervening local factorizations are retained, the equality of the two
outer words is tautological.  The only new marked object extracted by the
cell is the synchronized common bridge (Z).

A successful fixed-lag four-strip theorem would therefore have to prove
one of the following genuinely stronger assertions.

1.  The actual \(\tau\)-chronology restricts the common bridges to a
    sublanguage with critical mass (o(1)) relative to all bridges.

2.  The bridge can be removed or contracted while the two outer
    canonical first-maximum factorizations remain reconstructible, with
    only (o(\sqrt r)) synchronized renewal states.

3.  Edge-disjointness bounds the bridge-rich strata even though their
    start language has critical entropy.

None of these follows from the cell length, the interior bounds, or the
free-monoid identity proved above.  In particular, no injection into five
independent Catalan factors has been established.

Negative lags require no carrier estimate: they are identically absent
by (2.11).

## 6. Bounded winding forces a linear rare--rare cell

The cell furnished in the source reduction is in fact much longer than
the stated \(N/(4H)\) threshold.

### Theorem 6.1 (linear-cell strengthening)

Fix \(0<\varepsilon<1/16\) and an integer \(K\ge2\), and put

\[
 T=\lfloor\varepsilon N\rfloor.
\]

Let one positive-winding return have \(1\le w<K\).  Suppose its two
small-carrier ledger masses satisfy

\[
 L_E<\frac{wN}{4},\qquad L_O<\frac{wN}{4},
 \tag{6.1}
\]

with \(L_E,L_O\) as in Theorem 4.1 of the source report.  Then it has a
genuine cell \(E_j\cap O_k\) such that

\[
 c_j>T,\qquad \widehat c_k>T,
 \qquad
 \boxed{|E_j\cap O_k|>\frac{\varepsilon N}{4K}.}
 \tag{6.2}
\]

The cell may be selected after the near-total-carrier deletion, so its
two carriers also obey

\[
 c_j,\widehat c_k\le N-U_r.
 \tag{6.3}
\]

#### Proof

The common chronological range has length \(wN\).  The union of the
cells for which at least one carrier is small has measure at most
\(L_E+L_O<wN/2\).  Therefore the rare--rare cells have total length
strictly greater than \(wN/2\).

Let \(r_E\) and \(r_O\) be the numbers of rare even and odd indices.
The two exact ledgers give

\[
 \sum_{i<s}c_i=a_s+wN<KN,
 \qquad
 \sum_{i<s}\widehat c_i=a_0+wN<KN.
\]

Every rare summand is greater than \(\varepsilon N\), whence

\[
 r_E<\frac K\varepsilon,qquad r_O<\frac K\varepsilon.
 \tag{6.4}
\]

The nonempty intersections of two ordered interval partitions trace a
monotone path in the product grid.  Restricting to \(r_E\) selected rows
and \(r_O\) selected columns leaves at most \(r_E+r_O-1<2K/\varepsilon\)
rare--rare cells.  One therefore has length greater than

\[
 \frac{wN/2}{2K/\varepsilon}
 =\frac{\varepsilon wN}{4K}
 \ge\frac{\varepsilon N}{4K}.
\]

The near-total deletion removes whole returns before the cell is selected;
reselecting a cell in every surviving return preserves distinctness on
both carrier sides. \(\square\)

Thus throughout the remaining bounded-winding residual one may replace
the mesoscopic threshold by

\[
 \boxed{|E_j\cap O_k|\ge\gamma N,
 \qquad \gamma:=\frac{\varepsilon}{4K}.}
 \tag{6.5}
\]

After translating \(j\) to zero and writing \(\ell=k-j\), there is also
an exact scalar normal form.  Put

\[
 x_\ell=a_\ell-\sum_{i=1}^{\ell-1}c_i.
 \tag{6.6}
\]

Translation by \(C_j+c_j\) gives

\[
 \boxed{
 |E_j\cap O_k|
 =\left|(0,c_0]\cap(x_\ell-\widehat c_\ell,x_\ell]\right|.}
 \tag{6.7}
\]

Indeed the right endpoint of the translated odd interval is \(x_\ell\),
and its left endpoint is \(x_\ell-\widehat c_\ell\) by
\(a_{\ell+1}=a_\ell+c_\ell-\widehat c_\ell\).  Since both widths exceed
\(\gamma N\), condition (6.5) is equivalent to

\[
 x_\ell\ge\gamma N,
 \qquad
 c_0+\widehat c_\ell-x_\ell\ge\gamma N.
 \tag{6.8}
\]

These are two genuine voltage inequalities, but they impose no
first-crossing condition on the binary bridge inside the overlap.

## 7. Two Catalan collision estimates

Write

\[
 e_{n,h}=\#\{D\in\mathcal D_n:\operatorname {ht}(D)=h\},
 \qquad C_n=\operatorname {Cat}_n.
\]

### Lemma 7.1 (uniform exact-height atom)

There is an absolute constant \(C\) such that

\[
 \boxed{
 \sup_h e_{n,h}\le C\frac{4^n}{(n+1)^2}
 \le C\frac{C_n}{\sqrt{n+1}}.}
 \tag{7.1}
\]

#### Proof

Use the continuants

\[
 F_0=F_1=1,qquad F_{a+1}=F_a-zF_{a-1},
 \qquad C_a(z)=\frac{F_a(z)}{F_{a+1}(z)}.
\]

The continuant determinant identity gives

\[
 \sum_{n\ge0}e_{n,h}z^n
 =C_h(z)-C_{h-1}(z)
 =\frac{z^h}{F_h(z)F_{h+1}(z)}.
 \tag{7.2}
\]

In step variable \(x\), the right side is \(A_h(x)G_h(x)\), where

\[
 A_h(x)=\frac{x^h}{F_h(x^2)},
 \qquad G_h(x)=\frac{x^h}{F_{h+1}(x^2)}.
\]

The audited finite-path endpoint estimate says that the normalized
coefficient sequences of \(A_h,G_h\) have \(\ell^1\)-mass
\(O((h+1)^{-1})\) and pointwise bound

\[
 O((h+1)^{-3})
 \exp\!\left(-\frac{ct}{(h+1)^2}\right).
\]

In their convolution, one elapsed time is at least half the total.
Consequently

\[
 4^{-n}e_{n,h}
 \le C(h+1)^{-4}
       \exp\!\left(-\frac{cn}{(h+1)^2}\right)
 \le C(n+1)^{-2},
\]

because \(y^2e^{-cy}\) is bounded for \(y=n/(h+1)^2\).  Stirling's
estimate \(C_n\asymp4^n(n+1)^{-3/2}\) proves (7.1). \(\square\)

### Lemma 7.2 (fixed height-collision convolution)

For every fixed integer \(q\ge0\),

\[
 \boxed{
 \sum_{u+v=r}\#\{(U,V)\in\mathcal D_u\times\mathcal D_v:
 |\operatorname {ht}(U)-\operatorname {ht}(V)|\le q\}
 =O_q(C_r/r^{3/4}).}
 \tag{7.3}
\]

#### Proof

When \(u\le v\), equality of the two heights up to \(q\), with
\(t=(uv)^{1/4}\), implies either

\[
 \operatorname {ht}(U)\ge t-q
 \quad\hbox{or}\quad
 \operatorname {ht}(V)\le t+q.
\]

The audited upper- and lower-height tails therefore give, after absorbing
bounded ranks into the constant,

\[
 \#\{(U,V):|\operatorname {ht}(U)-\operatorname {ht}(V)|\le q\}
 \le C_qC_uC_v
       \exp\!\left(-c_q\sqrt{v/u}\right).
 \tag{7.4}
\]

Put \(\eta=r^{-1/4}\).  If \(\min(u,v)\ge\eta r\), apply (7.1) to one
factor and Stirling to the central Catalan convolution.  This gives

\[
 O_q\!\left(\frac{C_r}{\eta r}\right)
 =O_q(C_r/r^{3/4}).
\]

If, say, \(u<\eta r\), then

\[
 \frac{C_uC_{r-u}}{C_r}\le C(u+1)^{-3/2}.
\]

Equation (7.4) and integral comparison give

\[
 C_r\sum_{u<\eta r}(u+1)^{-3/2}
 e^{-c\sqrt{r/(u+1)}}
 \le C C_rr^{-1/2}e^{-c'/\sqrt\eta},
\]

which is smaller than the asserted bound.  The case \(v<\eta r\) is
symmetric. \(\square\)

## 8. Exact elimination of lags zero and one

### Theorem 8.1 (diagonal cells vanish)

The number of genuine roots supporting a nonempty diagonal cell is

\[
 \boxed{O(C_r/r^{3/4})=o(C_r/\sqrt r).}
 \tag{8.1}
\]

#### Proof

Translation by \(C_j\) gives

\[
 E_j=(-c_j,0],\qquad
 O_j=(a_{j+1}-c_j,a_j],
\]

and therefore

\[
 |E_j\cap O_j|=(c_j-a_{j+1})_+.
 \tag{8.2}
\]

Factor \(D_j=P1R0S\), and put \(U=P1R0\), \(V=S\).  Then \(U,V\)
are Dyck words, their semilengths sum to \(r\), and

\[
 \operatorname {ht}(U)=\operatorname {ht}(D_j)=h,
 \qquad \operatorname {ht}(V)\le h,
 \qquad c_j=|V|+1.
\]

If \(\operatorname {ht}(V)<h\), then in
\(\tau D_j=V1P0R\) the first visit to height \(h\) occurs only after
all of \(V\) has been read.  Hence

\[
 a_{j+1}=\delta(\tau D_j)\ge|V|+1=c_j,
\]

so the diagonal cell is empty.  A nonempty cell therefore forces
\(\operatorname {ht}(U)=\operatorname {ht}(V)\).  The map
\(D_j\mapsto(U,V)\) is injective, and (8.1) follows from Lemma 7.2 with
\(q=0\). \(\square\)

### Theorem 8.2 (adjacent rare carriers vanish)

Fix \(\varepsilon>0\), and retain the source cutoff

\[
 U_r=\left\lfloor\frac r{\kappa_0(\log r)^2}\right\rfloor.
\]

Then

\[
 \boxed{
 \#\{D\in\mathcal D_r:
 \varepsilon N<d(D),d(\phi\tau D),\ d(D)\le N-U_r\}
 =O_\varepsilon\!\left(
   \frac{C_r}{r^{3/4}}+
   \frac{C_r(\log r)^4}{r}\right).}
 \tag{8.3}
\]

In particular the lag-one part of \(P_{\rm cell}\) is
\(o_\varepsilon(C_r/\sqrt r)\).  The upper cutoff on
\(d(\phi\tau D)\) is not needed for this estimate.

#### Proof

Write the canonical predecessor factorization as

\[
 D=A1B0V,
 \qquad W:=\tau D=V1A0B.
 \tag{8.4}
\]

Thus \(V\) is a distinguished initial Dyck prefix of \(W\), and

\[
 d(D)=|V|+1.
\]

If \(v=|V|/2\), the carrier hypotheses imply, for all large \(r\),

\[
 v\ge\alpha r,qquad r-v\ge L,
 \qquad \alpha:=\varepsilon/3,quad L:=\lceil U_r/2\rceil.
 \tag{8.5}
\]

Canonically factor

\[
 W=P1R0S,
 \qquad h=\operatorname {ht}(W).
\]

If \(\operatorname {ht}(S)=h\), deleting \(S\) injects \(W\) into two
Dyck paths of equal height.  Lemma 7.2 contributes
\(O(C_r/r^{3/4})\).  Hence assume \(\operatorname {ht}(S)<h\), so the
first height-\(h\) primitive component is uniquely tallest.

Let \(P^-\) be the shortest prefix of \(P\) which reaches \(h-1\), and
write

\[
 P=P^-P^+,
 \qquad M=\overline {P^+}.
 \tag{8.6}
\]

Then \(M\) is Dyck.  The exact one-step word is

\[
 \phi W=\overline R,1\,\overline S,0\,
         \overline {P^-}\,\overline {P^+}.
\]

Because \(\operatorname {ht}(S)<h\), the path stays positive through
\(\overline S\); minimality of \(P^-\) says that
\(\overline {P^-}\) first reaches zero at its end.  Thus the terminal
canonical suffix of \(\phi W\) is exactly \(M\), and

\[
 d(\phi W)=|M|+1.
 \tag{8.7}
\]

Writing \(m=|M|/2\), the second rare-carrier hypothesis gives
\(m\ge\alpha r\).

Locate the marked first maximum of \(W\) relative to the inherited prefix
\(V\).

**Case I: the marked maximum lies inside \(V\).**  Write \(W=VZ\),
where \(Z\) is Dyck and \(z=|Z|/2=r-v\ge L\).  The anti-Dyck excursion
\(P^+=\overline M\) lies inside \(V\).  Deleting it produces a Dyck word
\(V^*\) of height \(h\).  The map

\[
 D\longmapsto(M,V^*,Z)
 \tag{8.8}
\]

is injective: in \(V^*\), reinsert \(\overline M\) immediately before
its canonical first height-\(h\) step, append \(Z\), and apply
\(\tau^{-1}\).

Put \(q=|V^*|/2\) and \(\eta=\kappa(\log r)^{-2}\), where \(\kappa>0\)
will be chosen small.  For \(q\ge\eta r\), Stirling and summation first
over the two macroscopic variables give

\[
 \sum C_mC_qC_z
 \le C_\varepsilon\eta^{-3/2}
       \frac{C_r}{\sqrt{rL}}.
 \tag{8.9}
\]

For \(q<\eta r\), one also has
\(\operatorname {ht}(M)\le\operatorname {ht}(V^*)\).  The height-pair
estimate (7.4), followed by the remaining Catalan convolution, gives

\[
 C_\varepsilon C_rr^{-1/2}e^{-c'/\sqrt\eta}.
 \tag{8.10}
\]

**Case II: the marked maximum lies after \(V\).**  If \(V\) already
reaches height \(h-1\), then \(W=VZ\) has

\[
 \operatorname {ht}(V)=h-1,qquad
 \operatorname {ht}(Z)=h.
\]

Lemma 7.2 with \(q=1\) gives \(O(C_r/r^{3/4})\).

Otherwise \(\operatorname {ht}(V)\le h-2\) and \(P^-=VX\).  Deleting
\(\overline M\) gives

\[
 Z=X1R0S\in\mathcal D,qquad \operatorname {ht}(Z)=h,
\]

and

\[
 D\longmapsto(V,M,Z)
 \tag{8.11}
\]

is injective, with \(v,m\ge\alpha r\) and
\(\operatorname {ht}(V)\le\operatorname {ht}(Z)-2\).  If
\(z=|Z|/2\ge\eta r\), the three-macroscopic Catalan convolution is

\[
 O_\varepsilon(\eta^{-3/2}C_r/r).
 \tag{8.12}
\]

If \(z<\eta r\), apply (7.4) to \((Z,V)\) and then convolve over \(M\):

\[
 O_\varepsilon(C_rr^{-1/2}e^{-c'/\sqrt\eta}).
 \tag{8.13}
\]

The restricted convolution estimates (8.9) and (8.12) follow directly
from

\[
 C_a\asymp\frac{4^a}{(a+1)^{3/2}}
\]

and the convergent tail
\(\sum_{z\ge L}(z+1)^{-3/2}=O(L^{-1/2})\).
Choose \(\kappa\) sufficiently small that the exponential terms are
\(O(C_r/r^2)\).  Since \(L\asymp r/(\log r)^2\), (8.9) is
\(O_\varepsilon(C_r(\log r)^4/r)\), while (8.12) is smaller.  Combining
the cases proves (8.3). \(\square\)

Together with (2.11), Theorems 8.1--8.2 remove every negative lag and
the two near-adjacent lags \(0,1\) from the strengthened residual.

## 9. Conditioning on the shared word and the two-sided matching audit

Fix \(\ell\ge2\).  For a chosen lag-\(\ell\) cell, let \(Z\) be its
maximal literal overlap word from Section 2.  Define a bipartite graph
whose left vertices are the selected even roots \(D_j\), whose right
vertices are the selected odd roots \(\phi D_k\), and whose edge colour
is \(\ell=k-j\).

### Proposition 9.1 (fixed-lag matching gives no extra integrality)

For fixed \(\ell\), the right endpoint is the deterministic bijective
image

\[
 g_\ell(D)=\phi\tau^\ell D.
 \tag{9.1}
\]

Hence the fixed-colour graph is already a subgraph of a permutation
matching.  If \(L_Z\) and \(R_Z\) denote the numbers of compatible left
and right endpoints carrying the conditioned word \(Z\), then every
actual fixed-lag family satisfies only

\[
 \boxed{
 |\mathcal M_\ell|
 \le\sum_Z\min\{L_Z,R_Z\}
 \le\sqrt{\Bigl(\sum_ZL_Z\Bigr)
              \Bigl(\sum_ZR_Z\Bigr)}.}
 \tag{9.2}
\]

No total-unimodularity or fractional-matching loss remains to be saved:
the missing estimate must be a bound on which permutation edges are
genuinely compatible with the intervening canonical history.

#### Proof

Both \(\phi\) and \(\tau\) are permutations of \(\mathcal D_r\), so
\(g_\ell\) is a bijection.  Distinct left roots therefore already have
distinct right images.  Partition the actual edges by their conditioned
word and use the two endpoint capacities; Cauchy--Schwarz gives the last
inequality. \(\square\)

The bridge obstruction survives this operation at the local carrier
level.

### Proposition 9.2 (a literal two-sided carrier matching at bridge scale)

For fixed \(n\), take the balanced bridges in Theorem 4.1 satisfying
\(p,q\le C_0\sqrt n\), and join

\[
 S_Z=1^pZ0^p
 \quad\hbox{to}\quad
 T_Z=1^q\overline Z0^q.
\]

These edges form a matching of size

\[
 \boxed{\Theta(4^n/\sqrt n)}
 \tag{9.3}
\]

between two families of genuine Dyck carrier words, and every edge has
the literal shared bridge \(Z\).

#### Proof

Theorem 4.1 supplies the count and the Dyck property.  The map
\(Z\mapsto S_Z\) is injective: from its length and the fixed value of
\(n\), recover \(p=(|S_Z|-2n)/2\) and then extract the middle \(2n\)
symbols.  The same argument applies to \(Z\mapsto T_Z\).  Thus no two
edges share an endpoint. \(\square\)

This proves that two-sided matching does not remove the renewal factor
from the local literal language.  It does **not** prove that the matched
pair \((S_Z,T_Z)\) occurs at lag \(\ell\) in one \(\tau\)-orbit.

The marginal root cut is also genuinely critical.

### Proposition 9.3 (critical population of genuine rare roots)

For every fixed \(0<\varepsilon<1/3\), the number of genuine roots with

\[
 \varepsilon N<d(D)\le N-U_r
\]

is \(\Omega_\varepsilon(C_r/\sqrt r)\).

#### Proof

For \(v\in[r/3,r/2]\), put \(u=r-v\).  Choose a primitive
\(U\in\mathcal D_u\) and \(V\in\mathcal D_v\) so that

\[
 \operatorname {ht}(U)>\operatorname {ht}(V).
\]

For a sufficiently small fixed \(\kappa>0\), the audited height tails
give a fixed positive fraction of pairs with

\[
 \operatorname {ht}(U)\ge\kappa\sqrt r,
 \qquad
 \operatorname {ht}(V)<\kappa\sqrt r.
\]

Then \(D=UV\) has first primitive component uniquely tallest and

\[
 d(D)=2v+1\in[2r/3+1,r+1],
\]

which is interior-macroscopic and below \(N-U_r\) for all large \(r\).
There are \(\Theta(C_{u-1}C_v)\) such pairs for each \(v\).  Stirling and
summation over \(\Theta(r)\) values of \(v\) give

\[
 \sum_{v=r/3}^{r/2}C_{r-v-1}C_v
 =\Theta(4^r/r^2)
 =\Theta(C_r/\sqrt r).
\]

The factorization \(D=UV\) is unique, proving injectivity. \(\square\)

Thus neither endpoint rarity nor the bipartite matching cut is by itself
little-oh.  What is **not** constructed is a genuine fixed-lag family of
\(\Theta(C_r/\sqrt r)\) orbit edges satisfying (6.8).  The bridge family
is a real two-sided literal carrier matching, but at present it is only a
local-language saturation, not a PBBS or wreath counterexample.

### 9.4 The quantitative renewal obstruction

The standard one-crossing four-strip relaxation has normalized
coefficient \(O(4^rs^{-6})\) when all four widths are proportional to a
Gaussian height \(s\).  For a fixed boundary gap, one width is bounded
and only three widths are proportional to \(s\); restricting the three
wide elapsed times to fixed positive fractions of \(r\) gives the sharp
order

\[
 \Theta_\ell(4^rs^{-5}).
 \tag{9.4}
\]

Summing \(s\asymp\sqrt r\) gives

\[
 \Theta_\ell(4^r/r^2)
 =\Theta_\ell(C_r/\sqrt r),
 \tag{9.5}
\]

exactly the coefficient-one boundary.  For interior gaps the ideal
four-strip coefficient is \(O(4^rs^{-6})\) per gap, but there are
\(\Theta(s)\) gaps, again giving the critical order after summation.

The exact shared-carrier factor is

\[
 \mathcal R(z)=\frac1{1-\rho(z)},
 \qquad
 \rho(z)=zC_{s-u}(z)C_{u-1}(z).
 \tag{9.6}
\]

At \(z=1/4\),

\[
 \mathcal R(1/4)=\frac{(s-u+2)(u+1)}{s+2}.
 \tag{9.7}
\]

Moreover the continuant derivative gives exactly

\[
 \left.\frac{zC_n'(z)}{C_n(z)}\right|_{z=1/4}=\frac n3,
\]

and hence

\[
 \boxed{
 \left.\frac{z\mathcal R'(z)}{\mathcal R(z)}\right|_{z=1/4}
 =\frac{u(s-u+1)}3.}
 \tag{9.8}
\]

At an interior seam, (9.8) is \(\Theta(s^2)=\Theta(N)\).  Pointing one
of the \(\Theta(N)\) symbols in the strengthened cell multiplies the
critical renewal mass by \(\Theta(N)\); dividing by the number of marks
recovers the original \(\Theta(s)\) Green loss.  A canonical absorbing
first crossing would remove it, but an arbitrary marked crossing does
not.

Equivalently, the exact outer carrier equation has the overlap branch

\[
 \mathcal A_{0,\ell}R_0=R_\ell\mathcal C_{0,\ell},
 \qquad
 R_\ell=\mathcal A_{0,\ell}Z,\qquad
 R_0=Z\mathcal C_{0,\ell},
 \tag{9.9}
\]

with arbitrary shared word \(Z\).  The reserve \(U_r\) can lie entirely
inside \(Z\), so the upper cutoff does not force
\(\exp(-cU_r/\ell^2)\) passage through a narrow strip.

## 10. Exact proved/conditional boundary

The following are proved.

1.  Every genuine forward nonadjacent cell has the exact coordinate
    realization (2.8).
2.  A cell of length (L) gives a common literal carrier word of length
    at least (L-1), with no loss depending on the phase lag.
3.  The two carrier intervals have the exact flank form (3.1)--(3.2);
    the interior-macroscopic hypotheses do not make the flanks
    independently positive.
4.  The synchronized common-word language contains
    \(\Theta(4^n/\sqrt n)\) Gaussian-height bridges at length (2n).
    Hence the common word is a renewal/Green factor, not an automatic
    extra Dyck strip.
5.  Bounded winding upgrades the selected cell to
    \(|E_j\cap O_k|\ge\varepsilon N/(4K)=\Omega(r)\).
6.  All negative lags are impossible.  The diagonal and lag-one sectors
    contribute respectively
    \[
      O(C_r/r^{3/4})
      \quad\hbox{and}\quad
      O_\varepsilon\!\left(C_r/r^{3/4}
          +C_r(\log r)^4/r\right),
    \]
    both \(o(C_r/\sqrt r)\).
7.  Conditioning on the shared word and imposing matching on both
    carrier sides does not by itself gain a factor: fixed-lag endpoints
    are already related by a permutation, and the bridge language itself
    admits a matching of order \(4^n/\sqrt n\).

The exact unresolved sector has lag \(k-j\ge2\), a linear cell, and both
interior carrier bounds.  The
bridge obstruction is a real two-sided **local carrier matching**, while
the marginal rare-root sets have the genuine critical order
\(\Theta(C_r/\sqrt r)\).  It remains open whether this local bridge
entropy survives the genuine quotient-edge packing constraints.
Establishing either

\[
 \sum_Z |\mathcal M_{\ell,Z}|=o(C_r/\sqrt r)
\]

from the intervening canonical history, or a genuine critical lower
family, is the remaining two-time correlation theorem.  Until then
\(P_{\rm cell}\), the positive-winding gate, and coefficient one remain
open.
