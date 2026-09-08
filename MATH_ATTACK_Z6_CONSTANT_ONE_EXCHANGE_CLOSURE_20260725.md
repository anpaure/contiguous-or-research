# Lane Z master redirect: macroscopic exchange obstruction and exact Graver completion

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver,
certificate, random experiment, or fractional endpoint is used.

## 0. Verdict

Let

\[
n=2m+1,\qquad
W=\binom nm,\qquad
B=\frac Wn=\operatorname{Cat}_m,
\qquad
H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\) and sufficiently large \(m\).

The floor-corrected energy is not \(M\)-convex, \(M^\natural\)-convex,
\(L\)-convex, \(L^\natural\)-convex, or jump-system convex on the genuine
positive exact-factor fibre.  This failure is not merely caused by the
absence of one-wreath exchanges.  There are two exact factors
\(F_m,G_m\) for which the coordinate interval

\[
\{Z:F_m\cap G_m\subseteq Z\subseteq F_m\cup G_m\}
\]

contains only its two endpoints, while

\[
|F_m\setminus G_m|
=|G_m\setminus F_m|
=s_m
=\operatorname{Cat}_{m-2}+\operatorname{Cat}_{m-1}
=\left(\frac5{16}+o(1)\right)B.
\tag{0.1}
\]

Thus every comparator-conformal exchange system which decomposes every
exact-factor difference must contain macroscopic moves.  No
\(O(1)\)-, polynomial-in-\(m\)-, or \(o(B)\)-wreath support bound is
possible.  The endpoint difference in (0.1) is itself a Graver primitive
of the exact middle matrix and of every fixed-window load lift.

There is nevertheless a complete stronger move theorem.

1. For the quadratic half floor energy, every nonglobal factor has an
   improving **Gram-antagonistic ownership packet**.  If a comparator is
   better by \(D\), one such legal packet gains at least

   \[
   \frac{D}{\lfloor |F\setminus G|/2\rfloor}
   \ge \frac{D}{\lfloor B/2\rfloor}
   \ge\frac{2D}{B}.
   \tag{0.2}
   \]

2. For every separable discrete-convex load potential, including the
   overload-equivalent free-quota corridor, the applicable augmented
   Graver moves are an exact test set and satisfy the same improved
   comparison factor (0.2).

3. Against one fixed global comparator, there exists a comparator-monotone
   strict exact descent reaching a global minimizer after at most
   \(\lfloor B/2\rfloor\) packet moves.

These are integral positive-factor moves throughout.  But they also give a
sharp logical ceiling for the lane.  Under the complete Graver neighborhood,
"local minimum" means exactly "global minimum."  Therefore the assertion
that every such local factor has \(o(W)\) overload-equivalent corridor is
not a new local lemma: it is exactly the fixed-window MWB optimum statement.
Establishing those optimum statements for every fixed \(A>0\), with the
exact factors allowed to depend on \(A\), diagonalizes to MWB and then to
the already audited literal contiguous-OR word of length \(W+o(W)\).

Accordingly, the pure discrete-exchange lane is closed as follows:

- standard and all sublinear conformal exchange convexities are false;
- a complete exact replacement is the macroscopic augmented-Graver /
  Gram-antagonistic packet neighborhood;
- that replacement removes false local minima with the quantitative
  constant \(2/B\), but an absolute \(o(W)\) bound on its global optimum is
  precisely the unresolved positive-factor theorem, not a consequence of
  exchange convexity.

No floor-energy bad local minimum is asserted.  The obstruction is to the
exchange architecture; it does not refute MWB or the constant-one
contiguous-OR conjecture.

## 1. Exact fibre, two floor potentials, and the literal implication

Let \(\mathscr W_m\) be the set of unoriented cyclic orders on \([n]\),
modulo rotation and reversal.  Let \(A_m\) be the middle-incidence matrix:
the column \(a_C\) of \(C\in\mathscr W_m\) records its \(n\) cyclic
intervals of length \(m\).  The positive exact-factor fibre is

\[
\mathcal X_m
=
\{x\in\{0,1\}^{\mathscr W_m}:A_mx=\mathbf1\}.
\tag{1.1}
\]

Every exact factor contains exactly \(B\) wreaths, because summing the
middle equations gives

\[
n\sum_Cx_C=W.
\tag{1.2}
\]

For \(1\le q\le H\), put

\[
r_q=m-q,\qquad
N_q=\binom n{r_q},\qquad
W=c_qN_q+\rho_q,
\quad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\quad
0\le\rho_q<N_q.
\tag{1.3}
\]

Let \(B_qx=\mu_q^x\) be the rank-\(r_q\) cyclic-interval load, and let
\(B_H\) be the vertical stack of the \(B_q\).  Every block has total

\[
\sum_S\mu_q^x(S)=W.
\tag{1.4}
\]

Define the deficit, high surplus, and mobile balanced overload by

\[
\begin{aligned}
D_q^-(x)&=\sum_S(c_q-\mu_q^x(S))_+,\\
D_q^+(x)&=\sum_S(\mu_q^x(S)-c_q-1)_+,\\
O_q(x)&=\max\{D_q^-(x),D_q^+(x)\}.
\end{aligned}
\tag{1.5}
\]

The quadratic half floor energy is

