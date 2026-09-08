# The phase-dense ternary carry: exact physical tag-Walsh Gram and a Gaussian fixed-frame obstruction

## 0. Verdict

The ternary-carry fusion from thread H genuinely repairs two defects of the
earlier R/G composition.  It acts on every activity cell, and its shore is a
state-dependent function of the ternary digits rather than a fixed shore.
It therefore gives the advertised long components and the exact middle-owner
factor.

It does **not**, in the parameter regime used in H, remove the fixed-pair
Gaussian shadow deficit.  The reason is precise.  Relative to the static
all-new factor, the carry changes

\[
 E=\frac{3(1-3^{-t})}{4h}\,G                                      \tag{0.1}
\]

outgoing edges on the good owner set of size \(G=W-o(W)\).  Consequently, at
depth \(q\), at most \(qE\) starts have a different physical target.  When
\(q=A\sqrt m\) and \(h/\sqrt m\to\infty\), this is \(o(W)\).  The static
all-new factor is supported by one fixed coordinate pairing, so the positive
Gaussian pair-type capacity deficit gives \(\delta_AW-o(W)\) missing targets
for some \(\delta_A>0\).  The carry can change the number of missing targets
by at most \(qE=o(W)\).  Thus

\[
 M_{\lfloor A\sqrt m\rfloor}^{\rm carry}
 \ge \delta_AW-o(W).                                               \tag{0.2}
\]

In particular, the required \(o(W)\) hole conclusion, and hence the
coefficient-one gate, does not follow from this carry.  Since failure at one
Gaussian depth already defeats the aggregate hole gate, summing over depths
cannot repair the problem.

The Walsh calculation below explains the apparent paradox.  The carry
predicate has exponentially many nonzero ternary Walsh coefficients, but its
physical \(L^1\) mass is only \(O(1/h)\) per edge and its depth-\(q\) incidence
perturbation has squared Hilbert--Schmidt norm \(O(qW/h)\).  It is spectrally
dense but physically sparse.

## 1. Exact carry state space

Fix a good canonical macrocell \(P\).  Suppress the exterior rows, which are
constant along the local factor.  The owner states can be indexed by

\[
 \Omega_P=B\times K\times Z\times \mathbb Z_{2h},\qquad
 B=\mathbb Z_2^t,\quad Z=\mathbb Z_3^t.                             \tag{1.1}
\]

Here \(b\in B\) chooses one of the two local holonomy orbits in each activity
block, \(k\in K\) is the Hamming syndrome translate, \(z\in Z\) is the vector
of ternary orbit coordinates, and the last coordinate is the phase.  The
carry leaves \(b\) and \(k\) fixed.  After one \(2h\)-phase lap, it sends the
base-three integer represented by \(z\) to \(z+1\pmod {3^t}\).  Hence every
component has length \(2h3^t\), exactly as in H.

For fixed \(k\), write the ordered port times as

\[
 i_1(k),\ldots,i_t(k).
\]

At port \(i_s(k)\), the carry uses the opposite-shore matching precisely when

\[
 c_s(z):={\bf 1}\{z_{i_1}=\cdots=z_{i_{s-1}}=0\}=1.                \tag{1.2}
\]

The empty condition makes \(c_1\equiv1\).  This predicate is independent of
the active digit \(z_{i_s}\), and is therefore constant on the entire
six-point alternating fibre.  This is exactly what makes the local switch
legal.

## 2. The carry Walsh field

Let \(\zeta=e^{2\pi i/3}\), and use the product character basis on
\(Z=\mathbb Z_3^t\).  Since

\[
 {\bf 1}\{x=0\}=\frac13(1+\zeta^x+\zeta^{-x}),
\]

(1.2) has the exact expansion

\[
 c_s(z)
 =3^{-(s-1)}
   \sum_{\alpha\in\mathbb Z_3^{\{i_1,\ldots,i_{s-1}\}}}
   \zeta^{\alpha\cdot z}.                                         \tag{2.1}
\]

Thus \(c_s\) has \(3^{s-1}\) nonzero ternary coefficients, all equal to
\(3^{-(s-1)}\), and

\[
 \mathbb E c_s=3^{-(s-1)},\qquad
 \sum_s\mathbb E c_s=\frac32(1-3^{-t}).                            \tag{2.2}
\]

There is no nonzero \(B\)-frequency and no nonzero \(K\)-frequency in (2.1):
the carry multiplier is constant in the persistent tags \(b,k\).  Equivalently,
in the full tag basis

\[
 \chi_{\rho,\kappa,\alpha}(b,k,z)
 =(-1)^{\rho\cdot b}\,\kappa(k)\,\zeta^{\alpha\cdot z},           \tag{2.3}
\]

the multiplier by \(c_s\) is supported only on \(\rho=0\) and the trivial
character \(\kappa=1\).  The carry therefore supplies rich ternary mixing but
does not by itself mix either of the two persistent physical tag quotients.

