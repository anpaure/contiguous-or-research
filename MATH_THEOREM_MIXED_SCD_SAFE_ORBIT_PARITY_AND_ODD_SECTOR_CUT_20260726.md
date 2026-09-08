# Mixed-SCD safe orbits: exact codegrees, parity kernel, and the odd-sector cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
probabilistic black box is used.

## 0. Result

Let

\[
             \Omega_m=\binom{[2m]}m
\]

be the middle owners.  The full coordinate orbit of one oriented
length-\(h\) product-SCD diagonal is the complete family of monotone
Johnson geodesics

\[
 X_t=C\cup\{a_1,\ldots ,a_t\}
          \cup\{b_{t+1},\ldots ,b_h\},
          \qquad 0\le t\le h.                         \tag{0.1}
\]

Fix conservative incoming queue supports

\[
 I\subset X,\quad |I|=f,
 \qquad R\subset X^c,\quad |R|=g.                    \tag{0.2}
\]

The safe orbit paths are exactly the paths in the sector

\[
 \Omega_{I,R}=\{Y\in\Omega_m:I\subseteq Y, R\cap Y=\varnothing\}
                                                               \tag{0.3}
\]

whose active coordinates avoid \(I\cup R\).  Their oriented owner
hypergraph is regular of degree

\[
 D_{f,g,h}=(h+1)(m-f)_h(m-g)_h.                       \tag{0.4}
\]

If two sector owners have Johnson distance \(d\le h\), their exact
codegree-to-degree ratio is

\[
 \boxed{
 \rho_d={2(h-d+1)\over h+1}
       {1\over \binom{m-f}d\binom{m-g}d}.}             \tag{0.5}
\]

It is zero for \(d>h\).  In the Gaussian core, and more generally when
\(2h\le\min(m-f,m-g)\),

\[
                  \rho:=\max_{X\ne Y}\rho(X,Y)
                  \le {2\over(m-f)(m-g)}.              \tag{0.6}
\]

Consequently every owner set \(S\subseteq\Omega_{I,R}\), \(|S|=s\),
has normalized mass at least

\[
                         s-\rho s(s-1)                  \tag{0.7}
\]

of safe orbit paths meeting \(S\) exactly once.  Thus no owner subset of
size \(o((m-f)(m-g))\) is closed against one-owner escape.  In particular
no parity or odd-sector cut supported on such a subset survives the
complete orbit.  This statement does not exclude nonlinear Hall,
stable-set-rank, or semigroup cuts involving a large family of
overlapping paths.

There is nevertheless an exact integral obstruction after dynamic queue
filtering.  If every next path must avoid one common coordinate set
\(Z\), then paths cannot change \(X\cap Z\).  The owner layer splits into
the \(2^{|Z|}\) sectors

\[
                         \Omega_Q=\{X:X\cap Z=Q\}.       \tag{0.8}
\]

For infinitely many odd \(m\), one may choose \(z=|Z|=o(m)\) such that
every \(|\Omega_Q|\) is odd.  Every product-SCD diagonal then has an even
number of owners, so every integral safe path packing leaves at least one
owner in every sector:

\[
                         L_{\rm int}\ge2^z.              \tag{0.9}
\]

On the other hand, each sector has an exact regular fractional perfect
matching.  Hence (0.9) is a literal odd-sector integrality gap which
pointwise orbit averaging cannot see.

The obstruction is sharp but subcritical.  If \(z=O(H)=o(m)\), then

\[
                         2^z=o(W/H),
             \qquad W=\binom{2m}m.                       \tag{0.10}
\]

Thus it refutes an **exact** rounding theorem from biregularity alone,
but it does not refute the coefficient-one near-atlas target.  Its entire
**parity lower bound** is only \(o(W/H)\); this does not itself construct a
packing attaining that bound.  Any coefficient-scale
obstruction must therefore be a simultaneous cross-history rank cut, not
a group-invariant parity or a bounded odd gadget.

