# The common-phase \(Q_4\) braid bank: exact physical Walsh--Gram and its common-mode reach

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

The generator in
MATH_THEOREM_Q4_COMMON_PHASE_BLOCK_TRANSPOSITION_20260726.md is genuine:
it changes the packet-order word, preserves exact ownership, preserves one
global phase colouring, and preserves isometric \(C_{2h}\)-cycles. It
therefore removes the former phase-semiconjugacy obstruction.

One replicated braid bank does **not** kill an order-\(W\) common-mode
outer Hall defect in the mesoscopic regime \(q=o(h)\).

The reason is exact. One braid component contains two \(C_{2h}\)'s and
\(4h\) owners, but its two shores differ on only eight outgoing edges.
Consequently at depth \(q\):

\[
 \#\{\hbox{starts whose literal target can change}\}\le 8q          \tag{0.1}
\]

per component. The syndrome factor has \(2^h/(4h)\) independent
components, so switching an arbitrary subset changes at most

\[
 \frac{2q}{h}\,2^h                                                \tag{0.2}
\]

depth-\(q\) occurrences in one \(Q_h\)-cell. Over a global owner factor
of mass \(W-o(W)\), the bound is

\[
 R_q\le \frac{2q}{h}W+o(W).                                       \tag{0.3}
\]

Thus, for \(q/h\to0\), every state of this entire Boolean braid bank is
an \(o(W)\)-occurrence perturbation of the unswitched state. Its physical
target load changes in \(L^1\) by at most \(2R_q=o(W)\), and its number
of covered targets changes by at most \(R_q=o(W)\). Any bounded outer
Hall witness of value \(\delta W\) survives with value
\(\delta W-o(W)\).

The exact incidence Walsh expansion is degree one:

\[
 A_q^\varepsilon=\overline A_q+\sum_{\kappa}
                       \varepsilon_\kappa D_{\kappa,q},\qquad
 \mu_q^\varepsilon=\overline\mu_q+\sum_\kappa
                       \varepsilon_\kappa d_{\kappa,q},            \tag{0.4}
\]

where \(\kappa\) ranges over the \(2^h/(4h)\) braid components. The exact
physical Gram is the quadratic Ising form displayed in (3.4). Uniform
braid bits add the nonnegative diagonal energy
\(\sum_\kappa\|d_{\kappa,q}\|_2^2\); they do not average away the common
mode.

Accordingly, the new theorem supplies the previously missing
**generator**, but not the required density. At Gaussian depth, a
successful braid architecture needs at least

\[
 \Omega(h/q)                                                       \tag{0.5}
\]

phase-distributed braid layers per owner, or another construction whose
changed-edge density is \(\Omega(1/q)\). Packing such overlapping layers
while retaining one exact factor is precisely the remaining braid-network
problem.

## 1. One component changes eight directed edges

Fix one syndrome pair of cycles \(C+k,C+k+v\). On shore zero their common
direction word is

\[
 1,2,3,4,5,\ldots,h,\ 1,2,3,4,5,\ldots,h.                         \tag{1.1}
\]

On shore one it is

\[
 1,4,3,2,5,\ldots,h,\ 1,4,3,2,5,\ldots,h.                         \tag{1.2}
\]

The common phase colouring identifies the owner sets phase by phase. At
phases

\[
 1,\ 3,\ h+1,\ h+3                                                \tag{1.3}
\]

the two vertices, one in each old cycle, acquire a different successor.
At every other phase the outgoing successor is unchanged. Hence the
directed edge-difference set \(E_\kappa\) satisfies

\[
 |E_\kappa|=4\cdot2=8.                                            \tag{1.4}
\]

This number is independent of \(h\). The suspension inserts extra
directions without inserting further shore disagreements.

Let \(F_\kappa^0,F_\kappa^1\) be the two successor maps on the common
\(4h\)-owner component. If their depth-\(q\) vertex sequences from a start
\(x\) differ, follow both paths until their first disagreement. Before
that point they coincide, and the common path uses an edge of
\(E_\kappa\). Every changed directed edge has at most one predecessor
start at each of the \(q\) possible positions in a window. Therefore

\[
 S_{\kappa,q}:=
 \{x:\Phi_{\kappa,q}^0(x)\ne\Phi_{\kappa,q}^1(x)\}
 \quad\hbox{satisfies}\quad
 |S_{\kappa,q}|\le8q.                                             \tag{1.5}
\]

The argument applies separately to lower intersections and upper unions.
It does not assume that a changed path necessarily has a changed target;
(1.5) is an upper bound and is therefore valid for both signs.

For \(2\le q\le h-2\), the four changed phases form two antipodal pairs
at cyclic separation two. Counting the unions of predecessor intervals
improves (1.5) to \(4q+8\). The simpler \(8q\) bound is uniform for all
\(q\ge1\) and is sufficient below.

