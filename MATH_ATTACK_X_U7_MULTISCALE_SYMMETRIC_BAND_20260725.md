# Lane X: multiscale row-core recoding after the U7 audit

Date: 2026-07-25

## 0. Exact outcome

The cross-audit of
`MATH_ATTACK_U7_EQUAL_PACK_MULTIPIN_20260725.md` passes.  In particular,
the parity-dependent carrier lengths and counts, the unrestricted
\(W_r+r\) lower bound, and the immutable-incidence coefficient

\[
 \frac{173}{13824}
\]

are all exact.  The detailed audit is in
`MATH_ATTACK_X_U7_MULTIPIN_DISTINCT_SUPPORT_AUDIT_20260725.md`.

The exact uncovered-rank calculation from that audit leads to a stronger
construction than literal missing-target repair.  The construction below
does not retain the U7 atlas.  It recodes its principal positions onto one
lower antidiagonal and thereby covers lower and upper targets at once.

Put

\[
 Q_R=[0,R]^4,
 \qquad
 M_R=w(Q_R)
 =\frac{2R^3+6R^2+7R+3}{3}.
\tag{0.1}
\]

For every pair of integers \(1\le H\le R\), there is one literal word
covering every target in the complete symmetric rank band

\[
 2R-H,2R-H+1,\ldots,2R+H
\tag{0.2}
\]

whose exact displayed raw length is

\[
 \boxed{M_R+E_{\rm sym}(R,H),}
\tag{0.3}
\]

where

\[
 \boxed{
 E_{\rm sym}(R,H)
 =\sum_{r=1}^{H-1}(4r^2+2r)
  +\sum_{r=H}^{R}(4Hr-H^2+2H).}
\tag{0.4}
\]

Equivalently,

\[
 \boxed{
 E_{\rm sym}(R,H)
 =2HR(R+1)+(2H-H^2)(R+1)
  +\frac{H(H^2-3H-1)}3.}
\tag{0.5}
\]

Prepending one complement gives one fully initialized literal MTF
chronology of exact length

\[
 \boxed{M_R+E_{\rm sym}(R,H)+1,}
\tag{0.6}
\]

with the one-packet ledgers

\[
 \boxed{t-M_R=E_{\rm sym}(R,H),\qquad b-1=1.}
\tag{0.7}
\]

Since

\[
 E_{\rm sym}(R,H)=O(HR^2+H^2R+H^3),
\tag{0.8}
\]

this proves

\[
 \boxed{
 |\mathscr W_{R,H}|=(1+o(1))M_R
 \quad\text{for every }H=o(R).}
\tag{0.9}
\]

In particular it crosses the square-root shell scale:

\[
 H=\left\lfloor\sqrt R\,\omega(R)\right\rfloor,
 \qquad
 \omega(R)\longrightarrow\infty,
 \qquad
 \omega(R)=o(\sqrt R).
\tag{0.10}
\]

This is a genuine symmetric-band theorem, not an aggregate-support count.
Every target in (0.2) has a displayed literal contiguous-maximum witness,
all target ownership remains inside one exact complementary shell, and all
lengths in (0.3)--(0.7) are integral.

It is not yet the Boolean constant-one theorem.  In a four-block Boolean
SCD, compact positive-width parents have side scale

\[
 R=\Theta(\sqrt m),
\tag{0.11}
\]

whereas the Boolean tail cutoff is

\[
 H_B=\sqrt m\,\omega(m),
 \qquad \omega(m)\to\infty,
 \qquad H_B=o(m).
\tag{0.12}
\]

Thus (0.12) eventually contains the entire rank range of every compact
parent.  It requires fixed-relative or full local depth, not \(o(R)\).
Both explicit row/slice architectures below—including a word whose slices
cross the complementary shells directly—have a positive relative excess
at every fixed \(H/R>0\), and the equal-parent full fixed-slice version has
asymptotic factor three.  Therefore these modules do not compose to
constant one without a stronger cross-slice, cross-shell, or cross-parent
reuse of the width baseline.

This necessity can be made quantitative.  If \(H/R\to c\in(0,1]\), an
explicit forcing family shows that every \(M_R+o(M_R)\) band word must use
non-slice-pure witnesses for at least

\[
 \left(3c-\frac32c^2+\frac14c^3-o(1)\right)M_R
\]

distinct selected targets.  Thus positive-density cross-slice witness
incidences are compulsory at fixed relative depth; merely reducing seams or
deduplicating anchors cannot suffice.  A separate overlap mechanism is
still needed to fit those non-pure witnesses into one near-width word.

No computation, finite search, or nonliteral synchronization is used.

---

## 1. The audited U7 packet and shell identities

For \(r\ge1\), let

\[
 \mathcal A_r=[0,r]^2\times H_r,
 \qquad
 \mathcal B_r=H_r\times
 \bigl(\{1,\ldots,r\}\times\{0,\ldots,r-1\}\bigr),
\tag{1.1}
\]

