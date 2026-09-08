# Mesoscopic cyclic repair: an exact (q=1) port and a Gaussian-safe switch reservoir

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, or web input is used.

## 0. Result

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad B=W/n,
 \qquad N_q=\binom n{m-q},
 \qquad c_q=\left\lfloor {W\over N_q}\right\rfloor .
\tag{0.1}
\]

This note gives two exact pieces of the proposed mesoscopic cyclic route.

1. A missing depth-one colour has an explicit Johnson-square insertion
   port.  The second cross edge exists under one of two elementary label
   equalities.  This identifies the local edge-colour geometry, but the
   square by itself need not preserve wreath components.
2. A balanced alternating (8)-switch which does preserve exact wreaths
   changes at most (8q) depth-(q) occurrences.  Consequently, for

   \[
   H=\left\lceil\sqrt{m\log m}\right\rceil,
   \tag{0.2}
   \]

   a sequence of (s=o(B)=o(W/n)) such switches changes the weighted
   shallow overload by only (o(W)):

   \[
   \left|\sum_{q\le H}{O_q(F_s)-O_q(F_0)\over c_q}\right|
   \le 8s\bigl(m+o(m)\bigr)=o(W).
   \tag{0.3}
   \]

There is therefore no Gaussian-window accounting obstruction to an
(o(W/n)) **local switch reservoir**.  An exact Hall lemma below shows how
such a reservoir would absorb an (o(B)) set of depth-one holes, provided
the required balanced switch ports exist with expansion.

There is an important distinction.  Adding (r) arbitrary whole wreath
rows to an extendible partial factor has the weaker bound

\[
 \sum_{q\le H}{O_q(F)\over c_q}
 \le
 \sum_{q\le H}{O_q(G)\over c_q}
 +O(rn\sqrt m).
\tag{0.4}
\]

Thus arbitrary completion rows are automatically harmless for weighted
overload only when

\[
 r=o(B/\sqrt m).
\tag{0.5}
\]

For the raw missing-target objective, additions never create holes, so an
(o(B)) completion is harmless without (0.5).  The gain from local
splicing is exactly the improvement from a whole-row (n)-occurrence
charge to a (q)-local seam charge.

What remains unproved is the geometric expansion hypothesis in the Hall
lemma.  The result here proves the repair and rate theorem once that exact
finite gate is supplied; it does not infer expansion from the number of
holes alone.

## 1. Loads and the Johnson projection

For an exact middle wreath factor (F), let

\[
 \mu_q^F(S)
 =\#\{(\pi,j):\pi\in F, I_\pi(j,m-q)=S\}.
\tag{1.1}
\]

Every depth has total mass (W).  Let ({\cal B}_q) be the balanced quota
vectors (b:\binom{[n]}{m-q}\to\{c_q,c_q+1\}) with total mass (W), and
put

\[
 O_q(F)=\min_{b\in{\cal B}_q}
 \sum_S(\mu_q^F(S)-b(S))_+.
\tag{1.2}
\]

It is useful to pass from the odd-graph factor to its Johnson projection.
If (X) has factor neighbours (Y,Z), then (Y,Z) are distinct
(m)-subsets of the ((m+1))-set (X^c), so (YZ) is a Johnson edge.
Taking this edge for every centre (X) gives a spanning (2)-factor
({\cal J}(F)) of (J(n,m)).  On a wreath component this is precisely the
cycle of consecutive length-(m) windows of its cyclic coordinate order.

At depth (q), the lower target is the intersection of (q+1)
consecutive vertices of ({\cal J}(F)):

\[
 I_\pi(j,m-q)
 =\bigcap_{t=0}^{q} I_\pi(j+t,m).
\tag{1.3}
\]

This makes every bounded-edge change in ({\cal J}(F)) automatically
local through all depths.

## 2. The exact depth-one hole port

Let (S\in\binom{[n]}{m-1}) be absent from the depth-one edge colours of
({\cal J}(F)), and put

\[
 C=[n]\setminus S,\qquad |C|=m+2.
\tag{2.1}
\]

