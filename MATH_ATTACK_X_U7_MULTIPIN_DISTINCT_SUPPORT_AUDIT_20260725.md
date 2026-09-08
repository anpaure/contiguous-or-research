# Lane X cross-audit: U7 multipins and distinct deeper support

Date: 2026-07-25

**Subsequent advance.**  The U7 cross-audit and the exact support formulas
in this report remain valid.  The later file
`MATH_ATTACK_X_U7_MULTISCALE_SYMMETRIC_BAND_20260725.md` supersedes this
report's one-sided chronology boundary: clamped antidiagonal row-core
recoding gives a complete literal symmetric band through every \(H=o(R)\).
The Boolean constant-one implication remains open because compact
four-block SCD parents have radius \(R=\Theta(\sqrt m)\), below the required
Boolean cutoff \(\sqrt m\,\omega(m)\).

## 0. Verdict

The exact claims in `MATH_ATTACK_U7_EQUAL_PACK_MULTIPIN_20260725.md` pass
cross-audit.  In particular:

* both parity-dependent carrier-word lengths are exact;
* the internal and distinct-owner carrier counts are exact;
* the half-upper atlas has length exactly \(W_r+2r\) and its displayed
  target count is a count of distinct literal targets;
* the unrestricted lower bound is exactly \(W_r+r\);
* the immutable-matching obstruction has exact leading coefficient

  \[
  \frac{173}{13824};
  \]

* the diagonal path forest and its selected source-gap restoration tax have
  the stated exact edge count.

The qualifications in U7 are necessary: the \(173/13824\) bound assumes
the single preassigned U5 side incidence is retained; the distinct-owner
carrier count is a certified witness-system count, not an optimum; and the
quadratic insertion tax restores only the selected source gaps.

Combining the audited half-upper atlas with the exact complementary-shell
peel and the macro-packet chronology from
`MATH_ATTACK_X_CROSS_SEAM_REPACKETIZATION_20260725.md` gives a new positive
result about **distinct**, rather than aggregate, deeper support.

Let

\[
 Q_R=[0,R]^4,
 \qquad
 M_R=w(Q_R).
\]

There is one literal word of length

\[
 \boxed{M_R+R(R+1)}
\tag{0.1}
\]

which covers the entire middle layer and, at every upper depth
\(0\le d\le R\), covers exactly the following certified number of distinct
rank-\((2R+d)\) targets:

\[
 \boxed{
 S_R(d)
 =(d+1)n^2+\frac{n(n-1)(2n-1)}3,
 \qquad n=R-d+1.}
\tag{0.2}
\]

The supports at different shells are disjoint by the literal shell
partition; no incidence multiplicity is counted in (0.2).  A single extra
initial complement makes (0.1) one fully initialized MTF chronology.  The
same word can be divided into genuine macro-packets, each owning at least
\(R^2\) middle targets, with total state surplus \(R(R+1)\) and only
\(O(R)\) total root surplus.

If \(d=o(R)\), then

\[
 \boxed{
S_R(d)=(1-o(1))
\left|Q_R\cap\{|x|=2R+d\}\right|.}
\tag{0.3}
\]

More strongly, let \(1\le H\le R\), put

\[
 A=\frac{H(H+1)}2,
 \qquad
 B=\frac{H(H+1)(2H+1)}6,
\]

and define

\[
 \boxed{
 \mathcal D_R(H)
 =(R+1)\bigl((R+1)A-B\bigr)
  +\frac{A^2-A}{6}.}
\tag{0.3a}
\]

The quantity \(\mathcal D_R(H)\) is the exact number of distinct targets
missing from the certified support in the complete upper band of depths
\(1,\ldots,H\).  Appending those targets literally gives one word covering
every target in ranks \(2R,\ldots,2R+H\), of exact length

\[
 \boxed{M_R+R(R+1)+\mathcal D_R(H).}
\tag{0.3b}
\]

Consequently the complete upper band has a literal \(M_R+o(M_R)\) cover
whenever

\[
 \boxed{H=o(\sqrt R).}
\tag{0.3c}
\]

This is a distinct-target repair theorem: every appended mask is an actual
member of the set-theoretic complement of the atlas support.

Thus one width-plus-\(O(R^2)\) chronology covers almost every target in
every simultaneously selected sublinear-depth upper rank.  More generally,
at depth \(d/R\to x\in[0,1]\), the exact limiting support fraction is

\[
 \boxed{
 \rho(x)=
 \frac{\frac23-x+\frac{x^3}{3}}
      {\frac23-x^2+\frac{x^3}{2}}.}
\tag{0.4}
\]

This does not prove PACK or the full constant-one theorem.  The lower half,
the missing upper caps, unequal product parents, and cross-parent Boolean
aggregation remain open.  The audited \(173/13824\) obstruction shows in
particular that those missing targets cannot be added while preserving the
old one-sided common-lift incidence system.

---

## 1. Exact U7 cross-audit

Throughout this section

\[
 W_r=(r+1)^2+r^2=2r^2+2r+1.
\]

### 1.1 Packet ranks and lower targets

The two packet rank polynomials are

\[
 P_r(z)^2P_{2r}(z),
 \qquad
 zP_{2r}(z)P_{r-1}(z)^2.
\]

Their aligned middle coefficients are \((r+1)^2\) and \(r^2\).  Their
numbers of nonzero targets below ambient rank \(2r\) are

\[
 L_A^-=r(r+1)^2-1,
 \qquad
 L_B^-=r^3,
\]

and hence

\[
 \boxed{L_r^-=2r^3+2r^2+r-1.}
\tag{1.1}
\]

The subtraction of one occurs only in \(\mathcal A_r\), whose local zero
is the ambient zero.  The rank-one translate defining \(\mathcal B_r\)
has no zero target to remove.

### 1.2 Snake and carrier lengths

