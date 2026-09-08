# Lane D: the single-copy orbit-rounding obstruction

Date: 2026-07-25

Method: pure mathematics only. No finite search, solver, web search, or
computer-assisted experiment is used.

## 0. Verdict

This report does not prove the constant-one theorem. It proves one
wreath-specific restricted rounding lemma that composes quantitatively into
constant one, and it definitively closes the **generic
orbit-discrepancy/rounding lane**.

The conclusions have four exact levels.

1. For actual wreath factors, every relabeling-invariant single-factor
   objective is constant on a coordinate orbit. More strongly, the full
   permutation-indexed orbit multicover is universal: it is independent of
   the factor that generated it. Optimizing either overload or the new
   fractional survival-packet cost over exact reblockings of that multicover
   is exactly the original one-factor optimization problem, not a
   relaxation.

2. Symmetrizing a fractional packet cover over the orbit makes its wreath
   weights constant. Any common threshold then selects either every wreath
   in a factor or none. There is no deterministic equivariant rounding of
   the invariant orbit barycenter to one exact factor, or even to one
   nonconstant balanced integer quota vector at a depth with
   \(0<s_q<N_q\).

3. Inside a genuine two-factor wreath ownership overlay, the correct
   deterministic target is a thin **quantization shell**, not zero vector
   discrepancy. If the multidepth component effects are collinear, the
   midpoint is already on that shell, and every nonzero-effect component has
   \(o(\sqrt W/m)\) wreaths per side, a scalar greedy signing makes both
   complementary children exact factors with weighted overload \(o(W)\).
   This is a proved, support-feasible special case.

4. Most decisively for generic rounding, there is an explicit transitive
   exact-cover
   countermodel in which:

   * every atom owns exactly \(n\) middle targets and \(n\) lower targets;
   * exact factors have formal Catalan size \(B=W/n\);
   * the complete factor orbit is exactly lower-balanced;
   * the two-factor ownership overlay is connected;
   * the survival-packet rank is only \(3\);
   * nevertheless every exact factor has overload \(W/2\), collision excess
     \(W\), and fractional packet-cover value exactly \(B/3\).

Thus transitivity, exact one-cover constraints, equal degrees, balanced
orbit marginals, connected overlays, ordinary discrepancy, and bounded-rank
Packet Hall do not imply any \(o(W)\) single-factor overload or
\(o(B/\sqrt m)\) packet cover. Any successful continuation must prove a
genuinely cyclic-window-specific support-feasible trade theorem. Such a
theorem would no longer follow from orbit balance or generic vector
rounding; it is precisely the missing one-factor content.

The countermodel is not a cyclic-wreath factor and therefore does not
disprove MWB or the contiguous-OR conjecture. It is a definitive
counterexample to the proposed **generic mechanism**.

## 1. Actual wreath-factor objectives

Put

\[
n=2m+1,\qquad
W=\binom nm,\qquad
B=\operatorname{Cat}_m=\frac Wn.
\tag{1.1}
\]

Let \(\Omega_m\) be the set of unoriented cyclic orders on \([n]\), modulo
rotation and reversal. An exact middle wreath factor \(F\subseteq\Omega_m\)
has

\[
|F|=B
\tag{1.2}
\]

and its cyclic length-\(m\) intervals cover every middle set exactly once.

For a fixed \(A>0\), put

\[
K_A=\lceil A\sqrt m\rceil.
\tag{1.3}
\]

At depth \(q\), write

\[
N_q=\binom n{m-q},
\qquad
\lambda_q=\frac W{N_q},
\qquad
c_q=\lfloor\lambda_q\rfloor.
\tag{1.4}
\]

Let \(\mu_q^F(S)\) be the number of wreaths of \(F\) in which \(S\) is a
cyclic length-\((m-q)\) interval. A balanced quota is

\[
\beta_q(S)\in\{c_q,c_q+1\},
\qquad
\sum_S\beta_q(S)=W.
\tag{1.5}
\]

The minimum balanced overload is

\[
O_q(F)
=
\min_{\beta_q}
\frac12\|\mu_q^F-\beta_q\|_1.
\tag{1.6}
\]

The half-energy collision excess is

\[
Q_q(F)
=
\sum_S\binom{\mu_q^F(S)}2
-
\min_{\substack{\nu\in\mathbb Z_{\ge0}^{N_q}\\\sum\nu=W}}
\sum_S\binom{\nu(S)}2.
\tag{1.7}
\]

It obeys

\[
O_q(F)\le Q_q(F).
\tag{1.8}
\]

