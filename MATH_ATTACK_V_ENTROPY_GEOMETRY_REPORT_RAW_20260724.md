Outcome: the lane does not yet prove the contiguous-OR conjecture, but it yields an exact entropy–geometry characterization, an actual \(o(W)\) construction theorem allowing \(\Theta(W)\) holes, and a matching dual obstruction. The sole remaining issue is now an explicit, unproved geometric property of hole families of one exact factor.

All logarithms below are natural.

## 1. Exact entropy–congestion theorem

Fix \(A>0\), \(K=\lceil A\sqrt m\rceil<m\), one exact factor \(F\), and its restricted lower-hole family

\[
\mathcal H=\bigsqcup_{q=1}^{K}\mathcal H_q,\qquad
\mathcal H_q=\left\{S\in\binom{[n]}{m-q}:\mu_q^F(S)=0\right\},
\qquad M=|\mathcal H|.
\]

Use proper opposite signed faces

\[
C(P,N)=
\{P\cup T:T\subseteq U\}\cup
\{N\cup T:T\subseteq U\},
\]

where \(P\cap N=\varnothing\), \(P\cup N\ne\varnothing\), and
\(U=[n]\setminus(P\cup N)\). Their literal cost is

\[
\gamma_C=2\nu(|U|)
+\mathbf 1_{P\ne\varnothing}
+\mathbf 1_{N\ne\varnothing}.
\]

Let \(A_{S,C}=\mathbf 1_{S\in C}\), and define the restricted functional

\[
\Psi_{\le K}
=
\inf_{\lambda\ge0}
\left[
\sum_C\gamma_C\lambda_C+
2\sum_{S\in\mathcal H}e^{-(A\lambda)_S}
\right].
\]

For a probability distribution \(\pi\) on \(\mathcal H\), write

\[
\operatorname{Ent}(\pi)=-\sum_S\pi_S\log\pi_S
\]

and

\[
\delta(\pi)=
\max\left\{
\frac{\|\pi\|_\infty}{2},
\max_C\frac{\pi(C)}{\gamma_C}
\right\}.
\]

Then, if \(M>0\),

\[
\boxed{
\Psi_{\le K}
=
\max_{\pi\in\mathcal P(\mathcal H)}
\frac{
1+\operatorname{Ent}(\pi)+\log(2\delta(\pi))
}{
\delta(\pi)
}.
}
\tag{1}
\]

If \(M=0\), \(\Psi_{\le K}=0\).

Proof. The audited Fenchel dual is

\[
\Psi_{\le K}
=
\max_{\substack{0\le y\le2\\A^Ty\le\gamma}}
\sum_S y_S\left(1+\log\frac2{y_S}\right).
\]

For nonzero \(y\), put \(t=\sum_Sy_S\) and \(\pi=y/t\). Feasibility is exactly

\[
0<t\le\frac1{\delta(\pi)}.
\]

The objective becomes

\[
t\left(1+\operatorname{Ent}(\pi)+\log\frac2t\right).
\]

Its derivative is

\[
\operatorname{Ent}(\pi)+\log\frac2t.
\]

Since \(t\le2/\|\pi\|_\infty\) and
\(\operatorname{Ent}(\pi)\ge-\log\|\pi\|_\infty\), this derivative is nonnegative throughout the feasible interval. Hence the optimum occurs at \(t=1/\delta(\pi)\), proving (1). ∎

Thus the exact obstruction is a high-entropy distribution on holes whose mass remains diffuse in every opposite trace-pair cylinder.

## 2. Fractional and deterministic repair

Let

\[
D_{\mathrm{frac}}
=
\min_{\substack{x_C,z_S\ge0\\Ax+z\ge\mathbf1}}
\left(
\sum_C\gamma_Cx_C+2\sum_Sz_S
\right)
\]

and let \(D_{\mathrm{det}}\) be the minimum cost of actual signed-face blocks followed by literal repair of every uncovered lower/complementary-upper pair.

Then

\[
\boxed{
D_{\mathrm{frac}}
=
\max_\pi\frac1{\delta(\pi)}
=
\frac1{\min_\pi\delta(\pi)}
}
\tag{2}
\]

and

\[
\boxed{
D_{\mathrm{frac}}
\le D_{\mathrm{det}}
\le\Psi_{\le K}
\le
D_{\mathrm{frac}}
\left(1+\log\frac{2M}{D_{\mathrm{frac}}}\right).
}
\tag{3}
\]

The middle inequality is constructive: select face \(C\) independently with probability \(1-e^{-\lambda_C}\), then append every uncovered hole and its complement. The expected cost is at most the Poisson objective, so some deterministic selection attains it.

