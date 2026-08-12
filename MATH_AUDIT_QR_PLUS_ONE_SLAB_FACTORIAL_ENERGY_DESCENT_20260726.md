# Audit: one-depth factorial energy under (Q_{R+1}) slab-resolution trades

Date: 2026-07-26

## 0. Verdict

Fix one signed depth (c=(\epsilon,q)).  The energy algebra of a
(Q_{R+1}) resolution trade is exact and particularly simple:

* a single resolution comparison is a **linear best-response problem**
  against the load outside that slab;
* a compatible family of slabs gives an exact quadratic multi-label
  objective whose mixed coefficients are the literal derivative inner
  products;
* those mixed coefficients have no forced sign;
* equal shore size, trace injectivity, balanced derivatives, and even the
  audited direction marginals do not by themselves imply an
  (M)-convex/exchange descent theorem.

An explicit set-system model below has a strict one-slab local minimum of
factorial collision energy, while switching two slabs together strictly
improves it.  This is not claimed to be an embedded compiler example; it
is a rigorous counterexample to any descent theorem using only the
currently proved universal properties of the slab columns.

There is also an exact invariant for the genuine trades.  If
(z_q^\epsilon) is the direction-support histogram, every move changes it
by

\[
             2qg_R(e_e-e_i),\qquad g_R=2^R/R.
\]

Consequently its coordinate residues modulo (2qg_R), its sums on
components of the allowed direction-exchange graph, and the cross-depth
quantities

\[
             z_q^\epsilon-qz_1^\epsilon
\]

are invariant under every sequence of these trades.  This does not alone
lower-bound literal collision energy, but it rules out treating the
resolution moves as unrestricted load exchanges.

## 1. One slab: the exact derivative is linear in the outside load

Let the old and new signed-depth trace images of one slab be

\[
                 A,B\subseteq\Omega,qquad |A|=|B|=M,
                 \qquad M=2^{R+1}.
\]

Both are sets, not multisets.  Put

\[
 \Gamma_A=\mathbf 1_A,\qquad \Gamma_B=\mathbf 1_B,
 \qquad \delta=\Gamma_B-\Gamma_A.
\]

Write

\[
 P=B\setminus A,\qquad N=A\setminus B,
 \qquad |P|=|N|=r.
\]

Then

\[
 \delta(T)\in\{-1,0,1\},\qquad
 \sum_T\delta(T)=0,\qquad
 \|\delta\|_2^2=\|\delta\|_1=2r.                 \tag{1.1}
\]

Let (h) be the load from every packet outside the slab.  For

\[
                   {\cal C}(L)=\sum_T\binom{L(T)}2,
\]

trace injectivity gives

\[
\boxed{
 {\cal C}(h+\Gamma_B)-{\cal C}(h+\Gamma_A)
       =\langle h,\delta\rangle.}                 \tag{1.2}
\]

Indeed, the positive sites create (h(T)) new collision pairs and the
negative sites remove (h(T)) old collision pairs.  There is no
within-shore term.

If (L=h+\Gamma_A) is the current total load, the same formula is

\[
 {\cal C}(L+\delta)-{\cal C}(L)
       =\langle L,\delta\rangle+r.                 \tag{1.3}
\]

For the integral floor energy

\[
 Q_c(L)=\sum_T(L(T)-c)(L(T)-c-1),
\]

the total occurrence mass is fixed, and hence

\[
\boxed{
 Q_c(L+\delta)-Q_c(L)
 =2\langle L-c-\tfrac12,\delta\rangle+\|\delta\|_2^2
 =2\langle h,\delta\rangle.}                     \tag{1.4}
\]

Thus the apparent quadratic self-cost in the first expression cancels
exactly against the old shore.  For a fixed outside load, the best of the
(R+1) facet resolutions is simply the resolution (j) minimizing

\[
                        \langle h,\Gamma_j\rangle. \tag{1.5}
\]

There can be no non-global local minimum inside one slab if all its
resolutions are compared.  Any trapping phenomenon is necessarily an
interaction between slabs.

## 2. A compatible family: exact quadratic identities

Let (k=1,\ldots,K) index owner-disjoint, simultaneously switchable
slabs.  At the present resolution let their trace indicators be
(A_k=\mathbf1_{I_k^0}), let the selected alternatives be
(B_k=\mathbf1_{I_k^1}), and put

\[
                 \delta_k=B_k-A_k,qquad
                 r_k=|I_k^1\setminus I_k^0|.
\]

Let (L_0) be the current total load, including all (A_k), and for
(x\in\{0,1\}^K) put