For balanced quotas through the whole window, form the survival-packet
hypergraph on vertex set \(F\): if

\[
\mathcal O_{q,S}(F)
=
\{E\in F:S\text{ is a length-}(m-q)\text{ interval of }E\},
\tag{1.9}
\]

then every

\[
P\subseteq\mathcal O_{q,S}(F),
\qquad
|P|=\beta_q(S)+1
\tag{1.10}
\]

is a packet. Let

\[
\vartheta(F,\beta)
=
\min\left\{
\sum_{E\in F}x_E:
x_E\ge0,\ 
\sum_{E\in P}x_E\ge1
\text{ for every packet }P
\right\},
\tag{1.11}
\]

and minimize over all common balanced quota systems:

\[
\Theta_A(F)=\min_\beta\vartheta(F,\beta).
\tag{1.12}
\]

The audited Packet-Hall theorem shows that

\[
\boxed{
\Theta_A(F)=o_A(B/\sqrt m)
}
\tag{1.13}
\]

for one exact factor \(F\) implies fixed-window weighted overload \(o(W)\).
Indeed, packet rank is \(O_A(1)\), so threshold rounding produces a
quota-safe deletion family of size \(o_A(B/\sqrt m)\). Equivalently, the
direct charge gives

\[
\sum_{q=1}^{K_A}\frac{O_q(F)}{c_q}
\le 3nK_A\Theta_A(F)
=o(W).
\tag{1.14}
\]

The already-audited wreath word then has length

\[
W+O(K_AW/m)
+2\sum_{q=1}^{K_A}\frac{O_q(F)}{c_q}
=W+o(W)
\tag{1.15}
\]

for the fixed central window. If (1.13) is proved for every fixed \(A\),
choose the audited slow diagonal \(A=A(m)\to\infty\) with
\(K_A=o(m)\). The known outer-tail construction and parity lift then give
the constant-one theorem. Thus the every-fixed-\(A\) criterion preserves
one integral factor and literal contiguous-OR realizability. The issue is
solely whether orbit balance can prove it.

## 2. Orbit rigidity of the packet objective

For \(\sigma\in S_n\), transport a quota system by

\[
(\sigma\beta)_q(S)=\beta_q(\sigma^{-1}S).
\tag{2.1}
\]

### Theorem 2.1 (packet-objective orbit rigidity)

For every exact wreath factor \(F\) and every coordinate permutation
\(\sigma\),

\[
\boxed{\Theta_A(\sigma F)=\Theta_A(F).}
\tag{2.2}
\]

The same invariance holds for integral packet-cover cost, every \(O_q\),
every \(Q_q\), and every relabeling-invariant weighted combination of them.

### Proof

The owner sets obey

\[
\mathcal O_{q,S}(\sigma F)
=
\sigma\mathcal O_{q,\sigma^{-1}S}(F).
\tag{2.3}
\]

Thus \(E\mapsto\sigma E\) is an isomorphism from the packet hypergraph for
\((F,\beta)\) to that for \((\sigma F,\sigma\beta)\). It preserves
fractional and integral cover costs. Transport of quota systems is a
bijection on balanced systems, so minimization proves (2.2).

The load identity

\[
\mu_q^{\sigma F}(S)=\mu_q^F(\sigma^{-1}S)
\]

proves the remaining assertions. \(\square\)

In particular,

\[
\min_{\sigma\in S_n}\Theta_A(\sigma F)=\Theta_A(F).
\tag{2.4}
\]

Selection, Markov's inequality, minimax, or conditional expectation over
the original whole-factor orbit gives literally no single-factor gain.

## 3. Universal reblocking is the one-factor problem

Retain all permutation indices, including repetitions, and form

\[
\mathcal U(F)=\biguplus_{\sigma\in S_n}\sigma F.
\tag{3.1}
\]

The \(S_n\)-action on \(\Omega_m\) is transitive, with stabilizer size
\(2n\). Since \(|F|=B\), every cyclic order occurs in \(\mathcal U(F)\)
with multiplicity

\[
2nB=2W.
\]

Hence

\[
\boxed{
\mathcal U(F)=2W\,\mathbf1_{\Omega_m},
}
\tag{3.2}
\]

independently of \(F\). Under the oriented-mod-rotation convention the
coefficient is \(W\), with no change to the conclusions.

Every exact-factor decomposition \(\mathscr D\) of \(\mathcal U(F)\) has
exactly \(n!\) blocks.

### Theorem 3.1 (exact packet reblocking minimax)

Put

\[
\Theta_A^*=\min_{H\text{ exact}}\Theta_A(H).
\]