## 1. The complete monotone-path orbit

An oriented monotone Johnson \(h\)-path is specified by disjoint ordered
lists

\[
             (a_1,\ldots ,a_h),\qquad(b_1,\ldots ,b_h)
\]

and a set \(C\), disjoint from both lists, of size \(m-h\).  Its vertices
are (0.1); the \(t\)-th edge removes \(b_{t+1}\) and inserts
\(a_{t+1}\).

### Lemma 1.1 (one product diagonal generates the complete orbit)

The labelled \(S_{2m}\)-orbit of any one oriented product-SCD diagonal
of length \(h\) is precisely the family \({\cal G}_h\) of all paths
(0.1).

#### Proof

A product-SCD diagonal has an \((m-h)\)-set of coordinates fixed to one,
an ordered \(h\)-set of inserted coordinates, an ordered \(h\)-set of
removed coordinates, and an exterior \((m-h)\)-set fixed to zero.  These
four pieces partition \([2m]\).  A coordinate permutation may send this
ordered partition to any other ordered partition with the same part
sizes, position by position on the two ordered parts.  This gives every
path (0.1), and a coordinate permutation plainly preserves the form
(0.1). \(\square\)

This is the point at which the full orbit differs from a bounded
catalogue of fixed BTK frames: the active alphabets and their two orders
are completely free.

## 2. Conservative queue filtering is a smaller complete orbit

Let \(I,R\) be disjoint sets with sizes \(f,g\), respectively forced
present and forced absent.  Put

\[
 n_+=m-f,
 \qquad n_-=m-g.                                      \tag{2.1}
\]

The free ground set has size \(n_++n_-\), and a sector owner has
\(n_+\) free present coordinates and \(n_-\) free absent coordinates.

### Lemma 2.1 (exact safe sector)

Suppose the incoming insertion support is \(I\subset X\) and the
incoming removal support is \(R\subset X^c\).  A full path passes the
conservative whole-support test if and only if none of its removed
coordinates lies in \(I\) and none of its inserted coordinates lies in
\(R\).  Equivalently, all of its vertices lie in \(\Omega_{I,R}\), and
after deleting the fixed labels \(I\cup R\) it is an arbitrary monotone
\(h\)-path on the free ground set.

#### Proof

An insertion in the incoming queue may not be removed while it remains
live, and a removal in the incoming queue may not be reinserted.  These
are exactly the two exclusions in the first sentence.  Since \(I\) is
initially present and \(R\) initially absent, those exclusions keep
\(I\) present and \(R\) absent throughout the path.  Conversely, a path
inside (0.3) never uses either kind of forbidden coordinate.  Lemma 1.1
on the remaining labels gives every such free path. \(\square\)

The conservative test is stronger than the age-sensitive test, but every
path retained here is a literal signed-safe option.

## 3. Exact degrees and codegrees

Write \((u)_v=u(u-1)\cdots(u-v+1)\).

### Theorem 3.1 (safe-orbit census)

Assume \(1\le h\le\min(n_+,n_-)\).  The oriented path hypergraph on
\(\Omega_{I,R}\) has degree (0.4).  If \(X,Y\) have Johnson distance
\(d\), their codegree is zero for \(d>h\), while for \(1\le d\le h\)
it is

\[
 \lambda_d
  =2(h-d+1)(d!)^2(n_+-d)_{h-d}(n_--d)_{h-d}.          \tag{3.1}
\]

Consequently (0.5) holds.

#### Proof

Fix an owner \(X\) and prescribe that it occurs at position \(t\).
Among its \(n_+\) free present labels, choose and order the \(t\) labels
inserted before \(X\) and the \(h-t\) labels removed after \(X\).  The
number of choices is \((n_+)_h\).  Independently, among its \(n_-\) free
absent labels choose and order the \(t\) labels removed before \(X\) and
the \(h-t\) labels inserted after \(X\).  This gives \((n_-)_h\)
choices.  Sum over \(0\le t\le h\) to obtain (0.4).