\[
                       L(x)=L_0+\sum_kx_k\delta_k. \tag{2.1}
\]

Define the current one-flip costs

\[
 d_k={\cal C}(L_0+\delta_k)-{\cal C}(L_0)
     =\langle L_0,\delta_k\rangle+r_k.             \tag{2.2}
\]

Then

\[
\boxed{
 {\cal C}(L(x))={\cal C}(L_0)
       +\sum_k d_kx_k
       +\sum_{k<\ell}\langle\delta_k,\delta_\ell\rangle x_kx_\ell.}
                                                               \tag{2.3}
\]

For (Q_c), multiply every nonconstant term in (2.3) by (2).
Equivalently, if (h_k(x)) is the load outside slab (k) at state (x),
then the exact best-response derivative is

\[
 {\cal C}(x^{k\leftarrow1})-{\cal C}(x^{k\leftarrow0})
                      =\langle h_k(x),\delta_k\rangle.          \tag{2.4}
\]

The mixed rectangle derivative is

\[
\boxed{
 {\cal C}(0,0)+{\cal C}(1,1)
 -{\cal C}(1,0)-{\cal C}(0,1)
                  =\langle\delta_k,\delta_\ell\rangle.}       \tag{2.5}
\]

No proved property of the compiler columns fixes the sign of (2.5).

Put

\[
       D=\sum_k\delta_k,qquad
       V=\sum_k\|\delta_k\|_2^2=2\sum_kr_k.                    \tag{2.6}
\]

The complete pair-interaction ledger is

\[
\boxed{
 \sum_{k<\ell}\langle\delta_k,\delta_\ell\rangle
                  ={\|D\|_2^2-V\over2}.}                       \tag{2.7}
\]

Pointwise, if (p_T) moves add (T) and (n_T) moves remove (T), then

\[
 D(T)=p_T-n_T,qquad
 V=\sum_T(p_T+n_T),                                             \tag{2.8}
\]

and the contribution of (T) to (2.7) is

\[
       \binom{p_T}{2}+\binom{n_T}{2}-p_Tn_T.                    \tag{2.9}
\]

Thus aligned additions/removals give positive interaction, while one
move adding precisely where another removes gives negative interaction.
Both signs are structurally possible at this algebraic level.

Two further useful identities are

\[
 \sum_kd_k=\langle L_0,D\rangle+{V\over2},                      \tag{2.10}
\]

and

\[
 {\cal C}(L_0+D)-{\cal C}(L_0)
                  =\langle L_0,D\rangle+{\|D\|_2^2\over2}.    \tag{2.11}
\]

If the moves are chosen independently with probability (1/2), then

\[
\boxed{
 \mathbb E{\cal C}(L(X))-{\cal C}(L_0)
 =\frac12\langle L_0,D\rangle
       +\frac18\bigl(V+\|D\|_2^2\bigr).}                       \tag{2.12}
\]

Equation (2.12) separates the coherent displacement (D) from the
unavoidable independent-choice variance (V).

For more than two resolutions per slab, if (Gamma_{k,j}) is the set
indicator for resolution (j), the exact global formula is

\[
 {\cal C}(h+\sum_k\Gamma_{k,j_k})
 ={\cal C}(h)+\sum_k\langle h,\Gamma_{k,j_k}\rangle
  +\sum_{k<\ell}\langle\Gamma_{k,j_k},\Gamma_{\ell,j_\ell}\rangle.
                                                               \tag{2.13}
\]

This is a quadratic multi-label potential, not a separable convex
exchange problem.

## 3. Strict bad local minimum under the proved universal column axioms

The following finite example uses only equal shore cardinality,
trace-injective shores, and balanced ({-1,0,1}) derivatives.

Let (X,Y) be disjoint sets of the same cardinality (K\ge2), and let
(a,b,c,d) be four further distinct targets.  Define two binary slabs by

\[
 \begin{array}{ll}
 A_1=X\cup\{a\},& B_1=Y\cup\{c\},\\
 A_2=Y\cup\{b\},& B_2=X\cup\{d\}.
 \end{array}                                                    \tag{3.1}
\]

Add one fixed trace-injective background packet (H) containing (a,b)
and no point of (X\cup Y\cup\{c,d\}).  Pad (A_k,B_k,H), if desired,
to any common cardinality (M\ge K+1) using slab-specific common fillers
and mutually disjoint background fillers.  Padding creates no new
intersection.

The four factorial collision energies are

\[
 \begin{array}{c|cc}
       &A_2&B_2\\ \hline
 A_1&2&K+1\\
 B_1&K+1&0.
 \end{array}                                                    \tag{3.2}
\]

