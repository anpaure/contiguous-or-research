# A noncancelling determinant enumerator for Catalan linear matchings

Date: 2026-07-31  
Status: exact all-\(m\) determinant/exterior-algebra identity, an exact
real-stability obstruction, and complete \(m=2,3\) calibrations. The identity
does **not** prove all-\(m\) nonvanishing.

## 0. Verdict

The directed acyclicity condition in the ordered four-transversal can be
filtered by one determinant **without signs or cancellation**. Three
partition determinants and one directed matrix-forest determinant have a
coefficientwise product whose coefficient of an atom set is exactly \(1\)
when that set is a Catalan linear matching and \(0\) otherwise.

Thus the Catalan Linear Matching Theorem is equivalent to nonvanishing of
one explicit homogeneous multiaffine polynomial. This is a concrete
exterior-algebra target, not merely an analogy with the matrix-tree theorem.

There is also a sharp limitation. Already at \(m=2\) the resulting positive
enumerator is not real stable: its support fails basis exchange. Hence it
cannot be replaced by one positive-semidefinite determinantal polynomial,
and the standard real-stable/mixed-discriminant capacity theorem cannot
prove its nonvanishing directly. The remaining operation is a four-fold
coefficientwise (Hadamard) intersection, exactly where the known odd
resource circuits live.

## 1. The four matrices

Use the notation of
MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md:

\[
 \mathcal L=\binom{\Omega}{m-1},\qquad
 \mathcal X=\binom{\Omega}{m},\qquad
 \mathcal U=\binom{\Omega}{m+1},
\]

\[
 N=|\mathcal L|=|\mathcal U|=m\operatorname{Cat}_m,
 \qquad M=|\mathcal X|=(m+1)\operatorname{Cat}_m.
\]

Let \(\mathcal Q_m\) be the ordered diamond atoms

\[
 q=(L,U,T,H),\qquad L=T\cap H,\quad U=T\cup H.
\]

For every atom let

\[
 \lambda_q=e_L\in\mathbb R^{\mathcal L},\quad
 \upsilon_q=e_U\in\mathbb R^{\mathcal U},\quad
 t_q=e_T\in\mathbb R^{\mathcal X},\quad
 h_q=e_H\in\mathbb R^{\mathcal X},
\]

and put

\[
                         c_q=t_q-h_q.                 \tag{1.1}
\]

Write \(\Lambda,V,T,H,C\) for the matrices with these vectors as columns.
For \(I\subseteq\mathcal Q_m\), append a subscript \(I\) to restrict to
the selected columns.

The first three Gram determinants below are ordinary partition-matroid
indicators:

\[
 \det(\Lambda_I^{*}\Lambda_I),\qquad
 \det(V_I^{*}V_I),\qquad
 \det(H_I^{*}H_I).                                  \tag{1.2}
\]

Each is \(1\) when the corresponding labels are distinct and \(0\)
otherwise. The tail condition and acyclicity will be imposed together,
rather than by a fourth partition determinant plus a separate graphic
determinant.

## 2. The directed determinant is a zero-one forest filter

### Theorem 2.1 (path-forest determinant)

For any \(I\subseteq\mathcal Q_m\) with \(|I|=N\), assume that the selected
heads are distinct. Then

\[
 \det(T_I^{*}C_I)=
 \begin{cases}
  1,&\text{the tails are distinct and the selected directed graph is acyclic},\\
  0,&\text{otherwise}.
 \end{cases}                                      \tag{2.1}
\]

#### Proof

If two selected tails coincide, the corresponding two rows of
\(T_I^{*}C_I\) coincide, so its determinant is zero.

Suppose the tails are distinct. Index the columns by their selected tails.
Then

\[
                 T_I^{*}C_I=I-P,                    \tag{2.2}
\]

where

\[
 P_{ij}=1\quad\Longleftrightarrow\quad
 \text{the head of arc }j\text{ is the tail of arc }i.
\]

Distinct tails and distinct heads make \(P\) a partial permutation matrix.
Its components are directed paths and directed cycles. On a path block
\(P\) is nilpotent, so \(\det(I-P)=1\). On a cycle block \(P\) has
eigenvalue one, so \(\det(I-P)=0\). Taking the product over blocks proves
(2.1). \(\square\)

No choice of roots and no matrix-tree sum is needed.

### Corollary 2.2 (sign-definite set formula)

For \(|I|=N\), define

\[
 w(I)=
 \det(\Lambda_I^{*}\Lambda_I)
 \det(V_I^{*}V_I)
 \det(H_I^{*}H_I)
 \det(T_I^{*}C_I).                                  \tag{2.3}
\]