where \(H_r=(h_0<\cdots<h_{2r})\) is the outer hook chain.  Their aligned
middle widths are

\[
 w(\mathcal A_r)=(r+1)^2,
 \qquad
 w(\mathcal B_r)=r^2,
\]

so put

\[
 W_r=(r+1)^2+r^2=2r^2+2r+1.
\tag{1.2}
\]

With

\[
 \tau_r=(R-r,0,R-r,0),
\tag{1.3}
\]

the equal four-cube has the exact disjoint complementary-shell partition

\[
 \boxed{
 Q_R
 =\{\tau_0\}
  \mathbin{\dot\cup}
  \bigdotcup_{r=1}^{R}
  \tau_r(\mathcal A_r\mathbin{\dot\cup}\mathcal B_r).}
\tag{1.4}
\]

Every packet middle layer translates to global rank \(2R\), and

\[
 \boxed{M_R=1+\sum_{r=1}^{R}W_r.}
\tag{1.5}
\]

Translation by \(\tau_r\) preserves coordinatewise joins.  Consequently
any word and interval witness constructed inside one local packet remains
a literal word and interval witness after translation.

The U7 arithmetic used to reach this point was independently checked:

\[
 |\mathcal C_r|
 =\begin{cases}
 r^2+r,&r\text{ odd},\\
 r^2+r-1,&r\text{ even},
 \end{cases}
\tag{1.6}
\]

\[
 P_r
 =\begin{cases}
 (r^2+r-2)/2,&r\text{ odd},\\
 (r^2+r-4)/2,&r\text{ even},
 \end{cases}
\tag{1.7}
\]

and

\[
 P_r^{\rm dist}
 =\begin{cases}
 (r^2+r-2)/2,&r\text{ odd},\\
 r^2/2-1,&r\text{ even}.
 \end{cases}
\tag{1.8}
\]

The unrestricted lower-target ledger is

\[
 2r^3+2r^2+r-1
 =(r-1)(2r^2+4r)+(5r-1),
\tag{1.9}
\]

with \(0<5r-1<2r^2+4r\), giving

\[
 g(\mathcal A_r\dot\cup\mathcal B_r)\ge W_r+r.
\tag{1.10}
\]

Finally, for \(k=\lfloor(r-1)/8\rfloor\), the immutable one-side
incidence calculation is

\[
 \Gamma_r=\frac{289}{1728}r^2+O(r),
 \qquad
 A_r^-=(k+1)r-\frac{k(k+1)}2
       =\frac{15}{128}r^2+O(r),
\]

and hence

\[
 \frac14\left(\frac{289}{1728}-\frac{15}{128}\right)
 =\frac{173}{13824}.
\tag{1.11}
\]

The side-incidence hypothesis in (1.11) remains essential.  The row-core
word below escapes it by replacing the physical atlas letters wholesale.

---

## 2. A clamped antidiagonal rectangle word

The local construction is a two-chain statement.

### Lemma 2.1 — exact symmetric diagonal-band word

Let

\[
 0\le y\le a,
 \qquad
 0\le q\le b,
\]

and fix integers \(L\) and \(H\ge0\).  Put

\[
 i_0=\max\{-2H,L-H-b\},
\tag{2.1}
\]

and, in increasing order of \(i\), emit

\[
 P_i=\bigl(\max\{i,0\},\max\{L-H-i,0\}\bigr),
 \qquad i_0\le i\le a.
\tag{2.2}
\]

Every occurrence in (2.2) lies in the rectangle: \(i\le a\) bounds the
first coordinate, while \(i\ge L-H-b\) bounds the second coordinate by
\(b\); both coordinates are clamped below by zero.

Then every legal target \((y,q)\in[0,a]\times[0,b]\) satisfying

\[
 y+q=L+d,
 \qquad -H\le d\le H,
\tag{2.3}
\]

is the coordinatewise maximum of one contiguous interval in (2.2).
Precisely, if

\[
 \alpha=y-H-d,
\tag{2.4}
\]

then

\[
 i_0\le\alpha\le y
\tag{2.5}
\]

and

\[
 \boxed{
 \bigvee_{i=\alpha}^{y}P_i=(y,q).}
\tag{2.6}
\]

#### Proof

Because \(y\ge0\) and \(d\le H\),

\[
 \alpha=y-H-d\ge-2H.
\]

Also \(q\le b\) and (2.3) give

\[
 \alpha=L-H-q\ge L-H-b.
\]

Thus \(\alpha\ge i_0\).  The inequality \(d\ge-H\) gives
\(\alpha\le y\), proving (2.5).

The first coordinate in (2.2) is nondecreasing, so its maximum on
\([\alpha,y]\) is \(y\).  The second coordinate is nonincreasing, so its
maximum is attained at \(\alpha\), where

