# The all-adjacent-block conjugate pair against the critical-root hinge

Date: 2026-07-26

Method: pure mathematics only. No finite search, computation, solver, or
web input is used.

## 0. Verdict

Let

\[
 \eta_r=\prod_{i=1}^{r-1}(2i\ \ 2i+1),
\]

let \(F_r\) be the canonical anchored \(D_r\)-port factor, and put

\[
                         G_r(P)=\eta_rF_r(\eta_rP).
\tag{0.1}
\]

The fixed-exterior twist correction does not invalidate (0.1). Every row
of \(G_r\) starts at \(P\) and ends at \(P^c\); (0.1) is a whole-factor
coordinate conjugation, not a nonidentity twisted local slab. Thus
\(F_r,G_r\) are two literal integral exact factors.

As \(\mathrm{CRH}_A\) is presently worded, its second clause asks for
genuinely unrelated seeds. The pair (0.1) is a coordinate conjugate and
therefore fails that clause formally. The remainder of this audit checks
the quantitative interfaces to determine whether that wording could be
relaxed for this explicit exception.

The audit against \(\mathrm{CRH}_A\) has the following sharp outcome.

1. The Lane N constant \(1/9\) is exact for the matrix whose cells retain
   both the source first-return class and the first-insertion target. It is
   not a physical first-column cap after that source label is forgotten.
2. Every exact component child of the direct \(F_r/G_r\) overlay has the
   immovable raw first-insertion load

   \[
                            h(2r)=C_{r-1}.
   \tag{0.2}
   \]

   Hence the exact raw threshold has asymptotic constant \(1/4\), not
   \(1/9\). In the normalization \(\theta=C_r/p\), a raw hard cap is
   impossible whenever

   \[
       \theta>{C_r\over C_{r-1}}
          ={2(2r-1)\over r+1}=4-{6\over r+1}.
   \tag{0.3}
   \]
3. The pair is nevertheless extensive in row distance:

   \[
       d(F_r,G_r)\ge C_r-R_{r-1}
          =\left({8\over9}+o(1)\right)C_r,
   \tag{0.4}
   \]

   where \(R_n=[z^n]\bigl(C(z)^2/(2C(z)-1)\bigr)\). This passes the
   necessary distance test from \(F_r\), but distance from the whole
   native invariant packet basin remains unaudited.
4. No July 26 theorem characterizes the full \(X/Y\) ownership overlay of
   this product conjugation. The single-transposition component laws do not
   compose to give it. Neither small size-biased components nor a giant
   component has been proved for this pair.
5. No complete parent-carrier/collar calculation proves the protected-mass
   mean hinge, and no targetwise covariance calculation proves the
   zero-margin rounding remainder. The \(1/9\) first-column matrix proves
   neither statement.

Therefore the explicit pair does not presently prove \(\mathrm{CRH}_A\).
Its first claimed physical interface already fails unless the parent lift
supplies an additional injective source-class separation. Even under that
extra separation, the full-overlay, mean-hinge, and targetwise-variance
theorems remain open. No MWB or coefficient-one implication follows.

This first-column failure alone is not a coefficient-scale no-go. A bounded
number of marked boundary columns through \(H=O(\sqrt m)\) carries only
\(O(H\operatorname{Cat}_m)=o(W)\) total global mass. A coefficient-scale
obstruction or proof must use the complete parent-collision and collar
tensor.

## 1. Literal exactness and the twist correction

Every \(\eta_r\) preserves \(D_r\). Define all lower and upper states by

\[
 X_t^{G_r}(P)=\eta_rX_t^{F_r}(\eta_rP),\qquad
 Y_t^{G_r}(P)=\eta_rY_t^{F_r}(\eta_rP).
\tag{1.1}
\]

Coordinate permutation preserves incidence and both complete ownership
ledgers. Since \(\eta_r^2=1\),

\[
 X_0^{G_r}(P)=P,
 \qquad
 X_r^{G_r}(P)=\eta_r([2r]\setminus\eta_rP)=[2r]\setminus P.
\tag{1.2}
\]

Thus every row is an ordinary length-\(r\) complement geodesic.

This is distinct from a proposed twisted slab with endpoints

\[
 O\cup P,\qquad O\cup(J\setminus\tau(P)).
\]

