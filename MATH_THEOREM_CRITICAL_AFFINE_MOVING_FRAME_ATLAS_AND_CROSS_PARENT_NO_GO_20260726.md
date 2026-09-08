# The critical affine moving-frame atlas: exact exposure, serial Gaussian no-go, and the joint-parent toll

Date: 2026-07-26

Method: pure mathematics only.  This note uses the exact descent and
occurrence results of
`MATH_THEOREM_LOWER_NEUTRAL_TRADE_DIAMETER_AND_OCCURRENCE_OBSTRUCTION_20260726.md`.
No marginal estimates are multiplied.

## 0. Outcome

There is an exact critical moving-frame scaffold.  On the affine-plane
subsequence

\[
                         n=q^2,\qquad q\text{ a prime power},  \tag{0.1}
\]

the \(q+1=\Theta(\sqrt m)\) parallel classes of affine lines give
\(q+1\) coordinate frames, each with blocks of size
\(d=q=\Theta(\sqrt m)\).  Every coordinate pair lies in exactly one block.
Consequently, for every Hamilton cycle \(C\subset J(n,m)\),

\[
 \boxed{
   \sum_{L\text{ affine line}} I_L(C)=W.}            \tag{0.2}
\]

Thus the critical \(\Theta(\sqrt m)\)-frame family completely removes the
pair-exposure shortage: every physical cycle edge is exposed once.  It also
has no frozen adjacency projection on the upper layer; every Johnson
adjacency of upper targets belongs to exactly one line-parent cell.

This scaffold is **not** by itself a lower-neutral trade atlas.  The
following two theorems locate the remaining obstruction.

1. A cross-parent trade obtained by serially composing parent-supported
   pieces has an overlap graph.  If every connected overlap component uses
   at most \(\lambda\) parents, its upper support has diameter at most
   \[
                         \lambda\lfloor q/2\rfloor. \tag{0.3}
   \]
   Hence, whenever \(\lambda q=O(\sqrt m)\), there are positive-density,
   exact-mass upper states, satisfying the complete-lower-shadow necessary
   condition and asymptotically perfect point margins, on which no such
   trade descends.  Since \(q\asymp\sqrt m\), a genuine critical-frame
   evader must have
   \[
                         \boxed{\lambda\longrightarrow\infty.} \tag{0.4}
   \]
   Merely possessing \(\Theta(\sqrt m)\) frames while using only boundedly
   many parents in each trade does not evade the Gaussian cut.

2. Even unbounded serial composition of pieces which are lower- and
   owner-neutral **inside each parent** preserves a new exact quadratic
   family of affine-line invariants:
   \[
     F_c(U)=\sum_{\{x,y\}\in\binom U2}c_{\ell(x,y)}. \tag{0.5}
   \]
   Here \(c_L\) is an arbitrary line weight and \(\ell(x,y)\) is the unique
   affine line through \(x,y\).  Therefore parentwise-neutral pieces cannot
   form the required unrestricted cross-parent atlas, regardless of serial
   depth.

The only surviving version is a **jointly neutral** cross-parent trade:
its restrictions to individual parents must carry nonzero owner/lower
boundary ledgers which cancel only after several parents are combined.  An
exact formula, (6.6), gives the toll paid by those ledgers to break (0.5).
No construction proving positive-density occurrence of such joint factors
in every lower-complete Hamilton cycle is obtained here.  Conversely, the
Gaussian and affine-invariant arguments do not refute these genuinely joint
factors.  They give a statewise no-go for the serial interpretation and a
sharp specification of what an actual \(\Theta(\sqrt m)\)-frame construction
must prove.

## 1. The affine-line frame system

Let \(\Omega=\mathbb F_q^2\), so \(|\Omega|=n=q^2\).  The affine lines form
a resolvable Steiner system

\[
                         S(2,q,q^2).                 \tag{1.1}
\]

There are \(q+1\) parallel classes, each consisting of \(q\) disjoint
\(q\)-sets.  Any two distinct coordinates lie on a unique line.

Take \(m=\lfloor n/2\rfloor\), so \(n\in\{2m,2m+1\}\), and put

\[
 \mathcal M=\binom\Omega m,\qquad
 \mathcal U=\binom\Omega{m+1},\qquad
 W=|\mathcal M|.                                    \tag{1.2}
\]

For a Johnson edge \(e=XY\), its exchanged coordinate pair is

\[
                         p(e)=X\triangle Y.          \tag{1.3}
\]

For a line \(L\), let