Then

\[
\boxed{
\min_{\mathscr D}
\frac1{n!}\sum_{J\in\mathscr D}\Theta_A(J)
=
\min_{\mathscr D}\max_{J\in\mathscr D}\Theta_A(J)
=
\min_{\mathscr D}\min_{J\in\mathscr D}\Theta_A(J)
=
\Theta_A^*.
}
\tag{3.3}
\]

The identical statement holds for every relabeling-invariant single-factor
objective.

### Proof

Every block of every decomposition is one literal exact factor, so each
displayed left side is at least \(\Theta_A^*\). Let \(H\) minimize
\(\Theta_A\). Equation (3.2) gives

\[
\mathcal U(F)=\mathcal U(H)
=
\biguplus_{\sigma\in S_n}\sigma H.
\tag{3.4}
\]

Every block in this decomposition has value \(\Theta_A(H)\) by Theorem
2.1, proving equality throughout. \(\square\)

### Corollary 3.2 (quantitative equivalence to FSP)

There is an exact reblocking \(\mathscr D\), with a balanced quota system
and a fractional packet cover \(x^J\) for each block, such that

\[
\sum_{J\in\mathscr D}\|x^J\|_1
=
o_A\left(\frac{n!B}{\sqrt m}\right)
\tag{3.5}
\]

if and only if one exact factor satisfies (1.13).

### Proof

If (3.5) holds, averaging over its \(n!\) blocks gives one block with
packet-cover mass \(o_A(B/\sqrt m)\). Conversely, take the full orbit of a
factor satisfying (1.13), together with its transported quotas and covers.
\(\square\)

Thus an exact support-feasible orbit reblocking theorem with the required
average loss is not an intermediate relaxation. It is quantitatively
equivalent to the missing one-factor theorem.

## 4. Symmetrized threshold rounding collapses

Let \(x\) be any fractional packet cover on \(F\), extend it by zero to
\(\Omega_m\), and transport it to every orbit factor:

\[
x^\sigma(\sigma E)=x(E).
\tag{4.1}
\]

### Theorem 4.1 (constant orbit average)

The uncolored orbit average is constant on all wreaths:

\[
\boxed{
\bar x(C)
:=
\frac1{n!}\sum_{\sigma\in S_n}x^\sigma(C)
=
\frac{2n}{n!}\|x\|_1
=
\frac{\|x\|_1}{|\Omega_m|}.
}
\tag{4.2}
\]

### Proof

For fixed \(E,C\in\Omega_m\), exactly \(2n\) permutations send \(E\) to
\(C\). Therefore

\[
\sum_\sigma x^\sigma(C)
=
\sum_{E\in F}2n\,x(E)
=2n\|x\|_1.
\]

Divide by \(n!\). \(\square\)

Any coordinate threshold applied to \(\bar x\), followed by restriction to
one factor, therefore selects either all \(B\) wreaths or none. The first
costs \(B\), far above \(o(B/\sqrt m)\); the second is packet-safe only when
there were no survival packets. If factor colors are retained, common
thresholding merely gives

\[
B_\sigma=\sigma B_0
\]

with identical deletion cost in every orbit block.

Thus the common-threshold Packet-Hall rounding theorem is powerful **inside
one selected factor**, but orbit symmetrization cannot supply its needed
small cover.

## 5. Equivariant single-copy selection is impossible

### Theorem 5.1 (no deterministic equivariant factor rounding)

For \(m\ge2\), there is no deterministic \(S_n\)-equivariant map from the
uncolored invariant multicover \(\mathcal U(F)\) to one exact wreath factor.

### Proof

The input (3.2) is fixed by every \(\sigma\in S_n\). If \(R\) were
equivariant, its output would satisfy

\[
R(\mathcal U(F))
=
R(\sigma\mathcal U(F))
=
\sigma R(\mathcal U(F))
\qquad(\sigma\in S_n).
\]

Thus the output would be an \(S_n\)-invariant subset of the transitive set
\(\Omega_m\), hence either \(\varnothing\) or \(\Omega_m\). For \(m\ge2\),
neither is an exact factor. \(\square\)

There is an analogous quota obstruction.

### Theorem 5.2 (no deterministic equivariant integer quota)

Suppose

\[
W=c_qN_q+s_q,
\qquad
0<s_q<N_q.
\]

No deterministic \(S_n\)-equivariant rule applied to the invariant orbit
barycenter can choose a balanced integer quota at depth \(q\).

### Proof

A balanced quota is

\[
\beta_q=c_q\mathbf1+\mathbf1_{\mathcal H}
\]