## 2. Owner-resolved incidence operator

Let \(\Omega_\kappa\) be the \(4h\)-owner support of component \(\kappa\),
and let \(\mathcal T_q^\pm\) be the literal signed target space. Define

\[
 A_{\kappa,q}^{b,\pm}(T,x)
 =
 {\bf1}\{\Phi_{\kappa,q}^{b,\pm}(x)=T\},
 \qquad b\in\{0,1\}.                                               \tag{2.1}
\]

Every column contains exactly one \(1\). Put

\[
\begin{aligned}
 \overline A_{\kappa,q}^{\pm}
   &=\frac12(A_{\kappa,q}^{0,\pm}
                   +A_{\kappa,q}^{1,\pm}),\\
 D_{\kappa,q}^{\pm}
   &=\frac12(A_{\kappa,q}^{0,\pm}
                   -A_{\kappa,q}^{1,\pm}),\\
 \overline z_{\kappa,q}^{\pm}
   &=\overline A_{\kappa,q}^{\pm}{\bf1},\\
 d_{\kappa,q}^{\pm}
   &=D_{\kappa,q}^{\pm}{\bf1}.
\end{aligned}                                                     \tag{2.2}
\]

If \(\varepsilon_\kappa=+1\) selects shore zero and
\(\varepsilon_\kappa=-1\) shore one, then

\[
 A_{\kappa,q}^{\varepsilon_\kappa,\pm}
 =\overline A_{\kappa,q}^{\pm}
       +\varepsilon_\kappa D_{\kappa,q}^{\pm}.                     \tag{2.3}
\]

The owner supports \(\Omega_\kappa\) are disjoint. Concatenating their
column operators gives the complete cell factor

\[
 \boxed{
 A_q^{\varepsilon,\pm}
 =\bigl[
   \overline A_{\kappa,q}^{\pm}
       +\varepsilon_\kappa D_{\kappa,q}^{\pm}
   \bigr]_{\kappa}.}                                              \tag{2.4}
\]

The load vector is consequently

\[
 \boxed{
 \mu_q^{\varepsilon,\pm}
 =\overline\mu_q^\pm+
   \sum_\kappa\varepsilon_\kappa d_{\kappa,q}^\pm,\qquad
 \overline\mu_q^\pm=\sum_\kappa\overline z_{\kappa,q}^\pm.}       \tag{2.5}
\]

Thus the incidence map has only the constant Walsh coefficient and the
singleton coefficients \(d_{\kappa,q}^\pm\). There are no higher Walsh
coefficients. Higher degrees appear only after the quadratic Gram
functional is formed.

By (1.5), a nonzero column of \(D_{\kappa,q}^{\pm}\) is half the
difference of two standard target basis vectors. Hence

\[
\begin{aligned}
 \|D_{\kappa,q}^{\pm}\|_{\rm HS}^2
 &\le\frac12|S_{\kappa,q}|\le4q,\\
 \|d_{\kappa,q}^{\pm}\|_1
 &\le |S_{\kappa,q}|\le8q,\\
 \langle d_{\kappa,q}^{\pm},{\bf1}\rangle&=0.
\end{aligned}                                                     \tag{2.6}
\]

These are literal physical bounds, not direction-support estimates.

## 3. Exact braid-bit physical Gram

For two components \(\kappa,\lambda\), the owner-resolved physical Gram
block is

\[
 \mathcal K_{\kappa,\lambda,q}^{\varepsilon,\pm}
 =
 \left(
   \overline A_{\kappa,q}^{\pm}
       +\varepsilon_\kappa D_{\kappa,q}^{\pm}
 \right)^*
 \left(
   \overline A_{\lambda,q}^{\pm}
       +\varepsilon_\lambda D_{\lambda,q}^{\pm}
 \right).                                                         \tag{3.1}
\]

Expanding,

\[
\boxed{
\begin{aligned}
 \mathcal K_{\kappa,\lambda,q}^{\varepsilon,\pm}
 ={}&
 (\overline A_{\kappa,q}^{\pm})^*
       \overline A_{\lambda,q}^{\pm}\\
 &+\varepsilon_\kappa
       (D_{\kappa,q}^{\pm})^*\overline A_{\lambda,q}^{\pm}
 +\varepsilon_\lambda
       (\overline A_{\kappa,q}^{\pm})^*D_{\lambda,q}^{\pm}\\
 &+\varepsilon_\kappa\varepsilon_\lambda
       (D_{\kappa,q}^{\pm})^*D_{\lambda,q}^{\pm}.
                                                                    \tag{3.2}
\end{aligned}}
\]

This equality retains the literal target-equality kernel. In particular,
it includes collisions between different syndrome components rather than
assuming their shadows are disjoint.

