# All-shuffle weighted Hall min-max for the canonical packet atlas

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Use the canonical owner-disjoint product-cell family

\[
                         \mathscr C,\qquad
 |\mathscr C|={G\over2^s},\qquad G=W-o(W),              \tag{0.1}
\]

and assume \(H\le s/2\). In every \(Q_s\)-cell allow the complete
all-shuffle conjugate menu

\[
                         \Gamma_s=\mathbb F_2^s\rtimes S_s             \tag{0.2}
\]

of the recursive half-depth injective factor. The permutation part is the
all-shuffle order array; the translation part varies affine phase without
changing the direction order.

For every tagged rank \(j=(q,\epsilon)\), put

\[
 \mathcal T_j=\binom{[n]}{m+\epsilon q},\qquad
 N_j=|\mathcal T_j|.                                   \tag{0.3}
\]

Each selected factor contributes exactly \(G\) physical target occurrences
at rank \(j\). Write

\[
                         c_j=\left\lfloor{G\over N_j}\right\rfloor,
 \qquad R_j=G-c_jN_j.                                  \tag{0.4}
\]

The balanced floor/ceiling polytope is

\[
 \mathcal B_j=
 \left\{b\in\mathbb R^{\mathcal T_j}:
 c_j\le b_T\le c_j+1,\quad\sum_Tb_T=G\right\}.          \tag{0.5}
\]

Its vertices are exactly the integer vectors with \(R_j\) coordinates
\(c_j+1\) and the others \(c_j\).

Let \(\mathcal P\) be the Minkowski sum of the cell choice polytopes:

\[
 \mathcal P=
 \sum_{c\in\mathscr C}
 \operatorname {conv}\{
 {\bf1}_{\mathcal S(c,g)}:g\in\Gamma_s\},              \tag{0.6}
\]

where \(\mathcal S(c,g)\) is the complete physical target tower through
all \(q\le H\) and both signs. Put

\[
                         \mathcal B=\prod_j\mathcal B_j.             \tag{0.7}
\]

The exact fractional floor/ceiling criterion is:

\[
\boxed{
 \mathcal P\cap\mathcal B\ne\varnothing
 \iff
 \sum_{c\in\mathscr C}
   \max_{g\in\Gamma_s}
     \sum_{T\in\mathcal S(c,g)}\alpha_T
 \ge
 \sum_j\left[
 c_j\sum_{T\in\mathcal T_j}\alpha_T
 +
 \sum_{i=1}^{R_j}\alpha^{\uparrow}_{j,i}
 \right]
 \quad(\alpha\in\mathbb R^{\mathcal T}).}              \tag{0.8}
\]

Here
\(\alpha^\uparrow_{j,1}\le\cdots\le\alpha^\uparrow_{j,N_j}\) are the
ordered weights at tagged rank \(j\). Equation (0.8) is the exact
all-weight Hall min-max theorem. Indicator-set cuts are only a subfamily.

The all-shuffle barycenter is physical and explicit. If
\(d_j(T)\) is the number of candidate product cells containing the unique
affine face with trace \(T\), then

\[
\boxed{
 \lambda_j(T)=p_{s,q}d_j(T),\qquad
 p_{s,q}={2^q\over\binom sq}.}                         \tag{0.9}
\]

The vector \(\lambda=(\lambda_j)_j\) belongs to \(\mathcal P\), and for
every real weight vector \(\alpha\),

\[
\boxed{
 \sum_c\max_g\alpha(\mathcal S(c,g))
 \ge\langle\alpha,\lambda\rangle.}                     \tag{0.10}
\]

Thus all physical Hall weights are controlled—not merely sectorwise
weights—up to the distance of \(\lambda\) from the floor/ceiling polytope.
Define

\[
 L_j=\sum_T(c_j-\lambda_j(T))_+,\qquad
 U_j=\sum_T(\lambda_j(T)-c_j-1)_+.                     \tag{0.11}
\]

Then the exact \(\ell_1\)-distance is

\[
\boxed{
 D_j:=\operatorname {dist}_1(\lambda_j,\mathcal B_j)
 =2\max\{L_j,U_j\}.}                                   \tag{0.12}
\]

Consequently, for every \(\alpha\) with
\(\|\alpha\|_\infty\le1\),

