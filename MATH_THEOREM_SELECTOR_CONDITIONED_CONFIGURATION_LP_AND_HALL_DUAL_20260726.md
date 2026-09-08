# Selector-conditioned configuration LP and the exact all-depth Hall dual

Date: 2026-07-26

Method: pure mathematics only.  No computation, random rounding, generic
nibble, solver, or web input is used.

## 0. Status

This note formulates the selector-conditioned problem exactly, including
both signs, every protected depth, and every floor/ceiling quota reset.
It also identifies precisely what the rank-twisted compatibility kernel
does and does not prove.

The main conclusions are:

1. The selection problem is a **multiple-choice configuration problem**,
   not an ordinary bipartite matching.  Choosing one active \(r\)-set and
   compiler label commits an entire selector fibre simultaneously.
2. Its fractional feasibility has an exact weighted Hall/Farkas dual,
   stated in Theorem 3.1 below.  The floor/ceiling resets contribute the
   support function of a hypersimplex; replacing them by uniform real
   loads gives the wrong dual.
3. Complete affine batching converts the exact rank-twisted candidate
   kernel into exact first marginals:

   \[
   \sum_{\omega\in\Omega_f}
       a_{f,\omega}^{-,q}(T)
     =\mu_{f,q}d_f^-(T),\qquad
   \sum_{\omega\in\Omega_f}
       a_{f,\omega}^{+,q}(U)
     =\mu_{f,q}d_f^+(U),                              \tag{0.1}
   \]

   where \(d_f^\pm\) are literal compatible-source counts and

   \[
      \mu_{f,q}
       =\binom{n_f-q}{r-q}2^r q!(r-q)!.              \tag{0.2}
   \]

   This is exact, but it is only an average over the options of one
   fibre.
4. The integral problem is the intersection of a Minkowski sum of
   finite configuration sets with a product of integer hypersimplices.
   The weighted Hall inequalities characterize the convex relaxation,
   not this semigroup intersection.
5. Neither an integral construction nor an \(\Omega(W)\) physical-target
   Hall cut follows from the currently proved identities.  In
   particular, the selector decoder gives a linear discrepancy from the
   *uniform conditional fractional marginal*, but quota resets allow
   conditional zero/one loads and prevent that discrepancy from being a
   physical Hall certificate.

Thus the requested coefficient-one dichotomy is not closed here.  The
exact missing assertion is now smaller: prove the integer decomposition
property for the configuration polytope below, or exhibit one dual weight
whose gap is \(\Omega(W)\).  Claiming either from complete-design
marginals would be unsupported.

## 1. Configuration incidence

Let \(\mathfrak F\) be the family of retained selector fibres over all
rank-twisted product status cells.  A fibre \(f\) has owner set \(V_f\)
and option library

\[
 \Omega_f=\binom{[n_f]}r\times
   (\mathbb F_2^r\rtimes\mathfrak S_r).              \tag{1.1}
\]

An option \(\omega=(A,g)\) partitions \(V_f\) into parallel physical
\(Q_r\) packets with active set \(A\) and installs the conjugated
compiler \(g\) on every packet.  Put

\[
 \mathcal C=\{(\sigma,q):\sigma\in\{-,+\},\
                         1\le q\le H\}.              \tag{1.2}
\]

For \(c=(\sigma,q)\), a literal target \(T\) in the appropriate signed
rank layer, and one option, define

\[
 a_{f,\omega}^{c}(T)
  =|\{x\in V_f:\text{the depth-\(q\) target from start \(x\)
                     under \(\omega\) is \(T\)}\}|.  \tag{1.3}
\]

Trace recovery inside a product cell gives

\[
                         a_{f,\omega}^{c}(T)\in\{0,1\}. \tag{1.4}
\]

For every \(f,\omega,c\),

\[
                         \sum_Ta_{f,\omega}^{c}(T)=|V_f|. \tag{1.5}
\]

Let

\[
                         W_0=\sum_{f\in\mathfrak F}|V_f|             \tag{1.6}
\]

be the retained owner mass.  The discarded owner mass is
\(o(W/H)\), so replacing \(W_0\) by \(W\) changes only the permitted
literal repair ledger.

