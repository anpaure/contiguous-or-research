# Balanced coordinate vortices for the two-hole packet family

## Status

This note gives an exact locality theorem for the `D+2` upper-rich packet
family and an exact fractional cover-down for the one-coordinate vortex.
It also records a sharp obstruction: a cover of *all* resources outside a
prescribed slice by fixed-size packets is often arithmetically impossible.

For a vortex fixing `a` present and `a` absent coordinates, deleting every
packet which meets the core slice changes packet degrees only in an explicit
constant-defect halo.  At

\[
                         a={1\over4}\log _2 r+O(1)
\]

that halo has size `O(W polylog(r)/sqrt(r))`.  The symmetric halo is the two
central ranks of a product poset and has an exact owner/root incidence
matching.  What is not proved here is a packet decomposition of that product
matching, nor an integral upper-decorated nibble in the bulk.

## 1. Packet and coordinate slice

Put

\[
 n=2r-1,\qquad D=d+1,\qquad L=D+2,\qquad c=r-D.            \tag{1.1}
\]

An all-high two-hole packet consists of

\[
 K\subset H\subset[n],\qquad |K|=c,\quad |H|=r+2,
\]

and a cyclic order of `F=H-K`, where `|F|=L`.  If `e_t` is the
cyclic edge at phase `t` and `T_t` the corresponding cyclic triple, then
its resources are

\[
 O_t=H-e_t,\qquad Q_t=H-T_t,\qquad U_t=H-\{f_t\}.          \tag{1.2}
\]

Thus the owners, immediate-lower roots, and immediate-upper colours have
ranks `r,r-1,r+1` respectively.

Fix disjoint coordinate banks `A,B`, with

\[
                           |A|=|B|=a.                      \tag{1.3}
\]

At rank `s` define the directed coordinate slice

\[
 \mathcal S_s(A,B)=
 \{X\in\tbinom{[n]}s:A\subseteq X,\ X\cap B=\varnothing\}. \tag{1.4}
\]

For an arbitrary set `X`, write

\[
 \alpha(X)=|A-X|,\qquad \beta(X)=|B\cap X|.               \tag{1.5}
\]

### Lemma 1.1 (exact slice-hitting criterion)

A packet contains an owner in `mathcal S_r(A,B)` if and only if

1. `A subset H`; and
2. some cyclic edge `e` of `F` satisfies

\[
                        H\cap B\subseteq e,
                 \qquad e\cap A=\varnothing.              \tag{1.6}
\]

#### Proof

The owner belonging to `e` is `H-e`.  It contains `A` exactly when
`A subset H` and `e cap A` is empty; it avoids `B` exactly when
`H cap B subset e`.  \(\square\)

For singleton banks, say `A={x},B={y}`, and `L>=4`, (1.6) collapses to

\[
 \boxed{\text{the packet avoids the slice}
        \iff x\notin H\ \text{or}\ y\in K.}               \tag{1.7}
\]

Indeed, if `x in H` and `y notin K`, then either `y notin H`, in which
case an edge avoiding `x` works, or `y in F`, in which case one of the two
cyclic edges through `y` avoids `x`.

## 2. Exact constant-radius halo

### Theorem 2.1 (packet exposure is confined to a rectangular halo)

Suppose a packet contains an owner `O_* in mathcal S_r(A,B)`.  Then every
resource of that packet satisfies

\[
\begin{array}{c|c|c}
\text{resource}&\alpha&\beta\\ \hline
\text{owner }O&\alpha(O)\le2&\beta(O)\le2\\
\text{root }Q&\alpha(Q)\le3&\beta(Q)\le2\\
\text{upper }U&\alpha(U)\le1&\beta(U)\le2.
\end{array}                                                \tag{2.1}
\]

Consequently, after deleting every packet which meets the owner slice,
the degree of every owner with `alpha>2` or `beta>2`, every root with
`alpha>3` or `beta>2`, and every upper target with `alpha>1` or `beta>2`
is **literally unchanged**.

#### Proof

Write `O_*=H-e_*`.  Since `O_*` is in the slice,

\[
                      A\cap e_*=\varnothing,
                 \qquad H\cap B\subseteq e_*.             \tag{2.2}
\]

For another owner `H-e`, at most the two elements of `e` can be missing
from `A`, and every surviving `B`-coordinate lies in the two-set `e_*`.
For a root `H-T`, where `|T|=3`, at most three `A`-coordinates are missing,
and again every surviving `B`-coordinate lies in `e_*`.  For an upper
target `H-{z}`, at most one `A`-coordinate is missing and at most the two
coordinates of `e_*` from `B` survive.  This proves (2.1).  The degree
claim is its contrapositive. \(\square\)