\[
\boxed{
\Psi_H(x)
=
\frac12\sum_{q\le H}\frac1{c_q}
\sum_S
(\mu_q^x(S)-c_q)(\mu_q^x(S)-c_q-1).
}
\tag{1.6}
\]

Its scalar summands are nonnegative on integers and have discrete second
difference \(1/c_q\).  The overload-equivalent corridor is

\[
\boxed{
\mathcal C_H(x)
=
\sum_{q\le H}\frac1{c_q}
\sum_S
\left[(c_q-\mu_q^x(S))_+
+(\mu_q^x(S)-c_q-1)_+\right].
}
\tag{1.7}
\]

Both are separable discrete-convex functions of the integral load vector.
At one depth, the corridor is \(D_q^-+D_q^+\), so

\[
\boxed{
\frac{O_q(x)}{c_q}
\le
\frac{D_q^-(x)+D_q^+(x)}{c_q}
\le
\frac{2O_q(x)}{c_q}.
}
\tag{1.8}
\]

Also the quadratic numerator is at least
\(2\max\{D_q^-,D_q^+\}\), whence

\[
\sum_{q\le H}\frac{O_q(x)}{c_q}
\le\Psi_H(x).
\tag{1.9}
\]

The corridor, unlike the quadratic potential, is factorwise equivalent to
mobile overload in both directions.

### Literal composition

If \(M_q(x)\) is the number of missing rank-\(r_q\) masks, then every
missing mask contributes \(c_q\) to \(D_q^-\).  Hence

\[
M_q(x)\le\frac{D_q^-(x)}{c_q}\le\frac{O_q(x)}{c_q}.
\tag{1.10}
\]

Consequently, if for every fixed \(A>0\) there are exact factors with

\[
\mathcal C_{\lceil A\sqrt m\rceil}(x)=o(W),
\tag{1.11}
\]

then (1.8) gives fixed-window overload.  A slow diagonal
\(A=A(m)\to\infty\) gives MWB, and (1.10) supplies the missing-mask
hypothesis in the audited exact wreath transfer inequality.  Its output is
one literal nonzero contiguous-OR word of length \(W+o(W)\).  The usual
one-bit trimmed lift covers even dimensions.

Conversely, fixed-window overload gives (1.11) by the upper inequality in
(1.8).  Thus, for the corridor,

\[
\boxed{
\min_{x\in\mathcal X_m}\mathcal C_{\lceil A\sqrt m\rceil}(x)=o(W)
\quad\text{for every fixed }A
\iff
\mathrm{MWB}.
}
\tag{1.12}
\]

The implication from the right side of (1.12) to a literal constant-one
word uses only the already proved transfer theorem.  No exchange trajectory
or fractional average is used as a word.

## 2. Standard discrete convexity fails on the genuine domain

### Lemma Z6.1 -- middle columns determine the unoriented wreath

For \(m\ge2\), distinct elements of \(\mathscr W_m\) have distinct columns
in \(A_m\).

#### Proof

For two labels \(u,v\), let
\(d_C(u,v)\in\{1,\ldots,m\}\) be their shorter cyclic distance in \(C\).
The number of owned middle intervals containing both is

\[
\#\{I\in a_C:u,v\in I\}=m-d_C(u,v).
\tag{2.1}
\]

Thus the column determines every cyclic distance.  In particular it
determines the distance-one pairs, which are exactly the edges of the
unoriented cycle.  Hence it determines \(C\) modulo reversal.  \(\square\)

### Theorem Z6.2 -- objective-independent native exchange obstruction

For every \(m\ge2\), the effective domain \(\mathcal X_m\) is neither an
\(M\)-domain, an \(M^\natural\)-domain, an \(L\)- or
\(L^\natural\)-domain, nor a jump system.  Consequently \(\Psi_H\) and
\(\mathcal C_H\), extended by \(+\infty\) off \(\mathcal X_m\), belong to
none of those discrete-convex classes.

#### Proof

For distinct wreaths \(C,D\), a unit exchange would give

\[
A_m(x-e_C+e_D)=\mathbf1-a_C+a_D.
\]

It is feasible only if \(a_C=a_D\), which Lemma Z6.1 forbids.  The fibre is
nonsingleton: exact factors exist, and a nonempty proper subset of the
transitive wreath set cannot be invariant under all coordinate
permutations.  Therefore the \(M\)-exchange axiom fails.

Every factor has the fixed cardinality \(B\).  The unpaired
\(M^\natural\) alternative changes this cardinality, while the paired
alternative is the impossible unit exchange above.

For distinct binary factor vectors \(x,y\), with
\(d=|\operatorname{supp}x\setminus\operatorname{supp}y|>0\),

\[
\left\lfloor\frac{x+y}{2}\right\rfloor=x\wedge y,
\qquad
\left\lceil\frac{x+y}{2}\right\rceil=x\vee y
\]

have cardinalities \(B-d\) and \(B+d\).  They are not exact factors, so
\(L^\natural\) midpoint closure and meet/join closure fail.  A finite
nonempty fixed-cardinality domain also lacks the all-ones translation
closure required for standard \(L\)-convexity.

Finally choose \(i\in\operatorname{supp}x\setminus\operatorname{supp}y\).
The unit step \(-e_i\) toward \(y\) leaves the fibre.  The two-step jump
axiom would require a second unit step toward \(y\).  Fixed cardinality
forces it to be \(+e_j\) for some
\(j\in\operatorname{supp}y\setminus\operatorname{supp}x\), again the
impossible one-wreath exchange.  Thus the jump axiom fails.  \(\square\)