The binary choice variables are

\[
 x_{f,\omega}\in\{0,1\},\qquad
 \sum_{\omega\in\Omega_f}x_{f,\omega}=1.             \tag{1.7}
\]

The resulting target load is

\[
 L_c(T)=\sum_{f,\omega}
               a_{f,\omega}^{c}(T)x_{f,\omega}.      \tag{1.8}
\]

This is not a bipartite \(b\)-matching: one variable in (1.7) inserts
the whole vector
\((a_{f,\omega}^{c}(T))_{c,T}\), simultaneously for all owners, signs,
and depths.

## 2. Exact quota resets

Let

\[
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q},\qquad
 h_q=\left\lfloor{W_0\over N_q}\right\rfloor,\qquad
 R_q=W_0-h_qN_q.                                    \tag{2.1}
\]

For either sign, exact balance at depth \(q\) means

\[
 L_{\sigma,q}(T)=h_q+y_{\sigma,q}(T),\qquad
 y_{\sigma,q}(T)\in\{0,1\},\qquad
 \sum_Ty_{\sigma,q}(T)=R_q.                          \tag{2.2}
\]

Thus the complete integer system is (1.7), (1.8), and (2.2).  Both
signs and all depths use the same \(x\)-variables.

Let \(\mathcal B_{\mathbb Z}\) be the set of all integer vectors
satisfying (2.2), and let \(\mathcal B=\operatorname{conv}
\mathcal B_{\mathbb Z}\).  For one colour \(c=(\sigma,q)\),

\[
 \mathcal B_c
  =\{b\in[h_q,h_q+1]^{N_q}:\sum_Tb(T)=W_0\}.         \tag{2.3}
\]

This is a translated hypersimplex.  If
\(\lambda_c(T)\in\mathbb R\), its support function is

\[
 h_{\mathcal B_c}(\lambda_c)
  =h_q\sum_T\lambda_c(T)
    +\sum_{\text{\(R_q\) largest }\lambda_c(T)}
                         \lambda_c(T).               \tag{2.4}
\]

Formula (2.4) is the exact contribution of the quota reset.

## 3. The weighted Hall/Farkas dual

For a fibre put

\[
 \mathcal A_f
   =\{a_{f,\omega}:\omega\in\Omega_f\},              \tag{3.1}
\]

where a configuration vector includes every coordinate \((c,T)\).
The fractional configuration polytope is

\[
 \mathcal P=\sum_{f\in\mathfrak F}
                      \operatorname{conv}\mathcal A_f,             \tag{3.2}
\]

a Minkowski sum.

### Theorem 3.1 (exact fractional dual)

The relaxed system

\[
 x_{f,\omega}\ge0,\qquad
 \sum_\omega x_{f,\omega}=1,\qquad
 (L_c(T))_{c,T}\in\mathcal B                         \tag{3.3}
\]

is feasible if and only if, for every real target-weight array
\(\lambda=(\lambda_c(T))\),

\[
 \boxed{
 \sum_{f\in\mathfrak F}
       \min_{\omega\in\Omega_f}
          \sum_{c,T}\lambda_c(T)a_{f,\omega}^{c}(T)
 \ \le\
 \sum_{c\in\mathcal C}
 \left[
   h_q\sum_T\lambda_c(T)
   +\sum_{\text{\(R_q\) largest }\lambda_c(T)}
                    \lambda_c(T)
 \right].}                                           \tag{3.4}
\]

#### Proof

System (3.3) is feasible exactly when
\(\mathcal P\cap\mathcal B\ne\varnothing\).  Two disjoint compact convex
sets are strictly separated by a real linear functional.  The minimum
of that functional on the Minkowski sum (3.2) is the sum of its minima
on the individual configuration polytopes.  Its maximum on
\(\mathcal B=\prod_c\mathcal B_c\) is the sum of (2.4).  Therefore
failure of (3.4) is equivalent to strict separation, and absence of a
failure is equivalent to intersection. \(\square\)