Now orient a common path from \(X\) to \(Y\).  Their positions must
differ by exactly \(d\), because every monotone step increases their
mutual Johnson distance by one until \(Y\) is reached.  The \(d\)
middle removals are the elements of \(X\setminus Y\), in any of \(d!\)
orders, and the \(d\) middle insertions are the elements of
\(Y\setminus X\), again in any of \(d!\) orders.

If there are \(s\) steps before \(X\), there are \(h-d-s\) after
\(Y\).  The remaining present-side labels can be chosen and ordered in
\((n_+-d)_{h-d}\) ways, independently of \(s\); the absent-side count is
\((n_--d)_{h-d}\).  There are \(h-d+1\) choices of \(s\).  Finally
there are two orientations, giving (3.1).

Divide by (0.4) and use

\[
 (n_\pm)_h=(n_\pm)_d(n_\pm-d)_{h-d},
 \qquad {(d!)^2\over(n_+)_d(n_-)_d}
       ={1\over\binom{n_+}d\binom{n_-}d}.
\]

This is (0.5).  If \(2h\le\min(n_+,n_-)\), then
\(\binom{n_\pm}d\ge n_\pm\) for \(1\le d\le h\).  Formula (0.5) then
gives (0.6). \(\square\)

### Corollary 3.2 (singleton escape from every small owner set)

Give every oriented path weight \(1/D_{f,g,h}\).  For every
\(S\subseteq\Omega_{I,R}\), \(|S|=s\), the total weight of paths meeting
\(S\) exactly once is at least (0.7).

#### Proof

If \(r_P=|P\cap S|\), double-counting owner pairs and using (0.6) gives

\[
 \sum_P\binom{r_P}2{1\over D_{f,g,h}}
 \le \rho\binom s2.                                      \tag{3.2}
\]

Regularity gives

\[
                         s=\sum_Pr_P/D_{f,g,h}.             \tag{3.3}
\]

For \(r\ge2\), \(r\le2\binom r2\).  Hence the contribution in (3.3)
from paths meeting \(S\) at least twice is at most
\(2\rho\binom s2=\rho s(s-1)\).  The remaining contribution is exactly
the weight of the one-hit paths. \(\square\)

In particular, a family \(S\) with no one-hit path must have

\[
                         s\ge1+\rho^{-1}
                         \ge1+{(m-f)(m-g)\over2}.            \tag{3.4}
\]

Thus determinant-two triangles and every Gaussian-size anchor gadget
have overwhelming cross-gadget escape in the complete safe orbit.

### Corollary 3.3 (simple design and its nibble parameter)

Assume \(2h\le\min(m-f,m-g)\).
After identifying a path with its reversal, the safe-orbit hypergraph is
a simple \((h+1)\)-uniform, \(D_{f,g,h}/2\)-regular hypergraph.  Its
maximum codegree \(\Delta_2\) satisfies

\[
 {\Delta_2\over D_{f,g,h}/2}
 \le {2\over(m-f)(m-g)},
 \qquad
 {(h+1)^2\Delta_2\over D_{f,g,h}/2}
 \le {2(h+1)^2\over(m-f)(m-g)}.                    \tag{3.5}
\]

In the Gaussian path core, with \(f,g=o(m)\) and
\(h=m^{1/2+o(1)}\), the second ratio is \(m^{-1+o(1)}\).

#### Proof

On the owner set of a monotone path, two vertices at positions \(i,j\)
have Johnson distance \(|i-j|\).  Hence the Johnson graph induced by the
path owners is exactly a path: consecutive vertices are adjacent and
there are no chords.  Its order is therefore determined by the owner set
up to reversal.  Every unoriented path occurs in exactly two orientations,
so dividing degrees and codegrees by two preserves their ratio.  Apply
(0.6). \(\square\)