The same obstruction appears after projecting to any nonsingleton rank-load
image.  Every rank-\(r\) exact load satisfies the fixed point margins

\[
\sum_{S\ni i}\mu(S)=rB\qquad(i\in[n]).
\tag{2.2}
\]

A unit load exchange \(\mu-e_S+e_T\) preserves (2.2) only when
\(\mathbf1_S=\mathbf1_T\), hence \(S=T\).  Thus merely changing from wreath
coordinates to joint load coordinates does not restore \(M\)- or jump
exchange.

## 3. A macroscopic primitive and a bounded-neighborhood local trap

We now strengthen Theorem Z6.2 from one-wreath failure to a linear-size
hole in the genuine exact fibre.

Use the proved MSW exact factor \(F_m\) and the coordinate transposition
\(\tau=(2\ 3)\).  The exact MSW component hierarchy states that the
ownership overlay of \(F_m\) and \(\tau F_m\) has, for
\(0\le j\le m-2\), components with side size

\[
\operatorname{Cat}_j+\operatorname{Cat}_{j+1}.
\tag{3.1}
\]

At \(j=m-2\) there is one top component.  Let \(P_m\) and \(Q_m\) be its
old and new sides, and switch only this component.  The result

\[
G_m=(F_m\setminus P_m)\cup Q_m
\tag{3.2}
\]

is a binary positive exact factor.

### Theorem Z6.3 -- macroscopic empty coordinate interval

Put

\[
s_m=|P_m|=|Q_m|
=\operatorname{Cat}_{m-2}+\operatorname{Cat}_{m-1}.
\tag{3.3}
\]

Then:

1. If \(Z\in\mathcal X_m\) and
   \(F_m\cap G_m\subseteq Z\subseteq F_m\cup G_m\), then
   \(Z=F_m\) or \(Z=G_m\).
2. The difference
   \(g_m=\mathbf1_{G_m}-\mathbf1_{F_m}\) is a Graver primitive of
   \(A_m\).
3. For every \(H\),

   \[
   \widehat g_{m,H}=(g_m,B_Hg_m)
   \]

   is a Graver primitive of

   \[
   \widehat A_H=
   \begin{pmatrix}
   A_m&0\\
   B_H&-I
   \end{pmatrix}.
   \tag{3.4}
   \]

4. The exact support ratio is

   \[
   \boxed{
   \frac{s_m}{B}
   =
   \frac{(m+1)(5m-6)}{4(2m-1)(2m-3)}
   \longrightarrow\frac5{16}.
   }
   \tag{3.5}
   \]

#### Proof

After canceling the common wreaths of \(F_m\) and \(G_m\), their ownership
overlay is exactly the one connected top component \(P_m\sqcup Q_m\).
For a putative intermediate \(Z\), mark an old vertex when its wreath is
omitted and mark a new vertex when its wreath is selected.  At every
middle-set edge, the exact-cover equation says that the two endpoint marks
are equal.  Connectivity makes the mark constant on the component.  The
constant is zero or one, giving the two endpoints and proving part 1.

If \(0\ne h\sqsubseteq g_m\) and \(A_mh=0\), mark an old vertex by
\(-h_C\) and a new vertex by \(h_D\).  On every ownership edge the equation
\(A_mh=0\) makes these marks equal.  Thus the support is a nonempty union of
complete ownership components.  There is only one, so \(h=g_m\).  This is
Graver primitivity.

If \((h,w)\sqsubseteq(g_m,B_Hg_m)\) lies in the kernel of (3.4), then
\(A_mh=0\).  The preceding paragraph gives \(h=0\) or \(h=g_m\), and the
lower block forces \(w=B_Hh\).  This proves part 3.

Finally,

\[
\frac{\operatorname{Cat}_{m-1}}{\operatorname{Cat}_m}
=\frac{m+1}{2(2m-1)},
\qquad
\frac{\operatorname{Cat}_{m-2}}{\operatorname{Cat}_m}
=\frac{m(m+1)}{4(2m-1)(2m-3)}.
\]

Adding gives (3.5).  \(\square\)

### Corollary Z6.4 -- no sublinear conformal exchange axiom

Say that \(\mathcal X_m\) has the comparator-conformal \(R\)-exchange
property if, for every distinct \(F,G\in\mathcal X_m\), there is an exact
\(Z\ne F\) with

\[
\mathbf1_Z-\mathbf1_F\sqsubseteq
\mathbf1_G-\mathbf1_F,
\qquad
|F\setminus Z|\le R.
\tag{3.6}
\]

The pair in Theorem Z6.3 forces \(R\ge s_m\).  Hence no
\(R=o(B)\) conformal exchange axiom holds.  In particular, every
sign-compatible move family which decomposes all exact-factor differences
must contain a move with at least \((5/16+o(1))B\) wreaths on each side.

This includes the fixed-window augmented load lift for every fixed \(A\).
It rules out bounded-support exchange, Graver-proximity, and local
enumeration arguments whose theorem requires a universal \(o(B)\) move
bound.  It does not rule out a small nonconformal detour which leaves the
coordinate interval in (3.6).

