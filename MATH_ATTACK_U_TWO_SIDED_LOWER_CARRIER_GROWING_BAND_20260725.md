# Lane U: two-sided lower carriers and a target-distinct growing band

Date: 2026-07-25

## 0. Outcome and exact boundary

Put

\[
 k=2m,\qquad W=\binom{2m}{m},\qquad
 L=\log m,\qquad \lambda=\log L.
\]

This report separates two statements which must not be conflated.

1. Deepening the carriers of a **frozen** radius-
   \(H\) strip matching creates many occurrences but does not certify many
   distinct deeper targets.  A run-endpoint theorem below shows that sparse
   seams can add at most linearly many distinct same-rank targets beyond the
   frozen carrier catalogue.

2. If the strips are reselected in one asymmetric hypergraph containing all
   desired deeper rows, the support issue is solved at the matching stage.
   For every integer function \(R=R(m)\) satisfying

   \[
   R\longrightarrow\infty,
   \qquad
   \frac{R^2\log\log m}{\log m}\longrightarrow0,
   \tag{0.1}
   \]

   there is an integral, literal contiguous-OR word covering every target in

   \[
   \boxed{m-2R,m-2R+1,\ldots,m+R}
   \tag{0.2}
   \]

   and having length

   \[
   \boxed{
   n\le W\left(
       1+(96+o(1))\frac{R^2\log\log m}{\log m}
       +L^{-9}
       \right)
   =W+o(W).}
   \tag{0.3}
   \]

The letters of the selected-strip part all lie in the deepest lower rank
\(m-2R\).  An old depth-\(R\) target is the OR of \(R+1\) consecutive such
letters, with its two endpoint letters deficient in opposite sets of exactly
\(R\) active coordinates.  This is a genuine two-sided multipin replacement,
not a one-pin occurrence count.

The result is a coefficient-one **growing central-band theorem**.  It does not
cover the tails of the Boolean lattice, and no full-cube constant-one theorem
is claimed.

All constructions below are integral.  Matching disjointness counts distinct
target masks, not occurrences.  Every repair is appended as its literal mask.

---

## 1. Cyclic strips and the asymmetric target hypergraph

Fix \(R\) satisfying (0.1), and define the integers

\[
 \ell=\left\lfloor\frac{L}{64R\lambda}\right\rfloor,
 \qquad s=2\ell.
 \tag{1.1}
\]

Then

\[
 \frac{\ell}{R}\longrightarrow\infty,
 \qquad
 \ell R=(1+o(1))\frac{L}{64\lambda}.
 \tag{1.2}
\]

In particular, for all sufficiently large \(m\),

\[
 2R<\ell<m.
 \tag{1.3}
\]

Choose disjoint sets \(C,D\subset[2m]\), each of size \(m-\ell\), and
write the remaining \(2\ell\) coordinates in an unoriented cyclic order

\[
 \gamma=(z_0,z_1,\ldots,z_{s-1}).
\]

For indices modulo \(s\), put

\[
 I_\gamma(i,h)=\{z_i,z_{i+1},\ldots,z_{i+h-1}\}.
\]

The asymmetric strip belonging to \((C,D,\gamma)\) contains the following
\(s\) targets in each displayed row:

\[
 T^-_{q,i}=C\cup I_\gamma(i+q,\ell-q),
 \qquad 0\le q\le2R,
 \tag{1.4}
\]

and

\[
 T^+_{q,i}=C\cup I_\gamma(i-q,\ell+q),
 \qquad 1\le q\le R.
 \tag{1.5}
\]

Thus \(|T^-_{q,i}|=m-q\) and \(|T^+_{q,i}|=m+q\).

Let \(\mathcal G_R\) be the multipartite hypergraph whose vertex parts are

\[
 \binom{[2m]}{m-q}\quad(0\le q\le2R),
 \qquad
 \binom{[2m]}{m+q}\quad(1\le q\le R),
 \tag{1.6}
\]

and whose edges are the complete asymmetric strips (1.4)--(1.5).
Its exact uniformity is

\[
 \kappa=s(3R+1)=2\ell(3R+1)
       =\left(\frac3{32}+o(1)\right)\frac{L}{\lambda}.
 \tag{1.7}
\]

### Lemma 1.1 — the hypergraph is ordinary

For all sufficiently large \(m\), a hyperedge of \(\mathcal G_R\) uniquely
determines \(C,D\), and the unoriented cycle \(\gamma\).  In particular,
there are no parallel edges.

#### Proof