One may instead diagonalize the one-lap odometer by the characters of
\(\mathbb Z/3^t\mathbb Z\).  This gives all \(3^t\)-th roots of unity as the
one-lap spectrum.  Formula (2.1), however, is the useful basis for seeing the
physical size of the shore-change field: exponential spectral support is
compatible with the geometrically decreasing means in (2.2).

Counting one occurrence of the relevant port among the \(2h\) phase edges
and the two local three-cycles gives exactly H's ledger

\[
 \frac EG=\frac{3(1-3^{-t})}{4h}.                                  \tag{2.4}
\]

## 3. The physical tag-Gram operator

Let \({\cal T}_q^-\) be the rank-\((m-q)\) target set; the upper case is
identical after complementing.  For \(F\in\{0,C\}\), where \(0\) denotes the
static all-new factor and \(C\) the carry factor, define the physical incidence
operator

\[
 A_{P,q}^{F}(T,\omega)
 ={\bf 1}\{\text{the depth-}q\text{ window from }\omega
               \text{ in }F\text{ has target }T\}.                \tag{3.1}
\]

Every column of \(A_{P,q}^{F}\) contains exactly one \(1\).  For two
macrocells \(P,R\), the exact physical tag-Gram operator is

\[
 {\cal K}_{P,R,q}^{F}=(A_{P,q}^{F})^*A_{R,q}^{F}.                  \tag{3.2}
\]

