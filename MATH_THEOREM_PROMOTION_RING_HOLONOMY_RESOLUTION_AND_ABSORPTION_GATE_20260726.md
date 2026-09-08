# Promotion-ring owner factors: holonomy resolution, full codegrees, and the minimal absorber

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Retain the covering-side tuned parameters

\[
H=(1+o(1))\sqrt{m\log m},\qquad
M=m+H,\qquad s=m-H,
\]

\[
W=\binom{2m}{m},\qquad
N_H=\binom{2m}{s},\qquad
L=MN_H=W+E,
\]

where

\[
0\le E=O(WH/m)=o(W).                                    \tag{0.1}
\]

For every root \(A\in\binom{[2m]}s\), a frame is a cyclic order of
\(U=A^c\). It owns the \(M\) middle targets

\[
Y_j=A\cup I_\pi(j,H),\qquad j\in\mathbb Z_M.              \tag{0.2}
\]

The conclusions are these.

1. A capacity-one matching is not the correct terminal object. Even a
   perfect right matching can select at most \(W/M\) roots, while there
   are \(N_H=L/M\) roots. Thus it may be forced to leave

   \[
   N_H-\frac WM=\frac EM=O(N_HH/m).                       \tag{0.3}
   \]

   The desired scale is

   \[
   o(N_H/\sqrt m).                                        \tag{0.4}
   \]

   Since \(H/m=(1+o(1))\sqrt{\log m/m}\), the bound (0.3) is
   potentially larger than (0.4) by a factor \(\sqrt{\log m}\).
   Therefore the scalar excess \(E\) must be absorbed as second middle
   copies; it cannot uniformly be paid by omitted roots.

2. There is an exact higher-order resolution relaxation with no scalar
   obstruction. Let

   \[
   F=(M-1)!,\qquad
   D=\frac{(m!)^2}{s!},\qquad
   \alpha=\frac DF=\frac LW=1+\frac EW<2.                 \tag{0.5}
   \]

   Colour the entire frame catalogue with \(F\) colours. At each root,
   its \(F\) frames must receive all colours once. At a middle target
   and a fixed colour, require load one or two. The uniform fractional
   colouring has root load one and middle load \(\alpha\). An integral
   colouring would give, in every colour:

   * exactly one frame for every root;
   * every middle target at least once;
   * exactly \(E\) repeated middle occurrences.

   Thus it gives a zero-root-leave owner factor with the information-
   theoretic minimum middle collision mass \(E=o(W)\).

3. Finite-character holonomy can be imposed on the overflow rather than
   guessed from density. For fixed \(K\), define

   \[
   \chi_{B,\ell,a}(Y)
   =\exp\!\left(\frac{2\pi ia}{\ell}|Y\cap B|\right),
   \quad
   2\le\ell\le K,\quad 1\le a<\ell,\quad |B|=m.            \tag{0.6}
   \]

   If \(b_c(Y)\in\{0,1\}\) is the second-copy indicator in colour \(c\)
   and \(\delta=E/W\), the exact holonomy requirement is

   \[
   \max_{B,\ell,a}
   \left|
   \sum_Y\bigl(b_c(Y)-\delta\bigr)\chi_{B,\ell,a}(Y)
   \right|=o(E).                                           \tag{0.7}
   \]

   It rules out the parity and mod-three packet-free residuals while
   allowing the unavoidable \(E\) overflow.

4. Let \(\mathfrak B_H\) be the exact Gould--Kelly full-codegree
   bottleneck of the augmented root--middle frame hypergraph. If a
   diagonal nibble/absorption theorem had right leave

   \[
   O\!\left(W\mathfrak B_H^{-1+o(1)}\right),               \tag{0.8}
   \]

   and if the scalar overflow were absorbed as in item 2, then its root
   leave would be

   \[
   O\!\left(N_H\mathfrak B_H^{-1+o(1)}\right).             \tag{0.9}
   \]

   Consequently it reaches (0.4) exactly under the quantitative
   condition

   \[
   \boxed{\mathfrak B_H^{\,1-o(1)}\gg\sqrt m.}             \tag{0.10}
   \]

5. The pair term permits (0.10):

   \[
   \sqrt{\frac{D_{\min}}{C_2}}
   =(1+o(1))\frac m{\sqrt2}.                               \tag{0.11}
   \]

   The complete higher sequence is given by an exact circular-breakpoint
   formula, but the uniform extremal bound needed for (0.10) has not been
   proved. A sufficient, sharply weaker-than-linear statement is

   \[
   C_j\le
   D_{\min}\,
   m^{-(1/2+\varepsilon)(j-1)}
   \qquad(4\le j\le M+1)                                  \tag{0.12}
   \]

   for some fixed \(\varepsilon>0\). This would give
   \(\mathfrak B_H\ge m^{1/2+\varepsilon}\).