\[
                         I_L(C)=|\{e\in E(C):p(e)\subset L\}|. \tag{1.4}
\]

### Theorem 1.1 (exact critical exposure)

For every Hamilton cycle \(C\) of \(J(n,m)\), (0.2) holds.

#### Proof

Every Hamilton edge has one exchanged pair, and that pair lies on exactly
one affine line.  Hence every edge is counted exactly once on the left of
(0.2).  A Hamilton cycle on \(W\) owners has \(W\) edges. \(\square\)

This is stronger than an expectation.  It holds statewise for every cycle,
including every lower-complete Hamilton cycle.

For a line \(L\), a set \(K\subset\Omega\setminus L\), and an integer \(r\),
define the upper parent cell

\[
 \mathcal C(K,L,r)
   =\{K\cup B:B\in\tbinom L{r+1}\}.                 \tag{1.5}
\]

### Theorem 1.2 (no frozen upper adjacency)

Every edge of the upper Johnson graph \(J(n,m+1)\) lies in exactly one cell
of the form (1.5).

#### Proof

Let upper targets \(U,V\) be adjacent, with

\[
                         U\triangle V=\{x,y\}.       \tag{1.6}
\]

Let \(L=\ell(x,y)\) be their unique affine line, put

\[
                         K=U\setminus L=V\setminus L,
 \qquad r+1=|U\cap L|=|V\cap L|.                    \tag{1.7}
\]

Then \(U,V\in\mathcal C(K,L,r)\).  Uniqueness follows from uniqueness of
\(L\). \(\square\)

Thus the old first-moment occurrence cut and every cut obtained merely by
deleting a fixed set of exchange directions are gone at this scale.

## 2. Serial cross-parent trades and their overlap depth

Let an upper change be written

\[
                         \delta=\delta_1+\cdots+\delta_t,      \tag{2.1}
\]

where each \(\delta_i\) is supported in one parent cell
\(\mathcal C_i=\mathcal C(K_i,L_i,r_i)\).  No neutrality assumption is
needed in this section.

Define the parent-overlap graph \(G_\delta\) on \([t]\) by

\[
 ij\in E(G_\delta)
 \quad\Longleftrightarrow\quad
 \operatorname {supp}\delta_i\cap
 \operatorname {supp}\delta_j\ne\varnothing.       \tag{2.2}
\]

Let \(\lambda(\delta)\) be the largest number of vertices in a connected
component of \(G_\delta\).

Every cell has Johnson diameter at most

\[
                         D_q:=\lfloor q/2\rfloor.    \tag{2.3}
\]

### Theorem 2.1 (overlap-depth diameter bound)

The union of the supports belonging to a \(k\)-vertex connected component
of \(G_\delta\) has diameter at most \(kD_q\).  Consequently, if the current
upper repeat and hole families have distance \(\rho\), and

\[
                         \lambda(\delta)D_q<\rho,    \tag{2.4}
\]

then \(\delta\) cannot strictly decrease upper repeat excess.

#### Proof

Choose two targets in the union and cells containing them.  A path between
the two cells in a spanning tree of the overlap component has at most
\(k-1\) links.  At every link choose a target common to the two consecutive
cells.  Moving inside the first cell, then between successive common
targets inside the intermediate cells, and finally to the second target
costs at most \(kD_q\).

Different components of \(G_\delta\) have disjoint upper supports.  Hence
the exact repeat variation is the sum of its variations on the components.
Under (2.4), each component has diameter less than \(\rho\), so the diameter
lock from the preceding note makes every summand nonnegative. \(\square\)

This theorem permits arbitrary cancellations at shared upper targets.  A
large catalogue of frames helps only when individual trades have large
*connected* cross-parent depth.

## 3. A shadow-admissible Gaussian statewise no-go

We strengthen the load-profile obstruction from the preceding note by also
enforcing the necessary lower-shadow coverage condition.

### Lemma 3.1 (small upper cover of every lower target)

For \(n\in\{2m,2m+1\}\), there is a family
\(\mathcal G\subset\binom{[n]}{m+1}\) such that

\[
                         |\mathcal G|=O(W/m),        \tag{3.1}
\]

and every \((m-1)\)-set is contained in some member of \(\mathcal G\).

#### Proof

Select every upper target independently with probability \(p=A/m\), where
\(A>2\log4\) is fixed.  A lower target \(S\) has

\[
                         \binom{n-m+1}{2}
                         ={m^2\over2}+O(m)           \tag{3.2}
\]