\[
 \max\{L-H-\alpha,0\}
 =\max\{q,0\}=q.
\]

This proves (2.6). \(\square\)

The negative indices in (2.2) are not fictitious coordinates.  They give
legal boundary-anchor occurrences, possibly repeated in the completely
general rectangle statement, whose first coordinate is clamped to zero.
They remove the two cap repairs from a naive lower-diagonal path.  In the
packet applications below \(L\ge H\), and the displayed negative-index
hook coordinates are distinct.

---

## 3. One packet: exact symmetric-band recoding

Fix integers

\[
 r\ge H\ge1.
\tag{3.1}
\]

The ambient rank centre of both packet pieces is \(2r\).

### 3.1 The \(\mathcal A_r\) rows

Fix \(0\le x\le r\).  A target \((x,y;h_q)\) has deviation \(d\) when

\[
 y+q=(2r-x)+d.
\tag{3.2}
\]

Apply Lemma 2.1 with

\[
 a=r,
 \qquad b=2r,
 \qquad L=2r-x.
\]

Then

\[
 i_0=-J_x,
 \qquad
 J_x=\min\{2H,H+x\},
\tag{3.3}
\]

and the literal fixed-\(x\) row is

\[
 C^A_{x,i}
 =\bigl(x,\max\{i,0\};
        h_{\max\{2r-H-x-i,0\}}\bigr),
 \qquad -J_x\le i\le r.
\tag{3.4}
\]

Every letter lies in \(\mathcal A_r\).  Lemma 2.1 gives every legal
\(\mathcal A_r\)-target of deviation \(-H\le d\le H\) a witness inside
its own fixed-\(x\) row.

Equivalently, the negative-index portion of (3.4) consists of anchors

\[
 A^A_{x,j}=(x,0;h_{2r-H-x+j}),
 \qquad j=J_x,J_x-1,\ldots,1,
\tag{3.5}
\]

followed by the \(r+1\) clamped cores with \(i=0,\ldots,r\).

The exact anchor sum is

\[
 \begin{aligned}
 \sum_{x=0}^{r}J_x
 &=\sum_{x=0}^{H-1}(H+x)
   +\sum_{x=H}^{r}2H\\
 &=2Hr-\frac{H^2-3H}{2}.
 \end{aligned}
\tag{3.6}
\]

Therefore all \(\mathcal A_r\)-rows together have exact length

\[
 L_A(r,H)
 =(r+1)^2+2Hr-\frac{H^2-3H}{2}.
\tag{3.7}
\]

### 3.2 The \(\mathcal B_r\) rows

Write

\[
 a=u-1,
 \qquad 0\le a\le r-1,
 \qquad 0\le b\le r-1.
\]

A target \((h_t;a+1,b)\) has deviation \(d\) when

\[
 t+b=(2r-1-a)+d.
\tag{3.8}
\]

Apply Lemma 2.1 with rectangle heights \(r-1,2r\) and centre
\(L=2r-1-a\).  Put

\[
 J'_a=\min\{2H,H+a+1\}.
\tag{3.9}
\]

The literal fixed-\(a\) row is

\[
 C^B_{a,i}
 =\bigl(
 h_{\max\{2r-1-H-a-i,0\}};
 a+1,\max\{i,0\}
 \bigr),
 \qquad -J'_a\le i\le r-1.
\tag{3.10}
\]

Every letter lies in \(\mathcal B_r\), because its third coordinate is
\(a+1\in\{1,\ldots,r\}\) and its fourth coordinate is in
\(\{0,\ldots,r-1\}\).  Lemma 2.1 covers every legal
\(\mathcal B_r\)-target of deviation \(-H\le d\le H\) inside one row.

The exact anchor sum is

\[
 \begin{aligned}
 \sum_{a=0}^{r-1}J'_a
 &=\sum_{a=0}^{H-2}(H+a+1)
   +\sum_{a=H-1}^{r-1}2H\\
 &=2Hr-\frac{H^2-H}{2},
 \end{aligned}
\tag{3.11}
\]

where the first sum is empty for \(H=1\).  Thus all
\(\mathcal B_r\)-rows together have exact length

\[
 L_B(r,H)
 =r^2+2Hr-\frac{H^2-H}{2}.
\tag{3.12}
\]

### Theorem 3.1 — exact packet band

For every \(1\le H\le r\), concatenating the rows (3.4) and (3.10)
gives one literal word covering every target of
\(\mathcal A_r\dot\cup\mathcal B_r\) whose ambient rank lies in

\[
 2r-H,\ldots,2r+H.
\]

Its exact length is

\[
 \boxed{
 L_r^{\rm sym}(H)
 =W_r+4Hr-H^2+2H.}
\tag{3.13}
\]

#### Proof

Coverage follows row by row from Lemma 2.1.  The packet pieces are
disjoint, so no target ownership is duplicated.  Adding (3.7) and (3.12)
and using (1.2) gives

