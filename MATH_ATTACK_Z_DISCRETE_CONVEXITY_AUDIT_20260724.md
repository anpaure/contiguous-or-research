# Independent audit: Lane Z discrete convexity

## Verdict

The main negative conclusion of the report survives adversarial audit:
standard (M)-, (M^\natural)-, and (L^\natural)-convexity do not provide
the missing fixed-window descent theorem.  The normalization, native-fibre
counterexamples, component-cube Hessian, full-depth rank-two obstruction,
augmented-Graver optimality theorem, and near-global (1/2) estimate are
mathematically valid.

The audit found no false central theorem, but it found two material scope
corrections and several self-containment corrections.

1. The explicit disconnected two-component augmented Graver packet is proved
   only when the augmented load map contains actual rank (2), equivalently
   (H\ge m-2).  Its existence in a fixed Gaussian window
   (H_A=O_A(\sqrt m)) is **unsupported**.
2. The phrase “connected components are the squarefree Gravers of (A_m)”
   is too broad without its factor-vertex qualifier.  What is proved is that
   connected ownership components are squarefree Graver elements, and that
   every squarefree Graver move feasible between two factor vertices has
   connected ownership overlay.  This does not classify non-packing-compatible
   squarefree Gravers or the full Graver basis of (A_m).

The report should also define its weighted inner product and the symbols
(d_I), state the Boolean extended-value convention for
(L^\natural)-convexity, give the explicit floor constant (\beta_q), and
qualify two statements about rank endpoints and locality.  These are recorded
below.

## 1. Normalization and overload constant

**Classification: VALID, with an explicit-constant correction.**

Write

\[
 W=c_qN_q+r_q,\qquad 0\le r_q<N_q,
\]

and put

\[
 \boxed{\beta_q=\frac{r_q(N_q-r_q)}{N_q}.}
 \tag{1.1}
\]

For (f_q=\mu_q-(W/N_q)\mathbf 1), direct expansion gives

\[
 Q_q
 =\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1)
 =\|f_q\|_2^2-\beta_q.
 \tag{1.2}
\]

Thus the half-energy normalization is exactly

\[
 \Psi_H(F)
 =\frac12\sum_{q\le H}\frac{Q_q(F)}{c_q}
 =\frac12\sum_{q\le H}
   \frac{\|f_q\|_2^2-\beta_q}{c_q}.
 \tag{1.3}
\]

The factor (1/2) and every (c_q^{-1}) are correct.

For completeness, set (d_S=\mu_q(S)-c_q) and

\[
 D^-_q=\sum_S(-d_S)_+,
 \qquad
 D^+_q=\sum_S(d_S-1)_+.
\]

The minimum overload against a floor/ceiling-balanced quota vector is
(O_q=\max\{D^-_q,D^+_q\}).  The pointwise inequality

\[
 \frac{d(d-1)}2\ge (-d)_+ +(d-1)_+
 \qquad(d\in\mathbb Z)
\]

therefore yields

\[
 \frac{Q_q}{2}\ge D^-_q+D^+_q\ge O_q.
 \tag{1.4}
\]

Consequently

\[
 \Psi_H(F)\ge\sum_{q\le H}\frac{O_q(F)}{c_q},
\]

so (\Psi_{H_A}=o(W)) is indeed a sufficient fixed-window MWB target.

The report's statement that (\beta_q) is factor-independent is correct,
but an exact-constants report should include (1.1).

## 2. Theorem Z1: native exact-factor fibre

### 2.1 Nontriviality and binary cardinality

**Classification: VALID.**

Every nonnegative integral solution of (A_mx=\mathbf1) is binary: if
(x_C\ge2), every middle interval of (C) already has load at least two.
Summing the (W) middle-row equations gives

\[
 n\sum_Cx_C=W,
 \qquad
 \sum_Cx_C=\frac Wn=\operatorname{Cat}_m.
 \tag{2.1}
\]

The number of unoriented cyclic orders is

\[
 |\mathscr W_m|=\frac{(n-1)!}{2}=\frac{(2m)!}{2},
\]

and

\[
 \frac{|\mathscr W_m|}{\operatorname{Cat}_m}
 =\frac{m!(m+1)!}{2}>1
 \qquad(m\ge2).
 \tag{2.2}
\]

Exact factors exist by the frozen MSW theorem.  If one factor were invariant
under every coordinate relabeling, transitivity of (S_n) on
(\mathscr W_m) would force its binary indicator to be constant on every
column, hence empty or full, contradicting (2.1)--(2.2).  A distinct
relabelled factor therefore exists for every (m\ge2).