\[
\boxed{
 \min_{b\in\mathcal B}\langle\alpha,b\rangle
 -\sum_c\max_g\alpha(\mathcal S(c,g))
 \le\sum_jD_j.}                                        \tag{0.13}
\]

Therefore

\[
                         \sum_jD_j=o(W)                 \tag{0.14}
\]

is a sufficient theorem that every weighted fractional Hall cut is
controlled up to \(o(W)\).

The distance has an exact physical Gram reduction. Let

\[
 \mathcal A_j(c)=
 \{T:T\text{ is the }j\text{-trace of an affine }q
       \text{-face of }c\},                            \tag{0.15}
\]

and put

\[
 I_j(c,c')=|\mathcal A_j(c)\cap\mathcal A_j(c')|.       \tag{0.16}
\]

Then

\[
\boxed{
 V_j:=\sum_T(d_j(T)-\overline d_j)^2
 =\sum_{c,c'}I_j(c,c')
  -{1\over N_j}
     \left(G{\binom sq\over2^q}\right)^2,}              \tag{0.17}
\]

and

\[
\boxed{
 D_j\le
 \|\lambda_j-(G/N_j){\bf1}\|_1
 \le p_{s,q}\sqrt{N_jV_j}.}                            \tag{0.18}
\]

Hence the fully physical pair-overlap estimate

\[
\boxed{
 \sum_{j=(q,\epsilon),\,q\le H}
 p_{s,q}\sqrt{N_jV_j}=o(W)}                            \tag{0.19}
\]

implies (0.14), and therefore controls every fractional dual weight by
\(o(W)\). This is the smallest exact second-moment target produced by the
all-shuffle route.

What remains unresolved is integrality. The polytope \(\mathcal P\) is the
convex hull of deterministic one-conjugate-per-cell load vectors, but
\(\mathcal P\cap\mathcal B\ne\varnothing\) does not imply that one such
vertex lies in \(\mathcal B\). Generic discrepancy rounding has additive
error of the wrong scale at shallow ranks. Thus a proof of (0.19) would
settle the weighted fractional gate, but coefficient one still requires a
specialized one-sided rounding theorem for the resolvable shadow towers.

## 1. Exact deterministic and fractional formulations

For \(c\in\mathscr C\) and \(g\in\Gamma_s\), let

\[
                         v_{c,g}={\bf1}_{\mathcal S(c,g)}
 \in\{0,1\}^{\mathcal T}.                              \tag{1.1}
\]

Packet-wide injectivity gives exactly \(2^s\) ones in every tagged-rank
block of \(v_{c,g}\). A deterministic order field is a tuple

\[
                         g_\bullet=(g_c:c\in\mathscr C),             \tag{1.2}
\]

with load vector

\[
                         n(g_\bullet)=\sum_cv_{c,g_c}.  \tag{1.3}
\]

It is a perfect floor/ceiling field precisely when

\[
                         n(g_\bullet)\in\mathcal B.      \tag{1.4}
\]

Thus the exact deterministic characterization is the integer feasibility
system

\[
\begin{aligned}
 &\sum_{g\in\Gamma_s}x_{c,g}=1
                         &&(c\in\mathscr C),\\
 &c_j\le
   \sum_{c,g:T\in\mathcal S(c,g)}x_{c,g}
   \le c_j+1
                         &&(j,\ T\in\mathcal T_j),\\
 &x_{c,g}\in\{0,1\}.                                  \tag{1.5}
\end{aligned}
\]

Replacing \(x_{c,g}\in\{0,1\}\) by \(x_{c,g}\ge0\) gives the fractional
intersection \(\mathcal P\cap\mathcal B\).

There is no automatic deterministic min-max theorem for (1.5): such a
theorem would assert an integrality property of this specific
multiple-choice shadow matrix. The cell decomposition gives no total
unimodularity because one choice carries an entire cross-depth target
tower.

## 2. Fractional floor/ceiling min-max

For \(\alpha\in\mathbb R^{\mathcal T}\), the support function of
\(\mathcal P\) is

\[
\boxed{
 h_{\mathcal P}(\alpha)
 =\sum_{c\in\mathscr C}
    \max_{g\in\Gamma_s}\langle\alpha,v_{c,g}\rangle.}   \tag{2.1}
\]