For the latter, the distance is \(|P\cap\tau(P)|\), so a fixed-exterior
\(r\)-step slab forces \(\tau(P)=P\). Formula (1.2) has no such twist:
the reindexing by \(\eta_rP\) is part of the definition and restores the
literal endpoint \(P^c\).

## 2. What the constant \(1/9\) actually proves

Let \(C_n=\operatorname{Cat}_n\), and define

\[
 R(z)=\sum_{n\ge0}R_nz^n
       ={1\over1-z^2C(z)^2}
       ={C(z)^2\over2C(z)-1}.
\tag{2.1}
\]

The number \(R_n\) counts Dyck words of semilength \(n\) with no singleton
primitive component. Let \({\cal F}_{r,j}\) be the canonical source
first-return class \(j\), and let \(M^{(r)}_{jk}\) count roots in
\({\cal F}_{r,j}\) whose \(\eta_r\)-image has first-return class \(k\).
Lane N proves the exact matrix

\[
 M^{(r)}_{jk}=
 \begin{cases}
  0,&j=k<r,\\[1mm]
  R_{\min(j,k)-1}C_{|j-k|-1}C_{r-\max(j,k)},
     &j\ne k,\ \max(j,k)<r,\\[1mm]
  R_{j-1}C_{r-j-1},&j<r,\ k=r,\\[1mm]
  R_{k-1}C_{r-k-1},&k<r,\ j=r,\\[1mm]
  R_{r-1},&j=k=r.
 \end{cases}
\tag{2.2}
\]

The first physical target associated with column \(k\) is

\[
 \lambda_r(k)=
 \begin{cases}
  2k+1,&k<r,\\
  2r,&k=r.
 \end{cases}
\tag{2.3}
\]

For \(r\ge3\),

\[
                         \max_{j,k}M^{(r)}_{jk}=R_{r-1},
\tag{2.4}
\]

and singularity extraction gives

\[
 {R_{r-1}\over C_r}\longrightarrow {1\over9}.
\tag{2.5}
\]

Equations (2.2)--(2.5) are exact and integral. They concern cells labelled
by \((j,k)\). A physical target is only the subset produced after the
carrier map; \(j\) is not automatically part of that subset.

Summing (2.2) over the source label gives

\[
 h_{G_r}(2k+1)=C_{k-1}C_{r-k}\quad(k<r),
 \qquad
 h_{G_r}(2r)=C_{r-1}.
\tag{2.6}
\]

Thus the \(1/9\) dispersion disappears when equal physical targets are
merged.

There is also an exact cube-wide resolved obstruction. Let

\[
 {\cal I}_r=\{P:\operatorname{fr}(P)=
                    \operatorname{fr}(\eta_rP)=r\}.
\tag{2.7}
\]

By (2.2), \(|{\cal I}_r|=R_{r-1}\). At every root in \({\cal I}_r\),
both shores insert \(2r\) first. Rooted component switching retains one of
those two rows at the same root, so every child of the entire component
cube retains at least \(R_{r-1}\) occurrences in the resolved
\((r,2r)\)-cell. Since the all-\(G_r\) child has maximum cell exactly
\(R_{r-1}\),

\[
 \min_{\text{component children }H}\ 
       \max_{j,x}h^H_{r,j}(x)=R_{r-1}.
\tag{2.8}
\]

Thus even perfect physical source separation cannot beat the \(1/9\)
threshold with this two-seed cube.

The newer coordinate-automorphism theorem proves

\[
                         \operatorname{Aut}_{S_{2r}}({\cal D}_r)
 =\langle(2i\ \ 2i+1):1\le i<r\rangle.
\tag{2.9}
\]

Consequently the all-block factor is minimax-optimal not merely in a
chosen adjacent-swap grammar, but among every coordinate conjugate of the
fixed canonical seed which remains anchored at \(D_r\). This does not
extend to arbitrary nonconjugate exact factors.

## 3. The exact physical first-column obstruction

### Theorem 3.1 (forced endpoint load)

For every anchored exact \(D_r\)-port factor \(H\),

\[
                         h_H(2r)=C_{r-1}.
\tag{3.1}
\]

Moreover \(h_H(x)\le C_{r-1}\) for every \(x\ne1\), so the raw maximum is
exactly \(C_{r-1}\).