### 2.2 Reconstruction from middle intervals

**Classification: VALID.**

If (d_C(u,v)\in\{1,\ldots,m\}) is the cyclic distance between two labels in
an odd (n=2m+1) cycle, exactly

\[
 m-d_C(u,v)
 \tag{2.3}
\]

length-(m) cyclic intervals contain both labels.  Equality of two middle
incidence columns therefore gives equality of every pairwise cyclic distance.
The pairs of distance one recover the cycle adjacency graph, so the cycle is
determined up to rotation and reversal.  Hence

\[
 A_m(e_D-e_C)=0\quad\Longrightarrow\quad C=D
 \quad\text{in }\mathscr W_m.
 \tag{2.4}
\]

There is no nonzero one-column exchange inside the exact-factor fibre.

### 2.3 (M)-, (M^\natural)-, and (L^\natural)-failure

**Classification: VALID.**

Take distinct factors (x,y) and (C\in\operatorname{supp}(x-y)).  An
(M)-exchange would require some
(D\in\operatorname{supp}(y-x)) for which
(x-e_C+e_D) is feasible, contrary to (2.4).  In the
(M^\natural)-exchange axiom, the unpaired branch changes the fixed
cardinality (2.1), while the paired branch is the same impossible exchange.

For the (L^\natural) claim, use the standard extended-value convention:
the function is finite on the fibre and (+\infty) outside it.  If

\[
 k=|\operatorname{supp}(x-y)_+|\ge1,
\]

then

\[
 \left\lfloor\frac{x+y}{2}\right\rfloor=x\wedge y,
 \qquad
 \left\lceil\frac{x+y}{2}\right\rceil=x\vee y
\]

have respective cardinalities
(\operatorname{Cat}_m-k) and (\operatorname{Cat}_m+k).  Neither belongs to
the fibre, so the discrete midpoint closure required of an
(L^\natural)-convex domain fails.

Thus Theorem Z1 is correct for every (m\ge2).

## 3. Rank-load images

**Classification: VALID, with endpoint and quantifier corrections.**

At an actual set rank (1\le r\le n-1), every selected wreath contributes
(n) distinct cyclic (r)-intervals and contains each point in exactly
(r) of them.  Hence every factor load satisfies

\[
 \sum_S\mu_r(S)=W,
 \qquad
 U_r\mu_r=r\operatorname{Cat}_m\,\mathbf1.
 \tag{3.1}
\]

If (\mu-e_S+e_T) were another rank-(r) load, (3.1) would force
(\mathbf1_S=\mathbf1_T), hence (S=T).  Every nonsingleton rank-load image
therefore fails (M)- and (M^\natural)-exchange.  In a joint multirank
image, an exchange between different rank blocks violates the separate
total (W) in each block, while an exchange within one block is excluded by
the same point-margin argument.

The generic phrase “at actual set rank (r)” should either be restricted to
(1\le r\le n-1), as above, or accompanied by a separate pointed-multiplicity
convention at (r=0,n).  This does not affect any depth
(q\le m-1).

For (m\ge3), the depth-one image is nonsingleton.  Otherwise its unique
integral load vector would be fixed by (S_n) and hence constant on the
((m-1))-sets, with coordinate

\[
 \frac{W}{N_1}=\frac{m+2}{m},
\]

which is nonintegral for (m\ge3).  Thus every joint Gaussian window
containing depth one is nonsingleton.  The report's phrase “this obstruction
applies directly in every fixed Gaussian window” should be read in this joint,
asymptotic sense; it does not prove that every individual depth-(q) image is
nonsingleton.  For (m=2), the depth-one image is constant, consistently with
the stated (m\ge3) range.

## 4. Theorem Z2: component-cube calculus

### 4.1 Definitions omitted from the report

**Classification: CORRECTED PRESENTATION; formulas valid.**

The report must define

\[
 \langle a,b\rangle_H
 :=\sum_{q\le H}\frac{\langle a_q,b_q\rangle_2}{c_q},
 \qquad
 \|a\|_H^2=\langle a,a\rangle_H,
 \tag{4.1}
\]

and must regard (f=(f_q)_{q\le H}).  For a component union (I), put

\[
 v_I=\sum_{K\in I}v_K.
\]

Then

\[
 \Psi_H(F_I)-\Psi_H(F)
 =\langle f,v_I\rangle_H+\frac12\|v_I\|_H^2.
 \tag{4.2}
\]