Indeed, at ((A_1,A_2)) the only collisions are (a) and (b) with
(H).  A single switch removes one of those collisions but creates the
(K)-fold cross intersection (X) or (Y).  Switching both removes all
collisions.

Therefore ((A_1,A_2)) is a **strict one-slab local minimum**, while
((B_1,B_2)) is strictly better.  Here

\[
 \langle\delta_1,\delta_2\rangle=-2K,                           \tag{3.3}
\]

which is exactly the cooperative term missed by one-slab descent.

Taking (M=2^{R+1}) and any

\[
                  2qg_R\le K<M
\]

also makes the changed-support size at least the lower scale forced by
the direction marginal of a genuine depth-(q) slab trade.  This does
not prove literal realizability by the compiler; it shows that neither
large derivative support nor the universal norm bounds repair the
exchange failure.

Thus no (M)-convex descent theorem follows from the currently audited
column properties alone.  A positive result must use an additional
literal exchange axiom, or permit coordinated multi-slab moves.

## 4. Exact direction-projection identities and invariants

Let (z_q^\epsilon) be the histogram whose coordinate (a) counts
signed-depth traces whose compiler direction support contains physical
direction (a).  For a trade which freezes old direction (e), freezes
new direction (i), and hence activates (e) while deactivating (i),
the audited slab theorem gives

\[
       z_q^\epsilon(\mathrm{new})-z_q^\epsilon(\mathrm{old})
           =\alpha_q(e_e-e_i),
       \qquad \alpha_q=2qg_R.                                  \tag{4.1}
\]

For (K) oriented trades put (v_k=e_{e_k}-e_{i_k}).  Then

\[
 \Delta z_q^\epsilon=\alpha_q\sum_kv_k,                        \tag{4.2}
\]

\[
 \sum_k\|\alpha_qv_k\|_2^2=2K\alpha_q^2,                     \tag{4.3}
\]

and

\[
 \sum_{k<\ell}\langle\alpha_qv_k,\alpha_qv_\ell\rangle
 =\frac{\alpha_q^2}{2}
      \left(\left\|\sum_kv_k\right\|_2^2-2K\right).         \tag{4.4}
\]

In particular, an Eulerian collection of oriented direction exchanges
has zero aggregate direction derivative and projected pair sum
(-K\alpha_q^2).  This is an exact projected cancellation identity.  It
does not determine the literal inner products in (2.7), because the
direction-support projection is not an isometry.

Every sequence of allowed trades preserves:

1. each coordinate of (z_q^\epsilon) modulo (2qg_R);
2. the exact sum of (z_q^\epsilon) over every connected component of
   the graph whose edges are allowed direction exchanges;
3. for each sign and each (q),
   
   \[
                  z_q^\epsilon-qz_1^\epsilon;                  \tag{4.5}
   \]
4. at fixed (q), the lower/upper difference
   
   \[
                  z_q^+-z_q^-.                                 \tag{4.6}
   \]

The last two follow because (4.1) is (q) times its depth-one value and
is identical for the two signs.  These are genuine invariants of the
resolution-trade system, independent of compiler order.

They are auxiliary incidence invariants, not functions of the literal
load vector alone.  Accordingly they are not yet a collision-energy
lower bound.  They do show that the reachable family lies in a proper
lattice coset and that an unrestricted transportation/M-convex model is
incorrect.

## 5. What a valid descent theorem would have to add

At a state (x), one-slab local optimality is exactly

\[
 \langle h_k(x),\Gamma_{k,j}-\Gamma_{k,j_k}\rangle\ge0
 \quad\text{for every slab (k) and every allowed resolution (j)}.
                                                               \tag{5.1}
\]

This is only membership of the outside-load vector in the polar cone of
the available derivatives.  It does not force global balance.

There are three plausible forms of genuinely new input:

1. **Conformal exchange.**  Prove that whenever two reachable load vectors
   differ, a bounded compatible compound trade moves one coordinate of
   the larger load toward the smaller without increasing any coordinate
   discrepancy.  This is the missing (M)-exchange axiom.
2. **Energy coercivity.**  Prove directly that every state with floor
   energy above the desired error admits a (possibly compound) compatible
   trade with negative value in (1.2).
3. **Cycle moves.**  Use Eulerian collections in the direction graph, but
   additionally prove literal, not merely projected, alignment of their
   derivatives so that the negative terms in (2.9) dominate the positive
   ones.

The present (Q_{R+1}) theorem establishes local reachability, but none
of these three properties.  The exact algebra therefore moves the open
gate from integrality to a literal compound-exchange/coercivity theorem.