#### Proof

In the row rooted at \(P\), let \(a(P)\) be the deletion time of coordinate
one and \(b(P)\) the insertion time of coordinate \(2r\). Every Dyck port
contains one and omits \(2r\). The number of lower states containing both
coordinates is

\[
                         (a(P)-b(P))_+,
\]

and the number of upper states containing both is

\[
                         (a(P)-b(P)+1)_+.
\]

The complete lower ledger gives

\[
 \sum_P(a(P)-b(P))_+
   =\binom{2r-2}{r-2}=(r-1)C_{r-1}.
\tag{3.2}
\]

The difference of the complete upper and lower ledgers gives

\[
 \#\{P:b(P)\le a(P)\}
 =\binom{2r-2}{r-1}-\binom{2r-2}{r-2}
 =C_{r-1}.
\tag{3.3}
\]

Only the rows counted in (3.3) contribute to (3.2), and every contribution
is at most \(r-1\). Equality in (3.2) forces every one of these rows to have

\[
                         b(P)=1,\qquad a(P)=r.
\]

These are exactly the rows inserting \(2r\) first, proving (3.1). Applying
the same upper-minus-lower pair count to \(\{1,x\}\) shows that at most
\(C_{r-1}\) roots can insert any fixed \(x\ne1\) first. \(\square\)

### Corollary 3.2 (componentwise immovability)

Let \({\cal K}_r\) be the full port-closed ownership components of the
direct \(F_r/G_r\) overlay. If \(\Delta_K^{(1)}(2r)\) is the change in the
raw first-column load at \(2r\) from switching only component \(K\), then

\[
                         \Delta_K^{(1)}(2r)=0
                         \qquad(K\in{\cal K}_r).
\tag{3.4}
\]

#### Proof

Switching one complete port-closed component gives another anchored exact
factor. Apply Theorem 3.1 before and after that switch. \(\square\)

Consequently every probability law on the component cube has mean exactly
\(C_{r-1}\) and variance zero at this raw coordinate. Against a hard
physical cap \(p\), its first-column excess is at least

\[
                         (C_{r-1}-p)_+.
\tag{3.5}
\]

The exact raw cap condition is \(p\ge C_{r-1}\), equivalently (0.3). The
resolved condition \(p\ge R_{r-1}\), asymptotically \(\theta\le9\), is
strictly weaker. In the entire interval

\[
 {C_r\over C_{r-1}}<\theta\le {C_r\over R_{r-1}},
\tag{3.6}
\]

the resolved matrix is cap-safe while every physical exact factor fails
the raw cap.

### Corollary 3.3 (the missing carrier-separation hypothesis)

Suppose the cells \((j,k)\) are pushed to physical targets by a map
\(\phi\), with unaffected background \(b(T)\). The \(1/9\) bound implies a
physical hard cap only if the actual inequalities

\[
 b(T)+\sum_{(j,k):\phi(j,k)=T}M^{(r)}_{jk}\le p
                         \qquad\hbox{for every }T
\tag{3.7}
\]

hold. Pairwise distinct images of all active cells, together with
\(b(T)\le p-R_{r-1}\), is a sufficient special case. Neither property is
proved by the Lane N first-column theorem. A common fixed exterior sends
all source labels with the same \(k\) to the same physical target and
recovers the column sums (2.6).

## 4. The pair passes the extensive row-distance test

### Theorem 4.1

One has

\[
                         d(F_r,G_r)\ge C_r-R_{r-1}.
\tag{4.1}
\]

#### Proof

The canonical first insertion on a root of first-return class \(j\) is the
even coordinate \(2j\). The first insertion in \(G_r(P)\) is odd unless
\(\eta_rP\) has class \(r\), in which case it is \(2r\). Therefore the two
rows can have the same first insertion only when both \(P\) and
\(\eta_rP\) have class \(r\). The number of such roots is the
\((r,r)\)-entry of (2.2), namely \(R_{r-1}\). Every other root has different
first edges and hence different complete rows. \(\square\)

By (2.5), (4.1) is (0.4). Thus the candidate is not a tiny perturbation
of \(F_r\) and passes the necessary endpoint-distance lower bound from
\(F_r\). This does not prove the separately required distance from the
entire native invariant packet basin; a different basin element could be
closer to \(G_r\).

