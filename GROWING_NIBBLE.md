# Growing-uniformity matching audit for the pair-flip blocks

This note audits only the matching step in `RANK_BALANCED_BLOCKS.md`.  It
does **not** claim a new block packing.  Its main conclusions are:

1. the pair-codegree estimate can be sharpened exactly;
2. the full `2m` block has an antipodal degeneracy which must be quotiented or
   avoided;
3. partial blocks of length `2 ell`, with `ell<m`, have
   `Delta_2/D=2/m^2` exactly;
4. nevertheless, every general matching theorem located in the audit either
   fixes the uniformity or has a quantitative hypothesis which the required
   growing blocks do not satisfy; and
5. the weakest useful missing result is an object-specific near-factor lemma,
   or equivalently a growing-uniformity version of the full-codegree nibble
   whose parameter is `B=Theta(m/ell)`, not merely a theorem about pair
   codegrees.

Throughout, put

\[
 W=\binom{2m}{m},\qquad 2\leq \ell\leq m,
 \qquad (m)_\ell=m(m-1)\cdots(m-\ell+1).
\]

## 1. The partial pair-flip hypergraph

Let `H_(m,ell)` have vertex set `binom([2m],m)`.  A parameter edge is
specified by

* a middle set `X`;
* an ordered `ell`-tuple `(a_0,...,a_(ell-1))` of distinct elements of `X`;
* an ordered `ell`-tuple `(b_0,...,b_(ell-1))` of distinct elements outside
  `X`.

Starting at `X`, flip `a_i` to `b_i` in order and then flip `b_i` back to
`a_i` in the same order.  The resulting `2 ell` distinct middle sets form
one hyperedge.  Parameter choices are retained as parallel edges.

There are

\[
 e(H_{m,\ell})=W(m)_\ell^2
\]

parameter edges.  Transitivity and double counting therefore give the exact
degree

\[
 \boxed{D=2\ell(m)_\ell^2}.                         \tag{1.1}
\]

### Theorem 1 (exact pair codegrees)

Let `A,B` be distinct middle sets and put

\[
 q=|A\setminus B|=|B\setminus A|.
\]

If `q>ell`, their codegree is zero.  If `1<=q<ell`, then

\[
 \lambda_q
 =4\ell\,[q!(m-q)_{\ell-q}]^2,
 \qquad
 \frac{\lambda_q}{D}=\frac{2}{\binom mq^2}.          \tag{1.2}
\]

At the antipodal distance inside the active cube, `q=ell`,

\[
 \lambda_\ell=2\ell(\ell!)^2,
 \qquad
 \frac{\lambda_\ell}{D}=\frac{1}{\binom m\ell^2}.   \tag{1.3}
\]

Consequently, when `2<=ell<m`,

\[
 \boxed{\frac{\Delta_2(H_{m,\ell})}{D}=\frac{2}{m^2}}. \tag{1.4}
\]

#### Proof

Suppose first that `q<ell`.  In a block containing both `A` and `B`, their
two positions have cyclic separation `q` in one of the two directions.
There are `2ell` choices for the position of `A` and two choices of direction.
For fixed positions, the `q` transition slots between them receive the
elements of `A\B` and `B\A` in `(q!)^2` ways.  The other `ell-q` active slots
receive distinct elements from `A cap B` and from the complement of
`A union B` in `(m-q)_(ell-q)^2` ways.  This proves the first formula in
(1.2).  Dividing by (1.1), and using

\[
 \frac{q!(m-q)_{\ell-q}}{(m)_\ell}
 =\frac{q!(m-q)!}{m!}=\binom mq^{-1},
\]

proves the second.

When `q=ell`, the two positions are separated by exactly half the block, so
there is only one direction for each of the `2ell` first positions.  The
active tuples may be ordered in `(ell!)^2` ways, proving (1.3).  No two states
of a block differ in more than `ell` elements, proving the zero assertion.
Finally, among `1<=q<ell`, the largest value in (1.2) is at `q=1`; (1.3) is
smaller when `ell>=2`.  This proves (1.4).  QED.

