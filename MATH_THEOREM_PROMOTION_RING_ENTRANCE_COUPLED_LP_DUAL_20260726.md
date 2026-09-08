# The promotion-ring entrance problem: exact coupled LP dual and convex-hull equivalence

Date: 2026-07-26

Method: pure mathematics.  The cyclic-frame constraint is retained in
every column of every program below.  No random-nibble heuristic is used.

## 0. Outcome

Let

\[
 q_0=\lceil m^{1/4}\rceil,\qquad
 H=\lfloor\sqrt{m\log m}\rfloor,\qquad
 M=m+H,
\]

and write

\[
 W=\binom{2m}{m},\qquad
 N=\binom{2m}{m-q_0},\qquad
 R=\binom{2m}{M}=N_H,\qquad
 T=MR.
\tag{0.1}
\]

The tuned-capacity calculation gives

\[
 T\ge W>N,\qquad T-N=o(W),\qquad T-W=o(W).
\tag{0.2}
\]

For every top \(U\in\binom{[2m]}M\), one must choose one oriented cyclic
frame \(\pi\) of \(U\).  The frame supplies

* \(M\) middle owners, its cyclic \(m\)-intervals;
* \(M\) entrance targets, its cyclic \((m-q_0)\)-intervals.

For an integral choice \(F\), let \(a_X(F)\) and \(b_S(F)\) be the two
load vectors.  Define the coupled deficiency

\[
 \Delta(F)=
 \sum_{X\in\binom{[2m]}m}(a_X(F)-1)_+
 +\sum_{S\in\binom{[2m]}{m-q_0}}(1-b_S(F))_+.
\tag{0.3}
\]

The first term is middle collision mass and the second is the entrance
hole count.  Necessarily \(\Delta(F)\ge T-W\).  The desired entrance
rounding is

\[
 \Delta(F)=T-W+o(W)=o(W).
\tag{0.4}
\]

This note proves four exact facts.

1. The natural LP relaxation, with actual cyclic frames as its columns,
   has value exactly

   \[
   \boxed{\operatorname{OPT}_{\rm LP}=T-W.}
   \tag{0.5}
   \]

   Its exact dual is

   \[
   \boxed{
   \max_{\substack{0\le u_X\le1\\0\le v_S\le1}}
   \left[
   \sum_Sv_S-\sum_Xu_X
   +\sum_U\min_{\pi\in\mathcal C(U)}
     \left(
       \sum_{X\in I_m(\pi)}u_X
       -\sum_{S\in I_r(\pi)}v_S
     \right)
   \right],}
   \tag{0.6}
   \]

   where \(r=m-q_0\).  The all-ones middle dual attains \(T-W\).
   Uniform frame weights attain the same value in the primal.  Thus
   there is no Farkas obstruction inside this natural relaxation beyond
   the already harmless \(T-W=o(W)\) owner surplus.  A genuinely
   integral odd-set-type inequality is not ruled out by this statement.

2. Let \(\bar x\) be the uniform fractional frame point and let
   \(\mathfrak G_\varepsilon\) be the set of integral selections with
   \(\Delta(F)\le T-W+\varepsilon W\).  Then

   \[
   \boxed{
   \bar x\in\operatorname{conv}(\mathfrak G_\varepsilon)
   \quad\Longleftrightarrow\quad
   \mathfrak G_\varepsilon\ne\varnothing.}
   \tag{0.7}
   \]

   Indeed the average of the \(S_{2m}\)-orbit of any one good selection
   is exactly \(\bar x\).  Consequently, testing membership in the
   good-selection convex hull is not a weaker LP task: it is logically
   equivalent to the desired integral existence theorem.

3. If the cyclic-frame constraint is deleted, the problem rounds
   integrally at the exact floor: every top can be assigned \(M\)
   distinct middle targets and \(M\) distinct entrance targets so that
   every target in either layer has load \(1\) or \(2\).  The total
   repeat masses are exactly \(T-W\) and \(T-N\).  Every ordinary Hall
   cut therefore passes.  A Lovász--Kruskal--Katona calculation also
   shows that, for every family \(\mathcal A\) of tops,

   \[
   M|\mathcal A|-|\partial_r\mathcal A|\le T-N=o(W).
   \tag{0.8}
   \]

4. Every integral or fractional one-frame-per-top selection has a fixed
   coordinate-degree vector in both layers.  Hence its degree-one
   Johnson character is forced and carries only the scalar surpluses in
   (0.2).  There is no degree-one character obstruction.  Any genuine
   obstruction or rounding theorem must see higher-order cyclic
   chronology.

