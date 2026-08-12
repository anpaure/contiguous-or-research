# Cross-audit U of X cross-seam repacketization

Date: 2026-07-25

Audited report: MATH_ATTACK_X_CROSS_SEAM_REPACKETIZATION_20260725.md.

## 0. Verdict

The chronology, exact word lengths, macro-packet arithmetic, fixed-rank
endpoint floor, and linear overlap trilemma all pass.

Two scope repairs are necessary.

1. In Corollary 3.2, the scalar equality
   \[
   \sum_\alpha M_\alpha+u_0=W
   \]
   does not by itself imply middle-layer coverage. The owned middle target
   sets and the \(u_0\) repair targets must be pairwise disjoint and must
   partition the middle layer. This holds in the verified matched-strip
   application.

2. The asymmetric prefix exposes \(s=2\ell\) distinct targets inside each
   individual new row, but cross-strip distinctness is imported only for
   depths \(|q|\le H\). Nothing in repacketization makes the new rows
   \(q>H\) target-disjoint.

The equal-PACK multipin pattern has an independently proved cyclic-strip
analogue at the witness level, not a formal transfer theorem and not an
ownership theorem. There is a literal two-deeper-row splice: with

\[
F_{\alpha,i}=A_{\alpha,i}^{(H+2)}
\]

one cyclic carrier row per strip covers the verified band and candidate
rows \(H+1,H+2\), with old lower cores represented by genuine multipin
intervals. If \(L_1,L_2\) are the distinct deep-row leaves, its exact
global length is

\[
\boxed{n=W+(U-u_0)+(2H+2)p+L_1+L_2.}
\tag{0.1}
\]

Thus \(L_1+L_2=o(W)\) would complete both rows at coefficient one. Neither
X nor U7 proves that estimate. Repeated rank-\(r\) carrier occurrences
cannot create new rank-\(r\) values: two distinct rank-\(r\) sets have
union of rank at least \(r+1\). A new deep-row matching or owner-injection
theorem remains necessary. No full-cube conclusion follows.

---

## 1. Exact useful-prefix length

Piece \(\alpha\) has cyclic length \(s_\alpha\), useful depths
\(a_\alpha,b_\alpha\), and prefix block count

\[
h_\alpha=1+a_\alpha+b_\alpha.
\]

The first piece emits one complement mask, its \(h_1\) blocks in reverse,
and \(s_1-1\) remaining principal updates. Its exact cost is

\[
1+h_1+(s_1-1)=s_1+a_1+b_1+1.
\tag{1.1}
\]

A later piece costs

\[
h_\alpha+(s_\alpha-1)=s_\alpha+a_\alpha+b_\alpha.
\tag{1.2}
\]

Therefore

\[
\boxed{
n_{\rm prin}
=\sum_\alpha s_\alpha+1+\sum_\alpha(a_\alpha+b_\alpha).}
\tag{1.3}
\]

There is no hidden full-tail reset. At a seam, after writing

\[
B_h,B_{h-1},\ldots,B_1,
\]

the suffix beginning at \(B_j\) has OR
\(B_1\cup\cdots\cup B_j\). Inherited-tail coordinates have older
last-occurrence times and are outside that suffix. Later MTF prefix unions
are represented by suffixes beginning at the last occurrence of their
final prefix block. Hence every advertised target has a literal contiguous
OR witness.

For

\[
s_\alpha=2\ell,\qquad a_\alpha=b_\alpha=H,\qquad
2\ell p=W-u_0,
\]

and \(U\) literal repairs,

\[
\boxed{n=W+(U-u_0)+2Hp+1.}
\tag{1.4}
\]

Since

\[
\frac{2Hp}{W}
=\frac H\ell\left(1-\frac{u_0}{W}\right)=o(1),
\]

the exact length claim passes.

---

## 2. Ownership quantifiers

Let \(\mathcal M_\alpha\) be the middle set owned by piece \(\alpha\), and
\(\mathcal R_0\) the middle repair set. The needed hypothesis is

\[
\mathcal M_\alpha\cap\mathcal M_\beta=\varnothing\quad(\alpha\ne\beta),
\qquad
\mathcal R_0\cap\mathcal M_\alpha=\varnothing,
\tag{2.1}
\]

\[
\left(\mathop{\dot\bigcup}_\alpha\mathcal M_\alpha\right)
\mathbin{\dot\cup}\mathcal R_0=\binom{[2m]}m.
\tag{2.2}
\]