This is sharper by a factor `m` than the earlier slot-count estimate
`O(D/m)`.

### Lemma 2 (parameter multiplicity)

For `ell>=2`, every underlying unordered block occurs with parameter
multiplicity exactly `4ell`.

#### Proof

The Johnson adjacencies induced by the `2ell` block states form exactly the
cycle `C_(2ell)`: consecutive states exchange one active pair, while any
nonconsecutive states differ on at least two active pairs.  Hence the
unordered vertex set recovers its cyclic order up to a starting point and a
direction.  There are `2ell` starting points and two directions.  Conversely
each such directed start gives one valid choice of the base state and the two
ordered active tuples.  QED.

Consequently one may discard parameter multiplicity and work with a simple
hypergraph of degree

\[
 D_{\rm simp}=\frac{(m)_\ell^2}{2}.                    \tag{1.5}
\]

All codegrees are divided by the same factor `4ell`, so (1.2)--(1.4) and all
relative estimates below are unchanged.  This verifies that the useful
degree is not being manufactured by arbitrary parallel repetition.

## 2. The full block has antipodal twins

For `ell=m`, every coordinate is active and

\[
 X_{t+m}=X_t^c.
\]

Thus every block containing `A` also contains `A^c`, and

\[
 \operatorname{codeg}(A,A^c)=D.                       \tag{2.1}
\]

So the unquotiented full-block hypergraph does **not** have small maximum
pair codegree.  This is a deterministic obstruction, not a weakness of the
count.

There is an exact repair.  Quotient the middle layer by the antipodal pairs
`[A]={A,A^c}`.  Every full block becomes an `m`-edge on these quotient
vertices.  If two distinct quotient vertices have quotient Johnson distance
`q=min(|A\B|,m-|A\B|)`, then (1.2) gives

\[
 \frac{\operatorname{codeg}([A],[B])}{D}
 =\frac{2}{\binom mq^2}\leq\frac2{m^2}.              \tag{2.2}
\]

In particular the quotient has uniformity `m` and

\[
 m\Delta_2/D=O(1/m),\qquad m^2\Delta_2/D=O(1).        \tag{2.3}
\]

For the growing-band program it is cleaner to use partial blocks with

\[
 h\ll\ell\ll m.                                      \tag{2.4}
\]

There are then no antipodal twins, and, with `r=2ell`,

\[
 r\Delta_2/D=O(\ell/m^2)=o(1),\qquad
 r^2\Delta_2/D=O(\ell^2/m^2)=o(1).                  \tag{2.5}
\]

For example, `h=Theta(sqrt(m log m))` and `ell=m^(3/4)` satisfy (2.4).

The full-block nonwrapping inequality from `RANK_BALANCED_BLOCKS.md` should
not be reused verbatim after this replacement.  For `R=2ell<<2m`, one can
have `R rho_q>R-q`.  Instead linearize each selected cycle by copying its
first `h` states.  Over `W/R+o(W/R)` blocks this costs

\[
 O\!\left(\frac hR W\right)=o(W)                   \tag{2.6}
\]

precisely because `h<<ell`.  Thus partial blocks trade the exact cut-capacity
lemma for an asymptotically negligible and completely explicit prefix cost.

## 3. The full codegree sequence is also spread

Pair codegrees alone are not the most faithful parameter.  A `j`-set of
distinct vertices lying in one block occupies `j` distinct positions of the
cycle `C_(2ell)`.  Two of those positions have cyclic distance at least
`ceil((j-1)/2)`.  If `ell=o(m)`, binomial coefficients are increasing through
all relevant distances, so Theorem 1 gives the useful bound

\[
 \frac{\Delta_j(H_{m,\ell})}{D}
 \leq
 \frac{2\binom j2}
      {\binom{m}{\lceil(j-1)/2\rceil}^{\,2}}
 \quad(2\leq j\leq2\ell).                             \tag{3.1}
\]