The minimum of \(\langle\alpha,b\rangle\) over \(\mathcal B_j\) is

\[
\boxed{
 \min_{b\in\mathcal B_j}\langle\alpha,b\rangle
 =c_j\sum_{T\in\mathcal T_j}\alpha_T
  +\sum_{i=1}^{R_j}\alpha^\uparrow_{j,i}.}              \tag{2.2}
\]

Indeed, after assigning \(c_j\) to every target, the remaining \(R_j\)
units go to the \(R_j\) smallest weights.

### Theorem 2.1 (balanced Hall separation)

The intersection \(\mathcal P\cap\mathcal B\) is nonempty if and only if
(0.8) holds for every real \(\alpha\).

#### Proof

If \(y\in\mathcal P\cap\mathcal B\), then

\[
                         h_{\mathcal P}(\alpha)
 \ge\langle\alpha,y\rangle
 \ge\min_{b\in\mathcal B}\langle\alpha,b\rangle,
\]

which is (0.8).

Conversely, if the compact convex sets \(\mathcal P,\mathcal B\) are
disjoint, strong separation gives a vector \(\alpha\) such that

\[
 \max_{y\in\mathcal P}\langle\alpha,y\rangle
 <\min_{b\in\mathcal B}\langle\alpha,b\rangle.
\]

Using (2.1)--(2.2) contradicts (0.8). \(\square\)

For prescribed lower capacities \(b_T\), rather than adaptive
floor/ceiling loads, the corresponding exact criterion is

\[
 \sum_Tb_T\alpha_T
 \le h_{\mathcal P}(\alpha)
 \qquad(\alpha_T\ge0).                                 \tag{2.3}
\]

This is the weighted Hall dual for covering every target to its prescribed
capacity. Upper capacities require signed weights, which is why (0.8)
uses arbitrary real \(\alpha\).

## 3. The all-shuffle physical barycenter

Fix a cell \(c\), a tagged rank \(j=(q,\epsilon)\), and a physical target
\(T\). By face separation there is at most one affine \(q\)-face
\(R_c(T)\subseteq c\) with physical trace \(T\).

The factor \(F_s\) selects \(2^s\) distinct affine \(q\)-faces. There are

\[
                         2^{s-q}\binom sq              \tag{3.1}
\]

affine \(q\)-faces in \(Q_s\), and the affine cube group \(\Gamma_s\) is
transitive on them. Therefore

\[
 {1\over|\Gamma_s|}
 \sum_{g\in\Gamma_s}{\bf1}_{\{T\in\mathcal S(c,g)\}}
 =
 \begin{cases}
  p_{s,q},&R_c(T)\text{ exists},\\
  0,&\text{otherwise}.
 \end{cases}                                           \tag{3.2}
\]

Average independently in every cell. The resulting load vector is

\[
                         \lambda_j(T)=p_{s,q}d_j(T),     \tag{3.3}
\]

proving (0.9). It belongs to \(\mathcal P\).

For any real \(\alpha\), maximum is at least average in every cell:

\[
\begin{aligned}
 h_{\mathcal P}(\alpha)
 &=\sum_c\max_g\langle\alpha,v_{c,g}\rangle\\
 &\ge\sum_c{1\over|\Gamma_s|}
       \sum_g\langle\alpha,v_{c,g}\rangle\\
 &=\langle\alpha,\lambda\rangle.                       \tag{3.4}
\end{aligned}
\]

This proves (0.10). No frame tags or macroprofile averaging occur in
(3.2)--(3.4); equal physical targets from different cells are aggregated
in \(d_j(T)\).

The total is correct:

\[
 \sum_T\lambda_j(T)
 =p_{s,q}\,G{\binom sq\over2^q}
 =G.                                                   \tag{3.5}
\]

## 4. Exact distance to balanced capacities

Fix one tagged rank and suppress \(j\). Let

\[
 c=\lfloor G/N\rfloor,\qquad R=G-cN,\qquad
 \sum_T\lambda_T=G.                                    \tag{4.1}
\]

Put

\[
 L=\sum_T(c-\lambda_T)_+,\qquad
 U=\sum_T(\lambda_T-c-1)_+.                            \tag{4.2}
\]