Then \(M_\alpha=|\mathcal M_\alpha|\), \(u_0=|\mathcal R_0|\), and the
scalar baseline follows. The converse is false: equal cardinalities alone
do not exclude duplicate owners. The other repairs must likewise be
distinct nonempty targets outside advertised ownership.

Under (2.1)--(2.2), the exact formula is

\[
\boxed{
n=W+\sum_\alpha(s_\alpha-M_\alpha)+(U-u_0)
+1+\sum_\alpha(a_\alpha+b_\alpha).}
\tag{2.3}
\]

The matched-strip input supplies these hypotheses through \(|q|\le H\).
For fixed strip and fixed \(q<\ell\), its \(s\) cyclic translates are
distinct because the active interval has proper length strictly between
\(0\) and \(s\). Cross-strip uniqueness for \(q>H\) is not imported.

---

## 3. Macro-packet ledger

Put

\[
s=2\ell,\qquad
g=\left\lceil\frac{k}{s}\right\rceil,\qquad
q=\left\lfloor\frac pg\right\rfloor,
\]

Work in the imported sufficiently large regime, where \(p\ge g\) and
hence \(q\ge1\). Write \(p=qg+r_0\), \(0\le r_0<g\). The first \(q-1\) groups have
\(g\) strips and the last has \(h_q=g+r_0\).

For a nonfinal group with \(h_\beta\) strips,

\[
M_\beta=sh_\beta,\qquad
t_\beta=sh_\beta+(h_\beta-1)(a+b).
\tag{3.1}
\]

For the final group,

\[
M_q=sh_q+u_0,\qquad
t_q=sh_q+(h_q-1)(a+b)+U.
\tag{3.2}
\]

Here \(t_\beta\) counts time-indexed state occurrences, including equal
consecutive occurrences. Each independently initialized macro begins with
\(b_\beta=a+b+2\) blocks. Hence

\[
\boxed{
\sum_{\beta=1}^q(t_\beta-M_\beta)
=(p-q)(a+b)+(U-u_0),}
\tag{3.3}
\]

\[
\boxed{
\sum_{\beta=1}^q(b_\beta-1)=q(a+b+1),}
\tag{3.4}
\]

\[
\boxed{p(a+b)+q+(U-u_0)}
\tag{3.5}
\]

is the total surplus. Every macro owns at least \(sg\ge k\) middle
targets. These formulas pass.

The macros are standalone freshly initialized realizations, not literal
cuts of the inherited-tail global walk. Their independent total length is

\[
W+p(a+b)+q+(U-u_0).
\tag{3.6}
\]

Replacing the later \(q-1\) complement roots by prefix seams yields

\[
W+p(a+b)+(U-u_0)+1,
\tag{3.7}
\]

the global chronology. This is the exact relation between the two ledgers.

---

## 4. Wholesale endpoint recoding

Let \(a=H+c\), \(0<c\), \(a<\ell\). Cyclically,

\[
\boxed{
A_i^{(H)}=\bigcup_{j=i-c}^{i}A_j^{(a)}.}
\tag{4.1}
\]

The first new interval begins at \(i+H\), the last ends at
\(i+\ell-1\), and consecutive intervals overlap.

There is also an exact cut witness. Let a linear run begin at \(i_0\) and
put \(\kappa=i_0+d\), \(0\le d<c\). Then

\[
\boxed{
A_\kappa^{(H)}
=
\left(\bigcup_{t=\kappa+H}^{i_0+a-1}\{z_t\}\right)
\cup
\left(\bigcup_{j=i_0}^{\kappa}A_j^{(a)}\right).}
\tag{4.2}
\]

The singleton union is a suffix of the future-marker string emitted in
increasing physical order; it is followed immediately by
\(A_{i_0}^{(a)},\ldots,A_\kappa^{(a)}\). Thus (4.2) is a literal interval, and
its active coordinates are exactly
\(z_{\kappa+H},\ldots,z_{\kappa+\ell-1}\).

Consequently every old lower-core witness survives. “Every principal
endpoint changes” means each of the \(P=2\ell p\) principal core
occurrences is replaced; it does not refer to reset singletons or inherited
tail blocks. The asymmetric length

\[
\boxed{
n=W+(U-u_0)+p(2H+c_-+c_+)+1}
\tag{4.3}
\]