Consequently,

\[
D_{\mathrm{frac}}
\left(1+\log\frac{2M}{D_{\mathrm{frac}}}\right)=o(W)
\]

is already an actual literal construction criterion. It does not require \(M=o(W)\).

The empty-anchor full-cube column \(C(\varnothing,\varnothing)\), whose cost is \(2\nu(n)\), was excluded to prevent circularity. This loses nothing at the \(o(W)\) scale: its cost is at least \(2W\), so its intensity in any \(o(W)\) certificate is \(o(1)\); deleting it changes the residual term by only an \(e^{o(1)}\) factor.

## 3. Dense-residual peeling: proved construction and obstruction

For nonempty \(\mathcal G\subseteq\mathcal H\), define

\[
\rho(\mathcal G)
=
\max\left\{
\frac12,
\max_C\frac{|\mathcal G\cap C|}{\gamma_C}
\right\},
\qquad
f(r)=\frac{1+\log(2r)}r.
\]

The \(1/2\) is attained by the zero-dimensional literal column
\(\{S,S^c\}\).

Uniform \(\pi\) on \(\mathcal G\) in (1) gives the exact lower certificates

\[
\boxed{
D_{\mathrm{frac}}\ge\frac{|\mathcal G|}{\rho(\mathcal G)},
\qquad
\Psi_{\le K}\ge|\mathcal G|f(\rho(\mathcal G)).
}
\tag{4}
\]

Conversely, suppose \(R\ge1/2\) and \(u\ge0\) satisfy

\[
\boxed{
|\mathcal G|>u
\Longrightarrow
\rho(\mathcal G)\ge R
\quad
\text{for every }\mathcal G\subseteq\mathcal H.
}
\tag{5}
\]

Then

\[
\boxed{
D_{\mathrm{det}}\le2u+\frac MR,
\qquad
\Psi_{\le K}\le2u+M\frac{1+\log(2R)}R.
}
\tag{6}
\]

Proof. Repeatedly choose a face \(C_i\) meeting the current residual in

\[
b_i\ge R\gamma_i
\]

holes, and delete those holes. Stop with at most \(u\) holes.

Selecting every \(C_i\) once costs at most

\[
\sum_i\gamma_i\le\frac1R\sum_i b_i\le\frac MR,
\]

which proves the deterministic bound.

For the Poisson bound, put \(r_i=b_i/\gamma_i\) and assign intensity
\(\lambda_i=\log(2r_i)\). The block and assigned-residual charge is

\[
\gamma_i\lambda_i+2b_ie^{-\lambda_i}
=b_i f(r_i).
\]

Since

\[
f'(r)=-\frac{\log(2r)}{r^2}\le0
\quad(r\ge1/2),
\]

this is at most \(b_if(R)\). Summation and literal repair of the final residual prove (6). ∎

This has a matching alternative: if peeling stalls at a residual \(\mathcal G\) with \(\rho(\mathcal G)<R\), then \(y_S=1/R\) on \(\mathcal G\) is a feasible explicit entropy-dual certificate.

In particular, if \(M=O(W)\), the following are equivalent:

\[
\Psi_{\le K}=o(W),
\qquad
D_{\mathrm{frac}}=o(W),
\qquad
D_{\mathrm{det}}=o(W),
\tag{7}
\]

and

\[
\boxed{
\text{for every fixed }\varepsilon>0,\quad
\inf_{\substack{\mathcal G\subseteq\mathcal H\\
|\mathcal G|\ge\varepsilon W}}
\rho(\mathcal G)\longrightarrow\infty.
}
\tag{8}
\]

Thus, in the \(M=O(W)\) regime, the needed geometry is characterized exactly: every linear-sized residual family must contain an increasingly economical signed face. A single dense face for the original family is not enough; density must persist after arbitrary earlier dense clusters have been removed.

## 4. What geometry is forced

If a face has free dimension \(s\ge1\), then at every fixed depth

\[
\left|C(P,N)\cap\binom{[n]}{m-q}\right|
\le
2\binom{s}{\lfloor s/2\rfloor}
\le\gamma_C.
\tag{9}
\]

Therefore a density-\(R\) face must meet holes on at least
\(\lceil R\rceil\) distinct depths. The required compression is genuinely cross-depth.

Also,

\[
|C(P,N)|\le2^{s+1}
\]

and

\[
\gamma_C
\ge
2\binom{s}{\lfloor s/2\rfloor}
\ge
\frac{2^{s+1}}{\sqrt{2(s+1)}}.
\]

