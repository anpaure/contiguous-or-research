# Rank-two queue owner incidence: exact codegrees and the fixed-density boundary

**Date:** 2026-08-07  
**Method:** orbit incidence counting, ternary omission states, and the
variable-uniformity Grable--Kostochka--Rödl estimate  
**Status:** unconditional owner-incidence theorem and proof-safe theorem
boundary. The owner-only queue makes the formal Grable codegree parameter
tend to zero. The published constants are not uniform in the growing edge
rank, so this is not itself an application of that theorem; moreover even
an optimistic diagonal reading of its displayed error scale would be too
weak to supply the fixed positive density required by the PBBS reset
ledger. Adding every marked target layer at once returns to the
constant-critical regime.

## 0. Outcome

Use the odd parameters

\[
n=2m+1,\qquad p=d+1,\qquad \ell=3p,
\tag{0.1}
\]

and the rank-two block queue of
`MATH_THEOREM_RANK2_BLOCK_QUEUE_FLAT_OWNER_RESET_20260807.md`.
The queue has \(\ell\) distinct rank-\(m\) owners.

Let \(\mathcal H_Q\) be the hypergraph on

\[
\mathcal V={{[n]}\choose m}
\tag{0.2}
\]

whose edges are all coordinate-labelled copies of one queue owner ring.
Then:

1. \(\mathcal H_Q\) is regular and \(\ell\)-uniform.
2. Its exact maximum relative pair codegree is

   \[
   \boxed{\frac{\Delta_2(\mathcal H_Q)}D=\frac2{m(m+1)}.}
   \tag{0.3}
   \]

3. Consequently the Grable parameter is

   \[
   \boxed{
   \eta_Q:=\frac{\ell\Delta_2\log W}{D}
      =(12\log2+o(1))\frac pm=\Theta(m^{-1/2})=o(1),}
   \qquad W={n\choose m}.
   \tag{0.4}
   \]

   Thus this queue, unlike a length-\(\Theta(m)\) carousel, clears the
   **numerical** Grable codegree expression. This does not authorize a
   diagonal use of a theorem whose constants depend on the uniformity.

4. That does **not** imply a matching covering a fixed positive fraction
   of \(\mathcal V\). If one formally substitutes the growing parameters
   into the fixed-uniformity displayed leave scale, one obtains

   \[
   W\,\eta_Q^{1/(2\ell-1+o(\ell))},
   \tag{0.5}
   \]

   and

   \[
   \eta_Q^{1/(2\ell-1+o(\ell))}
      =\exp\!\left[-\Theta\!\left(\frac{\log m}{\sqrt m}\right)\right]
      =1-o(1).
   \tag{0.6}
   \]

   The improvement of the factor in (0.5) below one is only
   \(\Theta(\log m/\sqrt m)\). Thus even an optimistic uniform reading
   would reach only a \(\Theta(W\log m/\sqrt m)\)-scale covered set, and
   that reading is not a published theorem. This scale tends to zero as a
   fraction of \(W\), whereas the reset ledger asks for
   \((\theta+o(1))W\) owners with fixed

   \[
   \theta=4\sum_{a\ge1}e^{-4\pi a^2}>0.
   \tag{0.7}
   \]

5. If the owner row and all \(d\) marked suffix-target rows are put into
   one edge, its uniformity is

   \[
   \kappa=3p^2=\Theta(m).
   \tag{0.8}
   \]

   The inherited owner-neighbour codegree alone makes the corresponding
   Grable parameter bounded away from zero. Hence the naive combined
   owner-plus-target hypergraph does not even pass the hypothesis.

The exact owner-packing statement still missing is therefore:

> **Fixed-density rank-two queue packing.** The actual queue-copy
> hypergraph has a matching covering at least
> \((\theta+o(1))W\) owner vertices.

The result below removes the earlier codegree obstruction, but it does not
prove this statement.

## 1. The abstract ternary queue

Let \(K_0\) be an abstract core of size

\[
c=m-2p,
\tag{1.1}
\]

and split a bank into labelled triples

\[
F_0=S_0\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}S_{p-1},
\qquad S_a=\{x_{a,0},x_{a,1},x_{a,2}\}.
\tag{1.2}
\]

Thus

\[
|K_0\cup F_0|=m+p.
\tag{1.3}
\]

At time \(t=qp+a\), where \(q\in\mathbb Z_3\) and
\(0\le a<p\), define the omission state

\[
\varepsilon_{q,a}(b)=
\begin{cases}
q,&b\le a,\\
q-1,&b>a,
\end{cases}
\qquad b\in\mathbb Z_p,
\tag{1.4}
\]

with values read modulo three, and put

\[
Q_{q,a}=\bigcup_{b=0}^{p-1}
\bigl(S_b\setminus\{x_{b,\varepsilon_{q,a}(b)}\}\bigr),
\qquad O_{q,a}=K_0\cup Q_{q,a}.
\tag{1.5}
\]

