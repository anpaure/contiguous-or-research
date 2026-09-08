# Proof audit: one-defect mountain rotor, cross-level carry, and nonoverlap corners

Date: 2026-07-25

Method: proof-level mathematics only. No computation, search, or external
input.

Audited notes:

1. `MATH_ATTACK_H_CRITICAL_ONE_DEFECT_ROTOR_AND_CARRY_20260725.md`;
2. `MATH_ATTACK_PBBS_NONOVERLAP_CORNER_EDGE_COLLISION_20260725.md`.

## 0. Verdict

The principal new claims in both notes are sound, subject to the scope they
state.  In particular:

* the exact mountain inverse-fibre rotor and the criterion \(z_0=0\) are
  correct;
* the \(y_p\ge2\) capacity tail is smaller by the claimed factor;
* the persistent-labelled full-rotor carry is exactly \(+2k\);
* the phase-union packing inequality is correct but leaves its advertised
  transported-union estimate unproved;
* the nonoverlap phase lattice, minimal-corner sector charges, suffix tail,
  and sparse-corner conclusion are correct;
* the corner theorem does not control persistent overlap or the sparse
  cross-interval residual.

The notes do **not** combine to prove the critical little-oh.  They reduce
the actual positive-boundary critical sector to two compatible residual
descriptions:

1. low-overlap transported phase sets above the terminal rotor;
2. persistent-overlap returns or returns whose nonoverlap atlas has only
   \(o(s)\) irreducible corners.

The buffered genuine return family lies in precisely this residual, so it
does not contradict either theorem and shows that the residual is nonempty
in actual PBBS chronology.

## 1. Audit of the terminal capacity deletion

Write

\[
 t_p(1/4)=(p+1)^{-2},
 \qquad b=2q-p+1.
\]

For \(p\ge\varepsilon\sqrt r\), \(s\le A\sqrt r\), one has
\(b=O_{A,\varepsilon}(p)\).  The negative-binomial terminal variable
satisfies

\[
 \Pr(Y\ge2)
 \le \frac{b(b+1)t_p^2}{2(1-t_p)^2}
 =O_{A,\varepsilon}(p^{-2}).
\]

The unconditioned critical partition factor is \(O(p^{-3})\).  Retaining
one independent \(1/Q_{p-1}\) first-passage factor gives the additional
largest-atom factor \(O(p^{-2})\), while a tilt

\[
 z_p=\frac14(1+\kappa/p^2)
\]

below the first continuant singularity gives
\(e^{-c(r-s)/p^2}\).  Thus the stated cell estimate

\[
 [z^{r-s}]\mathscr F_{\ge2}
 \le C4^r p^{-7}e^{-cr/p^2}
\]

has the correct powers.  Summing over \(O_A(r)\) pairs \((s,p)\) with
\(p\ge\varepsilon\sqrt r\) gives

\[
 O_{A,\varepsilon}(4^r/r^{5/2}).
\]

Likewise, the cell bound proportional to \(b/p^7\), summed over
\(b<\delta p\), gives

\[
 O_{A,\varepsilon}(\delta^2 4^r/r^2)
 +O_{A,arepsilon}(4^r/r^{5/2}).
\]

These are capacity-envelope statements, not counts of actual canonical
returns; the note states this distinction correctly.  Together with the
previous two-limit deletion of \(p=o(\sqrt r)\), they legitimately reduce
the critical envelope to

\[
 p,q,b\asymp\sqrt r,
 \qquad y_p=1.
\]

## 2. Exact audit of the mountain rotor

Let \(K=2q+1\).  With the note's slot ordering, direct first-maximum block
rotation gives

\[
 z'_0=z_{K-1},
 \qquad z'_i=z_{i-1}\quad(1\le i<K).
\]

The displayed formulas

\[
 d(D)=1+2z_0,
 \qquad
 \delta(D)=q+1+2\sum_{i=1}^qz_i
\]

are consistent with that ordering.  Over \(q+1\) quotient phases,

\[
 \sum_{j=0}^{q}d(\tau^jD)
 =q+1+2\left(z_0+\sum_{i=q+1}^{2q}z_i\right),
\]

whereas

\[
 \delta(\tau^{q+1}D)
 =q+1+2\sum_{i=q+1}^{2q}z_i.
\]

Therefore zero winding holds exactly when \(z_0=0\).  Every lift has
height \(q+1\), and its physical circumference is
\(2q+2y+3>2q+3\); the height-gap theorem then makes this return first and
consecutive.  The endpoint-excess computation is also exact:

\[
 \delta(D)+\delta(\tau^{q+1}D)=2(q+1+y)
\]

when \(z_0=0\).

For \(y=1\), the explicit \(A_i,B_i\) list has \(K\) elements, and the
stated cycle and \((\delta,d)\)-table agree with the general rotor formula.
Exactly the unit vector in the exposed \(z_0\)-slot is bad.  Consequently a
block of \(p\) terminal fan equations survives in exactly

\[
 K-p=2q+1-p=b
\]

phases.  This verifies the main actual-PBBS claim: the terminal capacity
envelope is attained and supplies no strict saving.

The statement that the quotient packing of the terminal duration-\((q+1)\)
returns on this \(K\)-cycle is one is correct because

\[
 2(q+1)>K.
\]

This packing fact is local to the terminal rotor; it does not bound the
packing of outer returns lying in different inverse towers.

## 3. Two blocks and the first carry

For two length-\(j\) cyclic slot blocks displaced by \(\rho_j\), their
union has size

\[
 u_j=2j-(j-\rho_j)_+-(j-(N_j-\rho_j))_+.
\]

This remains correct when the two overlaps occur on both sides of the
circle.  Stars and bars after fixing the union gives

\[
 \binom{r_{j-1}+r_{j+1}-u_j}{2r_j-u_j},
\]

and replacing \(u_j=N_j\) by \(N_j-1\) correctly records that the total
mass determines the final coordinate.  Multiplication down a fixed inverse
tower is a valid conditional upper bound; incompatible slot values can only
decrease it.

The local-time identity follows by subtracting the same persistent-slot
spacing equation at the two phases.  It is an exact extra equation, although
the note does not claim a global count from it.

For the carry lemma, a persistent-labelled return of all recorded bits and
relative gaps forces all \(N_j\) particles to have the same displacement.
There are \(2L\) one-step selections in \(L\) quotient moves, so the common
selection count is \(2L/N_j\).  On \(M_q\), the persistent selected label
advances by \(q\) modulo \(2q+1\), hence one full \(K\)-phase quotient lap
selects every particle exactly twice.  The induced outer carry is therefore

\[
 \xi_{p-1}(T+kK)-\xi_{p-1}(T)
 \equiv2k\pmod {N_{p-1}}.
\]

The hypotheses matter: this formula applies to full persistent-labelled
rotor laps, not to an arbitrary phase displacement.  Since the nearest
edge-disjoint outer starts need only one or two such laps, the carry adds
only \(O(1)\) upper slots and gives no uniform vanishing factor.  The note
states this limitation correctly.

## 4. Phase-union theorem and exact residual

Transporting every actual phase set

\[
 \mathcal R_x\subseteq\mathcal T_x
\]

to \(\mathcal T_0\) gives \(\mathcal A_x=\tau^{-x}\mathcal R_x\).  For a
fixed \(E\in\mathcal T_0\), its memberships correspond to length-\(s\)
return intervals on one top quotient orbit whose starts lie in a phase span
of length \(b-1<2s\).  At most two can be pairwise edge-disjoint.  This
proves

\[
 \operatorname{Pack}\left(\bigcup_{x\in I}\mathcal R_x\right)
 \le2\left|\bigcup_{x\in I}\mathcal A_x\right|.
\]

The statement remains valid on a short top cycle: if a trace wraps, its
internal edge use only reduces the number of mutually edge-disjoint choices.

If the transported sets repeat with literal period \(d\), each distinct set
occurs at least \(\lfloor b/d\rfloor\) times, giving the claimed
\(4d/b\) relative bound.  This is genuinely conditional on equality of the
sets, not merely equality of their sizes or terminal rotor states.

Thus the unproved transported-union estimate

\[
 \sum_{\text{critical fibres}}
 \left|\bigcup_{x\in I}\mathcal A_x\right|
 =o_A(4^r/r^2)                                    \tag{4.1}
\]

is a sound sufficient residual.  The rotor and carry results do not prove
(4.1).

## 5. Audit of the nonoverlap phase lattice

With \(t=a\), \(u=s-b-1\), the chronology quantities reduce exactly to

\[
 B_{t,u}=a+b+X_a+Y_b,
 \qquad S_{t,u}=a+b.
\]

The free-monoid dichotomy therefore yields

\[
 X_a+Y_b\ge\Lambda
\]

in the nonoverlap branch and

\[
 X_a+Y_b\le\Lambda-2(a+b)
\]

in the overlap branch.  Monotonicity makes the nonoverlap set an upper
ideal.

