# Lane W: proportional complete-column twin rounding

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or web use.

## 0. Outcome

This report composes the proportional tight-atom profile with the exact
two-state correlated rounding theorem while preserving complete physical
interval columns.  It proves two new statements.

First, the block length can be chosen arithmetically so that **every exact
middle wreath factor** splits into

\[
 p-o(p/\sqrt m)
\]

complete proportional rows.  The loss is not one block per wreath.  Choosing
the block length as a near divisor of \(2m+1\) makes the loss

\[
 O(W/b^2)=o(p/\sqrt m).
\]

Second, on each such row put the floor-proportional radii in monotone order
and use its one-place cyclic shift as the second state.  Both states retain
whole saturated interval columns, have identical middle ownership and type
counts, and their exact squared incidence-difference norm is at most
\(4H\).  Over
all rows the correlated-rounding action is therefore

\[
 O(WH/b)=o(W)
\]

in the regime

\[
 H=\sqrt m\,\omega,\qquad
 b=\sqrt m\,g,\qquad
 1\ll\omega\ll g\ll\log m.
\]

Consequently a two-cover pair-sum floor \(B=o(W)\) gives a literal
constant-one construction.  The theorem is integral at every stage and
never forms a vertex-independent residual.

There is also a sharp obstruction.  If both row states merely rearrange
complete columns carried by the **same** exact factor \(F\), then at the
first lower shadow

\[
 \boxed{B_{-1}\ge C_1(F)-O(W/b),}
\]

where

\[
 C_1(F)=\sum_S(\mu_{-1}^F(S)-1)_+
\]

is the raw duplicate excess of the full carrier factor.  Thus internal
column correlation cannot manufacture a good first shadow from a factor
with linear first-shadow collision.  In particular, the canonical MSW
carrier still has \(B_{-1}=\Omega(W)\).  To complete constant one by this
route, the two states must change physical row carriers inside exact middle
cells (genuine shadow-twin ownership trades).  At minimum one must first
construct a factor with \(C_1(F)=o(W)\); that necessary first-shadow
condition is not sufficient at the higher depths.

The report therefore derives the requested middle-disjoint physical-row
count leave and the complete-column curvature bound unconditionally.  The
surviving pair-sum condition
is not silently assumed: its fixed-carrier obstruction is proved exactly.

## 1. Parameters and exact proportional profile

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 \tau=\frac Wn=\operatorname{Cat}_m.
\tag{1.1}
\]

Choose functions \(\omega=\omega(m)\) and \(g=g(m)\) such that

\[
 \omega\longrightarrow\infty,qquad
 \omega=o(g),qquad g=o(\log m),qquad
 \omega^2=o(\log m).
\tag{1.2}
\]

Set

\[
 H=\lceil\sqrt m\,\omega\rceil,qquad
 k=\left\lfloor\frac{n}{\sqrt m\,g}\right\rfloor,qquad
 b=\left\lfloor\frac nk\right\rfloor,qquad
 r=n-kb.
\tag{1.3}
\]

Then

\[
 k=(2+o(1))\frac{\sqrt m}{g},qquad
 b=(1+o(1))\sqrt m\,g,qquad
 0\le r<k,
\tag{1.4}
\]

and hence

\[
 H=o(b),\qquad b=o(\sqrt m\log m),qquad b+H=o(m).
\tag{1.5}
\]

The last condition in (1.2) also gives

\[
 b\exp(-\omega^2)\longrightarrow\infty.
\tag{1.6}
\]

Uniformly for \(|q|\le H+1\), the elementary binomial-product expansion
gives

\[
 \log\frac{N_q}{W}=-\frac{q^2}{m}+o(1).
\]

Indeed the linear correction is \(O(H/m)=o(1)\) and the remainder after
the quadratic term is \(O(H^3/m^2)=o(1)\) under (1.2).  Hence
\(N_q/p\ge(1+o(1))b\exp(-\omega^2)\to\infty\) at the edge of the band.
Thus every proportional rank part below is nonempty for all sufficiently
large \(m\).