For simultaneous depths and both signs, put all load vectors in the
weighted direct-sum Hilbert space

\[
 \mathcal H=\bigoplus_{q\le H}\bigoplus_\pm
       \sqrt{w_q}\,\mathbb R^{\mathcal T_q^\pm}.                   \tag{3.3}
\]

Let \(r\in\mathcal H\) be the centered common load
\(\overline\mu-\lambda{\bf1}\), with the appropriate rankwise means.
Write \(d_\kappa\) for the direct sum of the
\(d_{\kappa,q}^{\pm}\). Then the exact centered Gram potential is

\[
\boxed{
 \Phi(\varepsilon)
 =\left\|r+\sum_\kappa\varepsilon_\kappa d_\kappa\right\|^2
 =\|r\|^2
  +2\sum_\kappa\varepsilon_\kappa\langle r,d_\kappa\rangle
  +\sum_{\kappa,\lambda}
      \varepsilon_\kappa\varepsilon_\lambda
      \langle d_\kappa,d_\lambda\rangle.}                         \tag{3.4}
\]

Thus the physical Walsh--Gram data are the field

\[
 g_\kappa=\langle r,d_\kappa\rangle                              \tag{3.5}
\]

and the positive-semidefinite Gram matrix

\[
 G_{\kappa,\lambda}=\langle d_\kappa,d_\lambda\rangle.            \tag{3.6}
\]

The diagonal part of the last sum is independent of the signs. Uniform
independent braid bits satisfy the exact identity

\[
 \mathbb E_\varepsilon\Phi(\varepsilon)
 =\|r\|^2+\sum_\kappa\|d_\kappa\|^2.                              \tag{3.7}
\]

They add variance; they do not cancel the common mode. A deterministic
choice can improve (3.7) only through the linear fields (3.5) and the
off-diagonal entries of (3.6).

## 4. Physical packet tags remain present

Inside the hashed \(B_4\) atlas, a braid component has the complete tag

\[
 \omega=(u,I,c;\ \theta;\ \kappa),                               \tag{4.1}
\]

where \(u\) is the frozen anchor subset, \(I,c\) are the first-eligible
packet indices and frozen context, \(\theta\) is its ternary seed vector,
and \(\kappa\) is the syndrome-cycle pair.

The braid changes only successor pairings inside \(\Omega_\kappa\). It
does not change \(u,I,c,\theta\), the owner support, or the phase class.
In particular, every target retains

\[
 T\cap A=u.                                                       \tag{4.2}
\]

Therefore the global physical Gram remains block diagonal in the anchor
tag:

\[
 \mathcal K_q^\pm
 =\bigoplus_{u\subseteq A}\mathcal K_{u,q}^\pm.                    \tag{4.3}
\]

Within one anchor block, (3.2) must still be evaluated with the actual
first-eligible indices, frozen contexts, ternary frames, syndrome labels,
phases, and literal port traces. The common phase colouring makes this
evaluation well-defined; it does not erase any of these tags.

Consequently the braid bank cannot couple two orthogonal anchor sectors
or change the ternary common mode between them. Its only possible action
is the sparse within-sector perturbation quantified next.

## 5. Total physical reach of one bank

There are

\[
 N_{\rm br}=\frac{2^h}{4h}                                       \tag{5.1}
\]

components in one \(Q_h\)-cell. Summing (1.5),

\[
 R_q^{\rm cell}
 :=\sum_\kappa|S_{\kappa,q}|
 \le8q\,N_{\rm br}
 =\frac{2q}{h}\,2^h.                                             \tag{5.2}
\]

For any two braid states \(\varepsilon,\eta\), couple their target maps
start by start. Only starts belonging to a component on which the bits
differ can change, so

\[
\begin{aligned}
 \|\mu_q^{\varepsilon,\pm}-\mu_q^{\eta,\pm}\|_1
 &\le2R_q^{\rm cell}
 \le\frac{4q}{h}\,2^h,\\
 \left|M_q^{\varepsilon,\pm}-M_q^{\eta,\pm}\right|
 &\le R_q^{\rm cell}
 \le\frac{2q}{h}\,2^h.
\end{aligned}                                                     \tag{5.3}
\]

The second inequality follows by replacing differing target occurrences
one at a time: one replacement changes the cardinality of the covered
target set by at most one.

If braid banks are installed in owner-disjoint cube cells covering
\(G=W-o(W)\) global starts, the same coupling gives

\[
\boxed{
\begin{aligned}
 \|\mu_q^{\varepsilon,\pm}-\mu_q^{\eta,\pm}\|_1
 &\le\frac{4q}{h}G,\\
 |M_q^{\varepsilon,\pm}-M_q^{\eta,\pm}|
 &\le\frac{2q}{h}G.
\end{aligned}}                                                     \tag{5.4}
\]