Expansion of (4.2) gives exactly the displayed formula in Z2, and

\[
 \Delta_K\Delta_L\Psi_H=\langle v_K,v_L\rangle_H.
 \tag{4.3}
\]

Every component union is a genuine factor: inside an ownership-overlay
component, the old and new sides own exactly the same middle sets.

### 4.2 (L^\natural)-criterion

**Classification: VALID, with the Boolean convention stated explicitly.**

On the Boolean component cube, extended by (+\infty) outside the cube,
(L^\natural)-convexity is equivalent to submodularity because the discrete
midpoint pair is (x\wedge y,x\vee y).  A quadratic pseudo-Boolean function
is submodular exactly when all its mixed coefficients are nonpositive.
Therefore

\[
 \Psi_H|_{\{0,1\}^{\mathcal K}}
 \text{ is }L^\natural\text{-convex}
 \iff
 \langle v_K,v_L\rangle_H\le0
 \quad(K\ne L).
 \tag{4.4}
\]

No diagonal condition is missing.

### 4.3 Transposition identity and sign

**Classification: VALID, but (d_I) is undefined in the report.**

For (G=\tau F), let (a_K) be the old-side component load and define

\[
 d_K=a_K-\tau a_K=-v_K,
 \qquad
 d_I=\sum_{K\in I}d_K,
 \qquad
 d=f-\tau f.
 \tag{4.5}
\]

Component equivariance gives that every (d_K) is (\tau)-anti-invariant.
Consequently

\[
 f(F_I)=\frac{f+\tau f}{2}+\frac{d-2d_I}{2},
\]

where the two summands are orthogonal.  Hence

\[
 \boxed{
 \Psi_H(F_I)-\Psi_H(F)
 =-\frac12\langle d_I,d_{I^c}\rangle_H
 =-\frac12\langle v_I,v_{I^c}\rangle_H.
 }
 \tag{4.6}
\]

A positive component-correlation cut therefore gives strict descent and
contains at least one positive Gram entry, contradicting (4.4).  Conversely,
if all pairwise Gram entries are nonpositive, every cut sum is nonpositive
and (F) is minimum on the entire transposition cube.  The report's
“wrong-sign” conclusion is exact.

The direct (M^\natural) transfer identity

\[
 \Psi_H(\mathbf1)+\Psi_H(\mathbf0)
 -\Psi_H(\mathbf1-e_K)-\Psi_H(e_K)
 =\sum_{L\ne K}\langle v_K,v_L\rangle_H
 \tag{4.7}
\]

is also correct.  Linear and diagonal terms cancel.  There is no universal
sign.

## 5. Theorem Z3: genuine MSW rank-two obstruction

### 5.1 Component realization and effects

**Classification: VALID.**

For the MSW factor and (\tau=(2\,3)), the exact component hierarchy gives

\[
 s=\operatorname{Cat}_{m-2}
 \tag{5.1}
\]

independently switchable (j=0), two-for-two ownership components indexed by
(R\in\mathcal D_{m-2}).  The universal four-letter trade formula gives their
actual-rank-two effects

\[
 \delta_R=B_2z_R,
 \qquad
 \|\delta_R\|_2^2=8.
 \tag{5.2}
\]

The eight nonzero coordinates in (5.2) are distinct and have coefficients
(\pm1).  For the one-rank floor energy, the Hessian is the positive scalar
(c_{m-2}^{-1}) times the ordinary Gram matrix.  That scalar does not affect
any sign conclusion.

### 5.2 The (m\ge9) threshold

**Classification: VALID; constants exact.**

Let

\[
 D=\binom{2m+1}{2}=m(2m+1).
\]

At (m=9),

\[
 s=\operatorname{Cat}_7=429,
 \qquad
 D=171,
 \qquad
 2D=342<429.
 \tag{5.3}
\]

Moreover

\[
 \frac{s_{m+1}}{s_m}=\frac{4m-6}{m},
 \qquad
 \frac{D_{m+1}}{D_m}
 =\frac{(m+1)(2m+3)}{m(2m+1)}.
 \tag{5.4}
\]

The first ratio exceeds the second exactly when

\[
 6m^2-13m-9>0,
\]

which already holds for (m\ge3).  Hence (s>2D) persists for every
(m\ge9).

### 5.3 Obtuse-vector lemma

**Classification: VALID; the report's proof is compressed.**

Normalize nonzero vectors (w_1,\ldots,w_s\in\mathbb R^D), let (G) be their
Gram matrix, and suppose (G_{ij}\le0) for (i\ne j).  Then