for a family

\[
\mathcal H\subseteq\binom{[n]}{m-q},
\qquad
|\mathcal H|=s_q.
\]

Equivariance on an invariant input would make \(\mathcal H\) invariant
under \(S_n\). The action on the rank is transitive, so
\(\mathcal H\) is empty or the whole rank, contradicting
\(0<s_q<N_q\). \(\square\)

Random symmetry breaking may select an integral orbit factor or quota, but
orbit invariance gives no guaranteed objective gain, and its expectation
returns the fractional barycenter. It does not by itself supply the mobile
regular high-cell families coupled to a good single factor.

## 6. Raw linear discrepancy cannot be the target

Let

\[
\lambda=\frac WN=c+\theta,
\qquad
0<\theta<1,
\]

and let \(\mu\in\mathbb Z_{\ge0}^N\) have total mass \(W\).

### Lemma 6.1 (exact scalar quantization floor)

\[
\boxed{
\|\mu-\lambda\mathbf1\|_1
\ge2N\theta(1-\theta),
}
\tag{6.1}
\]

\[
\boxed{
\|\mu-\lambda\mathbf1\|_2^2
\ge N\theta(1-\theta).
}
\tag{6.2}
\]

Equality holds precisely for floor/ceiling histograms.

### Proof

Write \(d_i=\mu_i-c\), let \(h=|\{i:d_i\ge1\}|\), and put

\[
D^-=\sum_i(-d_i)_+,
\qquad
D^+=\sum_i(d_i-1)_+.
\]

Since \(\sum_i d_i=N\theta\),

\[
N\theta=h+D^+-D^-.
\]

Directly separating \(d_i\le0\) from \(d_i\ge1\) gives

\[
\|\mu-\lambda\mathbf1\|_1
=
2N\theta(1-\theta)
+2(1-\theta)D^-
+2\theta D^+.
\]

This proves (6.1), with equality exactly when \(D^-=D^+=0\), namely when
every entry is \(c\) or \(c+1\).

For the squared norm, if two integer entries differ by at least two, moving
one unit from the larger to the smaller strictly decreases the sum of
squares while preserving the total. Iteration reaches, and equality forces,
a floor/ceiling vector. It has \(N\theta\) ceiling entries and
\(N(1-\theta)\) floor entries; substitution gives (6.2). \(\square\)

Choose

\[
q=x\sqrt m+O(1),
\qquad
0<x<A,
\qquad
e^{x^2}\notin\mathbb Z.
\tag{6.3}
\]

Then

\[
\lambda_q\longrightarrow e^{x^2},
\qquad
\frac{N_q}{W}\longrightarrow e^{-x^2}.
\tag{6.4}
\]

Equations (6.1)--(6.2) are therefore both \(\Theta_A(W)\). In particular:

* no integral factor can have \(o(W)\) raw \(\ell_1\) discrepancy from the
  orbit barycenter at all Gaussian depths;
* no integral factor can have \(O(B)\) raw centered squared discrepancy;
* Banaszczyk or Steinitz control around the fractional center
  \(\lambda_q\mathbf1\) cannot directly prove the desired scale.

The viable quantities are the mobile-quota overload \(O_q\) and the
collision excess \(Q_q\), which subtract the scalar quantization floor and
simultaneously choose a high-cell family. That nonlinear symmetry breaking
is exactly the single-copy step.

## 7. Exact wreath-specific shell rounding

The preceding no-go concerns zero-centered whole-factor discrepancy. Inside
one genuine two-factor ownership overlay there is a sharper, support-feasible
target.

On

\[
\mathcal H_A
=
\bigoplus_{q=1}^{K_A}\mathbb R^{N_q},
\]

use the weighted inner product

\[
\langle x,y\rangle_A
=
\sum_{q=1}^{K_A}\frac{\langle x_q,y_q\rangle}{c_q}.
\tag{7.1}
\]

Write

\[
\theta_q=\lambda_q-c_q,
\qquad
\phi_q=N_q\theta_q(1-\theta_q),
\]

and define the weighted quantization floor

\[
\mathfrak B_A
=
\sum_{q=1}^{K_A}\frac{\phi_q}{c_q}.
\tag{7.2}
\]

For an exact factor \(J\), put

\[
x_J=(\mu_q^J-\lambda_q\mathbf1)_{q\le K_A}
\]

and

\[
\begin{aligned}
\mathcal E_A(J)
&=
\|x_J\|_A^2-\mathfrak B_A\\
&=
\sum_{q=1}^{K_A}\frac1{c_q}
\sum_S
(\mu_q^J(S)-c_q)(\mu_q^J(S)-c_q-1).
\end{aligned}
\tag{7.3}
\]