\[
 L_A+L_B
 =W_r+4Hr-H^2+2H.
\]

Every witness is internal to one displayed row.  For \(H\le r\), the
hook indices in (3.4) and (3.10) stay in \([0,2r]\).  Every emitted letter
is nonzero.  In an \(\mathcal A_r\)-row with \(x=0\), a zero short
coordinate requires \(i\le0\), while a zero hook index requires
\(i\ge2r-H\ge r>0\), so they cannot occur together.  If \(x>0\),
nonzeroness is immediate.  Every \(\mathcal B_r\)-letter has third
coordinate at least one. \(\square\)

The formula extends trivially to \(H=0\) by emitting every aligned middle
target once.  At positive \(H\), the word has moved its \(W_r\) core
positions down to the lower boundary and uses longer intervals to recover
the middle and upper targets.  This is the physical recoding required by
the retained-letter lower-side obstruction; it is not an append-only
repair of the U7 atlas.

---

## 4. Small shells: exact full affine slice words

Theorem 3.1 applies when \(r\ge H\).  If \(r<H\), cover the entire shell.

For a product of three chains of heights \(a,b,c\) with nonzero affine
minimum, fix the first coordinate and use the two-dimensional word

\[
 (b,0),(b-1,0),\ldots,(0,0),(0,1),\ldots,(0,c).
\tag{4.1}
\]

The interval from \((y,0)\) to \((0,z)\) has maximum \((y,z)\).  Hence
the concatenated fixed-coordinate slices cover the whole three-box in
exact length

\[
 (a+1)(b+c+1).
\tag{4.2}
\]

In shell \(r<H\), one has \(r<R\), so translation by \(\tau_r\) makes
the local minimum nonzero.  Apply (4.2) to

\[
 \mathcal A_r\cong[0,r]\times[0,r]\times[0,2r]
\]

and, after shifting \(u\) by one and permuting factors, to

\[
 \mathcal B_r\cong[0,r-1]\times[0,r-1]\times[0,2r].
\]

The exact displayed lengths are

\[
 (r+1)(3r+1)
 \qquad\text{and}\qquad
 3r^2.
\tag{4.3}
\]

Thus the entire translated packet shell has one literal word of exact
length

\[
 \boxed{F_r=6r^2+4r+1=W_r+(4r^2+2r).}
\tag{4.4}
\]

This covers every cap whose local deviation has absolute value larger than
\(r\), so no rank exception remains in a small shell.

---

## 5. Exact global aggregation

### Theorem 5.1 — complete symmetric band of the equal four-cube

Let \(R\ge1\) and \(1\le H\le R\).  There is one nonzero literal word in
\(Q_R\) which covers every target in every rank from \(2R-H\) through
\(2R+H\) and has exact length (0.3)--(0.5).

#### Proof

Emit \(\tau_0\) once.  For each shell \(1\le r<H\), emit the translated
full word (4.4).  For each \(H\le r\le R\), emit the translated symmetric
row-core word of Theorem 3.1.

Let a target have global rank \(2R+d\), where \(|d|\le H\).  By the
disjoint partition (1.4), it has a unique shell \(r\).  Translation by
\(\tau_r\) has rank \(2(R-r)\), so the target's local rank is exactly
\(2r+d\).  If \(r<H\), the full slice word covers it.  If \(r\ge H\),
Theorem 3.1 covers it.  Every witness stays in the unique target shell.

The exact width part of the length is

\[
 1+\sum_{r=1}^{R}W_r=M_R.
\]

The small-shell excess is \(4r^2+2r\), and the large-shell excess is
\(4Hr-H^2+2H\).  This proves (0.3)--(0.4).

For the closed form,

\[
 \sum_{r=1}^{H-1}(4r^2+2r)
 =\frac{H(H-1)(4H+1)}3,
\]

and

\[
 \sum_{r=H}^{R}(4Hr-H^2+2H)
 =2H\bigl(R(R+1)-H(H-1)\bigr)
  +(2H-H^2)(R-H+1).
\]

Adding and simplifying gives (0.5). \(\square\)

### Corollary 5.2 — one exact chronology

In the Boolean realization of the four chains, \(\tau_0=(R,0,R,0)\) is a
nonempty proper mask.  Put it first in the raw word and prepend its
nonempty complement.  The resulting state has two blocks, and every later
raw letter is an ordinary MTF update.  Old contiguous maxima remain old
contiguous OR witnesses.  This proves the exact initialized length (0.6)
and the root surplus \(b-1=1\).  In every large shell, the selected witness
for each packet-middle target ends at its unique nonnegative-index core
occurrence in (3.4) or (3.10).  In every small shell choose the right
endpoint of its fixed-slice middle witness; along one rectangle diagonal
these endpoints are distinct, and different slices are disjoint subwords.
Let \(\tau_0\) own the remaining middle target.  The shell partition makes
these \(M_R\) owners distinct.
Thus the \(M_R+E_{\rm sym}\) raw positions give exactly
\(t=M_R+E_{\rm sym}\) visited state occurrences after initialization,
proving the full one-packet ledgers (0.7).