### Proposition Z6.5 -- a genuine bounded-move nonglobal local minimum

The macroscopic hole obstructs not only the exchange axiom but every
bounded exact-move test set uniformly over affine, hence separable-convex,
objectives in the wreath-indicator coordinates.
Fix an integer \(R<s_m\), put

\[
C_m=F_m\cap G_m,
\quad P_m=F_m\setminus G_m,
\quad Q_m=G_m\setminus F_m,
\]

and define the affine-linear objective on exact factors

\[
L_R(Z)
=|Z\cap P_m|
+(R+1)\left(
|C_m\setminus Z|+|Z\setminus(F_m\cup G_m)|
\right).
\tag{3.7}
\]

Then

\[
L_R(F_m)=s_m,
\qquad
L_R(G_m)=0,
\tag{3.8}
\]

but \(F_m\) is a strict local minimum under **all** exact-factor moves
replacing at most \(R\) wreaths.

#### Proof

Let \(Z\ne F_m\) be exact with \(|F_m\setminus Z|\le R\).  If the penalty
parenthesis in (3.7) were zero, then \(Z\) would lie in the coordinate
interval of Theorem Z6.3.  It cannot equal \(G_m\), whose distance from
\(F_m\) is \(s_m>R\), and it cannot be any other factor.  Hence the penalty
is at least one.  Removing at most \(R\) old \(P_m\)-wreaths reduces the
first term by at most \(R\), so

\[
L_R(Z)-L_R(F_m)\ge-R+(R+1)>0.
\]

Yet (3.8) gives a better exact factor.  \(\square\)

The objective (3.7) is not the floor energy.  Proposition Z6.5 therefore
does not construct a bad floor-energy local minimum.  Its exact conclusion
is that no \(o(B)\)-support neighborhood can be a universal discrete-convex
test set even for affine-linear objectives on the genuine positive fibre.

## 4. The exact quadratic replacement: Gram-antagonistic packets

Let \(F,G\) be exact factors.  Cancel common wreaths and form their
middle-ownership overlay.  Let \(\mathscr K(F,G)\) be its connected
components.  For each component \(K\), orient from its \(F\)-side to its
\(G\)-side and put

\[
z_K=\mathbf1_{G\cap K}-\mathbf1_{F\cap K},
\qquad
v_K=B_Hz_K.
\tag{4.1}
\]

Switching any component subset \(J\subseteq\mathscr K(F,G)\) gives one
binary positive exact factor

\[
F_J=F+\sum_{K\in J}z_K.
\tag{4.2}
\]

Define

\[
\langle a,b\rangle_H
=
\sum_{q\le H}\frac{\langle a_q,b_q\rangle_2}{c_q},
\qquad
v_J=\sum_{K\in J}v_K,
\qquad
\Delta_F(J)=\Psi_H(F_J)-\Psi_H(F).
\tag{4.3}
\]

Quadratic expansion gives the exact cut identity

\[
\boxed{
\Delta_F(I\dot\cup L)
=
\Delta_F(I)+\Delta_F(L)+\langle v_I,v_L\rangle_H.
}
\tag{4.4}
\]

Call a nonempty packet \(J\) **Gram-antagonistic** if either \(|J|=1\),
or

\[
\langle v_I,v_{J\setminus I}\rangle_H<0
\tag{4.5}
\]

for every nonempty proper \(I\subsetneq J\).

### Theorem Z6.6 -- exact packet descent and the factor-two divisor

Suppose

\[
\Psi_H(G)=\Psi_H(F)-D,
\qquad D>0.
\tag{4.6}
\]

Then there is a Gram-antagonistic packet \(P\subseteq\mathscr K(F,G)\)
such that

\[
\boxed{
\Psi_H(F)-\Psi_H(F_P)
\ge
\frac D{|\mathscr K(F,G)|}
\ge
\frac D{\lfloor|F\setminus G|/2\rfloor}
\ge
\frac D{\lfloor B/2\rfloor}
\ge\frac{2D}{B}.
}
\tag{4.7}
\]

Every endpoint in (4.7) is a genuine binary positive exact factor.

#### Proof

Start with the full packet \(J_0=\mathscr K(F,G)\), whose change is
\(-D\).  Whenever a current packet \(J\) is not Gram-antagonistic, split it
as \(J=I\dot\cup L\) across a cut with
\(\langle v_I,v_L\rangle_H\ge0\).  Equation (4.4) gives

\[
\Delta_F(J)\ge\Delta_F(I)+\Delta_F(L).
\tag{4.8}
\]

Continue until every leaf packet is Gram-antagonistic.  If the leaves are
\(P_1,\ldots,P_t\), repeated use of (4.8) yields

\[
-D=\Delta_F(J_0)
\ge\sum_{a=1}^t\Delta_F(P_a).
\tag{4.9}
\]

Therefore one leaf has \(\Delta_F(P_a)\le-D/t\), and \(t\le
|\mathscr K(F,G)|\).

The two sides of every reduced ownership component have equal size: every
remaining wreath vertex has degree \(n\), so count its middle edges from
both sides.  A component of side size one would join two equal
middle-incidence columns and hence, by Lemma Z6.1, would be a canceled common
wreath.  Thus every component contains at least two old wreaths.  Its old
sides partition \(F\setminus G\), proving

