# Lane B redirect: exact packet absorbers and a native-face no-go

## Conformal packet cubes, integral sparse thinning, and subexponential MSW rigidity

### 25 July 2026

## 0. Result

This note does not prove the constant-one theorem. It proves three new
statements at the exact-factor level.

1. The fractional survival-packet objective has an exact conformal Graver
   decomposition. Every subset of the resulting moves is one integral exact
   wreath factor, and the certified packet-cover gains add on the whole
   Boolean cube. This removes local minima for the packet objective while
   preserving exact middle ownership and keeping the quota variables
   integral and balanced at every leaf.

2. Any Boolean-compatible family of exact trades admits an integral
   sparse-thinning inequality. A bounded target-congestion, common-quota
   gain theorem would therefore contract the true weighted overload to
   \(O_A(H_A\operatorname{Cat}_m)=o(W)\), which composes through the audited
   diagonal and literal wreath transfer into
   \(\nu(k)\le(1+o(1))W(k)\).

3. The single static canonical MSW-versus-\((2\,3)\) component face is too
   rigid. Every connected region generated there by trades of degree
   \(e^{o(m)}\) has fixed-window overload diameter \(o(W)\). This remains
   true although its sublinear component strata can switch
   \((3/8+o(1))\operatorname{Cat}_m\) wreaths. Thus that entire native
   subexponential-degree face cannot supply a linear overload repair.

The unresolved assertion is absolute, not algebraic: either the minimum
packet-cover value must be shown to be
\(o_A(\operatorname{Cat}_m/\sqrt m)\), or one must construct the
bounded-congestion common-quota trade family isolated in Theorem 3.3 below.

Everything here concerns the unlabelled overload theorem. No common nested
labelled resolution is claimed.

## 1. Notation and exact overload

Put

\[
 n=2m+1,\qquad
 W=\binom nm,\qquad
 T=\frac Wn=\operatorname{Cat}_m,\qquad
 H=H_A=\lceil A\sqrt m\rceil .
\tag{1.1}
\]

Here \(A>0\) is fixed and \(m\) is sufficiently large that \(H\le m-2\).
At depth \(q\), write

\[
 N_q=\binom n{m-q},\qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,\qquad
 W=c_qN_q+r_q.
\tag{1.2}
\]

An exact factor \(F\) consists of \(T\) wreaths whose middle interval
families partition \(\binom{[n]}m\). Let \(\mu_q^F(S)\) be its lower
cyclic-interval load. If \(\mathcal B_q\) is the family of vectors with
exactly \(r_q\) coordinates \(c_q+1\) and every other coordinate \(c_q\),
then

\[
 O_q(F)=\frac12\min_{b\in\mathcal B_q}
                 \|\mu_q^F-b\|_1,
\qquad
 J_A(F)=\sum_{q=1}^{H}\frac{O_q(F)}{c_q}.
\tag{1.3}
\]

We use

\[
 S_A(m)=\sum_{q=1}^{H}\frac1{c_q}
       =(\kappa_A+o(1))\sqrt m,
\qquad
 \kappa_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
\tag{1.4}
\]

The equality in (1.3) and the asymptotic (1.4) are the audited overload
modulus and fixed-window ratio estimates. In particular, for any load
increment \(v\),

\[
 |J_A(\mu+v)-J_A(\mu)|
 \le\frac12\sum_{q,S}\frac{|v_q(S)|}{c_q}.
\tag{1.5}
\]

## 2. A full exact packet-absorber cube

Let \(\mathscr W_n\) be the finite catalogue of unoriented wreaths and
let \(M\) be its middle-incidence matrix. Exact factors are precisely the
nonnegative integral solutions

\[
 Mx=\mathbf1;
\tag{2.1}
\]

such a solution is automatically Boolean and has support size \(T\).

For a resource \(a=(q,S)\), let

\[
 \mathscr O_a=\{E\in\mathscr W_n:S\text{ is a length-}(m-q)
                         \text{ cyclic interval of }E\}.
\tag{2.2}
\]

A balanced quota is \(\beta_a=c_q+h_a\), where \(h_a\in\{0,1\}\) and

\[
 \sum_{S\in\binom{[n]}{m-q}}h_{q,S}=r_q.
\tag{2.3}
\]

