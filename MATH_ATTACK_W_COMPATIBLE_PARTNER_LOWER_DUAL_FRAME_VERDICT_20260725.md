# Compatible partner-pair and lower-dual charts: exact frame verdict

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

This report starts from
`MATH_AUDIT_PAIR_OMISSION_INTERVAL_CORNERS_AND_FLOOR_DESCENT_20260725.md`
and consolidates the independently audited partner-pair and lower-dual
attacks.  Every literal construction below is integral; the operators in
Section 1 and their formal lower copies are explicitly algebraic rather
than asserted physical charts.  No conclusion is drawn from a fractional
convex combination.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 T=\binom n{m-1},\qquad
 R_m=\operatorname {Cat}_{m-1}
     =\frac1{2m-1}\binom{2m-1}{m-1}.
\]

Throughout the physical lower-depth discussion, \(2\le H\le m-2\).
The intended asymptotic regime has \(H=o(m)\), in particular
\(H\asymp_A\sqrt m\).

There is a genuine positive algebraic result.  One can attach one fixed
conjugate exact factor to each member of a linear-size partner-pair family
\(\mathscr B_0\), and its coordinate involutions generate \(A_n\).  On
every nontrivial subset layer, and hence on every nonnegatively weighted
direct sum of signed-depth layers, they obey the exact frame inequality

\[
 \boxed{
 \sum_{B\in\mathscr B_0}\|(I-P_B)v\|_w^2
 \ge \frac1{288(n-1)^2}\|v\|_w^2,}
 \qquad P_B=\frac{I+\theta_B}{2}.
\tag{0.1}
\]

Formal upper and lower copies therefore have coherent signal at least

\[
 \boxed{
 \sum_{B\in\mathscr B_0}(A_B^++A_B^-)
 \ge \frac1{72(n-1)^2}\|v\|_w^2.}
\tag{0.2}
\]

The required literal low-boundary frame does **not** follow.  For the
currently certified partner-pair plus endpoint-dual architecture it is
false, for four separate exact reasons.

1. The complete partner star has no common direct \(F_A\)-old-side,
   fixed-background matching for \(m\ge6\).  Already the linear-size
   family \(\mathscr B_0\) used in (0.1) has no such common matching for
   \(m\ge8\).
2. Even without the owner obstruction, directly installing enough
   phase-one partner transports to eliminate all fixed-coordinate modes
   costs at least
   \[
      mR_m=\left(\frac18+o(1)\right)W
   \]
   typed independently selectable interval-component incidences, counted
   with multiplicity across charts.  This is not \(o(W/H)\).
3. The depth-isolated lower-dual atoms are exact Johnson edges and span
   every centered lower layer algebraically, but a nontrivial such atom
   cannot have both alternatives inside one fixed exact local factor.
   It intrinsically uses a conjugate typed copy of that factor.
4. Every certified endpoint-aligned or reverse-threshold lower interval
   has only one incidence-edge displacement at lower depth two.  A joint
   additive product catalog of \(b=o(W/H)\) such fixed components leaves a
   \((1-o(1))W\)-dimensional exact kernel.  Arbitrary multiway thresholds
   evade the binary rank count, but a product of \(b\) paths can fill at
   most \(b\) depth-two holes in one corner.

Thus the requested full weighted-mode frame under one direct
component-charged \(o(W/H)\) product catalog is refuted for the certified
partner-pair and endpoint-dual interval construction.  The result does not refute a new
non-endpoint-aligned circuit which reorders the entire chain of lower
endpoints through the interior of a long physical block, nor a
factor-specific theorem proving that every realizable defect has
negligible projection onto the kernels below.  Neither escape is presently
proved.  No constant-one conclusion is claimed.

## 1. A linear-size partner family gives a formal weighted frame

Fix

\[
 A=\{a,b\},\qquad
 R=[n]\setminus A=\{r_1,\ldots,r_{n-2}\}.
\]

For \(i<j\), define

\[
 \theta_{ij}=(a\ r_i)(b\ r_j),
 \qquad B_{ij}=\{r_i,r_j\}.
\tag{1.1}
\]

Fix an exact local factor \(F_A\) on \(R\), and attach exactly one factor
to each partner pair by

\[
 F_{B_{ij}}=\theta_{ij}F_A.
\tag{1.2}
\]

There is no duplicated factor type in (1.2).  Let