For \(-H\le q\le H+1\), put

\[
 N_q=\binom n{m+q},qquad
 p=\left\lfloor\frac Wb\right\rfloor,qquad
 b_q=\left\lfloor\frac{N_q}{p}\right\rfloor.
\tag{1.7}
\]

For large \(m\),

\[
 b_0=b_1=b,qquad b_{-d}=b_{d+1}.
\tag{1.8}
\]

Define the exact radius counts

\[
 a_d=b_{-d}-b_{-(d+1)}\quad(0\le d<H),
 \qquad a_H=b_{-H}.
\tag{1.9}
\]

They are nonnegative and satisfy

\[
 \sum_{d=0}^Ha_d=b,
 \qquad
 b_q=\sum_{d\ge\rho(q)}a_d,
 \qquad
 \rho(q)=\max\{-q,q-1\}.
\tag{1.10}
\]

The total number of designated band cells in one row is

\[
 \kappa=\sum_{q=-H}^{H+1}b_q=O(b\sqrt m).
\tag{1.11}
\]

Indeed \(b_q\le N_q/p\), \(p\ge W/(2b)\) for large \(m\), and the
central-binomial estimate gives

\[
 \frac1W\sum_qN_q\le\frac{2^n}{W}=O(\sqrt m).
\]

## 2. Near-divisor cutting of one exact factor

Fix any exact middle wreath factor \(F\).  Choose an orientation and a root
on each of its \(\tau\) cyclic rows.  In every row, take the first \(kb\)
middle-window starts and divide them into \(k\) consecutive blocks of \(b\)
starts.  Leave the final \(r\) starts unused.

For a block beginning at cyclic position \(u\), read

\[
 x_u,x_{u+1},\ldots,x_{u+m+b+H-1}
\]

cyclically.  Because \(m+b+H<n\), these coordinates are distinct.  Thus
the block is a genuine proportional physical row.  For a local start
\(0\le j<b\), its rank-\((m+q)\) interval is

\[
 A_{j,q}=\{x_{u+j},\ldots,x_{u+j+m+q-1}\}.
\tag{2.1}
\]

### Theorem 2.1 (exact complete-row leave)

The construction produces

\[
 s=\tau k
\tag{2.2}
\]

physical rows, and

\[
 \boxed{
 p-s=\left\lfloor\frac{\tau r}{b}\right\rfloor
 <\frac{W}{b^2}
 =o(p/\sqrt m).}
\tag{2.3}
\]

Their rank-\(m\) and rank-\((m+1)\) target systems are both pairwise
disjoint.  The number of unused middle owners is

\[
 \boxed{\tau r<\frac Wb=o(W/\sqrt m).}
\tag{2.4}
\]

#### Proof

Since \(n=kb+r\) and \(W=\tau n\),

\[
 p=\left\lfloor\frac{\tau(kb+r)}b\right\rfloor
   =\tau k+\left\lfloor\frac{\tau r}b\right\rfloor.
\]

This gives the equality in (2.3).  Since \(r<k\le n/b\),

\[
 \frac{\tau r}b<\frac{\tau n}{b^2}=\frac W{b^2}.
\]

Also \(p=(1+o(1))W/b\), so

\[
 \frac{W/b^2}{p/\sqrt m}=(1+o(1))\frac{\sqrt m}{b}=o(1).
\]

Equation (2.4) follows similarly from \(r<k\le n/b\).

At rank \(m\), distinct starts in the selected blocks are distinct middle
windows, and the exact factor makes them distinct across wreaths.  At rank
\(m+1\), the complement of a cyclic \((m+1)\)-window is a cyclic
\(m\)-window in the same wreath.  Equality of two selected upper windows
would therefore give equality of their complementary middle windows, which
is impossible. \(\square\)