For fixed nonnegative `p,q`, define the rank-`s` rectangular halo

\[
 \mathcal H_s^{p,q}(A,B)=
 \{X\in\tbinom{[n]}s:\alpha(X)\le p,\ \beta(X)\le q\}.     \tag{2.3}
\]

### Proposition 2.2 (exact halo size)

\[
 \boxed{
 |\mathcal H_s^{p,q}(A,B)|=
 \sum_{i=0}^p\sum_{j=0}^q
   \binom ai\binom aj
   \binom{n-2a}{s-a+i-j}.}                                \tag{2.4}
\]

For fixed `p,q`, `a=o(sqrt(r))`, and `s in {r-1,r,r+1}`,

\[
 |\mathcal H_s^{p,q}(A,B)|
   =O_{p,q}\!\left(\binom ns,4^{-a}(1+a)^{p+q}\right).   \tag{2.5}
\]

In particular, for `a=floor((log_2 r)/4)`, the affected owner, root, and
upper banks have respective sizes

\[
 O\!\left({W(\log r)^4\over\sqrt r}\right),\qquad
 O\!\left({W(\log r)^5\over\sqrt r}\right),\qquad
 O\!\left({W(\log r)^3\over\sqrt r}\right).              \tag{2.6}
\]

#### Proof

Choose the `i` missing members of `A`, the `j` present members of `B`, and
then the remaining `s-a+i-j` coordinates from the neutral ground set.
This gives (2.4).  For bounded `i,j`, adjacent central binomial
coefficients in the last factor differ by only a bounded ratio.  Also

\[
 {\binom{n-2a}{s-a}\over\binom ns}
 ={(s)_a(n-s)_a\over(n)_{2a}}
 =4^{-a}\exp(O(a^2/r)).                                   \tag{2.7}
\]

Now sum the bounded initial binomial tails in (2.4).  Equation (2.6)
follows from `4^{-a}=Theta(r^{-1/2})`. \(\square\)

## 3. The reserve is an exact product middle layer

The halo is not an arbitrary exceptional set.  Fix `0<=p<=a` and put
`C=[n]-(A union B)`
and, for `X` in the symmetric halo `mathcal H^{p,p}`, encode

\[
                I=A-X,\qquad J=B\cap X,\qquad Y=X\cap C.  \tag{3.1}
\]

Then the induced inclusion poset on all ranks of the halo is

\[
 \boxed{
 \left(\mathcal B_a^{\le p}\right)^{\rm op}
 \times \mathcal B_a^{\le p}
 \times \mathcal B_{,2r-1-2a}.}                         \tag{3.2}
\]

Its product rank is

\[
                   \rho(X)=p-|I|+|J|+|Y|=p-a+|X|.         \tag{3.3}
\]

The total product rank is `2p+2r-1-2a`, an odd number, so set-ranks
`r-1` and `r` are exactly the two central product ranks.

### Theorem 3.1 (exact owner/root matching in the symmetric reserve)

For every `p`, the incidence graph between

\[
        \mathcal H_{r-1}^{p,p}(A,B)
       \quad\text{and}\quad
        \mathcal H_r^{p,p}(A,B)                            \tag{3.4}
\]

has a perfect matching.

#### Proof

The truncated Boolean poset `mathcal B_a^{<=p}` has the normalized
matching property and a log-concave rank sequence.  The same is true of
its dual and of a Boolean lattice.  The standard product theorem for
normal posets with log-concave Whitney numbers therefore says that (3.2)
is normal.  It is rank-symmetric under interchanging the first two factors
and complementing the neutral factor.  Hence its two central ranks have
equal size, and the normalized matching property supplies a matching
saturating either one. \(\square\)

For `p=0`, (3.2) is just `mathcal B_(2(r-a)-1)`, and (3.4) is the ordinary
middle-levels graph.  Thus the core slice itself has a Hamilton cycle, not
merely a perfect matching.  For `p=3`, Theorem 3.1 gives an exact incidence
factor on a symmetric reserve containing every owner and root whose degree
can change in Theorem 2.1.  Lifting that matching to upper-decorated
`D+2` packets remains a separate problem.

## 4. Exact one-coordinate conditional degrees

We now take `A={x},B={y}`.  Write a resource type as `ij`, where `i`
records membership of `x` and `j` membership of `y`.  The forbidden type
is `10`.  Let `D_0` and `D_U` be the unrestricted owner/root and upper
packet degrees from the two-hole packet theorem.

### Theorem 4.1 (conditional packet degrees)