\[
 c=r_1,\qquad d=r_{n-2},\qquad
 \mathscr B_0=\{B\in\tbinom R2:c\in B\text{ or }d\in B\}.
\tag{1.3}
\]

Then

\[
 |\mathscr B_0|=2n-7.
\tag{1.4}
\]

### Lemma 1.1 (generation and diameter)

For \(n\ge7\), the involutions \(\theta_B\),
\(B\in\mathscr B_0\), generate \(A_n\).  Every element of \(A_n\) is a
word of length at most

\[
 D_n=12(n-1)
\tag{1.5}
\]

in these involutions.

#### Proof

Put

\[
 U=[n]\setminus\{a,c\},\qquad
 V=[n]\setminus\{b,d\}.
\]

Products of two generators whose partner pairs both contain \(c\) cancel
the common transposition \((a\ c)\) and give, up to orientation, every
rooted three-cycle \((b\ y\ z)\) on \(U\).  Hence they generate \(A_U\).
Similarly the pairs containing \(d\) give every rooted three-cycle
\((a\ y\ z)\) on \(V\), and hence \(A_V\).

The sets \(U,V\) cover \([n]\) and have intersection of size \(n-4\ge3\).
If a three-cycle meets both sides, choose distinct \(p,q\in U\cap V\).
The identities

\[
 (x\ y\ p)=(y\ p\ q)(x\ q\ p),
\tag{1.6}
\]

and

\[
 (x\ y\ z)=(x\ p\ z)(x\ y\ p)
\tag{1.7}
\]

express it as at most three three-cycles supported in \(U\) or \(V\).
Thus \(\langle A_U,A_V\rangle=A_n\).

Every rooted three-cycle used above is a product of two generators.  Every
three-cycle in \(A_U\) or \(A_V\) is a product of at most two rooted
three-cycles, and (1.6)--(1.7) use at most three such cycles.  An arbitrary
three-cycle therefore has generator length at most \(12\).

Finally, every even permutation is a product of at most \(n-1\)
three-cycles.  To see this, write it as an even number \(L\le n-1\) of
transpositions and pair them.  A pair sharing a point is one three-cycle,
while

\[
 (x\ y)(u\ v)=(x\ u\ y)(x\ u\ v)
\tag{1.8}
\]

for disjoint transpositions.  This proves (1.5). \(\square\)

### Theorem 1.2 (exact weighted partner frame)

Let \(1\le k\le n-1\), let \(v\) be a centered real function on
\(\binom{[n]}k\), and let \(P_B=(I+\theta_B)/2\).  Then

\[
 \boxed{
 \sum_{B\in\mathscr B_0}\|(I-P_B)v\|_2^2
 \ge\frac1{288(n-1)^2}\|v\|_2^2.}
\tag{1.9}
\]

The same assertion holds on an arbitrary finite direct sum of nontrivial
subset layers with arbitrary nonnegative weights.

#### Proof

The group \(A_n\) is transitive on every nontrivial subset layer.  Its
average kills a centered vector, and consequently

\[
 \frac1{|A_n|}\sum_{g\in A_n}\|v-gv\|_2^2=2\|v\|_2^2.
\tag{1.10}
\]

Write any \(g\) as a word of length \(\ell\le D_n\).  Telescoping and
Cauchy--Schwarz give

\[
 \|v-gv\|_2^2
 \le D_n^2
 \sum_{B\in\mathscr B_0}\|v-\theta_Bv\|_2^2.
\tag{1.11}
\]

Average (1.11), use (1.10), and substitute \(D_n=12(n-1)\):

\[
 \sum_B\|v-\theta_Bv\|_2^2
 \ge\frac1{72(n-1)^2}\|v\|_2^2.
\tag{1.12}
\]

Since \(I-P_B=(I-\theta_B)/2\), division by four proves (1.9).
Applying the result separately on each layer and summing its weight proves
the direct-sum statement. \(\square\)

For formal upper and lower copies of every operator, (1.12) is precisely
(0.2).  This establishes the desired algebraic span.  The remaining
sections prove that it cannot be realized by the direct low-boundary
interval construction.

## 2. Exact common-base owner obstruction

Let

\[
 K_m=\binom{2m-1}{m-1}.
\]

The predecessor convention in a row of \(F_A\) gives a bijection

\[
 f_A:\binom R{m-1}\longrightarrow\binom Rm,
 \qquad
 S\longmapsto Y(S)=S\cup\{p(S)\}.
\tag{2.1}
\]