There are \(\ell=3p\) owners, each of size \(m\). Formula (1.4) is
exactly the owner chronology obtained by moving a \(p\)-letter window
through the rank-two queue.

For two owners, their Johnson distance is the Hamming distance of their
omission vectors:

\[
d_J(O_{q,a},O_{q',a'})
=\bigl|\{b:\varepsilon_{q,a}(b)\ne
\varepsilon_{q',a'}(b)\}\bigr|.
\tag{1.6}
\]

For \(1\le r\le p\), let \(a_r\) denote the number of ordered pairs of
distinct abstract owners at Johnson distance \(r\). Then

\[
\sum_{r=1}^{p}a_r=\ell(\ell-1).
\tag{1.7}
\]

## 2. Exact degree and codegree

Initially retain coordinate-labelled embeddings: for every injection

\[
\phi:K_0\cup F_0\hookrightarrow[n]
\tag{2.1}
\]

take the edge

\[
E_\phi=\{\phi(O_{q,a}):q\in\mathbb Z_3,\ 0\le a<p\}.
\tag{2.2}
\]

This is a parameterized multihypergraph. Collapsing coincident copies
divides every degree and codegree by the same automorphism multiplicity:
the union of an edge recovers its coordinate support, and two embeddings
with the same edge differ by an automorphism of the abstract owner
configuration. Thus all normalized conclusions below also hold in the
simple copy hypergraph.

### Theorem 2.1 (exact queue incidence formula)

The parameterized hypergraph is regular of degree

\[
\boxed{D=\ell\,m!\,(m+1)_p.}
\tag{2.3}
\]

If \(X,Y\in\mathcal V\) have Johnson distance \(r\), then their
codegree is zero for \(r>p\), while for \(1\le r\le p\),

\[
\boxed{D(X,Y)=a_r(m-r)!(r!)^2(m+1-r)_{p-r}.}
\tag{2.4}
\]

Equivalently,

\[
\boxed{
\frac{D(X,Y)}D
=\frac{a_r/\ell}{{m\choose r}{m+1\choose r}}.}
\tag{2.5}
\]

#### Proof

Fix \(X\). Choose its abstract owner position, biject that owner's
\(m\) coordinates with \(X\), and inject the remaining \(p\) support
coordinates into \([n]\setminus X\). This gives (2.3).

For an ordered pair at distance \(r\), biject the common part and the two
ordered differences, contributing

\[
(m-r)!(r!)^2.
\]

The remaining \(p-r\) support coordinates inject outside \(X\cup Y\),
giving (2.4). Dividing by (2.3) gives (2.5). \(\square\)

## 3. The distance-one inventory

### Theorem 3.1 (only cycle neighbours have distance one)

For \(p\ge2\),

\[
\boxed{a_1=2\ell.}
\tag{3.1}
\]

Consequently, for all sufficiently large \(m\),

\[
\boxed{
\frac{\Delta_2(\mathcal H_Q)}D
=\frac2{m(m+1)}.}
\tag{3.2}
\]

#### Proof

Moving one step around the owner cycle increments one omission coordinate
modulo three. Consider two states separated by \(u\) update steps, with
\(1\le u\le3p-1\).

If \(1\le u\le p\), exactly \(u\) coordinates have been updated once.
If \(p<u<2p\), every coordinate has been updated once or twice, so all
\(p\) omission coordinates differ. If \(2p\le u\le3p-1\), exactly
\(3p-u\) coordinates have been updated twice rather than three times.
Therefore the Hamming distance equals one only when

\[
u=1\quad\hbox{or}\quad u=3p-1.
\]

These are precisely the two oriented cycle neighbours of each owner, so
(3.1) follows.

At \(r=1\), (2.5) gives (3.2). For \(r\ge2\), the coarse bound
\(a_r/\ell\le\ell-1\) gives

\[
\frac{D(X,Y)}D
\le\frac{\ell-1}{{m\choose2}{m+1\choose2}}
=O(m^{-7/2}),
\tag{3.3}
\]

because \(\ell=\Theta(\sqrt m)\). Hence the distance-one value is the
maximum for large \(m\). \(\square\)

### Corollary 3.2 (exact fractional owner factor)

Giving every parameterized copy weight \(1/D\) is a fractional perfect
matching. Its total weight is \(W/\ell\).

This closes the scalar and fractional owner rows exactly.

## 4. The formal Grable boundary and the nonuniformity warning

The numerical Grable--Kostochka--Rödl codegree expression, in the present
notation, is

\[
\Delta_2=o(D/(\ell\log W)).
\tag{4.1}
\]

By (3.2) and

\[
\log W=(2\log2+o(1))m,
\tag{4.2}
\]