passes.

---

## 5. Fixed-rank and overlap obstruction

If a Boolean word covers any \(Q\) distinct rank-\(r\) targets, it has at
least \(Q\) distinct positions whose letters have size at most \(r\):
choose right endpoints; suffix ORs ending at one position form a chain.

Put

\[
r=m-H-1,\qquad P=W-u_0,\qquad E=n-P.
\]

Choose one arbitrary interval \(I_i\) for each of the \(P\) distinct old
rank-\((m-H)\) lower cores, and set

\[
R=\#\{j:j\notin I_i\text{ for all }i\},
\qquad
O=\sum_{i=1}^P|I_i|-\left|\bigcup_{i=1}^PI_i\right|.
\]

### Theorem 5.1 (partial-row overlap trilemma)

If the word covers \(Q\) distinct targets of rank \(m-H-1\), then

\[
\boxed{2E+O\ge Q+R.}
\tag{5.1}
\]

#### Proof

At most \(n-Q\) letters have size at least \(m-H\). A singleton old-core
witness equals its distinct rank-\((m-H)\) target, so at most \(n-Q\) of
the \(P\) witnesses are singletons. At least \(P-n+Q=Q-E\) are
nonsingletons, giving

\[
\sum_i(|I_i|-1)\ge Q-E.
\tag{5.2}
\]

On the other hand,

\[
\sum_i(|I_i|-1)
=\left|\bigcup_iI_i\right|+O-P
=n-R+O-P
=E+O-R.
\tag{5.3}
\]

Combining proves (5.1). \(\square\)

For

\[
Q=N_{H+1}=\binom{2m}{m-H-1}
\]

this recovers X Theorem 8.1. Since

\[
\frac{N_{H+1}}W
=\prod_{i=1}^{H+1}\frac{m-i+1}{m+i}=1-o(1)
\]

when \(H=o(\sqrt m)\), any \(W+o(W)\) word covering all—or merely
\(N_{H+1}-o(W)\)—targets in that row obeys

\[
\boxed{O=(1-o(1))W.}
\tag{5.4}
\]

This survives wholesale recoding: no retained letter, strip order,
canonical root, or prescribed witness is assumed. Its only scope condition
is actual near-complete support in the next row. Recoding alone does not
trigger (5.4).

---

## 6. Testing the U7 multipin mechanism

### 6.1 Same-rank barrier

If \(|Y|=|Z|=r\) and \(|Y\cup Z|=r\), then \(Y=Z\). Therefore an interval
containing two distinct rank-\(r\) letters cannot have rank-\(r\) OR.

After recoding to depth \(q\), the principal letters
\(A_{\alpha,i}^{(q)}\) themselves have rank \(m-q\). Reordering or
overlapping them cannot manufacture a new target at that rank. U7 creates
many owners because its carriers are strictly below them and an explicit
product-box injection supplies owner labels. X supplies no analogous
cross-strip product embedding or owner injection beyond \(H\). Any new
rank-\((m-q)\) owner not already present among the principal values must
therefore use an interval of strictly smaller carriers. Those carriers may
be introduced while retaining the principal occurrences; wholesale
replacement is not forced. The splice below gives one independent
cyclic-strip analogue by recoding.

### 6.2 Independently proved cyclic-strip analogue

This subsection constructs a literal Boolean OR word. It is not claimed
to be a separately fully initialized MTF macro-root; full initialization
is unnecessary for testing target support and contiguous witnesses.

Assume \(H+2<\ell\), and set

\[
F_{\alpha,i}:=A_{\alpha,i}^{(H+2)}
=C_\alpha\cup I_\alpha(i+H+2,\ell-H-2).
\tag{6.1}
\]

For strip \(\alpha\), emit

\[
\boxed{
F_{\alpha,0},\ldots,F_{\alpha,s-1},
F_{\alpha,0},\ldots,F_{\alpha,2H+1}.}
\tag{6.2}
\]

The module length is \(s+2H+2\). A run of \(t\) consecutive carriers
ending at \(F_{\alpha,i}\), \(1\le t\le2H+3\), has OR

\[
\boxed{
\bigvee_{j=i-t+1}^{i}F_{\alpha,j}
=C_\alpha\cup
I_\alpha(i-t+1+H+2,\ell-H-2+t-1).}
\tag{6.3}
\]

The repeated prefix makes every cyclic run of maximum length \(2H+3\)
linear.