Taking negative indicator weights gives a familiar subset cut.  For
target families \(Y_c\) in any collection of colours, every fractional
or integral solution must satisfy

\[
 \boxed{
 \sum_f\max_{\omega\in\Omega_f}
             \sum_c a_{f,\omega}^{c}(Y_c)
 \ge
 \sum_c\left[
 h_q|Y_c|+
 \bigl(R_q-(N_q-|Y_c|)\bigr)_+
 \right],}                                           \tag{3.5}
\]

where

\[
 a_{f,\omega}^{c}(Y_c)=
                  \sum_{T\in Y_c}a_{f,\omega}^{c}(T). \tag{3.6}
\]

The maximum in (3.5) is joint across all selected colours.  It cannot be
replaced by a separate maximum for each sign or depth.

Positive indicator weights give the dual upper-capacity inequality

\[
 \sum_f\min_{\omega\in\Omega_f}
             \sum_c a_{f,\omega}^{c}(Y_c)
 \le
 \sum_c\left[
 h_q|Y_c|+\min(R_q,|Y_c|)
 \right].                                            \tag{3.7}
\]

Subset inequalities (3.5)--(3.7) are necessary but not sufficient for
(3.3); arbitrary real weights in (3.4) are required.

## 4. Exact insertion of the rank-twisted kernel

Fix a fibre \(f\) with \(n_f\) nonselector singleton axes.  For a lower
target \(T\), let \(d_f^-(T)\) be the number of sources \(x\in V_f\)
such that \(T\) is obtained by deleting \(q\) intrinsic singleton axes
of \(x\).  In macroblock notation it is the restriction to \(V_f\) of

\[
 [z^q]\prod_j
 \left(\sum_{\ell=0}^d
  2^\ell\binom{e_{t_j+\ell}(T_j)}{\ell}z^\ell\right). \tag{4.1}
\]

Define \(d_f^+(U)\) by the corresponding full-edge coefficient

\[
 [z^q]\prod_j
 \left(\sum_{\ell=0}^d
  2^\ell\binom{f_{u_j-\ell}(U_j)}{\ell}z^\ell\right). \tag{4.2}
\]

### Lemma 4.1 (exact option-average identity)

For every literal target in fibre range and every \(q<r\),

\[
\begin{aligned}
 \sum_{\omega\in\Omega_f}a_{f,\omega}^{-,q}(T)
      &=\mu_{f,q}d_f^-(T),\\
 \sum_{\omega\in\Omega_f}a_{f,\omega}^{+,q}(U)
      &=\mu_{f,q}d_f^+(U),
\end{aligned}                                       \tag{4.3}
\]

with \(\mu_{f,q}\) given by (0.2).

#### Proof