Thus

\[
\boxed{
\mathcal E_A(J)
=
2\sum_{q=1}^{K_A}\frac{Q_q(J)}{c_q}
\ge0,
}
\tag{7.4}
\]

and

\[
\boxed{
\sum_{q=1}^{K_A}\frac{O_q(J)}{c_q}
\le\frac12\mathcal E_A(J).
}
\tag{7.5}
\]

### Lemma 7.1 (size of the quantization shell)

For every fixed \(A>0\),

\[
\boxed{
\mathfrak B_A
=
(\beta_A+o_A(1))W\sqrt m,
}
\tag{7.6}
\]

where

\[
\beta_A
=
\int_0^A
e^{-x^2}
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
     {\lfloor e^{x^2}\rfloor}
\,dx
>0.
\tag{7.7}
\]

At the finitely many points \(e^{x^2}\in\mathbb Z\), define the integrand
to be zero.

### Proof

Uniformly on the fixed window,

\[
\lambda_q=e^{q^2/m+o_A(1)},
\qquad
N_q=W e^{-q^2/m+o_A(1)}.
\tag{7.8}
\]

Away from shrinking neighborhoods of the finitely many integer thresholds
of \(e^{x^2}\), the floor and fractional-part terms are uniform, so the
sum in (7.2), divided by \(W\sqrt m\), is a Riemann sum for (7.7). The
threshold neighborhoods contribute \(o_A(1)\) after this normalization.
The integrand is positive on a nonempty subinterval of \((0,A)\), proving
\(\beta_A>0\). \(\square\)

Now let \(F,G\) be two colored exact factors. Let \(K\) run over the
connected components of their middle-ownership overlay. At every depth,
let \(u_{K,q}\) and \(v_{K,q}\) be the lower-load vectors contributed by the
\(F\)- and \(G\)-sides of \(K\), and put

\[
d_K=(u_{K,q}-v_{K,q})_{q\le K_A}\in\mathcal H_A.
\tag{7.9}
\]

Choosing one complete side of every component, with sign
\(\varepsilon_K\), gives one exact factor \(J_\varepsilon\); the opposite
choices give a complementary exact factor \(J_{-\varepsilon}\). Define

\[
a=\frac{x_F+x_G}{2},
\qquad
D_\varepsilon=\sum_K\varepsilon_Kd_K.
\tag{7.10}
\]

### Theorem 7.2 (exact two-color shell formula)

For every component signing,

\[
\boxed{
\mathcal E_A(J_{\pm\varepsilon})
=
\|a\|_A^2-\mathfrak B_A
+
\frac14\|D_\varepsilon\|_A^2
\pm
\langle a,D_\varepsilon\rangle_A.
}
\tag{7.11}
\]

Consequently,

\[
\boxed{
\min_\varepsilon\min_{\pm}\mathcal E_A(J_{\pm\varepsilon})
=
\|a\|_A^2-\mathfrak B_A
+
\min_\varepsilon
\left[
\frac14\|D_\varepsilon\|_A^2
-
|\langle a,D_\varepsilon\rangle_A|
\right],
}
\tag{7.12}
\]

and

\[
\boxed{
\min_\varepsilon\max_{\pm}\mathcal E_A(J_{\pm\varepsilon})
=
\|a\|_A^2-\mathfrak B_A
+
\min_\varepsilon
\left[
\frac14\|D_\varepsilon\|_A^2
+
|\langle a,D_\varepsilon\rangle_A|
\right].
}
\tag{7.13}
\]

### Proof

The ownership-component theorem gives

\[
x_{J_{\pm\varepsilon}}
=
a\pm\frac12D_\varepsilon.
\tag{7.14}
\]

Expand the two squared norms and subtract \(\mathfrak B_A\). Choosing the
better or worse complementary child replaces the cross term by its negative
or positive absolute value, proving all three identities. \(\square\)

The formula shows that zero discrepancy is the wrong target: a good
integer factor lies close to the quantization shell of squared radius
\(\mathfrak B_A\).

### Theorem 7.3 (collinear-component constant-one special case)

Fix \(A>0\). Suppose \(G=\sigma F\) is a coordinate relabeling of \(F\) and
the genuine ownership components satisfy:

1. the midpoint is shell-balanced,
   \[
   \|a\|_A^2=\mathfrak B_A+o_A(W);
   \tag{7.15}
   \]
2. all nonzero multidepth effects \(d_K\) are collinear in
   \(\mathcal H_A\);