The parity-corrected snake contains

\[
 m=
 \begin{cases}
 r^2+r-1,&r\text{ odd},\\
 r^2+r-2,&r\text{ even}
 \end{cases}
\tag{1.2}
\]

target occurrences.  For odd \(r\), the \(r-1\) nonfinal rows each gain
one repeated endpoint.  For even \(r\), the \(r/2-1\) nonfinal even rows
each gain two.  Every completed row segment has even length, so every row
starts at an odd list index.

The carrier word has one more position than the target list and therefore
has length

\[
 \boxed{
 \begin{cases}
 r^2+r,&r\text{ odd},\\
 r^2+r-1,&r\text{ even}.
 \end{cases}}
\tag{1.3}
\]

At target occurrence \(i\), the two unmodified carriers are its meets with
the preceding and following occurrences.  Coordinatewise monotonicity
inside rows, the repeated low turns, and the endpoint conventions give

\[
 D_{i-1}\vee D_i=T_i.
\]

Exactly one of the adjacent physical carriers is odd.  That carrier retains
the target's positive third coordinate; zeroing the third coordinate only
on the even carrier therefore preserves the join.  This verifies the
literal identity

\[
 C_{i-1}\vee C_i=T_i
\]

at row interiors, both types of row turn, inserted copies, and the two word
ends.

There are exactly

\[
 \boxed{
 P_r=
 \begin{cases}
 (r^2+r-2)/2,&r\text{ odd},\\
 (r^2+r-4)/2,&r\text{ even}
 \end{cases}}
\tag{1.4}
\]

internal even carrier occurrences.  After choosing only one witness for
each distinct owner, the certified two-sided count is

\[
 \boxed{
 P_r^{\rm dist}=
 \begin{cases}
 (r^2+r-2)/2,&r\text{ odd},\\
 r^2/2-1,&r\text{ even}.
 \end{cases}}
\tag{1.5}
\]

In the even case precisely \(r/2-1\) triple-copy seams are lost.  In the
odd case the three-carrier replacement at each double-copy seam preserves
both even boundary sites.  No optimality beyond this selected witness
system is asserted.

For every interior value \(1\le v\le r-2\), the even carrier loses the
positive third coordinate and also either hook height or fourth-coordinate
height.  Thus the number of certified genuinely multipin owners is exactly
at least

\[
 r(r-2).
\]

### 1.3 Half-upper atlas

For \(\mathcal A_r\), the certified target family is

\[
 \mathcal U_{A,r}
 =\{(x,y;h_q):2r-x-y\le q\le2r-x\}.
\tag{1.6}
\]

For fixed \((x,y)\), it has \(y+1\) choices of \(q\), so

\[
 \boxed{
 |\mathcal U_{A,r}|=\frac{(r+1)^2(r+2)}2.}
\tag{1.7}
\]

For \(\mathcal B_r\), the certified family is

\[
 \mathcal U_{B,r}
 =\{(h_t;u,v):2r-u-v\le t\le2r-u\},
\tag{1.8}
\]

with \(v+1\) choices of \(t\), and therefore

\[
 \boxed{
 |\mathcal U_{B,r}|=\frac{r^2(r+1)}2.}
\tag{1.9}
\]

The two packet families are disjoint.  Their block words have respectively
\((r+1)(r+2)\) and \(r(r+1)\) letters.  Their common boundary letter is
identified once, giving exact word length

\[
 \boxed{
 (r+1)(r+2)+r(r+1)-1=W_r+2r.}
\tag{1.10}
\]

Every displayed witness stays inside one verified block, so identifying the
common boundary does not remove an interior witness position.  Both target
families contain their entire aligned middle layers.

### 1.4 Unrestricted linear lower bound

Let a full packet word have length \(W_r+e\).  Selected middle witnesses
have distinct left endpoints and distinct right endpoints in the same
order.  Writing their spans as \(d_i\), one has

\[
 \sum_i d_i\le W_re.
\]

A lower target beginning at a selected middle left endpoint must end before
that middle witness, giving at most \(d_i\) such targets.  Each of the
remaining \(e\) starts supports a strict nonzero chain of length at most
\(2r-1\).  Hence

\[
 L_r^-
 \le(W_r+2r-1)e
 =(2r^2+4r)e.
\tag{1.11}
\]

The exact division is

\[
 2r^3+2r^2+r-1
 =(r-1)(2r^2+4r)+(5r-1),
\]

with

\[
 0<5r-1<2r^2+4r.
\]

Therefore

\[
 \boxed{e\ge r,\qquad g(\mathcal A_r\dot\cup\mathcal B_r)\ge W_r+r.}
\tag{1.12}
\]

The proof permits arbitrary ambient letters and arbitrary seam-crossing
witnesses.

### 1.5 The \(173/13824\) immutable-matching coefficient

Put

\[
 k=\left\lfloor\frac{r-1}{8}\right\rfloor.
\]

The two selected endpoint tolls satisfy

\[
 \Gamma_r=\frac{289}{1728}r^2+O(r).
\tag{1.13}
\]

Indeed each of the two exact ceiling formulas has leading coefficient
\(289/3456\).  A displayed matching site at slope \(\sigma\) has rank
\(2r+\sigma\).  If its retained literal letter lies inside a rank-\(2r\)
middle witness, then \(\sigma\le0\), regardless of how many coordinates
the owner changes.  Under the hypothesis that only the one preassigned
side incidence at each displayed site may be used,

\[
 a\le
 \sum_{d=0}^{k}(r-d)
 =(k+1)r-\frac{k(k+1)}2
 =\frac{15}{128}r^2+O(r).
\tag{1.14}
\]

The audited endpoint ledger \(4e+a\ge\Gamma_r\) then gives the exact
integer bound

