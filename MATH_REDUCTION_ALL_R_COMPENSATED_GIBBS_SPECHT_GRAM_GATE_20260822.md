# The all-`r` compensated Gibbs problem is a four-versus-one Specht Gram gate

**Date:** 2026-08-22  
**Status:** unconditional representation-theoretic reduction.  It converts
the complete-catalogue compensated shallow-control question into a bounded
Gram/Schur-complement calculation inside each two-row irreducible.  The
required normalized lower bounds and coordinatewise-delocalized right
inverse are not proved here.

## 1. Complete catalogue as a regular representation

Fix `r>=2`, put `b=2r+1`, and let `C_r={E(w):w in S_b}` be the complete directed
punctured catalogue,

\[
 E(w)=\{(M,I_r^w(s)):s\ne0\}
 \mathbin{\dot\cup}
 \{(L,I_{r-1}^w(s)):s\ne0\}.                       \tag{1.1}
\]

The containment-path reconstruction makes `w -> E(w)` injective.  Coordinate
relabeling acts freely and transitively on the columns, so the real column
space is the left regular representation

\[
                              \mathscr R=\mathbb R[S_b].       \tag{1.2}
\]

Explicitly, write `L_s=I_(r-1)^w(s)` and `M_s=I_r^w(s)` for
`1<=s<=2r`.  The tagged containment graph is the intrinsically oriented
path

\[
 L_1-M_1-L_2-M_2-\cdots-L_{2r}-M_{2r}.
\]

The differences `M_s-L_s={w_(s+r-1)}` recover `2r` word positions; the
unique unused label recovers position `r-1`.  This proves injectivity and
also shows that the coordinate action is free.

For a tagged central target `v`, let

\[
 a_v(G)=\mathbf1_{\{v\in G\}}.                     \tag{1.3}
\]

For configurations `F,G`, put

\[
                              D(F,G)=(|F\cap G|-1)_+.          \tag{1.4}
\]

Let `R_D` be the right-kernel operator

\[
                    (fR_D)(G)=\sum_F f(F)D(F,G).              \tag{1.5}
\]

The unnormalised rooted duplicate-exposure row is exactly

\[
                              \widetilde p_v=a_vR_D.           \tag{1.6}
\]

Indeed (1.6) is
`sum_(F ni v)(|F cap G|-1)_+`.  The kernel (1.4) is invariant under
simultaneous coordinate relabeling, so `R_D` commutes with the left regular
action.

To fix orientations, identify `E(g)` with the permutation whose word is
`(g(0),...,g(b-1))`, and put

\[
 (L_hf)(g)=f(h^{-1}g),\qquad
 \kappa(x)=D(E(1),E(x)).                            \tag{1.6a}
\]

Then `D(E(g),E(h))=kappa(g^{-1}h)` and

\[
 (fR_D)(h)=\sum_g f(g)\kappa(g^{-1}h).             \tag{1.6b}
\]

Thus (1.5) is the right-convolution operator commuting with `L_h`; no
left/right convention is implicit below.

For a proper shallow rank `k`, let

\[
 q_T^{(k)}(G)=\mathbf1\{T\text{ is one of the }b
            \text{ full cyclic }k\text{-windows of }G\}.     \tag{1.7}
\]

The complete compensated constraint space and the rank-`k` objective space
are therefore the left submodules

\[
 \mathscr B=\operatorname {span}_{S_b}
   \{a_{M,0},a_{L,0},a_{M,0}R_D,a_{L,0}R_D\},       \tag{1.8}
\]

\[
                    \mathscr Q_k=\operatorname {span}_{S_b}
                                      \{q_{T_0}^{(k)}\}.       \tag{1.9}
\]

Here one fixed target on each indicated shore is enough because the group
is transitive on targets of a given size.  Dividing the exposure rows by
their positive shore degrees does not change (1.8).

## 2. Multiplicity-one source modules

For `0<=s<=b`, the permutation module on `s`-subsets has the multiplicity-
free decomposition

\[
 \mathbb R^{{[b]\choose s}}
 \cong\bigoplus_{j=0}^{\min(s,b-s)}V_{(b-j,j)}.      \tag{2.1}
\]

For self-containment, one can obtain (2.1) from the nested inclusion maps.
Let `U_j` map a `j`-set basis vector to the sum of all `s`-sets containing
it.  The images form a filtration.  The new quotient at step `j` has
dimension

\[
                         {b\choose j}-{b\choose{j-1}},         \tag{2.2}
\]