### Lemma 4.1

\[
                         \operatorname {dist}_1
                         (\lambda,\mathcal B)
 =2\max\{L,U\}.                                        \tag{4.3}
\]

#### Proof

Every point of \(\mathcal B\) must raise coordinates below \(c\) by total
at least \(L\) and lower coordinates above \(c+1\) by total at least
\(U\). These mandatory changes alter the total sum by \(L-U\). Restoring
the fixed total \(G\) requires an additional change of magnitude at least
\(|L-U|\) on coordinates inside the interval. Hence every correction has
\(\ell_1\)-cost at least

\[
                         L+U+|L-U|=2\max\{L,U\}.        \tag{4.4}
\]

Conversely perform the mandatory clipping. If \(L>U\), remove the remaining
\(L-U\) mass from coordinates still above \(c\); if \(U>L\), add the
remaining \(U-L\) mass to coordinates still below \(c+1\). The total-sum
identity guarantees enough such capacity. This attains (4.4). \(\square\)

Choose \(b^*\in\mathcal B\) attaining (4.3). If
\(\|\alpha\|_\infty\le1\), then (3.4) gives

\[
\begin{aligned}
 \min_{b\in\mathcal B}\langle\alpha,b\rangle
   -h_{\mathcal P}(\alpha)
 &\le\langle\alpha,b^*-\lambda\rangle\\
 &\le\|b^*-\lambda\|_1.
\end{aligned}                                         \tag{4.5}
\]

Summing over tagged ranks proves (0.13).

Thus the first exact attack on all weighted Hall cuts is the physical
candidate-load flatness statement (0.14), not a direction-support census.

## 5. Physical Gram reduction

For a tagged rank \(j=(q,\epsilon)\), define

\[
                         a_{c,T}={\bf1}_{\{T\in\mathcal A_j(c)\}}.
\tag{5.1}
\]

Then

\[
                         d_j(T)=\sum_ca_{c,T}.           \tag{5.2}
\]

The exact first moment is

\[
 \sum_Td_j(T)=G{\binom sq\over2^q}.                    \tag{5.3}
\]

For the second moment,

\[
\begin{aligned}
 \sum_Td_j(T)^2
 &=\sum_T\sum_{c,c'}a_{c,T}a_{c',T}\\
 &=\sum_{c,c'}|\mathcal A_j(c)\cap\mathcal A_j(c')|\\
 &=\sum_{c,c'}I_j(c,c').                               \tag{5.4}
\end{aligned}
\]

Subtracting the square of the mean proves (0.17).

Since \(\lambda_j=p_{s,q}d_j\) and
\(\overline\lambda_j=G/N_j\), Cauchy--Schwarz gives

\[
\begin{aligned}
 \|\lambda_j-(G/N_j){\bf1}\|_1
 &\le\sqrt{N_j}
       \|\lambda_j-(G/N_j){\bf1}\|_2\\
 &=p_{s,q}\sqrt{N_jV_j}.                               \tag{5.5}
\end{aligned}
\]

The constant vector \((G/N_j){\bf1}\) belongs to
\(\mathcal B_j\), so \(D_j\) is at most the left side of (5.5). This proves
(0.18)--(0.19).

Equation (0.17) is an untagged physical identity. The diagonal terms are

\[
 I_j(c,c)=|\mathcal A_j(c)|
 =2^{s-q}\binom sq,                                    \tag{5.6}
\]

while every off-diagonal term is the number of literally equal physical
targets in the two candidate face catalogues. Proving (0.19) is therefore
exactly a cross-cell physical overlap theorem.

There is an exact component formula for every off-diagonal term. Write one
physical cell as

\[
 c=\left(K_c;E^c_1,\ldots,E^c_s\right),                \tag{5.7}
\]

where \(K_c\) is its fixed core and the \(E^c_i\)'s are disjoint
two-element active coordinate pairs, disjoint from \(K_c\). Put

\[
                         U_c=K_c\cup\bigcup_iE^c_i.     \tag{5.8}
\]

Then a physical set \(T\) is a lower candidate trace of depth \(q\) in
\(c\) if and only if

