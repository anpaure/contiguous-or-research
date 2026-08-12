# The two MSW outer families at depth one: exact maps and a fixed-coordinate no-go

## 1. Outcome

There are two natural Catalan-sized root families in `D_(m+1)`:

\[
                         \mathcal R=\{w10:w\in D_m\},
 \qquad
                         \mathcal L=\{1w0:w\in D_m\}.              \tag{1.1}
\]

They are disjoint for `m>=1`; the remaining root count is

\[
                         C_{m+1}-2C_m=D_m.                         \tag{1.2}
\]

Both families have exact recursive path descriptions.  But they are clean
with respect to **different** old-coordinate embeddings.  Under one fixed
global split, the terminal family remains a two-flip extension while the
primitive family becomes a path-dependent cut.  Therefore the literal MSW
recursion does not yield two fixed descendants of an old shadow defect.

If instead one forces both outer families into one fixed punctured-prism
split, the unchanged MSW outer scaffold fails already at depth one: the
uniform target `T_m` of `MSW_SECOND_UPPER_OBSTRUCTION.md` is missing in the
zero-tag sector, and no residual one-tag path can create a zero-tag upper
colour.  This is an all-dimensional no-go, not a finite audit.

The correct positive replacement is the Mütze--Weber upper-layer recursion,
whose dangling paths cover the missing zero-tag layer before the mixed
families are joined.  The remaining open theorem is its equitable antipodal
refinement, not a further audit of the unchanged MSW outer factor.

## 2. Root decomposition

Let `N=2m`.  Every word `w10` has a proper return before its final peak, so
it is not primitive.  Every word `1w0` is primitive.  Hence the two families
in (1.1) are disjoint, and both have size `C_m`; (1.2) follows.

Equivalently, the residual roots are exactly

\[
 \mathcal X_{m+1}
 =\{1u0v:\ v\ne\epsilon,\ \ell(v)\ge2\},              \tag{2.1}
\]

where `ell(v)` is the final-descent length.  Indeed, `v=epsilon` is the
primitive family, while `ell(v)=1` means that the entire word ends in the
terminal peak `10`.  If the first primitive has semilength `a`, then

\[
 |\mathcal X_{m+1}|
 =\sum_{a=1}^{m}C_{a-1}
      \bigl(C_{m+1-a}-C_{m-a}\bigr)
 =C_{m+1}-2C_m.                                      \tag{2.2}
\]

The first equality is an exact first-return classification; the second is
the Catalan convolution.

## 3. Exact flip orders and the two old embeddings

Write `rho(w)=(r_1,...,r_N)`.  Concatenation locality and path reversal give

\[
 \rho(w10)=(r_1,\ldots,r_N,N+2,N+1),                 \tag{3.1}
\]

and

\[
 \rho(1w0)=(N+2,1+r_N,1+r_{N-1},\ldots,1+r_1,1).     \tag{3.2}
\]

Thus (3.1) embeds the old coordinates as `1,...,N` and uses the final two
coordinates as its outer pair.  Formula (3.2) embeds the old coordinates as
`2,...,N+1` and uses the first and final coordinates as its outer pair.
The two injections are fixed,

\[
 \alpha(i)=i,\qquad\beta(i)=i+1,                     \tag{3.3}
\]

but their omitted coordinate pairs are different.  There is no single
decomposition `[N+2]=X dotcup {p,q}` for which both (3.1) and (3.2) delete
the same `p,q`.

This distinction remains visible in the ordinary wreath order.  If `z` is
the closing coordinate, the old ordinary order is

\[
 C(w)=(z,r_2,r_4,\ldots,r_N,r_1,r_3,\ldots,r_{N-1}). \tag{3.4}
\]

For `p=N+1,q=N+2`, (3.1) gives

\[
 C(w10)=(z,r_2,\ldots,r_N,p,r_1,r_3,\ldots,r_{N-1},q).             \tag{3.5}
\]

This is the antipodal gap extension of `C(w)` with insertions after gaps
`m` and `2m`.  In contrast, with the natural primitive-family old injection
`beta`, (3.2) gives

\[
 C(1w0)=
 (z,\beta(r_N),\beta(r_{N-2}),\ldots,\beta(r_2),1,q,
       \beta(r_{N-1}),\ldots,\beta(r_1)).             \tag{3.6}
\]

After deleting `1,q`, (3.6) is not generally a rotation or reversal of
`beta(C(w))`.  Adjacency in the omitted-label flip word therefore must not
be mistaken for standard-order interval transport.

## 4. Exact first-shadow flag tables

Let an old complementary path be

\[
 P=(x_0,y_0,x_1,\ldots,y_{m-1},x_m),                 \tag{4.1}
\]

and use its positional flags

\[
 L_i=x_i\cap x_{i+1},\quad
 U_i=X\setminus(y_{i-1}\cup y_i),\quad
 E_0=X\setminus y_0,\quad E_1=X\setminus y_{m-1}.  \tag{4.2}
\]

For the terminal extension (3.1), on its natural abstract old copy the new
lower and upper states are

\[
 X_i=x_ip\ (0\le i\le m),\quad X_{m+1}=x_mq,
 \qquad
 Y_i=y_ip\ (i<m),\quad Y_m=x_mpq.                   \tag{4.3}
\]