Injectivity follows from exact middle ownership, and the two finite sets
have the same size \(K_m\).

For a partner family \(\mathscr B\subseteq\binom R2\), define its exposed
old roots by

\[
 \mathcal S(\mathscr B)=
 \left\{S\in\tbinom R{m-1}:
 \text{some }B\in\mathscr B\text{ satisfies }
 p(S)\in B\text{ and }B\cap S=\varnothing\right\}.
\tag{2.2}
\]

### Theorem 2.1 (common-background capacity)

For \(B\in\mathscr B\), put

\[
 \mathcal D_B=\{S\in\tbinom R{m-1}:S\cap B=\varnothing\}.
\]

Suppose one integral lower-saturating, middle-simple matching has a common
background and satisfies all three conditions below.

1. It uses the old \(F_A\)-token over every root in
   \(\bigcup_{B\in\mathscr B}\mathcal D_B\), and hence in particular over
   every root in \(\mathcal S(\mathscr B)\).
2. It saturates all other lower roots with distinct middle owners.
3. For every \(B\in\mathscr B\), the coherent endpoint obtained by
   replacing precisely the old tokens over \(\mathcal D_B\) by their
   \(F_B=\theta_BF_A\) alternatives, while leaving every token outside
   \(\mathcal D_B\) fixed, is middle-simple.

Then necessarily

\[
 \boxed{|\mathcal S(\mathscr B)|\le W-T=\frac{2W}{m+2}.}
\tag{2.3}
\]

#### Proof

For each exposed \(S\), choose a witnessing pair \(B(S)\).  Because
\(p(S)\in B(S)\) and \(B(S)\cap S=\varnothing\), its alternate owner is

\[
 Z(S)=\theta_{B(S)}Y(S)=S\cup\{\alpha_S\},
 \qquad \alpha_S\in A.
\tag{2.4}
\]

These alternate owners are pairwise distinct: intersecting \(Z(S)\) with
\(R\) recovers \(S\).  They meet \(A\), whereas all old owners \(Y(S)\)
avoid \(A\), so the two owner families are disjoint.  Moreover, fix the
witness \(B(S)\).  Every other token changed at its coherent endpoint has
an old \(F_A\)-owner contained in \(R\), while every token outside
\(\mathcal D_{B(S)}\) stays fixed.  If any other base token used \(Z(S)\),
that endpoint would therefore contain \(Z(S)\) twice.  Condition 3
excludes this.  Hence every \(Z(S)\) is unavailable to all other base
tokens.  The
\(|\mathcal S|\) old tokens and their \(|\mathcal S|\) reserved alternate
owners leave at most \(W-2|\mathcal S|\) owners for the other
\(T-|\mathcal S|\) tokens.  Therefore

\[
 T-|\mathcal S|\le W-2|\mathcal S|,
\]

which is (2.3). \(\square\)

### Corollary 2.2 (full and reduced star impossibility)

The complete partner star has no common background of the form in
Theorem 2.1 for any \(m\ge6\).  The reduced frame family
\(\mathscr B_0\) has none for any \(m\ge8\).

#### Proof

For the full star, every \(S\in\binom R{m-1}\) is exposed: choose
\(r\in R\setminus Y(S)\) and take \(B=\{p(S),r\}\).  Thus
\(|\mathcal S|=K_m\).  But

\[
 \frac{K_m}{W}=\frac{m+1}{2(2m+1)},
 \qquad
 \frac{W-T}{W}=\frac2{m+2}.
\tag{2.5}
\]

The necessary inequality \(K_m\le W-T\) is equivalent to

\[
 m^2-5m-2\le0,
\]

which fails for every integer \(m\ge6\).

For \(\mathscr B_0\), every \(S\) not containing both \(c,d\) is
exposed.  If \(c\notin S\), use a pair in the \(c\)-star containing
\(p(S)\), replacing a duplicate choice by \(\{c,r\}\) with
\(r\notin Y(S)\); if \(c\in S,d\notin S\), use the symmetric
\(d\)-star.  Hence the number of exposed roots is

\[
 \begin{aligned}
 L_m
 &=K_m-\binom{2m-3}{m-3}\\
 &=\frac{3m}{2(2m-1)}K_m.
 \end{aligned}
\tag{2.6}
\]