Then \(w(I)\in\{0,1\}\), and

\[
 w(I)=1
 \quad\Longleftrightarrow\quad
 I\text{ is an ordered Catalan linear matching}.    \tag{2.4}
\]

Cardinality \(N\) plus distinct lower and upper labels makes both outer
maps bijections. The head Gram factor and Theorem 2.1 give injective heads,
injective tails, and no directed cycle. This is exactly the ordered
four-transversal normal form. Conversely every such transversal makes all
four factors one.

In particular,

\[
 \boxed{
 |\mathfrak F_m|=
 \sum_{\substack{I\subseteq\mathcal Q_m\\|I|=N}}
 \det(\Lambda_I^{*}\Lambda_I)
 \det(V_I^{*}V_I)
 \det(H_I^{*}H_I)
 \det(T_I^{*}C_I).
 }                                                   \tag{2.5}
\]

Every nonzero summand in (2.5) is \(+1\).

## 3. Exterior algebra and the exact Hadamard identity

Let \(Z=\operatorname{diag}(z_q:q\in\mathcal Q_m)\), and define

\[
\begin{aligned}
 p_{\lambda}(z)&=\det(I+\Lambda Z\Lambda^{*}),\\
 p_{\upsilon}(z)&=\det(I+VZV^{*}),\\
 p_{\eta}(z)&=\det(I+HZH^{*}),\\
 p_{\rm df}(z)&=\det(I+CZT^{*}).                    \tag{3.1}
\end{aligned}
\]

The first three polynomials are explicit partition polynomials; for
example

\[
 p_{\lambda}(z)=
 \prod_{L\in\mathcal L}
 \left(1+\sum_{q:\lambda(q)=L}z_q\right).            \tag{3.2}
\]

Cauchy--Binet gives, for every atom set \(I\),

\[
\begin{aligned}
 [z^I]p_{\lambda}&=\det(\Lambda_I^{*}\Lambda_I),\\
 [z^I]p_{\upsilon}&=\det(V_I^{*}V_I),\\
 [z^I]p_{\eta}&=\det(H_I^{*}H_I),\\
 [z^I]p_{\rm df}&=\det(T_I^{*}C_I).                 \tag{3.3}
\end{aligned}
\]

For multiaffine polynomials write \(f\star g\) for coefficientwise
Hadamard product. If \((\cdot)_{[N]}\) denotes the homogeneous degree-\(N\)
part, the exact positive solution enumerator is

\[
 \boxed{
 \mathcal E_m(z)=
 \bigl(p_{\lambda}\star p_{\upsilon}\star
       p_{\eta}\star p_{\rm df}\bigr)_{[N]}
 =\sum_{F\in\mathfrak F_m}z^F.
 }                                                   \tag{3.4}
\]

Formula (3.3) has a literal exterior-algebra reading. The coefficient
\(\det(T_I^{*}C_I)\) is the diagonal contraction

\[
 \sum_{S\in\binom{\mathcal X}{N}}
       \det(T_{S,I})\det(C_{S,I})                    \tag{3.5}
\]

between the tail-transversal wedge and the oriented-incidence wedge. When
the tails are distinct only the tail image can contribute, and (3.5)
becomes \(\det(I-P)\).

Consequently the Catalan Linear Matching Theorem is equivalent to

\[
 \mathcal E_m\not\equiv0
 \quad\Longleftrightarrow\quad
 \operatorname{supp}p_{\lambda}\cap
 \operatorname{supp}p_{\upsilon}\cap
 \operatorname{supp}p_{\eta}\cap
 \operatorname{supp}p_{\rm df}\cap
 \binom{\mathcal Q_m}{N}\ne\varnothing.             \tag{3.6}
\]

This is a four-support intersection, not a five-matroid intersection. The
reduction is genuine, but the last support intersection is still the
integral-correlation theorem.

## 4. Three rigorous barriers to standard algebraic shortcuts

### 4.1 Plain characteristic-two parity vanishes

Reverse every selected arc:

\[
                    (L,U,T,H)\longleftrightarrow(L,U,H,T). \tag{4.1}
\]

This is a fixed-point-free involution on \(\mathfrak F_m\). Therefore

\[
                         |\mathfrak F_m|\equiv0\pmod2.       \tag{4.2}
\]

More strongly, after the specialization
\(z_{(L,U,T,H)}=z_{(L,U,H,T)}\), the two monomials in every reversal pair
coincide, so \(\mathcal E_m\) vanishes in characteristic two. A parity
proof must first fix an orientation gauge or retain orientation-sensitive
variables.

### 4.2 The directed-forest determinant is itself not stable