upper extensions.  Hence

\[
 \Pr\{S\text{ is uncovered}\}
 \le \exp\{-Am/2+O(1)\}.                            \tag{3.3}
\]

There are at most \(4^m\) lower targets up to a fixed polynomial factor, so
the union bound makes the probability of any uncovered target tend to zero.
The selected family has expected size \(O(W/m)\), and a standard Markov
bound gives a realization of size \(O(W/m)\) simultaneously with complete
coverage. \(\square\)

### Theorem 3.2 (bounded serial depth is statewise locked)

On the even ground \(n=2m\), let \(d_m\) be the maximum active block size
of a parent atlas and let
\(\lambda_m\) bound every connected parent-overlap component.  If

\[
                         \lambda_m d_m=O(\sqrt m),   \tag{3.4}
\]

then there are upper load vectors \(u_m\) with all of the following
properties:

1. \(\sum_Uu_m(U)=W\);
2. the repeat and hole families both have size \(\Theta(W)\);
3. the non-hole upper targets cover every lower target;
4. the point-margin error from a uniform vector has \(\ell^1\)-norm
   \(o(mW)\);
5. no feasible upper change whose connected parent depth is at most
   \(\lambda_m\) strictly decreases repeat excess.

#### Proof

Split the coordinate set into equal shores \(A,B\), and put

\[
 T(U)=|U\cap A|-{|U|\over2}.                         \tag{3.5}
\]

For a uniform upper target, \(T(U)/\sqrt m\) converges to a nondegenerate
centred Gaussian.  Let \(C\) be a constant for which
\(\lambda_md_m\le C\sqrt m\).  Choose constants \(0<a<b\) so that

\[
 \Pr\{|Z|\le a\}=\Pr\{|Z|\ge b\}=:\gamma>0,
 \qquad b-a>C,                                      \tag{3.6}
\]

for the limiting Gaussian \(Z\).  This is possible for every fixed \(C\):
take \(b\) large and then choose the small central quantile of the same
mass.

Let the preliminary repeat family be the central band and the preliminary
hole family the tail band.  Each has size \((\gamma+o(1))W\), and one
Johnson move changes \(T\) by at most one.  Their distance is therefore

\[
                         (b-a)\sqrt m-O(1)
                         >\lambda_m\lfloor d_m/2\rfloor        \tag{3.7}
\]

for all large \(m\).

Take the cover \(\mathcal G\) from Lemma 3.1 and remove its members from the
hole family.  This changes only \(o(W)\) targets, retains positive density
and the distance bound, and ensures that every lower target has a non-hole
upper extension.  Put load two on the repeat family, zero on the remaining
hole family, and one elsewhere.  Modify multiplicities on \(o(W)\) central
occupied targets to make the total load exactly \(W\).

Before the \(o(W)\) modifications, the central and tail bands are invariant
under the transitive group
\((S_A\times S_B)\rtimes\langle A\leftrightarrow B\rangle\), so their point
degrees are uniform.  The modifications change the total point ledger by
only \(o(mW)\).  Finally Theorem 2.1 and (3.7) prohibit strict descent. 
\(\square\)

For the affine atlas, \(d_m=q\asymp\sqrt m\).  Theorem 3.2 therefore forces
\(\lambda_m\to\infty\).  This is a statewise theorem.  As before, it does
not assert that the constructed load vector is chronologically realized by
a lower-complete Hamilton cycle; it now shows, however, that shadow coverage
does not remove the obstruction.

## 4. The exact transport-work inequality

The next inequality applies after the diameter lock has been evaded.

For a zero-mass signed vector \(\eta\) on \(\mathcal U\), define its
Johnson earthmover norm by

\[
 \|\eta\|_{\rm EM}
  =\min_\pi\sum_{U,V}d_J(U,V)\pi(U,V),               \tag{4.1}
\]

where \(\pi\) ranges over couplings from \(\eta^-\) to \(\eta^+\).

Suppose

\[
                         \delta=\sum_{i=1}^t\delta_i,           \tag{4.2}
\]

where every \(\delta_i\) has total mass zero, support diameter at most
\(D\), and positive mass

\[
                         s_i=\|\delta_i^+\|_1.       \tag{4.3}
\]

### Theorem 4.1 (descent costs transport work)

If \(\delta\) lowers the upper repeat excess by \(h>0\), and the current
repeat and hole families have distance \(\rho\), then

\[
 \boxed{
                         h\rho
          \le\|\delta\|_{\rm EM}
          \le D\sum_{i=1}^t s_i.}                   \tag{4.4}
\]