the dimensionless left side is exactly (0.4), and therefore tends to
zero. This is a genuine arithmetic improvement over the
length-\(\Theta(m)\) carousel, whose corresponding parameter stays bounded
away from zero.

For every fixed uniformity, the theorem has a displayed uncovered scale of
the form

\[
W\left(\frac{\ell\Delta_2\log W}{D}\right)^{
1/(2\ell-1+o(\ell))}.
\tag{4.3}
\]

Since \(p=d+1=\Theta(\sqrt m)\),

\[
\begin{aligned}
\log\eta_Q&=-\tfrac12\log m+O(1),\\
\frac{\log\eta_Q}{2\ell-1+o(\ell)}
&=-\Theta(\log m/\sqrt m).
\end{aligned}
\tag{4.4}
\]

This proves the formal estimate (0.6). The theorem's thresholds and error
constants are not uniform in \(\ell\), so (4.3) cannot be cited diagonally.
Even if that nonuniformity were ignored, its formal scale would still not
give a fixed-density queue packing. A fixed positive density needs either
a genuinely uniform matching theorem or a queue-specific packing argument.

The primary references for this boundary are:

- D. A. Grable, *More-than-nearly-perfect packings and partial designs*,
  Combinatorica 19 (1999), 221--239;
- A. V. Kostochka and V. Rödl, *Partial Steiner systems and matchings in
  hypergraphs*, Random Structures & Algorithms 13 (1998), 335--347.

## 5. Adding the named target rows

At proper suffix depth \(1\le j<p\), every queue target has rank

\[
r_j=m-2p+2j,
\tag{5.1}
\]

and the owner layer is \(r_p=m\). A full queue edge contains \(\ell\)
vertices in every one of the \(p\) layers. Hence its total size is

\[
\kappa=p\ell=3p^2.
\tag{5.2}
\]

The raw degrees in layer \(j\) are

\[
D_j=\ell\,r_j!\,(n-r_j)_{m+p-r_j},
\tag{5.3}
\]

up to the same configuration-automorphism divisor. Equivalently,

\[
\frac{D_j}{D_p}
=\frac{{n\choose m}}{{n\choose r_j}}.
\tag{5.4}
\]

Thus the augmented hypergraph is not literally regular, although all its
layer degrees differ by only constant factors. Indeed the smallest layer
is \(r_1=s=m-2d\), and the queue theorem gives

\[
\frac{{n\choose s}}W\longrightarrow e^{-\pi}.
\tag{5.5}
\]

The owner-neighbour pair from Theorem 3.1 is still present and has
codegree \(2D_p/[m(m+1)]\). Even normalizing by the largest layer degree,
(5.4)--(5.5) give

\[
\frac{\Delta_2^{\rm aug}}{D_{\max}}
\ge\frac{2e^{-\pi}+o(1)}{m^2}.
\tag{5.6}
\]

Moreover

\[
\log\left(\sum_{j=1}^{p}{n\choose r_j}\right)
=(2\log2+o(1))m.
\tag{5.7}
\]

At triangular depth \(p^2/m\to\pi/4\). Combining
(5.2), (5.6), and (5.7) yields

\[
\liminf
\frac{\kappa\Delta_2^{\rm aug}}{D_{\max}}
\log\left(\sum_{j=1}^{p}{n\choose r_j}\right)
\ge3\pi e^{-\pi}\log2>0.
\tag{5.8}
\]

Therefore the naive all-resource edge is constant-critical and fails the
little-\(o\) hypothesis before any more delicate target--target or
owner--target collision is counted.

This does not prove that simultaneous owner/target packing is impossible.
It proves only that it cannot be obtained by putting all rows into one raw
edge and invoking the same Grable theorem.

## 6. Exact remaining boundary

The owner-only computation has now removed two possible false barriers:

1. there is no scalar shortage, because the uniform fractional perfect
   owner factor is exact;
2. there is no constant-critical obstruction in the numerical Grable
   parameter, because \(\ell\Delta_2\log W/D\to0\).

The surviving owner theorem is nevertheless integral:

\[
\boxed{
\nu(\mathcal H_Q)\,\ell\ge(\theta+o(1))W.}
\tag{6.1}
\]

No published growing-uniformity theorem currently implies (6.1) from these
rows. A successful next step must exploit the full ternary omission
geometry, prove a hereditary short-time nibble for a fixed positive time,
or give a deterministic overlapping-core packing.

After (6.1), the target rows cannot simply be appended to the matching
edge: Section 5 shows that this loses the growing-uniformity advantage.
They require a second-stage target assignment, a compressed chain token,
or a queue-specific correlated nibble which treats each full rank-two
chain internally rather than as \(d\) independent resources.

Accordingly, this note closes the exact owner incidence calculation but
does **not** prove the rank-two rolling block-factor theorem or
\(\nu(k)\le B(k)+O(1)\).