3. if \(s_K\) is the number of wreaths on either side of component \(K\),
   then
   \[
   s_*:=\max_{d_K\ne0}s_K
   =o_A\left(\frac{\sqrt W}{m}\right).
   \tag{7.16}
   \]

   If every \(d_K=0\), define \(s_*=0\).

Then one common component signing makes **both** complementary children
literal exact factors satisfying

\[
\boxed{
\max\{
\mathcal E_A(J_{\varepsilon}),
\mathcal E_A(J_{-\varepsilon})
\}
=o_A(W).
}
\tag{7.17}
\]

Hence both have weighted fixed-window overload \(o(W)\).

If these hypotheses hold for every fixed \(A\), the audited
diagonalization, literal wreath word, outer tails, and parity lift prove

\[
\nu(k)\le(1+o(1))
\binom{k}{\lfloor k/2\rfloor}.
\tag{7.18}
\]

### Proof

For collinear vectors, absorb each vector's direction into its sign and
greedily sign their scalar magnitudes opposite to the current partial sum.
This gives

\[
\|D_\varepsilon\|_A
\le
\delta:=\max_K\|d_K\|_A.
\tag{7.19}
\]

At one depth,

\[
\|d_{K,q}\|_1\le2ns_K,
\qquad
\|d_{K,q}\|_\infty\le s_K,
\]

and therefore

\[
\|d_{K,q}\|_2^2\le2ns_K^2.
\]

Since \(c_q\ge1\),

\[
\delta
\le\sqrt{2nK_A}\,s_*
=O_A(s_*m^{3/4}).
\tag{7.20}
\]

Condition (7.16) implies

\[
\delta^2=o_A(W).
\tag{7.21}
\]

By (7.6) and (7.15),

\[
\|a\|_A=O_A(\sqrt W\,m^{1/4}),
\]

so

\[
\|a\|_A\delta
=O_A(s_*\sqrt W\,m)
=o_A(W).
\tag{7.22}
\]

Insert (7.15), (7.19), (7.21), and (7.22) into the max formula (7.13).
Both children obey (7.17). Equation (7.5) gives weighted overload \(o(W)\).
The last assertion is exactly the quantitative composition recorded in
(1.14)--(1.15), applied for every fixed \(A\). \(\square\)

This theorem is restricted but unconditional: once its three displayed
structural hypotheses hold, no fractional factor, separate depthwise
choice, or nonliteral block remains.

### Corollary 7.4 (thin-shell accuracy obstruction)

Consider the formal perfectly balanced midpoint \(a=0\). It need not be the
midpoint of an actual two-factor pair when \(2\lambda_q\) is nonintegral.
For every exact child represented by such a formal signing,

\[
\boxed{
\|D_\varepsilon\|_A^2\ge4\mathfrak B_A.
}
\tag{7.23}
\]

Moreover,

\[
\boxed{
\mathcal E_A(J_\varepsilon)=o(W)
\iff
\|D_\varepsilon\|_A^2
=4\mathfrak B_A+o(W).
}
\tag{7.24}
\]

Thus, for \(\eta_m\ge0\), a norm-only guarantee

\[
\|D_\varepsilon\|_A^2
\le(4+\eta_m)\mathfrak B_A
\tag{7.25}
\]

implies \(o(W)\) shell error only at the rate

\[
\boxed{\eta_m=o(m^{-1/2}).}
\tag{7.26}
\]

An unspecified \(4+o(1)\) Steinitz/Banaszczyk bound is therefore
quantitatively insufficient for the constant-one implication.

### Proof

At \(a=0\), (7.11) becomes

\[
\mathcal E_A(J_\varepsilon)
=
\frac14\|D_\varepsilon\|_A^2-\mathfrak B_A.
\]

Nonnegativity of \(\mathcal E_A\) proves (7.23), and the same equality proves
(7.24). By (7.6), the excess allowed by (7.25) is at most

\[
\frac{\eta_m}{4}\mathfrak B_A
=\Theta_A(\eta_mW\sqrt m).
\]

This upper bound is \(o(W)\) exactly at the inference rate (7.26).
\(\square\)

The rate statement concerns what the coarse norm bound (7.25) alone can
imply in the formal \(a=0\) normalization. At a nonzero genuine midpoint,
the cross term in (7.11) may help; Corollary 7.4 is not a universal lower
bound for every wreath-specific mechanism.

## 8. A transitive bounded-rank countermodel

We now give an exact counterexample to every black-box theorem based only
on orbit balance, transitivity, equal atom degrees, exact one-cover
constraints, connected two-factor overlays, and bounded packet rank.