There is no fractional ownership or labelled synchronization in this
argument.  The shell partition itself gives an integral owner for every
target, and the full raw word is one chronology.

### Corollary 5.3 — the super-root shell window

If \(H=o(R)\), then every term in (0.8) is \(o(R^3)\), while
\(M_R=(2/3+o(1))R^3\).  Therefore (0.9) holds.  Substitution of (0.10)
gives a concrete diverging window strictly larger than \(\sqrt R\).

For a fixed relative depth \(H/R\to c\in(0,1]\), however, (0.5) gives

\[
 \boxed{
 \frac{E_{\rm sym}(R,H)}{M_R}
 \longrightarrow
 3c-\frac32c^2+\frac12c^3>0.}
\tag{5.1}
\]

Thus the sublinear condition is the exact asymptotic ceiling of this
displayed row-core/shell ledger.  Equation (5.1) is not a lower bound for
all possible packet words.

### Proposition 5.4 — a direct cross-shell word

The shell concatenation is not responsible for the threshold in
Corollary 5.3.  There is a second word which never uses the shell
partition at all.  Fix \(R\ge1\) and \(0\le H\le R\).

Fix \((x,y)\in[0,R]^2\), put

\[
 s=x+y,
 \qquad
 L=2R-s,
\]

and define

\[
 \ell_s=\max\{-2H,R-s-H\},
 \qquad
 u_s=\min\{R,2R-s+H\}.
\tag{5.2}
\]

In increasing order of \(i\), emit the global letters

\[
 V_{x,y,i}
 =\bigl(x,y,\max\{i,0\},
              \max\{2R-s-H-i,0\}\bigr),
 \qquad \ell_s\le i\le u_s.
\tag{5.3}
\]

Concatenate these words over all fixed pairs \((x,y)\).  Every target of
\(Q_R\) in the band \(|d|\le H\) has a literal witness in its own fixed
\((x,y)\)-slice.  The exact displayed raw length, counting repeated
clamped occurrences, is

\[
 \boxed{M_R+E_{\rm dir}(R,H),}
\tag{5.4}
\]

where

\[
 \boxed{
 \begin{aligned}
 E_{\rm dir}(R,H)
 &=2HR^2-H^2R+4HR
   +\frac{H^3}{3}-H^2+\frac{5H}{3}\\
 &=E_{\rm sym}(R,H)+H^2.
 \end{aligned}}
\tag{5.5}
\]

#### Proof

For a target \((x,y,z,w)\) at deviation \(d\), one has

\[
 z+w=L+d.
\]

Lemma 2.1 applies to the \((z,w)\)-rectangle.  Its lower index is
\(\ell_s\).  Also every legal band target satisfies
\(z\le L+H\), so truncating the upper index to \(u_s\) removes no target
witness.  Thus (5.3) covers the entire band literally.

Let

\[
 m_s=\left|\{(x,y)\in[0,R]^2:x+y=s\}\right|
 =\begin{cases}
 s+1,&0\le s\le R,\\
 2R-s+1,&R\le s\le2R.
 \end{cases}
\]

For \(0\le H\le R\), (5.2) gives the exact slice length

\[
 u_s-\ell_s+1
 =\begin{cases}
 s+H+1,&0\le s\le R+H,\\
  2R-s+3H+1,&R+H<s\le2R.
 \end{cases}
\tag{5.6}
\]

At \(H=0\), summing these lengths with multiplicities \(m_s\) gives the
middle coefficient \(M_R\).  Relative to that baseline, the exact excess
is

\[
 \begin{aligned}
 E_{\rm dir}
 &=H\sum_{s=0}^{R}(s+1)
   +\sum_{j=1}^{H}(R-j+1)(2j+H)\\
 &\qquad
   +3H\sum_{j=1}^{R-H}j.
 \end{aligned}
\tag{5.7}
\]

Using the elementary sums of the first \(H\) integers and their squares
reduces (5.7) to the first line of (5.5).  Subtracting (0.5) gives exactly
\(H^2\).  Finally, no emitted global letter is zero.  Such a zero would
force \(x=y=0\), \(i\le0\), and \(i\ge2R-H\ge R\), a contradiction.
This proves the proposition. \(\square\)

### Corollary 5.5 — compressed and slice-optimal cross-shell ledger

In a slice with \(L<H\), the indices

\[
 L-H,L-H+1,\ldots,0
\]

all emit the same clamped moving pair \((0,0)\).  Replace that consecutive
run by one occurrence.  Every old witness remains a contiguous interval
with the same maximum.  Across all slices the exact number of removed
occurrences is