For \(0\le q\le H+2\), take \(t=H+3-q\). Formula (6.3) is

\[
C_\alpha\cup I_\alpha(i+q,\ell-q),
\]

the lower target at depth \(q\). For \(1\le q\le H\), take
\(t=H+q+3\); it is

\[
C_\alpha\cup I_\alpha(i-q,\ell+q),
\]

the upper target at depth \(q\). Thus the module covers the old strip band
and candidate lower rows \(H+1,H+2\). In particular,

\[
\boxed{
A_{\alpha,i}^{(H+1)}
=F_{\alpha,i-1}\cup F_{\alpha,i},}
\tag{6.4}
\]

\[
\boxed{
A_{\alpha,i}^{(H)}
=F_{\alpha,i-2}\cup F_{\alpha,i-1}\cup F_{\alpha,i}.}
\tag{6.5}
\]

The endpoint carriers in (6.5) are deficient in two opposite active
coordinates. This is the cyclic-strip analogue of the U7 multipin path.

Define

\[
D_j=
\left|
\{A_{\alpha,i}^{(H+j)}:
1\le\alpha\le p,\ i\in\mathbb Z_s\}
\right|,
\quad
N_j=\binom{2m}{m-H-j},
\quad
L_j=N_j-D_j
\quad(j=1,2).
\tag{6.6}
\]

Append the \(U\) old-band repairs and all missing targets in the two deep
rows. Since \(sp=P=W-u_0\), the exact length is

\[
\begin{aligned}
n
&=p(s+2H+2)+U+L_1+L_2\\
&=\boxed{
W+(U-u_0)+(2H+2)p+L_1+L_2.}
\end{aligned}
\tag{6.7}
\]

\[
\boxed{
\frac{(2H+2)p}{W}
=\frac{H+1}{\ell}\left(1-\frac{u_0}{W}\right)=o(1).}
\tag{6.8}
\]

Thus (6.7) is \(W+o(W)\) if \(L_1+L_2=o(W)\).

For the \(P\) old lower cores, use the three-letter witnesses (6.5). Per
strip their union contains the \(s\) base positions and first two repeated
positions. Therefore

\[
\sum_i|I_i|=3P,\qquad
\left|\bigcup_iI_i\right|=P+2p,
\]

\[
\boxed{O=2P-2p=(2-o(1))W.}
\tag{6.9}
\]

The splice meets the linear overlap requirement with room to spare.

### 6.3 Distinct support remains open

Every deep occurrence maps to its old distinct matched superset:

\[
A_{\alpha,i}^{(q)}\subseteq A_{\alpha,i}^{(H)}.
\]

A fixed rank-\((m-q)\) set has at most

\[
\binom{m+q}{q-H}
\]

rank-\((m-H)\) supersets. Hence the imported matching gives only

\[
\boxed{
D_q\ge
\left\lceil
\frac{W-u_0}{\binom{m+q}{q-H}}
\right\rceil.}
\tag{6.10}
\]

At \(q=H+1\), this is only order \(W/m\), whereas

\[
\binom{2m}{m-H-1}=(1-o(1))W.
\]

Thus neither the old matching nor the U7 carrier splice proves
\(L_1=o(W)\), let alone \(L_1+L_2=o(W)\). The braid supplies witness
sharing and overlap, not missing owner values.

---

## 7. Final boundary

### Passed

- Exact principal and repaired lengths.
- Literal suffix endpoints at useful-prefix seams.
- Verified set-level ownership.
- Macro state, root, ownership, and total-surplus formulas.
- Cyclic recoding and the exact cut witness.
- Fixed-rank endpoint floor and recoding-invariant overlap trilemma.
- Independently proved cyclic-strip multipin analogue, exact length, and
  exact overlap.

### Required scope repairs

- Scalar counts require an actual disjoint ownership partition.
- Standalone macros and cuts of the inherited-tail walk are different
  realizations, though seam replacement relates their ledgers exactly.
- New asymmetric rows are occurrence catalogs until cross-strip
  distinctness is proved.
- Linear overlap requires full or near-complete next-row support.

### Still unproved

\[
L_1+L_2=o(W),
\]

or any comparable near-surjective support theorem outside the verified
band. This is the exact remaining obstruction. The cyclic-strip analogue
solves the same kind of witness sharing after recoding, but the U7 theorem
itself supplies no Boolean owner allocation here.