For a selected factor \(x\), a fractional survival-packet cover is a vector
\(0\le y_E\le x_E\) such that

\[
 \sum_{E\in P}y_E\ge1
\tag{2.4}
\]

for every

\[
 P\subseteq\{E\in\mathscr O_a:x_E=1\},
 \qquad |P|=c_q+h_a+1.
\tag{2.5}
\]

Define

\[
 \Theta_A(F)=\min_{h,y}\sum_Ey_E,
\qquad
 \Theta_A^*=\min_{F\text{ exact}}\Theta_A(F).
\tag{2.6}
\]

### Lemma 2.1 (one integral conditional-packet lift)

Fix a positive integer \(D\). Denominator-\(D\) feasible covers for all
exact factors and balanced quotas are the projections of one nonnegative
integer equality system.

#### Proof

Introduce integer variables

\[
 x_E,\bar x_E,h_a,\bar h_a,Y_E,v_E\ge0
\]

and impose (2.1), (2.3), and

\[
 x_E+\bar x_E=1,\qquad
 h_a+\bar h_a=1,\qquad
 Y_E+v_E=Dx_E.
\tag{2.7}
\]

For every \(P\in{\mathscr O_a\choose c_q+1}\), impose

\[
 \sum_{E\in P}Y_E
 +D\sum_{E\in P}\bar x_E
 +Dh_a-s^{(1)}_{a,P}=D,
\qquad s^{(1)}_{a,P}\ge0.
\tag{2.8}
\]

For every \(P\in{\mathscr O_a\choose c_q+2}\), impose

\[
 \sum_{E\in P}Y_E
 +D\sum_{E\in P}\bar x_E
 -s^{(2)}_{a,P}=D,
\qquad s^{(2)}_{a,P}\ge0.
\tag{2.9}
\]

The complement equations make \(x,h\) Boolean. Equation (2.7) says
\(0\le Y_E/D\le x_E\). If a catalogue packet contains an unselected
wreath, a term \(D\bar x_E\) makes its inequality automatic. If all its
wreaths are selected, (2.8) enforces the size-\(c_q+1\) packets precisely
when \(h_a=0\), while (2.9) always enforces the size-\(c_q+2\) packets.
When \(h_a=0\), the latter constraints follow already from the former, but
including them is harmless. Thus \(y=Y/D\) satisfies exactly
(2.4)--(2.5), and every such denominator-\(D\) cover supplies the surplus
variables in (2.8)--(2.9). \(\square\)

### Theorem 2.2 (exact packet-absorber cube)

For every exact factor \(F\), there are pairwise middle-root-disjoint,
simultaneously applicable exact trades \(z_1,\ldots,z_s\), degrees
\(k_i=|z_i^-|=|z_i^+|\), and gains \(g_i>0\) such that, for every
\(I\subseteq[s]\),

\[
 F_I:=F+\sum_{i\in I}z_i
\tag{2.10}
\]

is an integral exact factor and

\[
 \boxed{
 \Theta_A(F_I)
 \le\Theta_A(F)-\sum_{i\in I}g_i.}
\tag{2.11}
\]

Moreover,

\[
 \boxed{
 \sum_i g_i=\Theta_A(F)-\Theta_A^*,
 \qquad 0<g_i\le k_i,
 \qquad \sum_i k_i\le T.}
\tag{2.12}
\]

The full child \(F_{[s]}\) is a global minimizer of \(\Theta_A\).

#### Proof

Choose an optimal packet cover above \(F\), and choose one globally optimal
factor, quota system, and cover. These are rational finite LP optima. Let
\(D\) be a common denominator and lift both endpoints, by Lemma 2.1, to
nonnegative integer solutions \(u,u^*\) of one equality system

\[
 \mathcal M_Du=b.
\]

Every integer kernel vector has a conformal decomposition into Graver
elements: if it is not already conformally minimal, split it into two
nonzero sign-compatible kernel vectors and iterate; the \(\ell_1\)-norm
strictly decreases. Thus write

\[
 u^*-u=\sum_iG_i
\tag{2.13}
\]