This positive fact does not prove that a positive density of rows changes
\(\Theta(r)\) carrier positions; that stronger extensive-word statement
still requires a complete trajectory comparison.

## 5. What is known about the full ownership overlay

Let \(A_P\) be the complete \(X/Y\) token set of the canonical row rooted at
\(P\). The conjugate row rooted at \(P\) has token set

\[
                         B_P=\eta_rA_{\eta_rP}.
\tag{5.1}
\]

Join the two owners of every physical token and contract the common root
port edges. Its connected root blocks are \({\cal K}_r\).

### Proposition 5.1 (overlay involution and exact component action)

The map induced by \(\eta_r\) permutes \({\cal K}_r\). For every
coordinate-equivariant complete local statistic and every component
\(K\in{\cal K}_r\),

\[
 \boxed{
 \Delta_{K,q}(T)
   =\mu^F_{q,\eta_rK}(\eta_rT)-\mu^F_{q,K}(T).}
\tag{5.2}
\]

If \(\eta_rK=K\), then every \(\eta_r\)-target-orbit total is invariant
under that component switch. If \(K'=\eta_rK\ne K\), then

\[
                         \Delta_{K',q}=-\eta_{r*}\Delta_{K,q}.
\tag{5.3}
\]

#### Proof

Let \(a(Z)\) and \(b(Z)\) be the \(F_r\)- and \(G_r\)-owners of token
\(Z\). From (5.1),

\[
                         a(\eta_rZ)=\eta_rb(Z),
 \qquad
                         b(\eta_rZ)=\eta_ra(Z).
\]

Hence exchanging the two shores and applying \(\eta_r\) is an automorphism
of the uncontracted overlay; after root contraction, \(\eta_r\) permutes
the component blocks.

The new shore over physical root block \(K\) consists of the rows
\(\eta_rF_r(\eta_rP)\), \(P\in K\). Coordinate equivariance and the change
of variable \(Q=\eta_rP\) give (5.2). Stability gives the target-orbit
invariance, and applying (5.2) to \(K'=\eta_rK\) gives (5.3). \(\square\)

This proposition is the full consequence of conjugacy alone. It does not
say that every component is \(\eta_r\)-stable. A graph automorphism may
pair two different components. Thus a componentwise two-target-orbit
obstruction cannot be asserted without an actual stability theorem.

One may force stability by bundling every raw component with its
\(\eta_r\)-mate. Such intrinsic bundles are legal but may merge two
independent raw bits and increase the size-biased component moment.
\(\mathrm{CRH}_A\) rounds the actual raw port-closed components, so
bundle-level invariance is not a substitute for a raw-component
classification.

There is a sharp conditional obstruction. If every raw component is
\(\eta_r\)-stable, then for every \(\eta_r\)-invariant dual load
\(z_q(T)=z_q(\eta_rT)\),

\[
                         \langle z,\Delta_K\rangle=0
                         \qquad\hbox{for every }K.
\tag{5.4a}
\]

Hence every excess in an \(\eta_r\)-target-orbit total is frozen throughout
the cube. Nonstable component pairs are the only mechanism in this
coordinate-conjugate pair that can move such orbit-total modes. A useful
fragmentation theorem must therefore count and profile nonstable raw
components, not merely small stable bundles.

The single-transposition hierarchy for \((2\ 3)\) does not determine
\({\cal K}_r\). The overlay of \(F_r\) with the one product conjugate
\(\eta_rF_r\eta_r\) is not obtained by intersecting or multiplying the
separate single-transposition component partitions. Upper-state owner
relations can also merge lower-state orbits. No current report proves a
bound for

\[
                         \chi_r^\eta
    ={1\over C_r}\sum_{K\in{\cal K}_r}|K|^2.
\tag{5.4}
\]

Accordingly the overlay-fragmentation gate is open, not passed.

More explicitly, if

\[
 \eta_rX_t^{F_r}(P)=X_t^{F_r}(\kappa_tP),
\]

then the contracted \(X\)-suboverlay has generator edges

\[
                         P\;--\;\kappa_t\eta_rP.
\tag{5.5}
\]

Its components are the orbits of
\(\langle\kappa_t\eta_r:0\le t\le r\rangle\). The \(Y\)-owner relations
can only merge those orbits. Hence transitivity of this phase group would
prove a connected full overlay, whereas a common small block system
preserved after all \(Y\)-closures would prove fragmentation. Neither
statement is known uniformly in \(r\).

## 6. The full-profile mean hinge is a separate theorem

After first-fringe lifting, let \(\omega\) index the disjoint parent
contexts and let \(U_{\omega K,q},V_{\omega K,q}\) be the complete old and
new physical histograms of component \(K\), including every row, cyclic
start, parent carrier, and crossing collar. Let \(\ell_q\) be the unaffected
background. For marginal switch probabilities \(t_{\omega K}\), the mean
is

\[
 \bar\mu_q
 =\ell_q+\sum_{\omega,K}
    \bigl((1-t_{\omega K})U_{\omega K,q}
                   +t_{\omega K}V_{\omega K,q}\bigr).
\tag{6.1}
\]

For balanced quotas \(\beta_q\), the least possible mean hinge has the
exact dual

\[
\begin{aligned}
 \Phi_\beta^*=\max_{0\le z_q(T)\le1/c_q}\Bigg\{&
   \sum_{q,T}z_q(T)(\ell_q(T)-\beta_q(T))\\
   &+\sum_{\omega,K}
       \min\bigl(\langle z,U_{\omega K}\rangle,
                  \langle z,V_{\omega K}\rangle\bigr)
                                      \Bigg\}.
\end{aligned}
\tag{6.2}
\]

The \(1/9\) calculation determines one boundary projection of some of the
vectors in (6.2). It does not determine the other \(2r-1\) starts of the
same local rows, either opposite boundary, any parent-crossing window, or
the unaffected load. Hence it supplies no bound on (6.2).

For a standalone coordinate-equivariant profile,

\[
 z^G_{q,P}(T)=z^F_{q,\eta_rP}(\eta_rT),
 \qquad
 \mu_q^G=\eta_{r*}\mu_q^F.
\tag{6.2a}
\]

For one ambient occurrence with push-forward \(\Phi_{\omega,q}\), the
corresponding identity is only

\[
 z^G_{\omega,q,P}
   =\Phi_{\omega,q}\eta_{r*}z^F_{q,\eta_rP}.
\tag{6.2b}
\]

There is no single global Reynolds permutation unless all row/start
carrier and collar maps intertwine local \(\eta_r\) with one common
physical target permutation. That intertwining is not proved. Even when it
does hold, the fair mean only equalizes within each two-point target orbit.
If

\[
 L_O=\mu_q^F(T)+\mu_q^F(\eta_rT),
 \qquad O=\{T,\eta_rT\},
\]

then that orbit contributes exactly

\[
 \left({L_O\over2}-\beta_q(T)\right)_+
 +\left({L_O\over2}-\beta_q(\eta_rT)\right)_+
\tag{6.2c}
\]

to the unweighted mean hinge. Orbit-total excess survives. Conjugacy gives
equal endpoint energies and an involution of the cube, but it does not
orient a protected-mass descent. Unsigned
component sizes, edit counts, or Gram norms cannot replace (6.2):
antipodal cube drifts average to zero. Thus the full-profile mean hinge is
presently unproved for the explicit pair.

Even at the raw first column, fair whole-factor averaging only produces
an order-two Reynolds projection. Put

\[
                         w_j=C_{j-1}C_{r-j}.
\]

The canonical factor places \(w_j\) at \(2j\). The conjugate places
\(w_j\) at \(2j+1\) for \(j<r\), while both place \(C_{r-1}\) at \(2r\).
Thus at zero background and hard cap \(p\), the exact fair-mean raw
first-column hinge is

\[
 \boxed{
   \sum_{j<r}(w_j-2p)_+ +(C_{r-1}-p)_+.}
\tag{6.3}
\]

This identity is useful diagnostically, but it is still only one boundary
column and does not control (6.2).

There is also a useful conditional obstruction. If the full overlay is
connected, its cube contains only \(F_r\) and \(G_r\). Unless one endpoint
already has \(o(W)\) balanced hinge, every genuinely mixed mean must be
audited directly; component mixing offers no additional deterministic
states.

More sharply, if the physical quotas and background are conjugacy
invariant, the two endpoint overloads are equal. Every law on this
two-point cube then obeys

\[
                         \Phi_\beta+{\cal R}_\beta
 \ge K_\beta(F_r)=K_\beta(G_r),
\tag{6.4}
\]

because the zero-margin inequality bounds the common expected integral
weighted overload \(K_\beta\) by \(\Phi_\beta+{\cal R}_\beta\). Thus
connectedness would close this pair unless the canonical endpoint were
already good.

## 7. Targetwise variance is not implied by fragmentation

For an arbitrary law on component indicators \(\varepsilon_I\), where
\(I=(\omega,K)\), put

\[
                         \Delta_{I,q}=V_{I,q}-U_{I,q}.
\]

Then the exact targetwise variance is

\[
 \operatorname{Var}(\mu_q(T))
   =\sum_{I,J}\operatorname{Cov}(\varepsilon_I,\varepsilon_J)
                 \Delta_{I,q}(T)\Delta_{J,q}(T).
\tag{7.1}
\]

The zero-margin rounding remainder required by \(\mathrm{CRH}_A\) is

\[
 {\cal R}_\beta
 ={1\over2}\sum_{q\le H_A}{1\over c_q}
       \sum_T\sqrt{\operatorname{Var}(\mu_q(T))}.
\tag{7.2}
\]

For independent choices, (7.1) becomes

\[
 \operatorname{Var}(\mu_q(T))
 =\sum_I t_I(1-t_I)\Delta_{I,q}(T)^2.
\tag{7.3}
\]

Neither the cell maximum \(R_{r-1}\) nor the component moment
\(\chi_r^\eta\) controls the sum of square roots in (7.2). One needs
targetwise overlap or an explicit covariance-routing theorem.

If the overlay is connected and the law chooses \(G_r\) with probability
\(t\), then exactly

\[
 {\cal R}_\beta
 ={\sqrt{t(1-t)}\over2}
   \sum_{q\le H_A}{1\over c_q}
     \|\mu_q^{G_r}-\mu_q^{F_r}\|_1.
\tag{7.4}
\]

At the first column with \(t=1/2\),

\[
 \|\mu_1^{G_r}-\mu_1^{F_r}\|_1
       =2(C_r-C_{r-1}),
\]

so its contribution to (7.4), before the depth weight, is exactly

\[
                         {C_r-C_{r-1}\over2}.
\tag{7.5}
\]

Thus a connected overlay with \(t\) bounded away from zero and one has
linear rounding loss whenever the weighted physical endpoint distance is
\(\Theta(W)\). A deterministic endpoint makes (7.2) zero but then must
itself satisfy the full mean hinge. This is the exact mean/variance
dichotomy; no present Lane N theorem resolves it.

## 8. Exact proved and conditional boundary

The four requested gates are:

| Gate | Exact status |
|---|---|
| First-column \(1/9\) cap | Proved only for source-resolved cells. False as a raw physical cap without carrier separation; the exact raw maximum is \(C_{r-1}\sim C_r/4\). |
| Full-overlay fragmentation | Open for the product conjugate \(\eta_r\). Single-transposition component theorems do not compose. |
| Full-profile mean hinge | Open. The exact obligation is the physical dual (6.2); first-column quotas do not bound it. |
| Targetwise variance | Open. The exact obligation is (7.2), with covariance tensor (7.1). |

The strongest positive facts are literal exactness and the extensive row
distance (4.1). The shortest surviving pair-specific theorem is:

> **All-block physical hinge theorem \(\mathrm{ABPH}_A\) (unproved).**
> At a critical scale \(r=\Theta_A(\sqrt m)\), characterize the full
> \(X/Y\) components of \(F_r,G_r\); lift them through the actual
> first-fringe carriers; and construct one law whose mean satisfies (6.2)
> with value \(o_A(W)\) and whose covariance satisfies (7.2) with value
> \(o_A(W)\). Every use of the \(1/9\) matrix must verify the collision
> inequalities (3.7).

This is strictly narrower than constructing an arbitrary critical pair,
because \(F_r,G_r\) are explicit and already pass exactness and extensive
row distance. It is not proved, and it cannot be shortened to the
source-resolved first-column calculation. If (3.7) fails in the raw cap
range (3.6), the explicit pair is already obstructed before
\(\mathrm{ABPH}_A\).