Fix any odd integer \(n\ge5\). Let

\[
V=\mathbb F_2^n.
\tag{8.1}
\]

The atoms are the vertices \(v\in V\). The middle targets are the edges of
the hypercube \(Q_n\). An atom owns its \(n\) incident middle edges.

Put

\[
B=2^{n-1},
\qquad
W=nB.
\tag{8.2}
\]

An exact factor is a vertex set containing exactly one endpoint of every
hypercube edge.

### Lemma 8.1 (the exact factor fibre is one segment)

The only integral exact factors are the two parity classes

\[
F_0=\{v:|v|\equiv0\pmod2\},
\qquad
F_1=\{v:|v|\equiv1\pmod2\}.
\tag{8.3}
\]

More generally, the fractional exact-factor polytope is

\[
x_v=t\quad(v\in F_0),
\qquad
x_v=1-t\quad(v\in F_1),
\qquad
0\le t\le1.
\tag{8.4}
\]

### Proof

The exact-cover equation on every edge \(uv\) is

\[
x_u+x_v=1.
\tag{8.5}
\]

The cube is connected and bipartite. Propagating (8.5) from one vertex
gives (8.4). Its zero-one endpoints are precisely (8.3). \(\square\)

For \(j\in\mathbb Z_n\), indices taken cyclically, define the even
two-dimensional subspace

\[
U_j
=
\operatorname{span}_{\mathbb F_2}
\{e_j+e_{j+1},\,e_{j+1}+e_{j+2}\}.
\tag{8.6}
\]

A lower target is a labelled affine coset

\[
(j,v+U_j).
\tag{8.7}
\]

Each atom lies in one such coset for every \(j\), so every atom owns exactly
\(n\) lower targets. There are

\[
N=n\,2^{n-2}=\frac W2
\tag{8.8}
\]

lower targets, and the balanced average load is

\[
\lambda=\frac WN=2.
\tag{8.9}
\]

Every \(U_j\)-coset has four vertices of one parity because \(U_j\) consists
entirely of even vectors.

### Theorem 8.2 (linear single-copy gap)

For the unique balanced quota \(\beta\equiv2\),

\[
\boxed{
O(F_0)=O(F_1)=\frac W2,
}
\tag{8.10}
\]

\[
\boxed{
Q(F_0)=Q(F_1)=W.
}
\tag{8.11}
\]

Yet the average of \(F_0,F_1\) has constant lower load \(2\) and zero
aggregate defect.

### Proof

In \(F_0\), every even labelled coset has load four and every odd coset has
load zero. There are \(W/4\) cosets of each parity. Hence

\[
\frac12\|\mu^{F_0}-2\mathbf1\|_1
=
\frac12\left(\frac W2\cdot2\right)
=\frac W2.
\]

The calculation for \(F_1\) is complementary.

For collision excess,

\[
\sum_S\binom{\mu^{F_0}(S)}2
=
\frac W4\binom42
=\frac{3W}{2},
\]

whereas the balanced floor is

\[
\frac W2\binom22=\frac W2.
\]

Their difference is \(W\). Averaging the complementary histograms gives
the constant vector two. \(\square\)

### Theorem 8.3 (exact fractional packet obstruction)

At quota \(\beta\equiv2\), the survival-packet rank is three and

\[
\boxed{
\vartheta(F_0,\beta)
=
\vartheta(F_1,\beta)
=
\frac B3.
}
\tag{8.12}
\]

### Proof

In \(F_0\), each active owner set is one even \(U_j\)-coset and has four
vertices. Its survival packets are its four three-subsets. The uniform
assignment

\[
x_v=\frac13\qquad(v\in F_0)
\]

covers every packet, so \(\vartheta\le B/3\).

Conversely, fix one \(j\). Its \(B/4\) even cosets partition \(F_0\). On one
coset \(C\), summing its four packet inequalities gives

\[
3\sum_{v\in C}x_v\ge4,
\qquad
\sum_{v\in C}x_v\ge\frac43.
\]

Summing over the fixed-\(j\) partition gives

\[
\sum_{v\in F_0}x_v
\ge
\frac B4\cdot\frac43
=\frac B3.
\]

Thus equality holds. The proof for \(F_1\) is identical. \(\square\)

Translations of \(\mathbb F_2^n\), together with cyclic coordinate
rotation, act transitively on:

* atoms;
* middle hypercube edges;
* labelled lower cosets.

