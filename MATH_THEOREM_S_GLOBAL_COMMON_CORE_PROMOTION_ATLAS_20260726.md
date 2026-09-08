# A global common-core promotion atlas: integral rankwise Hall and the remaining tight-path fusion gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome and scope

Put

\[
W=\binom{2m}{m},\qquad
N_q=\binom{2m}{m-q},\qquad
\lambda_q=\frac{W}{N_q}.
\tag{0.1}
\]

Let \(H=H(m)\) be at the calibrated promotion-ring height and write

\[
M=m+H,\qquad s=m-H,\qquad
\Lambda=\frac{W}{N_H},\qquad
L=m-3H+1=s-2H+1.
\tag{0.2}
\]

The exact hypotheses used below are

\[
H=(1+o(1))\sqrt{m\log m},\qquad m>4H,
\tag{0.3}
\]

and, for fixed constants \(c_0,C_0>0\),

\[
L+c_0H\le\Lambda\le m+C_0H.
\tag{0.4}
\]

Both audited critical choices—packing-side and covering-side—satisfy
(0.3)--(0.4), after changing the two absolute constants.  In particular,

\[
 H=\sqrt{m\log m}+c,\qquad |c|=O(1)
 \quad\Longrightarrow\quad
 \Lambda=m+2cH+o(H),
\tag{0.4a}
\]

so the floor choice \(-1<c\le0\) has
\(\Lambda-L=(3+2c)H+o(H)\ge(1+o(1))H\).  In particular,

\[
0<L<\Lambda,\qquad \frac{N_H}{W}=\Theta(1/m).
\tag{0.5}
\]

This note proves four positive statements.

1. One may choose a \(2H\)-set \(Q_U\subset U\) in every rank-\(M\)
   top \(U\) so that the core-constrained containment graph has the
   maximum-degree bound needed to match \(L\) clones of every top to
   distinct middle owners.
2. The same core choice simultaneously clears every individual signed
   rank. With a common per-top threshold profile, the separate rank
   matchings leave only

   \[
   O(H^{3/2}N_H)=o(W)
   \tag{0.6}
   \]

   aggregate masks unmatched.
3. A chosen core is physically compatible with one literal promotion
   path of length \(L\): retain the phases whose full \(2H\)-word lies
   outside the core block. Every mask in every retained truncated chain
   contains the core.
4. Even after imposing this actual core-safe cyclic-path catalogue, its
   complete nonnegative configuration LP has an exact symmetric
   fractional point. Thus no nonnegative one-set, weighted Hall,
   support, or separate-rank separator closes the lane.

The theorem does **not** construct a global promotion-ring factor. The
integral matchings at different ranks need not be traces of the same
phase, need not be nested, and need not be consecutive windows of one
tail order. The exact surviving assertion is a multilevel tight-path
fusion theorem. No coefficient-one conclusion is claimed.

## 1. The core-constrained middle graph

For every top

\[
U\in\binom{[2m]}{M},
\tag{1.1}
\]

choose a core

\[
Q_U\in\binom{U}{2H}.
\tag{1.2}
\]

Given the whole core assignment \(\mathbf Q=(Q_U)_U\), form a bipartite
graph \(G_0(\mathbf Q)\). Its left shore consists of \(L\) identical
clones of every top. Its right shore is the middle layer
\(\binom{[2m]}m\). A clone of \(U\) is adjacent to \(X\) precisely when

\[
Q_U\subset X\subset U.
\tag{1.3}
\]

Every top has the same right degree

\[
d_0=\binom{s}{H},
\tag{1.4}
\]

because, once \(Q_U\) is fixed, one chooses the \(H\)-set
\(U\setminus X\) inside the \(s\)-set \(U\setminus Q_U\).

### Theorem 1.1 (random-core maximum-degree cap)

For all sufficiently large \(m\), there is a core assignment
\(\mathbf Q\) such that every middle owner \(X\) has degree

\[
\deg_{\mathrm{top}}(X)\le \frac{d_0}{L}
\tag{1.5}
\]

in the un-cloned top--owner graph. Equivalently, at most \(d_0/L\)
tops \(U\) satisfy \(Q_U\subset X\subset U\).

#### Proof

Choose the \(Q_U\)'s independently and uniformly from
\(\binom U{2H}\). Fix \(X\in\binom{[2m]}m\). It is contained in

\[
\binom mH
\tag{1.6}
\]