and is the two-row module `V_(b-j,j)`; the dimensions telescope to
`binom(b,s)`.  The adjacent-transposition action on the polytabloid
differences in this quotient is the standard irreducible two-row action,
so the quotients are pairwise nonisomorphic and irreducible.  This proves
(2.1), including multiplicity one.

Equivalently, for the stabilizer `S_s times S_(b-s)`, the fixed space in
`V_(b-j,j)` is one-dimensional when `j<=min(s,b-s)` and zero otherwise.

The four generators in (1.8) are respectively fixed by the stabilizers of
an `r`-set or an `(r-1)`-set.  Because `R_D` commutes with the group action,
the same is true after applying it.  Consequently, inside the
`lambda=(b-j,j)` isotypic component of the regular representation,

\[
 \mathscr B_\lambda\cong
 V_\lambda\otimes M_{B,\lambda},
 \qquad                         \dim M_{B,\lambda}\le4,       \tag{2.3}
\]

whereas

\[
 \mathscr Q_{k,\lambda}\cong
 V_\lambda\otimes\operatorname {span}\{m_{k,\lambda}\}
                                                               \tag{2.4}
\]

for every `j<=min(k,b-k)` with a nonzero window projection.  The vectors
in (2.3)--(2.4) live in the `dim V_lambda`-dimensional multiplicity space
of the regular representation.  Formula (2.3) is the promised
four-versus-one reduction.

## 3. The five-vector Gram criterion

The multiplicity vectors have a concrete position-side description.  Let
`mathcal X_s` be the `s`-subsets of the position cycle `Z_b`, and put

\[
 u_s^-=\sum_{a\ne0}[\{a,a+1,\ldots,a+s-1\}],
 \qquad
 u_s^\circ=\sum_{a\in\mathbb Z_b}
             [\{a,a+1,\ldots,a+s-1\}].             \tag{3.0a}
\]

For a label `s`-set `T` and a permutation `g`, the corresponding row
function is the matrix coefficient

\[
 \mathbf1\{T\text{ is a retained/full }s\text{-window of }g\}
   =\langle[T],g u_s^\star\rangle,                  \tag{3.0b}
\]

where `star=-` for a retained punctured deck and `star=circle` for a full
deck.  Fix an orthogonal model of `V_lambda`, put
`d_lambda=dim V_lambda`, and use the isometric Peter--Weyl convention

\[
 \Phi_\lambda(v\otimes u)(g)
 =\sqrt{d_\lambda\over b!}\,\langle v,g u\rangle.             \tag{3.0e}
\]

Schur orthogonality makes (3.0e) an isometry onto one matrix-coefficient
copy in the regular representation.  Consequently the actual isometric
multiplicity vector belonging to the unscaled row (3.0b) is
`sqrt(b!/d_lambda)` times the position-side vector.  After an isometric
identification of the common two-row summand `V_lambda` in the different
subset modules, the *directions* of the first, second, and fifth
multiplicity vectors below are therefore the `lambda`-projections of

\[
                              u_r^-,\qquad u_{r-1}^-,
                              \qquad u_k^\circ.       \tag{3.0c}
\]

Right convolution by the duplicate kernel acts on the multiplicity factor
by the Fourier block, in the orientation fixed in (1.6),

\[
 \widehat D(\lambda)=\sum_{x\in S_b}\kappa(x)\rho_\lambda(x^{-1}).
                                                               \tag{3.0f}
\]

Hence the directions of the third and fourth vectors are, up to the
harmless positive shore normalizations,

\[
                    \widehat D(\lambda)u_{r,\lambda}^-,
                    \qquad
                    \widehat D(\lambda)u_{r-1,\lambda}^- .   \tag{3.0d}
\]

Thus the Gram gate can be evaluated from three explicit cyclic-deck
vectors and one Fourier block of the explicit overlap kernel (1.4); no LP
variables remain.

Choose isometric equivariant decompositions of the standard Euclidean
configuration space and each standard Euclidean target space.  Let the
following be the resulting actual, scaled multiplicity vectors (thus
including the factor in (3.0e)) for the four constraint copies and the
shallow incidence operator:

\[
 u_{M,\lambda},\quad u_{L,\lambda},\quad
 u_{M,\lambda}^{D},\quad u_{L,\lambda}^{D},\quad
 m_{k,\lambda}.                                      \tag{3.1}
\]

Zero vectors are allowed when a source module has no `lambda` component.
Let `G_(B,lambda)` be the `4 by 4` Gram matrix of the first four vectors,
and put