Odd translations interchange \(F_0,F_1\). Thus the full factor orbit
consists of the two exact factors and is exactly lower-balanced. Their
colored ownership overlay is the connected graph \(Q_n\), so the legal
two-factor component cube has one bit and produces only the two endpoints.

The formal Catalan size is \(B=W/n\). The required packet scale analogous
to (1.13) is \(o(B/\sqrt n)\), while (8.12) is \(B/3\). The gap is a factor
\(\Theta(\sqrt n)\).

## 9. Definitive scope of the no-go

The countermodel satisfies all of the following properties used by generic
orbit and discrepancy arguments:

1. binary atom-target incidence;
2. exact right-hand-side-one factor blocks;
3. factor size \(B=W/n\);
4. equal atom degree \(n\) in both middle and lower systems;
5. transitivity on atoms, middle targets, and lower targets;
6. an exactly balanced complete factor orbit;
7. a connected ownership overlay;
8. constant balanced lower capacity;
9. packet rank three;
10. an exact bounded-rank fractional-to-integral Packet-Hall theorem.

Nevertheless every exact factor has linear overload and fractional packet
cost \(\Theta(B)\). Therefore no theorem using only these ten properties can
prove the single-copy bound needed for constant one.

This rules out, as black-box mechanisms:

* selection or averaging of whole orbit factors;
* Steinitz ordering of whole-factor vectors;
* Banaszczyk signing without a support-feasible cyclic trade theorem;
* equivariant deterministic rounding of the orbit barycenter;
* symmetrize-then-threshold packet rounding;
* bounded-rank Packet Hall applied only after orbit averaging;
* connected-component signing when the overlay is connected.

It does **not** rule out a theorem using the special fact that a wreath atom
is a cyclic order and every lower flag consists of nested cyclic intervals.
That is the only remaining escape in this lane. Concretely, such a theorem
would have to prove that actual cyclic-wreath ownership overlays cannot
exhibit the connected rigid behaviour of the cube model at positive
factor-scale energy, or would have to construct larger support-feasible
multifactor circuits with signed lower effects and controlled positivity.

Either assertion is already a new wreath-specific structural theorem. It
cannot be inferred from orbit balance, transitivity, discrepancy, or packet
rounding. Thus the generic orbit-to-single-copy discrepancy lane is closed.

## 10. Adversarial audit

1. **Not a conjecture counterexample.** Section 8 is an abstract exact-cover
   system, not a family of cyclic wreath intervals. It falsifies a generic
   rounding principle, not MWB.

2. **One exact factor is preserved.** Every factor in Sections 1--7 is a
   literal exact wreath factor. The Section 8 countermodel likewise uses
   literal right-hand-side-one exact covers, not fractional blocks.

3. **Permutation indices are retained.** The universal multicover uses all
   \(n!\) coordinate permutations with multiplicity. The set of distinct
   orbit factors is not silently substituted.

4. **Uncolored versus colored scope.** Equation (3.2) permits reassignment
   of identical wreath copies among factor colors. If source colors must be
   preserved, only support-feasible colored trades are allowed; orbit
   equality alone does not construct them.

5. **No raw-norm confusion.** The quantization floor in Section 6 applies
   to raw discrepancy from the fractional barycenter. The meaningful
   overload and collision excess subtract or optimize over that floor.

6. **Packet rank does not solve selection.** Bounded packet rank rounds a
   cover already present inside one factor. Theorem 8.3 proves that its
   fractional input can remain factor-scale despite perfect orbit balance.

7. **Connected overlay conclusion.** In the cube model, exact supported
   factors are the two bipartition sides because the overlay is connected.
   This is the exact analogue of the two-factor ownership-component theorem.

8. **Literal OR implication is conditional only.** Equations
   (1.13)--(1.15) record the audited quantitative composition into a literal
   \(W+o(W)\) word. The present report proves that generic orbit rounding
   does not supply (1.13); it does not claim a new OR construction.

9. **Labelled synchronization is not used.** The packet and overload route
   is unlabelled. No small histogram distance is promoted to a common nested
   owner flow.

10. **Closure claim.** “Lane closed” means the generic mechanism specified
    above is refuted. A cyclic-wreath-specific positive trade theorem remains
    logically possible, but it is additional structural content rather than
    a consequence of exactly balanced orbit marginals.

The stable theorem-level conclusion is:

\[
\boxed{
\begin{array}{c}
\text{the ten generic properties in Section 9 do not force exact orbit}\\
\text{balance to round to one good factor by discrepancy or Packet Hall.}
\end{array}
}
\]

The single-copy obstruction is the cyclic exact-factor fibre itself.