Use the lowest lower row \(q=2R\).  Its active cyclic intervals have length

\[
 a=\ell-2R\ge2,
 \qquad a<\ell=s/2.
\]

The intersection of its \(s\) targets is exactly \(C\), and their union is
\(C\cup([2m]\setminus(C\cup D))\); hence the row recovers both \(C\) and
\(D\).  After deleting \(C\), two adjacent active coordinates occur together
in exactly \(a-1\) of the cyclic \(a\)-intervals.  A nonadjacent pair occurs
together in at most \(a-2\) such intervals, because \(a<s/2\).  The pairs of
maximum co-occurrence therefore recover the edges of the undirected cycle.
This recovers \(\gamma\) up to the reversal already identified in its
definition. \(\square\)

### Lemma 1.2 — exact degrees and codegree bound

The exact number of hyperedges is

\[
 |E(\mathcal G_R)|
 =\frac{(2m)!}{4\ell(m-\ell)!^2}.
 \tag{1.8}
\]

Every target in rank \(m\pm q\) has degree

\[
 \boxed{
 D_q=\frac{(m+q)!(m-q)!}{2(m-\ell)!^2}.}
 \tag{1.9}
\]

Consequently the minimum degree is \(D_0\), the maximum degree is
\(D=D_{2R}\), and

\[
 \frac D{D_0}=\exp\!\left(O(R^2/m)\right)=1+o(1),
 \qquad
 \log D=(2+o(1))\ell L.
 \tag{1.10}
\]

If \(\Gamma\) is the maximum pair-codegree, then

\[
 \boxed{
 \frac\Gamma D\le\frac{2\ell}{m-2R}.}
 \tag{1.11}
\]

#### Proof

There are

\[
 \binom{2m}{m-\ell}
 \binom{m+\ell}{m-\ell}
 \frac{(2\ell-1)!}{2}
 =\frac{(2m)!}{4\ell(m-\ell)!^2}
\]

choices of \((C,D,\gamma)\), proving (1.8).  Each edge contains exactly
\(s=2\ell\) vertices in each rank part.  Double-counting incidences in a
rank of size \(\binom{2m}{m-q}\) gives (1.9).  The ratios

\[
 \frac{D_{q+1}}{D_q}=\frac{m+q+1}{m-q}
\]

give the extrema and the first estimate in (1.10); the second follows by
expanding the two factorial quotients over \(m-\ell+1,\ldots,m\).

For (1.11), fix distinct vertices \(X,Y\).  The stabilizer of \(X\) has an
orbit on \(Y\) of size

\[
 \binom{|X|}{|X\cap Y|}
 \binom{2m-|X|}{|Y\setminus X|}.
 \tag{1.12}
\]

Every nontrivial such orbit has size at least \(m-2R\).  An orbit of size
one would force \(Y\in\{\varnothing,X,X^c,[2m]\}\).  The first and last
lie outside the selected ranks, \(Y=X\) is excluded, and \(X^c\) cannot
co-occur with \(X\) in one strip because all strip targets contain the
nonempty core \(C\).  Every edge through \(X\) contains at most \(2\ell\)
vertices in the rank of \(Y\).  Orbit double-counting, followed by
\(D_X\le D\), proves (1.11). \(\square\)

---

## 2. A target-disjoint asymmetric matching

We use the already audited near-regular matching theorem in the following
form.  For an ordinary \(\kappa\)-uniform hypergraph of maximum degree
\(D\), maximum pair-codegree at most \(C_*\), and minimum degree at least

\[
 D-f(D),\qquad
 f(D)=20(D^2C_*\log D)^{1/3},
\]

if

\[
 \kappa>4,
 \quad \kappa\le\tfrac12\log D,
 \quad f(D)\le D/10,
 \quad e^{2\kappa}C_*\log D=o(D),
 \tag{2.1}
\]

then there is a matching leaving

\[
 O\!\left(
 \kappa
 \left(\frac{C_*\log(1+C_*)}{D}\right)^{1/(\kappa-1)}
 |V|
 \right)
 \tag{2.2}
\]

vertices uncovered.

### Theorem 2.1 — asymmetric target-disjoint strip matching

For all sufficiently large \(m\), \(\mathcal G_R\) has a matching whose
total number \(U\) of uncovered vertices in all \(3R+1\) parts satisfies

\[
 \boxed{U\le W L^{-9}.}
 \tag{2.3}
\]

#### Proof

Take

\[
 C_*=\left\lceil\frac{2\ell D}{m-2R}\right\rceil,
 \qquad
 \eta=\frac{C_*\log(1+C_*)}{D}.
 \tag{2.4}
\]