6. Current nibble theorems do not yield (0.4), even if (0.12) is granted.
   Their hierarchy fixes the edge uniformity before the degree limit,
   whereas here \(M+1\sim m\), and the published leftover carries a
   \((\log D)^A\) loss with
   \(\log D=\Theta(m\log m)\). The needed new result is therefore not
   another first-bite estimate. It is a group-respecting overflow
   absorber with a \(B^{-1+o(1)}\) diagonal leave and the character
   guarantee (0.7).

The exact minimal new theorem is stated in Section 6. No generic
quasirandomness assertion is used.

## 1. The middle frame hypergraph and the scalar excess

Let \(\mathcal A=\binom{[2m]}s\) be the root set and
\(\mathcal Y=\binom{[2m]}m\) the middle target set. For
\(A\in\mathcal A\), let \(\mathcal C_A\) be the \(F=(M-1)!\) directed
cyclic orders of \(A^c\), modulo rotation.

The augmented frame hypergraph \(\mathcal G\) has vertex set
\(\mathcal A\sqcup\mathcal Y\). Its edge \(e=(A,\pi)\) consists of the
root \(A\) and the \(M\) targets (0.2).

Every root has degree \(F\). Every middle target has degree

\[
D=\binom mH H!m!=\frac{(m!)^2}{s!}.                       \tag{1.1}
\]

Moreover

\[
\frac DF=\frac{M}{\lambda_H}=\frac LW=\alpha.             \tag{1.2}
\]

A matching using \(r\) frame edges covers exactly \(r\) roots and \(Mr\)
middle targets. Hence, for a matching with middle leave \(h\) and root
leave \(t=N_H-r\),

\[
h=W-M(N_H-t)=Mt-E.                                        \tag{1.3}
\]

Since \(h\ge0\),

\[
t\ge\left\lceil\frac EM\right\rceil.                       \tag{1.4}
\]

This proves the capacity-one obstruction (0.3). It is purely scalar and
does not involve codegrees.

The obstruction disappears if middle load two is allowed. A selection
of one frame per root has \(L=W+E\) middle occurrences. If every target
has load one or two, exactly \(E\) targets have load two and none is
missed. This is the unique floor/ceiling optimum.

## 2. The exact owner-resolution system

Introduce variables

\[
x_{e,c}\in\{0,1\},
\qquad e\in E(\mathcal G),\quad c\in[F].
\]

The owner resolution \(\mathrm{OR}\) is

\[
\sum_{c=1}^{F}x_{e,c}=1
\qquad(e\in E(\mathcal G)),                               \tag{2.1}
\]

\[
\sum_{e\ni A}x_{e,c}=1
\qquad(A\in\mathcal A,\ c\in[F]),                         \tag{2.2}
\]

and

\[
1\le \sum_{e\ni Y}x_{e,c}\le2
\qquad(Y\in\mathcal Y,\ c\in[F]).                         \tag{2.3}
\]

### Proposition 2.1 (fractional feasibility and exact integral ledger)

The uniform point

\[
x_{e,c}=\frac1F                                           \tag{2.4}
\]

satisfies the linear relaxation of (2.1)--(2.3). If the system has an
integral solution, every colour class selects exactly one frame per root,
has zero middle holes, and has collision mass exactly \(E\).

#### Proof

Equation (2.1) is immediate. The load in (2.2) is \(F/F=1\). The load
in (2.3) is \(D/F=\alpha\), and \(1\le\alpha<2\) for large \(m\).

In an integral colour, (2.2) selects \(N_H\) frames and therefore
\(MN_H=L=W+E\) middle occurrences. Equation (2.3) says every one of the
\(W\) targets has load one or two. Hence exactly \(E\) have load two.
\(\square\)

This is the correct higher-order resolution: a capacity-one edge
colouring cannot use all roots, while (2.1)--(2.3) absorbs the exact
overshoot without any root leave.

## 3. Finite-character holonomy

For a function \(f:\mathcal Y\to\mathbb C\), define the order-\(K\)
holonomy seminorm

\[
\|f\|_{\mathrm{hol},K}
=
\max_{\substack{B\subset[2m],\ |B|=m\\
                 2\le\ell\le K,\ 1\le a<\ell}}
\left|\sum_{Y\in\mathcal Y}
f(Y)\chi_{B,\ell,a}(Y)\right|.                            \tag{3.1}
\]

The parity trap is \(\ell=2\), and the odd-rank mod-three trap is
detected by \(\ell=3\).

For an integral colour \(c\), put

\[
\mu_c(Y)=\sum_{e\ni Y}x_{e,c},\qquad
b_c(Y)=\mu_c(Y)-1.
\]