\[
 e\ge
 \max\left\{0,
 \left\lceil
 \frac{\Gamma_r-((k+1)r-k(k+1)/2)}4
 \right\rceil\right\}.
\tag{1.15}
\]

Its leading coefficient is

\[
 \begin{aligned}
 \frac14\left(\frac{289}{1728}-\frac{15}{128}\right)
 &=\frac14\left(\frac{578-405}{3456}\right)\\
 &=\boxed{\frac{173}{13824}}.
 \end{aligned}
\tag{1.16}
\]

The floor in \(k\), the two ceilings in \(\Gamma_r\), and the final ceiling
alter only the \(O(r)\) term.  The side-incidence hypothesis is essential;
the alternating braid deliberately replaces it.

### 1.6 Diagonal path tax

With \(m=\lceil r/2\rceil\), the diagonal portal graph has

\[
 V=rm,
 \qquad
 E=(r-1)(m-1),
 \qquad
 C=V-E=r+m-1.
\]

Its alternating component words use \(2E+C\) letters and cover \(2E\)
distinct middle targets.  Literal completion of the other middle targets
therefore has exact length

\[
 W_r+C=W_r+r+\left\lceil\frac r2\right\rceil-1.
\]

The selected source gaps are disjoint.  Each needs one inserted third-
coordinate pin before its contaminating old successor, while the literal
pin \((h_0;1,0)\) suffices in every gap.  The exact selected restoration tax
is consequently

\[
 \boxed{E=(r-1)(\lceil r/2\rceil-1).}
\tag{1.17}
\]

This is not a sufficiency statement for restoring every old common-lift
witness.

---

## 2. Rankwise support in one packet shell

The total cubic count in U7 can be refined exactly by ambient rank.

For a certified \(\mathcal A_r\)-target define its deviation above the
aligned middle by

\[
 d=x+y+q-2r.
\]

At fixed \(d\), its hook index is

\[
 q=2r-x-y+d.
\]

The atlas condition \(q\le2r-x\) is exactly \(d\le y\).  Therefore, for
\(0\le d\le r\), the number of distinct certified
\(\mathcal A_r\)-targets at deviation \(d\) is

\[
 (r+1)(r-d+1).
\tag{2.1}
\]

Likewise a certified \(\mathcal B_r\)-target at deviation \(d\) has

\[
 t=2r-u-v+d,
\]

and the cap \(t\le2r-u\) is exactly \(d\le v\).  Hence its exact count is

\[
 r(r-d),
 \qquad0\le d\le r,
\tag{2.2}
\]

where the expression is zero at \(d=r\).

### Lemma 2.1 — exact shell rank support

For every \(0\le d\le r\), the U7 half-upper atlas covers exactly the
following certified number of distinct packet targets at ambient rank
\(2r+d\):

\[
 \boxed{
 f_r(d)
 =(r+1)(r-d+1)+r(r-d)
 =W_r-d(2r+1).}
\tag{2.3}
\]

Summing (2.3) over \(d=0,\ldots,r\) recovers

\[
 \frac{(r+1)^2(r+2)}2+\frac{r^2(r+1)}2.
\]

This is an exact support count, not an occurrence count: the packet target
coordinates determine \((x,y,q)\) or \((t,u,v)\) uniquely, and the two
packet pieces are disjoint.

---

## 3. Exact shell fusion inside the equal four-cube

Put

\[
 \tau_r=(R-r,0,R-r,0).
\]

The exact complementary-shell identity is

\[
 \boxed{
 Q_R
 =\{\tau_0\}
 \mathbin{\dot\cup}
 \bigdotcup_{r=1}^{R}
 \tau_r(\mathcal A_r\mathbin{\dot\cup}\mathcal B_r).}
\tag{3.1}
\]

Every packet middle layer translates to global rank \(2R\), and

\[
 \boxed{
 M_R=1+\sum_{r=1}^{R}W_r
 =\frac{2R^3+6R^2+7R+3}{3}.}
\tag{3.2}
\]

For every \(r\), translate the U7 half-upper atlas by \(\tau_r\), and
concatenate the translated words.  Prepend or append the terminal middle
target \(\tau_0\) once.  Translation commutes with coordinatewise maximum,
so every local interval remains a literal interval witness.

### Theorem 3.1 — one-word distinct rank support

There is a nonzero word \(\mathscr W_R\) in \(Q_R\) of exact length

\[
 \boxed{
 |\mathscr W_R|
 =1+\sum_{r=1}^{R}(W_r+2r)
 =M_R+R(R+1).}
\tag{3.3}
\]

It covers the complete global middle layer.  For every integer
\(0\le d\le R\), its certified targets at global rank \(2R+d\) are
pairwise distinct and have exact cardinality

\[
 \boxed{
 S_R(d)=\sum_{r=d}^{R}\bigl(W_r-d(2r+1)\bigr),}
\tag{3.4}
\]

where at \(d=0\) the \(r=0\) term \(W_0=1\) denotes \(\tau_0\).  Equivalently,
with \(n=R-d+1\),

\[
 \boxed{
 S_R(d)
 =(d+1)n^2+\frac{n(n-1)(2n-1)}3.}
\tag{3.5}
\]

#### Proof

The word length is the exact shell width ledger plus
\(\sum_{r=1}^{R}2r=R(R+1)\).  At depth \(d\), only shells with
\(r\ge d\) contribute.  Translation adds rank \(2(R-r)\), so every local
rank \(2r+d\) becomes global rank \(2R+d\).  Lemma 2.1 gives each summand
in (3.4).

The shell decomposition (3.1) is disjoint.  Hence targets coming from
different \(r\) are distinct, while Lemma 2.1 already proves distinctness
inside one shell.  This proves that (3.4) counts actual support.

For the closed form, put \(r=d+j\), where \(0\le j<n\).  Then

\[
 W_r-d(2r+1)
 =2j^2+2(d+1)j+d+1.
\]