with every \(G_i\) sign-compatible with \(u^*-u\). Every partial sum
\(u+\sum_{i\in I}G_i\) lies coordinatewise between \(u\) and \(u^*\), so
it is nonnegative and feasible. Its \(x,h\) coordinates remain Boolean by
(2.7).

Let

\[
 \gamma_i=\frac1D\sum_E(G_i)_{Y_E}.
\tag{2.14}
\]

The vector \(u^*-G_i\) is feasible. If \(\gamma_i>0\), its cover objective
would be smaller than the global optimum, so \(\gamma_i\le0\). If the
factor projection \((G_i)_x\) is zero, then \(u+G_i\) is feasible over the
same factor \(F\); optimality of \(\Theta_A(F)\) gives
\(\gamma_i\ge0\), hence \(\gamma_i=0\).

Discard all zero-gain summands and put

\[
 z_i=(G_i)_x,\qquad g_i=-\gamma_i>0.
\]

Partial-sum feasibility gives (2.10)--(2.11). The discarded summands have
zero objective change, so summing (2.14) gives the first equality in
(2.12). The full retained child has a feasible cover of value
\(\Theta_A^*\), and is therefore globally optimal even if discarded
factor-changing zero-gain summands mean that it is not the originally
chosen endpoint.

Conformality between Boolean endpoint vectors makes the negative factor
supports of distinct \(z_i\) disjoint subsets of \(F\), and also makes their
positive supports disjoint. From the middle equations,

\[
 Mz_i=0.
\tag{2.15}
\]

Thus the positive side of \(z_i\) exactly repartitions the middle-root
packet owned by its negative side. Since \(F\) is exact, these packets are
pairwise disjoint. This proves exactness and simultaneous applicability of
every subset, as well as \(\sum_i k_i\le T\).