Under (2.3), \(b_c\) is the indicator of the \(E\)-set of overflow
targets. The holonomy-balanced strengthening of \(\mathrm{OR}\) is

\[
\boxed{
\|b_c-(E/W)\mathbf1\|_{\mathrm{hol},K}=o(E)
\quad\text{for every }c.}                                \tag{3.2}
\]

This is a deterministic condition. It cannot be replaced by exact
one-coordinate margins: the balanced parity residuals are coordinate
regular.

For an absorption theorem involving an uncovered root set
\(\mathcal R\subseteq\mathcal A\), use the analogous seminorm

\[
\|\mathbf1_{\mathcal R}-(|\mathcal R|/N_H)\mathbf1\|
_{\mathrm{hol},K}^{\rm root},                              \tag{3.3}
\]

with \(|A\cap B|\) in the character. A trajectory is
finite-character safe if (3.3) is \(o(|\mathcal R|)\) at every stopping
scale above \(N_H/\sqrt m\).

## 4. The exact full-codegree parameter

Let \(C_j\) be the maximum number of frame edges containing a prescribed
\(j\)-set of augmented vertices. Any set containing two roots has
codegree zero. A root--middle pair has codegree \(H!m!\), which is
superpolynomially small relative to both incident degrees. Thus the
only possible full-codegree obstruction is a family of middle targets.

For distinct \(Y_1,\ldots,Y_j\), the exact codegree is

\[
C(Y_1,\ldots,Y_j)
=
\sum_{\substack{A\subseteq\cap_iY_i\\|A|=s}}
c_{A^c}(Y_1\setminus A,\ldots,Y_j\setminus A),             \tag{4.1}
\]

where \(c_U(I_1,\ldots,I_j)\) counts cyclic orders of \(U\) in which all
\(I_i\) are \(H\)-windows.

For

\[
a_J=\#\{u\in U:\{i:u\in I_i\}=J\},
\]

and starts \(t=(0,t_2,\ldots,t_j)\), put

\[
c_J(t)=\#\{z\in\mathbb Z_M:
              \{i:z\in[t_i,t_i+H)\}=J\}.
\]

Then

\[
c_U(I_1,\ldots,I_j)
=
\sum_{\substack{t_2,\ldots,t_j\ {\rm distinct}\\
                 c_J(t)=a_J\ \forall J}}
\prod_{J\subseteq[j]}a_J!.                                \tag{4.2}
\]

Equations (4.1)--(4.2) are the complete higher-codegree generating
formula; there is no missing formal coefficient.

Put \(D_{\min}=F=D/\alpha\), and define

\[
\mathfrak B_H=
\min\left\{
\sqrt{\frac{D_{\min}}{C_2}},
\min_{4\le j\le M+1}
\left(\frac{D_{\min}}{C_j}\right)^{1/(j-1)}
\right\}.                                                 \tag{4.3}
\]

The exact pair calculation gives

\[
\frac{C_2}{D_{\min}}
=\frac{2\alpha}{m^2},
\qquad
\sqrt{\frac{D_{\min}}{C_2}}
=(1+o(1))\frac m{\sqrt2}.                                 \tag{4.4}
\]

Thus pair codegrees allow much more than the threshold \(\sqrt m\).
The unresolved extremal inequality is the second term in (4.3).

### Proposition 4.1 (the exact codegree threshold for the desired root leave)

Assume a group-respecting diagonal matching theorem whose right leave is

\[
\ell_R\le W\mathfrak B_H^{-1+o(1)},                        \tag{4.5}
\]

and assume the \(E\) scalar excess is handled by overflow vertices rather
than omitted roots. Then the root leave is

\[
\ell_{\rm root}
\le N_H\mathfrak B_H^{-1+o(1)}.                            \tag{4.6}
\]

Consequently (4.6) is \(o(N_H/\sqrt m)\) if and only if (0.10) holds.

#### Proof

After overflow absorption, every omitted frame edge accounts for \(M\)
units of right deficit, up to the terminal absorber's lower-order
boundary. Therefore

\[
M\ell_{\rm root}\le\ell_R+o(W/\sqrt m).
\]

Use \(W/M=(1+o(1))N_H\) and (4.5). The last assertion is immediate.
\(\square\)

The sufficient coefficient inequality (0.12) makes every higher term in
(4.3) at least \(m^{1/2+\varepsilon}\), and hence proves (0.10). It is
the minimal purely codegree statement presently missing. Proving the
stronger natural estimate

\[
C_j\le D_{\min}(cm)^{-(j-1)}                               \tag{4.7}
\]

would give \(\mathfrak B_H=\Theta(m)\), but (4.7) is not needed for the
requested root scale.