Thus the exact LP, its dual, ordinary Hall cuts, and the first character
sector are completely settled.  The remaining gap is an integrality gap
created solely by requiring the two balanced target tables to be the
middle and entrance interval rows of the same cyclic frame on every top.

## 1. The exact integer program

Let

\[
 \mathcal U=\binom{[2m]}M,\qquad
 \mathcal X=\binom{[2m]}m,\qquad
 \mathcal S=\binom{[2m]}r,\quad r=m-q_0.
\tag{1.1}
\]

For \(U\in\mathcal U\), let \(\mathcal C(U)\) be the set of oriented
cyclic frames of \(U\), modulo rotation.  Thus
\(|\mathcal C(U)|=(M-1)!\).  For \(e=(U,\pi)\), define the incidence
coefficients

\[
 A_{Xe}=\mathbf1\{X\in I_m(\pi)\},\qquad
 B_{Se}=\mathbf1\{S\in I_r(\pi)\}.
\tag{1.2}
\]

Every column has

\[
 \sum_XA_{Xe}=M,\qquad \sum_SB_{Se}=M.
\tag{1.3}
\]

An integral selection is a vector \(x\in\{0,1\}^{\mathcal E}\), where
\(\mathcal E=\{(U,\pi)\}\), satisfying

\[
 \sum_{\pi\in\mathcal C(U)}x_{U,\pi}=1
 \qquad(U\in\mathcal U).
\tag{1.4}
\]

The two loads are

\[
 a_X(x)=\sum_eA_{Xe}x_e,\qquad
 b_S(x)=\sum_eB_{Se}x_e.
\tag{1.5}
\]

Summing (1.3)--(1.4) gives

\[
 \sum_Xa_X(x)=\sum_Sb_S(x)=T.
\tag{1.6}
\]

Introduce collision variables \(c_X\ge0\) and hole variables \(h_S\ge0\).
The exact integer program is

\[
\begin{array}{ll}
\text{minimize}&\displaystyle \sum_Xc_X+\sum_Sh_S\\[1mm]
\text{subject to}
 &\displaystyle \sum_\pi x_{U,\pi}=1
                    \quad(U\in\mathcal U),\\[1mm]
 &\displaystyle a_X(x)-c_X\le1
                    \quad(X\in\mathcal X),\\[1mm]
 &\displaystyle b_S(x)+h_S\ge1
                    \quad(S\in\mathcal S),\\[1mm]
 &x_{U,\pi}\in\{0,1\},\qquad c_X,h_S\ge0.
\end{array}
\tag{1.7}
\]

For fixed integral \(x\), the minimizing slack values are

\[
 c_X=(a_X(x)-1)_+,\qquad h_S=(1-b_S(x))_+,
\]

so (1.7) has objective exactly (0.3).

### Lemma 1.1 (the forced lower bound)

Every feasible integral or fractional point of (1.7) satisfies

\[
 \sum_Xc_X\ge T-W.
\tag{1.8}
\]

#### Proof

Sum the owner inequalities \(a_X-c_X\le1\) over all \(W\) owners and use
(1.6). \(\square\)

### Lemma 1.2 (exact two-layer coverage form)

For an integral selection \(x\), let

\[
 C_m(x)=|\{X:a_X(x)>0\}|,\qquad
 C_r(x)=|\{S:b_S(x)>0\}|.
\]

Then

\[
 \boxed{\Delta(x)=T+N-C_m(x)-C_r(x).}
\tag{1.9}
\]

#### Proof

For every nonnegative integer \(L\),

\[
 (L-1)_+=L-\mathbf1_{\{L>0\}}.
\]

Summing this identity over middle owners gives \(T-C_m(x)\), by (1.6).
The entrance hole count is \(N-C_r(x)\). \(\square\)

Thus the integer problem is exactly a two-layer maximum-coverage problem
under the partition constraint “one cyclic frame from each top.”  The
target value is \(C_m+C_r=W+N-o(W)\).  This also explains the
\(2/e\) independent-rounding benchmark below; generic submodular coverage
rounding does not by itself reach the required near-total coverage.

## 2. The exact LP dual

Relax only the integrality condition in (1.7), replacing it by
\(x_{U,\pi}\ge0\).  The cyclic-frame columns themselves are unchanged.

### Theorem 2.1 (dual formula)

The dual of the relaxed program is (0.6).

#### Proof

Write the owner constraints as

\[
 -Ax+c\ge-\mathbf1
\]

and the entrance constraints as

\[
 Bx+h\ge\mathbf1.
\]

Let \(u_X\ge0\) and \(v_S\ge0\) be their dual variables, and let \(z_U\)
be the free dual variable for (1.4).  The dual objective is