The condition \(L_m\le W-T\) is equivalent to

\[
 3m(m+1)(m+2)\le8(2m-1)(2m+1).
\tag{2.7}
\]

Left minus right equals

\[
 3m^3-23m^2+6m+8,
\]

which is positive at \(m=8\) and strictly increasing thereafter.
Thus (2.7) fails for every \(m\ge8\). \(\square\)

This obstruction is prior to flag energy and prior to boundary cost.  The
separate adjacent-pair cubes remain legal because their old backgrounds
depend on \(B\); Corollary 2.2 says that the direct \(F_A\)-old-side,
fixed-background spanning family cannot be made available at one common
state.  It does not prohibit recoding the old tokens or changing the base
architecture.

## 3. Exact physical interval lower bound

First note why the already compatible fixed-partition atlas cannot be the
desired frame.  For a priority partition

\[
 [n]=P_1\sqcup\cdots\sqcup P_m\sqcup\{z\},
\]

every adjacent pair-block transport fixes \(z\).  Hence, on every
nontrivial rank \(k\), all of those transports fix the centered nonzero
mode

\[
 h_{z,k}(U)={\bf1}_{\{z\in U\}}-\frac kn.
\tag{3.0}
\]

The same is true after arbitrary pair-block permutations, internal flips,
or lower-dual copies using those coordinate transports.  Thus the cheap
fixed-partition atlas has an exact kernel even with no boundary
restriction.  Re-pairing coordinates is necessary for a full algebraic
frame; Sections 2--3 show why the direct spanning re-pairing cannot be
made into the required physical catalog.

For one phase-one comparison \((A,B,\ldots)\leftrightarrow
(B,A,\ldots)\), the changed roots are

\[
 \mathcal D_B={S\in\tbinom R{m-1}:S\cap B=\varnothing\}.
\tag{3.1}
\]

In each cyclic row of \(F_A\), deleting the two positions in \(B\) leaves
two arcs of total length \(2m-3\).  One arc has length at least \(m-1\),
so at least one length-\((m-1)\) window avoids \(B\).  The carrier is not
the whole row, and its maximal components number at most two.  Since
\(F_A\) has exactly \(R_m\) rows, the component count \(r_B\) obeys

\[
 \boxed{R_m\le r_B\le2R_m.}
\tag{3.2}
\]

An individual chart is cheap when \(H=o(m)\), because

\[
 \frac{2Hr_B}{W}
 \le\frac{2H(m+1)}{(2m-1)(2m+1)}=o(1).
\tag{3.3}
\]

Joint spanning is different.

### Proposition 3.1 (support-cover catalog lower bound)

Suppose \(s\) common-\(A\) phase-one partner transports are installed in
one joint catalog.  If they have no common fixed-coordinate mode on a
nontrivial subset layer, then

\[
 \boxed{
 s\ge m,\qquad
 \sum_{\ell=1}^s r_{B_\ell}\ge mR_m,}
\tag{3.4}
\]

and

\[
 \boxed{
 \frac{mR_m}{W}
 =\frac{m(m+1)}{2(2m-1)(2m+1)}
 \longrightarrow\frac18.}
\tag{3.5}
\]

#### Proof

Each transport moves only \(A\cup B_\ell\).  If some \(z\in R\) lies in
no \(B_\ell\), every transport fixes the nonzero centered mode

\[
 h_{z,k}(U)={\bf1}_{\{z\in U\}}-\frac kn.
\tag{3.6}
\]

Thus the \(s\) two-sets \(B_\ell\) must cover all \(2m-1\) points of
\(R\), forcing \(s\ge m\).  Equation (3.2) and the exact ratio

\[
 \frac{R_m}{W}=\frac{m+1}{2(2m-1)(2m+1)}
\]

give (3.4)--(3.5). \(\square\)

Here and below the direct component cost counts a typed independently
selectable interval occurrence separately for each chart, even if two
charts happen to place a seam at the same untyped geometric position.  It
does not assert a lower bound on the final run count of an unconstructed
shared multiway realization.

In this component metric, the direct reduced frame catalog has at least

\[
 (2n-7)R_m=\Theta(W)
\]

components, while the full star has at least
\(\binom{n-2}{2}R_m=\Theta(mW)\).  None is an
\(o(W/H)\)-component catalog.  This does not rule out paying for one
chart at a time in a renewable menu, but Corollary 2.2 separately rules
out the natural common-state menu for the spanning family.