Fix one compatible source-target pair.  Its physical start \(x\), its
\(q\) used axes, and its deleted or inserted endpoints are determined.
An active \(r\)-set contains those axes in
\(\binom{n_f-q}{r-q}\) ways.  For a fixed active set, choose a base
start \(x'\) of the un-conjugated compiler in \(2^r\) ways.  There are
\(q!\) possible orders taking its \(q\)-support to the prescribed
unordered physical support and \((r-q)!\) extensions to a full
coordinate permutation.  Once \(x'\), the permutation, and the physical
start \(x\) are fixed, the affine translation is forced.  Hence the pair
occurs in exactly

\[
 \binom{n_f-q}{r-q}2^rq!(r-q)!
\]

options.  Summing over the \(d_f^\pm\) compatible sources proves
(4.3). \(\square\)

Since

\[
 { \mu_{f,q}\over|\Omega_f|}
 ={\binom{n_f-q}{r-q}2^rq!(r-q)!\over
        \binom{n_f}r2^rr!}
 ={1\over\binom{n_f}q},                              \tag{4.4}
\]

the uniform fractional option sends each compatible source-target pair
with exact weight \(1/\binom{n_f}q\).  This identity is independent of
\(r\); it is the precise fractional deletion kernel implemented by the
complete active-set/affine library.

Equation (4.3) is the strongest consequence of complete affine batching
available without selecting one option.  For a target-weight array,
Theorem 3.1 needs

\[
 \min_\omega\sum_{c,T}
       \lambda_c(T)a_{f,\omega}^{c}(T),              \tag{4.5}
\]

whereas (4.3) determines only the average of (4.5) over \(\omega\).
The gap between minimum and average is precisely the selector grouping
problem.

## 5. Integral feasibility is a semigroup problem

The actual load vectors form the finite Minkowski sum

\[
                 \mathcal P_{\mathbb Z}
                   =\sum_{f\in\mathfrak F}\mathcal A_f.            \tag{5.1}
\]

Integral feasibility is exactly

\[
                 \mathcal P_{\mathbb Z}
                    \cap\mathcal B_{\mathbb Z}\ne\varnothing.      \tag{5.2}
\]

Equivalently, some balanced monomial has nonzero coefficient in

\[
 \prod_{f\in\mathfrak F}
   \left(\sum_{\omega\in\Omega_f}
      \prod_{c,T}X_{c,T}^{a_{f,\omega}^{c}(T)}\right). \tag{5.3}
\]

Theorem 3.1 proves only

\[
 \operatorname{conv}\mathcal P_{\mathbb Z}
       \cap\operatorname{conv}\mathcal B_{\mathbb Z}
                \ne\varnothing.                     \tag{5.4}
\]

To deduce (5.2) from (5.4), one needs an integer decomposition or
normality theorem for the grouped configuration semigroup.  Neither the
rank-twisted coefficient identities nor the complete-design batching
proves such a theorem.

The selector decoder explains why.  Inside one product status cell,
targets produced from fibre \(z\) retain all selector orientations.
Thus a configuration row must choose one whole column
\(a_{f,\omega}\).  It cannot split the owners in that row according to
the fractional coefficients of several options.

## 6. Why the obvious linear discrepancy is not a Hall cut

At depth one in one fibre, the symmetric complete-design average places
the same mass on every one of the \(n_f\) possible deleted axes.  One
integral active set uses only \(r\) of those axes.  Its conditional
\(\ell^1\)-distance from the uniform direction marginal is

\[
                  2\left(1-{r\over n_f}\right)|V_f|
                         =\Theta(|V_f|).              \tag{6.1}
\]

Summed over fibres, this is \(\Theta(W_0)\).  It is a genuine
configuration-grouping discrepancy.

It is not an \(\Omega(W)\) physical-target Hall cut.  Conditional on one
fibre, the abstract target universe has more points than source starts,
so its balanced conditional quota resets to zero/one.  Concentrating the
ones on the selected active directions is allowed.  Other product cells
may supply the literal targets omitted by this fibre.  Therefore (6.1)
cannot be inserted on the right side of (3.5).

This audit rules out a tempting but invalid no-go argument.

## 7. Exact remaining dichotomy

A positive coefficient-one theorem can now be proved in either of two
precise ways.

1. **Integer decomposition.**  Prove that the particular rank-twisted
   configuration sum (5.1) is normal within \(o(W)\) boundary, and verify
   the weighted inequalities (3.4) using (4.1)--(4.2).
2. **Direct grouped flow.**  Refine the option library into an explicit
   network whose integral flows choose one option per fibre and whose
   target sinks have the reset capacities (2.2).  Total unimodularity
   must be proved for that refinement, not assumed.

A negative theorem requires a real weight array \(\lambda\), or target
families in (3.5), for which the left side falls short by
\(\Omega(W)\).  The full-internal-quartet weight no longer works because
every rank-twisted packet has \(r\) crossing axes.  The conditional
direction discrepancy (6.1) also does not work because of quota resets.

Accordingly, this note does **not** claim the requested positive theorem
or a quantitative physical Hall cut.  It gives the exact dual against
which either claim must be checked and records why the two currently
available candidate cuts are invalid.

A sharp sufficient condition and its audit are given in
\`MATH_THEOREM_M_CONVEX_SUFFICIENCY_AND_SELECTOR_ATLAS_FAILURE_20260726.md\`:
saturated \(M\)-convex fibre option sets make the dual integrally
sufficient by polymatroid intersection, but the actual selector fibres
fail the unit exchange axiom already at lower depth one.