\[
 -\sum_Xu_X+\sum_Sv_S+\sum_Uz_U.
\tag{2.1}
\]

The \(c\)- and \(h\)-columns give

\[
 0\le u_X\le1,\qquad0\le v_S\le1.
\tag{2.2}
\]

For the actual cyclic-frame column \(e=(U,\pi)\), the zero primal cost
gives

\[
 -\sum_{X\in I_m(\pi)}u_X
 +\sum_{S\in I_r(\pi)}v_S+z_U\le0.
\tag{2.3}
\]

For fixed \(u,v\), the largest feasible value of \(z_U\) is

\[
 z_U=
 \min_{\pi\in\mathcal C(U)}
 \left(
 \sum_{X\in I_m(\pi)}u_X
 -\sum_{S\in I_r(\pi)}v_S
 \right).
\tag{2.4}
\]

Substitution in (2.1) proves (0.6). \(\square\)

### Theorem 2.2 (the relaxation is exactly tight at the scalar floor)

The LP optimum equals \(T-W\).

#### Proof

Give every frame over every top weight

\[
 \bar x_{U,\pi}={1\over(M-1)!}.
\tag{2.5}
\]

The exact frame-degree count gives the uniform loads

\[
 a_X(\bar x)={T\over W}=:\theta_m,\qquad
 b_S(\bar x)={T\over N}=:\theta_r.
\tag{2.6}
\]

By (0.2), both are at least one.  Thus

\[
 c_X=\theta_m-1,\qquad h_S=0
\]

is feasible and has objective

\[
 W(\theta_m-1)=T-W.
\tag{2.7}
\]

For the matching dual lower bound, take

\[
 u_X=1\quad(X\in\mathcal X),\qquad
 v_S=0\quad(S\in\mathcal S).
\tag{2.8}
\]

Every frame has \(M\) middle intervals, so (0.6) becomes

\[
 -W+\sum_UM=-W+MR=T-W.
\]

Weak duality and (2.7) prove equality. \(\square\)

### Proposition 2.3 (all dual cuts are dominated by scalar capacity)

For every \(u\in[0,1]^{\mathcal X}\) and
\(v\in[0,1]^{\mathcal S}\), the expression in (0.6) is at most \(T-W\).

#### Proof

For each top, the minimum over frames is at most the uniform average over
its frames.  Summing these averages over all tops gives

\[
 \sum_U\mathbb E_\pi
 \left(
 \sum_{X\in I_m(\pi)}u_X-\sum_{S\in I_r(\pi)}v_S
 \right)
 =\theta_m\sum_Xu_X-\theta_r\sum_Sv_S.
\tag{2.9}
\]

Consequently the dual expression is at most

\[
 (\theta_m-1)\sum_Xu_X+(1-\theta_r)\sum_Sv_S
 \le(\theta_m-1)W=T-W,
\tag{2.10}
\]

because \(\theta_r\ge1\). \(\square\)

This proof is stronger than merely exhibiting a feasible primal point:
it shows directly that **every** Farkas weighting of owners and entrance
targets is paid by the uniform frame average.  In particular, no
weighted Hall cut belonging to this LP improves the all-ones owner cut.
An additional valid inequality for the integral hull could still do so.

## 3. Convex hull of good integral selections

Let \(\mathfrak I\) be the finite set of all integral selections satisfying
(1.4), and put

\[
 \mathfrak G_\varepsilon=
 \{x\in\mathfrak I:\Delta(x)\le T-W+\varepsilon W\}.
\tag{3.1}
\]

The symmetric group \(G=S_{2m}\) acts on tops, frames, and selections by
coordinate relabelling.

### Theorem 3.1 (orbit-barycentre equivalence)

For every \(\varepsilon\ge0\), equation (0.7) holds.

#### Proof

If \(\bar x\) lies in the convex hull, the hull is nonempty, so the
reverse implication is immediate.

Conversely, suppose \(x^0\in\mathfrak G_\varepsilon\).  Relabelling only
permutes the two load vectors, so

\[
 \Delta(gx^0)=\Delta(x^0)
\qquad(g\in G).
\tag{3.2}
\]

Thus the entire orbit lies in \(\mathfrak G_\varepsilon\).  The action of
\(G\) is transitive on the formal frame columns: any oriented cyclic frame
on an \(M\)-set can be sent coordinate-by-coordinate to any other.
Therefore

\[
 y={1\over|G|}\sum_{g\in G}gx^0
\tag{3.3}
\]