#### Proof

Let \(s=\|\delta^+\|_1=\|\delta^-\|_1\).  Let \(a\) be the positive mass
placed on current holes, and let
\(b=\sum_U\min\{\delta^-(U),(u(U)-1)_+\}\) be the discounted negative mass
removed from current repeated targets.  The exact descent formula gives

\[
                         a+b\ge s+h.                 \tag{4.5}
\]

In every coupling from \(\delta^-\) to \(\delta^+\), at least
\(a+b-s\ge h\) units travel from a repeated target to a hole.  Each such
unit travels distance at least \(\rho\), proving the first inequality.

Inside the support of \(\delta_i\), its negative and positive masses can be
coupled at cost at most \(Ds_i\).  The earthmover norm is subadditive under
addition of zero-mass vectors.  Summing these local couplings proves the
second inequality. \(\square\)

For a directly applicable, negative-edge-disjoint bank of parent factors,
\(s_i\) is at most the number of deleted physical cycle edges in the
corresponding factor.  In the affine system every Johnson edge belongs to
one line-parent cell.  Therefore such a bank has

\[
                         \sum_i s_i\le W,            \tag{4.6}
\]

and hence

\[
                         h\rho\le DW.                \tag{4.7}
\]

This is an actual upper-hole capacity cut.  Serial procedures which delete
edges created by earlier stages pay their full work in \(\sum_i s_i\);
they are not entitled to the one-pass bound (4.6).

## 5. A surviving affine-line invariant

The affine scaffold has a further exact obstruction which pair exposure
does not see.

Give every affine line \(L\) an arbitrary real weight \(c_L\), and define

\[
 F_c(U)=\sum_{\{x,y\}\in\binom U2}c_{\ell(x,y)},
 \qquad U\in\mathcal U.                              \tag{5.1}
\]

### Lemma 5.1 (local affinity)

On a parent cell \(\mathcal C(K,L,r)\), with \(k=r+1\),

\[
 F_c(K\cup B)
   =C_{K,L,k}+\sum_{x\in B}a_{K,L}(x),               \tag{5.2}
\]

where

\[
 C_{K,L,k}=F_c(K)+\binom k2c_L,
 \qquad
 a_{K,L}(x)=\sum_{y\in K}c_{\ell(x,y)}.             \tag{5.3}
\]

#### Proof

Pairs inside \(K\) give \(F_c(K)\).  Every pair inside \(B\subset L\)
lies on \(L\), giving the constant \(\binom k2c_L\).  The remaining pairs
have one endpoint \(x\in B\) and one endpoint in \(K\), and their
contribution is additive in \(x\). \(\square\)

### Theorem 5.2 (parentwise-neutral serial invariant)

Let \(z\) be a lower- and owner-neutral Johnson edge trade supported in one
line-parent cell, and put \(\delta=B_+z\).  Then, for every line weighting
\(c\),

\[
                         \langle F_c,\delta\rangle=0.            \tag{5.4}
\]

The same identity holds for every finite sum or serial composition of such
parentwise-neutral trades.

#### Proof

The diamond identity gives

\[
 P_{m+1}\delta
   =P_mB_0z-P_{m-1}B_-z=0.                           \tag{5.5}
\]

Also \(\sum_U\delta(U)=0\).  Apply the affine formula (5.2): its constant
term pairs with the total mass and its linear terms pair with the point
margins, so both vanish.  Additivity proves the serial assertion. \(\square\)

For a nonconstant line weighting this is genuinely stronger than the point
invariant.  For example, give one line \(L_0\) weight one and every other
line weight zero.  Then

\[
                         F_c(U)=\binom{|U\cap L_0|}{2}.          \tag{5.6}
\]

This function is not of the form \(a_0+\sum_{x\in U}a_x\): an exchange
second difference using two coordinates of \(L_0\) and two outside it is
nonzero.  Hence, by row-space/kernel duality for the point-incidence matrix,
there is a zero-mass, zero-point-margin upper vector on which \(F_c\) is
nonzero.  The serial parentwise-neutral directions therefore lie in a
proper subspace of the full point-balanced upper space.

Thus the affine atlas is projection-free at the level of target adjacency
but not at the level of lower-neutral trade directions.  Port cancellation
between already-neutral parent trades cannot break (5.4).

This invariant alone is not claimed to force an \(\Omega(W)\) residual: an
\(o(W)\) exceptional load may concentrate on extreme values of \(F_c\).
Its rigorous role is to prove that the parentwise-neutral affine catalogue
is algebraically incomplete even after arbitrary serial composition.