## 4. Exact lower-dual atoms, and why they leave one fixed factor

In a cyclic row \(\pi=(x_i)\) on \(2m-1\) coordinates, use

\[
 S_i=I_\pi(i,m-1),\qquad
 Y_i=I_\pi(i-1,m),
\]

\[
 L_q(i)=I_\pi(i+q-1,m-q),\qquad
 U_q(i)=I_\pi(i-1,m+q).
\tag{4.1}
\]

Fix \(2\le q\le H\le m-2\), and set

\[
 b=x_{i+q-2},\qquad a=x_{i+q-1},\qquad \tau=(a\ b).
\tag{4.2}
\]

### Theorem 4.1 (depth-isolated parallel atom)

The token at \(i\) in \(\pi\) and its conjugate token in \(\tau\pi\)
have the same lower root and middle owner.  Every upper flag, and every
lower flag except depth \(q\), is identical.  At depth \(q\), the exact
innovation is

\[
 \boxed{
 d_q^-=
 \delta_{L_q(i)-a+b}-\delta_{L_q(i)}.}
\tag{4.3}
\]

If the old tokens lie at distinct roots of an already lower-saturating,
middle-simple base matching, then arbitrary choices of their seam
alternatives remain centrally compatible: every alternative is parallel
to its original central edge.

#### Proof

Both \(a,b\) lie in \(S_i\), so \(\tau S_i=S_i\).  The predecessor
\(x_{i-1}\) is neither, so \(\tau Y_i=Y_i\).  Every upper flag contains
both \(a,b\) and is fixed.  A lower depth \(p<q\) contains both, depth
\(q\) contains \(a\) but not \(b\), and depth \(p>q\) contains neither.
This proves (4.3) and every asserted equality. \(\square\)

The vectors (4.3), over coordinate-orbit typed factors, are all oriented
edges of the Johnson graph on \(\binom{[n]}{m-q}\).  Here is the exact
availability check.  Given an edge

\[
 L\longmapsto L-a+b,
 \qquad a\in L,\quad b\notin L,
\]

choose \(D\) of size \(q-2\), disjoint from \(L\cup\{b\}\), and put
\(S=L\cup\{b\}\cup D\).  The \((m-1)\)-set \(S\) misses at least one
pair \(P\) of the priority partition.  In a row on
\(Q_P=[n]\setminus P\), order the positions of \(S\) as

\[
 D,\ b,\ a,\ L\setminus\{a\},
\]

and complete the cyclic order arbitrarily.  A coordinate-orbit copy of an
exact factor contains this ordered row, and (4.2) realizes the prescribed
edge.  Since the Johnson graph is connected, its oriented edge vectors
span the complete zero-sum vertex space.

This algebraic lower span is unavailable inside one fixed local factor.

### Proposition 4.2 (fixed-factor exclusion)

Assume \(m\ge3\).  If the token in Theorem 4.1 belongs to one exact local
factor \(F_P\), its nontrivial seam mate does not belong to the same
\(F_P\).

#### Proof

An adjacent transposition changes a cyclic length-\(m\) window as a set
only when the window contains exactly one of \(a,b\).  Exactly two of the
\(2m-1\) middle windows have this property.  Thus \(\pi\) and
\(\tau\pi\) share \(2m-3>0\) middle targets.

They are distinct even as unoriented cyclic rows.  Otherwise swapping only
the two labels \(a,b\) would induce a nonidentity dihedral automorphism of
the odd \((2m-1)\)-cycle while fixing its other \(2m-3\ge3\) labelled
positions.  A nonidentity rotation fixes no position and an odd-cycle
reflection fixes exactly one.  Distinct rows of an exact local factor have
disjoint middle-window sets, so both rows cannot belong to \(F_P\).
\(\square\)

The same contradiction may be phrased at the token level: the two tokens
have the same middle owner but different depth-\(q\) flags, whereas that
middle target has one pointed row occurrence in an exact factor.  Thus a
pure Johnson atom intrinsically moves from \(F_P\) to the conjugate factor
\(\tau F_P\).  It cannot supply a lower dictionary while retaining the
rule “one fixed factor per omitted pair.”

## 5. Collar rigidity and the lower-depth-two kernel

There is a purely physical identity

\[
 \boxed{
 L_q(i)=\bigcap_{h=0}^{q-1}S_{i+h}.}
\tag{5.1}
\]