## 5. Why the present nibble still does not close

The valid conditioned first-bite calculation is

\[
\frac1{D_{\min}}
\sum_{\{Y,Z\}\subset e}D(Y,Z)
=\frac2m+O(m^{-2}).                                       \tag{5.1}
\]

It proves that an isolated bite loses only an \(o(1)\) fraction to
internal codegree overlap. It does not prove regeneration of an
arbitrary residual, and finite-character packet-free states show that
such a hereditary assertion is false.

Even if (0.12) were supplied, the current full-codegree nibble theorem
has the fixed-uniformity hierarchy

\[
\frac1D\ll\frac1A\ll\gamma\ll\frac1M.
\]

Its formal leftover is

\[
V\mathfrak B_H^{-1+\gamma}(\log D)^A.                     \tag{5.2}
\]

Here

\[
\log D=\Theta(m\log m),\qquad \mathfrak B_H\le O(m).
\]

There is no diagonal choice of \(A,\gamma\) for which (5.2) is
\(o(W/\sqrt m)\); the explicit proof hierarchy is already vacuous before
the desired root conversion. Thus the full codegree sequence may be
geometrically adequate while the available theorem is quantitatively
inapplicable.

The obstruction is not a request for a better independent nibble.
Independent frame choices have \(\Theta(W\sqrt m)\) aggregate nested
floor energy. The new selection must simultaneously:

1. retain the small-overlap first bite;
2. prevent drift into the character states measured by (3.1);
3. absorb the scalar excess \(E\) as second copies; and
4. round the remaining roots with loss \(B^{-1+o(1)}\), without a
   \((\log D)^A\) penalty.

## 6. Minimal new absorption theorem

The following statement is sufficient and isolates exactly what is not
provided by current nibble technology.

### Holonomy-safe owner absorption theorem \(\mathrm{HOA}_K\)

For every fixed \(K\ge3\), there are functions

\[
\eta_m=o(m^{-1/2}),\qquad \zeta_m=o(1),
\]

and a family of alternating frame absorbers with a right reservoir of
size \(o(W)\), such that the following holds.

Start from any first-bite packet matching whose uncovered root set
\(\mathcal R\) and unused right set satisfy:

1. the exact root/right incidence balance;
2. all normalized degrees and full codegrees down to scale
   \(\mathfrak B_H\) satisfy the inherited versions of (4.3);
3. the root and right residuals have order-\(K\) holonomy at most
   \(\zeta_m\) in the seminorms (3.1), (3.3).

Then alternating absorber switches produce a frame selection with:

\[
|\mathcal R_{\rm final}|\le\eta_mN_H
=o(N_H/\sqrt m),                                         \tag{6.1}
\]

\[
\mu(Y)\in\{1,2\}\quad\text{outside }o(W/\sqrt m)
\text{ exceptional targets},                             \tag{6.2}
\]

\[
\sum_Y(\mu(Y)-1)_+=E+o(W),                                \tag{6.3}
\]

and

\[
\|(\mu-1)-(E/W)\mathbf1\|_{\mathrm{hol},K}=o(E).           \tag{6.4}
\]

If the theorem is iterated over the nested tag colours, it must preserve
their aligned thread divisibilities and leave total floor energy \(o(W)\).

### Why this is minimal

* Without (6.3), the capacity-one lower bound (1.4) can exceed the target
  (6.1).
* Without (6.4), exact point margins permit parity or mod-three
  packet-free terminal states.
* Without the \(o(m^{-1/2})\) root rate, a root leave can expand to
  order \(W\) across the Gaussian nested colours.
* A first-bite theorem alone gives none of these three conclusions.

A stronger but cleaner sufficient route is an integral solution of the
owner resolution (2.1)--(2.3) satisfying (3.2), followed by the analogous
all-rank quota resolution. That would have zero root leave. The
absorption theorem above asks only for the asymptotically necessary
portion of that resolution.

## 7. Exact boundary

The current rigorous status is:

* fractional owner resolution with exact overflow: proved;
* pair codegrees and the complete higher-codegree coefficient formula:
  proved;
* valid small-overlap first bite: proved;
* capacity-one root leave \(o(N_H/\sqrt m)\): not uniformly possible
  from the scalar ledger alone;
* full-codegree sufficiency for the target: exactly
  \(\mathfrak B_H^{1-o(1)}\gg\sqrt m\);
* the needed higher-codegree inequality (0.12): open;
* a uniform theorem converting that inequality into the desired leave:
  absent from current nibble results;
* the minimal replacement: \(\mathrm{HOA}_K\).

Thus the next proof should not iterate the first bite generically. It
should build an overflow-aware alternating resolution and prove that its
absorber incidence remains expanding after quotienting the finitely many
character-holonomy modes.