Lemma 1.2 gives \(\Gamma\le C_*\).  Equations (1.1), (1.7), and (1.10)
give

\[
 \kappa=o(\log D),
 \qquad
 \frac{f(D)}D
 =\Theta\!\left(\left(\frac{\ell^2L}{m}\right)^{1/3}\right)=o(1).
 \tag{2.5}
\]

Here the two-sided estimate follows from

\[
 \frac{C_*}{D}=(2+o(1))\frac{\ell}{m},
 \qquad
 \log D=(2+o(1))\ell L;
\]

the ceiling in (2.4) is negligible because \(D\) grows faster than every
fixed power of \(m\).

The relative degree defect is \(O(R^2/m)\), which is

\[
 o\!\left(\left(\frac{\ell^2L}{m}\right)^{1/3}\right);
 \tag{2.6}
\]

hence every degree is at least \(D-f(D)\) eventually.  Also

\[
 \log\!\left(
 e^{2\kappa}\frac{C_*\log D}{D}
 \right)
 \le -L+2\kappa+O(\lambda)
 =-L+o(L).
 \tag{2.7}
\]

Thus all conditions in (2.1) hold for large \(m\).

Moreover,

\[
 \eta=O\!\left(\frac{\ell^2L}{m}\right),
 \qquad
 \log\eta\le-L+O(\lambda).
 \tag{2.8}
\]

Together with (1.7), this yields

\[
 \eta^{1/(\kappa-1)}
 \le L^{-32/3+o(1)}.
 \tag{2.9}
\]

Every selected rank has at most \(W\) vertices, so

\[
 |V(\mathcal G_R)|\le(3R+1)W.
 \tag{2.10}
\]

Since (0.1) implies \(R\le\sqrt{L/\lambda}\) eventually, substitution in
(2.2) gives

\[
 U
 \le W L^{-55/6+o(1)}
 \le W L^{-9}
 \tag{2.11}
\]

for all sufficiently large \(m\). \(\square\)

The matching is vertex-disjoint in the multipartite hypergraph.  Therefore
it certifies distinct masks in every selected row; this is stronger than
counting repeated occurrences in different strips.

---

## 3. The literal two-sided lower-carrier word

For one matched strip define its deepest lower carriers

\[
 F_i=C\cup I_\gamma(i+2R,\ell-2R),
 \qquad i\in\mathbb Z_s.
 \tag{3.1}
\]

These are nonempty masks of rank \(m-2R\).  Linearize the cyclic carrier
order by the exact word

\[
 \boxed{
 F_0,F_1,\ldots,F_{s-1},F_0,F_1,\ldots,F_{3R-1}.}
 \tag{3.2}
\]

It has length exactly \(s+3R\).

### Lemma 3.1 — exact carrier windows

For \(1\le t\le3R+1\), the OR of the \(t\) consecutive cyclic carriers
ending at index \(i\) is

\[
 \boxed{
 \bigvee_{j=i-t+1}^{i}F_j
 =C\cup I_\gamma(i-t+1+2R,\ell-2R+t-1).}
 \tag{3.3}
\]

Consequently:

* for every \(0\le q\le2R\), taking \(t=2R-q+1\) gives

  \[
  \bigvee_{j=i-2R+q}^{i}F_j
  =T^-_{q,i};
  \tag{3.4}
  \]

* for every \(1\le q\le R\), taking \(t=2R+q+1\) gives

  \[
  \bigvee_{j=i-2R-q}^{i}F_j
  =T^+_{q,i}.
  \tag{3.5}
  \]

The repeated prefix in (3.2) is exactly long enough to realize all \(s\)
cyclic windows in (3.4)--(3.5) as literal intervals.

#### Proof

Consecutive active intervals in the carriers start one coordinate apart.
Their union starts at the first start and ends at the last endpoint, which
is (3.3).  Its maximum active length is \(\ell+R<2\ell\), so no saturation
or duplicate-coordinate correction is hidden.  Substituting the two values
of \(t\) gives (3.4)--(3.5).  The largest window length is \(3R+1\), so a
linearization of one cycle requires and receives exactly its first \(3R\)
carriers again. \(\square\)

### Lemma 3.2 — fixed-order optimality

Among words which retain the cyclic \(+1\) carrier order (allowing a repeated
prefix) and use no foreign letters inside the module, \(s+3R\) is the
minimum length which exposes all \(s\) designated upper depth-\(R\) targets.