\[
 g_{k,\lambda}
 =\bigl(\langle u_{M,\lambda},m_{k,\lambda}\rangle,
          \langle u_{L,\lambda},m_{k,\lambda}\rangle,
          \langle u^D_{M,\lambda},m_{k,\lambda}\rangle,
          \langle u^D_{L,\lambda},m_{k,\lambda}\rangle
   \bigr)^{\mathsf T}.                                \tag{3.2}
\]

Use the Moore--Penrose inverse if the four vectors are dependent and define

\[
 \boxed{
 \eta_{k,\lambda}
 =\|m_{k,\lambda}\|^2
  -g_{k,\lambda}^{\mathsf T}
       G_{B,\lambda}^{\dagger}g_{k,\lambda}.}       \tag{3.3}
\]

### Theorem 3.1 (exact compensated shallow criterion)

For every relevant two-row `lambda`,

\[
 \boxed{
 \eta_{k,\lambda}>0
 \quad\Longleftrightarrow\quad
 \mathscr Q_{k,\lambda}\not\subseteq\mathscr B_\lambda
 \quad\Longleftrightarrow\quad
 \text{some }\delta\in\ker(A,P)
 \text{ has a nonzero rank-}k\ \lambda\text{-current}.}     \tag{3.4}
\]

Moreover, on that component the least Hilbert-space norm of a compensated
preimage of a unit shallow current is

\[
                              \boxed{\eta_{k,\lambda}^{-1/2}} \tag{3.5}
\]

where both norms are standard Euclidean norms and (3.1) uses the isometric
convention (3.0e).

#### Proof

In the regular isotypic decomposition, the orthogonal complement of the
constraint row space is

\[
 V_\lambda\otimes M_{B,\lambda}^{\perp}.            \tag{3.6}
\]

The shallow copy has a component in (3.6) exactly when the orthogonal
projection of `m_(k,lambda)` onto `M_(B,lambda)^perp` is nonzero.  The
squared norm of that projection is the Gram Schur complement (3.3), which
proves the first equivalence.  Row-space orthogonality says precisely that
a column perturbation in `ker(A,P)` pairs nontrivially with the shallow
row, proving the second equivalence.  The singular value of this rank-one
multiplicity projection is `sqrt(eta)`, giving (3.5).  `square`

If one computes with the raw position vectors in (3.0c)--(3.0d), the
factor `sqrt(b!/d_lambda)` must be restored before using (3.5).  It
cancels from the qualitative span test (3.4), but not from a numerical
right-inverse norm.

All entries of the five-vector Gram matrix are finite orbit correlations.
For example, the two unexposed central entries are the known punctured
pair-codegree kernels, entries involving `R_D` are first- or second-
blocker duplicate correlations, and the shallow entries are the mixed-root
gap kernels.  Thus (3.3) is a bounded list of scalar sums, not the original
`b!`-variable LP.

## 4. Calibrations at `r=4,5`

For `b=9`, `k=2`, the balanced pair-current space is the irreducible

\[
                              V_{(7,2)},\qquad\dim V_{(7,2)}=27.          \tag{4.1}
\]

The exact complete-catalogue rank theorem proves

\[
                              \eta_{2,(7,2)}>0,               \tag{4.2}
\]

and in fact `Q_2(ker(A,P))` is the whole module (4.1).  The companion Haar
calculation proves something subtler: the obvious puncture-averaged Haar
orbit supplies the desired `V_(7,2)` current, but its exposure image
down-projects to a nonzero scalar multiple of that same current.  Hence
that particular orbit lies outside `ker P`, even though a more global
compensated preimage exists by (4.2).

This is exactly the geometry predicted by (3.3): positivity of the Schur
complement is a statement about the full multiplicity space, not about one
named trade vector.

At `r=5`, the depth-two target rank is `k=3`.  The exact complete-catalogue
rank theorem gives

\[
 Q_3(\ker(A,P))
 =\left\{j:\sum_{T\ni a}j_T=0\text{ for every }a\right\}
 \cong V_{(9,2)}\oplus V_{(8,3)}.                  \tag{4.3}
\]

The two summands have dimensions `44` and `110`.  Hence

\[
 \eta_{3,(9,2)}>0,\qquad \eta_{3,(8,3)}>0.         \tag{4.4}
\]

This tests both nontrivial depth-two modules and is stronger evidence for
the qualitative all-`r` criterion.  The same exact certificate also tests
the adjacent full cyclic ranks and gives

\[
\begin{aligned}
 Q_2(\ker(A,P))
   &\cong V_{(9,2)},\\
 Q_4(\ker(A,P))
   &\cong V_{(9,2)}\oplus V_{(8,3)}\oplus V_{(7,4)}.
\end{aligned}                                                   \tag{4.5}
\]