\[
|\mathscr K(F,G)|
\le\left\lfloor\frac{|F\setminus G|}{2}\right\rfloor
\le\left\lfloor\frac B2\right\rfloor.
\tag{4.10}
\]

Combining (4.9)--(4.10) proves (4.7).  \(\square\)

### Theorem Z6.7 -- packet primitivity and exact local/global optimality

Every Gram-antagonistic packet \(J\) gives an applicable augmented-Graver
primitive

\[
(z_J,v_J)\in\mathcal G(\widehat A_H).
\tag{4.11}
\]

Conversely, every inclusion-minimal improving component packet for
\(\Psi_H\) is Gram-antagonistic.  Consequently

\[
\boxed{
F\text{ globally minimizes }\Psi_H
\iff
F\text{ has no improving Gram-antagonistic exact packet.}
}
\tag{4.12}
\]

Against a fixed global comparator, there exists a comparator-monotone
sequence of strict packet descents which reaches a global minimizer after at
most \(\lfloor B/2\rfloor\) moves.

#### Proof

Suppose a nonzero proper lifted kernel vector
\((h,w)\sqsubseteq(z_J,v_J)\) existed.  The middle equations force
\(h=z_I\) for a union \(I\) of complete ownership components, and the load
equations force \(w=v_I\).  Load conformality implies that \(v_I\) and
\(v_{J\setminus I}=v_J-v_I\) have the same coordinatewise signs wherever
nonzero.  Hence

\[
\langle v_I,v_{J\setminus I}\rangle_H\ge0,
\]

contrary to (4.5).  A singleton component has no proper middle-kernel
subcomponent, so it is primitive as well.  This proves (4.11).

If \(J\) is inclusion-minimal improving, then for every proper cut
\(J=I\dot\cup L\), both \(\Delta_F(I)\) and \(\Delta_F(L)\) are
nonnegative.  Since \(\Delta_F(J)<0\), (4.4) forces
\(\langle v_I,v_L\rangle_H<0\).  Thus \(J\) is Gram-antagonistic.

If \(F\) is nonglobal, apply Theorem Z6.6 to a global comparator to obtain
an improving packet.  The converse in (4.12) is immediate.  After switching
one such packet toward a fixed global comparator, those ownership components
cancel from the new overlay and never reappear.  Unless the new factor is
already global, apply the theorem to the remaining components.  There were
at most \(\lfloor B/2\rfloor\) initially.  \(\square\)

Theorem Z6.7 is a genuine objective-specific exchange theorem on the
positive exact fibre.  It allows disconnected cancellation-minimal packets,
as the full lifted Graver geometry requires; audited depth-\(1,2\) MSW
components give explicit disconnected lifted primitives for every
\(H\ge2\).  Theorem Z6.3 shows, in the opposite direction, that connected
primitives can themselves be macroscopic.

For completeness, the fixed-window disconnected primitive is obtained from
the genuine \(p=0\) MSW components indexed by

\[
R_0=(10)^{m-2},
\qquad
R_1=1100(10)^{m-4}
\qquad(m\ge4).
\tag{4.13}
\]

Fix all other component sides and orient these switches as \(z_0,z_1\).
The exact depth-two calculation in
`MATH_ATTACK_Z2_DISCRETE_CONVEXITY_20260724.md` shows that their common
nonzero dipole cancels in \(B_H(z_0-z_1)\).  Between the exact endpoints

\[
F=X+z_1,
\qquad
G=X+z_0,
\]

the only proper middle-kernel submoves are \(z_0\) and \(-z_1\), and each
has a nonzero coordinate where the total lifted load effect is zero.
Neither is conformal to the total.  Hence

\[
(z_0-z_1,B_H(z_0-z_1))\in\mathcal G(\widehat A_H)
\qquad(H\ge2),
\tag{4.14}
\]

although its wreath part is the union of two disconnected ordinary
ownership components.

## 5. The overload-equivalent replacement: full lifted Graver moves

The quadratic inner-product split is special to \(\Psi_H\).  The complete
test-set theorem survives for every separable discrete-convex load
potential, including \(\mathcal C_H\).

Lift an exact factor to

\[
\widehat x=(x,u),
\qquad
u=B_Hx,
\tag{5.1}
\]

inside the genuine box

\[
\widehat{\mathcal X}_{m,H}
=
\left\{
(x,u)\in\mathbb Z^{|\mathscr W_m|+d_H}:
\widehat A_H(x,u)=\binom{\mathbf1}{0},
\ 0\le x\le1,
\ 0\le u\le W\mathbf1
\right\}.
\tag{5.2}
\]

This lifted fibre is in bijection with positive exact factors.

For integer vectors \(a,b\), write \(a\sqsubseteq b\) when they are
coordinatewise sign-compatible and \(|a_i|\le|b_i|\) for every \(i\).
The Graver basis consists of the nonzero \(\sqsubseteq\)-minimal vectors in
\(\ker_{\mathbb Z}\widehat A_H\).

### Lemma Z6.8 -- conformal decomposition and feasible summands

For two lifted exact factors \(\widehat x,\widehat y\), their difference
has a conformal decomposition

\[
\widehat y-\widehat x
=g^1+\cdots+g^t,
\qquad
g^a\in\mathcal G(\widehat A_H),
\qquad
g^a\sqsubseteq\widehat y-\widehat x.
\tag{5.3}
\]

