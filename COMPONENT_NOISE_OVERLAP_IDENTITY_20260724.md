# Component-noise overlap identities and rigidity

This note uses only exact factors and exact component switches.  It does not
prove the component-noise upper bound.  Its point is to identify exactly what
that upper bound contains, and to isolate two structural obstructions which
are invisible in the scalar heat calculation.

Put \(n=2m+1\).  Fix a height \(H<m\), and at depth \(q\) put

\[
r_q=m-q,\qquad
f_q=\mu_q-\frac{W}{N_q}{\bf 1}.
\]

Use the weighted Hilbert space

\[
 \mathscr H_H=
 \bigoplus_{q=1}^H
 \mathbb R^{\binom{[n]}{r_q}},
 \qquad
 \langle x,y\rangle_H=
 \sum_{q=1}^H\frac{\langle x_q,y_q\rangle}{c_q}.
\]

Write

\[
 S_H=\|f\|_H^2=B_H+\Phi_H,
 \qquad
 B_H=\sum_{q\le H}\frac{V_q^{\min}}{c_q},
 \qquad
 \Phi_H=\sum_{q\le H}\frac{\|f_q\|_2^2-V_q^{\min}}{c_q}.
\]

Thus \(\Phi_H\) is the full integer variance above its floor, twice the
pair-collision excess used in some companion notes.

All coordinate transpositions below are unordered.

## 1. Component equivariance

Fix a transposition \(\tau=(a\ b)\), and overlay an exact factor \(F\)
with \(\tau F\).  Let (C) be one connected component of the bipartite
overlap graph, with left rows (L_C\subseteq F) and right rows
(R_C\subseteq\tau F).

For every left row \(P\), the corresponding right row \(\tau P\) is in the
same component.  Indeed, among the (n) cyclic middle intervals of (P),
the total number of incidences with (a,b) is (2m=n-1).  Hence some
middle interval contains both of (a,b), or neither of them.  That interval
is fixed by \(\tau\), and gives an overlap edge from (P) to \(\tau P).
Since a finite regular bipartite component has equally many vertices on its
two sides,

\[
 \boxed{R_C=\tau L_C.}                                      \tag{1.1}
\]

Let (u_{q,C}) and (w_{q,C}) be the depth-(q) histograms of the two
sides.  Then

\[
 \boxed{w_{q,C}=\tau u_{q,C}.}                              \tag{1.2}
\]

If (k_C=|L_C|=|R_C|), each side has total mass (nk_C), and every
coordinate belongs to exactly (r_qk_C) of its cyclic (r_q)-intervals.
Consequently

\[
 d_{q,C}:=w_{q,C}-u_{q,C}
\]

has zero total and zero point margins, component by component.  In Johnson
language,

\[
 \boxed{d_{q,C}\in\bigoplus_{j\ge2}E_j.}                    \tag{1.3}
\]

The same statement holds for the full centered histogram (f_q).

There is also a useful contracted description of the overlap graph.  Its
vertices are the rows of (F).  For every nonfixed middle pair
\(\{A,\tau A\}\), join the owner of (A) to the owner of \(\tau A\).
Loops coming from fixed middle sets do not change components.  The connected
components of this row graph are exactly the sets (L_C).

## 2. Exact orbit and correlation formula

For a nonfixed two-element \(\tau\)-orbit
\(p=\{S,\tau S\}\) in rank (r_q), choose one representative (S) and
put

\[
 z_{C,q,p}=u_{q,C}(S)-u_{q,C}(\tau S).
\]

Fixed targets contribute zero.  From (1.2),

\[
 \|d_{q,C}\|_2^2=2\sum_p z_{C,q,p}^2,
 \qquad
 \|\tau\mu_q-\mu_q\|_2^2
 =2\sum_p\left(\sum_Cz_{C,q,p}\right)^2.             \tag{2.1}
\]

Define, for this transposition,