For owners outside the slice,

\[
\begin{array}{c|c}
00&D_0\,{r-3\over r-1}\\
01&D_0\!\left(1-{2D\over r(r-1)}\right)\\
11&D_0\,{r-D\over r}.
\end{array}                                                \tag{4.1}
\]

For roots outside the slice,

\[
\begin{array}{c|c}
00&D_0\,{r-3\over r}\\
01&D_0\!\left(1-{3(D-1)\over r(r-1)}\right)\\
11&D_0\,{r-D\over r-1}.
\end{array}                                                \tag{4.2}
\]

For upper targets outside the slice,

\[
\begin{array}{c|c}
00&D_U\,{r-3\over r-2}\\
01&D_U\!\left(1-{D+1\over(r-2)(r+1)}\right)\\
11&D_U\,{r-D\over r+1}.
\end{array}                                                \tag{4.3}
\]

#### Proof

Through a fixed owner choose `H-O`, a two-set in an `(r-1)`-set, and
choose `K subset O`, `|K|=c`.  Use (1.7).  For type `00`, avoidance says
that `x` is not one of the two new labels.  For type `01`, failure requires
both `x in H-O` and `y notin K`, whose relative frequencies are
`2/(r-1)` and `D/r`.  For type `11`, avoidance requires `y in K`, of
relative frequency `c/r`.  This gives (4.1).

For a root, `H-Q` is a three-set in an `r`-set and `K` is a `c`-subset of
an `(r-1)`-set.  The corresponding frequencies are

\[
 {\binom{r-1}3\over\binom r3}={r-3\over r},\qquad
 {3\over r}{D-1\over r-1},\qquad {c\over r-1},
\]

which gives (4.2).  For an upper target, `H-U` is one label in an
`(r-2)`-set and `K` is a `c`-subset of an `(r+1)`-set.  This gives (4.3).
\(\square\)

## 5. Exact fractional vortex factor and all central chain tickets

There are five stabilizer-orbits of slice-avoiding packets:

\[
\begin{array}{c|c}
\mathcal P_{00}&x,y\notin H\\
\mathcal P_{0K}&x\notin H,\ y\in K\\
\mathcal P_{0F}&x\notin H,\ y\in F\\
\mathcal P_{KK}&x,y\in K\\
\mathcal P_{FK}&x\in F,\ y\in K.
\end{array}                                                \tag{5.1}
\]

Put

\[
 N=\binom{2r-3}{r},\qquad
 S=\binom{2r-3}{r-1},\qquad
 \Delta=S-N={2N\over r-2}.                               \tag{5.2}
\]

The outside owner type counts are `(N,S,S)`, while the outside root type
counts are `(S,S,N)`.

### Theorem 5.1 (five-orbit fractional cover-down)

Assume `r>=2L`.  Distribute the following total packet masses uniformly
inside the five orbits in (5.1):

\[
\begin{aligned}
 m_{0F}=m_{FK}&=\Delta,\\
 m_{00}&={N-2\Delta\over L},\\
 m_{0K}&={S\over L}-\Delta,\\
 m_{KK}&={S-D\Delta\over L}.                              \tag{5.3}
\end{aligned}
\]

Every owner and every root outside the slice then has load exactly one,
and no selected packet meets the slice.

Moreover, at source width `q`, `1<=q<=D+1`, put `h=D-q`.  The total raw
ticket incidences of types `00,01,11` are

\[
 \boxed{
 I_{00}(q)=N+h\Delta,\qquad
 I_{01}(q)=S,\qquad
 I_{11}(q)=S-h\Delta.}                                   \tag{5.4}
\]

For `q=D+1`, these are immediate-upper occurrences; for `1<=q<=D-2`,
they are the complete two-ray central lower tickets.  For the actual
triangular depth and all sufficiently large `r`, every rank-`c+q` target
outside the slice can be marked to load exactly one.

#### Proof

At width `q`, the five packet orbits contribute respectively

\[
\begin{array}{c|ccc}
 &00&01&11\\ \hline
\mathcal P_{00}&L&0&0\\
\mathcal P_{0K}&0&L&0\\
\mathcal P_{0F}&L-q&q&0\\
\mathcal P_{KK}&0&0&L\\
\mathcal P_{FK}&0&L-q&q.
\end{array}                                                \tag{5.5}
\]

At `q=D` and `q=D-1`, substitution of (5.3) gives respectively
`(N,S,S)` and `(S,S,N)`, proving the owner/root statement.  The same
substitution at arbitrary `q` gives (5.4).

At `q=D+1`, the upper target counts are