Every \(\widehat x+g^a\) is itself a lifted positive exact factor.  If
\(s=|\operatorname{supp}x\setminus\operatorname{supp}y|\), then

\[
t\le\left\lfloor\frac s2\right\rfloor.
\tag{5.4}
\]

#### Proof

If a nonzero kernel vector is not Graver-minimal, split off a proper
nonzero conformal kernel subvector.  Repeating terminates because the
\(\ell^1\)-norm strictly decreases, proving (5.3).

Conformality places \(\widehat x+g^a\) coordinatewise between the two boxed
endpoints.  It satisfies the lifted equations, so it is feasible and its
wreath part is binary.

The wreath coordinates of the summands partition the \(\pm1\) support of
\(y-x\).  For a nonzero summand, \(A_mg_x^a=0\).  Summing all middle rows
gives

\[
n\sum_C(g_x^a)_C=0,
\]

so the positive and negative wreath masses agree.  They cannot both have
mass one, since that would give two equal middle columns.  Lemma Z6.1 then
forces at least two removed and two added wreaths per summand.  Their old
supports are disjoint and use only the \(s\) old comparator differences,
which proves (5.4).  \(\square\)

### Lemma Z6.9 -- conformal convex superadditivity

Let \(\Phi(u)=\sum_i\phi_i(u_i)\), where every \(\phi_i\) is discrete
convex.  If \(h^1,\ldots,h^t\) are coordinatewise conformal, then

\[
\Phi\!\left(u+\sum_a h^a\right)-\Phi(u)
\ge
\sum_a\left[\Phi(u+h^a)-\Phi(u)\right].
\tag{5.5}
\]

#### Proof

At one coordinate all nonzero increments have one sign.  Discrete convexity
means that successive forward differences are nondecreasing.  Therefore
placing several positive increments together costs at least the sum of
placing each at the common base point.  The same statement for negative
increments follows by reversing the integer line.  Sum over coordinates.
\(\square\)

### Theorem Z6.10 -- complete Graver descent with the improved constant

Let \(\Phi\) be any separable discrete-convex load potential.  If exact
\(G\) is better than exact \(F\) by

\[
D=\Phi(F)-\Phi(G)>0,
\]