Hence two endpoint-aligned phases with the same ordered lower roots on a
physical interval have identical lower depth-\(q\) flags except in the
last \(q-1\) starts.  At \(q=2\), one interval component changes at most
one lower occurrence.

The audited reverse predecessor/successor path has an exact telescope.
For a proper cyclic interval \(I=[u,v]\),

\[
 z_{I,q}^-=E_{m-q}(I)-E_{m-q}(I+q-1),
\tag{5.2}
\]

so at depth two

\[
 \boxed{
 z_{I,2}^-
 =\delta_{I_\pi(u,m-2)}-
  \delta_{I_\pi(v+1,m-2)}.}
\tag{5.3}
\]

A full cyclic interval has zero innovation.  Every same-orientation
partner interval has zero lower innovation at every depth.

Let

\[
 N_2^-=\binom n{m-2}
 =\frac{m(m-1)}{(m+2)(m+3)}W.
\tag{5.4}
\]

### Theorem 5.1 (additive binary low-boundary no-frame theorem)

Consider a jointly compatible binary product catalog consisting of
arbitrary same-orientation partner-pair intervals and \(b\) certified
endpoint-aligned or reverse lower-dual interval components.  Assume the
components are fixed commuting atoms on the lower-depth-two load ledger,
so every corner has the additive form

\[
 x_\varepsilon=x_0+\sum_{C=1}^b\varepsilon_Cz_C,
 \qquad \varepsilon_C\in\{0,1\}.
\tag{5.4a}
\]

Let
\(\mathcal Z_2^-\) be their lower-depth-two innovation span.  Then

\[
 \boxed{
 \dim\mathcal Z_2^-\le b,\qquad
 |\operatorname{supp}\mathcal Z_2^-|\le2b.}
\tag{5.5}
\]

Inside the zero-sum lower-depth-two layer, the common orthogonal kernel has
dimension at least

\[
 \boxed{N_2^- -1-b.}
\tag{5.6}
\]

There is also a coordinate-supported kernel of dimension at least
\(N_2^--2b-1\).  Therefore, if the lower-depth-two weight is positive,
no positive all-mode frame inequality can hold whenever \(b<N_2^--1\).
In particular it cannot hold for \(b=o(W/H)\).

#### Proof

By (5.3), each lower component is one signed incidence column of a graph
on the \(N_2^-\) target cells.  Thus \(b\) components have rank at most
\(b\) and use at most \(2b\) target coordinates.  Partner components add
no lower columns.  Every incidence column has coordinate sum zero, so
subtracting its rank from the \((N_2^--1)\)-dimensional zero-sum layer
gives (5.6).

More explicitly, if \(2b<N_2^--1\), choose two targets outside the union
of all endpoints.  Their difference \(v=\delta_X-\delta_Y\) is nonzero,
centered, and orthogonal to every catalog innovation.  Embedding this
vector in the full weighted signed-depth space, with every other component
zero, makes the left side of any positive frame inequality zero and its
right side positive. \(\square\)

Because \(N_2^-/W=1-O(1/m)\), a catalog with \(b=o(W/H)\) leaves a
\((1-o(1))W\)-dimensional kernel.  This conclusion grants simultaneous
compatibility and commutation of the fixed atoms; within this additive
product architecture, compatibility cannot rescue the frame.

## 6. Multiway thresholds: exact one-corner capacity

A multiway reverse path can have large affine span, so Theorem 5.1 must
not be applied by counting one entire path as one binary vector.  There is
nevertheless a sharp one-corner obstruction.

Assume \(m\ge6\).  Fix one reference threshold on each of \(b\) fixed,
mutually compatible reverse paths, and assume their product corners add
the individual path transfers on the load ledger.  Let
\(x\in\mathbb Z_{\ge0}^{N_2^-}\) be the reference
lower-depth-two load of mass \(T\), and let
\(y\in\mathbb Z_{\ge0}^{N_2^-}\) be the mass-\(T\) load after choosing an
arbitrary legal threshold on every path.  Define

\[
 V_+(y;x)=\sum_R(y_R-x_R)_+.
\]

### Theorem 6.1 (unit positive variation per path)

For every such product corner,

\[
 \boxed{V_+(y;x)\le b.}
\tag{6.1}
\]

If \(x\) has \(R_0\) zero coordinates, the undoubled depth-two factorial
excess with floor baseline one satisfies