is constant on all columns.  Every integral selection has exactly \(R\)
chosen columns, while the total number of columns is \(R(M-1)!\).
Consequently the constant in (3.3) is \(1/(M-1)!\), so
\(y=\bar x\).  Hence \(\bar x\) lies in
\(\operatorname{conv}(\mathfrak G_\varepsilon)\). \(\square\)

### Corollary 3.2 (exact separation criterion)

The desired \(o(W)\)-defect theorem is equivalent to the following
statement: for every fixed \(\varepsilon>0\) and all sufficiently large
\(m\), every linear functional \(c\) on frame columns satisfies

\[
 \langle c,\bar x\rangle
 \le
 \max_{x\in\mathfrak G_\varepsilon}\langle c,x\rangle.
\tag{3.4}
\]

#### Proof

This is the finite-dimensional separation theorem applied to Theorem
3.1. \(\square\)

The equivalence is diagnostic rather than a proof.  It says that one
cannot certify membership of the uniform point in the good convex hull
without, in effect, proving the integral existence statement itself.

### Proposition 3.3 (rigorous constant-defect convex-hull membership)

For every fixed \(\varepsilon>2/e\), and all sufficiently large \(m\),

\[
 \boxed{\bar x\in\operatorname{conv}(\mathfrak G_\varepsilon).}
\tag{3.5}
\]

More precisely, independent uniform frames have

\[
 \mathbb E\Delta(F)
 =T-W+\left({2\over e}+o(1)\right)W.
\tag{3.6}
\]

#### Proof

For a rank-\(k\) target \(Q\), put

\[
 R_k=\binom{2m-k}{M-k},\qquad
 p_k={M\over\binom Mk}.
\tag{3.7}
\]

There are \(R_k\) tops containing \(Q\).  Their frame choices are
independent, and in each such top \(Q\) is an interval with probability
\(p_k\).  Therefore its load is exactly

\[
 L_k\sim\operatorname{Bin}(R_k,p_k),\qquad
 R_kp_k={T\over\binom{2m}{k}}=:\theta_k.
\tag{3.8}
\]

At both \(k=m\) and \(k=r=m-q_0\), one has

\[
 p_k=o(1),\qquad\theta_k=1+o(1).
\tag{3.9}
\]

For the entrance layer,

\[
 \mathbb E(1-L_r)_+
 =\Pr(L_r=0)=(1-p_r)^{R_r}=e^{-1}+o(1).
\tag{3.10}
\]

For the middle layer, the identity

\[
 (L_m-1)_+=L_m-\mathbf1_{\{L_m\ge1\}}
\]

gives

\[
\begin{aligned}
 \mathbb E(L_m-1)_+
 &=\theta_m-\left(1-(1-p_m)^{R_m}\right)\\
 &=(\theta_m-1)+e^{-1}+o(1).
\end{aligned}
\tag{3.11}
\]

Summing (3.10) over \(N=(1+o(1))W\) entrance targets and (3.11)
over \(W\) middle targets proves (3.6), since
\(W(\theta_m-1)=T-W\).

Some integral selection has defect at most the expectation.  For any
fixed \(\varepsilon>2/e\), it belongs to
\(\mathfrak G_\varepsilon\) for all sufficiently large \(m\).
Theorem 3.1 then proves (3.5). \(\square\)

Thus the current rigorous convex-hull interval is sharp in form:

\[
 \bar x\in\operatorname{conv}
 \{\Delta\le T-W+(2/e+o(1))W\},
\]

while replacing the constant \(2/e\) by \(o(1)\) is the unresolved
correlated-rounding theorem.

## 4. Ordinary Hall cuts after deleting cyclic chronology

It is useful to identify exactly what happens if one keeps top containment
but forgets that each top's \(M\) chosen targets must form one cyclic
interval family.

### Proposition 4.1 (exact independent table rounding)

There is an integral assignment of \(M\) distinct middle targets to every
top such that every middle target has load \(1\) or \(2\), with exactly
\(T-W\) load-two targets.  Independently, there is an integral assignment
of \(M\) distinct entrance targets to every top such that every entrance
target has load \(1\) or \(2\), with exactly \(T-N\) load-two targets.

#### Proof

Fix either target rank \(k\in\{m,r\}\).  In the bipartite inclusion graph
between \(M\)-tops and rank-\(k\) targets, put the fractional value

\[
 {M\over\binom Mk}
\tag{4.1}
\]

on every incidence.  Every top has total flow \(M\).  Every target has
load

\[
 \binom{2m-k}{M-k}{M\over\binom Mk}
 ={MR\over\binom{2m}{k}},
\tag{4.2}
\]

