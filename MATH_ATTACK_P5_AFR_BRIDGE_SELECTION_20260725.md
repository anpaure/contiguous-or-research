# Fifth-wave lane P: coordinate-bridge exposure, canonical cancellation, and mesoscopic capacity

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, numerical
experiment, solver, or computer algebra is used.

## 0. Verdict

Put

\[
 n=2m+1,
 \qquad W=\binom{n}{m},
 \qquad B=\frac Wn=\operatorname{Cat}_m,
 \qquad H_A=\lceil A\sqrt m\rceil.
\]

Throughout every fixed-\(A\) asymptotic statement, \(m\) is sufficiently
large that \(1\le H_A\le m-2\).

This attack does **not** prove \(\mathrm{AFR}_A\).  It proves a sharp
canonical fixed-depth counterinvariant, constructs an exact mesoscopic
positive-density rebundling, proves its complete capacity ceiling, and
identifies the exact limitation of release-weighted bridge averaging.

The decisive fixed-depth theorem is the following.  In the canonical MSW
factor, take \(\tau=(2\ 3)\).  There are

\[
 T=\operatorname{Cat}_{m-4}
\]

pairwise disjoint genuine size-two components \(K_V\), indexed by
\(V\in\mathcal D_{m-4}\), and two moved depth-one target pairs
\(p_V,p'_V\) per component such that

\[
 (\mu(p_V^-),\mu(p_V^+))=(3,1),
 \qquad
 (\mu((p'_V)^-),\mu((p'_V)^+))=(1,1).
\]

Switching \(K_V\) sends these loads to

\[
 (3,1)\longmapsto(2,2),
 \qquad
 (1,1)\longmapsto(0,2).
\]

Since \(c_1=1\), the first move lowers the exact floor energy by two and
the second raises it by two.  The four-cell supports are disjoint as \(V\)
varies.  Therefore

\[
 \boxed{
 Q_1(F_I)=Q_1(F_m^{\rm MSW})
 \quad\text{for every }I\subseteq\{K_V:V\in\mathcal D_{m-4}\}.
 }
 \tag{0.1}
\]

At the same time, the displayed \((3,1)\) pairs contribute elementary
\(\tau\)-orbit release

\[
 \boxed{
 \mathcal R_{\tau,1}(F_m^{\rm MSW})
 \ge 2\operatorname{Cat}_{m-4}
 >\frac{\operatorname{Cat}_m}{128}
 =\frac{W}{128n}.
 }
 \tag{0.2}
\]

Thus the natural bridge really exposes a Catalan-scale integer profile
floor, and every displayed exposed pair is touched by its own distinct
private genuine exact-factor component, but the natural private component
family captures exactly zero full depth-one heat.  The obstruction is not
lack of components.  It is a second, forced, oppositely productive target
pair in every displayed \(\mathcal K_V\) C8 effect.

This does not prove that the **complete** canonical \((2\ 3)\)-cube has
zero best gain: larger components may interact with the same targets.  It
is an exact no-go for the most direct private-component selection and for
every mesoscopic rebundling of that family.

There is nevertheless a genuine mesoscopic construction.  Partition the
full fixed-colour \(p=0\) reservoir of

\[
 T_0=\operatorname{Cat}_{m-2}
 =\left(\frac1{16}+o(1)\right)B
\]

independent C8 coordinates into blocks of \(\Theta(m)\) coordinates.  A
full block switch is an exact factor-to-factor move, replaces
\(\Theta(m)\) wreaths, and changes exactly \(\Theta(m)\) depth-one target
slots.  All blocks together move

\[
 \left(\frac18+o(1)\right)B
\]

wreath rows.  Thus positive-density mesoscopic exact motion exists.
However, for any two vertices at Hamming distance \(k\) in one fixed-colour
cube,

\[
 \frac12\|\Delta\mu_1\|_1=2k,
 \qquad
 \frac12\|\Delta\mu_q\|_1\le4k\quad(2\le q\le m-2).
 \tag{0.3}
\]

Consequently one complete row-disjoint local-packet pass changes the
weighted fixed-window overload by at most

\[
 \boxed{
 (2S_{H_A}-1)B
 =\bigl(\kappa_A+o_A(1)\bigr)\frac W{\sqrt m},
 }
 \tag{0.4}
\]

where

\[
 S_H=\sum_{q=1}^{H}\frac1{c_q},
 \qquad
 \kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
\]

For the whole \(p=0\) reservoir the sharper constant is

\[
 \boxed{
 (4S_{H_A}-2)\operatorname{Cat}_{m-2}
 =\left(\frac{\kappa_A}{8}+o_A(1)\right)
   \frac W{\sqrt m}.
 }
 \tag{0.5}
\]

Rebundling changes the packet geometry but cannot increase this capacity.
It also cannot create a nontrivial deep-only move which exactly preserves
the first-shadow histogram: within a fixed-colour cube, exact preservation
forces the component choice to be trivial.

A second positive-density ceiling holds for the large \(3/8\)-mass tail
of the canonical \((2\ 3)\)-component hierarchy.  If \(q\le A\sqrt m\),
then uniformly at each individual depth, writing
\(\operatorname{diam}_1^{(q)}\) for the **full** \(\ell^1\) histogram
diameter,

\[
 \boxed{
 \operatorname{diam}_1^{(q)}
 \le
 \left(
   \frac5{4\sqrt\pi}+\frac{3q}{4\sqrt m}+o_A(1)
 \right)\frac W{\sqrt m}
 =o(W).
 }
 \tag{0.6}
\]

Hence this tail can reassign \((3/8+o(1))W\) middle owners while remaining
\(o(W)\)-inert at every single shallow rank in a Gaussian window.  The
weighted sum of the upper bounds is only \(O_A(W)\), not \(o(W)\), so
(0.6) is a rankwise ceiling and not a bundled multidepth no-go.

Finally, for an arbitrary exact factor and freshly recomputed bridge
\(\rho\), the full lower-rank component effect is exactly a leakage
derivative.  If \(e_{J,q}\) is the noncyclic containment leakage of fresh
component \(J\), then

\[
 d_{J,q}=\frac{(\mathrm{Id}-\rho)e_{J,q}}{q+1},
 \tag{0.7}
\]

and every deterministic component cut has exact gain

\[
 \boxed{
 \Gamma_\rho(I)=
 \sum_{q\le H}\frac{
 \langle(\mathrm{Id}-\rho)e_{I,q},
         (\mathrm{Id}-\rho)e_{I^c,q}\rangle}
 {c_q(q+1)^2}.
 }
 \tag{0.8}
\]

All raw middle-owner turnover cancels in (0.8).  Same-bridge productivity
is a signed correlation theorem for leakage derivatives; ordinary
fragmentation and turnover do not control it.

There is an unconditional exact-factor locking barrier.  If \(F_*\)
globally minimizes \(\mathcal Q_H\), keep it unchanged while analytically
growing any ordered coordinate spanning tree.  Then

\[
 \sum_t\Delta_t^Q=\mathcal Q_H(F_*),
 \qquad
 \Gamma_t^*=0\quad\text{for every fresh bridge }t.
 \tag{0.9}
\]

Thus, unless \(\mathcal Q_H(F_*)=0\), some same bridge satisfies

\[
 \boxed{
 \Delta_t^Q\ge\frac{\mathcal Q_H(F_*)}{n-1}>0,
 \qquad \Gamma_t^*=0.
 }
 \tag{0.10}
\]

The statement remains true after arbitrary old-group preparation and
new-group cleanup when gain is charged net of preparation.  Consequently,
any universal no-residue positive-fraction theorem would force
\(\mathcal Q_H(F_*)=0\) at every global minimizer.  Locking is a barrier to
deriving such a theorem from the present identities, not an unconditional
refutation: it is not known whether the global minimum is positive.  It
also does **not** refute \(\mathrm{AFR}_A\), whose additive
\(O_A(H_AB)\) residue is precisely what can absorb the locked release and,
if proved, would yield the desired global-minimum bound.

All conclusions remain integral inside literal exact factors.  No
fractional factor, partial middle packing, labelled common-owner
synchronization, or literal OR word is used.

## 1. Exact setup and the two AFR gates

Unless explicitly stated otherwise, depth indices in a window run through
\(1\le q\le H\le m-2\).  The middle depth \(q=0\) has zero factor
discrepancy and may be adjoined harmlessly.

At depth \(q\), let

\[
 N_q=\binom{n}{m-q},
 \qquad
 W=c_qN_q+\delta_q,
 \qquad 0\le\delta_q<N_q.
\]

For an exact middle wreath factor \(F\), let \(\mu_q^F(S)\) be the number
of its wreaths which own the rank-\((m-q)\) target \(S\).  Each of the
\(B\) wreaths contributes \(n\) targets, so

\[
 \sum_S\mu_q^F(S)=W.
\]

Use the exact integral floor polynomial

\[
 Q_q(F)=\sum_S
 (\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)
 \tag{1.1}
\]

and the weighted window energy

\[
 \mathcal Q_H(F)=\sum_{q\le H}\frac{Q_q(F)}{c_q}.
 \tag{1.2}
\]

At depth one,

\[
 \frac W{N_1}=\frac{m+2}{m},
 \qquad c_1=1,
 \qquad
 \phi_1(u):=(u-1)(u-2).
 \tag{1.3}
\]

For a transposition-generated coordinate subgroup \(G\), let
\(\mathfrak B_{H,G}(F)\) be the exact minimum of (1.2), independently at
each rank, over nonnegative integral load vectors with the same
\(G\)-orbit totals as \(F\).  This is an integral orbit-profile relaxation,
not an assertion that a minimizing vector is realized by an exact factor.
If \(\rho\) joins two coordinate components and
\(G^+=\langle G,\rho\rangle\), its subgroup profile release is

\[
 \Delta_H^Q(G,\rho)
 =\mathfrak B_{H,G}(F)-\mathfrak B_{H,G^+}(F).
 \tag{1.4}
\]

For the trivial old group, write the elementary moved-pair release as

\[
 \mathcal R_{\rho,H}(F)
 :=\mathcal Q_H(F)-\mathfrak B_{H,\langle\rho\rangle}(F)
 =\Delta_H^Q(\{1\},\rho).
 \tag{1.4a}
\]

For the direct \(F\)-versus-\(\rho F\) overlay, let \(J\) range over its
genuine ownership components and let \(d_J\) be the old-to-new multidepth
load effect.  Switching a component set \(I\) is one literal exact factor
and has exact gain

\[
 \Gamma_\rho(I)
 =\mathcal Q_H(F)-\mathcal Q_H(F_I)
 =\langle d_I,d_{I^c}\rangle_H,
 \tag{1.5}
\]

where

\[
 \langle x,y\rangle_H
 =\sum_{q\le H}\frac{\langle x_q,y_q\rangle}{c_q}.
\]

If

\[
 A_\rho=\left\|\sum_Jd_J\right\|_H^2,
 \qquad
 V_\rho=\sum_J\|d_J\|_H^2,
\]

\[
 \varrho_\rho=
 \min_{\varepsilon_J\in\{\pm1\}}
 \left\|\sum_J\varepsilon_Jd_J\right\|_H^2,
\]

then

\[
 \Gamma_\rho^{\rm fair}=\frac{A_\rho-V_\rho}{4},
 \qquad
 \Gamma_\rho^*=\frac{A_\rho-\varrho_\rho}{4}.
 \tag{1.6}
\]

Thus a bridge theorem has two logically separate tasks:

1. expose a fixed share of the subgroup release (1.4) in the elementary
   moved target pairs of the same \(\rho\); and
2. find one common component cut whose signed correlations capture a fixed
   share of that exposed release.

The next theorem shows both the promise and the exact failure of the most
natural canonical family.

## 2. Canonical MSW: exact exposed pairs and exact collateral lock

Let \(F_m^{\rm MSW}\) be the canonical MSW exact factor and
\(\tau=(2\ 3)\), with \(m\ge4\).  Write \(\mathcal D_s\) for the Dyck
words of semilength \(s\), \(E(w)\) for the canonical MSW wreath rooted at
\(w\), and \(\rho(w)\) for its flip permutation.  The standard MSW maps
\(g,h\) select the next inserted and deleted coordinates; \(a_0(W)\) and
\(b_{m-1}(W)\) denote the initial inserted and terminal deleted
coordinates of the root \(W\).  For \(V\in\mathcal D_{m-4}\), put

\[
 K(V)=\{7\}\cup(8+\operatorname{Down}(V)),
 \tag{2.1}
\]

where \(8+D=\{8+d:d\in D\}\), and define four rank-\((m-1)\)
targets

\[
 S_V=K(V)\cup\{2,n\},
 \qquad \tau S_V=K(V)\cup\{3,n\},
 \tag{2.2}
\]

\[
 T_V=K(V)\cup\{3,8\},
 \qquad \tau T_V=K(V)\cup\{2,8\}.
 \tag{2.3}
\]

The sets in (2.1)--(2.3) all have the asserted sizes because
\(|\operatorname{Down}(V)|=m-4\).

Let

\[
 \mathcal K_V=\mathcal C_{0,1100V}
 =\{E(11001100V),E(10101100V)\}
 \tag{2.4}
\]

be the size-two component in the canonical \((2\ 3)\)-overlay.

### Theorem 2.1 -- exact private-pair release and collateral cancellation

For every \(m\ge4\) and \(V\in\mathcal D_{m-4}\):

\[
 \boxed{
 (\mu_1(S_V),\mu_1(\tau S_V))=(3,1),
 \qquad
 (\mu_1(T_V),\mu_1(\tau T_V))=(1,1).
 }
 \tag{2.5}
\]

The old-to-new effect of switching \(\mathcal K_V\) is exactly

\[
 \boxed{
 d_V=-e_{S_V}+e_{\tau S_V}-e_{T_V}+e_{\tau T_V}.
 }
 \tag{2.6}
\]

The components \(\mathcal K_V\) are pairwise distinct and simultaneously
switchable.  Their four-cell supports in (2.6) are pairwise disjoint.
Consequently every subset \(I\subseteq\mathcal D_{m-4}\) gives an exact
factor \(F_I\) satisfying

\[
 \boxed{Q_1(F_I)=Q_1(F_m^{\rm MSW}).}
 \tag{2.7}
\]

Nevertheless the elementary \(\tau\)-orbit floor released on the pair
\(\{S_V,\tau S_V\}\) is exactly two.  Hence

\[
 \mathcal R_{\tau,1}(F_m^{\rm MSW})
 \ge2\operatorname{Cat}_{m-4}.
 \tag{2.8}
\]

#### Proof

The canonical MSW four-letter component has old omitted-label orders

\[
 (4,2,3,1,T),
 \qquad(2,1,4,3,T),
\]

and new orders

\[
 (4,3,2,1,T),
 \qquad(3,1,4,2,T).
\]

The exact C8 first-shadow formula is the elementary rectangle

\[
 e_{K\cup\{2,x\}}-e_{K\cup\{3,x\}}
 -e_{K\cup\{2,y\}}+e_{K\cup\{3,y\}}.
 \tag{2.9}
\]

For the component indexed by \(1100V\), the exact flip recursion gives

\[
 \rho(1100V)=(4,2,3,1,4+\rho(V)).
\]

Thus the common tail in the four-letter normal form is

\[
 (8,6,7,5,8+\rho(V),n),
\]

whose even list is

\[
 (8,7,8+\operatorname{Down}(V),n).
\]

Therefore \(x=8\), \(y=n\), and the common core is exactly (2.1).
Reordering (2.9) gives (2.6), including all four signs.

For the pair containing \(n\), complement to the upper core word.  The
two words are

\[
 10111101V,
 \qquad11011101V.
 \tag{2.10}
\]

The audited suffix-separation lemma from
`FRACTIONAL_PACKET_CANONICAL_MSW_OBSTRUCTION_20260725.md` shows that every
canonical preimage of either word uses both added coordinates in the first
eight positions.  Its short height proof is as follows.  The prefix
\(10111101\) ends at height four and the Dyck suffix never falls below that
height.  If the \(g\)-selected coordinate were in the suffix, its down-step
could not start at height zero or one.  If only the preceding
\(h\)-coordinate were in the suffix, the possible prefix \(g\)-coordinates
are \(1,3,4\); coordinate one is impossible from the candidate count,
while coordinates three and four make \(h\) select five and three,
respectively.  For \(11011101\), the possible coordinates are \(1,2,4\);
one is again impossible, while two and four both make \(h\) select five.
Thus both coordinates lie in the first eight positions.

The complete symbolic semilength-four inverse-owner table, derived from
the MSW recursion and independently audited, contains complement pair
\(27\) exactly in the three roots

\[
 11110000,\qquad11101000,\qquad11001100,
\]

and complement pair \(37\) exactly in the root \(11011000\).
Appending \(V\) preserves these owners and introduces no further one.
This proves the first equality in (2.5).

For completeness, the companion count requires a different owner inversion;
plain suffix locality of the preceding upper-core colour does not apply.
On the first \(2m\) coordinates its two incidence words are

\[
 T_V=00100011\,\overline V,
 \qquad
 \tau T_V=01000011\,\overline V.
 \tag{2.10a}
\]

Here \(\overline V\) is the bitwise complement of \(V\).

Every first-shadow occurrence avoiding \(n\) is either an internal
intersection \(x_i\cap x_{i+1}\), the initial boundary
\([2m]\setminus y_0\), or the terminal boundary
\([2m]\setminus y_{m-1}\).

For an internal occurrence of a proposed target \(L\), choose
\(b\notin L\), put \(x=L\cup\{b\}\), let \(a=g(x)\), and require

\[
 h(x\cup\{a\})=b.
 \tag{2.10b}
\]

Write \(V\) as a product of \(k\) primitive Dyck factors and apply the
defining height rules for \(g,h\).  The following list is exhaustive.  For
\(L=\tau T_V\), every suffix choice of \(b\), and the choices
\(b=4,5,6\), lie in the terminal nonpositive-flaw class; \(b=1\) makes
\(h\) delete coordinate two, and \(b=3\) makes it delete coordinate
three.  Exactly one internal state remains:

\[
 x=01100011\,\overline V.
 \tag{2.10c}
\]

For \(L=T_V\), the same terminal cases eliminate the suffix choices and
\(b=4,5,6\); the choices \(b=1,2\) both make \(h\) delete coordinate
three.  Thus \(T_V\) has no internal occurrence.

At the initial boundary one has

\[
 [2m]\setminus y_0
 =\operatorname{Down}(W)\setminus\{a_0(W)\}
 \tag{2.10d}
\]

for the owner root \(W\).  The target \(\tau T_V\) would force \(W\) to
begin with \(10\), so \(a_0(W)=2\in\tau T_V\), impossible after the
deletion in (2.10d).  For \(T_V\), the unique possibility is
\(a_0(W)=4\), giving the owner root

\[
 W=11001100V.
 \tag{2.10e}
\]

Here \(a_0=2\) makes the proposed prefix fall below zero; \(a_0=5,6\)
cannot be the first return; and a suffix choice begins after a prefix of
height two and cannot be the required added first-return down-step.  The
coordinates already in \(T_V\), together with the impossibility of a
down-step at coordinate one, exclude all remaining choices.  This proves
the asserted uniqueness of \(a_0=4\).

At the terminal boundary,

\[
 [2m]\setminus y_{m-1}
 =\operatorname{Up}(W)\setminus\{b_{m-1}(W)\}.
 \tag{2.10f}
\]

Both targets omit coordinate one, so Dyckness forces the added coordinate
to be one.  The two candidate roots are

\[
 11000011\,\overline V,
 \qquad
 10100011\,\overline V,
\]

and both fall below height zero at coordinate five.  Neither is Dyck, so
there is no terminal-boundary owner.  Therefore \(T_V\) has its one
initial-boundary owner and \(\tau T_V\) has its one internal owner.  This
proves the second equality in (2.5) for every Dyck suffix \(V\).

Now use \(\phi_1(u)=(u-1)(u-2)\).  On the first pair,

\[
 (3,1)\longmapsto(2,2)
\]

changes \(\phi_1(3)+\phi_1(1)=2\) to zero, a gain of two.  On the second,

\[
 (1,1)\longmapsto(0,2)
\]

changes zero to \(\phi_1(0)+\phi_1(2)=2\), a loss of two.  Thus one
component has net gain zero.

The components in (2.4) are different components of one genuine
interaction cube.  Their supports are disjoint directly from
(2.1)--(2.3): cells containing \(n\) avoid \(8\), cells containing \(8\)
avoid \(n\), membership of \(2\) versus \(3\) identifies the corner, and
removing the two displayed corner labels recovers
\(K(V)=\{7\}\cup(8+\operatorname{Down}(V))\), hence \(V\).  Thus gains
add with no cross term for every subset, proving (2.7).  The integer minimum on a
two-cell orbit of total four is \((2,2)\), so each displayed \((3,1)\)
pair has release two.  The pairs are distinct; summing proves (2.8).
\(\square\)

The numerical inequality in (0.2) follows from

\[
 \frac{\operatorname{Cat}_{m-4}}{\operatorname{Cat}_m}
 =\frac{(m-2)(m-1)m(m+1)}
 {16(2m-7)(2m-5)(2m-3)(2m-1)}
 >\frac1{256}.
 \tag{2.10g}
\]

For the strict inequality, compare the four denominator factors with
\(2(m-2),2(m-1),2m,2(m+1)\), respectively.

### Corollary 2.2 -- projected success is not full heat

If one projects the energy onto only the pairs
\(\{S_V,\tau S_V\}\), switching all \(\mathcal K_V\) captures one
hundred percent of their release:

\[
 Q_{1,\mathcal P}(F_m^{\rm MSW})
 -Q_{1,\mathcal P}(F_{\mathcal D_{m-4}})
 =2\operatorname{Cat}_{m-4}.
 \tag{2.11}
\]

The full energy sees the forced companion pairs and has gain zero by
(2.7).  Thus target-private signs are not enough; the exact factor lift
forces a second signed target obligation.

### Scope of Theorem 2.1

The theorem concerns the positive-density subcube generated by the
components \(\mathcal K_V\).  The complete canonical \((2\ 3)\)-overlay
also contains the components \(\mathcal C_{j,R}\) for \(j\ge1\), including
the seven-row components which carry the other two owners of \(S_V\).
Theorem 2.1 neither proves nor disproves a productive cut using those
larger components.  It proves that the obvious private C8 correction,
despite exact exposure and exact fragmentation, is globally locked at
depth one.

Indeed the total \((2\ 3)\)-displacement on the displayed four-cell
rectangle is

\[
 -2e_{S_V}+2e_{\tau S_V},
\]

whereas the private component contributes (2.6).  All remaining overlay
components therefore aggregate on this rectangle to

\[
 -e_{S_V}+e_{\tau S_V}+e_{T_V}-e_{\tau T_V}.
 \tag{2.12}
\]

No other \(p=0\) component contributes, by fixed-position support
disjointness.  The compensating effect comes from larger components, which
is exactly why Theorem 2.1 is not a theorem about the best cut of the full
cube.

## 3. Exact mesoscopic rebundling and its capacity ceiling

The previous theorem used only the subfamily with suffix \(1100V\).  We
now use the full fixed-position family.  For

\[
 0\le p\le m-2,
 \qquad P\in\mathcal D_p,
 \qquad R\in\mathcal D_{m-p-2},
\]

the canonical roots

\[
 P1100R,\qquad P1010R
 \tag{3.1}
\]

form a genuine two-for-two component for

\[
 \tau_p=(2p+2\ \ 2p+3).
\]

For fixed \(p\), all

\[
 T_p=\operatorname{Cat}_p\operatorname{Cat}_{m-p-2}
 \tag{3.2}
\]

components are independent coordinates of one exact-factor cube.

### Theorem 3.1 -- exact local-packet movement

Let two vertices of one fixed-\(p\) cube differ in \(k\) component
coordinates.  Then

\[
 \boxed{
 \frac12\|\mu_1(F')-\mu_1(F)\|_1=2k,
 }
 \tag{3.3}
\]

and, for \(2\le q\le m-2\),

\[
 \boxed{
 \frac12\|\mu_q(F')-\mu_q(F)\|_1\le4k.
 }
 \tag{3.4}
\]

At depth one the changed support has exactly \(4k\) cells.  In
particular, a nonempty component choice never preserves the first-shadow
histogram.

#### Proof

For one component, split the common tail order into parity lists
\(E,O\), and put \(\partial H=e_{H\cup\{\gamma\}}-e_{H\cup\{\beta\}}\).
At rank \(r=m-q\), the exact effect is

\[
 \partial\operatorname{suf}_{r-1}(O)
 +\partial\operatorname{suf}_{r-1}(E)
 -\partial\operatorname{pre}_{r-1}(E)
 -\partial\operatorname{pre}_{r-1}(O).
 \tag{3.5}
\]

At \(q=1\), the two \(O\)-terms cancel and (3.5) is one four-cell
rectangle.  For \(2\le q\le m-2\), its eight cells are distinct.  Hence
one component has half-\(\ell^1\) movement two at depth one and four at
every displayed deeper depth.

For fixed \(p\), the four-cell first-shadow supports are pairwise disjoint.
Indeed one endpoint side recovers the Dyck suffix by the first-return
height rule, while the other recovers the Dyck prefix by the dual
first-negative rule.  Therefore the fixed-\(p\) first-shadow map is an
exact isometry,

\[
 \left\|B_{m-1}\sum_{P,R}a_{P,R}z_{p,P,R}\right\|_2^2
 =4\sum_{P,R}a_{P,R}^2.
 \tag{3.6}
\]

Taking coefficients in \(\{-1,0,1\}\) proves (3.3).  Triangle inequality
over the eight-cell effects proves (3.4).  \(\square\)

### Theorem 3.2 -- a positive-density mesoscopic exact rebundling

Fix constants \(0<\alpha<\beta<\infty\).  Choose integers \(b_m\) with

\[
 \alpha m\le b_m\le\beta m.
\]

Partition all but fewer than \(b_m\) of the \(p=0\) components into

\[
 P_m=\left\lfloor\frac{\operatorname{Cat}_{m-2}}{b_m}\right\rfloor
\]

blocks of \(b_m\) component coordinates.  Then:

1. every full block flip is a literal exact factor-to-factor move;
2. every block replaces exactly \(2b_m=\Theta(m)\) wreath rows;
3. every block changes exactly \(4b_m=\Theta(m)\) first-shadow cells and
   has first-shadow half-\(\ell^1\) movement \(2b_m\);
4. all full blocks together replace
   \[
   2b_mP_m
   =\left(\frac18+o(1)\right)B
   \]
   wreath rows; and
5. no nonempty block or subcoordinate choice is first-shadow neutral.

#### Proof

For \(p=0\), (3.2) gives

\[
 T_0=\operatorname{Cat}_{m-2},
 \qquad
 \frac{T_0}{B}
 =\frac{m(m+1)}{4(2m-3)(2m-1)}
 \longrightarrow\frac1{16}.
 \tag{3.7}
\]

The component coordinates are independently switchable, so any union of
blocks is an exact cube vertex.  Each component contains two old wreaths,
and distinct coordinates have disjoint old and new middle supports.
Statements 1--2 and 4 follow.  Statements 3 and 5 are (3.3).  \(\square\)

This construction meets the literal mesoscopic requirement: it changes
\(\Theta(m)\) shallow slots per packet, has positive total wreath density,
and preserves exact middle ownership.  The next theorem proves why it is
not a bulk absorber.

For the capacity statement, let

\[
 O_q(F)=\frac12
 \min_{\substack{b(S)\in\{c_q,c_q+1\}\\\sum_Sb(S)=W}}
 \|\mu_q(F)-b\|_1
 \tag{3.7a}
\]

be the exact balanced overload at depth \(q\).

### Theorem 3.3 -- overload, hole, and weighted capacity ceilings

Assume \(m\ge3\) and \(1\le H\le m-2\).  Let \(T\) pairwise
owner-disjoint local C8 coordinates be available in one exact factor, and
let two cube vertices differ in \(k\le T\) coordinates.
For every balanced-overload functional \(O_q\), and also for the number of
uncovered rank-\((m-q)\) targets,

\[
 |\Delta O_1|\le2k,
 \qquad
 |\Delta O_q|\le4k\quad(2\le q\le m-2).
 \tag{3.8}
\]

Consequently

\[
 \boxed{
 \left|\Delta\sum_{q\le H}\frac{O_q}{c_q}\right|
 \le k\left(\frac2{c_1}+4\sum_{q=2}^H\frac1{c_q}\right)
 =k(4S_H-2).
 }
 \tag{3.9}
\]

Since every local coordinate uses two wreath rows, \(T\le B/2\).  Hence

\[
 \boxed{
 \left|\Delta\sum_{q\le H}\frac{O_q}{c_q}\right|
 \le(2S_H-1)B.
 }
 \tag{3.10}
\]

For fixed \(A\),

\[
 S_{H_A}=\kappa_A\sqrt m+O_A(1),
 \qquad
 \kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor},
 \tag{3.11}
\]

so (3.10) is (0.4).  For the full \(p=0\) cube, (3.9) and (3.7) give
(0.5).

#### Proof

For a zero-total histogram difference \(h\), both the optimized balanced
overload and the hole count can improve by at most
\(\|h\|_1/2\).  Apply (3.3)--(3.4), then sum with the positive weights
\(1/c_q\).  The row count gives \(T\le B/2\).

Finally,

\[
 \log\frac W{N_q}=\frac{q(q+1)}m+O_A(m^{-1/2})
\]

uniformly for \(q\le A\sqrt m\).  Apart from \(O_A(1)\) floor-threshold
indices, \(c_q=\lfloor e^{q^2/m}\rfloor\).  The bounded-variation Riemann
sum gives (3.11).  \(\square\)

### Corollary 3.4 -- first-shadow anchoring survives rebundling

For two vertices of a fixed-\(p\) cube, put

\[
 D_q=\frac12\|\Delta\mu_q\|_1.
\]

Then

\[
 \boxed{D_q\le2D_1\quad(2\le q\le m-2).}
 \tag{3.12}
\]

In particular \(D_1=0\) forces the two vertices to be identical.  Grouping
\(\Theta(m)\) coordinates into one mesoscopic decision does not create a
nontrivial correction which is exactly first-shadow neutral while changing
a deeper histogram.  This does not exclude transport between two different
balanced first-shadow profiles or preservation of a Hall inequality despite
nonzero first-shadow motion.

More generally, the first-shadow effects of **all** shifted local
components, over all \(p\), are linearly independent over every field.
Thus no nonzero signed integer combination of the complete local atlas is
first-shadow neutral.  Across different \(p\) these components need not
form one simultaneously switchable cube, so this last assertion is an
increment-lattice obstruction, not a claim of joint applicability.

### Theorem 3.5 -- the exact depth-one quadratic ceiling

For every exact factor and every rank-\((m-1)\) target,

\[
 \mu_1(S)\le M_1:=\left\lfloor\frac{m+2}{2}\right\rfloor.
 \tag{3.13}
\]

The decrease of \(Q_1\) under any \(k\)-coordinate move in a
pairwise-owner-disjoint persistent local C8 cube is at most

\[
 4k(M_1-1).
 \tag{3.14}
\]

For the whole \(p=0\) cube this gives

\[
 \boxed{
 \Delta Q_1
 \le4\operatorname{Cat}_{m-2}
 \left(\left\lfloor\frac{m+2}{2}\right\rfloor-1\right)
 =\left(\frac1{16}+o(1)\right)W.
 }
 \tag{3.15}
\]

#### Proof

The occurrences of a fixed \((m-1)\)-set \(S\) correspond to factor edges
on its \(m+2\) middle supersets.  No two such edges share a middle vertex,
so they form a matching and (3.13) follows.

For \(\phi_c(x)=(x-c)(x-c-1)\), a unit transfer from a cell of load \(u\)
to one of load \(v\) changes the floor energy by

\[
 \phi_c(u)+\phi_c(v)-\phi_c(u-1)-\phi_c(v+1)
 =2(u-v-1).
 \tag{3.16}
\]

This is at most \(2(M_1-1)\).  A depth-one C8 rectangle contains two unit
transfers, proving (3.14).  Insert \(k\le\operatorname{Cat}_{m-2}\) and
(3.7) to obtain (3.15).  \(\square\)

The quadratic ceiling is only constant-order.  It is not an
amplitude-free \(o(W)\) bound, and it does not exclude capture of a small
fixed fraction of a large quadratic release.  The overload and hole
ceilings (3.9)--(3.10) are much sharper because those objectives are
one-Lipschitz under a unit transfer.

## 4. A multidepth \(3/8\)-tail ceiling

The preceding local family uses constant-size components.  The canonical
\((2\ 3)\)-hierarchy also contains components

\[
 \mathcal C_{j,R}=\{AR:A\in\mathcal A_j\},
 \qquad
 |\mathcal C_{j,R}|=C_j+C_{j+1},
 \tag{4.1}
\]

where \(C_s=\operatorname{Cat}_s\),
\(0\le j\le m-2\), and the suffix depth is

\[
 r=m-j-2,
 \qquad R\in\mathcal D_r.
\]

### Theorem 4.1 -- exact rank-\(q\) component ledger

For every \(1\le q\le m-2\), the depth-\(q\) histogram effect of one
component satisfies

\[
 \boxed{
 \|\Delta^{(q)}_{j,R}\|_1
 \le(4j+4q+6)(C_j+C_{j+1}).
 }
 \tag{4.2}
\]

For \(q=0\), exact middle ownership gives the stronger value zero.

#### Proof

Put \(a=j+2\), so \(a+r=m\).  In step-two cyclic order, the old roots of
the component decompose into blocks

\[
 (n,X_A,U_R,Y_A,D_R)
 \tag{4.3}
\]

of lengths

\[
 (1,a,r,a,r).
\]

A depth-\(q\) target is a cyclic window of length

\[
 \ell=m-q=a+r-q.
\]

Assume first \(r\ge q\).  A window which contains all of \(X_A\), none of
\(Y_A\), and otherwise only fixed gap labels is specified by choosing
\(u,v\ge0\) with

\[
 u+v=r-q.
\]

There are exactly \(r-q+1\) choices; the preceding and following capacities
do not bind.  The same count holds for \(Y_A\), and the two families are
disjoint.  For a fixed split, the gap portion is independent of \(A\) and
fixed by \(\tau\), while the multisets \(\{X_A\}\) and \(\{Y_A\}\) are
separately \(\tau\)-invariant.  These occurrences therefore cancel in the
component aggregate.

The number of uncertified old occurrences per root is at most

\[
 n-2(r-q+1)=2a+2q-1.
\]

Applying \(\tau-\mathrm{Id}\) gives at most one removal and one addition
per candidate.  Multiplying by the component size proves

\[
 2(2a+2q-1)(C_j+C_{j+1})
 =(4j+4q+6)(C_j+C_{j+1}).
\]

If \(q>r\), the trivial bound \(2n(C_j+C_{j+1})\) is no larger than the
right side of (4.2), because

\[
 4j+4q+6=4m+4(q-r)-2\ge4m+2=2n.
\]

This proves all cases.  \(\square\)

The coefficient in (4.2) counts uncancelled candidate occurrences, not
distinct nonzero target cells and not a lower bound.  Further target
coincidences or cross-root cancellation can only reduce the actual effect.

For \(L\ge0\), let the suffix tail consist of all components with
\(r\ge L\), and put

\[
 M_{m,L}
 =\sum_{r=L}^{m-2}
 C_r(C_{m-r-2}+C_{m-r-1}).
 \tag{4.4}
\]

This is the number of canonical wreaths carried by the tail.  Let

\[
 A_{m,L}
 =\sum_{r=L}^{m-2}
 (4m-4r+2)
 C_r(C_{m-r-2}+C_{m-r-1})
 \tag{4.5}
\]

be its audited depth-one triangle ledger.

### Theorem 4.2 -- uniform Gaussian rankwise inertness

For \(1\le q\le L\), any two vertices of the tail cube satisfy

\[
 \boxed{
 \|\mu_q(F')-\mu_q(F)\|_1
 \le A_{m,L}+4(q-1)M_{m,L}.
 }
 \tag{4.6}
\]

If \(L=\lfloor m/2\rfloor\), then

\[
 M_{m,L}=\left(\frac38+o(1)\right)B,
 \tag{4.7}
\]

\[
 A_{m,L}\sim\frac5{4\sqrt\pi}\frac W{\sqrt m}.
 \tag{4.8}
\]

For all sufficiently large \(m\), uniformly for integers
\(1\le q\le A\sqrt m\) (so \(q\le L\)), with \(x=q/\sqrt m\),

\[
 \boxed{
 \|\mu_q(F')-\mu_q(F)\|_1
 \le
 \left(
   \frac5{4\sqrt\pi}+\frac{3x}{4}+o_A(1)
 \right)\frac W{\sqrt m}.
 }
 \tag{4.9}
\]

#### Proof

Sum (4.2) over the components on which the two cube vertices differ.  The
sum over the whole tail is

\[
 A_{m,L}+4(q-1)M_{m,L},
\]

and triangle inequality gives (4.6) with no extra factor two.

The fixed-\(j\) endpoint of the Catalan convolution gives

\[
 \frac{M_{m,L}}B\longrightarrow
 \sum_{j\ge0}\frac{C_j+C_{j+1}}{4^{j+2}}
 =\frac38
\]

when \(L\to\infty\) and \(m-L\to\infty\), proving (4.7).

For (4.8), the \(+10\) part of (4.5) is \(O(B)\), negligible on the
\(W/\sqrt m\) scale.  Catalan asymptotics turn the remaining sum into

\[
 \frac5{8\sqrt\pi}
 \int_0^{1/2}t^{-1/2}(1-t)^{-3/2}\,dt
 \cdot\frac W{\sqrt m}.
\]

The integral is two.  This proves (4.8).  Finally, (4.7) gives

\[
 4(q-1)M_{m,L}
 =\left(\frac{3x}{4}+o_A(1)\right)\frac W{\sqrt m},
\]

which proves (4.9).  \(\square\)

The tail replaces \((3/8+o(1))B\) wreaths and therefore reassigns
\((3/8+o(1))W\) middle-owner incidences, yet (4.9) is \(o(W)\) at every
fixed shallow depth uniformly throughout the Gaussian window.  Thus
positive-density root turnover does not imply constant-fraction rankwise
exposure.

### Corollary 4.3 -- the bundled ceiling is only critical

Put

\[
 J_A=\int_0^A\frac{x\,dx}{\lfloor e^{x^2}\rfloor}.
\]

The weighted overload or hole-objective diameter of the tail is at most

\[
 \boxed{
 \left(
   \frac{5\kappa_A}{8\sqrt\pi}
   +\frac{3J_A}{8}
   +o_A(1)
 \right)W.
 }
 \tag{4.10}
\]

Indeed the objective difference at depth \(q\) is at most half the
\(\ell^1\) difference in (4.6), and

\[
 \sum_{q\le H_A}\frac1{c_q}
 =\kappa_A\sqrt m+O_A(1),
 \qquad
 \sum_{q\le H_A}\frac{q-1}{c_q}
 =J_Am+O_A(\sqrt m).
\]

The right side of (4.10) is linear in \(W\).  The theorem therefore does
not rule out a bundled \(\Theta(W)\) multidepth effect.  It proves only
rankwise inertness and a sharp triangle-ledger ceiling.

## 5. Fresh components are pure leakage derivatives

The preceding sections are canonical.  The next identity holds for every
exact factor and every freshly recomputed bridge.

For a coordinate transposition \(\rho\), its action on a histogram is

\[
 (\rho x)(S)=x(\rho S).
 \tag{5.0}
\]

We first record the structural fact needed below.

### Lemma 5.0 -- transposition stability of a fresh component

Let \(C\) be a wreath and let the two labels exchanged by \(\rho\) have
shorter cyclic distance \(d\le m\) in \(C\).  Then \(C\) and \(\rho C\)
share exactly

\[
 n-2d\ge1
\]

middle intervals.  Consequently, in the direct ownership overlay of
\(F\) and \(\rho F\), every component is carried to itself by the
side-exchanging \(\rho\)-involution.  If \(K_J\) is its old-side wreath
set, its new side is \(\rho K_J\), and the common middle-root union
\(V_J\) satisfies

\[
 \rho V_J=V_J.
 \tag{5.0a}
\]

#### Proof

A cyclic \(m\)-interval changes under swapping the two labels exactly when
it contains one of them but not the other.  There are \(2d\) such starts,
so the remaining \(n-2d\) intervals are shared.  Hence every old row
\(C\) is connected in the overlay to its corresponding new row
\(\rho C\).  The coordinate involution exchanges the two sides and cannot
send one connected component to another.  Thus the two row sides are
\(K_J\) and \(\rho K_J\).  By the definition of an ownership component,
their middle unions are equal; the second is also \(\rho V_J\).  This
proves (5.0a).  \(\square\)

Fix a fresh \(\rho\)-component \(J\).  Let \(V_J\) be the common union of
its middle roots; Lemma 5.0 makes \(V_J\) \(\rho\)-invariant.  At depth
\(q\), let

\[
 x_{J,q}(S)
 =\#\{\text{old-side wreath occurrences in }J\text{ owning }S\}.
\]

Define the containment shadow and leakage

\[
 H_{V_J,q}(S)=\#\{X\in V_J:S\subseteq X\},
 \tag{5.1}
\]

\[
 e_{J,q}=H_{V_J,q}-(q+1)x_{J,q}.
 \tag{5.2}
\]

### Theorem 5.1 -- exact fresh leakage identity

For every fresh component,

\[
 \boxed{
 (q+1)(x_{J,q}-\rho x_{J,q})
 =-(e_{J,q}-\rho e_{J,q}).
 }
 \tag{5.3}
\]

Consequently its old-to-new effect is

\[
 \boxed{
 d_{J,q}=\rho x_{J,q}-x_{J,q}
 =\frac{(\mathrm{Id}-\rho)e_{J,q}}{q+1}.
 }
 \tag{5.4}
\]

For every deterministic component cut \(I\),

\[
 \boxed{
 \Gamma_\rho(I)=
 \sum_{q\le H}\frac{
 \langle(\mathrm{Id}-\rho)e_{I,q},
         (\mathrm{Id}-\rho)e_{I^c,q}\rangle}
 {c_q(q+1)^2}.
 }
 \tag{5.5}
\]

#### Proof

The cyclic containment identity is exactly (5.2).  Apply \(\rho\) and
subtract.  Since \(V_J\) is \(\rho\)-invariant,

\[
 H_{V_J,q}=\rho H_{V_J,q}.
\]

The containment terms therefore cancel and give (5.3).  Rearrangement
gives (5.4).  Substitute (5.4) into the exact component-cut identity
\(\Gamma_\rho(I)=\langle d_I,d_{I^c}\rangle_H\) to obtain (5.5).
\(\square\)

Equation (5.5) is the rigorous same-bridge obstruction.  Middle-root
turnover, owner-Schreier boundary size, and coarse quotient expansion are
absent.  Once components are freshly regrouped, every lower-rank effect is
the antisymmetric derivative of noncyclic leakage.  A successful AFR
selection theorem must prove favorable cross-correlation of those leakage
derivatives for the **same** bridge which has large subgroup profile
release.

Unsigned fragmentation does not determine the sign in (5.5).  Neither a
large number of components nor small component size prevents the inner
products from being zero or negative.

## 6. What deterministic or averaged bridge selection can prove

Consider any realized adaptive spanning-tree path

\[
 (F_0,G_0),(F_1,G_1),\ldots,(F_{n-1},G_{n-1}),
\]

where \(G_0\) is trivial and \(G_{n-1}=S_n\).  Let \(\Delta_t^Q\) be the
subgroup release and

\[
 \Gamma_t^Q=\mathcal Q_H(F_{t-1})-\mathcal Q_H(F_t)
\]

the net stage gain, including preparation and cleanup.

Here “adaptive path” includes the essential legality condition: through
stage \(t\), every switch uses a transposition in \(G_t\), so the entire
stage transition preserves every \(G_t\)-orbit total; the fresh bridges
form a spanning tree.  Under precisely this condition, the profile
telescope below is valid.

The exact profile and energy telescopes are

\[
 \sum_t\Delta_t^Q=\mathcal Q_H(F_0),
 \qquad
 \sum_t\Gamma_t^Q
 =\mathcal Q_H(F_0)-\mathcal Q_H(F_{n-1}).
 \tag{6.1}
\]

### Theorem 6.1 -- exact release-weighted bridge accounting

Assume \(\mathcal Q_H(F_0)>0\).  Choose a random stage \(T\) with

\[
 \Pr(T=t)=\frac{\Delta_t^Q}{\mathcal Q_H(F_0)},
\]

with the ratio below evaluated only on positive-release stages.  Put

\[
 Z_0=\{t:\Delta_t^Q=0\},
 \qquad
 G_{\rm zr}=\sum_{t\in Z_0}\Gamma_t^Q.
\]

Then the exact identity is

\[
 \boxed{
 \mathbb E\left[\frac{\Gamma_T^Q}{\Delta_T^Q}\right]
 =1-\frac{\mathcal Q_H(F_{n-1})}{\mathcal Q_H(F_0)}
  -\frac{G_{\rm zr}}{\mathcal Q_H(F_0)}
 }
 \tag{6.2}
\]

Thus some positive-release bridge has efficiency at least the right side.
If \(G_{\rm zr}\) itself is a positive fixed fraction of
\(\mathcal Q_H(F_0)\),
the zero-release stages have already supplied that much net descent.  If
not, a positive right side still comes only from endpoint contraction not
already charged to those stages.  No unconditional positive constant
emerges.  In the common special case \(G_{\rm zr}=0\), (6.2) reduces to the simpler
endpoint-contraction ratio.

#### Proof

Multiply the sampled ratio by its probability and sum.  Equation (6.1)
gives

\[
 \sum_{t\notin Z_0}\frac{\Delta_t^Q}{\mathcal Q_H(F_0)}
 \frac{\Gamma_t^Q}{\Delta_t^Q}
 =\frac{\sum_t\Gamma_t^Q-G_{\rm zr}}{\mathcal Q_H(F_0)},
\]

which is (6.2).  \(\square\)

### Theorem 6.2 -- exact global-minimum bridge locking

Let \(F_*\) globally minimize \(\mathcal Q_H\) over all exact factors.
Fix any ordered coordinate spanning tree and keep the factor equal to
\(F_*\) at every stage.  Then

\[
 \sum_{t=1}^{n-1}\Delta_t^Q=\mathcal Q_H(F_*),
 \tag{6.3}
\]

while, for every fresh bridge \(\rho_t\) and every subset \(I\) of its
freshly recomputed direct ownership components,

\[
 \Gamma_{\rho_t}(I)\le0,
 \qquad
 \Gamma_{\rho_t}^*=0.
 \tag{6.4}
\]

Therefore either \(\mathcal Q_H(F_*)=0\), or some stage obeys (0.10).

The assertion is preparation-safe in the following exact sense.  At a
stage with old group \(G\), permit any finite sequence of \(G\)-internal
exact switches, then one freshly recomputed \(\rho\)-component choice,
then any finite sequence of \(G^+=\langle G,\rho\rangle\)-internal exact
switches.  Charge the net gain from \(F_*\) to the final exact factor.
The supremum of this prepared net gain is still zero, while the release
\(\Delta_H^Q(G,\rho)\) is unchanged by the preparation.

#### Proof

Every component child is an exact factor, so global minimality gives
\(\mathcal Q_H(F_I)\ge\mathcal Q_H(F_*)\).  The empty cut attains equality,
proving (6.4).  The release telescope gives (6.3), and pigeonholing its
\(n-1\) nonnegative terms proves (0.10).

A \(G\)-internal switch preserves every \(G\)-orbit total.  Hence it
preserves both the old \(G\)-floor and the candidate \(G^+\)-floor, so it
does not change the release.  Every prepared endpoint remains an exact
factor and therefore has energy at least that of \(F_*\); the do-nothing
route attains zero.  This proves the preparation-safe statement.
\(\square\)

At a global minimizer, (1.6) strengthens (6.4) to

\[
 \boxed{
 \varrho_\rho=A_\rho,
 \qquad V_\rho\ge A_\rho
 \quad\text{for every transposition }\rho.
 }
 \tag{6.5}
\]

Thus every signed cut is locked and fair component variance is at least the
coherent displacement.

### Theorem 6.3 -- the corrected spectral floor does not select a productive bridge

Let

\[
 f_q=\mu_q(F_*)-\frac W{N_q}\mathbf1.
\]

Exact point regularity kills Johnson degrees zero and one.  For unordered
coordinate transpositions,

\[
 \boxed{
 \sum_\rho\|f-\rho f\|_H^2
 \ge4(n-1)\|f\|_H^2.
 }
 \tag{6.6}
\]

Moreover

\[
 \|f\|_H^2=B_H+\mathcal Q_H(F_*),
 \tag{6.7}
\]

where

\[
 B_H=\sum_{q\le H}\frac{N_q\theta_q(1-\theta_q)}{c_q},
 \qquad
 \theta_q=\frac{\delta_q}{N_q}.
\]

Hence some transposition satisfies

\[
 \boxed{
 A_\rho=\|f-\rho f\|_H^2
 \ge\frac8n\bigl(B_H+\mathcal Q_H(F_*)\bigr),
 \qquad \Gamma_\rho^*=0.
 }
 \tag{6.8}
\]

There is also a coordinate spanning tree \(T\) such that

\[
 \boxed{
 \sum_{\rho\in E(T)}A_\rho
 \ge\frac{8(n-1)}n
 \bigl(B_H+\mathcal Q_H(F_*)\bigr),
 }
 \tag{6.9}
\]

while every one of its direct bridge cubes is locked.

#### Proof

On Johnson degree \(j\), the unordered-transposition Laplacian identity is

\[
 \sum_\rho\|v-\rho v\|_2^2
 =2j(n-j+1)\|v\|_2^2.
\]

For \(j\ge2\), the least coefficient is \(4(n-1)\), proving (6.6).
Identity (6.7) is the scalar equality between variance about the fractional
mean and excess above the two adjacent integral floors.  Averaging (6.6)
over the \(\binom n2\) transpositions proves (6.8).

In a uniformly random labelled spanning tree, symmetry gives edge
probability \(2/n\).  Therefore the expected tree sum is \(2/n\) times the
left side of (6.6); some tree attains at least the expectation, proving
(6.9).  Locking is (6.4).  \(\square\)

The constant \(4(n-1)\) is a sum over all unordered transpositions; it is
not a per-bridge bound.  The averaged coefficient is \(8/n\).  Also,
\(A_\rho\) is coherent squared displacement, not the exact integer
two-point-orbit release: parity plateaux can absorb part or all of it.
The subgroup telescope (6.3), not (6.6), supplies the exact integer release
in (0.10).

## 7. Consequences for \(\mathrm{AFR}_A\)

The exact results separate four statements which must not be conflated.

1. **Projected canonical capture is true.**  The private C8 components
   capture all release on the selected \((3,1)\) pairs.

2. **Full canonical depth-one capture by those components is false.**  The
   forced \((1,1)\to(0,2)\) companion pairs cancel the gain exactly for
   every component subset.

3. **Positive-density mesoscopic exact motion is true.**  The block
   construction of Theorem 3.2 changes \(\Theta(m)\) shallow slots per
   packet and a positive density of wreath rows overall.

4. **A bulk absorber does not follow.**  Its whole weighted overload
   capacity is only \(O_A(H_AB)=O_A(W/\sqrt m)\), and it has no nontrivial
   first-shadow kernel.  The \(3/8\)-tail is also \(o(W)\)-inert at each
   individual Gaussian depth, although its bundled triangle ledger is
   still \(O_A(W)\).

The global-minimum locking theorem is not a counterexample to the stated
\(\mathrm{AFR}_A\), because \(\mathrm{AFR}_A\) includes an additive
Catalan-scale residue.  At a minimizer, an estimate

\[
 \sum_t\Gamma_t^Q
 \ge\eta_A\sum_t\Delta_t^Q-C_AH_AB
\]

would read

\[
 0\ge\eta_A\mathcal Q_{H_A}(F_*)-C_AH_AB
\]

and would prove

\[
 \mathcal Q_{H_A}(F_*)
 \le\frac{C_A}{\eta_A}H_AB=o(W).
\]

Thus any successful proof must make a genuinely global assertion above the
residue scale.  The local theorem it still needs may be stated exactly as
follows.

> **Same-bridge leakage-correlation gate (UNPROVED).**  For every fixed
> \(A\), above total error \(O_A(H_AB)\), an adaptive coordinate forest
> admits a fresh bridge \(\rho\) and a cut of its genuinely recomputed
> components for which the leakage correlation in (5.5) captures a fixed
> positive fraction of the same bridge's subgroup release (1.4), with one
> common component sign across all \(q\le H_A\).

Theorem 2.1 shows why checking only designated hole--duplicate pairs is
insufficient.  Theorem 3.3 shows why packet abundance or mesoscopic
rebundling is insufficient.  Theorem 4.2 shows why positive-density root
turnover is insufficient at a fixed depth.  Theorem 5.1 identifies the
signed quantity which remains.  Theorems 6.1--6.3 show that deterministic
or averaged bridge selection cannot manufacture the missing correlation
from telescopes or spectral exposure alone.

No theorem here excludes a route which uses larger canonical components,
noncommuting preparation followed by genuinely new recomputed components,
or \(\Omega(n)\) renewed rounds.  Such a route must additionally prove:

1. correlation of high-amplitude target release with the same bridge's
   leakage derivatives;
2. dispersion of useful occurrences among components with favorable
   common multidepth signs;
3. bounded risk on already covered target pairs;
4. renewal without recycling the same owner core; and
5. total collateral loss \(O_A(H_AB)\).

These are unproved lemmas, not consequences of the present report.

## 8. Exact-factor, unlabelled, and objective caveats

1. Every switch used above is a complete ownership-component switch between
   two exact middle wreath factors.  No argument switches part of a
   component or mixes factors at different depths.

2. The mesoscopic blocks are bundles of independent exact coordinates, not
   newly connected ownership components.  Their exactness comes from the
   existing cube; rebundling does not create new signs.

3. The \(\ell^1\), hole, and overload ceilings do not automatically bound
   quadratic energy when target loads are large.  Theorem 3.5 records the
   explicit available depth-one amplitude bound and its limitation; no
   attainment or optimality of that ceiling is claimed.

4. The tail bounds are triangle-ledger upper envelopes.  The coefficients
   in (4.2) count candidate occurrences; they are not attained support
   sizes or lower bounds.

5. Theorem 2.1 does not assert that the full canonical \((2\ 3)\)-cube is
   depth-one flat.  It asserts flatness of the explicit private C8 subcube.

6. The profile and energy objectives are unlabelled.  Nothing constructs a
   common labelled owner across depths.  Labelled common-owner
   synchronization remains strictly stronger and only sufficient.

7. An exact-factor switching path is not a literal MTF chronology and does
   not directly construct a contiguous-OR word.

## 9. Independent audit

The decisive claims were audited independently in four directions.

### 9.1 Canonical owner and sign audit

The canonical audit independently checked:

1. the four old/new omitted-label order prefixes;
2. the exact rectangle orientation in (2.6);
3. the all-\(m\) suffix-local owner inversion giving loads \((3,1)\) and
   \((1,1)\);
4. the values
   \[
   \phi_1(3)+\phi_1(1)-2\phi_1(2)=2,
   \]
   \[
   2\phi_1(1)-\phi_1(0)-\phi_1(2)=-2;
   \]
5. fixed-position support disjointness; and
6. the exact zero sum for every component subset.

The sign convention was checked both from the C8 formula and from ownership:
the old owner of \(S_V\) is removed and its transposed row adds one owner to
\(\tau S_V\); the companion transfer has the same old-to-new orientation.

### 9.2 Mesoscopic-capacity audit

An independent capacity audit checked:

1. four nonzero \(\pm1\) cells at depth one and eight at every
   \(2\le q\le m-2\);
2. the fixed-\(p\) isometry (3.6), hence exact half-\(\ell^1\) value
   \(2k\);
3. the row bound \(T\le B/2\);
4. the constants \(4S_H-2\), \(2S_H-1\), \(\kappa_A\), and
   \(\kappa_A/8\);
5. the exact Catalan ratio in (3.7); and
6. the matching proof of the load cap (3.13) and transfer identity (3.16).

The audit explicitly rejected the invalid inference from \(\ell^1\)
capacity to an amplitude-free quadratic \(o(W)\) ceiling.

### 9.3 Multidepth-tail audit

The tail theorem was rederived independently.  The audit checked:

1. the block lengths in (4.3);
2. exactly \(r-q+1\) full-\(X_A\) and \(r-q+1\) full-\(Y_A\) cancellation
   classes when \(r\ge q\);
3. the endpoint \(q=r\), where exactly one class of each type remains;
4. the trivial-bound transition at \(q=r+1\), where the coefficient in
   (4.2) equals \(2n\);
5. the identity (4.6) and the absence of an extra factor two;
6. the \(3/8\) Catalan endpoint mass;
7. the constant \(5/(4\sqrt\pi)\); and
8. the distinction between rankwise \(o(W)\) and bundled \(O_A(W)\).

The audit emphasized that (4.2) is an upper candidate ledger, not a claim
that \(\Theta(m)\) distinct slots survive for a large component.

### 9.4 Same-bridge and global-locking audit

A separate audit checked:

1. the sign and factor \((q+1)^{-2}\) in (5.5);
2. transposition stability of each fresh component and invariance of its
   middle-root union;
3. disappearance of the raw containment-shadow term for a fresh component;
4. the zero-release correction in the release-weighted identity (6.2);
5. pathwise global-minimum locking for every exact endpoint;
6. invariance of a candidate bridge release under old-group preparation;
7. the \(1/(n-1)\) pigeonhole constant in (0.10);
8. the corrected \(4(n-1)\) unordered-transposition spectral floor;
9. the \(8/n\) averaged coefficient; and
10. the \(2/n\) edge probability used in the spanning-tree average.

No audit converts coherent displacement \(A_\rho\) into exact integer
profile release without the parity correction.  The report keeps those
quantities separate.

## 10. Final status

### Proved

1. A canonical \((2\ 3)\) bridge exposes at least
   \(2\operatorname{Cat}_{m-4}\) depth-one integer profile energy on
   explicit target pairs.
2. Those pairs have distinct private genuine C8 components.
3. Every private component has a forced companion pair which cancels its
   depth-one gain exactly; the entire private subcube is \(Q_1\)-flat.
4. A positive-density mesoscopic exact rebundling with \(\Theta(m)\)
   first-shadow motion per packet.
5. Its exact fixed-depth and weighted overload/hole capacity ceilings.
6. The absence of any nontrivial exactly first-shadow-neutral deep-only
   kernel in the fixed-colour local cube, and linear independence for the
   complete local atlas.
7. The depth-one quadratic amplitude ceiling and its exact constant.
8. Uniform rankwise \(o(W)\) inertness of the canonical \(3/8\)-mass tail
   throughout every fixed Gaussian window.
9. The exact fresh leakage-derivative formula and same-bridge cut identity.
10. The corrected release-weighted accounting identity and its limitation.
11. Preparation-safe global-minimum bridge locking.
12. The corrected spectral floor and a high-coherent-exposure spanning tree
    whose every direct bridge remains locked at a global minimizer.

### Unproved and not claimed

1. \(\mathrm{AFR}_A\).
2. A productive cut in the complete canonical \((2\ 3)\)-cube.
3. Favorable signs for the companion loads of larger components.
4. A bundled \(o(W)\) ceiling for the \(3/8\)-tail.
5. An amplitude-free quadratic consequence of the local \(\ell^1\)
   ceilings.
6. Renewal of useful fragmentation through \(\Omega(n)\) adaptive rounds.
7. \(\mathrm{FSP}_A\), MWB, labelled common-owner synchronization, or a
   literal contiguous-OR word.

The fifth-wave conclusion is therefore exact.  Coordinate-bridge exposure
and component abundance can coexist with zero captured heat inside one
genuine canonical exact-factor subcube.  Positive-density mesoscopic
rebundling exists but has only Catalan-residue overload capacity and no
nontrivial exactly first-shadow-neutral deep-only kernel.  For arbitrary
fresh components, the productive quantity
is the signed cross-correlation of leakage derivatives.  Selecting that
correlation for the same high-release bridge, above total
\(O_A(H_A\operatorname{Cat}_m)\) error, remains the precise open theorem.