Its \((\omega,\omega')\)-entry is one exactly when the two tagged windows
have the same literal target.  Thus (3.2), unlike a random or abstract trace
surrogate, retains every physical target equality.

Writing \(A_q^F=[A_{P,q}^F]_P\), the full physical Gram is the block operator

\[
 {\cal K}_q^F=(A_q^F)^*A_q^F
             =\bigl({\cal K}_{P,R,q}^F\bigr)_{P,R}.                \tag{3.2a}
\]

Thus no cross-packet collision has been discarded in passing to (3.2).

Let \({\cal F}_P\) denote any unitary tag Fourier transform, using (2.3) in
\((b,k,z)\) and ordinary Fourier characters in phase.  Then

\[
 \widehat{\cal K}_{P,R,q}^{F}
 ={\cal F}_P{\cal K}_{P,R,q}^{F}{\cal F}_R^{-1}                   \tag{3.3}
\]

is the combined physical tag-Walsh Gram.  If
\(e_0=|\Omega_P|^{-1/2}{\bf 1}\), then the actual cross-packet collision
count is its constant--constant matrix coefficient:

\[
 \langle A_{P,q}^{F}{\bf1},A_{R,q}^{F}{\bf1}\rangle
 =|\Omega_P|^{1/2}|\Omega_R|^{1/2}
   \langle e_0,{\cal K}_{P,R,q}^{F}e_0\rangle.                    \tag{3.4}
\]

All ternary states are used in a complete factor.  Hence the nonconstant
carry characters are not free packet signs: they are internal modes of
\(A^C\).  Only their deterministic contribution to the constant--constant
coefficient in (3.4) can alter the collision count.

Put

\[
 D_{P,q}=A_{P,q}^{C}-A_{P,q}^{0}.
\]

The exact Gram expansion is

\[
 \begin{aligned}
 {\cal K}_{P,R,q}^{C}
 ={}&{\cal K}_{P,R,q}^{0}
 +(A_{P,q}^{0})^*D_{R,q}
 +D_{P,q}^*A_{R,q}^{0}
 +D_{P,q}^*D_{R,q}.                                                \tag{3.5}
 \end{aligned}
\]

Equation (3.5), conjugated by the two tag Fourier transforms, is the requested
combined physical Walsh--Gram operator.  It also locates exactly where a
negative covariance could occur: only in the three displayed perturbation
terms.

## 4. Deterministic size of the Gram perturbation

Let \(S_{P,q}\) be the set of starts whose depth-\(q\) window encounters an
edge on which the carry and static matchings differ.  Every changed directed
edge has at most one predecessor start at each of the \(q\) possible positions
in a window.  Therefore

\[
 |S_{P,q}|\le qE_P.                                                \tag{4.1}
\]

For \(\omega\notin S_{P,q}\), the entire physical window, and hence its
literal target, is identical in the two factors.  Each remaining column of
\(D_{P,q}\) is either zero or the difference of two standard basis vectors.
It follows that

\[
 \|D_{P,q}\|_{\rm HS}^2\le2qE_P.                                 \tag{4.2}
\]

Unitary Fourier conjugation preserves (4.2).  Thus the aggregate spectral
energy of all the ternary modes introduced into the literal depth-\(q\)
incidence table is at most \(2qE_P\).  Summing over macrocells and using
(0.1),

\[
 \sum_P\|D_{P,q}\|_{\rm HS}^2
 \le \frac{3(1-3^{-t})q}{2h}\,G.                                 \tag{4.3}
\]

For \(q=A\sqrt m\) and \(h/\sqrt m\to\infty\), (4.3) is \(o(W)\).
This is the exact sense in which the carry is Fourier-dense but physically
too sparse at a fixed Gaussian depth.

Equivalently, the fraction of good starts whose literal target can differ
from the fixed-frame baseline is bounded by

\[
 \frac{|S_q|}{G}\le
 \frac{3(1-3^{-t})q}{4h}=o(1).                                   \tag{4.3a}
\]

There is an even sharper statement for holes.  Let

\[
 Z_q^F(T)=\sum_{P,\omega} A_{P,q}^F(T,\omega)
\]

be the target load.  From (4.1),

\[
 \|Z_q^C-Z_q^0\|_1\le2qE.                                        \tag{4.4}
\]

Replacing the image of one start changes the cardinality of the covered
target set by at most one.  Consequently

\[
 |M_q^C-M_q^0|\le qE,                                             \tag{4.5}
\]

where \(M_q^F=|\{T:Z_q^F(T)=0\}|\).  This conclusion is statewise and uses
neither independence nor a second-moment estimate.

## 5. The surviving fixed-pair capacity cut

In the static all-new factor, every active transition belongs to the same
global coordinate pairing: on a selected eight-block its pairs are
\(ac,bd,uv,wx\), and the pairing may be completed arbitrarily on frozen
coordinates.  Hence the established fixed-pair type cut applies.

For completeness, if a middle set has \(f\) full coordinate pairs, then the
number of middle owners of that type is

\[
 V_f=\frac{m!}{f!^2(m-2f)!}\,2^{m-2f}.                            \tag{5.1}
\]

A rank-\((m-q)\) target with \(f\) full pairs has count

\[
 T_{f,q}
 =\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.                       \tag{5.2}
\]

Any resolution confined to this pair frame has at most \(V_f\) available
middle owners for the relevant type demand.  Thus

\[
 M_q^0\ge D_{m,q}:=\sum_f(T_{f,q}-V_f)_+.                          \tag{5.3}
\]

Here is the short Gaussian deduction, included to make the scale explicit.
For a target chosen uniformly from rank \(m-q\), its full-pair count has
saddle

\[
 f_*=\frac{(m-q)^2}{4m}
\]

and a local central limit law on scale \(\sqrt m\).  If
\(\lambda_{f,q}=V_f/T_{f,q}\), then uniformly near the saddle

\[
 \log\lambda_{f_*,q}=-q^2/m+o(1),\qquad
 \partial_f\log\lambda_{f,q}=O(q/m).                              \tag{5.4}
\]

Fix \(A>0\) and take \(q=\lfloor A\sqrt m\rfloor\).  Choose a fixed
\(\varepsilon>0\), small in terms of \(A\).  On
\(|f-f_*|\le\varepsilon\sqrt m\), (5.4) gives
\(\lambda_{f,q}\le e^{-A^2/2}<1\) for all sufficiently large \(m\), while
the local central limit law assigns this interval a positive limiting target
mass.  Also
\(\binom{2m}{m-q}/W\to e^{-A^2}\).  Therefore, for a constant
\(\delta_A>0\),

\[
 q=\lfloor A\sqrt m\rfloor,qquad
 D_{m,q}\ge\delta_AW+o(W).                                        \tag{5.5}
\]

Deleting the exponentially small canonical-macrocell leave can only reduce
the available supply; allowing every leave owner one additional literal
target changes (5.3) by at most \(u=o(W)\).  Combining (0.1), (4.5), and
(5.5) yields

\[
 \begin{aligned}
 M_q^C
 &\ge \delta_AW-u-qE\\
 &=\delta_AW-o(W).                                                 \tag{5.6}
 \end{aligned}
\]

because \(q/h\to0\).  Complementation gives the corresponding upper-depth
statement with the usual one-step shift, although one lower depth already
suffices for the obstruction.

## 6. Interpretation as a covariance no-go

The old R/G audit failed before reaching (3.5): R did not have the required
literal trace injectivity, while G was confined to an all-main shore.  H's
carry overcomes those formal composition defects.  The obstruction here is
different and strictly later in the argument.

The carry's negative correlations are temporal correlations among shore
choices inside a complete odometer orbit.  They do not constitute independent
cross-packet signs.  More importantly, their projection on the fixed-pair
capacity witness can move only \(qE=o(W)\) literal occurrences.  An
order-\(W\) deficit remains on that witness.  Therefore no rearrangement of
the nonzero ternary Walsh terms in (3.5) can produce the negative covariance
needed for \(o(W)\) holes while (0.1) and \(q/h\to0\) remain in force.

This does not prove that every ternary-carry construction is impossible.  It
isolates the necessary change:

* either a positive fraction of Gaussian \(q\)-windows must cross a genuine
  frame-changing edge, so one needs \(qE=\Omega(W)\), or
* the baseline itself must mix coordinate pairings across owners before the
  sparse carry is applied.

If instead \(h=\Theta(\sqrt m)\), the bound \(qE=\Theta(W)\) no longer decides
the issue.  But the H regime used to cover every fixed Gaussian depth has
\(H/\sqrt m\to\infty\), \(h=\Theta(H)\), and therefore falls exactly under
(5.6).
