# The full sixteen-state conjugacy library of the new `D_4` port factor

Date: 2026-07-26

Method: pure mathematics.  All finite tables are obtained by literal
substitution in the path words of
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md`.  The contravariant
symmetry is the exact one proved in
`MATH_THEOREM_CHUNG_FELLER_AUTOMORPHISM_AND_PENTAGON_ESCAPE_20260726.md`,
Section 3.  No search or computation is used.

## 0. Verdict

Put

\[
 \alpha=(2\ 3),\qquad \beta=(4\ 5),\qquad \gamma=(6\ 7),
 \qquad H=\langle\alpha,\beta,\gamma\rangle\cong C_2^3,       \tag{0.1}
\]

let `R(i)=9-i`, and let `omega=CR` act on four-subsets, where `C` is
complementation in `[8]`.  The exact port symmetry group is

\[
 \Gamma=H\rtimes\langle\omega\rangle,
 \qquad \omega\alpha\omega=\gamma,
 \quad \omega\beta\omega=\beta.                         \tag{0.2}
\]

The `H` coset acts covariantly.  The second coset has the contravariant
physical realization

\[
              \widetilde X_t=R(X_{4-t}).                  \tag{0.3}
\]

It is essential that (0.3) uses coordinate reversal `R`, not
complementation.  It preserves both exact ledgers and has new root

\[
              \widetilde X_0=R(P^c)=\omega P\in D_4.       \tag{0.4}
\]

Thus the conjugacy orbit of the new factor `G` contains sixteen valid
`D_4`-ported factors.  Their first-insertion supports are:

\[
\begin{array}{c|c}
P&\{\theta_g(P):g\in\Gamma\}\\ \hline
1234&\{8\}\\
1235&\{8\}\\
1236&\{4,5,7,8\}\\
1237&\{4,5,6,8\}\\
1245&\{3,6,7,8\}\\
1246&\{3,5,7,8\}\\
1247&\{3,5,6,8\}\\
1256&\{3,4,7,8\}\\
1257&\{3,4,6,8\}\\
1345&\{2,6,7,8\}\\
1346&\{2,5,7,8\}\\
1347&\{2,5,6,8\}\\
1356&\{2,4,7,8\}\\
1357&\{2,4,6,8\}.
\end{array}                                               \tag{0.5}
\]

Consequently exactly the two primitive roots `1234,1235` are frozen; at
both, every valid conjugate inserts coordinate `8`.  Each of the other
twelve roots has exactly four labels.  This is a sharper answer than the
`H`-only calculation, in which the four port-occupancy strata have support
sizes `1,2,3,4`.

The positive conclusion is only a support theorem.  One factor choice is
one of sixteen globally correlated transition matrices, not an independent
choice from each row of (0.5).  Moreover the contravariant coset reflects
every collar offset.  Therefore this library supplies four marked states
at a nonfrozen boundary, but it does not supply four states at **every**
boundary and does not by itself supply eight independently selectable
joint cells.

## 1. Root action and stabilizers

The `H`-orbits are

\[
\begin{aligned}
 {\cal O}_{210}&=\{1234,1235\},\\
 {\cal O}_{201}&=\{1236,1237\},\\
 {\cal O}_{120}&=\{1245,1345\},\\
 {\cal O}_{111}&=\{1246,1247,1256,1257,
                    1346,1347,1356,1357\}.             \tag{1.1}
\end{aligned}
\]

The subscript records occupancy in `{2,3},{4,5},{6,7}`.  The `H` point
stabilizers are

\[
 H_P=\begin{cases}
 \langle\alpha,\gamma\rangle,&P\in{\cal O}_{210},\\
 \langle\alpha,\beta\rangle,&P\in{\cal O}_{201},\\
 \langle\beta,\gamma\rangle,&P\in{\cal O}_{120},\\
 \{1\},&P\in{\cal O}_{111}.
 \end{cases}                                             \tag{1.2}
\]

Direct reverse-complement gives

\[
\begin{gathered}
 \omega(1234)=1234,\quad\omega(1235)=1235,\\
 1236\leftrightarrow1245,\quad
 1237\leftrightarrow1345,\quad
 1247\leftrightarrow1346,\quad
 1257\leftrightarrow1356,\\
 \omega(1246)=1246,\quad\omega(1256)=1256,\quad
 \omega(1347)=1347,\quad\omega(1357)=1357.            \tag{1.3}
\end{gathered}
\]

Hence the `Gamma` root orbits have sizes `2,4,8`:

\[
 {\cal O}_{210},\qquad
 {\cal O}_{201}\cup{\cal O}_{120},\qquad
 {\cal O}_{111}.                                        \tag{1.4}
\]

Their point stabilizer sizes are respectively `8,4,2`.  More explicitly,

\[
 \Gamma_P=\begin{cases}
 \langle\alpha,\gamma,\omega\rangle,
     &P=1234,1235,\\
 \langle\alpha,\beta\rangle,&P=1236,1237,\\
 \langle\beta,\gamma\rangle,&P=1245,1345,\\
 \langle\omega\rangle,&P=1246,1256,1347,1357,\\
 \langle\alpha\gamma\omega\rangle,
     &P=1247,1257,1346,1356.
 \end{cases}                                             \tag{1.5}
\]

For example, `omega(1247)=1346` and `alpha gamma` sends `1346` back to
`1247`, proving the last line.  All other lines follow immediately from
(1.2)--(1.3).

## 2. Exactness and first insertion in the contravariant coset

For an original row write

\[
 X_t=(P\setminus\{a_1,\ldots,a_t\})
       \cup\{b_1,\ldots,b_t\},
 \qquad Y_t=X_t\cup X_{t+1}.                            \tag{2.1}
\]

Under (0.3),

\[
 \widetilde Y_t
 =R(X_{4-t})\cup R(X_{3-t})
 =R(Y_{3-t}).                                            \tag{2.2}
\]

Since `R` is a bijection, the transformed `X` entries enumerate every
four-set once and the transformed `Y` entries enumerate every five-set
once.  Thus (0.3) is an exact factor.  Its first transition is

\[
 R(X_4)\longrightarrow R(X_3),                          \tag{2.3}
\]

which deletes `R(b_4)` and inserts `R(a_4)`.  If the new root is denoted
`Q=omega P`, its first-insertion function is therefore

\[
                \psi(Q)=R\bigl(a_4(\omega Q)\bigr).     \tag{2.4}
\]

From the word table of `G`,

\[
\begin{array}{c|rrrrrrrrrrrrrr}
P&1234&1235&1236&1237&1245&1246&1247&1256&1257&1345&
1346&1347&1356&1357\\ \hline
a_4(P)&1&1&6&1&5&2&2&6&5&5&1&1&6&5,
\end{array}                                             \tag{2.5}
\]

and hence

\[
\begin{array}{c|rrrrrrrrrrrrrr}
Q&1234&1235&1236&1237&1245&1246&1247&1256&1257&1345&
1346&1347&1356&1357\\ \hline
\psi(Q)&8&8&4&4&3&7&8&3&3&8&7&8&4&4.
\end{array}                                             \tag{2.6}
\]

This proves the base target map in the second coset.

## 3. The sixteen root-target transition matrices

For `h in H`, reindexing each conjugate back to the fixed root set gives

\[
 \theta_h(P)=h\theta_G(hP),
 \qquad
 \theta_{h\Omega}(P)=h\psi(hP),                         \tag{3.1}
\]

where `Omega` denotes the physical operation (0.3).  Order `H` as

\[
 1,\alpha,\beta,\gamma,\alpha\beta,\alpha\gamma,
 \beta\gamma,\alpha\beta\gamma.                        \tag{3.2}
\]

The covariant half is

\[
\begin{array}{c|rrrrrrrr}
P&1&\alpha&\beta&\gamma&\alpha\beta&\alpha\gamma&
       \beta\gamma&\alpha\beta\gamma\\ \hline
1234&8&8&8&8&8&8&8&8\\
1235&8&8&8&8&8&8&8&8\\
1236&7&7&7&8&7&8&8&8\\
1237&8&8&8&6&8&6&6&6\\
1245&3&6&3&3&6&7&3&7\\
1246&3&8&7&3&3&8&3&5\\
1247&3&8&3&3&5&8&6&3\\
1256&7&3&3&3&8&4&3&8\\
1257&3&4&3&6&8&3&3&8\\
1345&6&2&6&7&2&2&7&2\\
1346&8&2&2&8&7&2&5&2\\
1347&8&2&5&8&2&2&2&6\\
1356&2&7&8&4&2&2&8&2\\
1357&4&2&8&2&2&6&8&2.
\end{array}                                             \tag{3.3}
\]

The contravariant half, in the same column order, is

\[
\begin{array}{c|rrrrrrrr}
P&\Omega&\alpha\Omega&\beta\Omega&\gamma\Omega&
 \alpha\beta\Omega&\alpha\gamma\Omega&
 \beta\gamma\Omega&\alpha\beta\gamma\Omega\\ \hline
1234&8&8&8&8&8&8&8&8\\
1235&8&8&8&8&8&8&8&8\\
1236&4&4&5&4&5&4&5&5\\
1237&4&4&5&4&5&4&5&5\\
1245&3&8&3&3&8&8&3&8\\
1246&7&7&3&8&5&8&3&5\\
1247&8&8&3&6&5&6&3&5\\
1256&3&4&7&3&7&4&8&8\\
1257&3&4&8&3&8&4&6&6\\
1345&8&2&8&8&2&2&8&2\\
1346&7&7&5&8&2&8&5&2\\
1347&8&8&5&6&2&6&5&2\\
1356&4&2&7&4&7&2&8&8\\
1357&4&2&8&4&8&2&6&6.
\end{array}                                             \tag{3.4}
\]

For audit, the sixteen-column multisets are

\[
\begin{array}{c|l}
P&\{\!\{\theta_g(P):g\in\Gamma\}\!\}\\ \hline
1234&8^{16}\\
1235&8^{16}\\
1236&4^4,5^4,7^4,8^4\\
1237&4^4,5^4,6^4,8^4\\
1245&3^8,6^2,7^2,8^4\\
1246&3^6,5^3,7^3,8^4\\
1247&3^6,5^3,6^3,8^4\\
1256&3^6,4^3,7^3,8^4\\
1257&3^6,4^3,6^3,8^4\\
1345&2^8,6^2,7^2,8^4\\
1346&2^6,5^3,7^3,8^4\\
1347&2^6,5^3,6^3,8^4\\
1356&2^6,4^3,7^3,8^4\\
1357&2^6,4^3,6^3,8^4.
\end{array}                                             \tag{3.5}
\]

Tables (3.3)--(3.5) prove (0.5) and every claimed multiplicity.

## 4. The exact factor-level target polytope

Define the root-target incidence matrix

\[
 T_g(P,x)={\bf1}_{\{x=\theta_g(P)\}},
 \qquad g\in\Gamma.                                    \tag{4.1}
\]

The full transition polytope is exactly

\[
 \boxed{{\cal T}_G=\operatorname {conv}
          \{T_g:g\in\Gamma\}.}                         \tag{4.2}
\]

The sixteen displayed matrices are distinct.  Indeed, the `H` orbit is
already distinguished by its three within-pair orientations, while the
two cosets have different pair-total vectors.  Hence the factor stabilizer
inside `Gamma` is trivial.  Moreover every displayed zero-one matrix is a
vertex: if it were a nontrivial convex combination of the others, every
coordinate at which it is zero would force all matrices in the combination
to be zero there, and every coordinate at which it is one would force all
of them to be one there.  They would therefore be identical.  Thus (4.2)
has exactly the sixteen displayed vertices and is not the product of the
fourteen supports in (0.5).

The target-count histogram of `G` is

\[
 n^+=e_2+4e_3+e_4+e_6+2e_7+5e_8.                     \tag{4.3}
\]

Its `H`-orbit convex hull is

\[
\begin{gathered}
 n_1=0,\quad n_8=5,\quad n_2+n_3=5,\quad
 n_4+n_5=1,\quad n_6+n_7=3,\\
 1\le n_2\le4,qquad0\le n_4\le1,qquad1\le n_6\le2.
                                                               \tag{4.4}
\end{gathered}
\]

The contravariant base histogram is

\[
 n^\Omega=3e_3+4e_4+2e_7+5e_8,                       \tag{4.5}
\]

and its `H`-orbit convex hull is

\[
\begin{gathered}
 n_1=0,\quad n_8=5,\quad n_2+n_3=3,\quad
 n_4+n_5=4,\quad n_6+n_7=2,\\
 0\le n_2\le3,qquad0\le n_4\le4,qquad0\le n_6\le2.
                                                               \tag{4.6}
\end{gathered}
\]

Therefore the target-count projection of (4.2) has the following exact
parametrization.  For some `0<=lambda<=1`,

\[
\boxed{
\begin{gathered}
 n_1=0,\qquad n_8=5,\\
 n_2+n_3=3+2\lambda,qquad
 n_4+n_5=4-3\lambda,qquad
 n_6+n_7=2+\lambda,\\
 \lambda\le n_2\le3+\lambda,qquad
 0\le n_4\le4-3\lambda,qquad
 \lambda\le n_6\le2.
\end{gathered}}                                        \tag{4.7}
\]

To prove the interval bounds, write a point as
`lambda x^+ +(1-lambda)x^Omega` with `x^+` in (4.4) and
`x^Omega` in (4.6).  Minkowski addition of the three independent pair
intervals gives exactly (4.7), and every value in those intervals is
attained.  This proves both necessity and sufficiency.

## 5. Complete collar action

Let

\[
 q(P)=(a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,9),             \tag{5.1}
\]

and, with cyclic indices modulo nine, define

\[
 I_{\ell,j}(q)=\{q_j,q_{j+1},\ldots,q_{j+\ell-1}\},
 \qquad
 U_{\ell,j;P}=e_{I_{\ell,j}(q(P))},
 \qquad
 U_{\ell,j}=\sum_{P\in D_4}U_{\ell,j;P}.               \tag{5.2}
\]

The word of the transformed row rooted at `omega P` is

\[
 q^\Omega(\omega P)=
 (R(b_4),R(b_3),R(b_2),R(b_1),
  R(a_4),R(a_3),R(a_2),R(a_1),9).                       \tag{5.3}
\]

Thus the two cosets act root by root according to

\[
 \boxed{
 U_{\ell,j;P}^{h}=h_*U_{\ell,j;hP},
 \qquad
 U_{\ell,j;P}^{h\Omega}
       =h_*R_*U_{\ell,\,8-j-\ell;\,\omega hP}.}         \tag{5.4}
\]

After summing over all roots, this becomes

\[
 \boxed{
 U_{\ell,j}^{h}=h_*U_{\ell,j},
 \qquad
 U_{\ell,j}^{h\Omega}
       =h_*R_*U_{\ell,\,8-j-\ell}.}                    \tag{5.5}
\]

The index in the second formula is modulo nine.  It follows because the
reflection `rho(j)=7-j` sends a length-`ell` interval starting at `j` to
the forward interval starting at `8-j-ell`.

For a fixed exterior carrier `O` and local embedding `iota`, one pushes
(5.4)--(5.5) through

\[
                         S\longmapsto O\cup\iota(S).    \tag{5.6}
\]

This is the full collar statement.  The extra four root labels in (0.5)
are legal at the same `D_4` port set, but a choice from the second coset
simultaneously reflects every local collar and relabels it by `R`.  Hence
the marked target choices cannot be detached from their seven companion
cells.

## 6. The naive reversal collision remains only a warning

The incorrect anchored operation

\[
                  \widehat X_t=[8]\setminus X_{4-t}    \tag{6.1}
\]

would insert `b_4` first.  It is not (0.3), and it is not exact.  Indeed,
in two rows of `G`,

\[
 1238\cap1368=138,
 \qquad
 1358\cap1378=138.                                     \tag{6.2}
\]

Under (6.1), both edges acquire adjacent union

\[
                         [8]\setminus138=24567,         \tag{6.3}
\]

so the upper ledger repeats.  This collision excludes only the naive
statewise complement-reversal.  It does not affect the exact
reverse-and-reflect operation (0.3), whose union identity is (2.2).

## 7. Exact finite boundary

### Theorem 7.1 (the `D_4`-ported Haar support gate)

The full symmetry library `Gamma` of the new factor has sixteen valid,
port-preserving states.  At each of the twelve roots other than
`1234,1235`, their first-insertion targets have support exactly four.  At
`1234,1235`, the support is the singleton `{8}`.  All root choices are
globally coupled by one of the sixteen matrices (3.3)--(3.4), and the
complete collar transforms according to (5.4).

Consequently a root-scale construction whose charged occurrences avoid
the two frozen roots obtains the requested four-state marked support from
this library.  A construction quantified over every charged root does
not: the frozen orbit is an exact support/ownership obstruction.  Even on
the twelve nonfrozen roots, an eight-joint-cell conclusion requires a
separate joined-collar argument; it does not follow from the four marked
labels alone.

#### Proof

Exactness of all sixteen factors is Section 2.  The root support and
factor correlations are Sections 3--4.  The collar formula is Section 5.
These statements prove every assertion. \(\square\)

The next exact finite question is therefore whether the charged root
measure can be routed away from `{1234,1235}` while respecting the
sixteen-matrix correlations and the reflected collar, or whether a second
non-symmetry `D_4` factor can unfreeze this primitive orbit.