This is the requested \(o(p/\sqrt m)\) middle-disjoint physical-row count
leave.  It is not yet a matching in the noncentral target parts.  It avoids
the old one-remainder-per-wreath loss by choosing \(b\)
after \(k\), so that \(r<k\asymp m/b\), rather than merely \(r<b\).

## 3. Two complete-column states with exact small action

List the multiset containing \(a_d\) copies of \(d\) in nondecreasing
order:

\[
 0\le d_0\le d_1\le\cdots\le d_{b-1}\le H.
\tag{3.1}
\]

We allow the radius locations to move with the state; only the exact
histogram \((a_0,\ldots,a_H)\) is fixed.  This is the mobile-profile
proportional atom family.  The literal interval identity and every slot
count remain unchanged.

On one physical row define two states:

\[
 \text{state }0:\quad j\mapsto d_j,
 \qquad
 \text{state }1:\quad j\mapsto d_{j-1\pmod b}.
\tag{3.2}
\]

The complete column of radius \(d\) at start \(j\) is

\[
 \mathcal C(j,d)=\bigl(A_{j,q}:-d\le q\le d+1\bigr).
\tag{3.3}
\]

Thus each state retains whole saturated columns.  Both states have exactly
\(a_d\) columns of radius \(d\), exactly \(b_q\) targets in rank
\(m+q\), and exactly the same \(b\) middle and \(b\) upper-central
targets.

Let \(a_e^0,a_e^1\) be the two incidence vectors of row \(e\), over all
rank parts in the band, and put

\[
 z_e=a_e^1-a_e^0.
\tag{3.4}
\]

### Lemma 3.1 (exact total-variation action)

For every selected row,

\[
 \boxed{
 \|z_e\|_2^2
 =2\sum_{j=0}^{b-1}|d_j-d_{j-1}|
 =4(d_{b-1}-d_0)
 \le4H.}
\tag{3.5}
\]

Consequently

\[
 \boxed{
 \sum_{e=1}^{s}\|z_e\|_2^2
 \le4Hs
 \le\frac{4HW}{b}=o(W).}
\tag{3.6}
\]

The same bounds hold for every coordinate weighting by numbers in
\([0,1]\).

#### Proof