tops. For each such top,

\[
\Pr(Q_U\subset X)=\frac{\binom m{2H}}{\binom M{2H}}.
\tag{1.7}
\]

Thus its random degree \(Z_X\) is binomial with mean

\[
\begin{aligned}
\mu_0
&=\binom mH\frac{\binom m{2H}}{\binom M{2H}}\\
&=\frac{(m!)^2}{H!(m-2H)!M!}
=\frac{d_0}{\Lambda}.
\end{aligned}
\tag{1.8}
\]

The last identity follows from

\[
\Lambda=\frac{M!s!}{(m!)^2},\qquad
d_0=\frac{s!}{H!(m-2H)!}.
\tag{1.9}
\]

Put

\[
\delta_0=\frac{\Lambda}{L}-1.
\tag{1.10}
\]

By (0.4),

\[
\delta_0\ge\frac{c_0H}{L},\qquad
\delta_0=O_{C_0}(H/m).
\tag{1.11}
\]

The Chernoff bound gives

\[
\Pr\left(Z_X>\frac{d_0}{L}\right)
\le
\exp\left(-\frac{\mu_0\delta_0^2}{2+\delta_0}\right)
\le
\exp\left(-c\frac{d_0H^2}{m^3}\right)
\tag{1.12}
\]

for an absolute \(c>0\). Moreover,

\[
d_0=\binom{s}{H}\ge (s/H)^H.
\tag{1.13}
\]

Under (0.3), \(d_0H^2/m^3\gg m\). Since \(W<4^m\), the union
bound over all middle owners is strictly less than one for sufficiently
large \(m\). Hence some core assignment satisfies (1.5).
\(\square\)

### Theorem 1.2 (integral \(L\)-clone middle Hall theorem)

For a core assignment supplied by Theorem 1.1, \(G_0(\mathbf Q)\) has
a matching saturating all \(LN_H\) top clones. Thus every top \(U\) can
be assigned \(L\) distinct middle owners satisfying (1.3), and no
middle owner is assigned to two tops.

#### Proof

It is enough to test a set \(\mathcal A\) of complete top fibres: a
nonempty subset of the identical clones of one top has the same
neighbourhood as all its clones, and completing every touched clone
fibre only increases the left side of Hall's inequality.

There are \(d_0|\mathcal A|\) incidences from the tops of
\(\mathcal A\) to their common neighbourhood. By (1.5), every owner
receives at most \(d_0/L\) of them. Therefore

\[
|N(\mathcal A)|
\ge \frac{d_0|\mathcal A|}{d_0/L}
=L|\mathcal A|.
\tag{1.14}
\]

This is Hall's condition for all \(L\) clones of every top.
\(\square\)

The count is already at coefficient-one scale:

\[
W-LN_H=(\Lambda-L)N_H=O_{C_0}(HN_H)=o(W).
\tag{1.15}
\]

Unlike the unstructured clone theorem, Theorem 1.2 imposes one literal
common \(2H\)-core on all owners assigned to a top.

## 2. A literal core-safe partial promotion ring

Fix a top \(U\), a core \(Q\subset U\) of size \(2H\), and put

\[
S=U\setminus Q,\qquad |S|=s.
\tag{2.1}
\]

Choose linear orders

\[
Q=(q_1,\ldots,q_{2H}),\qquad
S=(t_1,\ldots,t_s),
\tag{2.2}
\]

and regard their concatenation as a cyclic order of \(U\). The exact
promotion-ring theorem gives one full radius-\(H\) state at every cyclic
phase. Retain the phases whose full \(2H\)-letter central word lies
entirely inside the displayed \(S\)-block.

### Theorem 2.1 (core-safe partial-ring path)

There are exactly

\[
s-2H+1=L
\tag{2.3}
\]

retained phases. They are consecutive phases of the promotion ring and
therefore form one literal directed promotion path after the two
boundary edges are cut. Assign arbitrary tags in
\(\{0,\ldots,H\}\), with at most one tag \(H\). Then:

1. the retained truncated symmetric chains are pairwise mask-disjoint;
2. every mask of every retained chain contains \(Q\); and
3. their middle omissions are the \(L\) consecutive \(H\)-windows of
   one injective word of length \(s-H\).

#### Proof

The eligible \(2H\)-words start at

\[
t_1,t_2,\ldots,t_{s-2H+1},
\tag{2.4}
\]