## 6. The exact toll for a genuinely joint-parent trade

Let a global trade be decomposed at the edge-vector level as

\[
                         z=z_1+\cdots+z_t,           \tag{6.1}
\]

where \(z_i\) is supported in the parent cell
\(\mathcal C(K_i,L_i,r_i)\), but do **not** assume that \(z_i\) is neutral.
Put

\[
 \delta_i=B_+z_i,\qquad
 \tau_i=\sum_U\delta_i(U),
 \qquad
 b_i(x)=\sum_{U\ni x}\delta_i(U).                  \tag{6.2}
\]

The global conditions \(B_0z=B_-z=0\) imply

\[
                         \sum_i\tau_i=0,
 \qquad
                         \sum_i b_i(x)=0\quad(x\in\Omega),    \tag{6.3}
\]

but the individual ledgers need not vanish.  The diamond identity gives
their physical meaning:

\[
 b_i=P_mB_0z_i-P_{m-1}B_-z_i.                       \tag{6.4}
\]

Thus \(b_i\) is exactly the point projection of the owner/lower imbalance
exported by parent \(i\).

### Theorem 6.1 (joint-parent invariant-breaking formula)

For every line weighting \(c\),

\[
\boxed{
 \langle F_c,B_+z\rangle
  =\sum_{i=1}^t
    \left[
      C_{K_i,L_i,r_i+1}\tau_i
      +\sum_{x\in L_i}a_{K_i,L_i}(x)b_i(x)
    \right].}                                      \tag{6.5}
\]

In particular, define

\[
 \Xi(z_1,\ldots,z_t)
   =\sum_i\left(|\tau_i|+\sum_{x\in L_i}|b_i(x)|\right).       \tag{6.6}
\]

If

\[
 A_c=\max_i\max\left\{
 |C_{K_i,L_i,r_i+1}|,
 \max_{x\in L_i}|a_{K_i,L_i}(x)|
 \right\},                                         \tag{6.7}
\]

then

\[
                         |\langle F_c,B_+z\rangle|
                         \le A_c\Xi(z_1,\ldots,z_t).            \tag{6.8}
\]

#### Proof

Apply Lemma 5.1 to each \(\delta_i\).  Its constant part contributes
\(C_i\tau_i\), while its linear part contributes
\(\sum_{x\in L_i}a_i(x)b_i(x)\).  Summation proves (6.5), and the triangle
inequality proves (6.8). \(\square\)

Formula (6.5) is the promised cross-parent toll.  If every parent is
separately neutral, all \(\tau_i,b_i\) vanish and Theorem 5.2 returns.  A
genuine evader must export nonzero owner/lower ledgers from many parents and
cancel them only globally.  Shared upper targets alone are insufficient.

## 7. Consequence for the coefficient-one lane

The critical frame count itself is now settled:

* \(q+1=\Theta(\sqrt m)\) affine frames give exact \(W\)-edge exposure for
  every lower-complete Hamilton cycle;
* the union of their parent cells contains every upper Johnson adjacency;
* bounded connected cross-parent depth is nevertheless statewise blocked;
* arbitrary-depth composition of separately neutral parents preserves the
  quadratic invariants (5.1).

Therefore a successful growing-diameter atlas cannot be a larger pentagon
placed independently in each affine line, nor a serial network of such
already-neutral gadgets.  It must supply complete physical factors
\(z_1,\ldots,z_t\) with all of the following properties simultaneously:

1. connected parent depth \(\lambda\to\infty\);
2. nonzero local boundary ledgers \((\tau_i,b_i)\) satisfying the global
   cancellations (6.3);
3. total transport work meeting (4.4);
4. negative factors actually contained in the current Hamilton cycle;
5. exact negative repeat / positive hole score \(\Omega(W)\), evaluated by
   the nonlinear descent formula;
6. a legal Hamilton replacement after the joint pieces are fused.

The affine construction proves that the old Gaussian pair-occurrence count
is not the final obstruction.  Theorem 3.2 refutes every bounded-depth
cross-parent interpretation, and Theorem 5.2 refutes arbitrary serial
composition of parentwise-neutral pieces.  The unrestricted jointly-neutral
factor satisfying items 1--6 remains open; its minimal missing inequality is
a positive-density occurrence bound for factors with nonzero local ledger
\(\Xi\), not another coordinate-pair or lattice-span estimate.