A radius-\(d\) column occupies the consecutive rank interval
\([-d,d+1]\).  Replacing radius \(d\) by \(d'\) changes exactly

\[
 2|d-d'|
\]

rank-target cells.  At a fixed rank, intervals belonging to distinct starts
in one injective cyclic row are distinct.  Hence different changed starts
produce distinct incidence cells, and their squared contributions add.
This proves the first equality in (3.5).

For a cyclically closed nondecreasing sequence, the total variation is
twice its range:

\[
 \sum_j|d_j-d_{j-1}|=2(d_{b-1}-d_0).
\]

This proves (3.5).  Summing and using \(s\le p\le W/b\) proves (3.6).
Finally \(H/b=\omega/g+o(1)=o(1)\). \(\square\)

The saving comes from the \(O(H)\) boundaries of a monotone Ferrers
profile.  A vertex-independent residual would instead expose
\(\kappa=\Theta(b\sqrt m)\) unrelated cells per row.

## 4. Exact correlated rounding and the constant-one implication

Add one fixed singleton owner for each of the \(\tau r\) unused middle
sets.  Every global state choice then has exact middle ownership.  Different
row cells are middle-disjoint, and each row state has the same type
histogram, so every band rank has a fixed total

\[
 T_q=sb_q\le pb_q\le N_q
\qquad(q\ne0).
\tag{4.1}
\]

For a sign vector \(\varepsilon\in\{-1,1\}^s\), let
\(\mu^\varepsilon_q(S)\) be the resulting load.  Pair it with the
complementary corner \(-\varepsilon\) and define the invariant pair sum

\[
 t_q(S)=\mu_q^\varepsilon(S)+\mu_q^{-\varepsilon}(S).
\tag{4.2}
\]

For \(u\in\mathbb Z_{\ge0}\), put

\[
 \beta(u)=\left\lfloor\frac{(u-1)^2}{4}\right\rfloor,
\qquad
 B=\sum_{\substack{-H\le q\le H+1\\q\ne0}}
       \sum_{S\in\binom{[n]}{m+q}}\beta(t_q(S)).
\tag{4.3}
\]

Notice that \(\beta(u)=0\) exactly for \(u\in\{0,1,2\}\).  Thus \(B\)
is the exact obstruction to splitting the invariant two-cover into two
collision-free corners, before paying signing action.

### Theorem 4.1 (complete-column twin rounding)

Some integral global state choice satisfies

\[
 \boxed{
 \sum_{\substack{-H\le q\le H+1\\q\ne0}}
 \sum_S\binom{\mu_q(S)}2
 \le\frac B2+\frac18\sum_{e=1}^s\|z_e\|_2^2
 \le\frac B2+\frac{HW}{2b}.}
\tag{4.4}
\]

In particular, if

\[
 \boxed{B=o(W),}
\tag{4.5}
\]

then the selected complete physical rows have total band collision excess
\(o(W)\).

#### Proof

For integers \(x,y\ge0\) of fixed sum \(u=x+y\), direct expansion gives

\[
 \binom x2+\binom y2
 =\beta(u)+\frac{(x-y)^2-\mathbf1_{\{u\ \mathrm{odd}\}}}{4}.
\tag{4.6}
\]

For a complementary sign pair, the coordinatewise difference of its loads
is

\[
 d^\varepsilon=\sum_e\varepsilon_ez_e.
\]

Averaging (4.6) over the two corners and then over independent fair signs
gives

\[
 \mathbb E_\varepsilon
 \sum_{q\ne0,S}\binom{\mu_q^\varepsilon(S)}2
 \le\frac B2+\frac18
 \mathbb E\left\|\sum_e\varepsilon_ez_e\right\|_2^2
 =\frac B2+\frac18\sum_e\|z_e\|_2^2.
\]

Some integral corner is no larger than the expectation.  Use Lemma 3.1.
Every corner chooses complete columns and is an exact middle-owner family;
no fractional or vertex-independent state is used. \(\square\)

### Theorem 4.2 (literal constant-one consequence)

Under (1.2)--(1.6), condition (4.5) implies

\[
 \boxed{\nu(2m+1)\le W+o(W).}
\tag{4.7}
\]

#### Proof

Let \(\delta=p-s\).  The total unfilled slot mass in the band, apart from
the middle singletons, is

\[
\begin{aligned}
 \mathcal D
 &=\sum_{q\ne0}(N_q-sb_q)\\
 &\le(2H+1)p+\delta\kappa.
\end{aligned}
\tag{4.8}
\]

By Theorem 2.1, \(\delta<W/b^2\), and by (1.11),

\[
 \mathcal D
 =O(WH/b)+O(W\sqrt m/b)=o(W).
\tag{4.9}
\]

For a class with total load \(T\le N\), its number of holes is exactly

\[
 N-T+\sum_S(\mu(S)-1)_+
 \le N-T+\sum_S\binom{\mu(S)}2.
\tag{4.10}
\]

Theorems 4.1 and (4.9) therefore leave only \(o(W)\) band masks uncovered.

For each selected block \(e\), use block-local indexing for its underlying
coordinate word and emit

\[
 E_{e,j}=\{x_j,\ldots,x_{j+m-H-1}\},
 \qquad 0\le j\le b+2H.
\tag{4.11}
\]

For every designated start \(0\le i<b\) and
\(-H\le q\le H+1\), the literal contiguous identity is

\[
 \bigcup_{j=i}^{i+q+H}E_{e,j}=A_{i,q}.
\tag{4.12}
\]

Thus the emitted word for one row has \(b+2H+1\) entries.  Its total
length over all rows is

\[
 s(b+2H+1)
 \le W+O(WH/b)=W+o(W).
\tag{4.13}
\]

Append the \(\tau r=o(W)\) unused middle masks and all remaining band holes
literally.  Finally append the audited symmetric-chain product word for the
two outer Boolean tails.  Its length is \(o(W)\) whenever
\(H/\sqrt m\to\infty\) and \(H\le m/2\).  The row may cover additional,
undesignated columns; ignoring those can only enlarge the certified hole
set.  Equation (4.12) shows that every designated target is a literal
contiguous union of base windows, so the resulting object is one literal
contiguous-OR word of length \(W+o(W)\). \(\square\)

The standard parity lift gives the even-dimensional subsequence as well:

\[
 \nu(2m+2)\le2\nu(2m+1),
 \qquad
 W(2m+2)=2W(2m+1).
\]

The physical-row count leave in Theorem 2.1 and the collision conclusion
in Theorem 4.2 are different ledgers.  The former is unconditional.  The latter needs
the exact two-cover condition (4.5), but only at the aggregate \(o(W)\)
scale; it does not require an atom matching with leave
\(o(p/\sqrt m)\).

## 5. Exact fixed-carrier obstruction at the first shadow

The pair-sum floor in Theorem 4.1 cannot be discarded.  The first lower
rank already gives a sharp obstruction.

Let \(F\) be the exact carrier factor.  For
\(S\in\binom{[n]}{m-1}\), let \(\mu_F(S)\) be the number of cyclic
\((m-1)\)-interval occurrences in all rows of \(F\).  Then

\[
 \sum_S\mu_F(S)=W.
\tag{5.1}
\]

Define its raw duplicate excess

\[
 C_1(F)=\sum_S(\mu_F(S)-1)_+.
\tag{5.2}
\]

Consider any two radius-assignment states on the same fixed oriented and
rooted carrier columns, not necessarily the shifted monotone states,
provided both have the same proportional type counts and only rearrange
stopping radii.  They do not reorder, reverse, or replace carrier columns,
so both only delete occurrences from the same one-copy full-carrier
system.  At the first lower rank the explicit hypothesis is

\[
 \mu^\epsilon(S)=\mu_F(S)-d_\epsilon(S),
 \qquad d_\epsilon(S)\ge0,
 \qquad \epsilon\in\{0,1\}.
\tag{5.3}
\]

Both states delete the same total number

\[
 D=\sum_Sd_\epsilon(S)=W-sb_{-1}.
\tag{5.4}
\]

Let \(B_{-1}\) be the contribution of this rank to (4.3).

### Theorem 5.1 (fixed-carrier pair-floor lower bound)

\[
 \boxed{B_{-1}\ge C_1(F)-D.}
\tag{5.5}
\]

Moreover, in the near-divisor regime,

\[
 \boxed{
 D<\frac{2W}{m+2}+p+\delta b
 =O(W/b).}
\tag{5.6}
\]

Hence

\[
 \boxed{B_{-1}\ge C_1(F)-O(W/b).}
\tag{5.7}
\]

For completeness, the opposite elementary bound is

\[
 \boxed{
 B_{-1}\le
 \sum_S\mu_F(S)(\mu_F(S)-1)
 =2\sum_S\binom{\mu_F(S)}2.}
\tag{5.7a}
\]

Thus the construction supplies no noncircular upper estimate on
\(B_{-1}\): it can only inherit a pre-existing carrier second-moment
bound.

#### Proof

Fix \(S\), put \(\mu=\mu_F(S)\),
\(a=d_0(S)+d_1(S)\), and \(u=2\mu-a\).  For \(\mu\ge1\),

\[
 \beta(u)\ge\frac u2-1
 =\mu-1-\frac a2.
\tag{5.8}
\]

Indeed the right side is nonpositive for \(u\le2\), while for \(u\ge3\)
the inequality follows directly from
\(\beta(u)=\lfloor(u-1)^2/4\rfloor\).  For \(\mu=0\), both sides of the
desired inequality are zero.  Summing (5.8) over \(S\) gives

\[
 B_{-1}
 \ge\sum_S(\mu_F(S)-1)_+
     -\frac12\sum_S(d_0(S)+d_1(S))
 =C_1(F)-D.
\]

For (5.6), write \(N_{-1}=\binom n{m-1}\).  Since

\[
 W-N_{-1}=\frac{2W}{m+2},
 \qquad 0\le N_{-1}-pb_{-1}<p,
\]

and \(s=p-\delta\),

\[
\begin{aligned}
 D
 &=W-(p-\delta)b_{-1}\\
 &=(W-N_{-1})+(N_{-1}-pb_{-1})+\delta b_{-1}\\
 &<\frac{2W}{m+2}+p+\delta b.
\end{aligned}
\]

Now \(p=O(W/b)\), \(\delta<W/b^2\), and \(b=o(m)\), proving (5.6).
Finally \(u\le2\mu\), and \(\beta\) is nondecreasing on the nonnegative
integers, so

\[
 \beta(u)\le\beta(2\mu)=\mu(\mu-1).
\]

Summing proves (5.7a).
\(\square\)

### Corollary 5.2 (canonical fixed-carrier failure)

For the canonical MSW factor, the audited marked-gap theorem gives

\[
 C_1(F^{\rm MSW})\ge\left(\frac1{16}-o(1)\right)W.
\tag{5.9}
\]

Therefore every pair of proportional complete-column rearrangements on
that fixed carrier has

\[
 \boxed{
 B_{-1}\ge\left(\frac1{16}-o(1)\right)W,}
\tag{5.10}
\]

so Theorem 4.2 cannot be invoked.

#### Proof

The marked-gap theorem is stated as a linear lower bound on first-shadow
holes.  Since the full carrier has \(W\) occurrences on a rank of size
\(N_{-1}\),

\[
 C_1(F)=W-|\operatorname{supp}\mu_F|
       =(W-N_{-1})+M_1(F)\ge M_1(F).
\]

Use the audited \((1/16-o(1))W\) hole bound and (5.7). \(\square\)

Theorem 5.1 is broader than the monotone-shift construction.  It applies to
arbitrary dependent rearrangements of complete radii on fixed carrier rows.
It shows exactly what genuine shadow twins must do: they must alter the
physical carrier rows inside an exact middle cell, not merely move stopping
depths on one bad carrier.

## 6. Proved and conditional boundary

### Proved unconditionally

1. There are parameter choices
   \(H=\sqrt m\,\omega\), \(H\ll b\ll\sqrt m\log m\) satisfying all
   proportional floor and product-tail requirements.
2. Every exact factor cuts into \(s=p-o(p/\sqrt m)\) complete physical
   proportional rows, with only \(o(W/\sqrt m)\) middle owners left.
3. The two radius states (3.2) preserve complete interval columns, exact
   middle ownership, and every type count.
4. Their exact total signing action is \(O(WH/b)=o(W)\).
5. The pair-floor identity gives a literal constant-one word whenever the
   invariant two-cover floor is \(B=o(W)\).
6. On a fixed carrier, \(B_{-1}\ge C_1(F)-O(W/b)\); in particular the
   canonical carrier has \(B_{-1}=\Omega(W)\).

### Still unproved

1. No theorem here constructs two different physical carrier tilings of
   common exact middle cells whose invariant pair floor is \(o(W)\).
2. No theorem here proves an exact factor with \(C_1(F)=o(W)\).
3. Thus (4.5), and hence the unconditional constant-one theorem, remains
   open.

The route has nevertheless advanced beyond the generic curvature gate.  The
complete-row leave and the complete-column action are now solved at the
required scales.  The sole remaining obstruction in this composition is the
two-cover pair floor, and Theorem 5.1 proves that fixed-carrier radius
correlation cannot remove it.