\[
 N_{\tau,H}=\sum_C\|d_C\|_H^2,
 \qquad
 A_{\tau,H}=\left\|\sum_Cd_C\right\|_H^2.
\]

Then the exact component-correlation identity is

\[
 \boxed{
 N_{\tau,H}-A_{\tau,H}
 =-4\sum_{q\le H}\frac1{c_q}
   \sum_p\sum_{C<D}z_{C,q,p}z_{D,q,p}.}              \tag{2.2}
\]

Thus fair component switching loses against coherent smoothing precisely
when the aggregate cross-component correlation is nonpositive.  Neither
connectivity nor zero point margins determines the sign of the right-hand
side.

## 3. The whole switching cube

For \(I\subseteq\mathcal C_\tau(F)\), switch exactly the components in
\(I\).  In the weighted Hilbert space its centered profile is

\[
 f_I=f+\sum_{C\in I}d_C.
\]

Put

\[
 e_\tau(I)=\|f_I\|_H^2-\|f\|_H^2.
\]

Switching all components gives \(\tau F\), so \(e_\tau(\mathcal C)=0\).
Moreover

\[
 \tau f_I=f_{I^c},
 \qquad e_\tau(I)=e_\tau(I^c).                      \tag{3.1}
\]

If (I) is a uniform random subset, the exact fair-drift identity is

\[
 \boxed{
 \mathbb E_I e_\tau(I)
 =\frac14\bigl(N_{\tau,H}-A_{\tau,H}\bigr).}         \tag{3.2}
\]

At a global minimizer of the same (H)-window objective,
\(e_\tau(I)\ge0\) for every (I).  Hence

\[
 N_{\tau,H}\ge A_{\tau,H}.                          \tag{3.3}
\]

Equality has a much stronger meaning than equality of two scalar norms.
If (N_{\tau,H}=A_{\tau,H}), then the nonnegative function
\(e_\tau(I)\) has mean zero, and is therefore identically zero.  Expanding
one- and two-component switches gives

\[
 \boxed{
 2\langle f,d_C\rangle_H+\|d_C\|_H^2=0
 \quad(C\in\mathcal C),}                            \tag{3.4}
\]

and

\[
 \boxed{
 \langle d_C,d_D\rangle_H=0
 \quad(C\ne D).}                                    \tag{3.5}
\]

Conversely, (3.4)--(3.5) make the energy constant on the entire switching
cube and imply (N_{\tau,H}=A_{\tau,H}).

Two elementary no-mixing cases are worth recording.

* If the transposition overlay is connected, it has only the two children
  (F) and \(\tau F\), so (N_{\tau,H}=A_{\tau,H}) automatically and
  the move offers no descent at all.
* More generally, if every nonfixed target orbit is active in at most one
  component, the component differences have disjoint supports, so
  (N_{\tau,H}=A_{\tau,H}) algebraically, without any local-minimality
  assumption. At the first shadow this includes the unresolved one-sided
  width-one target orbits; no broader NAE-clause identification is used.

Thus fragmentation alone is not a mixing theorem.

## 4. Exact global slack decomposition

Sum over transpositions:

\[
 R_H=\sum_\tau N_{\tau,H},
 \qquad
 D_H=\sum_\tau A_{\tau,H}.
\]

Decompose each (f_q) into Johnson harmonics.  Since degrees zero and one
vanish,

\[
\begin{aligned}
 D_H
 &=\sum_{q\le H}\frac1{c_q}
   \sum_{j\ge2}2j(n-j+1)\|f_q^{(j)}\|_2^2,\\
 D_H-4(n-1)S_H
 &=2\sum_{q\le H}\frac1{c_q}
   \sum_{j\ge3}(j-2)(n-j-1)\|f_q^{(j)}\|_2^2.
                                                               \tag{4.1}
\end{aligned}
\]

At a global minimizer, (3.3) and (4.1) give three nonnegative slacks and
the exact identity

