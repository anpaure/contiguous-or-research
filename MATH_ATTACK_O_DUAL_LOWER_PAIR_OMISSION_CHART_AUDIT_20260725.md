# O: dual lower pair-omission interval charts — exact construction and same-core audit

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad
 W=\binom{2m+1}{m},\qquad
 T=\binom{2m+1}{m-1},\qquad
 d=W-T=\frac{2W}{m+2}.
\tag{0.1}
\]

The duality question has two different answers, depending on whether
"dual" means a same-core history change or a bulk lossless interval chart.

1. **Same-core pure lower chart.**  There is an exact contained-pair
   conjugation which fixes every lower root, every middle owner, and every
   upper flag.  Its token innovation is

   \[
   \ell_{i,q}^-=\mathbf e_{\sigma L_q(i)}-\mathbf e_{L_q(i)},
   \qquad \ell_{i,q}^+=0,
   \tag{0.2}
   \]

   and its lower Gram is the exact positive mirror of the audited upper
   partner-pair Gram:

   \[
   \boxed{
   \left\langle
   \mathbf e_{\sigma R}-\mathbf e_R,
   \mathbf e_{\sigma R'}-\mathbf e_{R'}
   \right\rangle
   =2\mathbf1_{\{R=R',\ D\nsubseteq R\}}\ge0.}
   \tag{0.3}
   \]

   It combines with the upper adjacent-pair chart on the same middle
   matching; the mixed commutator and every upper/lower cross-Gram entry
   are zero.  Its completed literal length is

   \[
   \boxed{
   L\le W+2H\left(J+2r_++2r_-+d\right),}
   \tag{0.4}
   \]

   so (J,r_+,r_-=O(W/m)) and (H=o(m)) give (W+o(W)), with no
   second leading core.

   This chart is, however, only a collar chart.  On a physical block
   (I=[a,b]),

   \[
   \boxed{
   z_{I,q}^-
   =\sum_{i=\max\{a,b-q+2\}}^b
     \left(\mathbf e_{\sigma L_q(i)}-\mathbf e_{L_q(i)}\right).}
   \tag{0.5}
   \]

   Thus a block of arbitrary length changes at most (q-1) depth-(q)
   occurrences.  A catalogue with (o(W/H)) history blocks moves only
   (o(W)) occurrences at every (q\le H).  It is not the missing bulk
   lower atlas.

2. **Bulk lossless lower chart.**  Global complementation gives a complete
   exact dual of the upper adjacent interval chart.  It changes first-
   avoided priority into first-contained priority and shifts the central
   incidence

   \[
   S^{m-1}\subset Y^m
   \quad\longmapsto\quad
   cY^{m+1}\subset cS^{m+2}.
   \tag{0.6}
   \]

   On the changed top roots it has exact lower innovations

   \[
   \boxed{
   \Delta_{R,q}^-
   =\mathbf e_{\theta(cU_{q+1}(cR))}
      -\mathbf e_{cU_{q+1}(cR)},
   \qquad 1\le q\le H,}
   \tag{0.7}
   \]

   with zero positive-depth top-upper flag innovation.  (Its
   rank-\((m+1)\) central owner is the matching endpoint and does change.)
   Its interval Gram is entrywise
   nonnegative and packetization is lossless.  A (t)-owner dual interval
   through global lower depth (H) has the exact literal word length

   \[
   \boxed{t+2H+2.}
   \tag{0.8}
   \]

   A completed dual corner has

   \[
   \boxed{
   L_\vee=W+2(H+1)(C+d)=W+o(W)}
   \tag{0.9}
   \]

   for \(H\le m-3\) and \(H=o(m/\log^2m)\), in particular throughout
   every fixed Gaussian window for all sufficiently large \(m\).

   This bulk dual is a **separate top-centred core**.  Complementation is
   not an OR-word automorphism, and the owners in (0.6) lie at rank
   (m+1), not rank (m).  Concatenating the already literal upper and
   dual words therefore costs (2W+o(W)).  No theorem below fuses their
   (W) principal positions.

3. **Complement/reversal does not repair the gap.**  Local complementation
   in a (2m-1)-coordinate row sends a predecessor token to a distinct
   successor token.  Reversal turns this into a legal threshold path, but
   its exact lower displacement telescopes to the two endpoint collars:

   \[
   z_{K,q}^-=E_{m-q}(K)-E_{m-q}(K+q-1),
   \tag{0.10}
   \]

   and at depth two

   \[
   \boxed{
   z_{[a,b],2}^-
   =\mathbf e_{I_\pi(a,m-2)}
    -\mathbf e_{I_\pi(b+1,m-2)}.}
   \tag{0.11}
   \]

   The reverse chart changes the middle leave and has nonzero upper
   collateral; it is not the pure bulk dual.

Consequently the exact answer to the assigned question is:

> The lower chart can be put on the same token word and middle matching
> only in collar-local form.  The lossless bulk complement dual requires a
> separate shifted core.  Formal complementation of the (q\ge2) upper
> layer is algebraically and floor-exact, but it does not combine with the
> upper word without doubling the leading length.  A nonlocal shared-core
> rebundling theorem remains unproved.

No constant-one conclusion is claimed.

## 1. Bottom token convention and the audited upper chart

Fix disjoint coordinate pairs (P_1,\ldots,P_m) and one unpaired
coordinate.  Let

\[
 A=P_j,\qquad B=P_{j+1},
\]

and let \(\theta\) exchange (A) and (B) coordinatewise.  Put

\[
 Q_A=[n]\setminus A,\qquad |Q_A|=2m-1,
\]

choose an exact local factor (F_A) on (Q_A), and set

\[
 F_B=\theta F_A.
\tag{1.1}
\]

For a row

\[
 \pi=(x_0,\ldots,x_{2m-2})
\]

write, with cyclic indices,

\[
 S_i=I_\pi(i,m-1),\qquad
 X_i=I_\pi(i,m),\qquad
 Y_i=X_{i-1}=I_\pi(i-1,m).
\tag{1.2}
\]

The predecessor token is

\[
 e_A(i)=(S_i,Y_i),
\tag{1.3}
\]

with canonical flags

\[
 L_q(i)=I_\pi(i+q-1,m-q),
 \qquad
 U_q(i)=I_\pi(i-1,m+q).
\tag{1.4}
\]

When a depth-zero convention is needed below, set
\(L_0(i)=U_0(i)=Y_i\); then the same displayed interval formulas remain
valid at \(q=0\).

The changed roots of the adjacent priority exchange are exactly

\[
\mathcal D_j=\left\{
 S\in\binom{[n]}{m-1}:
 S\cap(A\cup B)=\varnothing,
 \ S\cap P_h\ne\varnothing\ (h<j)
 \right\}.
\tag{1.5}
\]

For (S\in\mathcal D_j), \(\theta S=S\) pointwise and the two upper-chart
tokens are (e_A(S)) and \(\theta e_A(S)).  Their lower flags agree,
and their upper innovation is

\[
 d_{S,q}^+=\mathbf e_{\theta U_q(S)}-\mathbf e_{U_q(S)}.
\tag{1.6}
\]

The audited unit-vector identity is

\[
 \left\langle
 \mathbf e_{\theta U}-\mathbf e_U,
 \mathbf e_{\theta U'}-\mathbf e_{U'}
 \right\rangle
 =2\mathbf1_{\{U=U',\ U\cap B\ne\varnothing\}}.
\tag{1.7}
\]

The issue is that every lower innovation in this chart is zero.

## 2. An exact same-core pure lower chart

The correct same-core mirror exchanges two pairs already contained in the
lower root, rather than two pairs avoided by it.

Fix disjoint two-sets

\[
 C=\{c_0,c_1\},\qquad D=\{d_0,d_1\},
\]

and put

\[
 \sigma=(c_0\ d_0)(c_1\ d_1).
\tag{2.1}
\]

For a fixed window (H\le m-2), call a start (i) eligible when

\[
 C\subseteq L_H(i),\qquad D\subseteq S_i.
\tag{2.2}
\]

Since (L_H(i)\subseteq S_i), eligibility implies

\[
 C\cup D\subseteq S_i.
\tag{2.3}
\]

### Theorem 2.1 (parallel-edge lower history)

At an eligible start, the token in the conjugate row \(\sigma\pi\) has
the same central endpoints as the token in \(\pi\):

\[
 \sigma S_i=S_i,\qquad \sigma Y_i=Y_i.
\tag{2.4}
\]

Every upper flag is fixed, while the lower flags satisfy

\[
 L_q^{\sigma}(i)=\sigma L_q(i),
\qquad
 U_q^{\sigma}(i)=U_q(i)
\qquad(1\le q\le H).
\tag{2.5}
\]

Thus the exact signed innovation is (0.2).  Arbitrary history choices at
distinct central tokens preserve lower saturation and middle simplicity.

#### Proof

Both exchanged pairs lie in (S_i), so \(\sigma S_i=S_i\).  The unique
point (Y_i\setminus S_i\) is outside (C\cup D), giving
\(\sigma Y_i=Y_i\).  Every (U_q(i)) contains (S_i), hence contains
both complete pairs and is fixed by \(\sigma\).  Coordinate conjugation
gives (L_q^\sigma(i)=\sigma L_q(i)\).

Changing the history therefore changes neither endpoint of the central
edge.  Central matching legality is automatic, independently at every
distinct lower root.  The conjugate history is a row of the exact factor
\(\sigma F_A\); interval pieces chosen from it are literal OR pieces.  We
do not assert that \(\pi\) and \(\sigma\pi\) are two rows of the same fixed
factor. \(\square\)

### Lemma 2.2 (exact lower unit-vector identity)

If (R,R'\) both contain (C), then (0.3) holds.

#### Proof

Expanding the four unit-vector terms gives

\[
 2\mathbf1_{\{R=R'\}}
 -\mathbf1_{\{\sigma R=R'\}}
 -\mathbf1_{\{R=\sigma R'\}}.
\tag{2.6}
\]

If \(\sigma R=R'\), then (R'\) contains (C), while \(\sigma R\)
automatically contains (D).  Thus \(\sigma R\) contains both complete
pairs, is fixed by \(\sigma\), and (R=R').  The other cross equality is
identical.  On the diagonal the innovation vanishes exactly when
\(D\subseteq R\); otherwise its squared norm is two. \(\square\)

Because (C\subseteq L_H(i)\subseteq L_q(i)), the lemma applies at every
depth (q\le H).  Therefore, for arbitrary finite nonnegative weights,

\[
 \boxed{
 \langle \ell_i,\ell_k\rangle_w
 =2\sum_{q=1}^H w_q^-
 \mathbf1_{\{L_q(i)=L_q(k),\ D\nsubseteq L_q(i)\}}
 \ge0.}
\tag{2.7}
\]

This is the exact lower analogue of (1.7), including its factor two.

## 3. Exact same-core collar rigidity

The positive tokenwise Gram does not make the chart bulk-active.

### Lemma 3.1 (lower flags are endpoint intersections)

For every (q\ge1),

\[
 \boxed{
 L_q(i)=\bigcap_{h=0}^{q-1}S_{i+h}.}
\tag{3.1}
\]

#### Proof

The common position interval of

\[
 [i,i+m-2], [i+1,i+m-1],\ldots,
 [i+q-1,i+m+q-3]
\]

is ([i+q-1,i+m-2]), of length (m-q). \(\square\)

Let (I=[a,b]) be a consecutive block of eligible starts and switch all
its histories by \(\sigma\).  If (i+q-1\le b), then every root in the
intersection (3.1) is fixed by \(\sigma\), whence

\[
 \sigma L_q(i)=L_q(i).
\tag{3.2}
\]

Put

\[
 K_{I,q}=[\max\{a,b-q+2\},b].
\tag{3.3}
\]

Then (0.5) is exact.  Define

\[
 a_{I,q}=|\{i\in K_{I,q}:D\nsubseteq L_q(i)\}|.
\tag{3.4}
\]

Proper cyclic windows at distinct starts are distinct.  Equation (2.7)
therefore gives

\[
 \boxed{
 \|z_I\|_w^2
 =2\sum_{q=2}^H w_q^-a_{I,q}
 \le2\sum_{q=2}^H(q-1)w_q^-.}
\tag{3.5}
\]

In particular (z_{I,1}^-=0), as it must be because the lower roots are
fixed.  At depth two a block supplies at most one Johnson-edge direction.

More generally, if a same-core atlas has (C_\mathrm{hist}) physical
history blocks, it changes at most

\[
 (q-1)C_\mathrm{hist}
\tag{3.6}
\]

depth-(q) occurrences in this one-sided convention, and at most
(2qC_\mathrm{hist}) under a two-seam convention.  Hence

\[
 C_\mathrm{hist}=o(W/H)
 \quad\Longrightarrow\quad
 \#\{\text{movable depth-}q\text{ occurrences}\}=o(W)
\tag{3.7}
\]

uniformly for (q\le H).  Conversely, moving (\delta W) occurrences at
a Gaussian depth (q\asymp H) needs (\Omega_\delta(W/H)) blocks.  Under
the standard separately initialized \(2H\)-collar realization used here,
this costs \(\Omega(W)\) letters.  The occurrence lower bound is
unconditional for ordered-core parallel histories; the letter lower bound
does not exclude a future bridge theorem which shares resets between many
blocks.  This is the exact obstruction to using the currently certified
same-core parallel histories as the missing bulk lower chart.

## 4. Exact combination with the upper adjacent chart

Assume an upper chart uses the avoided pairs (A,B), and the lower chart
uses (C,D).  On their common carrier,

\[
 S_i\cap(A\cup B)=\varnothing,
 \qquad C\cup D\subseteq S_i.
\tag{4.1}
\]

Thus the supports of \(\theta\) and \(\sigma\) are disjoint and the two
involutions commute.  The upper chart fixes every lower flag.  The lower
chart fixes every upper flag, the old owner (Y_i), and the new owner
\(\theta Y_i\).  Consequently

\[
 \Phi(\theta\sigma e)-\Phi(\theta e)
 -\Phi(\sigma e)+\Phi(e)=0,
\tag{4.2}
\]

and

\[
 \boxed{
 \langle d^{\rm upper},d^{\rm lower}\rangle_w=0}
\tag{4.3}
\]

tokenwise and blockwise.  All four histories use whichever central edge is
chosen by the upper bit; central legality depends only on that upper bit.

This proves a genuine same-core product of one upper chart with one fixed
contained-pair collar chart.  It does not compute mutual Grams or run
refinements for a menu of many contained-pair swaps.  It also does not
prove endpoint energy-flatness for
the partial contained-pair chart: (2.7) gives the Gram sign and (4.3) the
mixed orthogonality, but the two coherent lower-history endpoints need not
have equal completed floor energy without an additional stratum symmetry.

### Exact run and word ledger

For fixed (C,D), eligibility (2.2) is the intersection of four circular
coordinate-membership arcs.  Its boundary has at most eight edges and it
has at most four circular components.  Intersecting it with one already
selected physical run produces at most five linear blocks.  Hence, if (J)
is the old run count and (r_-) the lower-history block count,

\[
 \boxed{r_-\le5J.}
\tag{4.4}
\]

Let (r_+) be the upper packet count.  Cut every selected source run at all
upper- and lower-bit boundaries.  Each interval bit contributes at most
two such boundaries, and every constant two-bit state segment is a literal
segment of exactly one of
\(\pi,\theta\pi,\sigma\pi,\theta\sigma\pi\).  The resulting common
refinement therefore has

\[
 \boxed{C'\le J+2r_++2r_-.}
\tag{4.5}
\]

A (t)-token tight history interval has the exact standard word length
(t+2H).  The selected core contains (T) tokens, and every one of the
(d) unused middle owners costs (1+2H) as an isolated component.
Summing gives (0.4).

Thus the collar chart really does combine with the upper layer without
doubling the leading length.  Here “same core” means the same central
incidences and the same \(T\) leading owner count in the chosen final word,
with separately initialized constant-history segments.  It does not mean
that one unreset queue substring simultaneously realizes all four
histories.  Its failure is quantitative lower action, not central legality
or chronology.

## 5. The exact bulk dual by global complement

Write (cR=[n]\setminus R).  Complement the entire bottom token:

\[
 e_A^\vee(i)=(cY_i,cS_i).
\tag{5.1}
\]

This is the incidence (0.6).  Define the first-contained category on
rank-((m+2)) roots by

\[
 \kappa^\vee(R)=\min\{h:P_h\subseteq R\}.
\tag{5.2}
\]

It is defined for every (R): a set containing at most one coordinate
from each of the (m) pairs, and perhaps the singleton, has size at most
(m+1).

### Theorem 5.1 (exact first-contained matching)

Assign each rank-((m+2)) root to the first pair it contains and take the
complemented token from that local factor.  Every root is used once and
all rank-((m+1)) owners are distinct.

#### Proof

If (j=\kappa^\vee(R)), then (cR) avoids (P_j) and meets every earlier
pair.  Exact first-avoided coverage supplies its unique bottom token.  The
complemented owner lies inside (R), contains (P_j), and contains no
earlier pair completely.  Owners in different categories are therefore
distinct.  Within one category, bottom owner injectivity and complementation
give distinct top owners. \(\square\)

The changed dual roots of the adjacent exchange are

\[
 \boxed{
 \mathcal D_j^\vee
 =\left\{R\in\binom{[n]}{m+2}:
 A\cup B\subseteq R,\quad
 P_h\nsubseteq R\ (h<j)
 \right\}
 =c\mathcal D_j.}
\tag{5.3}
\]

Their exact cardinality is

\[
 \boxed{
 |\mathcal D_j^\vee|
 =\sum_{\ell=0}^{j-1}(-1)^\ell\binom{j-1}{\ell}
 \binom{2m-3-2\ell}{m-2-2\ell}
 =\sum_{\ell=0}^{j-1}(-1)^\ell\binom{j-1}{\ell}
 \binom{2m-3-2\ell}{m-1}.}
\tag{5.4}
\]

For (R\in\mathcal D_j^\vee), \(\theta R=R\) setwise and the two token
alternatives are (e_A^\vee(R)) and \(\theta e_A^\vee(R)).

### Theorem 5.2 (independent-root and interval legality)

Choosing either alternative independently at every changed root, and
retaining all common tokens, gives an exact root-saturating, owner-simple
matching.  Hence the same is true when one bit is assigned to each maximal
physical interval.

#### Proof

Complement the chosen top edge family.  It becomes the audited independent
bottom cube on \(\mathcal D_j\), which is lower-saturating and middle-
simple.  Complementation is a bijection on both vertex parts and reverses
inclusion.  It therefore preserves matching legality. \(\square\)

## 6. Exact bulk lower innovations and cross-Gram

Put

\[
 s=i+m-1\pmod{2m-1}.
\tag{6.1}
\]

Then the top owner and root are

\[
 Z_s^A=A\cup I_\pi(s,m-1),
 \qquad
 R_s^A=A\cup I_\pi(s,m).
\tag{6.2}
\]

For (0\le p\le m-2), define the top-relative lower and upper flags

\[
 D_p^A(s)=A\cup I_\pi(s+p,m-1-p),
\tag{6.3}
\]

\[
 E_p^A(s)=A\cup I_\pi(s,m-1+p).
\tag{6.4}
\]

Direct complementation gives

\[
 \boxed{D_p^A(s)=cU_p(i),\qquad E_p^A(s)=cL_p(i).}
\tag{6.5}
\]

For every \(p\ge1\), \(E_p\) contains \(A\cup B\) on the changed domain
and is fixed by \(\theta\).  (The depth-zero set \(E_0=D_0=cY_i\) is the
rank-\((m+1)\) owner itself and generally changes; it is not an upper flag.)
The top-relative lower innovation is

\[
 (d_R^\vee)_{p}^-
 =\mathbf e_{\theta D_p(R)}-\mathbf e_{D_p(R)}.
\tag{6.6}
\]

The desired global lower rank (m-q) corresponds to

\[
 m+1-p=m-q
 \quad\Longleftrightarrow\quad
 p=q+1.
\tag{6.7}
\]

Thus (6.6) becomes the exact formula (0.7).  The one-step depth shift is
essential, and the range through global lower depth (H) requires

\[
 K=H+1\le m-2,
 \qquad\text{that is,}\qquad H\le m-3.
\tag{6.8}
\]

### Lemma 6.1 (bulk lower pair-swap identity)

If (D,D'\) both contain (A), then

\[
 \boxed{
 \left\langle
 \mathbf e_{\theta D}-\mathbf e_D,
 \mathbf e_{\theta D'}-\mathbf e_{D'}
 \right\rangle
 =2\mathbf1_{\{D=D',\ B\nsubseteq D\}}.}
\tag{6.9}
\]

#### Proof

Expansion gives two diagonal indicators minus the two mixed indicators.
If \(\theta D=D'\), then the common set contains (B) from the left and
(A) from the right.  It contains both complete pairs, is fixed by
\(\theta\), and lies on the diagonal.  The other mixed equality is the
same.  On the diagonal the innovation vanishes exactly when (B\subseteq
D\). \(\square\)

For global lower depths (1\le q\le H), put

\[
 G_q(R)=D_{q+1}(R)=cU_{q+1}(cR)
\tag{6.10}
\]

and

\[
 \lambda_{q,D}=|\{R\in\mathcal D_j^\vee:G_q(R)=D\}|.
\tag{6.11}
\]

For arbitrary finite nonnegative weights,

\[
 \boxed{
 \langle d_R^\vee,d_{R'}^\vee\rangle_w
 =2\sum_{q=1}^H w_q^-
 \mathbf1_{\{G_q(R)=G_q(R'),\ B\nsubseteq G_q(R)\}}
 \ge0.}
\tag{6.12}
\]

Distinct starts in one row give distinct proper (G_q)-windows, so a
maximal physical interval loses no variance.  If \(\mathfrak A_j^\vee\)
is the coherent endpoint square and \(\mathfrak V_j^\vee\) the sum of
the interval-column squares, then exactly

\[
 \boxed{
 \begin{aligned}
 \mathfrak A_j^\vee
 &=2\sum_{q=1}^H w_q^-
   \sum_{D:B\nsubseteq D}\lambda_{q,D}^2,\\
 \mathfrak V_j^\vee
 &=2\sum_{q=1}^H w_q^-
   \sum_{D:B\nsubseteq D}\lambda_{q,D},\\
 \mathfrak A_j^\vee-\mathfrak V_j^\vee
 &=2\sum_{q=1}^H w_q^-
   \sum_{D:B\nsubseteq D}\lambda_{q,D}(\lambda_{q,D}-1).
 \end{aligned}}
\tag{6.13}
\]

Fair independent interval bits therefore lower the average of the two
coherent endpoint quadratic energies by

\[
 \boxed{
 \frac12\sum_{q=1}^H w_q^-
 \sum_{D:B\nsubseteq D}\lambda_{q,D}(\lambda_{q,D}-1).}
\tag{6.14}
\]

The statement is exact for adjacent-integer factorial floor energies after
subtracting the rankwise corner-independent baseline.  Descent below a
specified completed endpoint still requires endpoint symmetry; (6.14)
itself is an endpoint-average identity.

## 7. Exact dual literal word and run cost

Take (K=H+1\) and define

\[
 C_r=A\cup I_\pi(r+K,m-1-K).
\tag{7.1}
\]

Every (C_r) has rank

\[
 |C_r|=m+1-K=m-H.
\tag{7.2}
\]

For (0\le p\le K), consecutive-window union gives

\[
 \boxed{
 D_p^A(s)=\bigcup_{r=s+p-K}^{s}C_r,}
\tag{7.3}
\]

\[
 \boxed{
 E_p^A(s)=\bigcup_{r=s-K}^{s+p}C_r.}
\tag{7.4}
\]

For a selected token interval (s\in[a,b]), emit

\[
 C_{a-K},C_{a-K+1},\ldots,C_{b+K}.
\tag{7.5}
\]

All witnesses in (7.3)--(7.4) lie inside this word, whose exact length is

\[
 (b+K)-(a-K)+1=(b-a+1)+2K=t+2H+2.
\tag{7.6}
\]

This proves (0.8) directly.  It is a sliding-core OR word, not a formal
complement of the bottom MTF word.

Let

\[
 R_m=\operatorname{Cat}_{m-1}
 =\frac1{2m-1}\binom{2m-1}{m-1}.
\tag{7.7}
\]

In one row, membership in \(\mathcal D_j^\vee\) has at most (4j)
boundary edges and at most (2j) circular components.  Therefore the
dual packet count is

\[
 \boxed{
 r_j^\vee\le\min\{2jR_m,|\mathcal D_j^\vee|\}.}
\tag{7.8}
\]

One corner has at most \(2r_j^\vee\) packet endpoints.  The complete
two-phase raw endpoint catalogue has at most \(4r_j^\vee\), hence

\[
 \boxed{
 E_{j,\mathrm{corner}}^\vee\le4jR_m,
 \qquad
 E_{j,\mathrm{catalog}}^\vee\le8jR_m.}
\tag{7.9}
\]

The exact comparison is

\[
 \frac{8jR_m}{W/H}
 =\frac{4jH(m+1)}{(2m-1)(2m+1)}.
\tag{7.10}
\]

Thus one chart has (o(W/H)) raw endpoints whenever (jH=o(m)).  The
first-contained tail is the complement of the first-avoided tail, so the
cumulative separate-chart menu satisfies

\[
 \boxed{
 \sum_{j=1}^{m-1}r_j^\vee
 =O\left(\frac{W\log^2m}{m}\right).}
\tag{7.11}
\]

This is a menu-size statement, not simultaneous product-cube legality for
all adjacent positions.

Let (C_0=O(W\log^2m/m)) be the run count of one coherent first-contained
endpoint.  Switching (r) packets gives

\[
 C\le C_0+2r=O(W\log^2m/m).
\tag{7.12}
\]

The top matching uses (T) owners and leaves (d) rank-((m+1)) owners.
Adding each unused owner as one isolated radius-(K) component and summing
(7.6) gives exactly

\[
 L_\vee
 =T+2KC+d(1+2K)
 =W+2(H+1)(C+d).
\tag{7.13}
\]

For (H=o(m/\log^2m)), this is (W+o(W)).  All constants in (0.8)--
(0.9) are therefore literal and exact.

## 8. Why local complement and reversal do not give the bulk chart on the old core

There are two complements in this problem.  Global complement produced
the valid shifted chart above.  Local complement in (Q_A) attempts to
return to the original central ranks, but changes the token carrier.

Write

\[
 \bar R=Q_A\setminus R,
 \qquad U_0(i)=Y_i.
\]

Since the complement of a cyclic interval is its opposite cyclic arc,

\[
 \boxed{
 \overline{L_q(i)}=U_{q-1}(i+m)
 \qquad(1\le q\le m-1),}
\tag{8.1}
\]

\[
 \boxed{
 \overline{U_q(i)}=L_{q+1}(i+m-1)
 \qquad(0\le q\le m-2).}
\tag{8.2}
\]

At the central edge,

\[
 \bar S_i=X_{i+m-1},
 \qquad
 \bar Y_i=S_{i+m-1}.
\tag{8.3}
\]

After reversing inclusion, local complement sends

\[
 (S_i,X_{i-1})
 \quad\longmapsto\quad
 (S_{i+m-1},X_{i+m-1}),
\tag{8.4}
\]

the successor token at start (i+m-1).  For (m\ge2), this is never the
same lower endpoint or owner as the original token: the lower-root starts
\(i\) and \(i+m-1\) differ by \(m-1\), while the owner starts \(i-1\)
and \(i+m-1\) differ by \(m\); neither difference is zero modulo
\(2m-1\).  Distinct proper cyclic windows are distinct.  Equations
(8.1)--(8.2) also show that the two halves of the flag tower attach at
different shifted token indices.

For an explicit reversal audit, put \(\rho_k=x_{-k}\).  The locally
complemented edge (8.4) is the predecessor token of \(\rho\) at
\(k=2-i\).  By contrast, the predecessor token of \(\rho\) whose lower
root is the original \(S_i\) occurs at \(k=-i-m+2\).  These are different
alignments; conflating them is precisely what would incorrectly turn the
reverse collar coboundary into a tokenwise bulk dual.

There is an even simpler phasewise obstruction.  For a changed bottom root
\(S\), write its \(A\)-phase owner as \(Y_A=S\cup\{u\}\).  The two
locally complemented incidences have lower roots and middle owners

\[
 T_A=Q_A\setminus Y_A,\qquad Z_A=Q_A\setminus S,
\tag{8.5a}
\]

\[
 T_B=Q_B\setminus\theta Y_A=\theta T_A,\qquad
 Z_B=Q_B\setminus S=\theta Z_A.
\tag{8.5}
\]

The set \(Z_A\) avoids \(A\) and contains all of \(B\), whereas \(Z_B\)
avoids \(B\) and contains all of \(A\), so \(Z_A\ne Z_B\).  Moreover
\(T_A\) avoids \(A\) and retains at least one coordinate of \(B\), because
\(Y_A\) adds at most one coordinate to the \(B\)-avoiding set \(S\).
Thus \(T_B=\theta T_A\ne T_A\).  Phasewise local complement therefore
shares neither lower root nor middle owner between its two alternatives.
Already at (j=1) this failure occurs on

\[
 |\mathcal D_1|=\binom{2m-3}{m-1}
 =\frac{m^2(m^2-1)}{(2m+1)(2m)(2m-1)(2m-2)}W
 =\left(\frac1{16}+o(1)\right)W
\tag{8.6}
\]

tokens.  This is a linear obstruction to rootwise repair of the naive
local-complement chart; it is not a universal lower bound on arbitrary
nonlocal OR-word fusion.

## 9. The closest legal old-centre substitute: reverse thresholds

Reverse the transported (F_B)-row.  At a changed start (i), the two
central tokens become

\[
 e_A(i)=(S_i,X_{i-1}),
 \qquad
 e_B^{\rm rev}(i)=(S_i,\theta X_i).
\tag{9.1}
\]

For a maximal changed interval (I=[a,b]), their symmetric difference is
the literal alternating path

\[
 X_{a-1}-S_a-X_a-S_{a+1}-\cdots-X_{b-1}-S_b-\theta X_b.
\tag{9.2}
\]

Every lower-saturating, middle-simple state on this path is uniquely an
old prefix followed by a new suffix.  Indeed, choosing new at (i) and
old at (i+1) would use (X_i) twice.  Conversely every monotone threshold
uses every lower root once and every middle path vertex at most once.

The reverse flags are

\[
 L_q^B(i)=I_\pi(i,m-q),
 \qquad
 U_q^B(i)=\theta I_\pi(i-q,m+q).
\tag{9.3}
\]

For a switched consecutive set (K), put

\[
 E_r(K)=\sum_{i\in K}\mathbf e_{I_\pi(i,r)}.
\tag{9.4}
\]

Then the exact new-minus-old innovations are

\[
 \boxed{
 z_{K,q}^-=E_{m-q}(K)-E_{m-q}(K+q-1),}
\tag{9.5}
\]

\[
 \boxed{
 z_{K,q}^+=\theta E_{m+q}(K-q)-E_{m+q}(K-1).}
\tag{9.6}
\]

Equation (0.11) is the (q=2) telescope.  More generally,

\[
 \|z_{K,q}^-\|_2^2\le2(q-1).
\tag{9.7}
\]

Thus reversal gives a legal one-core chart, but not independent upper and
lower bits: it changes the middle leave, has the upper collateral (9.6),
and its lower action is a coboundary confined to interval endpoints.

If (s_j\) is the number of reverse paths, then

\[
 s_j\le2jR_m,
 \qquad
 J(M_{\rm threshold})\le J(M_A)+2s_j.
\tag{9.8}
\]

Each final tight run still costs exactly (t+2H), so after isolated
completion its word length is

\[
W+2H\bigl(J(M_{\rm threshold})+d\bigr)=W+o(W)
\tag{9.9}
\]

provided
\[
J(M_A)=o(W/H),\qquad s_j=o(W/H),\qquad Hd=o(W).
\tag{9.10}
\]
For example, the audited bounds give this when
\(H=o(m/\log^2m)\) and \(jH=o(m)\), including each fixed adjacent
position in the Gaussian range.  This no-doubling fact does not contradict
the separate-core conclusion: the reverse chart is precisely the
collar-local substitute, not the lossless bulk dual of Section 6.

## 10. A depth-isolated same-edge audit

The preceding no-go must not be overstated.  Pure lower changes preserving
one central edge do exist tokenwise.

Fix \(2\le q\le m-2\) and put

\[
 b=x_{i+q-2},\qquad a=x_{i+q-1},\qquad \tau=(a\ b).
\tag{10.1}
\]

Both (a,b\) lie in (S_i).  At start (i) in the conjugate row
\(\tau\pi), the lower root and middle owner are unchanged, every upper
flag is unchanged, and every lower flag except depth (q) is unchanged.
At depth (q),

\[
 \boxed{
 L_q(i)\longmapsto L_q(i)-a+b.}
\tag{10.2}
\]

This is an exact Johnson-edge lower atom on a parallel copy of the same
central edge.

It is not an internal switch of one fixed exact local factor.  The rows
\(\pi\) and \(\tau\pi\) share at least (2m-3) middle windows: only the
two windows whose boundary separates the adjacent transposed positions
change.  Distinct rows of one exact factor have disjoint middle-window
sets.  Hence \(\tau\pi\notin F_A\) whenever \(\pi\in F_A\).

One such atom costs (O(1)) physical seams.  Identity (3.1) shows why
many such atoms cannot be compressed into a same-core long block with
bulk action: all interior lower flags are forced by the unchanged ordered
root sequence.

## 11. The (q\ge2) algebraic duality and the physical length boundary

The formal upper-to-lower correspondence is exact.  From (6.5)--(6.7),
bottom upper depth (p\ge2) maps under global complement to global lower
depth (q=p-1\):

\[
 \boxed{cU_p=G_{p-1}.}
\tag{11.1}
\]

The target rank sizes agree,

\[
 \binom n{m+p}=\binom n{m+1-p},
\tag{11.2}
\]

so for a completed mass-(W) word the exact floor capacities obey

\[
 \boxed{c_p^+=c_{p-1}^-\qquad(p\ge2).}
\tag{11.3}
\]

There is no missing constant, floor shift, or factor of two.  Algebraically,
the already relevant (q\ge2) upper layers are exactly the source of all
global lower depths (q\ge1).

Physically, however,

\[
 c(X\cup Y)=cX\cap cY,
\tag{11.4}
\]

so complementing targets does not complement an OR witness.  The bottom
word has rank-(m) owners and the dual sliding-core word has rank-(m+1)
owners.  Direct composition therefore gives

\[
 (W+o(W))+(W+o(W))=2W+o(W).
\tag{11.5}
\]

There is also an exact obstruction to the most direct attempt to recenter
the top chart.  Let

\[
 f:\binom{[n]}{m+1}\longrightarrow\binom{[n]}m
\]

be a bijection with \(f(U)\subset U\).  Here the domain consists of the
rank-\((m+1)\) top-owner sets which one is attempting to use as roots of
a recentered rank-\(m\) chart.  For every coordinate \(x\), the number of
such sets deleting \(x\), namely \(U\setminus f(U)=\{x\}\), is forced to
be

\[
 \Delta_m
 =\binom{2m}{m}-\binom{2m}{m-1}
 =\frac1{m+1}\binom{2m}{m}.
\tag{11.6}
\]

A direct \(A\)-phase recentering on these rank-\((m+1)\) sets containing
\(A\cup B\), under the natural rule that the \(A\)-phase deletes one
coordinate of \(A\), has carrier at most \(2\Delta_m\).  But its required
first carrier has size

\[
 \binom{2m-3}{m-3},
\tag{11.7}
\]

and

\[
 \binom{2m-3}{m-3}>2\Delta_m
 \quad\Longleftrightarrow\quad
 m^2-17m+6>0.
\tag{11.8}
\]

Thus this direct recentering is impossible for every (m\ge17).  This
does not rule out every nonlocal fusion; it rules out the natural
single-deletion recentering and confirms that no such fusion is hidden in
formal complement/reversal.

## 12. Exact proved and unproved boundary

### Proved

1. The same-core contained-pair lower innovation (0.2), positive Gram
   (2.7), exact central legality, and zero cross-Gram with the upper chart.
2. The exact collar formula (0.5), norm bound (3.5), and the conclusion
   that a subcritical low-run same-core catalogue moves only (o(W))
   depth-(q) occurrences.
3. The joint same-core run and literal length ledger (0.4).
4. The first-contained top matching, its changed domain, rootwise and
   intervalwise legality.
5. The bulk lower innovations (0.7), factor-two Gram (6.12), lossless
   packetization, and exact Haar gap (6.13)--(6.14).
6. The depth shift (p=q+1), the exact (t+2H+2) sliding-core word, all
   packet constants, and the completed length (0.9).
7. The local-complement index shift (8.1)--(8.4), the linear common-root
   failure (8.6), the reverse threshold path, and its endpoint telescope.
8. The exact floor correspondence between bottom upper depths (p\ge2)
   and global lower depths (p-1).

### Not proved

1. A bulk lower chart which keeps the rank-(m) middle-owner matching and
   moves a linear number of lower occurrences using (o(W/H)) seams.
2. A literal fusion sharing the (W) principal positions of the bottom
   and top-centred charts.
3. Endpoint energy-flatness or a charged coverage inequality for the
   partial same-core contained-pair chart.
4. Simultaneous product-cube legality for every adjacent position of the
   separate top-dual menu.
5. A constant-one theorem.

The decisive boundary is therefore physical, not algebraic: lower Gram
positivity is available, but bulk lower motion and one-core chronology have
not been achieved simultaneously.