For (x\in C), write (X_x=S\cup\{x\}).  Since (S) is a hole, no
selected Johnson edge joins two of the (X_x)'s.

Choose distinct (x,y\in C), labels (r,s\in S), and
(z\in C\setminus\{y\}).  Suppose the selected factor contains

\[
 X_xA,qquad X_yD,
\tag{2.2}
\]

where

\[
 A=S-r+x+y,qquad D=S-s+y+z.
\tag{2.3}
\]

These are the general forms of a selected edge at (X_x) whose entering
outside label is (y), and a selected edge at (X_y).

### Lemma 2.1 (exact square-port criterion)

Assume the four displayed vertices are distinct.  Then (A,D) are
Johnson adjacent if and only if exactly one of

\[
 r=s,\qquad z=x
\tag{2.4}
\]

holds.  In that case

\[
 X_xA,\ X_yD
 \quad\longmapsto\quad
 X_xX_y,\ AD
\tag{2.5}
\]

is an alternating Johnson-square switch which inserts the missing colour
(S).  Its complete lower-colour ledger is

\[
 \begin{array}{c|c}
 \text{removed edge}&\text{colour}\\ \hline
 X_xA&S-r+x\\
 X_yD&S-s+y
 \end{array}
\tag{2.6}
\]

and

\[
 \begin{array}{c|c}
 \text{added edge}&\text{colour}\\ \hline
 X_xX_y&S\\
 AD&S-r+y\quad(r=s, z\ne x),\\
 AD&S-\{r,s\}+\{x,y\}\quad(z=x, r\ne s).
 \end{array}
\tag{2.7}
\]

#### Proof

If (r=s), the two sets in (2.3) have common part (S-r+y) and differ
only in (x,z).  They are adjacent when (z\ne x), and equal when
(z=x).  If (r\ne s), then outside the common part
(S-\{r,s\}+y), the two difference pairs are

\[
 \{s,x\},\qquad\{r,z\}.
\]

They are at Johnson distance one exactly when (z=x).  This proves
(2.4).  The intersections of the four edges give (2.6)--(2.7) directly.
\(\square\)

The square preserves the spanning (2)-factor degree ledger if its two
new edges were absent.  It need not preserve the decomposition into
literal length-(n) wreaths.  Exact-factor repair must therefore pair such
ports inside a balanced wreath-preserving alternating switch, or use a
larger exact trade.  Lemma 2.1 identifies the port which that larger move
must contain.

## 3. A general multidepth seam bound