\[
 \begin{aligned}
 C_H
 &=\sum_{j=1}^{H}j(H-j+1)\\
 &=\frac{H(H+1)(H+2)}6.
 \end{aligned}
\tag{5.8}
\]

Consequently there is a compressed direct cross-shell word of exact length

\[
 \boxed{M_R+E_\times(R,H),}
\tag{5.9}
\]

where

\[
 \boxed{
 \begin{aligned}
 E_\times(R,H)
 &=E_{\rm dir}(R,H)-C_H\\
 &=2HR^2-H^2R+4HR
   +\frac{H^3}{6}-\frac{3H^2}{2}+\frac{4H}{3}.
 \end{aligned}}
\tag{5.10}
\]

Order the \((x,y)=(0,0)\) slice first and prepend the complement of its
first letter.  This gives a fully initialized MTF chronology of exact
length

\[
 M_R+E_\times(R,H)+1,
\]

with \(t-M_R=E_\times(R,H)\) and \(b-1=1\).  Middle targets in one slice
have distinct terminal moving coordinate, and different slices use
disjoint subwords, so the middle ownership is integral.

Moreover (5.9) is minimum in the following precisely slice-confined class:
the physical word is partitioned into disjoint subwords
\(W_{x,y}\), every letter of \(W_{x,y}\) has first two coordinates
\((x,y)\), and every selected witness for a target with those first two
coordinates lies wholly in \(W_{x,y}\).

#### Proof

Only the displayed consecutive \((0,0)\)-runs are collapsed, so coverage
is unchanged.  Such a run occurs when \(s=2R-H+j\), \(1\le j\le H\); it
saves \(j\) positions in each of the \(H-j+1\) slices with that value of
\(s\).  This proves (5.8), and subtraction from (5.5) proves (5.10).

For optimality, fix one moving \((z,w)\)-rectangle and put

\[
 q_- =\max\{0,L-H\},
 \qquad
 q_+=\min\{2R,L+H\}.
\]

All legal points on the diagonal \(z+w=q_-\) are band targets and form an
antichain.  Their selected witnesses have distinct right endpoints and
therefore require at least the size of that diagonal in physical positions.
If \(q_-\le R\), put \(K=\min\{R,q_+\}\).  The diagonal has \(q_-+1\)
points, and every additional axis target

\[
 (0,q),\ (q,0),
 \qquad q_-<q\le\min\{R,q_+\},
\]

forces its own literal occurrence: a witness with maximum first coordinate
zero contains only first-coordinate-zero letters, and its second-coordinate
maximum must occur in one of them, and symmetrically for the other axis.
These \(2(K-q_-)\) forced letters have moving-coordinate sum above
\(q_-\) and hence cannot occur in a witness for any target on the lower
diagonal.  They therefore add to the antichain position bound, giving
\(q_-+1+2(K-q_-)\), exactly the compressed path length.  If \(q_->R\),
there are no such axis targets; the lower diagonal has
\(2R-q_-+1\) points, again exactly the compressed path length.

In both cases the resulting lower bound is exactly the number of positions
in the compressed clamped-antidiagonal slice.  Summing over the disjoint
fixed \((x,y)\)-slice subwords proves slice-confined optimality. \(\square\)

For fixed \(H/R\to c\in(0,1]\), the compressed ledger has the exact limit

\[
 \boxed{
 \frac{E_\times(R,H)}{M_R}
 \longrightarrow
 3c-\frac32c^2+\frac14c^3>0.}
\tag{5.11}
\]

### Corollary 5.6 — positive-density cross-slice necessity

For every fixed \((x,y)\)-slice, take the lower-diagonal antichain and the
higher axis targets used in the proof of Corollary 5.5.  Let
\(\mathcal F_{R,H}\) be their union over all slices.  Then

\[
 \boxed{|\mathcal F_{R,H}|=M_R+E_\times(R,H).}
\tag{5.12}
\]

Let an arbitrary ambient word of length

\[
 n=M_R+D
\]

cover the whole band, and choose one witness for every target in
\(\mathcal F_{R,H}\).  Call a selected witness **slice-pure** if every
letter in it has the same first two coordinates as its target.  If \(X\)
selected witnesses are not slice-pure, then

\[
 \boxed{X\ge E_\times(R,H)-D.}
\tag{5.13}
\]

#### Proof

In each slice, the slice-pure witnesses retained from the lower diagonal
still have distinct right endpoints.  Every retained slice-pure higher-axis
witness still forces its literal moving-axis occurrence.  Such an
occurrence has moving rank above the lower diagonal and cannot lie in any
retained lower-diagonal witness.  The positions counted from pure witnesses
with different fixed first-coordinate pairs cannot coincide.  Removing the
\(X\) non-pure targets
therefore lowers the summed position bound from (5.12) by at most \(X\):