#### Proof

Before saturation, a run of \(t\) consecutive carriers has rank

\[
 m-2R+t-1.
\]

It has rank \(m+R\) exactly when \(t=3R+1\).  Longer runs add active
coordinates and therefore cannot represent a rank-\((m+R)\) target.  A
linear word of length \(N\) has at most \(N-(3R+1)+1=N-3R\) windows of
length \(3R+1\).  The \(s\) designated targets are distinct inside one
strip, so \(N-3R\ge s\).  Hence \(N\ge s+3R\), with equality in (3.2).
\(\square\)

### Theorem 3.3 — exact target-distinct growing-band word

Let the matching in Theorem 2.1 contain \(p\) strips.  Put

\[
 N_q=\binom{2m}{m-q},
 \qquad
 u_0=W-sp,
 \tag{3.6}
\]

and, for the nonmiddle selected parts,

\[
 u_q^-=N_q-sp\quad(1\le q\le2R),
 \qquad
 u_q^+=N_q-sp\quad(1\le q\le R).
 \tag{3.7}
\]

Then

\[
 U=u_0+\sum_{q=1}^{2R}u_q^-
       +\sum_{q=1}^{R}u_q^+.
 \tag{3.8}
\]

Concatenate (3.2) for all matched strips and then append, once each, every
vertex not covered by the matching in the parts (1.6).  The resulting
literal word covers every target in (0.2) and has exact length

\[
 \boxed{
 n=p(s+3R)+U
   =W+(U-u_0)+3Rp.}
 \tag{3.9}
\]

Moreover,

\[
 \frac{3Rp}{W}
 =\frac{3R}{2\ell}\left(1-\frac{u_0}{W}\right)
 \le(96+o(1))\frac{R^2\lambda}{L}=o(1),
 \tag{3.10}
\]

so (0.3) follows.

#### Proof

A matched hyperedge supplies \(s\) distinct designated targets in every
part.  Different matched hyperedges are vertex-disjoint, so the certified
support in each part has size exactly \(sp\).  Lemma 3.1 realizes every one
of those targets inside its own carrier module.  Appending the set-theoretic
complement of that certified support covers every remaining target literally.
This proves coverage and (3.8).  Since \(sp=W-u_0\), the exact word length is
(3.9).  Theorem 2.1 and (1.1) give (3.10). \(\square\)

The word may accidentally realize further targets at module seams.  They are
not credited in (3.9): the repair list is the literal complement of the
certified matching support.  Thus no occurrence is silently promoted to a
distinct owner.

### Corollary 3.4 — the requested two-sided replacement

Let

\[
 A_i^{(R)}=C\cup I_\gamma(i+R,\ell-R)
\]

be the old depth-\(R\) lower target.  Then

\[
 \boxed{
 A_i^{(R)}=F_{i-R}\vee F_{i-R+1}\vee\cdots\vee F_i.}
 \tag{3.11}
\]

The left endpoint \(F_{i-R}\) misses exactly the last \(R\) active
coordinates of \(A_i^{(R)}\), while the right endpoint \(F_i\) misses
exactly its first \(R\) active coordinates.  The intermediate \(R-1\)
carriers fill the gap.  More generally,

\[
 T^-_{R+j,i}
 =F_{i-R+j}\vee\cdots\vee F_i,
 \qquad 0\le j\le R.
 \tag{3.12}
\]

Thus the replacement is genuinely multipin and two-sided.  It evades any
lower bound whose hypothesis requires one carrier, one endpoint, or a
bounded number of endpoint pins to own the target.

---

## 4. Exact capacity reconciliation

The deepest part is smaller than the middle part.  This causes an unavoidable
leave, but it is much smaller than the residual allowed in Theorem 2.1.

Put

\[
 \delta=N_{2R}-sp\ge0
 \tag{4.1}
\]

and

\[
 A_R=
 \sum_{q=1}^{2R}(N_q-N_{2R})
 +\sum_{q=1}^{R}(N_q-N_{2R}).
 \tag{4.2}
\]

Then the leave identities are exactly

\[
 \boxed{
 u_0=W-N_{2R}+\delta,}
 \tag{4.3}
\]

\[
 \boxed{
 U-u_0=A_R+3R\delta,}
 \tag{4.4}
\]

and

\[
 \boxed{
 U=(W-N_{2R})+A_R+(3R+1)\delta.}
 \tag{4.5}
\]

For \(R\to\infty\), \(R=o(\sqrt m)\), the central binomial ratios give