\[
\boxed{
\begin{aligned}
 R_H-4(n-1)B_H
 ={}&(R_H-D_H)\\
 &+\bigl(D_H-4(n-1)S_H\bigr)\\
 &+4(n-1)\Phi_H.
\end{aligned}}                                      \tag{4.2}
\]

The first term is exactly

\[
 R_H-D_H=4\sum_\tau\mathbb E_I e_\tau(I).          \tag{4.3}
\]

This has two consequences.

1. The proposed estimate

   \[
   R_H\le4(n-1)B_H+o(nW)                            \tag{4.4}
   \]

   certainly implies \(\Phi_H=o(W)\), but it also requires

   \[
   R_H-D_H=o(nW),
   \qquad
   D_H-4(n-1)S_H=o(nW).                              \tag{4.5}
   \]

   It is therefore analytically stronger than the desired low-energy
   conclusion; it is not an easier reformulation of that conclusion.

2. The component-switching and zero-margin facts alone cannot prove
   (4.4).  For a connected overlay at one fixed transposition, that
   transposition's contribution to the first slack is identically zero,
   while the last slack is exactly (4(n-1)\Phi_H).  In that case the
   claimed upper bound already contains the target assertion itself.
   Any proof of (4.4) must add a genuine theorem about the factor fibre,
   rather than only reusing global minimality and the Johnson gap.

The exact baseline equation \(R_H=4(n-1)B_H\) at a global minimizer is
rigid. It forces, at every
controlled depth,

* a floor-balanced load vector, \(\Phi_q=0\);
* a centered load lying entirely in Johnson degree two;
* constant energy on every transposition component cube, equivalently
  (3.4)--(3.5) for every transposition.

There is a further integral consequence which is stronger than Hilbert
orthogonality.  At exact baseline equality, \(F\) is balanced and every
child in every switching cube has the same zero floor excess.  Fix a target
\(S\).  The affine scalar function

\[
 \mu(S)+\sum_{C\in I}d_C(S)
\]

therefore takes values only in \(\{c,c+1\}\) for every subset \(I\).  If
\(\mu(S)=c\), each nonzero \(d_C(S)\) must be \(+1\), and there can be at
most one of them.  If \(\mu(S)=c+1\), each nonzero \(d_C(S)\) must be
\(-1\), again with at most one.  Hence