\[
 \boxed{\Phi_2^-(y)\ge R_0-b.}
\tag{6.2}
\]

#### Proof

The exact difference between any two thresholds on one reverse path is
one consecutive interval between the two cuts, and (5.3) makes its complete lower-depth-two
innovation \(\delta_A-\delta_D\).  Summing \(b\) such unit transfers and
using subadditivity of positive \(\ell_1\)-variation proves (6.1).

At baseline one,

\[
 e_1(t)=\frac{(t-1)(t-2)}2
\]

is nonnegative on every nonnegative integer and satisfies \(e_1(0)=1\).
A zero coordinate of \(x\) can cease contributing only if it receives at
least one positive unit.  Inequality (6.1) permits this for at most \(b\)
of the \(R_0\) holes, proving (6.2). \(\square\)

For an exact numerical witness on the integral load simplex, assume
\(m\ge6\) and put \(N=N_2^-\).  Then

\[
 \frac TN=\frac{m+3}{m-1}=1+\frac4{m-1},
 \qquad
 \delta:=T-N=\frac{4N}{m-1}.
\tag{6.3}
\]

Start with a balanced mass-\(T\) vector having \(\delta\) coordinates of
load two and every other coordinate of load one.  On

\[
 R_0=\left\lfloor\frac{N-\delta}{2}\right\rfloor
\tag{6.4}
\]

disjoint pairs of load-one coordinates, replace \((1,1)\) by \((2,0)\).
The resulting nonnegative integral vector has mass \(T\), exactly \(R_0\)
holes, and

\[
 \Phi_2^-(x)=R_0,
 \qquad
 Q_2^-(x)=2R_0.
\tag{6.5}
\]

Consequently every corner obtainable from it by \(b\) certified paths
satisfies

\[
 \Phi_2^-(y)\ge R_0-b,
 \qquad
 Q_2^-(y)\ge2(R_0-b).
\tag{6.6}
\]

Here

\[
 R_0=\left(\frac12-o(1)\right)W.
\]

Thus \(b=o(W/H)\) unit-transfer paths cannot repair a dispersed linear
defect in one corner.  The vector (6.4)--(6.5) is an abstract integral
mass-\(T\) load.  Its realization as the histogram of one specified
prepared exact factor is **not proved**.  Accordingly (6.6) refutes a
universal theorem on the integral load simplex, but not a hypothetical
factor-specific theorem that first proves all realizable loads have
\(o(W)\) holes in this invariant sector.

## 7. Why coherent harmonic signal is not charged floor descent

Even if the common-base and lower-factor obstructions were bypassed, the
formal frame (0.2) would still not be the desired charged inequality.
Write the coherent displacement of one endpoint chart as

\[
 z_B=\sum_I z_{B,I},
 \qquad
 A_B=\|z_B\|_w^2,
 \qquad
 V_B=\sum_I\|z_{B,I}\|_w^2.
\tag{7.1}
\]

Use here the doubled factorial-floor normalization

\[
 \mathcal Q_w=\sum_{q,S}w_q
   (x_{q,S}-c_q)(x_{q,S}-c_q-1).
\]

For fair independent interval bits, direct expansion gives

\[
 \boxed{
 \mathbb E\mathcal Q_w
 =\frac{\mathcal Q_w(M_B^0)+\mathcal Q_w(M_B^1)}2
  -\frac{A_B-V_B}{4}.}
\tag{7.2}
\]

Indeed, the mean random load is the endpoint midpoint.  Its variance is
\(V_B/4\), whereas the average squared distance of the two coherent
endpoints from their midpoint is \(A_B/4\).  Rankwise mass is fixed, so
the adjacent-integer factorial floor differs from centered square norm by
a constant and the same identity holds for \(\mathcal Q_w\).
For the undoubled normalization \(\Phi_w=\mathcal Q_w/2\), the last term
in (7.2) is \(-(A_B-V_B)/8\).

Conditional on literal endpoints realizing the formal full-state coherent
signals in (0.2), that frame yields only

\[
 \boxed{
 \sum_B\bigl(A_B^++A_B^--V_B^+-V_B^-\bigr)
 \ge
 \frac1{72(n-1)^2}\|v\|_w^2
 -\sum_B(V_B^++V_B^-).}
\tag{7.3}
\]