At a minimal corner \((a,b)\), subtracting the overlap inequality at an
available predecessor gives

\[
 a>0\Rightarrow |T_{a-1}|\ge2(a+b)-2,
\]

\[
 b>0\Rightarrow |S_{s-b}|\ge2(a+b)-2.
\]

The word cancellations producing the stronger shield factorizations are
consistent with the tail cocycle, and the identified blocks are actual
first-maximum suffix sectors of \(\phi D_{a-1}\) or \(D_{s-b}\).

## 6. Suffix tail and corner charging

The first-highest-component decomposition gives

\[
 b_{m,j}=\sum_hA_{m-j,h}C_h(j).
\]

For \(j\le m/2\), the Catalan convolution bound sums to
\(O(B_mJ^{-1/2})\).  For \(j>m/2\), writing \(n=m-j\), the cap
\(h\le n\) gives

\[
 b_{m,m-n}\le B_nC_n(m-n).
\]

The path-spectrum estimate for \(n\le\sqrt m\), together with the ordinary
Catalan bound for \(n>\sqrt m\), indeed sums to \(O(B_mm^{-1/4})\).
Therefore

\[
 \mathcal T_m(L)
 \le CB_m(L^{-1/2}+m^{-1/4})
\]

is valid uniformly.

The two-coloured corner charge is injective: distinct corners of one return
have distinct relevant phase coordinates, different selected returns have
disjoint quotient supports, and the two colours separate the exceptional
vertical corner.  Hence

\[
 \sum_{I\in\mathcal P}\kappa_R(I)
 \le2\mathcal T_m(2R-1).
\]

At \(R\asymp\sqrt m\), this is \(O(B_mm^{-1/4})\).  Dividing by a positive
density of \(s\asymp\sqrt m\) corners gives
\(O(B_mm^{-3/4})=o(B_m/\sqrt m)\), exactly as claimed.

The passage from this fixed-density statement to sparse average corner
density is also valid: for fixed \(\rho>0\), the small corners contribute at
most \(\rho s+O(1)\) per return, while the macroscopic-corner total is
\(O_\rho(B_mm^{-1/4})\).  Under a critical-order lower bound on the packing,
divide first by \(\sum s(I)=\Omega(B_m)\), let \(m\to\infty\), and then let
\(\rho\downarrow0\).

## 7. Combination and buffered-family stress test

The two audited reductions are compatible but do not close each other.

* The rotor note compares **different outer starts** above one terminal
  inverse fibre and asks for small transported union (4.1).
* The corner note studies the complete phase-pair atlas **inside one outer
  return** and proves that a critical packing must have persistent overlap or
  only \(o(s)\) irreducible nonoverlap corridors.

No theorem in either note converts low transported phase multiplicity into
many macroscopic internal corners, or converts sparse internal corners into
periodicity of the transported sets.  Such an implication would be the new
cross-interval incidence theorem still required.

The buffered family

\[
 D_{s,p,h}(F)=
 1^{s-p+1}0^p1^{2p-1}0^{s-h}F0^h,
 \qquad \operatorname{ht}(F)\le h\le p-2,
\]

is a direct stress test.  It has

\[
 y_p=1,
 \qquad \lambda=p>0,
 \qquad p,q,b\asymp\sqrt r
\]

in fixed critical ratios, and all positive boundary is created above the
terminal rotor.  Its explicit first-return chronology has only two
exceptional **primal suffix-charge** phases.  This does not by itself
determine the dual blocks or its exact corner set, but it is fully compatible
with the sparse-shield/persistent-overlap residual and is not removed by the
proved positive-density-corner estimate.  The family is only
\(\exp[-\Theta(\sqrt r)]\) of the ambient Catalan layer, so it does not
disprove the desired little-oh, but it confirms that the residual contains
genuine, internally Catalan-complex PBBS returns.

## 8. Correct current boundary

Proved:

1. only \(y_p=1\), \(b\asymp p\) remains capacity-critical;
2. its terminal rotor and all-zero fan are genuine PBBS chronology;
3. full rotor laps carry the next anchor by \(+2\) per lap;
4. periodic transported upper structure with period \(o(b)\) is negligible;
5. a critical-order nonoverlap packing has \(o(s)\) irreducible corners per
   return after negligible deletion.

Unproved:

1. the transported-union estimate (4.1);
2. any implication from sparse corners to small transported union;
3. persistent-overlap packing control;
4. a cross-interval collision theorem for sparse corner roots;
5. the full critical little-oh and coefficient one.

Thus the residual reduction is sound and substantially narrower, but it is
not a proof of coefficient one.