A ball of cyclic radius `d` has at most `2d+1` positions, so every placement
of the `j` prescribed vertices supplies a pair at cyclic distance at least
`ceil((j-1)/2)`.  The identity of that pair may depend on the containing
block.  Partition the containing blocks according to one such pair and use a
union bound over the at most `binom(j,2)` pairs; Theorem 1 then proves (3.1).

It follows, with an absolute constant `c>0`, that the full-codegree parameter

\[
 B(H):=\min\left\{
  \sqrt{D/\Delta_2},
  \min_{4\leq j\leq2\ell}(D/\Delta_j)^{1/(j-1)}
 \right\}                                             \tag{3.2}
\]

satisfies

\[
 \boxed{B(H_{m,\ell})\geq c\,m/\ell}.                \tag{3.3}
\]

For odd `j-1=2s`, for example, (3.1) gives, up to the harmless factor
`(2 binom(j,2))^(-1/(j-1))`, the root
`binom(m,s)^(1/s)>=m/s`; the even case is no smaller up to an absolute
constant.  Thus (2.4) gives `B(H)->infinity`.

This is the numerical signature that distinguishes these blocks from the
standard bad growing-rank examples.  Merely recording (1.4) throws away most
of the available information.

## 4. Audit of existing black boxes

### 4.1 Pippenger--Frankl--Rodl and Pippenger--Spencer

The classical almost-perfect matching and asymptotic edge-colouring theorems
quantify in the order

\[
 \text{fix }r,\varepsilon;\quad
 \text{then choose }\delta(r,\varepsilon);\quad
 \text{then let }D\to\infty.
\]