It remains to prove \(g_i\le k_i\). More generally, if two exact factors
differ by \(k=|F\setminus F'|\) rows, then

\[
 |\Theta_A(F')-\Theta_A(F)|\le k.
\tag{2.16}
\]

Retain an optimal quota and all old cover weights on common rows, and give
weight one to every new row. A packet of \(F'\) either contains a new row,
and is hit by that unit weight, or consists entirely of common rows and was
already a packet of \(F\). This gives
\(\Theta_A(F')\le\Theta_A(F)+k\); reverse the roles for the other
inequality. Applying (2.16) to \(F,F+z_i\), and using (2.11), yields
\(g_i\le k_i\). \(\square\)

### Corollary 2.3 (support-density dichotomy)

Let \(\Delta=\Theta_A(F)-\Theta_A^*\). Then

\[
 \sum_i k_i\ge\Delta.
\tag{2.17}
\]

For every \(D_0\ge1\), either at least

\[
 \frac{\Delta}{2D_0}
\tag{2.18}
\]

of the trades have degree at most \(D_0\), or the degree-\(>D_0\) trades
consume at least \(\Delta/2\) old wreaths in total.

#### Proof

Equation (2.17) follows from (2.12). If the small trades are fewer than
(2.18), their gains, each at most their degree and hence at most \(D_0\),
sum to less than \(\Delta/2\). The large trades carry more than half the
gain, and (2.12) makes their total degree at least that gain. \(\square\)

This is positive density of total replaced support when
\(\Delta=\Omega(T)\). It is not a positive-density count of bounded or
medium trades: all support could lie in one degree-\(\Theta(T)\) move.

### Corollary 2.4 (exact conditional composition into constant one)

If, for every fixed \(A>0\),

\[
 \boxed{
 \Theta_A^*=o_A(T/\sqrt m),}
\tag{2.19}
\]

then there is an exact factor with

\[
 J_A(F)=o(W).
\tag{2.20}
\]

Consequently the audited fixed-window diagonal and literal wreath-shadow
transfer give

\[
 \nu(k)\le(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\tag{2.21}
\]

#### Proof

For any factor and balanced quota system, the packet-cover-to-overload
theorem gives

\[
 J_A(F)\le3nH\,\vartheta(F,\beta).
\tag{2.22}
\]

Apply Theorem 2.2 through its full child and then use (2.19):

\[
 J_A(F_{[s]})
 \le3nH\Theta_A^*
 =3n\,O_A(\sqrt m)\,o_A(T/\sqrt m)
 =o(nT)=o(W).
\]

Fixed-window overload MWB is equivalent to (2.20) for every fixed \(A\).
The already proved slow diagonal, central literal wreath word, outer-tail
word, and parity lift then give (2.21). \(\square\)

### Proposition 2.5 (ordinary convex factor relaxation is vacuous)

In the natural real conditional-packet formulation underlying Lemma 2.1,
relax \(x,\bar x\) to \([0,1]\) while retaining \(Mx=\mathbf1\) (the quota
choice \(h\) may remain integral). Its minimum packet-cover objective is
zero.

#### Proof

Every middle target belongs to exactly

\[
 d=\frac{m!(m+1)!}{2}
\tag{2.23}
\]

unoriented catalogue wreaths: double-count catalogue wreath--middle-target
incidences, or arrange the chosen middle block and its complement and divide
by reversal. Hence \(x_E=1/d\) satisfies \(Mx=\mathbf1\). Choose any
integral balanced \(h\) and put \(y_E=0\). Every packet size \(k\) in
(2.8)--(2.9) is at least two, and

\[
 \sum_{E\in P}(1-x_E)=k(1-1/d)\ge1.
\]

Thus every conditional packet inequality holds with objective zero.
\(\square\)

Thus this natural joint ordinary relaxation has no positive objective
certificate. Coordinate averaging, packet-LP duality, or signed lattice
saturation applied only after relaxing the exact-factor selector cannot by
itself prove (2.19). A successful absolute argument must use additional
integral geometry of exact factors.

## 3. Integral sparse thinning of compatible trades

The packet cube is unbounded-degree and relative to an unknown optimum. The
next theorem gives an exact way to turn a genuinely local positive family
into bulk overload descent.

Fix one balanced quota tuple \(b=(b_q)_{q\le H}\) attaining (1.3) for an
exact factor \(F\), and write

\[
 \Phi_b(\mu)=\frac12\sum_{q,S}\frac{|\mu_q(S)-b_q(S)|}{c_q},
\qquad \Phi_b(\mu^F)=J_A(F).
\tag{3.1}
\]

A family of applicable exact trades is **Boolean-compatible at \(F\)** if
every subset can be applied simultaneously and produces an integral exact
factor. Pairwise-disjoint negative middle-root packets, with each positive
side exactly repartitioning its negative packet, are sufficient.

### Theorem 3.1 (exact sparse-thinning inequality)

Let \(z_1,\ldots,z_s\) be Boolean-compatible at \(F\), and let \(v_i\) be
their full fixed-window lower-load increments. Define

\[
 g_i=\Phi_b(\mu^F)-\Phi_b(\mu^F+v_i),
\tag{3.2}
\]

\[
 \omega_{ij}=\sum_{q,S}\frac{
       \min\{|v_{i,q}(S)|,|v_{j,q}(S)|\}}{c_q},
\quad
 G=\sum_i g_i,
\quad
 \Omega=\sum_{i<j}\omega_{ij}.
\tag{3.3}
\]

For every \(p\in[0,1]\), there is a subset \(I=I(p)\) such that its exact
leaf satisfies

\[
 \boxed{
 J_A(F_I)\le J_A(F)-pG+p^2\Omega.}
\tag{3.4}
\]

If \(G>0\), this certifies a gain of at least

\[
 \boxed{
 \begin{cases}
 G-\Omega\ge G/2,&G\ge2\Omega,\\[1mm]
 G^2/(4\Omega),&0<G<2\Omega.
 \end{cases}}
\tag{3.5}
\]

#### Proof

For \(D_a(x)=|x+a|-|x|\), the triangle inequality and symmetry give

\[
 |D_a(x+b)-D_a(x)|
 \le2\min(|a|,|b|).
\tag{3.6}
\]

Order the increments of a fixed subset \(I\). When \(v_i\) is added after
the earlier increments, move its base point back to the original base one
earlier increment at a time and apply (3.6). Summing coordinates, with the
factor \(1/2\) in (3.1), gives the deterministic inequality

\[
 \Phi_b\!\left(\mu^F+\sum_{i\in I}v_i\right)
 \le J_A(F)-\sum_{i\in I}g_i
       +\sum_{\{i,j\}\subseteq I}\omega_{ij}.
\tag{3.7}
\]

The same \(b\) is an admissible balanced quota at every leaf, so its true
overload is at most the left side. Select each trade independently with
probability \(p\). The expected right side of (3.7) is

\[
 J_A(F)-pG+p^2\Omega.
\]

Some integral exact leaf is no worse than this expectation, proving (3.4).
If \(G\ge2\Omega\), take \(p=1\). Otherwise take
\(p=G/(2\Omega)\). This proves (3.5). \(\square\)

### Corollary 3.2 (bounded target congestion)

Put

\[
 \ell_i=\frac12\sum_{q,S}\frac{|v_{i,q}(S)|}{c_q}.
\tag{3.8}
\]

Suppose every coordinate \((q,S)\) is affected by at most \(R\) of the
trades and

\[
 G\ge\alpha\sum_i\ell_i>0.
\tag{3.9}
\]

If \(R>1\), some exact leaf satisfies

\[
 \boxed{
 J_A(F_I)\le J_A(F)-\frac{\alpha}{4(R-1)}G.}
\tag{3.10}
\]

For \(R=1\), all fixed-quota gains add exactly.

#### Proof

For nonnegative \(a_i\), at most \(R\) of which are nonzero, layer cake
gives

\[
 \sum_{i<j}\min(a_i,a_j)
 =\int_0^\infty\binom{|\{i:a_i>t\}|}{2}\,dt
 \le\frac{R-1}{2}\sum_i a_i.
\tag{3.11}
\]

Apply this in every target-depth coordinate. Equations (3.3) and (3.8)
give

\[
 \Omega\le(R-1)\sum_i\ell_i
       \le\frac{R-1}{\alpha}G.
\tag{3.12}
\]

Since \(|g_i|\le\ell_i\), (3.9) forces \(\alpha\le1\). Thus
\(p=\alpha/[2(R-1)]\le1\) is admissible in (3.4), and substitution of
(3.12) proves (3.10). If \(R=1\), no two increments meet the same
coordinate, so (3.7) has no interaction term and is equality for
\(\Phi_b\). \(\square\)

### Theorem 3.3 (a scale-correct exact trade theorem would finish)

Assume that for every fixed \(A\) there are constants

\[
 R_A\in\mathbb N,\quad R_A\ge1,\qquad
 \alpha_A,\eta_A>0,\qquad \Lambda_A<\infty
\]

such that every exact factor satisfying

\[
 J_A(F)>\Lambda_AH_AT
\tag{3.13}
\]

has a Boolean-compatible exact trade family, measured against one common
optimal quota \(b\) for \(F\), with target congestion at most \(R_A\) and

\[
 G\ge\alpha_A\sum_i\ell_i,
\qquad
 G\ge\eta_A\bigl(J_A(F)-\Lambda_AH_AT\bigr).
\tag{3.14}
\]

Then

\[
 \min_FJ_A(F)\le\Lambda_AH_AT=o(W)
\tag{3.15}
\]

for every fixed \(A\), and therefore (2.21) holds.

#### Proof

Put

\[
 \delta_A=
 \begin{cases}
 \min\{1/2,\eta_A\},&R_A=1,\\[1mm]
 \min\{1/2,\alpha_A\eta_A/[4(R_A-1)]\},&R_A>1.
 \end{cases}
\]

If \(R_A=1\), use exact additivity. If \(R_A>1\), use Corollary 3.2.
In either case there is an exact leaf with

\[
 J_A(F_I)-\Lambda_AH_AT
 \le(1-\delta_A)
 \bigl(J_A(F)-\Lambda_AH_AT\bigr).
\tag{3.16}
\]

Strict descent in the finite exact-factor state space must terminate. It
cannot terminate above the threshold in (3.13), because (3.16) would give
another strict descent. Hence (3.15). Finally,

\[
 \frac{H_AT}{W}=\frac{H_A}{n}=O_A(m^{-1/2}),
\]

and the fixed-window diagonal and literal transfer give (2.21). \(\square\)

If every trade additionally has footprint \(\ell_i=O_A(m)\), as for a
general nonaligned profile-\(3\) move, then a linear value of \(G\) forces
\(\Theta_A(T)\) trades. Thus (3.14) is exactly a positive-density medium-
trade assertion, not a connectivity statement.

## 4. The static native MSW face is subexponentially rigid

Let \(F_m\) be the canonical MSW exact factor and
\(\tau=(2\,3)\). The audited component hierarchy of the static ownership
overlay \(F_m\cup\tau F_m\) consists of components

\[
 K_{j,R},\qquad
 0\le j\le m-2,\qquad R\in\mathcal D_{m-j-2},
\tag{4.1}
\]

where \(\mathcal D_t\) is the set of Dyck words of semilength \(t\), each
side has

\[
 s_j=C_j+C_{j+1},\qquad C_j=\operatorname{Cat}_j,
\tag{4.2}
\]

wreaths, and there are \(C_{m-j-2}\) components of type \(j\). Every side
choice is an exact factor. Let \(\mathcal Q_{m,J}\) be any face obtained by
freezing all bits with \(j>J\) and allowing arbitrary choices for
\(j\le J\).

### Lemma 4.0 (the two endpoint catalogues are disjoint)

For \(m\ge2\),

\[
 F_m\cap\tau F_m=\varnothing.
\tag{4.2a}
\]

#### Proof

Every wreath \(C\) has a \(\tau\)-fixed middle interval. Indeed, the two
transposed labels have total membership \(2m=n-1\) among the \(n\) middle
intervals. If every interval contained exactly one of them, that total
would be \(n\). Hence one interval contains both or neither and is fixed.
Thus \(C\) and \(\tau C\) share a middle target.

Also \(\tau C\ne C\) as unoriented cyclic orders. Otherwise a single
transposition would be a dihedral automorphism of an odd \(n\)-cycle.
A nontrivial rotation fixes no labels, while an odd-cycle reflection has
one fixed label and \(m\) transpositions; neither has the cycle type of
\(\tau\) when \(m\ge2\).

If \(C\in F_m\cap\tau F_m\), write \(C=\tau D\) with \(D\in F_m\). Then
\(C\ne D\), but the preceding fixed interval is owned by both \(D\) and
\(\tau D=C\), contradicting exactness of \(F_m\). \(\square\)

### Lemma 4.1 (one component's exact footprint bound)

For every controlled depth \(q\le H\),

\[
 a_q(K_{j,R})
 :=\frac12\|\mu_q^{K_{j,R}^{\rm new}}
              -\mu_q^{K_{j,R}^{\rm old}}\|_1
 \le4(j+2)s_j.
\tag{4.3}
\]

Consequently,

\[
 \ell_A(K_{j,R})\le4(j+2)s_jS_A(m).
\tag{4.4}
\]

#### Proof

Put \(d=2j+4\). The exact MSW concatenation law writes every old row of
\(K_{j,R}\) as

\[
 (\rho(A),\ d+\rho(R),\ n),
\tag{4.5}
\]

so the two labels transposed by \(\tau\) lie among the first \(d\) cyclic
positions. Their shorter cyclic distance \(\delta_C\) is at most \(d-1\).

For a cyclic row \(C\), let \(w_{C,r}\) be its length-\(r\) interval
indicator. For \(2\le r\le m\), direct interval counting gives

\[
 \|\tau w_{C,r}-w_{C,r}\|_1
 =4\min(r,\delta_C)-4\mathbf1_{\{\delta_C=r\}}
 \le4d.
\tag{4.6}
\]

Indeed, the start-position arcs of the \(r\)-windows containing the two
transposed labels have symmetric difference \(2\min(r,\delta_C)\). Each
such old-only interval normally has a distinct transposed new-only partner,
giving the factor two. Exactly when \(\delta_C=r\), the two boundary
intervals transpose to each other and remove four from the \(\ell_1\)
count. This proves (4.6).

The new side of a component is the coordinate transpose of its \(s_j\) old
rows. By the triangle inequality and (4.6), with \(r=m-q\ge2\),

\[
 a_q(K_{j,R})
 \le\frac12\sum_{C\in K_{j,R}^{\rm old}}
       \|\tau w_{C,m-q}-w_{C,m-q}\|_1
 \le2ds_j=4(j+2)s_j.
\]

Weighting and summing proves (4.4). \(\square\)

### Theorem 4.2 (native-face overload rigidity)

If \(J=J(m)=o(m)\), then

\[
 \boxed{
 \operatorname{diam}_{J_A}\mathcal Q_{m,J}
 \le(5+o(1))T S_A(m)\sqrt{J+1}.}
\tag{4.7}
\]

Equivalently,

\[
 \boxed{
 \operatorname{diam}_{J_A}\mathcal Q_{m,J}
 \le\left(\frac{5\kappa_A}{2}+o(1)\right)
 W\sqrt{\frac{J+1}{m}}=o(W).}
\tag{4.8}
\]

#### Proof

Two face vertices differ by a subset of the allowed component bits. Apply
(1.5) and (4.4):

\[
 |J_A(F)-J_A(F')|
 \le4S_A(m)\sum_{j=0}^{J}
        (j+2)s_jC_{m-j-2}.
\tag{4.9}
\]

The elementary Catalan estimate

\[
 C_j\le\frac{4^j}{(j+1)^{3/2}}
\tag{4.10}
\]

follows by putting \(b_j=4^{-j}\binom{2j}j\), observing

\[
 \frac{b_{j+1}}{b_j}=\frac{2j+1}{2j+2}
 \le\sqrt{\frac{j+1}{j+2}},
\]

and inducting. Hence

\[
 s_j\le\frac{5\,4^j}{(j+1)^{3/2}}.
\tag{4.11}
\]

Uniformly for \(j\le J=o(m)\), the exact adjacent Catalan ratios give

\[
 \frac{C_{m-j-2}}{C_m}
 =(1+o(1))4^{-j-2}.
\tag{4.12}
\]

Indeed, (4.18) below with \(k=j+2\) has logarithm \(O(j/m)=o(1)\).
Also, with \(N=J+1\),

\[
 \sum_{k=1}^{N}k^{-1/2}\le2\sqrt N-1,\qquad
 \sum_{k=1}^{N}k^{-3/2}\le3-\frac2{\sqrt N},
\]

so their sum is at most \(4\sqrt N\). Therefore

\[
 \begin{aligned}
 \frac1T\sum_{j=0}^{J}(j+2)s_jC_{m-j-2}
 &\le\left(\frac5{16}+o(1)\right)
       \sum_{j=0}^{J}\frac{j+2}{(j+1)^{3/2}}\\
 &\le\left(\frac54+o(1)\right)\sqrt{J+1}.
 \end{aligned}
\tag{4.13}
\]

Substitute into (4.9) to obtain (4.7). Equations (1.1) and (1.4) give
(4.8). \(\square\)

### Corollary 4.3 (a positive-density but overload-flat face)

If \(J\to\infty\) and \(J=o(m)\), the components allowed in
\(\mathcal Q_{m,J}\) contain

\[
 \left(\frac38+o(1)\right)T
\tag{4.14}
\]

old wreaths, while their entire overload diameter is \(o(W)\).

#### Proof

For every fixed \(j\), (4.12) applies, while (4.11) gives a summable
dominating tail after division by \(4^j\). Thus

\[
 \begin{aligned}
 \frac1T\sum_{j=0}^{J}s_jC_{m-j-2}
 &\longrightarrow
 \frac1{16}\sum_{j\ge0}\frac{C_j+C_{j+1}}{4^j}\\
 &=\frac1{16}\bigl(C(1/4)+4(C(1/4)-1)\bigr)\\
 &=\frac1{16}(2+4)=\frac38,
 \end{aligned}
\]

where \(C(x)=\sum_{j\ge0}C_jx^j\) and \(C(1/4)=2\). The diameter claim is
(4.8). \(\square\)

### Theorem 4.4 (exponential degree bottleneck in the static face)

For every fixed \(A,\varepsilon>0\), there is
\(\delta_{A,\varepsilon}>0\) such that, for all sufficiently large \(m\),
every path wholly contained in the static face

\[
 \mathfrak F[F_m,\tau F_m]
\tag{4.15}
\]

whose endpoints differ in \(J_A\) by at least \(\varepsilon W\) contains a
move of degree at least

\[
 2^{\lfloor\delta_{A,\varepsilon}m\rfloor-1}.
\tag{4.16}
\]

One may take

\[
 \delta_{A,\varepsilon}
 =\min\left\{\frac18,
 \frac{\varepsilon^2}{200e^2(A+1)^2}\right\}.
\tag{4.17}
\]

Consequently, if \(D_m=\exp(o(m))\) and a move atlas inside this one static
face has every edge of degree at most \(D_m\), each of its connected
components has \(J_A\)-diameter \(o(W)\).

#### Proof

The exact ratio identity

\[
 4^k\frac{C_{m-k}}{C_m}
 =\prod_{t=m-k+1}^{m}\left(1+\frac3{2t-1}\right)
\tag{4.18}
\]

is at most \(e\) for all sufficiently large \(m\) when
\(k\le m/4+2\). Repeating (4.9)--(4.13), now without an \(o(1)\) ratio,
gives for \(J\le m/4\)

\[
 \operatorname{diam}_{J_A}\mathcal Q_{m,J}
 \le5e\,T S_A(m)\sqrt{J+1}.
\tag{4.19}
\]

With \(J<\delta_{A,\varepsilon}m\), (1.4), (4.17), and \(W=(2m+1)T\)
make (4.19) strictly smaller than \(\varepsilon W\).

Also

\[
 C_1=1,\qquad C_j\ge2C_{j-1}\quad(j\ge2),
\]

so \(s_j\ge C_j\ge2^{j-1}\). A face move which changes a type-\(j\) bit
must replace at least its whole side of \(s_j\) wreaths; an arbitrary
composite changing that bit has degree at least \(s_j\). Here Lemma 4.0 and
the disjoint component partition ensure that the degree of a face move is
the sum of the side sizes of all changed bits. Therefore a path
whose every move has degree below (4.16) freezes every bit with
\(j\ge\lfloor\delta_{A,\varepsilon}m\rfloor\). Its endpoints lie in one
smaller face covered by (4.19), and so cannot differ by
\(\varepsilon W\). This proves (4.16).

For a uniform maximum degree \(D_m=\exp(o(m))\), choose
\(J=o(m)\) above every changeable bit index and apply (4.8). \(\square\)

The theorem covers arbitrary composites, repetitions, and paths inside the
single static support face (4.15). It does not cover a union of several
native faces, outside-face trades, or components recomputed after leaving
that face.

## 5. Exact status and adversarial audit

1. **The constant-one theorem is not proved.** The packet cube reaches
   \(\Theta_A^*\), not zero or \(o(T/\sqrt m)\). The estimate (2.19) is
   still unproved.

2. **Support density is not trade-count density.** Corollary 2.3 permits
   one degree-\(\Theta(T)\) move. The augmented Graver matrix also depends
   on the endpoint denominator \(D\); it is not a uniform bounded Markov
   basis.

3. **The sparse-thinning quota is common.** The gains in (3.2) are measured
   against one fixed optimal \(b\) for the current factor. Separately
   reoptimized individual overload gains do not imply (3.14).

4. **Every thinning leaf is integral.** No expectation is used as a
   fractional factor: expectation only selects one leaf among exact factors.
   The correct quantifiers in Theorem 3.1 are
   \(\forall p\,\exists I(p)\).

5. **The native no-go is static.** Theorem 4.4 definitively closes the
   subexponential-degree component graph of the single canonical
   \(F_m\)-versus-\((2\,3)F_m\) face. It does not rule out adaptive
   recomputation or genuinely outside-face medium trades.

6. **Literal realizability is preserved.** Every constructed state in
   Theorems 2.2 and 3.1 is one exact factor. If either (2.19) or the
   hypothesis of Theorem 3.3 is proved, (2.20) follows inside an exact
   factor and the already audited literal wreath word—not a fractional or
   separately depthwise object—gives the contiguous-OR conclusion.

Thus the strongest surviving Lane-B replacement lemma is precisely
Theorem 3.3's bounded-congestion, common-quota, positive-gain family. The
static native hierarchy cannot furnish it at subexponential degree, and
the zero-valued ordinary convex relaxation does not itself control the
alternative absolute packet bound (2.19).