For every fixed Gaussian depth \(q=x\sqrt m+O(1)\), the mesoscopic choice
\(h/\sqrt m\to\infty\) makes both quantities \(o(W)\).

The algebraic braid span is small for the same reason. From (2.6),

\[
 \sum_\kappa\|D_{\kappa,q}^{\pm}\|_{\rm HS}^2
 \le4qN_{\rm br}
 =\frac qh\,2^h.                                                  \tag{5.5}
\]

Moreover every load difference \(d_{\kappa,q}^\pm\) is supported on the
old and new targets of the starts in \(S_{\kappa,q}\). Hence the union of
all target coordinates on which the braid span is nonzero has size at
most

\[
 2R_q^{\rm cell}\le\frac{4q}{h}\,2^h.                             \tag{5.6}
\]

Thus both the Boolean reachable zonotope and its real linear span vanish
on all but an \(O(q/h)\) fraction of the occurrence-scale target
coordinates.

## 6. Projection on an outer Hall witness

Let \(w_q^\pm\) be any physical outer Hall dual with

\[
 \|w_q^\pm\|_\infty\le1.                                         \tag{6.1}
\]

This normalization includes ordinary missing-target witnesses and every
unit-capacity target cut. By (5.4),

\[
 \left|
 \left\langle w_q^\pm,
 \mu_q^{\varepsilon,\pm}-\mu_q^{\eta,\pm}
 \right\rangle
 \right|
 \le\frac{4q}{h}G.                                                \tag{6.2}
\]

Suppose the unswitched or common-mode factor has an extensive dual defect

\[
 \left\langle w_q^\pm,
 b_q^\pm-\mu_q^{0,\pm}\right\rangle
 \ge\delta W-o(W)                                                 \tag{6.3}
\]

for some fixed \(\delta>0\), where \(b_q^\pm\) is the target demand or
capacity vector. Then every braid state satisfies

\[
 \left\langle w_q^\pm,
 b_q^\pm-\mu_q^{\varepsilon,\pm}\right\rangle
 \ge
 \left(\delta-\frac{4q}{h}\right)W-o(W).                          \tag{6.4}
\]

When \(q/h\to0\), the right side is \(\delta W-o(W)\). Hence the common
Hall mode is outside the effective reach of one braid bank.

The same conclusion has a support form. If the common factor misses
\(\delta W\) literal targets, the braid span is supported on only
\(O(qW/h)=o(W)\) old/new target coordinates. All but \(o(W)\) of those
holes lie outside the support of every braid difference and are fixed by
every choice of bits.

This conclusion does not require the Hall witness to arise from one fixed
coordinate pairing. It applies to the surviving outer packet Hall defect
after the ternary frame diffusion, provided that defect has a bounded
dual margin of order \(W\).

## 7. Required braid density

Suppose \(L\) factor-compatible braid banks are composed, and pessimistically
allow their affected starts to be disjoint. Repeating (5.2) gives

\[
 R_q^{(L)}\le\frac{2Lq}{h}W.                                      \tag{7.1}
\]

Changing an order-\(W\) Hall defect requires \(R_q^{(L)}=\Omega(W)\).
Therefore necessarily

\[
 \boxed{L=\Omega(h/q).}                                           \tag{7.2}
\]

For \(q=\Theta(\sqrt m)\) and \(h=m^{3/4+o(1)}\), this means

\[
 L=\Omega(m^{1/4-o(1)}).                                         \tag{7.3}
\]

The independent components in Theorem 5.1 all belong to one bank and do
not count as \(L=2^h/(4h)\) layers: together they still change only eight
edges per \(4h\) owners. Relabelling the four active directions produces
other banks, but overlapping banks cannot be chosen independently unless
their interaction components are recomputed. The generator theorem does
not yet provide such a braid-network factorization.

## 8. Exact conclusion

The new \(Q_4\) theorem changes the structural answer but not yet the
coefficient-one answer.

* **Closed:** block order is not a semiconjugacy invariant of exact
  common-phase isometric factors.
* **Closed:** there are exponentially many independent literal factor
  states inside one syndrome cell.
* **Exact operator:** their incidence Walsh expansion is (2.4)--(2.5),
  and their physical Gram is (3.2)--(3.6).
* **Still open:** a dense, overlapping braid network whose changed-edge
  density reaches \(\Omega(1/q)\) while preserving exact ownership and
  the B4 physical tags.
* **Negative for one bank:** at every \(q=o(h)\), its entire Boolean state
  cube changes only \(o(W)\) occurrences and cannot remove an
  order-\(W\) common-mode outer Hall defect.

Thus the braid bits do not yet kill the surviving common mode. They
identify the minimal generator from which a sufficiently dense solution
would have to be assembled.