then an applicable augmented-Graver move takes \(F\) to an exact factor
\(F'\) with

\[
\boxed{
\Phi(F)-\Phi(F')
\ge
\frac D{\lfloor|F\setminus G|/2\rfloor}
\ge
\frac D{\lfloor B/2\rfloor}
\ge\frac{2D}{B}.
}
\tag{5.6}
\]

Consequently

\[
\boxed{
F\text{ globally minimizes }\Phi
\iff
F\text{ has no feasible improving augmented-Graver move.}
}
\tag{5.7}
\]

No nonzero scaled move \(\lambda g\), \(\lambda>1\), is feasible between
binary factor vertices.

#### Proof

Use (5.3).  If

\[
\delta_a=\Phi(F+g^a)-\Phi(F),
\]

then (5.5) gives

\[
-D=\Phi(G)-\Phi(F)\ge\sum_{a=1}^t\delta_a.
\tag{5.8}
\]

Hence some \(\delta_a\le-D/t\).  Apply (5.4) and \(s\le B\) to obtain
(5.6).  A nonglobal point therefore has an improving Graver move, while a
global point has no improving feasible move of any kind, proving (5.7).

Finally, a nonzero lifted kernel vector has nonzero wreath part.  If both
\(x\) and \(x+\lambda g_x\) are binary, then
\(\lambda|(g_x)_C|\le1\) on a nonzero coordinate.  Thus \(\lambda=1\).
\(\square\)

Theorem Z6.10 applies both to \(\Psi_H\) and to the corridor
\(\mathcal C_H\).  The objective-specific Theorem Z6.7 identifies a
smaller sufficient packet family for the quadratic potential.

## 6. The exact ceiling: complete exchange is the original optimum

For the fixed-window corridor define

\[
C^*_{m,A}
=
\min_{F\in\mathcal X_m}
\mathcal C_{\lceil A\sqrt m\rceil}(F),
\tag{6.1}
\]

and let \(\mathcal L^{\mathrm{Gr}}_{m,A}\) be the factors with no improving
applicable augmented-Graver move.

### Theorem Z6.11 -- logical completion ceiling

For every fixed \(A\) and every sufficiently large \(m\) such that
\(H=\lceil A\sqrt m\rceil\le m-1\),

\[
\mathcal L^{\mathrm{Gr}}_{m,A}
=
\operatorname*{argmin}_{F\in\mathcal X_m}\mathcal C_H(F).
\tag{6.2}
\]

Consequently the following asymptotic statements are equivalent:

1. every Graver-local factor has corridor \(o(W)\);
2. \(C^*_{m,A}=o(W)\);
3. there are exact factors with
   \(\sum_{q\le H}O_q/c_q=o(W)\).

If these hold for every fixed \(A>0\), they imply the literal
constant-one theorem.

#### Proof

Equation (6.2) is Theorem Z6.10 with \(\Phi=\mathcal C_H\).  Thus statements
1 and 2 are equivalent.  Statements 2 and 3 are equivalent by (1.8).
The every-\(A\) implication is (1.12) followed by the exact wreath transfer.
\(\square\)

More generally, any exact move family containing all applicable augmented
Gravers has precisely the global minimizers as its local minima.  Therefore
strengthening the neighborhood beyond Theorem Z6.10 cannot turn the
absolute \(o(W)\) optimum bound into a weaker local assertion.  One must
prove new positive-factor information which bounds (6.1).

This is the rigorous no-go for the pure exchange-convexity architecture:
the complete local/global theorem exists, with an explicit constant, but
its small-local-minimum statement is exactly MWB rather than an intermediate
lemma.

## 7. Static orbit averaging is also exactly the original optimization

The full coordinate orbit gives a tempting perfectly balanced fractional
object.  It does not reduce the integral optimum.

Let

\[
\mathcal U(F)=\biguplus_{\sigma\in S_n}\sigma F
\tag{7.1}
\]

be the indexed wreath-copy multiset.  Since \(S_n\) acts transitively on
the \((n-1)!/2\) unoriented wreaths and a wreath stabilizer has size
\(2n\), every wreath occurs in \(\mathcal U(F)\) exactly

\[
2n|F|=2nB=2W
\tag{7.2}
\]

times.  Thus \(\mathcal U(F)\) is independent of \(F\).  Its aggregate
depth-\(q\) load is exactly

\[
\sum_{\sigma\in S_n}\mu_q^{\sigma F}
=n!\frac W{N_q}\mathbf1.
\tag{7.3}
\]

An exact reblocking is a partition of this multiset of wreath copies into
\(n!\) positive exact factors.

### Theorem Z6.12 -- orbit reblocking identity

For every relabeling-invariant real functional \(\Phi\) on exact factors,

\[
\boxed{
\min_{\mathscr D\vdash\mathcal U(F)}
\frac1{n!}\sum_{G\in\mathscr D}\Phi(G)
=
\min_{G\in\mathcal X_m}\Phi(G),
}
\tag{7.4}
\]

and

\[
\boxed{
\min_{\mathscr D\vdash\mathcal U(F)}
\max_{G\in\mathscr D}\Phi(G)
=
\min_{G\in\mathcal X_m}\Phi(G).
}
\tag{7.5}
\]

#### Proof

Every block in every reblocking is an exact factor, so both left sides are
at least the one-factor minimum \(\Phi^*\).  Choose a minimizing factor
\(G^*\).  Equations (7.1)--(7.2) give
\(\mathcal U(G^*)=\mathcal U(F)\).  The indexed orbit
\((\sigma G^*)_{\sigma\in S_n}\) is therefore a reblocking of the same
multiset, and every block has value \(\Phi^*\).  \(\square\)

For \(\Psi_H\), \(\mathcal C_H\), entropy, or any other invariant convex
load potential, the orbit barycenter is perfectly uniform while each orbit
endpoint retains exactly its original energy.  Theorem Z6.12 says that an
integral reblocking theorem producing one low block is equivalent to the
original low-factor theorem.  Static Jensen averaging does not dissipate
the discrepancy; it hides it in the coordinate-frame coloring.

This closes static orbit averaging and colored full-orbit reblocking as
independent convexity relaxations.  It does not rule out an
incidence-sensitive reblocking theorem, adaptive component recomputation,
or construction of new perfect matchings using information beyond the
orbit barycenter; any such result would supply genuinely new positive-factor
information.

## 8. Exchange trajectories and literal-word cost

Every endpoint of Theorems Z6.6 and Z6.10 is exact, so the clean literal
route is to discard the trajectory and apply the wreath transfer directly
to the terminal factor.  Retaining all intermediate wreaths gives no free
connector theorem.

Let \(F_0,\ldots,F_T\) be an exact trajectory and let \(\mathcal P\) be the
set of all wreaths visited.  Write

\[
|\mathcal P|=B+R.
\tag{8.1}
\]

Orient each visited unoriented wreath arbitrarily and put
\(p=|\mathcal P|=B+R\).  The relaxed erosion-block transfer for these
\(p\) cyclic orders gives a literal word of length

\[
p(n+2H+1)
+2\sum_{q=0}^H M_q(\mathcal P)
+2\sum_{r=0}^{m-H-1}\binom nr-1.
\tag{8.2}
\]

Since \(F_0\subseteq\mathcal P\), the middle defect in (8.2) is zero.  The
novel-wreath overhead is

\[
(n+2H+1)R.
\tag{8.3}
\]

If \(s_t=|F_t\setminus F_{t-1}|\), then positive and negative move degrees
agree and every first-seen wreath is charged at its first positive support,
so

\[
R\le\sum_{t=1}^Ts_t.
\tag{8.3a}
\]

Also \(M_q(\mathcal P)\le M_q(F_t)\) for every visited factor, and every
hole contributes one full unit to the weighted corridor.  Therefore

\[
\sum_{q=0}^HM_q(\mathcal P)\le\mathcal C_H(F_t)
\tag{8.3b}
\]

when the harmless zero middle term is included.  Within the specific
erosion-block union construction (8.2), the extra core term (8.3) is
\(o(W)\) on a fixed Gaussian window exactly when \(R=o(B)\).  This is not a
lower bound on every conceivable literal encoding.

The Graver comparison proof gives one exact gain-density statement.  If
\(G\) is better than \(F\) by gap \(D\), a conformal Graver decomposition
with move degrees \(s_a=|(g_x^a)^-|\) satisfies

\[
\sum_as_a=|F\setminus G|\le B,
\qquad
\sum_a[-\delta_a]\ge D.
\]

Hence some applicable move obeys

\[
\boxed{
\frac{\Phi(F)-\Phi(F+g^a)}{s_a}
\ge\frac DB.
}
\tag{8.4}
\]

There is a stronger fixed-comparator statement.  Fix a global minimizer
\(G^*\) and one conformal augmented-Graver decomposition of the lifted
difference \(\widehat G^*-\widehat F_0\).  At any partial sum, all remaining
summands are still individually feasible and conformal.  Applying (5.5) at
the new base shows that, unless the current factor is already global, at
least one remaining summand improves.  Thus
there exists an improving path with disjoint wreath supports; every visited
factor lies inside \(F_0\cup G^*\), and

\[
\boxed{
\sum_ts_t\le|F_0\setminus G^*|\le B.
}
\tag{8.5}
\]

In particular, abstract convexity gives the universal \(O(B)\) ceiling,
which does not imply \(o(B)\).

For comparison, let \(\Phi^*=\min\Phi\), put
\(D_t=\Phi(F_t)-\Phi^*>0\), and recompute at each step a maximum
gain-per-degree Graver as in (8.4).  Before the final zero-gap move, its
total degree obeys

\[
\sum_{t<T}s_t
\le B\log\frac{D_0}{D_T}.
\tag{8.6}
\]

Indeed \(D_{t+1}\le D_t(1-s_t/B)\), and
\(-\log(1-x)\ge x\).  A final move, if needed, has degree at most \(B\).
This recomputed rule likewise supplies no \(o(B)\) conclusion from
convexity alone.

There is also an exact support/energy separation.  The wreath universe has

\[
M_m=\frac{(2m)!}{2}
\tag{8.7}
\]

elements, and \(B^2/M_m\to0\).  For any exact factors \(F,G\), a uniform
coordinate relabeling \(\pi\) satisfies

\[
\mathbb E_\pi|F\cap\pi G|=\frac{B^2}{M_m}.
\tag{8.8}
\]

Indeed \(B^2/M_m=1/3\) at \(m=2\), and the ratio of consecutive values is

\[
\frac{2(2m+1)}{(m+1)(m+2)^2}<1,
\tag{8.9}
\]

which also tends to zero.  Equation (8.8) follows from transitivity: each
of the \(B\) wreaths of \(G\) lands uniformly in the \(M_m\)-element
wreath universe.

Thus, for every \(m\ge2\), some relabeling makes
\(F\cap\pi G=\varnothing\), while preserving every relabeling-invariant
floor or corridor value of \(G\).  The endpoint difference is a legal exact
packet, namely a union of complete ownership components, but need not be one
Graver primitive or admit an arbitrary monotonically improving component
order.  Thus scalar energy values and drops alone do not force \(R=o(B)\) for
arbitrary support-feasible endpoint-packet trajectories.  Selecting a
literal-sparse improving Graver path would require an additional support
alignment theorem.  A literal trajectory-union theorem would likewise need
a separate proof of \(R=o(B)\), or a construction which does not retain
visited blocks.

This does not obstruct the terminal-factor route: the final exact factor
alone has exactly \(B\) wreaths and is already a valid input to the literal
transfer inequality.

## 9. Audited scope and final conclusion

The decisive statements have the following exact scopes.

1. **Native domain.**  Standard \(M/M^\natural/L/L^\natural\) and jump
   convexity fail independently of the chosen floor weights.
2. **Macroscopic obstruction.**  The support lower bound
   \(s_m=(5/16+o(1))B\) applies to comparator-conformal exchanges and to
   the actual Graver bases.  It does not forbid arbitrary nonconformal
   detours outside an endpoint coordinate interval.
3. **Quadratic replacement.**  Gram-antagonistic packets form an exact
   local/global test family for \(\Psi_H\), with gain at least \(2D/B\).
4. **General replacement.**  Applicable augmented Gravers form an exact
   test family for every separable discrete-convex load potential, again
   with gain at least \(2D/B\).
5. **Positivity.**  Every move endpoint is a binary exact factor.  No
   signed or fractional endpoint and no independent rankwise choice is
   used.
6. **Literal realizability.**  A terminal small-corridor factor composes
   through (1.10)--(1.12) into the already proved literal contiguous-OR
   word.  The exchange path itself need not be encoded.
7. **No overclaim.**  No \(o(W)\) upper bound on the global quadratic or
   corridor optimum is proved, and no high-energy floor-local factor is
   constructed.

The theorem-level closure of lane Z is therefore:

> The genuine exact-factor fibre has macroscopic conformal holes, so no
> sublinear-support discrete exchange convexity can hold.  Any complete
> sign-compatible replacement must allow macroscopic connected primitives,
> while the lifted geometry also contains disconnected cancellation-minimal
> packets.  Gram-antagonistic packets
> and augmented Gravers provide exact positive descent with the universal
> comparison factor \(2/\operatorname{Cat}_m\).  Once that complete
> neighborhood is installed, however, its local minima are exactly the
> unknown global corridor minima.  Proving those minima \(o(W)\) for every
> fixed Gaussian window is exactly MWB and hence the constant-one theorem,
> not a consequence of exchange convexity alone.