\[
\boxed{
 \begin{aligned}
 &K_c\subseteq T\subseteq U_c,\\
 &|T\cap E^c_i|\in\{0,1\}\quad(i\in[s]),\\
 &\#\{i:T\cap E^c_i=\varnothing\}=q.
 \end{aligned}}                                        \tag{5.9}
\]

It is an upper candidate trace if and only if

\[
\boxed{
 \begin{aligned}
 &K_c\subseteq T\subseteq U_c,\\
 &|T\cap E^c_i|\in\{1,2\}\quad(i\in[s]),\\
 &\#\{i:E^c_i\subseteq T\}=q.
 \end{aligned}}                                        \tag{5.10}
\]

These are physical set identities, with no frame tag retained.

### Lemma 5.1 (matching-union coefficient formula)

For two cells \(c,c'\), the overlap
\(I^\epsilon_q(c,c')\) is the coefficient of \(x^qy^q\) in a product of
polynomials indexed by the path and even-cycle components of the
degree-two multigraph

\[
                         \mathcal M(c,c')
 =\{E^c_i:i\in[s]\}\cup\{E^{c'}_i:i\in[s]\}.            \tag{5.11}
\]

More precisely, first impose the core pins
\(K_c\cup K_{c'}\subseteq T\) and the support restrictions
\(T\subseteq U_c\cap U_{c'}\). If these are inconsistent, the overlap is
zero. Otherwise, for a component \(Q\) of (5.11), define

\[
 P_Q^-(x,y)
 =\sum_{A\subseteq V(Q)}
   {\bf1}_{\{A\text{ satisfies both lower systems on }Q\}}
   x^{z_c(A)}y^{z_{c'}(A)},                            \tag{5.12}
\]

where \(z_c(A)\) and \(z_{c'}(A)\) count empty edges of the two matchings.
Define \(P_Q^+(x,y)\) analogously, with exponents counting full edges.
Then

\[
\boxed{
 I_q^\epsilon(c,c')
 =[x^qy^q]\prod_{Q\in\operatorname {comp}\mathcal M(c,c')}
                         P_Q^\epsilon(x,y).}           \tag{5.13}
\]

#### Proof

Conditions (5.9) and (5.10) are edge-local after the fixed core pins and
support exclusions are imposed. The union of two matchings has maximum
degree two, hence decomposes into paths, even cycles, doubled edges, and
isolated pinned vertices. Choices of \(T\) on different components are
independent, while the exponents add the two touched-edge counts.
Multiplication followed by extraction of \(x^qy^q\) proves (5.13).
\(\square\)

Thus (9.1) can be attacked by a transfer-matrix enumeration on alternating
paths and cycles, followed by summation over the canonical exterior cores.
No sectorwise quota or Gaussian type replacement is needed.

## 6. Indicator cuts and an invariant obstruction

Although all real weights are required in (0.8), indicator weights expose
the underlying physical Hall cuts.

Fix one tagged rank \(j\) and \(A\subseteq\mathcal T_j\). From (2.2),

\[
 \min_{b\in\mathcal B_j}b(A)
 =c_j|A|+\max\{0,R_j-(N_j-|A|)\}.                      \tag{6.1}
\]

Thus a necessary fractional cut is

\[
\boxed{
 c_j|A|+\max\{0,R_j-N_j+|A|\}
 \le
 \sum_{c\in\mathscr C}
   \max_{g\in\Gamma_s}
      |\mathcal S_j(c,g)\cap A|.}                      \tag{6.2}
\]

Let

\[
                         f_c(A)=|\mathcal A_j(c)\cap A|.             \tag{6.3}
\]

Every factor selects only \(2^s\) faces at rank \(j\), so

\[
 \max_g|\mathcal S_j(c,g)\cap A|
 \le\min\{2^s,f_c(A)\}.                                \tag{6.4}
\]

Consequently

\[
\boxed{
 c_j|A|+\max\{0,R_j-N_j+|A|\}
 >
 \sum_c\min\{2^s,f_c(A)\}}                             \tag{6.5}
\]

is an invariant obstruction: no all-shuffle orders, translations, or
discrepancy rounding can satisfy the floor/ceiling capacities.

Conversely, averaging the all-shuffle menu gives

\[
\begin{aligned}
 \sum_c\max_g|\mathcal S_j(c,g)\cap A|
 &\ge p_{s,q}\sum_cf_c(A)\\
 &=\sum_{T\in A}\lambda_j(T).                          \tag{6.6}
\end{aligned}
\]

Thus candidate-load flatness controls every indicator cut, while (0.13)
shows that its \(\ell_1\) version controls every weighted cut.

The known macroprofile flow theorem does not evaluate either side of
(6.2) for a physical set \(A\). Two targets with the same macroprofile may
have disjoint candidate-cell neighborhoods. Hence (6.2) cannot be replaced
by a sectorwise quota.

## 7. What the context-dependent order array contributes

The context-dependent array permits the conjugate \(g_c\) to depend on the
full product-cell label. This justifies the product of independent cell
menus in (0.6); there is no owner coupling between distinct cells.

The all-shuffle hierarchy realizes every coordinate permutation, so the
average (3.2) is exactly uniform over affine faces. It also implies that
every candidate face can be forced by some cell order. Therefore the
singleton version of (6.2) is exactly the candidate-capacity condition

\[
                         d_j(T)\ge c_j.                 \tag{7.1a}
\]

At the shallow unit-quota ranks this reduces to \(d_j(T)>0\); at deeper
ranks the distinction is essential.

What the array does not do is flatten \(d_j(T)\). Candidate cells are fixed
by the physical packet embeddings and cell cores before any order is
chosen. Hence:

\[
\boxed{\text{all-shuffle controls the support function inside each
cell; the outer candidate Gram (0.17) controls physical flatness.}} \tag{7.1}
\]

This is why a balanced macro-order census, although exact, does not prove
(0.8).

## 8. Integrality and discrepancy

The equality

\[
 \mathcal P=
 \operatorname {conv}
 \left\{\sum_cv_{c,g_c}:g_c\in\Gamma_s\right\}          \tag{8.1}
\]

follows by distributing products in the Minkowski sum. Thus every point of
\(\mathcal P\) is a probability mixture of deterministic order fields.

Nevertheless,

\[
                         \mathcal P\cap\mathcal B\ne\varnothing           \tag{8.2}
\]

does not imply that one deterministic load vector belongs to
\(\mathcal B\). Such an implication would be an integrality theorem for
the multiple-choice tower matrix in (1.5). No total-unimodularity or
matroid-base representation has been proved.

Independent rounding of the all-shuffle barycenter cannot suffice at
shallow ranks: its mean target load is \(G/N_j=1+o(1)\), so a constant
fraction of targets are missed even when the candidate degrees are
perfectly flat. Standard signed discrepancy bounds are also too weak:
an additive error of one at a positive fraction of unit-quota targets is
\(\Theta(W)\).

The precise remaining rounding assertion is:

> If (0.8) has \(o(W)\) slack loss uniformly for all
> \(\|\alpha\|_\infty\le1\), choose one \(g_c\) per cell so that the
> aggregate distance of the resulting loads from
> \(\prod_j\mathcal B_j\) is \(o(W)\).

This is a one-sided, multiple-choice, cross-depth discrepancy theorem for
resolvable shadow towers. It is strictly stronger than marginal
discrepancy and strictly weaker than exact target-by-target equality.

## 9. Exact next lemma

The all-shuffle Hall attack has reduced the fractional constant-one gate
to the physical candidate-overlap statement

\[
 \boxed{
 \sum_{q\le H}\sum_{\epsilon=\pm}
 {2^q\over\binom sq}
 \sqrt{
 N^\epsilon_q
 \left[
  \sum_{c,c'}I^\epsilon_q(c,c')
  -{G^2\over N^\epsilon_q}
      \left({\binom sq\over2^q}\right)^2
 \right]
 }=o(W).}                                               \tag{9.1}
\]

Every term is explicit:

* \(c,c'\) are canonical physical product cells;
* \(I^\epsilon_q(c,c')\) counts literally equal lower or upper target
  traces among all affine \(q\)-faces of the two cells;
* no order, frame tag, or sector projection remains.

A proof of (9.1) controls every fractional Hall weight up to \(o(W)\).
A violation yields a genuine physical candidate-collision variance and
identifies where an indicator or higher weighted cut must be sought.
After (9.1), only the specialized integral tower rounding assertion of
Section 8 remains.