\[
 A=I-G
\]

is symmetric and entrywise nonnegative.  Since (G\succeq0),
(\lambda_{\max}(A)=1-\lambda_{\min}(G)\le1).  Perron--Frobenius for the
symmetric nonnegative matrix (A) gives

\[
 \rho(A)=\lambda_{\max}(A)\le1,
\]

so every eigenvalue of (A) lies in ([-1,1]), and every eigenvalue of
(G=I-A) lies in ([0,2]).  Thus

\[
 s=\operatorname{tr}G
 \le2\operatorname{rank}G
 \le2D.
 \tag{5.5}
\]

This proves the bound used in Z3.

### 5.4 No orientation and (M^\natural)-violation

**Classification: VALID.**

Reorienting one component coordinate replaces (\delta_R) by
(-\delta_R).  If some orientation made the component-cube energy
(L^\natural)-convex, all signed effects would have pairwise nonpositive
inner products, contradicting (5.3)--(5.5).  Thus every orientation fails.

Since (s>D), the effects cannot be mutually orthogonal.  Choose a
nonorthogonal pair and flip one orientation so its inner product is negative.
Fixing all other bits gives an exact two-component face with

\[
 E_{11}+E_{00}-E_{10}-E_{01}
 =c_{m-2}^{-1}
   \langle\pm\delta_R,\pm\delta_{R'}\rangle_2<0.
 \tag{5.6}
\]

For (x=11,y=00), the (M^\natural)-exchange axiom has no negative-support
partner and requires the left side of (5.6) to be nonnegative.  Hence this is
a genuine (M^\natural)-violation.

The report correctly states the decisive scope limitation: actual rank two is
depth (q=m-2), outside every fixed Gaussian window for large (m).  Z3 does
not prove fixed-window component-cube nonconvexity or produce a nonglobal
fixed-window local minimum.

## 6. Theorem Z4: augmented Graver optimality

### 6.1 Matrix, box, and separable objective

**Classification: VALID.**

The augmented matrix has the correct sign:

\[
 \widehat A_H=
 \begin{pmatrix}
 A_m&0\\
 B_H&-I
 \end{pmatrix},
 \qquad
 \widehat A_H(x,u)=\binom{\mathbf1}{0}
\]

is exactly

\[
 A_mx=\mathbf1,
 \qquad
 u=B_Hx.
 \tag{6.1}
\]

Integer bounds (0\le x\le1) make (x) a factor vertex, and
(0\le u\le W\mathbf1) safely contain every load.  The upper bound
(x\le1) is redundant once (x\ge0) and (A_mx=\mathbf1), but harmless;
nonnegativity is the essential condition excluding the unrestricted signed
fibre.

On this fibre,

\[
 \Psi_H(x,u)=\sum_{q\le H}\sum_S\phi_q(u_{q,S}),
 \qquad
 \phi_q(t)=\frac{(t-c_q)(t-c_q-1)}{2c_q},
 \tag{6.2}
\]

up to the already included factor-independent normalization, and

\[
 \Delta^2\phi_q(t)=\frac1{c_q}>0.
 \tag{6.3}
\]

The objective is separable discrete convex in (u), with zero coordinate
functions in (x).

### 6.2 Graver local-to-global proof

**Classification: VALID.**

Let (\widehat x=(x,u)) be feasible and suppose a better feasible point
(\widehat y) exists.  A conformal Graver decomposition gives

\[
 \widehat y-\widehat x=g^1+\cdots+g^t,
 \qquad
 g^j\in\mathcal G(\widehat A_H).
 \tag{6.4}
\]

Each (\widehat x+g^j) lies coordinatewise between the two feasible
endpoints and is therefore box-feasible.  Sign-compatible separable convexity
gives

\[
 \Psi_H\!\left(\widehat x+\sum_jg^j\right)-\Psi_H(\widehat x)
 \ge
 \sum_j\bigl(\Psi_H(\widehat x+g^j)-\Psi_H(\widehat x)\bigr).
 \tag{6.5}
\]

The left side is negative, so at least one Graver summand improves.  The
converse is immediate.  Thus a feasible point is globally optimal if and only
if it admits no feasible improving Graver augmentation.

The report should use (\widehat x,\widehat y), rather than overloading (x,y)
for augmented points, but the proof direction is correct.

If (g=(g_x,g_u)\ne0) lies in the augmented kernel, then (g_x\ne0), since
(g_x=0) would force (g_u=0).  If
(\widehat x+\lambda g) is feasible from a binary point, some nonzero integer
(g_{x,i}) must satisfy

\[
 |\lambda g_{x,i}|\le1.
\]

Therefore every feasible nonzero scale has exactly

\[
 \boxed{\lambda=1.}
 \tag{6.6}
\]

This does not assert that every augmented Graver element is feasible at scale
one; it only classifies a scale once feasibility is assumed.

## 7. Packet characterization

### 7.1 Exact factor-vertex theorem

**Classification: VALID.**

Cancel common wreaths between two factor vertices and let (K) range over
the connected components of their ownership overlay.  For a component union
(J), put

\[
 z_J=\sum_{K\in J}z_K,
 \qquad
 v_J=B_Hz_J.
\]

Then

\[
 \boxed{
 (z_J,v_J)\in\mathcal G(\widehat A_H)
 \iff
 \nexists\,\varnothing\ne I\subsetneq J
 \text{ with }v_I\sqsubseteq v_J.
 }
 \tag{7.1}
\]

Indeed, the (x)-part of any conformal augmented kernel submove is a
squarefree vector conformal to (z_J).  The middle ownership equations force
its selected old and new wreaths to form a union (I) of whole overlay
components.  Its load part is then necessarily (v_I=B_Hz_I).  Conversely,
such an (I) is a conformal proper kernel submove exactly when
(v_I\sqsubseteq v_J).

Every connected ownership component therefore gives an augmented Graver
element, even when its restricted load effect is zero.

### 7.2 Scope correction for squarefree Gravers

**Classification: CORRECTED.**

The report should replace

> connected components are the squarefree Gravers of (A_m)

by

> Connected ownership components are squarefree Graver elements of (A_m).
> Conversely, every squarefree Graver move feasible between two factor
> vertices has connected ownership overlay.

This is exactly the support-feasible theorem proved by the trade/Markov
analysis.  It does not classify non-packing-compatible squarefree Gravers or
the full Graver basis of (A_m).

### 7.3 Disconnected cancellation packets

**Classification: VALID AT FULL DEPTH; UNSUPPORTED IN FIXED WINDOWS.**

For (m\ge9), choose two rank-two MSW effects with nonzero inner product and
orient one so that their inner product is negative.  Since the effects have
coefficients (\pm1), a negative inner product supplies at least one rank-two
coordinate on which their signs are opposite.  At that coordinate their sum
cancels to zero.  Neither individual effect is conformal to the sum, so the
two-component union satisfies (7.1) and is a genuine disconnected augmented
Graver packet.

This argument requires the augmented map to contain actual rank two.  For the
prefix convention (B_H=(B_{m-1},\ldots,B_{m-H})), the required hypothesis is

\[
 \boxed{H\ge m-2.}
 \tag{7.2}
\]

It proves existential full-depth cancellation-coupled packets.  It does not
prove a disconnected augmented Graver packet when
(H=H_A=O_A(\sqrt m)).  Any reading of Section 5 as a fixed-window packet
theorem is unsupported.  The final summary's phrase “full-depth rank-2” has
the correct scope and should also be inserted beside the packet claim itself.

## 8. Near-global component estimate

### 8.1 Exact identity and constant

**Classification: VALID.**

For the (F)-versus-(G) overlay, define

\[
 a_K=\Psi_H(F_K)-\Psi_H(F)
 =\langle f,v_K\rangle_H+\frac12\|v_K\|_H^2,
 \qquad
 v=\sum_Kv_K.
\]

Exact expansion gives the stronger identity

\[
 \boxed{
 \Psi_H(F)-\Psi_H(G)
 =\frac12\left(
   \sum_K\|v_K\|_H^2-\|v\|_H^2
   \right)
 -\sum_Ka_K.
 }
 \tag{8.1}
\]

If every individual component is nonimproving, (a_K\ge0), so

\[
 \boxed{
 \Psi_H(F)-\Psi_H(G)
 \le\frac12\left(
   \sum_K\|v_K\|_H^2-\|v\|_H^2
   \right)
 \le\frac12\sum_K\|v_K\|_H^2.
 }
 \tag{8.2}
\]

No floor term is missing: (\beta_q) is factor-independent.  The coefficient
(1/2) is exactly the coefficient forced by the half-energy normalization;
for (2\Psi_H) it becomes (1).  If “exact” is intended to claim an attained
best constant within genuine exact-factor fibres, no such sharpness witness is
given.  The algebraic normalization claim itself is valid.

### 8.2 Locality quantifier

**Classification: CORRECTED WORDING.**

For one specified comparator (G), (8.2) requires nonimprovement only for the
connected components of the (F)-versus-(G) overlay.  A natural
comparator-independent sufficient hypothesis is that (F) be nonimproving
under every factor-feasible connected ownership-component move.  Therefore
the report's phrase “locality must hold against every feasible connected
component move” is stronger than literal necessity for one chosen (G), but
is correct as a uniform sufficient condition for comparison with an unknown
global minimizer.

Components of one transposition overlay are insufficient for comparison with
an arbitrary global minimizer.  Moreover connected-component locality is not
the same as augmented-Graver locality: exact global optimality requires
checking the cancellation-coupled packets characterized by (7.1).

No cited theorem bounds the variance residue in (8.2) by (o(W)).  Section 6
is therefore a conditional near-global inequality, not a proof that
component-local minima are near-global.

## 9. Corrected claim inventory

### Valid

- The exact normalization (1.2)--(1.4) and the half-energy constant.
- Nontriviality of the exact-factor fibre for every (m\ge2).
- Reconstruction of an unoriented cyclic order from its middle intervals.
- Failure of native-coordinate (M)-, (M^\natural)-, and
  (L^\natural)-convexity.
- Failure of (M/M^\natural)-exchange on every nonsingleton rank-load or
  joint multirank image in the stated rank range.
- Nonsingleton character of the joint fixed window via depth one for (m\ge3).
- Exact component-cube Hessian and the transposition Max-Cut sign identity.
- The (s=\operatorname{Cat}_{m-2}), norm-eight MSW rank-two component
  family.
- The (m\ge9) no-orientation (L^\natural) obstruction and an oriented
  two-component (M^\natural) violation.
- The augmented positive fibre, Graver local-to-global theorem, and
  feasible-scale conclusion (\lambda=1).
- The factor-vertex packet characterization (7.1).
- Existence of disconnected cancellation-minimal augmented packets when the
  augmented map includes rank two.
- The exact near-global identity (8.1) and bound (8.2).
- The conclusion that none of these results proves or disproves the
  fixed-window positive-cut/local-minimum lemma (LM_A).

### Corrected

- Use the explicit (\beta_q=r_q(N_q-r_q)/N_q).
- Restrict the generic distinct-interval rank formula to (1\le r\le n-1),
  or specify an endpoint multiplicity convention.
- Interpret “every Gaussian window” as the joint window containing depth one,
  for sufficiently large (m).
- Define (\langle\cdot,\cdot\rangle_H), (f), (v_I), and (d_I).
- State the extended-value Boolean-cube convention for (L^\natural).
- Restrict the squarefree-Graver converse to moves feasible between factor
  vertices.
- Add (H\ge m-2) to the explicit two-component augmented-packet claim.
- Interpret “every connected move is necessary” as a uniform sufficient
  locality condition, not literal necessity for one fixed comparator.
- Interpret the (1/2) constant as an exact normalization coefficient unless
  a genuine factor-realized sharpness witness is separately supplied.

### Unsupported

- Existence of a disconnected cancellation-coupled augmented Graver packet
  inside a fixed Gaussian window (H_A=O_A(\sqrt m)).  The supplied example is
  a depth-(m-2), actual-rank-two construction only.
- Any (o(W)) bound on the component variance in (8.2).
- Any conclusion that a connected-component local minimum is globally or
  (o(W))-nearly optimal without such a variance bound.
- Any implication to labelled common-owner synchronization.

## 10. Final fixed-window assessment

The native exact-factor domain is genuinely outside the standard
(M/M^\natural/L^\natural) classes, and the weighted Gram calculation shows
why (L^\natural)-submodularity has the wrong sign for the desired positive
cut.  Augmenting by the load variables restores the correct general
separable-convex local-to-global theorem, but its Graver moves are governed by
cancellation-minimal packets rather than individual ownership components.

The only proved disconnected packet currently lies at depth (m-2), so it
does not settle the geometry of the fixed Gaussian window.  Likewise, the
near-global component estimate stops at an uncontrolled variance residue.
Accordingly the report's negative verdict is correct, but the surviving
fixed-window question is unchanged:

\[
 \boxed{
 \text{Does every transposition-cut local minimum have }
 \Psi_{H_A}(F)=O_A(H_A\operatorname{Cat}_m)?
 }
\]

This remains unsupported.  The audit does not produce either a proof or a
counterexample to (LM_A), MWB, or the contiguous-OR conjecture.