which proves (2.3) and phase contiguity. A retained full state has its
entire central word in \(S\). At signed rank \(m+r\), its truncated
chain mask is the top \(U\) with a suffix of length \(H-r\) of that
central word omitted. The omitted set is therefore contained in \(S\),
so the mask contains \(Q\).

For two distinct retained phases and a rank occurring in both chains,
the omitted sets are distinct nonempty intervals of the same ordered
\(S\)-word. They cannot agree. The only zero-length omission occurs at
rank \(m+H\), and at most one retained chain has tag \(H\). This proves
pairwise mask-disjointness.

At the middle rank, the omitted windows are

\[
\{t_{j+H},t_{j+H+1},\ldots,t_{j+2H-1}\},
\qquad 1\le j\le L.
\tag{2.5}
\]

They are precisely the consecutive \(H\)-windows of

\[
t_{H+1},t_{H+2},\ldots,t_s,
\tag{2.6}
\]

whose length is \(s-H\).
\(\square\)

Conversely, any injective word of length \(s-H\) in \(S\), together
with an ordering of the remaining \(H\) letters before it, gives a path
of the form in Theorem 2.1. Thus the exact middle configuration inside
one top is a tight \(H\)-uniform path of \(L\) edges, not an arbitrary
family of \(L\) admissible \(H\)-sets.

Theorem 1.2 does not imply Theorem 2.1 for its assigned owners. It may
assign a family of \(H\)-deletions with no two members meeting in
\(H-1\) coordinates, whereas consecutive windows in (2.5) must do so.
This is the first exact cyclic-window compatibility gap.

## 3. One common core clears every rank separately

For a signed integer \(-H<r<H\), put

\[
\mathcal Y_r=\binom{[2m]}{m+r},\qquad
\Lambda_r=\frac{|\mathcal Y_r|}{N_H}
          =\frac{N_{|r|}}{N_H}.
\tag{3.1}
\]

For fixed cores, join a top \(U\) to \(Y\in\mathcal Y_r\) when

\[
Q_U\subset Y\subset U.
\tag{3.2}
\]

The left degree is

\[
d_r=\binom{s}{H-r}.
\tag{3.3}
\]

Choose the per-top target counts

\[
b_0=L,
\tag{3.4}
\]

and, for \(1\le q<H\),

\[
b_q=\min\left\{L-1,\,
       \max\left\{0,\left\lfloor\frac{N_q}{N_H}\right\rfloor-1\right\}
       \right\}.
\tag{3.5}
\]

The same \(b_q\) is used at signs \(r=q\) and \(r=-q\). The sequence
\(b_0,b_1,\ldots,b_{H-1}\) is nonincreasing.

### Theorem 3.1 (simultaneous random-core degree caps)

There is one core assignment \(\mathbf Q\) such that (1.5) holds and,
simultaneously for every \(0<|r|<H\) with \(b_{|r|}>0\),

\[
\deg_r(Y)\le \frac{d_r}{b_{|r|}}
\qquad(Y\in\mathcal Y_r).
\tag{3.6}
\]

#### Proof

Continue to choose all \(Q_U\)'s independently and uniformly. A fixed
\(Y\in\mathcal Y_r\) is contained in

\[
\binom{m-r}{H-r}
\tag{3.7}
\]

tops, and for each such top

\[
\Pr(Q_U\subset Y)
=\frac{\binom{m+r}{2H}}{\binom M{2H}}.
\tag{3.8}
\]

Its degree is binomial with mean

\[
\mu_r
=\binom{m-r}{H-r}
 \frac{\binom{m+r}{2H}}{\binom M{2H}}
=\frac{d_r}{\Lambda_r}.
\tag{3.9}
\]

The last equality also follows by double counting top--target
incidences.

When \(b_{|r|}>0\), definition (3.5) gives

\[
\Lambda_r-b_{|r|}\ge1.
\tag{3.10}
\]

The Chernoff exponent at threshold \(d_r/b_{|r|}\) is therefore at
least

\[
c\frac{d_r}{\Lambda_r^3}
\tag{3.11}
\]

for an absolute \(c>0\). To see that (3.11) is much larger than \(m\),
put \(q=|r|\). Since \(b_q>0\), one has \(\Lambda_r\ge2\). For
\(r\ge0\), the exact product for \(N_q/N_H\) and the bound

\[
\log\frac{m+j}{m-j+1}=O(H/m)\qquad(q<j\le H)
\tag{3.12}
\]