They do not give a statement uniform for `r=2ell->infinity`.  Thus (2.5)
cannot simply be substituted into them.  A primary modern statement with
this quantifier order is Theorem 1.1 of
[Ehard--Glock--Joos](https://arxiv.org/abs/1907.09946).

### 4.2 Quantitative pseudorandom and conflict-free matchings

The Ehard--Glock--Joos pseudorandom theorem assumes fixed `r` and a fixed
power saving

\[
 \Delta_2\leq D^{1-\delta}.
\]

Here

\[
 \frac{\log(D/\Delta_2)}{\log D}
 =\Theta\!\left(\frac{\log m}{\ell\log m}\right)
 =\Theta(1/\ell),                                    \tag{4.1}
\]

so there is no fixed `delta>0`.  The conflict-free theorems of
[Glock--Joos--Kim--Kuehn--Lichev](https://arxiv.org/abs/2205.05564) and
[Delcourt--Postle](https://arxiv.org/abs/2204.08981) likewise fix the base
uniformity (and their conflict uniformities) before the asymptotics.  Their
power-codegree hypotheses are not consequences of (1.4).

### 4.3 The genuinely growing-uniformity theorem of Alon--Bollobas--Kim--Vu

The paper
[Economical covers with geometric applications](https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf)
does explicitly allow the uniformity to grow.  Its near-matching corollary is
quantitative, but its useful regime requires, in particular,

\[
 e^{2r}\Delta_2=o(D/\log D),                          \tag{4.2}
\]

and gives an error containing

\[
 r\left(\frac{\Delta_2\log(1+\Delta_2)}D\right)^{1/(r-1)}.
                                                               \tag{4.3}
\]

For `r=2ell` and `Delta_2/D=2/m^2`, the left-to-right ratio in (4.2) is

\[
 \Theta(e^{4\ell}\log D/m^2),
\]

which diverges in the required range `ell>>sqrt(m log m)`.  Moreover
`log Delta_2=(1+o(1))log D=Theta(ell log m)`, so the expression in (4.3)
does not tend to zero.  This is the closest located theorem which genuinely
tracks growing uniformity, and it does not apply.

### 4.4 Grable, Vu, Kang--Kuehn--Methuku--Osthus

The exact estimate (1.4) does make the old condition

\[
 \Delta_2=o(D/\log W)
\]

true, since `log W=Theta(m)`.  However, Grable's uncovered-fraction exponent
is of order `1/r`; a formal substitution gives roughly

\[
 (1/m)^{1/O(\ell)}=1-o(1)
\]

in the required range.  The theorem is not uniform in growing `r` anyway.

Vu's higher-codegree theorem and the 2023 theorem of
[Kang--Kuehn--Methuku--Osthus](https://arxiv.org/abs/2010.04183) also fix the
uniformity.  The latter additionally asks for a fixed power gap
`Delta_2<=D^(1-gamma)`, contradicted by (4.1).

### 4.5 Gould--Kelly's full-codegree nibble

The 2025 preprint
[Gould--Kelly, *Advancing the Rodl Nibble*](https://arxiv.org/abs/2511.11375)
is structurally the best match: its controlling quantity is essentially
`B(H)` from (3.2), and (3.3) says that `B(H)->infinity`.  But its theorem has
the hierarchy

\[
 1/D\ll1/A\ll\gamma\ll1/r,
\]

so `r` is fixed.  Its conclusion contains the error
`B^{-1+gamma} log^A D`; no dependence of `A` on growing `r` is supplied.
Consequently the formal observation `B(H)=Omega(m/ell)` is promising but is
not an application of the theorem.

### 4.6 Absorption and design theorems

The standard iterative-absorption and design results fix the local template
size before the ambient order tends to infinity.  They also require an
explicit absorber/transformer and divisibility conditions for the relevant
design complex.  No located theorem turns (1.1), (1.4), and (3.1) into a
near-factor when the block itself has `2ell->infinity` vertices.

## 5. Why a pair-codegree-only lemma is the wrong target

It is tempting to conjecture the following black box:

> an `r`-uniform regular hypergraph with
> `r^2 Delta_2/D=o(1)` has an almost-perfect matching.

That assertion is not supported by the literature and should not be used.
The growing-rank examples in Section 2 of *Economical covers* show that very
small pair codegrees do not by themselves control growing-rank packings.  In
particular, random regular simple hypergraphs can have effective branching
degree too small relative to `r`.  Repeating every edge also shows why a
multihypergraph theorem cannot depend only on `r`, `D`, and `Delta_2/D`:
parallel repetition makes `D` arbitrarily large without changing the
matching number or the relative codegree.

The Stage-A hypergraph has two pieces of extra information absent from those
examples:

* parameter-edge multiplicity is only the symmetry multiplicity of a single
  cycle, not arbitrary parallel repetition; and
* the entire codegree sequence has the spread (3.1), giving
  `B(H)=Omega(m/ell)->infinity`.

Any valid new lemma should use at least one of these facts.

## 6. The weakest sufficient new statement

The logically weakest useful assertion is object-specific.

### Partial pair-flip near-factor lemma

Let

\[
 \sqrt{m\log m}\ll\ell\ll m.
\]

Then `H_(m,ell)` has a matching of

\[
 \frac{W}{2\ell}-o(W/\ell)
\]

parameter blocks, equivalently covering `W-o(W)` middle sets.

This lemma alone proves Stage A.  It avoids claiming a false general theorem.

A useful, slightly stronger black box would be the following uniform form of
the full-codegree nibble.

### Growing full-codegree nibble target

For a sequence of `r`-uniform, nearly `D`-regular hypergraphs, define

\[
 B=\min\left\{\sqrt{D/\Delta_2},
       \min_{4\leq j\leq r}(D/\Delta_j)^{1/(j-1)}\right\}.
\]

Under a bounded-multiplicity hypothesis and the explicit link-spread bounds
of (3.1), prove that `B->infinity` implies a matching covering `1-o(1)` of the
vertices, uniformly for `r=2ell` in (2.4).

The adjective "explicit" is essential: an unrestricted theorem with only
`B->infinity` has not been verified.  For the present blocks, (3.3) supplies
`B=Omega(m/ell)`.

## 7. A specialized proof program

The most economical proof would analyze a nibble directly on
`H_(m,ell)` rather than first prove a universal theorem.

1. **Use small bites.**  In one round select each remaining block with
   probability `theta/(rD_t)`, for a fixed small `theta`, and keep isolated
   selected blocks.  A round covers `Theta(1/r)` of the surviving vertices
   and reduces the typical degree by a constant factor.

2. **Track every link scale.**  For a `j`-set `S`, track its surviving link
   degree.  Bound every derivative in the concentration calculation using
   (3.1), not merely `Delta_2`.

3. **Stop early.**  It is unnecessary to drive the leftover to the natural
   random-greedy barrier.  Stop when the vertex survival probability is
   `p=(ell/m)^c` for any fixed `0<c<1`.  This is already `o(1)`, while
   `D p^(r-1)` remains exponentially large for a suitable fixed `c`, leaving
   ample concentration.

4. **Exploit symmetry instead of a union bound over parameter edges.**  The
   only state variables needed are vertex and link degrees.  Their number is
   at most `sum_(j<=r) binom(W,j)`, but bad-event dependencies are governed by
   the active support and (3.1); a direct local-lemma or exceptional-outcome
   argument should use this geometry rather than a global union bound.

5. **Prove bounded multiplicity separately.**  Quotient parameterizations
   which give the same unordered cycle before running the process.  The
   dihedral/base-point ambiguity is polynomial in `ell`; arbitrary parallel
   repetition must not enter the theorem.

The quantitative heart is one lemma: after a bite, simultaneously for every
surviving `j`-link needed in the next round,

\[
 d_{t+1}(S)=(1\pm o(1))d_t(S)p_t^{\,r-j}
\]

until the global surviving fraction reaches `(ell/m)^c`.  Establishing this
with errors summable over `O(r log(m/ell))` rounds proves the partial
pair-flip near-factor lemma.

## 8. Effect on the one-stage decorated hypergraph

The sharper Stage-A estimate does **not** automatically validate the
one-stage all-rank decorated hypergraph.

First, independent Bernoulli decoration produces nonuniform edge sizes; a
matching theorem would require fixed per-rank counts (or a carefully cloned
mixture).  Second, the full blocks have complementary shadow pairs:

\[
 (L_t^q)^c=U_{t+m}^q.
\]

They should be retained in complementary pairs and quotiented if full blocks
are used.

More seriously, cross-rank codegrees are larger.  For a middle set `A` and a
fixed `(m-1)`-set `S subset A`, a random incident pair-flip block exposes `S`
as one of the two adjacent intersections with probability `2/m` (up to the
chosen rank-slot retention).  Hence a balanced decorated hypergraph has

\[
 \Delta_2/D=\Theta(1/m)                              \tag{8.1}
\]

across these two classes.  Its balanced edge size is
`Theta(ell sqrt(m))`; in the required range `ell>>sqrt(m log m)`, even
`r Delta_2/D` does not tend to zero.  Thus the two-stage formulation is not
just expository: Stage A has much better pseudorandomness than the one-stage
decorated object, while Stage B is an ordinary capacitated bipartite matching
problem.

## 9. Verdict

No audited theorem currently proves Stage A or the one-stage decorated
packing at the required growing uniformity.

The corrected partial-block geometry is nevertheless a real improvement:

\[
 D=2\ell(m)_\ell^2,\qquad
 \Delta_2/D=2/m^2,\qquad
 B(H)=\Omega(m/\ell)\to\infty.
\]

It removes the projective-plane-scale pair-codegree warning from Stage A and
pinpoints the missing theorem much more sharply.  The next proof should be a
uniform full-codegree nibble specialized to the pair-flip links, not another
application of a fixed-uniformity black box and not a one-stage decorated
nibble.