Thus the owner-only design satisfies the natural growing-uniformity
small-overlap condition \((h+1)^2\Delta_2/D=o(1)\).  A fixed-uniformity
nibble theorem cannot simply be quoted uniformly in the growing value
\(h+1\), and an unspecified \(o(|\Omega_{I,R}|)\) leave would not imply
the required \(o(W/H)\) global leave.  More importantly, the dynamic
problem is a union of differently filtered sectors and carries endpoint
and all-depth target claims.  Equation (3.5) therefore identifies a
favourable owner-only input, not an applicable theorem that completes
the requested rounding.

Corollary 3.2 controls only cuts witnessed by the absence of one-hit
paths.  It does **not** bound the full matching rank function, prove
semigroup normality, or rule out nonlinear Hall cuts on exponentially
many paths.

## 4. The complete mod-two kernel

Let \(A_h\) be the owner-by-path incidence matrix of the safe sector,
viewed over \(\mathbb F_2\).

### Theorem 4.1 (only the total-sector parity survives)

Assume

\[
                  1\le h\le\min(n_+,n_-)-1.                \tag{4.1}
\]

Then

\[
 \ker(A_h^{\mathsf T})=
 \begin{cases}
   \{0\},&h\text{ even},\\
   \langle\mathbf1\rangle,&h\text{ odd}.
 \end{cases}                                                \tag{4.2}
\]

More generally, for every abelian group \(G\), any owner function
\(\varphi:\Omega_{I,R}\to G\) whose sum is the same on every safe
\(h\)-path is constant.

#### Proof