\[
 W-N_{2R}=(4+o(1))\frac{R^2}{m}W,
 \qquad
 A_R=(9+o(1))\frac{R^3}{m}W.
 \tag{4.6}
\]

Indeed, uniformly for \(0\le q\le2R\),

\[
 \log\frac{N_q}{W}
 =\sum_{j=1}^{q}\log\frac{m-j+1}{m+j}
 =-\frac{q^2}{m}+O\!\left(\frac{q^3}{m^2}\right),
\]

and hence

\[
 \frac{N_q}{W}
 =1-\frac{q^2}{m}+O\!\left(\frac{R^4}{m^2}\right).
 \tag{4.7}
\]

The first formula in (4.6) follows by taking \(q=2R\).  For the second,
the coefficient of \(W/m\) in (4.2) is

\[
 \sum_{q=1}^{2R}(4R^2-q^2)
 +\sum_{q=1}^{R}(4R^2-q^2)
 =9R^3-\frac52R^2-\frac12R.
\]

The accumulated error is \(O(R^5W/m^2)=o(R^3W/m)\), proving the constant
\(9\).

In the present polylogarithmic range these terms are \(o(WL^{-9})\).
Combining (4.5) with Theorem 2.1 also forces

\[
 \delta\le\frac{WL^{-9}}{3R+1}.
 \tag{4.8}
\]

Thus the asymmetric matching has the stronger bottom accuracy needed for
literal append-repair.  Merely asserting a target-disjoint family, without
the quantitative residual (2.3), would not have been sufficient.

---

## 5. What a frozen carrier family cannot certify

The next theorem rigorously separates distinct target support from
occurrence multiplicity.

### Theorem 5.1 — run-endpoint support bound

Fix an integer carrier depth \(a<\ell\), and canonical carriers

\[
 F_{\alpha,i}=C_\alpha\cup
 I_{\gamma_\alpha}(i+a,\ell-a).
 \]

Fix a lower row \(0\le q\le a\), put \(c=a-q\), and let
\(\mathcal D_q\) be the set of distinct canonical row-\(q\) values

\[
 C_\alpha\cup I_{\gamma_\alpha}(i+q,\ell-q)
\]

in the frozen catalogue.  Let \(D_q=|\mathcal D_q|\).

Consider any word whose nonexceptional positions are canonical carriers and
which decomposes into \(J\) maximal runs in which the indices of one fixed
strip advance cyclically by \(+1\).  Let \(B\) be the number of arbitrary
exceptional or bridge positions.  If \(Q_q\) is the number of distinct
rank-\((m-q)\) masks represented by arbitrary contiguous OR intervals of the
word, then

\[
 \boxed{Q_q\le D_q+B+cJ.}
 \tag{5.1}
\]

#### Proof

Choose one witness for each distinct rank-\((m-q)\) target and charge it to
its right endpoint.  For a fixed right endpoint, ORs of intervals ending
there form an inclusion chain as the left endpoint moves left.  Two distinct
members of that chain cannot have the same rank.  Hence the endpoint charge
is injective on distinct rank-\((m-q)\) targets.

Suppose a witness for a target outside \(\mathcal D_q\) ends at a
nonexceptional carrier at least \(c+1\) positions into its current run.  Its
last \(c+1\) carriers have OR equal to the canonical row-\(q\) value at that
endpoint.  This suffix OR is contained in the full witness OR, and both have
rank \(m-q\); therefore they are equal, a contradiction.  Every target
outside \(\mathcal D_q\) must consequently end either at one of the \(B\)
exceptional positions or among the first \(c\) carriers of one of the
\(J\) runs.  Endpoint injectivity proves (5.1). \(\square\)

At the physical carrier rank \(q=a\), (5.1) becomes

\[
 Q_a\le D_a+B.
 \tag{5.2}
\]

Thus cross-strip joins add no new same-rank support unless a new physical
position is paid.  More generally, if \(B+aJ=o(W)\), sparse seams add only
\(o(W)\) distinct lower targets beyond the frozen catalogue, even if the
word has long witnesses crossing many seams.

The construction in Sections 1--3 escapes this obstruction exactly where it
must: the fresh matching already supplies \(sp\) distinct owners at the
bottom carrier rank, and all remaining bottom targets are literal repairs.
The carrier joins are used for multipin witnessing, not for manufacturing
uncertified support.

For comparison, suppose only an old depth-\(H\) target-disjoint strip family
is frozen, and let \(0\le j<\ell-H\).  A depth-\((H+j)\) value which occurs
in \(t\) strips produces
\(t(j+1)\) distinct old depth-\(H\) supersets.  Since it has only