Summing the three elementary polynomial sums gives (3.5). \(\square\)

The total number of certified distinct targets in all displayed ranks is

\[
 \boxed{
 1+\sum_{r=1}^{R}
 \left[
 \frac{(r+1)^2(r+2)}2+\frac{r^2(r+1)}2
 \right]
 =1+\frac{3R^4+16R^3+33R^2+32R}{12}.}
\tag{3.6}

Thus the word has \(M_R+O(R^2)\) positions and certifies
\((1/4+o(1))|Q_R|\) distinct targets.  This total count is secondary to the
rankwise support statement (3.5).

---

## 4. One MTF chronology and genuine macro-packets

Regard the four chain factors as disjoint coordinate-increment sets.  The
first raw letter of \(\mathscr W_R\) is a nonempty proper Boolean mask.
Prepend its complement once.  The standard two-block initialization then
embeds the entire raw literal word into one MTF walk.

### Theorem 4.1 — one global chronology

The support in Theorem 3.1 is covered by one fully initialized MTF word of
exact length

\[
 \boxed{M_R+R(R+1)+1.}
\tag{4.1}
\]

With the complete middle layer owned by this one packet, its exact ledgers
are

\[
 \boxed{t-M_R=R(R+1),\qquad b-1=1.}
\tag{4.2}
\]

#### Proof

For a raw literal word of length \(P\), prepending the complement of its
first letter gives a two-block initial state and an MTF walk with
\(t=P\).  Every old contiguous OR is a prefix union at its old endpoint.
Here \(P=M_R+R(R+1)\). \(\square\)

The chronology can also be divided into large packets without losing
distinct support.  Give the terminal target weight one and shell \(r\)
weight \(W_r\).  Scan the shell order greedily, ending a group as soon as
its accumulated middle weight is at least \(R^2\); if the last group has
smaller weight, merge it into its predecessor.  For sufficiently large
\(R\), every resulting group has middle weight at least \(R^2\).

### Theorem 4.2 — exact macro-packet accounting

Let \(q_R\) be the number of groups.  Turning every grouped raw subword into
its own two-block-root MTF walk gives genuine target packets such that

\[
 \boxed{
 M_\beta\ge R^2,
 \qquad
 q_R\le\frac{M_R}{R^2}=O(R),}
\tag{4.3}
\]

and

\[
 \boxed{
 \sum_\beta(t_\beta-M_\beta)=R(R+1),
 \qquad
 \sum_\beta(b_\beta-1)=q_R.}
\tag{4.4}

Both sums are \(o(M_R)\).  Every target counted by (3.5) has exactly one
owner packet.

#### Proof

The shell target families are disjoint, so grouping them gives an integral
ownership partition.  A group containing shell set \(J\) has raw word
length

\[
 M_\beta+2\sum_{r\in J}r.
\]

Its two-block embedding has the same number of visited states and root
surplus one.  Summing over the groups gives
\(2\sum_{r=1}^{R}r=R(R+1)\), proving (4.4).  Since every group has weight
at least \(R^2\), (4.3) follows.  Internal shell witnesses are unchanged,
and disjoint shell ownership proves the final assertion. \(\square\)

Joining the grouped raw words and paying only the first complement recovers
Theorem 4.1 and saves \(q_R-1\) root letters.  Thus the macro-packets and
the single chronology are two exact views of the same literal support.

---

## 5. Comparison with the full deeper ranks

Let

\[
 A_R(d)=\left|Q_R\cap\{|x|=2R+d\}\right|.
\]

For \(0\le d\le R\), inclusion-exclusion gives the exact coefficient

\[
 \boxed{
 A_R(d)
 =\binom{2R+d+3}{3}
  -4\binom{R+d+2}{3}
  +6\binom{d+1}{3},}
\tag{5.1}
\]

where \(\binom ab=0\) for \(a<b\).  There are no triple-coordinate
violations in this range.

The shell description gives an exact set-theoretic deficit, not just the
difference of two asymptotic estimates.  At local depth \(0\le d\le r\),
the entire shell has

\[
 n_r(d)=W_r-d^2
\tag{5.1a}
\]

targets.  Indeed the \(\mathcal A_r\) and \(\mathcal B_r\) deficits are
respectively \(d(d+1)/2\) and \(d(d-1)/2\).  At
\(r<d\le2r\), the shell cap has

\[
 n_r(d)=(2r-d+1)^2.
\tag{5.1b}
\]

The U7 atlas contributes only when \(r\ge d\).  Hence, for
\(1\le d\le R\), its exact missing support at global depth \(d\) is

\[
 \begin{aligned}
 D_R(d)
 &=\sum_{r=d}^{R}\bigl(n_r(d)-f_r(d)\bigr)
   +\sum_{\lceil d/2\rceil\le r<d}n_r(d)\\
 &=\sum_{r=d}^{R}d(2r+1-d)
   +\sum_{\lceil d/2\rceil\le r<d}(2r-d+1)^2.
 \end{aligned}
\tag{5.1c}
\]

The first sum is \(d(R+1)(R-d+1)\).  The second is the sum of the odd
squares \(1^2+3^2+\cdots+(d-1)^2\) when \(d\) is even, and of the even
squares \(2^2+4^2+\cdots+(d-1)^2\) when \(d\) is odd.  In both parities it
equals \(d(d^2-1)/6\).  Therefore

\[
 \boxed{
 D_R(d)=A_R(d)-S_R(d)
 =d(R+1)(R-d+1)+\frac{d(d^2-1)}6.}
\tag{5.1d}
\]

Every term counts a target in a disjoint shell, so (5.1d) is the cardinality
of the literal complement of the certified target family.

If \(d/R\to x\in[0,1]\), equations (3.5) and (5.1) give

\[
 \frac{S_R(d)}{R^3}
 \longrightarrow
 \frac23-x+\frac{x^3}{3}
 =\frac{(1-x)^2(x+2)}3,
\tag{5.2}
\]

and

\[
 \frac{A_R(d)}{R^3}
 \longrightarrow
 \frac23-x^2+\frac{x^3}{2}.
\tag{5.3}
\]

Their quotient is (0.4).  In particular, for every sequence \(d=o(R)\),

\[
 \boxed{S_R(d)=(1-o(1))A_R(d).}
\tag{5.4}
\]

This is simultaneous rankwise distinctness.  It is stronger than a lower
bound on the sum of endpoint incidences or on the total number of exposed
flags.  Every counted object is a different box target, and (5.4) holds for
each selected depth separately.

For each fixed \(\varepsilon>0\), (0.4) is positive uniformly on
\(0\le x\le1-\varepsilon\).  Hence the same word covers a fixed positive
fraction of every rank through depth \((1-\varepsilon)R\), although the
fraction tends to zero as \(x\uparrow1\).

### Theorem 5.1 — complete distinct upper-band repair

For \(1\le H\le R\), append every target in the disjoint missing sets
counted by \(D_R(d)\), \(1\le d\le H\), once literally to
\(\mathscr W_R\).  The resulting one word covers every target in the ranks

\[
 2R,2R+1,\ldots,2R+H
\]

and has exact length

\[
 \boxed{
 M_R+R(R+1)+\mathcal D_R(H),}
\tag{5.5}
\]

where

\[
 \boxed{
 \begin{aligned}
 \mathcal D_R(H)
 &=\sum_{d=1}^{H}D_R(d)\\
 &=(R+1)\bigl((R+1)A-B\bigr)
   +\frac{A^2-A}{6},\\
 A&=\frac{H(H+1)}2,
 \qquad
 B=\frac{H(H+1)(2H+1)}6.
 \end{aligned}}
\tag{5.6}
\]

If a fully initialized MTF chronology is required, prepend the complement
of the first raw letter once, increasing (5.5) by exactly one.

#### Proof

The missing sets at different ranks and in different shells are disjoint.
Appending a missing target as one literal letter represents it by its
one-position interval and does not disturb any old witness.  Summing the
first term of (5.1d) gives

\[
 (R+1)\sum_{d=1}^{H}d(R+1-d)
 =(R+1)((R+1)A-B).
\]

Also

\[
 \sum_{d=1}^{H}\frac{d(d^2-1)}6
 =\frac{1}{6}\left(A^2-A\right).
\]

This proves (5.5)--(5.6). \(\square\)

Uniformly for \(H\le R\),

\[
 \mathcal D_R(H)=O(H^2R^2+H^4).
\tag{5.7}
\]

Since \(M_R=\Theta(R^3)\), Theorem 5.1 has length \(M_R+o(M_R)\) whenever
\(H=o(\sqrt R)\).  At \(H\asymp\sqrt R\), its first repair term is already
\(\Theta(M_R)\); this is the exact ceiling of literal append-repair for the
present atlas, not a no-go for a different recoding.

### Corollary 5.2 — repaired macro-packet ledger

Assign every appended missing target to the final macro-packet of
Theorem 4.2.  Its middle ownership is unchanged, while each repair letter
adds one visited state.  The exact aggregate ledgers become

\[
 \boxed{
 \sum_\beta(t_\beta-M_\beta)
 =R(R+1)+\mathcal D_R(H),
 \qquad
 \sum_\beta(b_\beta-1)=q_R.}
\tag{5.8}
\]

Thus the complete upper band through every \(H=o(\sqrt R)\) is carried by
genuine \(R^2\)-middle-owner macro-packets with both surpluses \(o(M_R)\),
or equivalently by the one global chronology of Theorem 5.1 with one
initial complement letter.

---

## 6. Two orientations: a sharper distinct-support target

There is a second exact support gain which, viewed by itself, does not
identify a one-baseline fusion.  The subsequent row-core report cited
above obtains a stronger symmetric-band chronology by wholesale recoding.
On \(\mathcal A_r\), interchange the two short coordinates:

\[
 \iota_A(x,y;h_q)=(y,x;h_q).
\]

On the \(\mathcal B_r\) *target coordinates*, put \(a=u-1\) and \(b=v\),
and interchange \(a,b\):

\[
 (h_t;u,v)\longmapsto(h_t;v+1,u-1).
\]

The second formula must **not** be applied letter by letter to U7's mixed
\(\mathcal A_r/\mathcal B_r\) carrier block: its \(u=0\) letters would be
sent outside the shifted coordinate range.  The transposed target family
nevertheless has the following literal realization.  For each
\(0\le b\le r-1\), use

\[
 G_{b,0}=(h_{2r-b-1};0,b),
 \qquad
 G_{b,j}=(h_{2r-b-1-j};j,b)
 \quad(1\le j\le r).
\]

Here \(G_{b,0}\in\mathcal A_r\), because \((0,b)=h_b\), and every
\(G_{b,j}\) with \(j\ge1\) lies in \(\mathcal B_r\).  If
\(T=(h_t;u,b)\) is a transposed-family target and
\(a=2r-b-1-t\), then \(0\le a<u\) and

\[
 \bigvee_{j=a}^{u}G_{b,j}=T.
\]

Thus the support transposition below is literal, but its \(\mathcal B_r\)
word is this new block rather than an affine image of the old mixed word.
No one-baseline fusion claim is made in this section.

### Theorem 6.1 — exact two-orientation shell support

For \(0\le d\le r\), the union of the original U7 support and its
short-coordinate transpose misses exactly

\[
 \boxed{d^2}
\tag{6.1}
\]

targets from the complete rank-\((2r+d)\) layer of
\(\mathcal A_r\dot\cup\mathcal B_r\).  Equivalently, its exact distinct
support is

\[
 \boxed{g_r(d)=W_r-2d^2.}
\tag{6.2}
\]

#### Proof

In \(\mathcal A_r\), a full layer target at depth \(d\) is determined by
\((x,y)\in[0,r]^2\) with \(x+y\ge d\).  The original atlas covers
\(y\ge d\), and the transposed atlas covers \(x\ge d\).  A target missed
by both therefore has

\[
 0\le x,y<d,
 \qquad x+y\ge d.
\]

There are exactly

\[
 1+2+\cdots +(d-1)=\frac{d(d-1)}2
\]

such targets.

For \(\mathcal B_r\), use \(a=u-1,b=v\in[0,r-1]\).  A full layer target
is legal exactly when \(a+b\ge d-1\).  The original atlas covers
\(b\ge d\), while its transpose covers \(a\ge d\).  Thus the common
missing set has \(0\le a,b<d\) and \(a+b\ge d-1\), of exact size

\[
 1+2+\cdots+d=\frac{d(d+1)}2.
\]

The packet pieces are disjoint, so the total miss is \(d^2\).  Since the
full shell layer has \(n_r(d)=W_r-d^2\) targets, its covered part has size
\(W_r-2d^2\). \(\square\)

### Corollary 6.2 — exact global two-orientation deficit

Across the equal-cube shell peel, the union of the two translated support
families misses exactly

\[
 \boxed{
 D_R^{(2)}(d)
 =d^2(R-d+1)+\frac{d(d^2-1)}6}
\tag{6.3}
\]

distinct targets from global rank \(2R+d\), for \(0\le d\le R\).  Hence
its exact support is

\[
 \boxed{S_R^{(2)}(d)=A_R(d)-D_R^{(2)}(d).}
\tag{6.4}
\]

Indeed, every shell \(r\ge d\) contributes the \(d^2\) miss from
Theorem 6.1, and the omitted shells \(\lceil d/2\rceil\le r<d\) contribute
the same cap sum \(d(d^2-1)/6\) as in (5.1d).  These are disjoint literal
shell targets.  Concatenating the original atlas, the transposed
\(\mathcal A_r\)-blocks, and all explicit \(G\)-blocks in every shell
realizes the union without any boundary identification, in exact displayed
raw length

\[
 \boxed{2M_R-1+2R(R+1)+R.}
\tag{6.5}
\]

Thus (6.4) is an unconditional literal support theorem, but (6.5) pays two
middle-width baselines.

For \(1\le H\le R\), define

\[
 A_H=\frac{H(H+1)}2,
 \qquad
 B_H=\frac{H(H+1)(2H+1)}6.
\]

The exact missing-target count through depth \(H\) is

\[
 \boxed{
 \begin{aligned}
 \mathcal D_R^{(2)}(H)
 &=\sum_{d=1}^{H}D_R^{(2)}(d)\\
 &=(R+1)B_H-\frac{5A_H^2+A_H}{6}.
 \end{aligned}}
\tag{6.6}
\]

In particular,

\[
 \mathcal D_R^{(2)}(H)=O(RH^3+H^4)=o(M_R)
 \quad\hbox{when}\quad H=o(R^{2/3}).
\tag{6.7}
\]

Consequently, a one-baseline dynamic fusion of the two literal atlas
supports, with \(o(M_R)\) fusion loss, would give a complete upper-band
cover through every \(H=o(R^{2/3})\) after literal complement repair.
This implication is conditional: no such fusion is proved here.

### Proposition 6.3 — immutable principal-order obstruction

Let

\[
 E_{x,y}=(x,y;h_{2r-x-y-1}),
 \qquad (x,y)\in[0,r]^2,
\]

with the U7 corner convention.  These \((r+1)^2\) principal masks occur
row-major in the original \(\mathcal A_r\)-atlas and column-major in its
transpose.  The longest common subsequence of the two principal-mask
orders has exact length \(2r+1\).  Hence every word which retains both
orders as subsequences has length at least

\[
 \boxed{
 2(r+1)^2-(2r+1)=2r^2+2r+1=W_r.}
\tag{6.8}
\]

#### Proof

Two distinct grid points occurring in the same order in both sequences
must be nondecreasing in both coordinates.  Thus a common subsequence is a
strict chain in \([0,r]^2\), and its length is at most \(2r+1\) because
the rank \(x+y\) strictly increases.  A monotone lattice path from
\((0,0)\) to \((r,r)\) attains \(2r+1\).  The shortest-common-supersequence
identity now gives (6.8). \(\square\)

This is not an absolute obstruction to dynamic recoding.  It says that an
immutable fusion of only the two common \(\mathcal A_r\) principal grids
already consumes the full \(W_r\) packet baseline.  A
\(W_r+o(r^2)\)-length fusion can therefore leave only \(o(r^2)\) positions
outside those retained principal occurrences; the \(\mathcal B_r\)
service must be multiplexed through or dynamically recoded from them.

---

## 7. Boolean one-step distinct multipin allocation

The equal-box theorem above gives an unconditional special regime.  There is
also a general Boolean allocation theorem which imports the U7 multipin
principle directly into the verified strip boundary.  It separates distinct
target allocation from chronology.

Let \(N\) and \(h\) satisfy

\[
 0\le h,
 \qquad
 N\ge2h+2.
\]

Put

\[
 \mathcal L=\binom{[N]}h,
 \qquad
 \mathcal U=\binom{[N]}{h+1}.
\]

Let \(D\subseteq\mathcal U\), \(|D|=u\), and write

\[
 F=\mathcal U\setminus D.
\]

### Theorem 7.1 — two-matching distinct-carrier graph

There are two edge-disjoint inclusion matchings

\[
 M_0,M_1:\mathcal L\longrightarrow\mathcal U
\]

which both saturate \(\mathcal L\).  After deleting at most \(2u\) lower
targets, the remaining lower targets label the edges of a simple graph
\(\Gamma\) on vertex set \(F\) such that

1. every edge label \(B\) is contained in its two endpoint owners;
2. the endpoint intersection is exactly \(B\);
3. all edge labels are distinct;
4. \(\Delta(\Gamma)\le2\); and
5. the number of edges is at least \(|\mathcal L|-2u\).

#### Proof

In the full inclusion graph, every left vertex has degree

\[
 d_L=N-h,
\]

and every right vertex has degree

\[
 d_U=h+1.
\]

For \(S\subseteq\mathcal L\), edge counting gives

\[
 d_L|S|\le d_U|N(S)|.
\]

Since \(d_L\ge d_U\), Hall's theorem gives a matching \(M_0\) saturating
the left side.  Delete its edges.  Every left degree is now \(d_L-1\),
every right degree is at most \(d_U\), and

\[
 d_L-1\ge d_U
\]

by \(N\ge2h+2\).  The same edge-count proof of Hall gives a second
left-saturating matching \(M_1\), edge-disjoint from \(M_0\).

Delete every \(B\in\mathcal L\) for which
\(M_0(B)\in D\) or \(M_1(B)\in D\).  Since each \(M_i\) is injective, at
most \(2u\) labels are deleted.  For every retained \(B\), put an edge
between \(M_0(B)\) and \(M_1(B)\), labelled by \(B\).  The endpoints are
distinct because the two inclusion edges at \(B\) are distinct.  Two
distinct \((h+1)\)-sets containing \(B\) intersect exactly in \(B\), so
the endpoint pair determines its label and parallel edges are impossible.
Every owner is used at most once by each matching, proving maximum degree
two. \(\square\)

This is already a distinct-support statement: it produces at least
\(|\mathcal L|-2u\) different deeper masks, each with two different old
owners.  No incidence multiplicity is substituted for target cardinality.

### Theorem 7.2 — exact component-word ledger

Let \(q\le2u\) be the number of deleted lower labels.  Write

* \(p\) for the number of nontrivial path components of \(\Gamma\);
* \(z\) for its number of cycle components; and
* \(i\) for its number of isolated vertices.

Then all targets in \(F\) and all retained lower labels have one literal
word of exact length

\[
 \boxed{|F|+p+z.}
\tag{7.1}
\]

After appending \(D\) and the \(q\) deleted lower targets literally, both
complete adjacent levels have a word of exact length

\[
 \boxed{
 |\mathcal U|+p+z+q.}
\tag{7.2}
\]

Moreover

\[
 \boxed{
 p+z+q
 \le |\mathcal U|-|\mathcal L|+3u+z.}
\tag{7.3}
\]

#### Proof

For a nontrivial path

\[
 T_0\mathbin{-}_{B_1}T_1
 \mathbin{-}_{B_2}\cdots
 \mathbin{-}_{B_s}T_s,
\]

use the word

\[
 T_0,B_1,B_2,\ldots,B_s,T_s.
\]

It covers each edge label singly, both endpoint owners singly, and every
internal owner because the two distinct incident \(h\)-subsets have union
\(T_j\).  Its length is \(s+2\).  For a cycle with successive labels
\(B_1,\ldots,B_s\), use

\[
 B_1,B_2,\ldots,B_s,B_1;
\]

this has length \(s+1\) and covers every edge and vertex.  An isolate is
written literally.

If \(E\) is the number of graph edges, then

\[
 |F|=E+p+i.
\]

The concatenated component length is

\[
 E+2p+z+i=|F|+p+z,
\]

proving (7.1).  Appending \(u+q\) missing targets and using
\(|F|+u=|\mathcal U|\) gives (7.2).

Finally,

\[
 p\le |F|-E
 =|\mathcal U|-|\mathcal L|-u+q.
\]

Use \(q\le2u\) in \(p+z+q\) to obtain (7.3). \(\square\)

### Application to the verified lower strip boundary

Take

\[
 N=2m,
 \qquad
 h=m-H-1,
\]

and let \(F\) be the distinct rank-\((m-H)\) targets already supplied by
the verified strip matching.  Then

\[
 u=u_H^-=o(W),
\]

while

\[
 |\mathcal U|-|\mathcal L|
 =\binom{2m}{m-H}-\binom{2m}{m-H-1}
 =o(W)
\]

in the verified regime \(H=o(\sqrt m)\).  Theorems 7.1--7.2 therefore
prove:

> There is an exact multipin allocation of all but \(o(W)\) distinct
> rank-\((m-H-1)\) targets to pairs of distinct already covered
> rank-\((m-H)\) owners.  A near-width two-level carrier word follows if
> the two matchings can be chosen with \(z=o(W)\).

This reduces distinct one-step support to a cycle-selection question; the
support allocation itself is solved.

For compatibility with the full macro-packet chronology, more is needed.
If the selected graph paths can be decomposed into \(J\) runs which follow
the imported cyclic-strip owner order, with

\[
 J=o(W/H)
\]

and only \(o(W)\) exceptional labels, then the asymmetric
\(a=H+1\) useful-prefix recoding realizes every run.  Closing a run with its
endpoint owner and reverse-writing the next useful prefix costs
\(O(H)\) per run, hence \(O(HJ)=o(W)\) in total.  The exceptional targets
are literal \(o(W)\) repair.

The exact remaining gate is therefore:

> **Chronology-compatible two-matching gate — UNPROVED.**  Choose the two
> inclusion matchings in Theorem 7.1 so that \(z=o(W)\) and, after deleting
> \(o(W)\) labels, their component order splits into
> \(J=o(W/H)\) canonical strip runs.

This is strictly stronger than Hall and strictly more precise than an
aggregate support demand.  It asks for one integral distinct-target
allocation and the same allocation's legal macro chronology.

---

## 8. What the combination does and does not solve

Two exact obstructions show why the one-sided theorem does not automatically
become a symmetric band theorem.

### 8.1 Summed immutable source-gap tax

U7's diagonal-path theorem charges shell \(r\) exactly

\[
 E_r=(r-1)(\lceil r/2\rceil-1)
\]

insertions if its diagonal multipin order and all selected old source-gap
witnesses are simultaneously retained.  These source gaps belong to
disjoint shell subwords, so macro grouping cannot make one insertion lie in
two of them.  Therefore the exact summed tax is

\[
 \mathcal E_R=\sum_{r=2}^{R}E_r.
\tag{8.1}
\]

Writing \(R=2s\) or \(R=2s+1\), direct summation gives

\[
 \boxed{
 \mathcal E_{2s}
 =\frac{s(8s^2-9s+1)}6,}
\tag{8.2}
\]

and

\[
 \boxed{
 \mathcal E_{2s+1}
 =\frac{s(8s^2+3s+1)}6.}
\tag{8.3}
\]

Consequently

\[
 \boxed{
 \mathcal E_R
 =\frac{R^3}{6}+O(R^2)
 =\left(\frac14+o(1)\right)M_R.}
\tag{8.4}
\]

Thus the old source-gap chronology cannot be restored shellwise at
coefficient one.  A successful symmetric or cap-completing braid must
reorder a positive density of those local gaps; this conclusion does not
apply to a new dynamic chronology which abandons them.

### 8.2 Retained-letter lower-side obstruction

The physical ranks of the U7 atlas letters can also be counted exactly.
In an \(\mathcal A_r\)-block, \(P_0\) has rank \(2r\) and every other
letter has rank \(2r-1\).  In a \(\mathcal B_r\)-block,

\[
 |C_{u,0}|=2r-u,
 \qquad
 |C_{u,j}|=
 \begin{cases}
 2r-1,&j\text{ odd},\\
 2r-u-1,&j\text{ even}.
 \end{cases}
\tag{8.5}
\]

For a fixed lower depth \(d\ge2\), the exact number of old atlas letters
in translated shell \(r\) whose global rank is at most \(2R-d\) is

\[
 \lambda_r(d)
 =(r-d+1)_+
  +\left\lfloor\frac r2\right\rfloor(r-d+2)_+.
\tag{8.6}
\]

The shared \(\mathcal A/\mathcal B\) boundary letter has local rank
\(2r-1\), so it is ineligible and causes no double-count correction for
\(d\ge2\).  Across the whole atlas put

\[
 \boxed{
 \Lambda_R(d)
 =\sum_{r=d}^{R}(r-d+1)
  +\sum_{r=d-1}^{R}\left\lfloor\frac r2\right\rfloor(r-d+2).}
\tag{8.7}
\]

Let

\[
 n_0=M_R+R(R+1)
\]

be the raw atlas length.  Suppose a final word of length \(n\) retains
\(n_0-a_{\rm rec}\) of these occurrences as unchanged physical letters,
in arbitrary positions and order, and covers the complete lower rank
\(2R-d\).  Fixed-rank endpoint injection requires
\(A_R(d)\) physical letters of rank at most \(2R-d\).  At most
\(\Lambda_R(d)\) retained atlas letters qualify, while all recoded and new
positions number at most \(a_{\rm rec}+n-n_0\).  Hence the exact ledger is

\[
 \boxed{
 a_{\rm rec}+(n-n_0)
 \ge A_R(d)-\Lambda_R(d).}
\tag{8.8}
\]

For every fixed \(d\ge2\),

\[
 \Lambda_R(d)=\frac{R^3}{6}+O_d(R^2)
 =\left(\frac14+o(1)\right)M_R,
\]

whereas \(A_R(d)=(1-o(1))M_R\).  Therefore any
\(n=M_R+o(M_R)\) lower-side completion which physically retains atlas
letters must recode

\[
 \boxed{
 a_{\rm rec}\ge\left(\frac34-o(1)\right)M_R.}
\tag{8.9}
\]

This is a retained-letter obstruction, not an absolute no-go.  The
asymmetric useful-prefix mechanism can in principle perform wholesale
recoding; (6.9) says that mere macro seams and \(o(M_R)\) insertions cannot
substitute for it.

### Proved

1. The entire U7 exact ledger, including the \(173/13824\) coefficient,
   survives adversarial cross-audit.
2. The U7 half-upper family has the exact rank profile (2.3).
3. Complementary-shell translation makes these targets globally disjoint;
   the exact support at every depth is (3.5).
4. One width-plus-\(O(R^2)\) global chronology covers almost every target
   in every upper rank of depth \(o(R)\).
5. Genuine \(R^2\)-middle-owner macro-packets retain this same integral
   support with both aggregate MTF surpluses \(o(M_R)\).

### Not proved

1. The U7 word does not cover the lower packet halves or the upper caps
   \(q>2r-x\) and \(t>2r-u\).
2. The support fraction in (0.4) is not one at fixed positive depth ratio.
3. Exact-root or immutable common-lift insertion cannot add the missing
   family at subquadratic packet cost; the audited \(173/13824\) and
   selected-gap bounds quantify this failure.
4. Different four-chain parents cannot be serviced independently in the
   global Boolean aggregation.  The theorem here fuses shells inside one
   equal parent; a literal cross-parent allocation remains necessary.
5. No lower-half partner chronology sharing the same width baseline is
   constructed.

The precise new boundary is therefore support-theoretic.  Multipin carriers
and macro chronology already give near-surjective **distinct** support at
every sublinear upper depth inside the equal four-cube.  The remaining task
is to build a dynamically reordered lower/cap partner, or a cross-parent
analogue, without freezing the U5 side incidences and without duplicating
the middle baseline.