Let \(Y,Y'\) be adjacent sector owners and write their free parts as

\[
                         K+u,\qquad K+v.
\]

Choose a free absent label \(w\notin K\cup\{u,v\}\) and put
\(Z=K+w\).  Condition (4.1) permits a monotone path of length \(h-1\)
ending at \(Z\), using neither \(u\), \(v\), nor \(w\): choose its
past inserted labels from the \(n_+-1\) present labels other than \(w\),
and its past removed labels from the \(n_--2\) absent labels other than
\(u,v\).  The two extensions

\[
                         Z-w+u=Y,
             \qquad      Z-w+v=Y'                              \tag{4.3}
\]

are safe \(h\)-paths sharing their first \(h\) vertices.

If \(\varphi\), with values in an arbitrary abelian group, has the same
path sum on all paths, comparison of these
two paths gives \(\varphi(Y)=\varphi(Y')\).  The Johnson graph on the
sector is connected, so \(\varphi\) is constant.  The all-one function
has path sum \(h+1\) modulo two.  It belongs to the kernel exactly when
\(h\) is odd, proving (4.2). \(\square\)

### Corollary 4.2 (all owner-linear congruences are total congruences)

For every modulus \(q\), the left kernel of the incidence matrix over
\(\mathbb Z/q\mathbb Z\) consists precisely of the constant vectors
\(c\mathbf1\) satisfying

\[
                              (h+1)c=0.                       \tag{4.4}
\]

Thus every owner-linear modular obstruction to an exact safe-sector
factor is a divisibility condition on the total sector cardinality.
There is no coordinate-sensitive or locally supported linear congruence.

#### Proof

Apply the abelian-group assertion of Theorem 4.1 to a function with zero
sum on every path.  It is constant, and a constant function has zero path
sum exactly under (4.4). \(\square\)

For the unfiltered full orbit, \(|\Omega_m|=\binom{2m}m\) is even for
every \(m\ge1\).  Hence even the sole kernel vector when \(h\) is odd
does not obstruct an exact cover: its necessary right-hand-side parity
is automatically satisfied.  There is no nontrivial full-group parity
cut hidden behind the orbit average.

## 5. A genuine dynamic odd-sector obstruction

The preceding theorem also identifies exactly how a parity cut can be
created: queue filtering may disconnect the owner graph into sectors.

Fix \(Z\subset[2m]\), \(|Z|=z\), and retain only paths whose active
labels avoid \(Z\).  Then \(X\cap Z\) is constant along every path, so
the safe hypergraph is the disjoint union of (0.8), with

\[
                         |\Omega_Q|
                 =\binom{2m-z}{m-|Q|}.                    \tag{5.1}
\]

### Theorem 5.1 (replicated odd-sector cut)

Let

\[
 m=2^{t}+d,qquad
 z=2d+1,qquad
 1\le d\le2^t-1,                                           \tag{5.2}
\]

where \(d\) is odd.  Suppose \(h\equiv m\pmod2\) and
\(1\le h\le m-z\).  Then:

1. every one of the \(2^z\) sectors \(\Omega_Q\) is nonempty and has
   odd cardinality;
2. every safe product path has even cardinality; and
3. every integral owner-disjoint safe path packing leaves at least
   \(2^z\) owners uncovered.

Nevertheless, for each fixed admissible length \(h\), every sector has
the regular fractional perfect matching assigning weight
\(1/D_{|Q|,z-|Q|,h}\) to each of its oriented paths.

#### Proof

From (5.2),

\[
                         2m-z=2^{t+1}-1.                    \tag{5.3}
\]

The inequalities on \(d\) imply
\(0\le m-|Q|\le2m-z\) for every \(Q\subseteq Z\), so every sector is
nonempty.  Over \(\mathbb F_2\),

\[
 (1+x)^{2^{t+1}-1}
   =\prod_{j=0}^{t}(1+x^{2^j}),                              \tag{5.4}
\]

whose coefficients are all one.  Therefore every binomial coefficient
in row \(2^{t+1}-1\), and in particular every number in (5.1), is odd.

Since \(m\) and \(h\) are odd, a length-\(h\) path has \(h+1\) even
vertices.  More generally every product-SCD diagonal length has the form
\(m-2r\), so all nonempty product diagonals have even owner cardinality.
Every selected path stays in one sector.  The number of covered owners
in that sector is consequently even, while its total cardinality is odd;
at least one owner is uncovered.  Summing over all \(2^z\) sectors proves
(0.9).

Finally, \(h\le m-z\) makes Theorem 3.1 applicable in every sector.
Its regular weight covers each sector owner to total weight one. \(\square\)

The integral inequality exposed by the proof is literal.  If \(e_X\)
is the uncovered-owner indicator, then every integral safe packing obeys

\[
                         \sum_{X\in\Omega_Q}e_X\ge1
                         \qquad(Q\subseteq Z),               \tag{5.5}
\]

whereas the regular fractional matching has \(e_X=0\).  These are
\(2^z\) independent odd-sector cuts.

### Lemma 5.2 (the frozen-support states are pointwise reachable)

Assume \(z\le H-1\) and \(z\le m\).  For every owner \(X\), there is a
signed-safe length-\(z\) history ending at \(X\) whose live insertion and
removal support union contains \(Z\).

#### Proof

Choose \(A_X\subseteq X\) and \(B_X\subseteq X^c\), both of size \(z\),
so that

\[
                         X\cap Z\subseteq A_X,
              \qquad     Z\setminus X\subseteq B_X.          \tag{5.6}
\]

The choices are possible because \(z\le m\).  Start at

\[
                         (X\setminus A_X)\cup B_X
\]

and, in any bijected order, remove every label of \(B_X\) once and
insert every label of \(A_X\) once.  No physical coordinate is reused,
so the word is safe for both signs.  At its endpoint the last \(z\)
insertions and removals are precisely \(A_X,B_X\), whose union contains
\(Z\).  Since \(z\le H-1\), all remain live. \(\square\)

Thus the odd-sector cut is compatible with every state separately and
with the exact two-queue chronology.  Lemma 5.2 does **not** assert that
all these histories can themselves be selected simultaneously as one
owner-disjoint preceding atlas.  Accordingly, Theorem 5.1 refutes a
rounding theorem based only on pointwise reachability and orbit
biregularity; it is not a coherent-route no-go.

There is a second distinction.  The exact regular fractional matching in
Theorem 5.1 belongs to the common-\(Z\) filter.  Lemma 5.2 pads the two
chronological queues to equal lengths by owner-dependent labels outside
\(Z\).  Those labels can delete further path options.  The parity cut
survives every such deletion, but regular fractional feasibility for the
more restrictive, root-dependent family is not asserted.  In a fixed
cross-half product block the irrelevant padding can be placed on inactive
halves, which recovers the projected \((f,g)\) model exactly; in the fully
unrestricted \(S_{2m}\) path orbit this requires a separate grouping
argument.

If a following path has length at most \(h\) and

\[
                              z+h\le H,                       \tag{5.7}
\]

then every label of \(Z\) is still live throughout that following path.
In this range, avoidance of \(Z\) is forced by the exact age-sensitive
two-queue rule, not merely by the conservative whole-support test.  When
(5.7) fails, Theorem 5.1 remains an exact obstruction for the
conservative option subcatalogue, but later use of an expired \(Z\)-label
can connect its sectors.

## 6. Exact asymptotic accounting

### Proposition 6.1 (all common-support parity repairs are cheap)

If \(z=o(m)\), then

\[
                         2^z=o(W/H)                            \tag{6.1}
\]

for every \(H\le\exp(o(m))\).  In particular this holds at
\(H=\sqrt m\log\log m\).  Even allowing at most \(h\) additional
uncovered owners per sector costs

\[
                         h2^z=o(W/H)                           \tag{6.2}
\]

whenever \(h,H\le\exp(o(m))\).

#### Proof

The largest binomial coefficient in row \(2m\) is at least the row
average, so

\[
                         W\ge{4^m\over2m+1}.                  \tag{6.3}
\]

Therefore

\[
 {Hh2^z\over W}
 \le Hh(2m+1)2^{z-2m}=o(1),                                 \tag{6.4}
\]

because \(z=o(m)\) and \(Hh=\exp(o(m))\).  Equation (6.1) is the case
\(h=1\). \(\square\)

At the coefficient-one scale, therefore, the exact odd-sector
parity deficit is small enough to be reserved for residual singletons or
an absorber without changing the required ledger.  Proposition 6.1 does
not construct the packing of the remaining owners.  What Theorem 5.1
forbids is the stronger claim that the biregular fractional orbit always
rounds **exactly**.

## 7. Proved boundary

The following statements are proved.

1. The full coordinate orbit of one product diagonal is the complete
   monotone-path design.
2. After fixing conservative queue supports, its owner degree and every
   pair codegree are exactly (0.4)--(0.5).
3. Every owner family of size \(o(m^2)\) has essentially full one-hit
   escape, so no bounded or Gaussian-size closed parity gadget survives.
4. Within one safe sector, every owner-linear modular invariant is a
   total-sector divisibility invariant; mod two this is just sector
   parity.
5. A common dynamically forbidden coordinate set can create
   \(2^z\) literal odd-sector cuts and a genuine fractional-versus-integral
   gap.
6. For \(z=O(H)=o(m)\), the total cost of all those cuts is
   \(o(W/H)\).

The following statements are not proved.

1. A nibble or group-design theorem selecting paths from different queue
   sectors simultaneously.
2. Joint owner-disjoint realization of the pointwise histories in
   Lemma 5.2.
3. Preservation of the dynamic empty-rectangle expansion after many
   integral selections.
4. Coefficient one.

Nor is any nonlinear Hall, weighted-rank, or affine-semigroup inequality
classified here.  The mod-two kernel theorem is not a matching-polytope
description.

Thus fractional averaging is indeed insufficient: it misses the exact
odd-sector cuts (5.5).  But those cuts are too small to close the
coefficient-one lane.  The surviving integral problem is a quantitative
cross-history matching theorem with an \(o(W/H)\) reserve, not an exact
SCD factorization and not a local parity audit.