Direct substitution into the definitions gives

\[
\begin{aligned}
 L(\mathcal R)&=\{pL_i:0\le i<m\}\ \dot\cup\ \{x_m\},\\
 U(\mathcal R)&=\{qU_i:1\le i<m\}\ \dot\cup\ \{E_1\},\\
 E_0(\mathcal R)&=qE_0,\\
 E_1(\mathcal R)&=x_0.                               \tag{4.4}
\end{aligned}
\]

For the primitive extension (3.2), on its natural shifted old copy the
contracted lower path is

\[
 x_0p,\ \bar y_{m-1}pq,\ldots,\bar y_0pq,\ x_mq.    \tag{4.5}
\]

Its exact flag table is

\[
\begin{aligned}
 L(\mathcal L)&=\{pE_1\}\ \dot\cup\
                \{pqU_i:1\le i<m\}\ \dot\cup\ \{qE_0\},\\
 U(\mathcal L)&=\{L_i:0\le i<m\},\\
 E_0(\mathcal L)&=x_m,\\
 E_1(\mathcal L)&=x_0.                               \tag{4.6}
\end{aligned}
\]

The actual wreath first shadow is

\[
       L\ \dot\cup\ \{E_0,E_1\}\ \dot\cup\
       \{z\cup U:U\in U(P)\}.                       \tag{4.7}
\]

Consequently every old **positional flag occurrence** has two outer
descendants, one under `alpha` and one under `beta`:

\[
\begin{array}{c|cc}
\text{old flag}&\mathcal R&\mathcal L\\ \hline
L&\alpha(L)\cup\{p_R\}&\beta(L)\cup\{z\}\\
U&\alpha(U)\cup\{z,q\}&\beta(U)\cup\{p_L,q\}\\
E_0&\alpha(E_0)\cup\{q\}&\beta(E_0)\cup\{q\}\\
E_1&\alpha(E_1)\cup\{z\}&\beta(E_1)\cup\{p_L\}.
\end{array}                                           \tag{4.8}
\]

Here `p_R=N+1`, `p_L=1`, and the two families share `q=N+2`.
Table (4.8) has branching two only in a **flagged** norm.  The ordinary old
shadow sees the aggregate `L+E_0+E_1`, so one missing target can be missing
from three positional classes simultaneously.  No coefficient-two theorem
for the unflagged defect follows from (4.8).

## 5. Why the residual family is not an additive halo

The residual family has `D_m=Theta(C_m)` paths, but every path has
`Theta(m)` middle vertices.  Its total middle mass is

\[
                         (2m+3)D_m=\Theta(mC_m),      \tag{5.1}
\]

a positive fraction of the new width.  Constantly many seams per residual
path therefore do not make its **bulk** shadow an `O(HC_m)` exception.
One must prove a targetwise transport theorem for that bulk.

There is also a sharp obstruction to doing so with the unchanged fixed MSW
outer scaffold.  In the fixed split `X dotcup {p,q}`, every residual lower
vertex of the punctured prism has exactly one new tag.  An edge between two
such vertices has one or two new tags in its upper colour, never zero.
Hence residual paths cannot repair a zero-tag upper-colour hole.

For every `m>=4`, `MSW_SECOND_UPPER_OBSTRUCTION.md` gives the explicit
zero-tag target

\[
 T_m=\{1,2,3,5,6\}\cup\{8,9,\ldots,m+4\}            \tag{5.2}
\]

which is absent from every unchanged MSW outer colour
`y_(i-1) union y_i`.  Since the residual prism has no zero-tag edge, (5.2)
remains absent after any completion confined to residual vertices.

Thus the fixed-coordinate statement

\[
 \text{outer MSW copies}+\text{residual completion}
 \Longrightarrow\text{complete depth-one shadow}      \tag{5.3}
\]

is false in every dimension `m>=4`.

## 6. Endpoint invariant and the surviving route

Cutting one edge in each of `k` complementary paths and reconnecting their
tails induces a permutation `pi` of the terminal endpoints.  With distinct
antipodal endpoint pairs, every resulting path is complementary only if

\[
                                  \pi=\mathrm{id}.      \tag{6.1}
\]

An MNW alpha switch induces a nontrivial three-cycle of tails.  It therefore
cannot be an endpoint-safe absorber by itself, even though it preserves the
middle-level vertices used by its alternating cycle.

The abstract endpoint-safe replacement is a double switch.  Cut the same
three paths at two ordered boundary triples, apply a permutation `pi` at
the first triple and `pi^(-1)` at the second, and permute the intervening
segments.  Every original endpoint pair is then retained.  For an alpha
move, `pi=(123)` and the second boundary must realize `(132)`.  What remains
unproved is an all-dimensional MSW/Mütze--Weber context supplying both
boundary cycles with the required individual upper colours.

The published Mütze--Weber upper-layer path system avoids the zero-tag
obstruction: it covers every upper target first and leaves only explicit
ports, which are consumed by its mixed family.  The exact remaining theorem
is therefore the equitable antipodal, `O(C_m)`-switch refinement stated in
`MUTZE_WEBER_PRISM_TRANSLATION.md`.