Boundary count alone does not control the last term: a long interval has
two seams but can carry nonzero endpoint-strip action at many signed
depths.  Thus (0.1) is a coherent representation-theoretic frame, not a
charged factorial-energy theorem.

## 8. Independent audits of the decisive steps

### 8.1 Frame constant

The only losses are the word bound \(D_n=12(n-1)\), the group-average
identity (1.10), and the factor four between \(I-\theta_B\) and
\(I-P_B\).  They give

\[
 \frac{2}{D_n^2}\cdot\frac14
 =\frac1{288(n-1)^2}.
\]

No unstated spectral-gap theorem is used.

### 8.2 Owner capacity

The injection is recovered exactly by

\[
 Z(S)\cap R=S.
\]

The two reserved families are disjoint because old owners avoid \(A\)
and exposed alternate owners meet \(A\).  The full-star threshold reduces
to \(m^2-5m-2>0\), first true at \(m=6\).  The reduced-family threshold
reduces to

\[
 3m^3-23m^2+6m+8>0,
\]

true at \(m=8\) and increasing thereafter.  These counts were audited
independently of the group/frame proof.

### 8.3 Depth-two telescope

For \(I=[u,v]\),

\[
 \begin{aligned}
 E_{m-2}(I)-E_{m-2}(I+1)
 &=\sum_{i=u}^v\delta_{I_\pi(i,m-2)}
   -\sum_{i=u+1}^{v+1}\delta_{I_\pi(i,m-2)}\\
 &=\delta_{I_\pi(u,m-2)}
   -\delta_{I_\pi(v+1,m-2)}.
 \end{aligned}
\]

Every interior term cancels exactly.  This proves both the binary rank
bound and the unit positive-variation bound without probability or an
asymptotic approximation.

### 8.4 Fixed-factor lower atom

The proposed seam alternatives have the same middle owner but different
lower depth-\(q\) flags.  Exact ownership permits one pointed occurrence
of that owner in one local factor.  Hence both alternatives cannot belong
to that factor.  The algebraic Johnson span therefore cannot be silently
promoted to a literal fixed-factor span.

## 9. Exact proved and conditional boundary

The following are proved.

1. The \(2n-7\) partner transports in \(\mathscr B_0\) use one conjugate
   factor per omitted pair, generate \(A_n\), and satisfy (0.1) with the
   exact constant \(1/[288(n-1)^2]\).
2. The full direct \(F_A\)-old-side, fixed-background star has no common
   matching for \(m\ge6\), and the reduced frame family has none for
   \(m\ge8\).
3. Any direct common-\(A\), phase-one coordinate-transport catalog
   eliminating all fixed-coordinate modes costs at least
   \(mR_m=(1/8+o(1))W\) typed interval-component incidences.
4. Pure depth-isolated lower Johnson atoms are centrally compatible in
   the coordinate-orbit token multigraph and algebraically span each
   centered lower layer, but they cannot stay inside one fixed local
   factor.
5. A joint additive binary catalog of \(o(W/H)\) fixed endpoint lower
   intervals has an exact \((1-o(1))W\)-dimensional lower-depth-two
   kernel.
6. A product of \(b\) fixed mutually compatible reverse paths, whose
   ledger changes add pathwise, has at most \(b\) units of positive
   lower-depth-two variation in one corner.
7. Coherent frame signal and charged floor descent differ by the exact
   variance term in (7.2).

The following remain unproved and are not consequences of this report.

1. A non-endpoint-aligned necklace circuit with macroscopic interior
   lower-depth-two action, exact middle ownership, one fixed factor per
   omitted pair, and \(o(W/H)\) physical seams.
2. A factor-specific theorem showing that every prepared exact-factor
   defect has negligible projection on the fixed-coordinate and
   lower-depth-two kernels.
3. A renewable state-adaptive menu whose background is reconstructed
   after every choice and whose cumulative final boundary cost remains
   \(o(W/H)\).
4. A variance/curvature inequality that subordinates the \(V_B^\pm\)
   term in (7.3) to charged factorial excess.

Therefore the currently certified direct old-side,
component-charged partner-pair/endpoint-dual interval architecture is
closed at the stated boundary scale.  A surviving route may instead use a
different common base or old-token recoding, a quantitatively spanning
subfamily below the exposure cap (2.3), a renewed menu, a structurally
different nonlocal lower circuit, or a new factor-specific
invariant-subspace theorem.  None is proved here.