\[
 \binom{m+H+j}{j}
\]

such supersets, its occurrence multiplicity is at most that quantity divided
by \(j+1\).  Hence \(W-u_0\) deeper occurrences imply only the weak support
bound

\[
 \boxed{
 D_{H+j}^{\rm distinct}\ge
 \left\lceil
 \frac{(j+1)(W-u_0)}{\binom{m+H+j}{j}}
 \right\rceil.}
 \tag{5.3}
\]

This is why deepening a frozen matching is not the proof of Theorem 2.1.

---

## 6. Odd-dimensional band transfer

Let \(A=(a_1,\ldots,a_n)\) be the even-dimensional word from Theorem 3.3,
and add a new coordinate \(x\).  The literal word

\[
 A,\ \{x\},\ \{x\}\cup a_1,\ldots,\{x\}\cup a_{n-1}
 \tag{6.1}
\]

has length exactly \(2n\).  If an even target has a witness ending before
\(a_n\), use its lifted copy; if its chosen witness ends at \(a_n\), append
the intervening singleton \(\{x\}\).  Therefore (6.1) covers every odd
rank

\[
 m-2R+1\le r\le m+R.
 \tag{6.2}
\]

Since

\[
 W_{2m+1}=\binom{2m+1}{m}=\frac{2m+1}{m+1}W,
\]

the exact length identity is

\[
 2n=W_{2m+1}+\frac{W}{m+1}+2(n-W)
     =W_{2m+1}+o(W_{2m+1}).
 \tag{6.3}
\]

This transfers the growing-band theorem, not a full-cube conclusion.

---

## 7. Independent audit and final scope

### 7.1 One-shot architecture ceiling

The achieved depth is near the limit of this particular full-row ABKV plus
fixed-carrier-module architecture.  If such a matching leaves \(o(W)\)
middle vertices, then

\[
 p=(1-o(1))\frac{W}{2\ell}.
\]

The exact module overhead \(3Rp=o(W)\) therefore forces

\[
 \frac{R}{\ell}\longrightarrow0.
 \tag{7.1}
\]

There is also an unavoidable codegree.  Fix a middle target \(X\).  Every
strip through \(X\) contains exactly two immediate rank-\((m+1)\)
supertargets of \(X\).  The stabilizer of \(X\) is transitive on its \(m\)
immediate supertargets, so

\[
 \Gamma\ge\frac{2D_0}{m}=(2-o(1))\frac Dm.
 \tag{7.2}
\]

If the same one-shot hypergraph is certified through the matching
hypothesis \(e^{2\kappa}\Gamma\log D=o(D)\), then, since
\(\kappa=(6+o(1))\ell R\),

\[
 12\ell R\le(1+o(1))L.
 \tag{7.3}
\]

Combining (7.1) and (7.3) gives

\[
 \boxed{R=o(\sqrt{\log m}).}
 \tag{7.4}
\]

This is only a certification ceiling for one full-row strip hypergraph
followed by the fixed cyclic carrier module.  It does not obstruct a
multiscale matching, a dense dynamic braid, or a different global
trajectory.  The proved range \(R^2\log\log m=o(\log m)\) is within a
\(\sqrt{\log\log m}\) factor of this scoped ceiling.

### 7.2 Audit verdict

The two decisive points were independently audited.

1. **Asymmetric ABKV application: PASS.**  The bottom row recovers the
   strip, so the hypergraph is ordinary.  The exact degrees, near-regular
   defect, stabilizer-orbit codegree bound, growing uniformity, exponential
   codegree hypothesis, and residual exponent \(-32/3\) all check.  The
   exact capacity identity (4.5) is consistent with (2.3) and forces the
   stronger bottom leave (4.8).

2. **Literal carrier transfer: PASS.**  The module must repeat exactly
   \(3R\) carriers, not \(3R+1\).  Its longest desired witness has length
   \(3R+1\), and formulas (3.3)--(3.5) expose every certified row needed
   here.  No additional occurrence is credited.  The endpoint-support
   obstruction leaves no hidden
   gap because support is supplied by the fresh matching and repairs.

The proved theorem closes the distinct-support gate for a growing
polylogarithmic central band and gives a literal two-sided multipin carrier
braid of width \(W+o(W)\).  It does not show how to cover ranks outside
(0.2) with total additional cost \(o(W)\).  That tail/global-fusion step is
the exact remaining boundary before this lane can imply the full
constant-one theorem.