\[
 n\ge M_R+E_\times-X.
\]

Rearranging gives (5.13). \(\square\)

Consequently, if \(H/R\to c\in(0,1]\) and \(D=o(M_R)\), every
coefficient-one word must use non-slice-pure witnesses for at least

\[
 \boxed{
 \left(3c-\frac32c^2+\frac14c^3-o(1)\right)M_R}
\tag{5.14}
\]

members of the explicit forcing family.  This is not a length lower bound
for unrestricted words.  It is an exact chronology requirement: a
fixed-relative solution must use positive-density cross-slice witness
incidences.  It does not by itself force a positive density of distinct
portals or multiply reused physical positions.

The fixed global slices in (5.3) cut across the complementary-shell
partition inside one equal parent \(Q_R\), so Proposition 5.4 is a literal
cross-shell fusion, not a relabeling of independent shell epochs.  It does
not fuse unequal Boolean parents.  Even after the optimal within-slice
compression of Corollary 5.5, it still has

\[
 E_\times=\Theta(HR^2)
\]

when \(H=o(R)\), and a positive \(R^3\)-scale excess when \(H/R\) tends
to a positive constant.  Thus eliminating every shell seam and every
redundant clamped occurrence does not alter the sublinear-depth threshold.
The leading obstruction in this family is the density of boundary anchors.

---

## 6. Relation to the transposed U7 support

The earlier rankwise audit found that the original U7 atlas covers

\[
 f_r(d)=W_r-d(2r+1)
\tag{6.1}
\]

distinct shell targets at upper depth \(0\le d\le r\).  Combining its
target support with the short-coordinate transpose leaves exactly \(d^2\)
targets in the full shell layer.  Across the equal-cube shells, the exact
two-orientation deficit is

\[
 D_R^{(2)}(d)
 =d^2(R-d+1)+\frac{d(d^2-1)}6.
\tag{6.2}
\]

There is one physical correction to the first formulation of that
observation.  U7's displayed \(\mathcal B_r\)-blocks mix
\(\mathcal A_r\)- and \(\mathcal B_r\)-letters, so the affine swap
\((u-1,v)\leftrightarrow(v,u-1)\) is not a letterwise automorphism of the
mixed block.  The transposed target support is nevertheless realized
literally by the explicit word

\[
 G_{b,0}=(h_{2r-b-1};0,b),
 \qquad
 G_{b,j}=(h_{2r-b-1-j};j,b),
 \quad1\le j\le r.
\tag{6.3}
\]

Indeed, for a target \((h_t;u,b)\) in the transposed family, put

\[
 a=2r-b-1-t.
\]

Then \(0\le a<u\) and

\[
 \bigvee_{j=a}^{u}G_{b,j}=(h_t;u,b).
\tag{6.4}
\]

This repairs the literal-support statement but is no longer needed for
Theorem 5.1.  The row-core theorem is stronger: it covers the complete
lower and upper band in one recoded baseline instead of appending a second
orientation and then repairing (6.2).

The distinction is quantitative.  Literal singleton repair after the two
orientations reaches only \(H=o(R^{2/3})\).  Three-box corner words remove
that ceiling and reach \(H=o(R)\) on the upper side.  The clamped
antidiagonal word reaches the same \(H=o(R)\) scale on both sides and also
meets the retained-letter recoding requirement exactly.

---

## 7. Why this still does not compose to Boolean constant one

Within the equal-shell lane, the obstruction is now scale rather than
one-sided support.  Generic compact four-block parents are also anisotropic;
Theorem 5.1 itself is proved only for the equal cube.

In a balanced four-block SCD of the \(2m\)-cube, the chain heights in every
fixed compact positive-width sector are \(\Theta(\sqrt m)\).  Such compact
parents carry a positive fraction of the exact middle width.  If a
representative side scale is denoted by \(R\) (the four sides need not be
literally equal), then

\[
 R=\Theta(\sqrt m).
\tag{7.1}
\]

For the Boolean cutoff (0.12),

\[
 \frac{H_B}{R}\longrightarrow\infty.
\tag{7.2}
\]

Every compact four-chain parent has total rank radius \(O(R)\), so the
Boolean central band eventually contains that parent in its entirety.
Consequently Theorem 5.1, whose relative excess vanishes only for
\(H/R\to0\), cannot be inserted into the verified four-block aggregation
to prove \(\nu(k)\le(1+o(1))W(k)\).

Already on one equal parent, taking only the inner band \(H=R\) in
Corollary 5.6 shows that any \(M_R+o(M_R)\) realization must assign
non-slice-pure witnesses to at least

\[
 \left(\frac74-o(1)\right)M_R
\]

members of the explicit forcing family.  Thus a Boolean-scale use of this
lane would require positive-density coordinate-mixed witnesses—and then a
separate overlap mechanism to fit them at near width—before the remaining
outer packet caps are even considered.

