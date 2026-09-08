# M-convex sufficiency for the all-depth dual, and failure in the selector atlas

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, random rounding,
generic discrepancy theorem, or web input is used.

## 0. Result

This note strengthens the weighted Hall/Farkas theorem in
\`MATH_THEOREM_SELECTOR_CONDITIONED_CONFIGURATION_LP_AND_HALL_DUAL_20260726.md\`
under a precise discrete-convexity hypothesis.

### Positive theorem

If every selector fibre's complete option-load set is \(M\)-convex,
equivalently it is the full set of integer points of an integral
polymatroid base polytope, then the exact weighted all-depth dual is
sufficient for an **integral** balanced selection.  No rounding error is
needed.  If the hypothesis fails only on \(o(W/H)\) owner mass, it gives
all-depth aggregate error \(o(W)\).

### Audit of the actual atlas

The rank-twisted selector atlas is not \(M\)-convex.  At lower depth one,
the direction-count projection of one fibre option is

\[
                         L_f\mathbf1_A,\qquad
                         L_f={|V_f|\over r},          \tag{0.1}
\]

where \(A\) is its active \(r\)-set.  A unit exchange between two active
sets would create direction counts \(L_f-1\) and \(1\), but every legal
option has only \(0\) or \(L_f\) in every direction.  Thus the symmetric
exchange axiom fails.

The primitive support-changing step in the quotient exchange lattice has
\(\ell^1\)-norm \(2L_f\).  Since

\[
                         L_f={2^{n_f}\over r},        \tag{0.2}
\]

the local exchange/Graver scale is unbounded and in fact exponential in
the fibre dimension.  Complete affine conjugates do not change this
projection, and complete selector batching does not repair it because
literal targets retain the selector label.

Hence the polymatroidal sufficiency theorem does not prove coefficient
one for the current atlas.  This is a concrete structural failure, not a
mere absence of a known rounding argument.

## 1. Integral base-polytope hypothesis

Let \(E\) be the set of all literal target coordinates
\((\sigma,q,T)\), with both signs and \(1\le q\le H\).  For a selector
fibre \(f\), let

\[
 \mathcal A_f=\{a_{f,\omega}\in\mathbb Z_{\ge0}^E:
                         \omega\in\Omega_f\}          \tag{1.1}
\]

be its complete option-load set.

For an integer-valued submodular function
\(p_f:2^E\to\mathbb Z\), write

\[
 B(p_f)=\{x\in\mathbb R^E:
      x(S)\le p_f(S)\ \text{for all }S\subseteq E,\
      x(E)=p_f(E)\}.                                 \tag{1.2}
\]

The required saturation hypothesis is

\[
                 \boxed{\mathcal A_f=B(p_f)\cap\mathbb Z^E.}       \tag{1.3}
\]

Sets satisfying (1.3) are the \(M\)-convex sets.  It is not enough that
\(\operatorname{conv}\mathcal A_f\) merely have the same real span as a
base polytope: every integer point is required.

The equivalent symmetric exchange axiom says that, for
\(x,y\in\mathcal A_f\) and \(i\) with \(x_i>y_i\), there is \(j\) with
\(x_j<y_j\) such that

\[
 x-e_i+e_j\in\mathcal A_f,\qquad
 y+e_i-e_j\in\mathcal A_f.                           \tag{1.4}
\]

The fixed total-load equations for each sign and depth can be encoded by
making the corresponding colour classes separate direct-sum components.

## 2. The balanced quota set is M-convex

For a colour \(c=(\sigma,q)\), recall

\[
 h_q=\left\lfloor{W_0\over N_q}\right\rfloor,\qquad
 R_q=W_0-h_qN_q.                                    \tag{2.1}
\]

Its balanced integer load set is

\[
 \mathcal B_{c,\mathbb Z}
 =\{h_q\mathbf1+y:y\in\{0,1\}^{N_q},\
                         \mathbf1^Ty=R_q\}.           \tag{2.2}
\]

The vectors \(y\) are precisely the bases of the uniform matroid
\(U_{R_q,N_q}\).  Hence (2.2) is a modular translation of an
\(M\)-convex set.  Taking the direct sum over all signs and depths gives

\[
          \mathcal B_{\mathbb Z}
             =\bigoplus_{c\in\mathcal C}
                         \mathcal B_{c,\mathbb Z},   \tag{2.3}
\]

again \(M\)-convex.  Its convex hull is exactly the product of translated
hypersimplices used in the weighted dual.

## 3. Integral sufficiency theorem

### Theorem 3.1 (M-convex all-depth rounding)

Assume (1.3) for every retained fibre.  If the weighted Hall/Farkas
inequality

\[
 \sum_f\min_{\omega\in\Omega_f}
          \langle\lambda,a_{f,\omega}\rangle
 \le h_{\mathcal B}(\lambda)                         \tag{3.1}
\]

holds for every \(\lambda\in\mathbb R^E\), then there are options
\(\omega_f\in\Omega_f\) such that

\[
                         \sum_fa_{f,\omega_f}
                              \in\mathcal B_{\mathbb Z}.            \tag{3.2}
\]

Thus every literal lower and upper target at every protected depth has
one of its two exact floor/ceiling loads, with the correct reset count.

#### Proof

By the weighted dual theorem, (3.1) is equivalent to

\[
 \left(\sum_f\operatorname{conv}\mathcal A_f\right)
                    \cap\operatorname{conv}\mathcal B_{\mathbb Z}
                         \ne\varnothing.             \tag{3.3}
\]

Minkowski sums of base polytopes satisfy

\[
                         \sum_fB(p_f)=B\!\left(\sum_fp_f\right).    \tag{3.4}
\]

One proof is by support functions: the greedy formula for a base
polytope is additive in its submodular rank function.  Integral base
polytopes also have the integer decomposition property,

\[
 B\!\left(\sum_fp_f\right)\cap\mathbb Z^E
    =\sum_f\bigl(B(p_f)\cap\mathbb Z^E\bigr).         \tag{3.5}
\]

This is the integral polymatroid decomposition theorem; it also follows
inductively from the symmetric exchange axiom.

The two polytopes in (3.3) are therefore integral base polytopes.  The
integral polymatroid-intersection theorem says that their nonempty
intersection contains an integer point \(b\).  By (2.3),
\(b\in\mathcal B_{\mathbb Z}\).  By (3.5) and (1.3), write

\[
                         b=\sum_fa_f,\qquad
                         a_f\in\mathcal A_f.          \tag{3.6}
\]

Choose the option realizing each \(a_f\).  This proves (3.2).
\(\square\)

### Corollary 3.2 (negligible exceptional fibres)

Suppose Theorem 3.1 applies after discarding fibres of total owner mass
\(\varepsilon W\).  Every discarded owner contributes one occurrence to
each of the \(2H\) signed depth ledgers.  Hence exact balancing on the
good fibres, followed by literal treatment of the discarded fibres,
has aggregate error at most

\[
                              2H\varepsilon W.        \tag{3.7}
\]

In particular, exceptional mass \(o(W/H)\) gives \(o(W)\) aggregate
all-depth error.

This is the sense in which an \(M\)-convex theorem would be directly
usable for coefficient one.

## 4. Concrete exchange failure in one selector fibre

Fix one retained selector fibre \(f\), having

\[
                         |V_f|=2^{n_f}               \tag{4.1}
\]

owners after its selector axes are frozen.  Project a configuration
vector to its lower-depth-one counts by deleted physical direction:

\[
 \pi:\mathbb Z^E\longrightarrow\mathbb Z^{n_f},\qquad
 \pi_j(a)=\sum_{\substack{T:\ \text{the unique}\\
                    \text{zeroed axis is }j}}
                         a^{-,1}(T).                 \tag{4.2}
\]

In an isometric \(C_{2r}\)-factor of \(Q_r\), each of the \(r\)
directions occurs twice on every cycle.  There are
\(2^r/(2r)\) cycles, and there are \(2^{n_f-r}\) parallel packets in
the fibre.  Therefore every active direction contributes exactly

\[
             2^{n_f-r}\,{2^r\over r}
                         ={2^{n_f}\over r}=L_f        \tag{4.3}
\]

depth-one targets.  Inactive directions contribute none.  Consequently

\[
 \boxed{
 \pi(\mathcal A_f)
   =\{L_f\mathbf1_A:A\in\tbinom{[n_f]}r\}.}          \tag{4.4}
\]

Affine compiler conjugation changes the target identities inside these
direction classes but not (4.4).

Choose disjoint active \(r\)-sets \(A,B\), possible because
\(r=o(n_f)\), and choose configurations \(x,y\) with those supports.
There is a literal target coordinate \(i\) of an \(A\)-direction for
which \(x_i=1,y_i=0\).  If (1.4) held, there would be a coordinate \(j\)
with \(x_j=0,y_j=1\) and a legal configuration
\(x-e_i+e_j\).  Fixed colour totals force \(j\) to be another
lower-depth-one coordinate, necessarily in a \(B\)-direction.
Its direction projection has one coordinate \(L_f-1\), another
coordinate \(1\), and the remaining \(A\)-coordinates \(L_f\).  This is
not of the form (4.4) when \(L_f>1\).

Thus (1.4) fails.  The option set is not \(M\)-convex.  No claim about
all integer points of its full high-dimensional convex hull is needed.

## 5. Failure of bounded exchange and Graver-scale hypotheses

The difference lattice of the projected set (4.4) is

\[
 \operatorname{span}_{\mathbb Z}
   \{\pi(x)-\pi(y):x,y\in\mathcal A_f\}
 =L_f\{z\in\mathbb Z^{n_f}:\mathbf1^Tz=0\}.          \tag{5.1}
\]

Its primitive conformal support-changing moves are

\[
                         L_f(e_i-e_j),               \tag{5.2}
\]

of \(\ell^1\)-norm \(2L_f\).  Hence any Markov, exchange, or Graver
system which changes the active support has a quotient move of size at
least

\[
                         2L_f={2^{n_f+1}\over r}.     \tag{5.3}
\]

There is no fibre-uniform bounded exchange complexity.

Bounded Graver norm would not, by itself, have made the fractional dual
integral.  For example, the fixed \(3\times3\) matrix

\[
 \begin{pmatrix}
  1&1&0\\
  0&1&1\\
  1&0&1
 \end{pmatrix}                                      \tag{5.4}
\]

has bounded finite-dimensional Graver complexity, but the equations
\(Ax=\mathbf1,\ x\ge0\) have the fractional solution
\((1/2,1/2,1/2)\) and no integer solution.  What is needed is
total unimodularity, normality, or an integer decomposition theorem, not
merely a quantitative augmentation bound.

## 6. Why complete selector batching does not restore M-convexity

Index the projection (4.2) also by the decoded selector value \(z\).
For a complete selector batch, its literal projection is

\[
        \bigl(L_f\mathbf1_{A_z}\bigr)_{z\in\mathbb F_2^t}.          \tag{6.1}
\]

Forgetting \(z\) makes the complete-design average perfectly uniform.
Literal targets retain \(z\), so the feasible set before quotienting is
a direct product of scaled matroid-base sets (4.4).  Each factor still
has the same unit-exchange hole and primitive scale \(L_f\).

Thus batching proves exact quotient marginals but not the saturation
hypothesis (1.3).  Any successful integral theorem must introduce
cross-fibre trades that break the selector decoder, or prove normality
only after combining a growing family of differently selected status
cells.  That property is not present in the current atlas theorem.

## 7. Audited consequence

The all-depth weighted dual becomes an integral sufficiency theorem under
a strong but standard structural hypothesis: saturated polymatroidal
option sets.  The balanced quota resets are fully compatible with that
hypothesis.

The actual rank-twisted selector fibres fail it at the first protected
depth, by the exact direction-count projection (4.4).  They also fail
every bounded local-exchange version at the exponential scale (5.3).
Therefore no \(M\)-convex, polymatroid-intersection, or bounded-Graver
rounding argument can be applied to the atlas without a new
cross-fibre recoupling operation.

The smallest such operation is audited in
\`MATH_THEOREM_CROSS_FIBRE_QR_PLUS_ONE_RECOUPLING_AND_SCALED_CONGRUENCE_20260726.md\`.
A \(Q_{r+1}\) slab has \(r+1\) two-packet resolutions whose normalized
direction vectors form \(U_{r,r+1}\), but the literal direction lattice
retains the unavoidable atom \(2^r/r\) and a cubical parity factor two.