show that

\[
H-q=\Omega(m/H).
\tag{3.13}
\]

For \(r<0\), \(H-r=H+q\ge H\). Thus in both cases

\[
H-r\ge c_1m/H
\tag{3.14}
\]

for an absolute \(c_1>0\). Since
\(\Lambda_r\le\Lambda=O(m)\),

\[
\frac{d_r}{\Lambda_r^3}
\ge
\frac{1}{O(m^3)}
\binom{s}{\lceil c_1m/H\rceil}
\gg m.
\tag{3.15}
\]

The union bound over the \(O(HW)\) signed targets is therefore \(o(1)\).
Intersect this event with the event from Theorem 1.1.
\(\square\)

### Theorem 3.2 (simultaneous separately integral rank atlas)

For the cores in Theorem 3.1, every signed rank has an integral matching
which assigns \(b_{|r|}\) distinct targets to every top and never assigns
one target to two tops. These rankwise matchings may all be chosen for
the same fixed cores. They are not asserted to be mutually nested.

#### Proof

If \(b_{|r|}=0\), take the empty matching. Otherwise, at rank \(r\),
replace every top by \(b_{|r|}\) identical clones. For
a top family \(\mathcal A\), there are \(d_r|\mathcal A|\) incidences
into its neighbourhood, while (3.6) bounds every right degree by
\(d_r/b_{|r|}\). Hence

\[
|N_r(\mathcal A)|\ge b_{|r|}|\mathcal A|.
\tag{3.16}
\]

Hall's theorem proves the assertion. The middle rank is Theorem 1.2.
\(\square\)

### Proposition 3.3 (aggregate hole ledger)

The number of middle holes plus the holes in all separately matched
signed internal ranks is

\[
O_{C_0}(H^{3/2}N_H)=o(W).
\tag{3.17}
\]

Leaving both boundary ranks exceptional adds only \(2N_H=o(W)\). Even
charging a full \(O(H)\)-mask collar to every exceptional boundary
chain costs \(O(HN_H)=o(W)\).

#### Proof

The middle estimate is (1.15). If the cap \(L-1\) in (3.5) is inactive,
then

\[
0\le N_q-b_qN_H<2N_H.
\tag{3.18}
\]

The same inequality holds when \(b_q=0\), because then \(N_q/N_H<2\).

It remains to count capped depths. Uniformly at the critical scale,

\[
\frac{N_q}{N_H}
=\Lambda\exp\left(
-\frac{q^2}{m}
+O\left(\frac{q}{m}+\frac{q^4}{m^3}\right)
\right).
\tag{3.19}
\]

If \(b_q=L-1\), then \(N_q/N_H\ge L-1\). Equations (0.4) and
(3.19), or the elementary bound \(N_q/W\le e^{-q^2/(2m)}\), imply

\[
q=O_{C_0}(\sqrt H).
\tag{3.20}
\]

At every such depth,

\[
\frac{N_q}{N_H}-(L-1)=O_{C_0}(H).
\tag{3.21}
\]

Therefore capped depths contribute \(O_{C_0}(H^{3/2}N_H)\). The
\(H\) uncapped depths contribute \(O(HN_H)\) by (3.18). Doubling for
the two signs and adding the middle rank proves (3.17). Finally,

\[
\frac{H^{3/2}N_H}{W}
=O\left(\frac{H^{3/2}}m\right)
=O\left(m^{-1/4}(\log m)^{3/4}\right)=o(1).
\tag{3.22}
\]

\(\square\)

The numbers \(b_q\) are nested and fit inside the \(L\) physical phase
slots. Thus there is no per-top tag-histogram obstruction. What
Theorem 3.2 does not supply is a common choice of which phases carry the
rankwise targets.

## 4. No nonnegative configuration-Hall separator

Let \(\mathscr P(U)\) be the literal catalogue obtained by choosing:

1. a \(2H\)-core \(Q\subset U\);
2. orders of \(Q\) and \(U\setminus Q\); and
3. the \(L\)-phase core-safe path from Theorem 2.1.

Every option in \(\mathscr P(U)\) is one actual promotion path and uses
exactly \(L\) distinct middle owners.

### Theorem 4.1 (exact symmetric fractional core-safe atlas)

Give the options of every fixed top equal weight summing to one. Then
every middle owner has load exactly