Hence

\[
\boxed{
\frac{|\mathcal G\cap C|}{\gamma_C}
\le\sqrt{2(s+1)}.
}
\tag{10}
\]

A density-\(R\) repair block must therefore have

\[
\boxed{s\ge R^2/2-1.}
\tag{11}
\]

Bounded-dimensional subcubes can never supply the required asymptotic compression.

More generally, for any subset \(Q\) of depths, put

\[
M_Q=\sum_{q\in Q}M_q,
\qquad
L_Q=\min\{|Q|,\sqrt{2n}\}.
\]

Then

\[
\boxed{
D_{\mathrm{frac}}\ge\frac{M_Q}{L_Q},
\qquad
\Psi_{\le K}\ge
\frac{1+\log(2L_Q)}{L_Q}M_Q.
}
\tag{12}
\]

This strengthens the earlier whole-window and one-rank bounds to every intermediate rank subset. Consequently,

\[
\Psi_{\le K}=o(W)
\Longrightarrow
M_Q=o\left(
\frac{WL_Q}{1+\log(2L_Q)}
\right)
\]

uniformly over choices of \(Q\). For \(K=\lceil A\sqrt m\rceil\), this recovers

\[
\sum_{q\le K}M_q
=o\left(\frac{W\sqrt m}{\log m}\right),
\]

but it does not require \(\sum_qM_q=o(W)\).

## 5. Nonsummable defects really can be compressed

The distinction is genuine, not merely formal.

Choose an even

\[
d=\tfrac12\log_2 n+O(1),
\]

split a \(d\)-set \(D=P\sqcup N\) equally, and put \(s=n-d\). Let

\[
\mathcal G=
C(P,N)\cap
\bigsqcup_{q=1}^{\lceil A\sqrt m\rceil}
\binom{[n]}{m-q}.
\]

Gaussian central-binomial estimates give

\[
|\mathcal G|=\Theta_A(W),
\qquad
|\mathcal G\cap\mathcal H_q|
=\Theta_A(W/\sqrt n)
\]

at each depth. Using the standard bound
\(\nu(s)=O(\binom{s}{\lfloor s/2\rfloor})\),

\[
\gamma_C=\Theta(W/\sqrt n),
\qquad
\rho(\mathcal G)=\Theta_A(\sqrt n).
\]

One face with intensity \(\log(2|\mathcal G|/\gamma_C)\) gives

\[
\Psi_{\le K}
=
\Theta_A\left(\frac{W\log n}{\sqrt n}\right)
=o(W).
\]

A single deterministic copy costs only \(\Theta(W/\sqrt n)\).

Thus \(\Theta(W)\) aggregate holes, with \(o(W)\) holes at every individual rank, can be repaired in \(o(W)\) by genuine cross-depth face reuse. This example is order-sharp for the Poisson obstruction.

It is only an abstract set family. It is not proved realizable as the holes of an exact wreath factor.

## 6. Exact unproved factor-geometric lemma

A clean sufficient target is now:

> **UNPROVED \(\mathrm{FG}_A\).** For every fixed \(A>0\), there exist exact factors \(F_m\), a constant \(C_A\), and \(R_m\to\infty\) such that
> \[
> M_{\le K}(F_m)\le C_AW,
> \qquad K=\lceil A\sqrt m\rceil,
> \]
> and every
> \[
> \mathcal G\subseteq\mathcal H_{\le K}(F_m),
> \qquad |\mathcal G|\ge W/R_m,
> \]
> contains a proper opposite face \(C\) satisfying
> \[
> |\mathcal G\cap C|\ge R_m\gamma_C.
> \]

The proved peeling theorem would then give

\[
\frac{\Psi_{\le K}}W
\le
\frac2{R_m}
+
C_A\frac{1+\log(2R_m)}{R_m}
+o(1)
\longrightarrow0.
\]

No known exact-factor family currently satisfies \(\mathrm{FG}_A\), even in a weaker quantitatively sufficient form.

If \(\mathrm{FG}_A\) were proved for every fixed \(A\), slow diagonalization would yield a literal signed-face repair of one exact factor on a growing Gaussian window. Together with the audited seams and outer tails, this would directly give coefficient one.

It would not prove MWB, balanced multiplicities, or common-owner synchronization. This lane sees only binary holes. Conversely, failure of the entropy–congestion criterion obstructs this signed-face architecture, not arbitrary contiguous-OR words.

The decisive entropy reparametrization, peeling estimate, zero-dimensional endpoint, full-face circularity removal, and implication scope were all independently rederived and audited. No shared files were modified.