The additive full-depth ledger makes the failure exact.  Cover a complete
\(\mathcal A_r\)-packet by fixed-coordinate affine slices in

\[
 (r+1)(3r+1)
\]

positions, and a complete \(\mathcal B_r\)-packet in \(3r^2\) positions.
For the nonzero-target problem on the unshifted cube \(Q_R\), omit the
unique global zero from the outer \(\mathcal A_R\)-slice word and retain
the terminal target
\(\tau_0\).  The exact displayed full-cube length is then

\[
 \begin{aligned}
 L_{\rm slice}(R)
 &=\sum_{r=1}^{R}(6r^2+4r+1)\\
 &=\boxed{2R^3+5R^2+4R}.
 \end{aligned}
\tag{7.3}
\]

Therefore

\[
 \boxed{
 \frac{L_{\rm slice}(R)}{M_R}\longrightarrow3.}
\tag{7.4}
\]

The factor three is exact for the fixed-slice architecture.  In an affine
two-chain rectangle of heights \(a,b\) whose minimum is a required target,
every point on each coordinate axis must occur as a physical letter: a
witness for an axis target cannot contain a letter positive in the other
coordinate, and the desired coordinate maximum must occur in the witness.
The two axes therefore force at least \(a+b+1\) positions.  Word (4.1)
attains that bound.  Summing independently over fixed slices gives (7.3).

This is an architecture-scoped no-go.  It rules out obtaining constant one
by iterating or regrouping independently concatenated row/slice modules at
the Boolean cutoff.  It does **not** rule out an unrestricted packet word:
the audited lower bound \(W_r+r\) is still compatible with PACK.

There is also an independent global scope restriction already proved in
`MATH_ATTACK_X3_PRODUCT_ROUTE_RESCUE_20260724.md`: for every fixed number
\(t\ge2\) of Boolean coordinate blocks, separately paying the resulting
\(t\)-chain product parents costs at least

\[
 (1+\epsilon_t)W(k)-o(W(k))
\]

for some \(\epsilon_t>0\).  Thus even a stronger equal-parent theorem could
enter the Boolean proof only through a genuinely cross-parent braid,
nonproduct packets, or a growing-dimensional decomposition.  The theorem
here supplies a new exact local chronology and a new cross-slice forcing
ledger; it does not invalidate that fixed-parent no-go.

Any continuation of this lane must therefore do at least one of the
following:

1. reuse a positive density of physical core positions across different
   complementary shells;
2. fuse different four-chain parents before their width baselines are
   paid; or
3. construct a full PACK braid whose intervals cross the fixed-coordinate
   slices and abandon their separate axis occurrences.

Those are exactly the density-scale reuse mechanisms not supplied by
Theorem 5.1 or by the direct fixed-slice word of Corollary 5.5.

---

## 8. Proved and unproved boundary

### Proved

1. The U7 carrier lengths, carrier counts, \(W_r+r\) lower bound, and
   \(173/13824\) immutable-incidence coefficient pass exact cross-audit.
2. Lemma 2.1 gives one clamped antidiagonal word for a complete symmetric
   band of a two-chain rectangle, including both boundary caps.
3. Every equal complementary packet has the exact symmetric-band word
   (3.13), with literal witnesses and integral ownership.
4. The complementary-shell aggregation covers every target in the complete
   global band \(|d|\le H\) with exact length (0.3)--(0.5).
5. One complement turns the construction into one fully initialized MTF
   chronology with exact ledgers (0.6)--(0.7).
6. The equal-cube symmetric band has coefficient one for every
   \(H=o(R)\), including every shell window (0.10).
7. Proposition 5.4 and Corollary 5.5 give a direct global cross-shell word
   and its exact slice-confined optimum; removing every shell seam and
   every duplicate clamp does not improve the sublinear-depth ceiling.
8. The equal-cube fixed-slice full-depth implementation has exact
   asymptotic factor three, so independently paying that architecture
   cannot be a coefficient-one local input.
9. Corollary 5.6 proves the exact non-slice-pure witness demand (5.13)--
   (5.14) for every arbitrary ambient near-width word at fixed relative
   depth.

### Not proved

1. No coefficient-one word is constructed for a fixed-relative or complete
   equal four-cube.
2. No cross-shell reuse which removes the \(\Theta(R^3)\) fixed-relative
   anchor excess is constructed.
3. No cross-parent fusion removes the separately paid compact-parent
   baselines.
4. The theorem does not imply MWB, labelled common-owner synchronization,
   PACK, or the sharp constant-one Boolean theorem.

The precise advance is therefore a complete local theorem up to every
sublinear shell depth, together with an exact scale diagnosis.  The old
one-sided support and lower-letter obstruction are both removed by dynamic
row-core recoding.  The remaining barrier is the full-depth compact-parent
baseline required by the actual Boolean cutoff.