which lies in \([1,2)\) for both \(k=m,r\) when \(m\) is large.
Impose unit capacity on each incidence, demand \(M\) at every top, and
give every target lower capacity \(1\) and upper capacity \(2\).
The displayed fractional flow is feasible.  Bipartite network-flow
integrality gives an integral feasible flow.

The total assigned mass is \(T\), so exactly
\(T-\binom{2m}{k}\) targets have load two. \(\square\)

Thus even the coupled scalar budgets admit perfect independent integral
tables.  The missing condition is precisely:

\[
 \text{the two \(M\)-sets assigned to a top must be }
 I_m(\pi)\text{ and }I_r(\pi)\text{ for one frame }\pi.
\tag{4.3}
\]

### Proposition 4.2 (every ungrouped entrance Hall cut has only global deficiency)

For every \(\mathcal A\subseteq\mathcal U\), let

\[
 \partial_r\mathcal A=
 \{S\in\mathcal S:S\subseteq U\text{ for some }U\in\mathcal A\}.
\]

Then (0.8) holds.

#### Proof

Write \(|\mathcal A|=\binom{x}{M}\) for the unique real \(x\in[M,2m]\).
The continuous Lovász form of the Kruskal--Katona theorem gives

\[
 |\partial_r\mathcal A|\ge\binom{x}{r}.
\tag{4.4}
\]

For \(r<M\), the function

\[
 f(x)={\binom{x}{r}\over\binom{x}{M}}
\]

is decreasing on \([M,\infty)\).  Hence

\[
 {|\partial_r\mathcal A|\over|\mathcal A|}
 \ge {N\over R}.
\tag{4.5}
\]

It follows that

\[
\begin{aligned}
 M|\mathcal A|-|\partial_r\mathcal A|
 &\le\left(M-{N\over R}\right)|\mathcal A|\\
 &\le\left(M-{N\over R}\right)R=T-N=o(W).
\end{aligned}
\]

This proves (0.8). \(\square\)

The full family \(\mathcal A=\mathcal U\) attains the final deficiency
\(T-N\).  Therefore, at the ordinary containment level, the global scalar
surplus is the extremal Hall cut.  Any worse cut must use cyclic-frame
compatibility, not just top containment.

## 5. The degree-one character is frozen

### Proposition 5.1 (exact coordinate degrees)

For every fractional or integral \(x\) satisfying the top equalities
(1.4), and every coordinate \(i\in[2m]\),

\[
 \boxed{
 \sum_{X\ni i}a_X(x)
 =m\binom{2m-1}{M-1},\qquad
 \sum_{S\ni i}b_S(x)
 =r\binom{2m-1}{M-1}.}
\tag{5.1}
\]

#### Proof

In any cyclic frame on \(U\), each coordinate of \(U\) belongs to exactly
\(k\) of the \(M\) cyclic intervals of length \(k\).  Therefore a selected
frame on a top containing \(i\) contributes exactly \(m\) to the first
sum and \(r\) to the second.  There are
\(\binom{2m-1}{M-1}\) tops containing \(i\), and every top has total frame
weight one. \(\square\)

### Corollary 5.2 (no first-character obstruction)

The projections of \(a(x)-(T/W)\mathbf1\) and
\(b(x)-(T/N)\mathbf1\) onto the first nonconstant Johnson eigenspaces
vanish identically.

#### Proof

The first Johnson eigenspace is generated by the centered coordinate-star
indicators.  Equation (5.1) says that every such inner product is zero.
\(\square\)

Thus coordinate stars, their linear combinations, and all degree-one
representation-theoretic tests see no defect beyond the scalar totals.
A separating invariant, if one exists, must occur in Johnson degree at
least two or must couple the two ranks nonlinearly.

## 6. Exact remaining theorem

The coupled entrance problem has now been reduced without loss to:

> **Cyclic two-row resolution theorem (open).**  Select one cyclic frame
> on every rank-\(M\) top so that
> \[
> \sum_X(a_X-1)_+
> +\#\{S:b_S=0\}
> =T-W+o(W).
> \]

The natural LP and every one-rank containment Hall cut attain the scalar
floor; the uniform point belongs to the good integral convex hull if and
only if this theorem is true.  Consequently a successful proof must give
one of the following genuinely integral objects:

1. a dependent rounding theorem for cyclic-frame columns that beats the
   usual mean-one coverage loss;
2. a higher-order alternating-cycle exchange that preserves middle
   collision mass while filling entrance holes; or
3. a proof that the cyclic interval incidence matrices have asymptotically
   vanishing integrality gap under the two-row objective (0.3).

No fractional Farkas, ordinary Hall, scalar-capacity, or degree-one
character obstruction remains.