Consequently the corresponding `eta_(k,lambda)` is positive for every
nontrivial module present at each tested `k=2,3,4`.  This finite statement
does not cover untested ranks or supply any uniform lower bound for the
normalized quantities in Section 5.

## 5. Exact asymptotic gate

For the stopped Gate-B application one needs more than nonvanishing.  A
suitable normalization is essential.  For the uniform baseline
`lambda_G^0=1/b!`, the entropy Hessian gives the Fisher norm

\[
 \|\delta\|_{\rm F}^2
   =\sum_G{\delta_G^2\over\lambda_G^0}
   =b!\,\|\delta\|_2^2.                            \tag{5.1}
\]

Thus the squared singular value in Fisher input norm and standard shallow
output norm is

\[
                         \bar\eta_{k,\lambda}
                         ={\eta_{k,\lambda}\over b!}.          \tag{5.2}
\]

This standard-output quantity cannot have a polynomial lower bound through
the whole depth-two band.  Indeed, let `theta_(k,lambda)` be the
unconstrained squared Fisher singular value of the full cyclic shallow
operator.  Its target covariance has trace `b`, and the multiplicity of
the `lambda=(b-j,j)` eigenvalue is

\[
 d_j={b\choose j}-{b\choose{j-1}}.
\]

Consequently `theta_(k,lambda)<=b/d_j` and
`bar eta_(k,lambda)<=theta_(k,lambda)`.  At `k=j=r-2`,

\[
 d_{r-2}={6\over r+4}{2r+1\choose r-2},             \tag{5.3}
\]

so even the unconstrained standard-output singular value is exponentially
small.  Thus a condition `bar eta>=r^(-C)` in standard Euclidean target
norm is impossible.

The natural relative-density output divides each shallow coordinate by its
uniform marginal

\[
                         p_k={b\over {b\choose k}}.             \tag{5.4}
\]

Put

\[
 \alpha_{k,\lambda}={\eta_{k,\lambda}\over
                            \|m_{k,\lambda}\|^2}\in[0,1],
 \qquad
 \Theta_{k,\lambda}={\theta_{k,\lambda}\over p_k^2}.          \tag{5.5}
\]

The corrected complete-catalogue squared singular value is then

\[
 \boxed{\widehat\sigma_{k,\lambda}^2
       =\alpha_{k,\lambda}\Theta_{k,\lambda}.}                 \tag{5.6}
\]

A sufficient complete-catalogue input would give

\[
 \alpha_{r-q,(b-j,j)}\Theta_{r-q,(b-j,j)}\ge r^{-C}            \tag{5.7}
\]

on enough modules to synthesize the desired nested current for every
`2<=q<=H`, with the target-current norm stated explicitly.  Even (5.7)
controls only a Hilbert norm.  Nonnegativity relative to the uniform law
requires a delocalized right inverse: for the produced perturbation one
must also prove, in an appropriate simultaneous all-depth norm,

\[
 \left\|{\delta\over\lambda^0}\right\|_\infty
       \le r^C\|j\|_* .                            \tag{5.8}
\]

For each fixed `r`, any finite signed direction allows some sufficiently
small positive amplitude.  Without (5.8), however, that amplitude may be
exponentially too small to create Gate-B drift.  Therefore (3.5) alone
does not yet yield a quantitatively usable Gibbs tilt.

The stopped residual additionally requires stability: the normalized
singular values and delocalization bound must not collapse before the
terminal density, or their collapse must trigger a priority cleanup of
negligible total cost.  Those are the precise analytic statements.  The
reduction neither assumes nor proves them.

After symmetry is broken, there is no literal Specht block.  Here
"stability" means the corresponding constrained singular value of the
current restricted operators `(A_j,P_j,Q_j)`, compared with its complete
block value; it is not an assertion that the residual remains a group
module.

The conceptual gain is that the proposed adaptive construction is no
longer an opaque exponential-dimensional rate LP.  At the symmetric
starting state its all-depth freedom is governed, module by module, by the
five-vector scalar quantity (3.3); `r=4` proves that this quantity is
genuinely positive in the first nontrivial depth-two module, and `r=5`
does so in both of its depth-two modules.

## 6. Mechanical orientation audit

The standard-library checker

```text
python3 scratch/verify_all_r_compensated_gibbs_orientation_20260822.py
```

exhausts the catalogues at `r=2,3`.  It verifies injectivity, the
matrix-coefficient identity (3.0b), the convention
`D(g,h)=kappa(g^{-1}h)`, the right-convolution formula (1.6b), and its
commutation with the left action.  It is an orientation audit, not a
substitute for the open normalized estimates (5.3)--(5.4).