\[
 M=\binom{2r-3}{r+1}=N{r-3\over r+1},\qquad N,\qquad S.
\]

The raw counts are `N-Delta,S,S+Delta`, all at least their target counts.
Thus typewise thinning gives exact upper load.  Explicit thinning factors
are

\[
 {M\over N-\Delta}
 ={(r-3)(r-2)\over(r+1)(r-4)},\qquad
 {N\over S}={r-2\over r},\qquad
 {S\over S+\Delta}={r\over r+2}.                          \tag{5.6}
\]

For `q<=D-2`, let `h=D-q>=2`.  The three target counts are

\[
 \binom{2r-3}{r-h},\qquad
 \binom{2r-3}{r-h-1},\qquad
 \binom{2r-3}{r-h-2}.                                    \tag{5.7}
\]

The first two are at most `S`, hence at most the first two entries of
(5.4).  For the last one, set `t=h-1` and divide by `N`:

\[
 {\binom{2r-3}{r-h-2}\over N}
 =\prod_{j=0}^{t-1}{r-3-j\over r+1+j}
 \le \exp\!\left(-{4t\over r+t}\right).                 \tag{5.8}
\]

The established triangular bound `d<=ceil(sqrt(r))` gives `t<=sqrt(r)`.
For `r>=25`, Taylor's inequality and

\[
 2(r-t)(r-2)\ge(r+t)^2                                   \tag{5.9}
\]

give

\[
 \exp\!\left(-{4t\over r+t}\right)
 \le1-{2t\over r-2}.
\]

This is exactly

\[
 \binom{2r-3}{r-h-2}\le N-t\Delta=S-h\Delta.             \tag{5.10}
\]

The stabilizer of `x,y` is transitive on every rank/type class, so constant
typewise thinning marks every target exactly once. \(\square\)

Thus the one-coordinate vortex has no fractional owner, root, upper, or
central-chain separator.  Notice also that every proper interval ticket of
every packet in (5.1) avoids the slice: either `x` is absent from the whole
top `H`, or `y` lies in the common core `K`.

## 6. Weighted codegrees and the integral obstruction

Let `|mathcal P|=WD_0/L` be the unrestricted packet count.  The five orbit
probabilities are

\[
 { (r-3)(r-4),\ (r-3)c,\ (r-3)L,\ c(c-1),\ Lc
   \over (2r-1)(2r-2)}.                                  \tag{6.1}
\]

Consequently the individual packet weights induced by (5.3) are

\[
\begin{array}{c|c}
00&{(r-1)(r-6)\over(r-3)(r-4)D_0}\\
0K&{(r-1)(r-2L)\over(r-3)cD_0}\\
0F&{2(r-1)\over(r-3)D_0}\\
KK&{(r-1)(r-2D)\over c(c-1)D_0}\\
FK&{2(r-1)\over cD_0}.
\end{array}                                                \tag{6.2}
\]

For `r>=4L`, every entry is at most `3/D_0`.  Since the unrestricted
owner/root packet hypergraph has maximum pair codegree `2D_0/r`, the
weighted vortex factor has maximum pair load at most

\[
                              {6\over r}.                  \tag{6.3}
\]

Its aggregate within-packet collision mass is likewise only a constant
multiple of the unrestricted `O(L/r)` mass.  Thus deleting the slice
creates no new local or fractional nibble obstruction.

There is, however, a sharp global obstruction to the literal statement
"cover every outside resource while avoiding the slice".  Every packet
contains exactly `L` owners.  Hence an integral exact cover requires

\[
                         L\mid N+2S.                       \tag{6.4}
\]

This fails already in the two most relevant calibrated cases:

\[
\begin{array}{c|c|c|c}
k&r&D+2&N+2S\\ \hline
15&8&6&4719\equiv3\pmod6,\\
17&9&6&17875\equiv1\pmod6.
\end{array}                                                \tag{6.5}
\]

Therefore no involution or fixed-`L` exact matching theorem can cover all
outside owners at `k=15` or `k=17`.  A correct integral vortex theorem must
do at least one of the following:

1. reserve the whole constant-defect halo and solve it as a product
   middle-level instance;
2. admit a bounded number of packets crossing the core slice;
3. mix packet periods whose gcd pays the congruence; or
4. leave a controlled residue for the terminal absorber.

Theorems 2.1--3.1 justify the first option geometrically.  Theorem 5.1 and
(6.3) show that its bulk has an exact spread fractional factor.  The
remaining balanced-vortex theorem is now precise: round that bulk factor
while protecting `mathcal H^{3,3}`, then lift the exact product matching in
the reserve to upper-decorated packets and reconnect the two parts.