\[
\rho_0=\frac{LN_H}{W}=\frac{L}{\Lambda}<1.
\tag{4.1}
\]

More generally, choose a phase-tag distribution invariant under phase
rotation and having exactly \(b_q\) active phases at threshold \(q\).
Every signed depth-\(q\) target has load exactly

\[
\rho_q=\frac{b_qN_H}{N_q}\le1.
\tag{4.2}
\]

#### Proof

The full symmetric group on \([2m]\) acts transitively on the tops, on
the core-safe catalogue, and on target masks of any fixed rank. The
uniform option distribution is invariant under this action. Hence every
middle owner has one common load. The total middle occurrence mass is
\(LN_H\), proving (4.1).

At threshold \(q\), the invariant tag distribution contributes exactly
\(b_qN_H\) occurrences. Transitivity on the corresponding signed rank
again makes the load constant, giving (4.2).
\(\square\)

### Corollary 4.2 (all additive weighted cuts pass)

For every nonnegative weight \(w\) on the middle layer,

\[
\sum_U\min_{P\in\mathscr P(U)}\sum_{X\in P}w_X
\le \rho_0\sum_Xw_X
\le\sum_Xw_X.
\tag{4.3}
\]

The analogous inequality holds at every signed rank with \(\rho_q\) in
place of \(\rho_0\), and for any nonnegative sum of signed-rank weights.

#### Proof

For each top, its minimum is at most its average under the distribution
of Theorem 4.1. Sum over tops and interchange the two finite sums. Each
target then carries its uniform load \(\rho_q\le1\).
\(\square\)

Equivalently, the rooted core-safe path hypergraph has an explicit
fractional matching which saturates every top root and respects every
nonnegative target capacity. Therefore an obstruction based only on one
target family, one nonnegative Farkas weight, core support, or separate
rank Hall expansion cannot refute the unrestricted catalogue.

This statement does not exclude an integral odd mesh or a common-history
obstruction. Row identification across ranks is not totally unimodular,
and a convex combination of paths is not one integral path per top.

## 5. Exact dynamic-fusion boundary

The proved statements leave one exact gate.

For every top \(U\), choose one core \(Q_U\), one injective tail word

\[
t_{U,1},\ldots,t_{U,s-H},
\tag{5.1}
\]

and tags on its \(L\) consecutive \(H\)-windows so that:

1. the middle owners

   \[
   U\setminus\{t_{U,j},\ldots,t_{U,j+H-1}\}
   \tag{5.2}
   \]

   are globally distinct up to \(o(W)\) exceptions;
2. at every threshold \(q\), the lower and upper suffix intervals of the
   same selected phases are globally distinct up to aggregate \(o(W)\)
   exceptions;
3. the selected thresholds are nested on every phase; and
4. the omitted exceptions occupy only \(o(W/H)\) promotion-path
   components, or have total literal repair cost \(o(W)\).

Theorem 1.2 proves (5.2) after deleting tight-path compatibility.
Theorem 2.1 proves the tight path inside one top. Theorem 3.2 proves all
signed target assignments after deleting common phase/nesting. Theorem
4.1 proves that their common convex relaxation is feasible. None of
these implications is reversible.

In particular, middle-owner distinctness does not imply lower- or
upper-trace distinctness across different cores, and independent rank
matchings do not reconstruct an ordered central word. The surviving
problem is a genuine integral common-history theorem, not another scalar
capacity estimate.

## 6. Proved and unproved ledger

Proved:

1. the exact random-core degree formula and simultaneous maximum-degree
   cap;
2. an integral assignment of \(L=m-3H+1\) core-compatible distinct
   middle owners to every top;
3. the literal \(L\)-phase core-safe promotion path and its all-depth
   common-core property;
4. simultaneous, separately integral target matchings at every signed
   rank with aggregate \(O(H^{3/2}N_H)=o(W)\) holes; and
5. an exact symmetric fractional solution for the complete core-safe
   cyclic-path catalogue, clearing every nonnegative additive
   configuration-Hall cut.

Not proved:

1. refinement of the middle Hall assignment to one tight path in every
   top;
2. nesting of the separate signed-rank matchings into common chain
   phases;
3. a one-fold owner-disjoint family of core-safe paths;
4. completion of the unused Boolean masks to one full SCD; or
5. \(\mathrm{RPE}\), \(\mathrm{TCB}\), \(\mathrm{EP}\), or the
   coefficient-one theorem.