This failure occurs before taking any Hadamard product. At \(m=2\), use the
directed Johnson triangle

\[
             12\longrightarrow13\longrightarrow14\longrightarrow12.
                                                               \tag{4.3}
\]

Its three arcs are valid ordered diamonds. Set every other atom variable to
zero. Every proper subset of the triangle is a directed forest, while the
three-edge set is a directed cycle. Therefore the corresponding
specialization of \(p_{\rm df}\) is

\[
              1+x+y+z+xy+yz+zx.                    \tag{4.4}
\]

On the diagonal \(x=y=z=t\) this is

\[
                        1+3t+3t^2,                  \tag{4.5}
\]

whose discriminant is \(-3\). A real-stable polynomial remains real-rooted
under a real diagonal specialization. Hence

\[
                         \boxed{p_{\rm df}\text{ is not real stable}.} \tag{4.6}
\]

Thus even before accounting for the three palettes, the nonsymmetric
nilpotence determinant lies outside the ordinary stable matrix-tree
framework.

### 4.3 The positive enumerator is not real stable

At \(m=2\), let the outer perfect matchings be

\[
 P=(2,3,4,1),\qquad Q=(2,4,1,3).                    \tag{4.7}
\]

Their physical lifts are respectively

\[
 14-13-23\ \sqcup\ 12-24-34,
 \qquad
 13-14-24\ \sqcup\ 12-23-34.                       \tag{4.8}
\]

Orient both path forests consistently. They give two members of
\(\operatorname{supp}\mathcal E_2\). Remove from \(P\) the atom whose
lower colour is \(3\) and whose upper colour omits \(4\). No atom of
\(Q\setminus P\) has both that lower and that upper colour. Hence no
one-element exchange restores the two outer bijections, and
\(\operatorname{supp}\mathcal E_2\) fails basis exchange.

The support of every homogeneous multiaffine real-stable polynomial with
nonnegative coefficients is the base family of a matroid. Consequently

\[
                         \boxed{\mathcal E_2\text{ is not real stable}.} \tag{4.9}
\]

In particular, the exact positive enumerator cannot be one Hermitian
positive-semidefinite determinant polynomial, nor can its nonvanishing be
deduced by applying the usual real-stable/mixed-discriminant capacity
theorem to (3.4) as though Hadamard intersection preserved that structure.

This does not rule out a non-Hermitian determinant identity—
\(p_{\rm df}\) in (3.1) is already non-Hermitian—or an identity using
auxiliary variables and a nonlocal projection. It rules out the most
direct stable-polynomial shortcut from the known uniform fractional point
to one-copy integral nonvanishing.

## 5. Exact small-case calibration

The companion audit gives:

| \(m\) | result |
|---:|---|
| 2 | all \(6^4=1296\) lower-complete ordered selections exhausted; (2.3) is \(1\) on exactly \(24\) and \(0\) on the rest |
| 3 | \(458544\) undirected Catalan linear matchings; \(9549888\) ordered four-transversals |
| 4 | the explicit repaired decorated \(ML(7)\) fixture gives one literal positive determinant term and a \(\operatorname{Cat}_4=14\)-path lift |

At \(m=3\), the undirected solutions by number of nontrivial path
components are

\[
 (2:5760),\qquad(3:82920),\qquad
 (4:185760),\qquad(5:184104).                       \tag{5.1}
\]

Each forest has two coherent orientations per nontrivial path, and

\[
 5760\,2^2+82920\,2^3+185760\,2^4+184104\,2^5
 =9549888.                                          \tag{5.2}
\]

Run

~~~text
python3 scratch/audit_catalan_noncancelling_determinant_enumerator_20260731.py
~~~

The audit reconstructs the \(m=4\) diamonds from the displayed Hamilton
cycle and turn SDRs; it does not trust a precomputed ordered-atom file.

## 6. What remains

Identity (3.4) answers the determinant/exterior-algebra formulation
question sharply:

* acyclicity causes no sign problem;
* tail injection and acyclicity collapse to one determinant;
* every surviving term has coefficient \(+1\);
* raw parity and real-stable capacity are provably unavailable (already
  the directed-forest factor has a non-real-rooted triangle specialization);
* the missing theorem is nonemptiness of one four-fold Hadamard support
  intersection.

A successful algebraic proof must exploit more than the separate Newton
polytopes or the uniform fractional point. It must prove a special Boolean
support-intersection identity for the diamond tensor, or introduce an
orientation-sensitive gauge/recursive factorization absent from generic
mixed-discriminant theory. No such all-\(m\) nonvanishing theorem is proved
here.