\[
 \boxed{\#\{C:d_{q,C}(S)\ne0\}\le1}                 \tag{4.6}
\]

at every rank and target. Thus exact attainment forces the component
wall-crossing supports to be disjoint targetwise for each fixed
transposition, not merely orthogonal after summation. No disjointness across
different transpositions is asserted.

## 5. Arithmetic rigidity of spectral equality

Suppose the load at one rank is balanced.  Write

\[
 \mu=c+{\bf1}_{\mathcal B},
 \qquad
 \theta=|\mathcal B|/N.
\]

Then \(f={\bf1}_{\mathcal B}-\theta{\bf1}\). If equality holds in the Johnson
gap, (f\in E_2), so with (L_J) the Johnson Laplacian,

\[
 L_Jf=2(n-1)f.                                      \tag{5.1}
\]

Let (d=r(n-r)) be the Johnson degree.  Equation (5.1) says precisely
that \(\mathcal B\) is an equitable two-colouring:

\[
\boxed{
\begin{aligned}
 S\notin\mathcal B&:\quad
   |N_J(S)\cap\mathcal B|=2(n-1)\theta,\\
 S\in\mathcal B&:\quad
   |N_J(S)\setminus\mathcal B|=2(n-1)(1-\theta).
\end{aligned}}                                      \tag{5.2}
\]

In particular (2(n-1)\theta\) must be an integer.  This is an additional
arithmetic obstruction to exact attainment of the spectral floor.

At the first shadow, \(r=m-1\) and \(\theta=2/m\).  Hence exact floor
attainment would require every nonbonus target to have exactly (8)
bonus Johnson neighbours, and every bonus target to have exactly
(4m-8) nonbonus neighbours.  These conditions are necessary, not known
to be sufficient for a wreath factor.

## 6. A row-level connectivity expansion

There is an exact expansion which shows how much cancellation a small
component-noise bound must create.  Let (h_{P,r}) be the indicator of the
(n) cyclic (r)-intervals of one row (P), and put

\[
 g_{P,\tau,r}=\tau h_{P,r}-h_{P,r}.
\]

For (2\le r\le m), if the two transposed coordinates have shorter cyclic
distance \(\ell\in\{1,\ldots,m\}\) in (P), then

\[
 \boxed{
 \|g_{P,\tau,r}\|_2^2
 =4\min(r,\ell)-4{\bf1}_{\{\ell=r\}}.}              \tag{6.1}
\]

Indeed, (2\min(r,\ell)) cyclic (r)-windows contain exactly one of the
two coordinates.  Apart from fixed windows, two exchanged windows remain
cyclic windows exactly when \(\ell=r\).  Since an odd cycle has exactly
(n) unordered coordinate pairs at each shorter distance,

\[
 \boxed{
 \sum_\tau\|g_{P,\tau,r}\|_2^2
 =2n\bigl(r(n-r)-2\bigr).}                          \tag{6.2}
\]

For (r=1), the cyclic interval family is the complete singleton layer and
the sum is zero.

As the component left sides partition the rows of (F), (1.2) yields

\[
R_q:=\sum_\tau\sum_{C\in\mathcal C_\tau(F)}\|d_{\tau,q,C}\|_2^2,
\qquad
D_q:=\sum_\tau\|\tau\mu_q-\mu_q\|_2^2.
\]

\[
\boxed{
\begin{aligned}
 R_q
 ={}&2W\bigl(r_q(n-r_q)-2\bigr)\\
 &+2\sum_\tau\sum_{C\in\mathcal C_\tau(F)}
   \sum_{P<P'\in L_C}
   \langle g_{P,\tau,r_q},g_{P',\tau,r_q}\rangle,
\end{aligned}}                                      \tag{6.3}
\]

for (r_q\ge2).  The corresponding formula for (D_q) has the same
diagonal term but sums the row-pair inner product over all pairs of rows,
not only pairs in the same overlap component.  Therefore

\[
\boxed{
 R_q-D_q
 =-2\sum_\tau
   \sum_{\substack{P<P'\\P,P'\text{ in different }\tau\text{-components}}}
   \langle g_{P,\tau,r_q},g_{P',\tau,r_q}\rangle.}  \tag{6.4}
\]

For central ranks the diagonal term in (6.3) is of order (Wm^2) per
rank, whereas the spectrally forced floor is only of order at most (Wm)
per generic rank (and only order (W) at the first shadow).  Thus a proof
of (4.4) must establish almost complete cancellation of the row
self-energies *inside the actual overlap components*.  A bound on component
sizes, by itself, does not provide that cancellation.

For \(m\ge3\), at the first shadow these two quantities are explicit:

\[
 2W\bigl((m-1)(m+2)-2\bigr)
   =2W(m^2+m-4)                                      \tag{6.5}
\]

is the row-diagonal term, while

\[
 4(n-1)V_1^{\min}
 =16W\,\frac{m-2}{m+2}.                              \tag{6.6}
\]

So exact floor-scale component noise requires cancellation of all but an
\(O(m^{-2})\) fraction of the first-shadow row-diagonal mass.

## 7. Conclusion

The exact upper gate

\[
 R_H\le4(n-1)B_H+o(nW)
\]

is a valid sufficient condition, but the slack identity (4.2) shows that it
packages three different assertions: near floor balance, near degree-two
spectrality, and near-zero fair component drift.  Overlap connectivity and
zero point margins give the exact formulas above, but do not control any of
those slacks from above.  The missing input must be a factor-fibre theorem
forcing the internal cancellations in (6.3), or a different move system
which bypasses connected and width-one locked overlays.