Let (F,F') be exact wreath factors.  Suppose their Johnson projections
have (k) deleted and (k) added edges:

\[
 |E({\cal J}(F))\setminus E({\cal J}(F'))|
 =|E({\cal J}(F'))\setminus E({\cal J}(F))|=k.
\tag{3.1}
\]

### Theorem 3.1 (depth-(q) Lipschitz exchange)

For every (1\le q<n),

\[
 \boxed{
 {1\over2}\sum_S|\mu_q^{F'}(S)-\mu_q^F(S)|\le kq.}
\tag{3.2}
\]

Consequently

\[
 \boxed{|O_q(F')-O_q(F)|\le kq.}
\tag{3.3}
\]

#### Proof

Delete the (k) noncommon edges from ({\cal J}(F)).  Every old
(q)-window which uses only common edges lies in one retained path and
appears, possibly reversed, as the identical vertex window in
({\cal J}(F')).  Cancel all such common occurrences.  A fixed deleted
edge belongs to exactly (q) cyclic (q)-edge windows, so at most (kq)
old occurrences remain.  The same argument with (F,F') reversed leaves
at most (kq) new occurrences.  Both load vectors have equal total mass,
so their positive and negative variations agree, proving (3.2).

For a fixed balanced quota (b), the map

\[
 \mu\longmapsto\sum_S(\mu(S)-b(S))_+
\]

can increase by at most (sum_S(\mu'(S)-\mu(S))_+).  Use (3.2), first
with a quota minimizing for (F) and then with (F,F') reversed, to get
(3.3). \(\square\)

### Corollary 3.2 (balanced alternating (8)-switch)

Suppose (F') is obtained from (F) by one alternating (8)-cycle in
the odd graph and both are exact wreath factors.  Then (3.2)--(3.3) hold
with (k=8).

Indeed, at a middle vertex (X), the projected Johnson edge is the edge
between the two factor neighbours of (X).  This edge is unchanged unless
(X) is one of the eight vertices of the alternating cycle.  Hence at
most eight projected Johnson edges change.

This includes the balanced two-wreath switches characterized by equal
unordered cut-length profiles.  No run or orientation hypothesis beyond
the assertion that both endpoints are literal exact wreath factors is
needed for the load estimate.

## 4. The Gaussian sums

Put

\[
 \lambda_q={W\over N_q}
 =\prod_{j=0}^{q-1}{m+2+j\over m-j}.
\tag{4.1}
\]

For every (lambda\ge1), (lfloor\lambda\rfloor\ge\lambda/2).  Thus

\[
 {1\over c_q}\le {2N_q\over W}.
\tag{4.2}
\]

Let (H=o(m)) and (M=m+H+1).  For (q\le H),

\[
 \begin{aligned}
 {N_q\over W}
 &=\prod_{j=0}^{q-1}{m-j\over m+2+j}\\
 &\le
 \exp\left(-\sum_{j=0}^{q-1}{2j+2\over m+2+j}\right)
 \le \exp\left(-{q(q+1)\over M}\right)
 \le e^{-q^2/M}.
 \end{aligned}
\tag{4.3}
\]

Integral comparison now gives the explicit bounds

\[
 \boxed{
 \sum_{q=1}^{H}{1\over c_q}
 \le \sqrt{\pi M},}
\tag{4.4}
\]

\[
 \boxed{
 \sum_{q=1}^{H}{q\over c_q}
 \le M+\sqrt{\pi M}.}
\tag{4.5}
\]

For example,

\[
 2\sum_{q\ge1}q e^{-q^2/M}
 \le2\int_0^\infty(x+1)e^{-x^2/M}\,dx
 =M+\sqrt{\pi M}.
\]

At (H=\lceil\sqrt{m\log m}\rceil), one has (M=m+o(m)).  Combining
Corollary 3.2 with (4.5), one balanced switch changes the complete weighted
window objective by at most

\[
 \boxed{8\bigl(M+\sqrt{\pi M}\bigr)=8m+o(m).}
\tag{4.6}
\]

Therefore (s=o(B)) switches have total possible adverse change

\[
 O(sm)=o(Bm)=o(W).
\tag{4.7}
\]

The same proof gives a factor two if lower and complementary upper
objectives are recorded separately rather than identified by
complementation.

## 5. A Hall repair lemma for disjoint exact switch cells

The following statement isolates the minimal finite expansion theorem
needed by this route.

Let (F) be an exact wreath factor and let

\[
 {\cal C}_1,\ldots,{\cal C}_r
\]

be pairwise owner-disjoint cells, each consisting of two wreath rows.  A
menu option in ({\cal C}_i) replaces those two rows by two other literal
wreath rows on exactly the same (2n) middle owners, through a balanced
alternating (8)-switch.  Thus choices in different cells preserve exact
middle ownership and commute.

Let ({\cal U}) be the union of all cell owners, and let ({\cal H}) be
a set of currently missing depth-one colours.  Call an option
**frozen-safe for (h\in{\cal H})** if

1. its new depth-one support contains (h); and
2. every old depth-one colour which it removes has another occurrence
   centred outside ({\cal U}).

Form the bipartite graph

\[
 h\sim i
 \quad\Longleftrightarrow\quad
 {\cal C}_i\text{ has a frozen-safe option for }h.
\tag{5.1}
\]

### Theorem 5.1 (mesoscopic switch-reservoir Hall lemma)

If

\[
 |N({\cal A})|\ge|{\cal A}|
 \qquad({\cal A}\subseteq{\cal H}),
\tag{5.2}
\]

then one may modify distinct cells so that every colour in ({\cal H})
is covered, no previously covered depth-one colour becomes missing, and
the result is again an exact wreath factor.  Moreover, for every
(H=o(m)), its weighted multidepth change is at most

\[
 8|{\cal H}|\bigl(m+H+1+\sqrt{\pi(m+H+1)}\bigr).
\tag{5.3}
\]

In particular, when (H=\lceil\sqrt{m\log m}\rceil) and
(|{\cal H}|=o(B)), this change is (o(W)).

#### Proof

Hall's theorem gives an injection (h\mapsto i(h)) with
(h\sim i(h)).  In every selected cell use a witnessing option.  The
cells have disjoint owner supports, so their exact replacements commute.
Every assigned hole is inserted.  A removed old colour has a frozen
occurrence outside the union of all cells and therefore survives every
choice.  Hence no new depth-one hole is created.

At most (8|{\cal H}|) projected Johnson edges are changed.  Apply
Theorem 3.1 once to the simultaneous old and new factors, and then use
(4.5).  This gives (5.3). \(\square\)

The Hall condition is not a consequence of (|{\cal H}|=o(B)).  It is the
new geometric task: prove that a mesoscopic family of balanced two-row
cells supplies frozen-safe ports with the expansion (5.2), or construct a
larger exact trade with the same locality bound.

## 6. Whole-row completion versus local switch completion

Let (G) be a partial middle packing which is extendible to an exact
factor

\[
 F=G\mathbin{\dot\cup}E,
 \qquad |E|=r.
\tag{6.1}
\]

Each added row contributes exactly (n) occurrences at every depth.
Using the same balanced-quota Lipschitz argument as in Theorem 3.1 gives

\[
 O_q(F)\le O_q(G)+rn.
\tag{6.2}
\]

Together with (4.4),

\[
 \boxed{
 \sum_{q\le H}{O_q(F)\over c_q}
 \le
 \sum_{q\le H}{O_q(G)\over c_q}
 +rn\sqrt{\pi(m+H+1)}.}
\tag{6.3}
\]

At (H=\sqrt{m\log m}), the last term is

\[
 O(rn\sqrt m).
\tag{6.4}
\]

Since (W=nB), condition (r=o(B/\sqrt m)) makes it (o(W)).  Merely
(r=o(B)) does not suffice for this worst-case weighted-overload bound.

For missing-target counts

\[
 M_q(G)=\#\{S:\mu_q^G(S)=0\},
\]

one instead has the monotonicity

\[
 M_q(F)\le M_q(G).
\tag{6.5}
\]

Thus an (o(B)) auxiliary completion is entirely safe for the raw-hole
version, assuming the partial core already has aggregate (o(W)) holes.

## 7. Exact repair-capacity limits

The preceding positive rates do not create repair capacity.

* One balanced (8)-switch changes at most eight depth-one occurrences,
  so it can newly cover at most eight depth-one holes.  Repairing (R)
  holes by such switches requires at least (R/8) switches.
* One added cyclic order contains only (n) depth-one targets, so an
  (r)-row auxiliary family can cover at most (rn) holes.

Consequently an (o(B)) balanced-switch reservoir can mop up only an
(o(B)) depth-one residue.  An (o(B)) whole-row reservoir has the larger
cardinality capacity (o(nB)=o(W)), but its arbitrary weighted-overload
cost is controlled only at the sharper scale (o(B/\sqrt m)), unless its
own shadows are also designed.

The minimal surviving construction theorem is therefore:

> Build an exact or extendible cyclic near-design whose depth-one residue
> is (o(B)), together with (o(B)) pairwise owner-disjoint balanced
> switch cells satisfying the frozen-safe Hall expansion (5.2).

Theorem 5.1 then repairs depth one without losing coefficient one through
(H=\sqrt{m\log m}).  Alternatively, a row-scale trade which inserts
Θ((n)) missing colours while changing only (O(q)) occurrences at
depth (q) would combine the larger capacity of whole rows with the
Gaussian-safe locality of balanced switches.  No such row-scale trade is
proved here.
