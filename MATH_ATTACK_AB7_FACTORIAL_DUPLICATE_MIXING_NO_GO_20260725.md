# Master-redirect AB: factorial collision, duplicate separation, and the exact same-cell obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver,
computer algebra, or numerical experiment is used. Every factor and every
component child used in the decisive no-go is a literal integral exact middle
wreath factor.

---

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
B=\operatorname{Cat}_m=\frac Wn,\qquad
H=\lceil A\sqrt m\rceil ,
\]

where \(A>0\) is fixed. At depth \(q\), let

\[
N_q=\binom n{m-q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,\qquad
b_q=\binom{c_q+1}{2}.
\]

For an exact factor \(F\), write \(\Phi_q(F)\) for its undoubled balanced
pair/factorial collision excess and put

\[
\mathfrak F_A(F)
=\sum_{q=1}^{H}\frac{\Phi_q(F)}{b_q}.
\tag{0.1}
\]

This report proves three exact theorems.

1. **Aggregate duplicate--mixing ledger.** Summed over all coordinate
   transpositions, separated same-target duplicates, opposite-target mixing,
   within-component residue, Johnson degree, the integer balancing floor, and
   \(\mathfrak F_A\) satisfy one exact identity. It gives the sharp
   coefficient-one implication

   \[
   X_A^{\rm fac}
   \le(2-\eta)(n-1)\mathfrak F_A
      +C(n-1)HB
   \Longrightarrow
   \max_\tau\mathbb E\operatorname{gain}_\tau
   \ge\frac{\eta}{n}\mathfrak F_A-\frac{CHB}{n}.
   \tag{0.2}
   \]

   Thus the displayed \(X_A^{\rm fac}\)-bound, if proved at a global
   minimizer, would give

   \[
   \mathfrak F_A=O_A(HB)=O_A(W/\sqrt m)=o(W),
   \]

   and hence the fixed-window factorial criterion needed for coefficient one.
   Implication (0.2) is proved; its hypothesis is not.

2. **Explicit fragmentation obstruction.** If every wreath owner is artificially
   separated into a singleton counting block, the total duplicate-minus-mixing
   gap is

   \[
   \frac12\sum_{\{S,T\}\in E(J(n,m-q))}
   (\mu_q(S)-\mu_q(T))^2
   -\left(\frac{(m-q)(m+q+1)}2-1\right)W.
   \tag{0.3}
   \]

   Whenever \(\Phi_q=o(W)\), this is at most

   \[
   D_q^{\rm sing}
   \le-(\sqrt2-1-o_A(1))(m-q)(m+q+1)W.
   \tag{0.4}
   \]

   A genuine component partition can escape this negative baseline only by
   co-locating a correspondingly large excess of opposite-target pairs over
   same-target duplicates. Unsigned fragmentation is therefore quantitatively
   hostile, not merely inconclusive.

3. **Exact same-cell no-go.** For every sufficiently large \(m\), the full
   intrinsic \(\tau=(2\,3)\) component cell of the canonical MSW factor
   contains an exact factor \(G_m\) such that

   \[
   \boxed{
   \max_I\bigl(
   \mathfrak F_A(G_m)-\mathfrak F_A(G_m^I)
   \bigr)=0,
   }
   \tag{0.5}
   \]

   although

   \[
   \boxed{
   \frac{\mathfrak F_A(G_m)}W
   \ge
   \frac{4^H}{2048K_A\,nH^4}-1
   \longrightarrow\infty ,
   }
   \tag{0.6}
   \]

   where

   \[
   K_A=
   \binom{\left\lceil
   e^{\,2(A+1)(A+2)}
   \right\rceil+1}{2}.
   \tag{0.7}
   \]

   In fact \(\mathfrak F_A(G_m)/(nW)\to\infty\). Equation (0.5) ranges over
   every correlated cut of the genuine ownership components, not only fair or
   balanced-half signs.

The third theorem definitively refutes every prescribed-bridge or
same-overlay claim that high balanced factorial collision forces a productive
duplicate-separation cut with inverse-polynomial capture and polynomial
residue. Conjugation gives the same obstruction for every transposition fixed
in advance.

It does **not** refute a selector with quantifiers

\[
\forall F\ \exists\tau,
\]

nor adaptive recomputation under genuinely new transpositions. Those are the
only overlay directions left by this lane. No conclusion against the
contiguous-OR conjecture itself is claimed.

---

## 1. Exact factorial objective

Let \(F\) be an exact middle wreath factor. Its depth-\(q\) load is

\[
\mu_q^F(S)
=
\#\{C\in F:S\text{ is a cyclic }(m-q)\text{-interval of }C\}.
\tag{1.1}
\]

Every exact factor has \(B=W/n\) rows and every row contributes \(n\)
intervals at each rank, so

\[
\sum_S\mu_q^F(S)=W.
\tag{1.2}
\]

Write

\[
W=c_qN_q+\rho_q,\qquad 0\le\rho_q<N_q.
\tag{1.3}
\]

The minimum second factorial moment among all nonnegative integral load
vectors of mass \(W\) is

\[
P_q^{\min}
=(N_q-\rho_q)\binom{c_q}{2}
+\rho_q\binom{c_q+1}{2}.
\tag{1.4}
\]

Define

\[
\Phi_q(F)
=\sum_S\binom{\mu_q^F(S)}2-P_q^{\min}.
\tag{1.5}
\]

Then

\[
\boxed{
2\Phi_q(F)
=
\sum_S
(\mu_q^F(S)-c_q)(\mu_q^F(S)-c_q-1)
\ge0.
}
\tag{1.6}
\]

Thus \(\Phi_q\) is the undoubled balanced pair/factorial collision excess,
and (0.1) is exactly

\[
\mathfrak F_A(F)
=\sum_{q\le H}
\frac{\Phi_q(F)}{\binom{c_q+1}{2}}.
\tag{1.7}
\]

The audited factorial-hole theorem uses precisely this normalization. On a
fixed Gaussian window, \(c_q=O_A(1)\); hence
\(\mathfrak F_A=o(W)\) bounds balanced overload and supplies the exact-factor
input to the established literal reservoir/tail transfer. No fractional or
labelled synchronization assertion is used here.

---

## 2. Exact component-cut duplicate/mixing identity

Fix a coordinate transposition \(\tau\). Let \(K\) range over the connected
ownership components of \(F\) versus \(\tau F\). Every component has old side
\(K\), new side \(\tau K\), and a common \(\tau\)-invariant middle-root
union. Hence independently choosing either complete side of every component
produces an integral exact factor.

For an unordered moved target pair

\[
p=\{S,T=\tau S\},
\]

orient \(p\) once and put

\[
x_K=x_K(S),\qquad y_K=x_K(T),\qquad d_K=x_K-y_K.
\tag{2.1}
\]

For a component cut \(I\), write

\[
x_I=\sum_{K\in I}x_K,\quad
y_I=\sum_{K\in I}y_K,\quad
u_p=x_I-y_I,
\tag{2.2}
\]

and define \(x_{\bar I},y_{\bar I},v_p\) analogously on the complementary
components.

### Theorem 2.1 (literal duplicate separation minus opposite mixing)

If \(F^I\) is obtained by switching precisely the components in \(I\), then

\[
\boxed{
\Phi_q(F)-\Phi_q(F^I)
=\sum_{p}u_pv_p.
}
\tag{2.3}
\]

Targetwise,

\[
\boxed{
u_pv_p
=
\underbrace{x_Ix_{\bar I}+y_Iy_{\bar I}}
_{\text{same-target duplicates separated by the cut}}
-
\underbrace{x_Iy_{\bar I}+y_Ix_{\bar I}}
_{\text{opposite-target mixing across the cut}}.
}
\tag{2.4}
\]

Consequently

\[
\boxed{
\mathfrak F_A(F)-\mathfrak F_A(F^I)
=
\sum_{q\le H}\frac1{b_q}
\sum_p
\bigl(\operatorname{Dup}_{q,p}(I)
-\operatorname{Mix}_{q,p}(I)\bigr).
}
\tag{2.5}
\]

#### Proof

On \(p\), switching \(I\) changes the two loads from

\[
(x_I+x_{\bar I},\,y_I+y_{\bar I})
\]

to

\[
(y_I+x_{\bar I},\,x_I+y_{\bar I}).
\]

The pair total is fixed. Direct expansion gives

\[
\begin{aligned}
&\binom{x_I+x_{\bar I}}2+\binom{y_I+y_{\bar I}}2\\
&\quad-
\binom{y_I+x_{\bar I}}2-\binom{x_I+y_{\bar I}}2\\
&=(x_I-y_I)(x_{\bar I}-y_{\bar I})
=u_pv_p.
\end{aligned}
\]

The balanced floor (1.4) is factor-independent and cancels. Expansion of
\(u_pv_p\) gives (2.4), and summing with the weights \(1/b_q\) proves
(2.5). \(\square\)

### 2.1 Fair residual form

Put

\[
z_p=\sum_Kd_K,
\qquad
\mathsf B_p=\binom{|z_p|}{2},
\tag{2.6}
\]

\[
\mathsf M_p
=\frac{\sum_K|d_K|-|z_p|}{2},
\qquad
\mathsf R_p
=\sum_K\binom{|d_K|}{2}.
\tag{2.7}
\]

Then

\[
\boxed{
\mathsf B_p-\mathsf M_p-\mathsf R_p
=\frac12\left(z_p^2-\sum_Kd_K^2\right).
}
\tag{2.8}
\]

Here \(\mathsf B_p\) is coherent imbalance, \(\mathsf M_p\) is exact
opposite-sign mixing, and \(\mathsf R_p\) is residual same-component
multiplicity. A uniformly random cut separates each component pair with
probability \(1/2\), so its expected normalized factorial gain is

\[
\boxed{
\mathcal D_\tau^{\rm fac}(F)
=
\sum_{q\le H}\frac1{2b_q}
\sum_p
(\mathsf B_p-\mathsf M_p-\mathsf R_p).
}
\tag{2.9}
\]

If both endpoint loads of \(p\) lie in
\(\{c_q,c_q+1\}\), then \(|z_p|\le1\), so

\[
\mathsf B_p=0,\qquad
\mathsf B_p-\mathsf M_p-\mathsf R_p\le0.
\tag{2.10}
\]

Thus floor-balanced target pairs can only hurt fair duplicate separation.
All positive coherent contribution comes from targets outside the two
balanced levels.

There is also a sharp no-amplification bound:

\[
\boxed{
\sum_p\mathsf B_p\le 2\Phi_q(F).
}
\tag{2.11}
\]

Indeed, for nonnegative integers \(x,y\), put

\[
h_c(x)=(x-c)(x-c-1).
\]

If \(a,b\) are the distances of \(x,y\) from the interval
\(\{c,c+1\}\), the largest possible \(|x-y|\) is \(a+b+1\). Therefore

\[
\binom{|x-y|}{2}
\le a(a+1)+b(b+1)
=h_c(x)+h_c(y).
\]

Summing over the disjoint \(\tau\)-pairs and using (1.6) proves (2.11).

---

## 3. The all-transposition factorial/overlay ledger

Fix one depth \(q\), put

\[
r=m-q,\qquad N=\binom nr,\qquad
\lambda=\frac WN=c+\theta,
\qquad
\beta=N\theta(1-\theta),
\tag{3.1}
\]

and write

\[
f=\mu_q^F-\lambda\mathbf1.
\tag{3.2}
\]

Exact row regularity gives

\[
\sum_Sf(S)=0,\qquad
\sum_{S\ni i}f(S)=0\quad(i\in[n]).
\tag{3.3}
\]

Hence, in the Johnson harmonic decomposition,

\[
f=\sum_{j\ge2}f^{(j)}.
\tag{3.4}
\]

Sum the quantities in (2.6)--(2.7) over every unordered coordinate
transposition and every moved unordered target pair:

\[
\mathbf B_q=\sum_{\tau,p}\mathsf B_{\tau,p},
\quad
\mathbf M_q=\sum_{\tau,p}\mathsf M_{\tau,p},
\quad
\mathbf R_q=\sum_{\tau,p}\mathsf R_{\tau,p}.
\tag{3.5}
\]

Also put

\[
\operatorname{TV}_q=\sum_{\tau,p}|z_{\tau,p}|,
\qquad
\mathbf V_q=\sum_{\tau,p,K}d_{\tau,p,K}^2,
\tag{3.6}
\]

and define the nonnegative higher-harmonic surplus

\[
\mathsf S_q
=\sum_{j\ge3}
(j-2)(n-j-1)\|f^{(j)}\|_2^2.
\tag{3.7}
\]

### Theorem 3.1 (exact aggregate duplicate--mixing ledger)

For every exact factor,

\[
\boxed{
\|f\|_2^2=2\Phi_q(F)+\beta,
}
\tag{3.8}
\]

\[
\boxed{
\mathbf B_q
=2(n-1)\Phi_q(F)
+\frac{
2(n-1)\beta+\mathsf S_q-\operatorname{TV}_q
}{2},
}
\tag{3.9}
\]

\[
\boxed{
\mathbf M_q+\mathbf R_q
=\frac{\mathbf V_q-\operatorname{TV}_q}{2},
}
\tag{3.10}
\]

and therefore

\[
\boxed{
\mathbf B_q-\mathbf M_q-\mathbf R_q
=2(n-1)\Phi_q(F)-\frac{X_q}{2},
}
\tag{3.11}
\]

where

\[
\boxed{
X_q
=\mathbf V_q-2(n-1)\beta-\mathsf S_q.
}
\tag{3.12}
\]

Equivalently, if

\[
U_q=\operatorname{TV}_q-2(n-1)\beta-\mathsf S_q,
\tag{3.13}
\]

then

\[
\boxed{
X_q=U_q+2(\mathbf M_q+\mathbf R_q).
}
\tag{3.14}
\]

Thus opposite-target mixing and within-component residue are not the whole
obstruction: \(U_q\) is a distinct unit-gradient/harmonic term. It may have
either sign; its positive part is the shielding obstruction.

#### Proof

Write \(b(S)=\mu_q(S)-c\). Since

\[
\sum_Sb(S)=\theta N,
\]

one has

\[
2\Phi_q
=\sum_Sb(S)(b(S)-1)
=\sum_Sb(S)^2-\theta N
=\|f\|_2^2-\beta,
\]

which proves (3.8).

Every Johnson edge of \(J(n,r)\) is represented exactly once by a pair
\((\tau,p)\). Its unnormalized Laplacian has eigenvalue

\[
j(n-j+1)
\]

on degree \(j\). Hence

\[
\begin{aligned}
\sum_{\tau,p}z_{\tau,p}^2
&=\langle f,L_{J(n,r)}f\rangle\\
&=2(n-1)\|f\|_2^2
+\sum_{j\ge3}
\bigl(j(n-j+1)-2(n-1)\bigr)
\|f^{(j)}\|_2^2\\
&=2(n-1)(2\Phi_q+\beta)+\mathsf S_q,
\end{aligned}
\tag{3.15}
\]

because

\[
j(n-j+1)-2(n-1)
=(j-2)(n-j-1).
\]

Targetwise,

\[
2\mathsf B_p=z_p^2-|z_p|,
\qquad
2(\mathsf M_p+\mathsf R_p)
=\sum_Kd_{K,p}^2-|z_p|.
\tag{3.16}
\]

Summing (3.16) and using (3.15) proves
(3.9)--(3.11). Equation (3.14) is immediate. \(\square\)

### Corollary 3.2 (exact coefficient-one gate)

Put

\[
\omega_q=\frac1{2b_q}=\frac1{c_q(c_q+1)},
\qquad
X_A^{\rm fac}=\sum_{q\le H}\omega_qX_q.
\tag{3.17}
\]

Then

\[
\boxed{
\sum_{\tau}\mathcal D_\tau^{\rm fac}(F)
=(n-1)\mathfrak F_A(F)-\frac12X_A^{\rm fac},
}
\tag{3.18}
\]

and therefore

\[
\boxed{
\max_\tau\mathcal D_\tau^{\rm fac}(F)
\ge
\frac2n\mathfrak F_A(F)
-\frac{X_A^{\rm fac}}{n(n-1)}.
}
\tag{3.19}
\]

In particular, if

\[
\boxed{
X_A^{\rm fac}
\le
(2-\eta)(n-1)\mathfrak F_A(F)
+C(n-1)HB,
}
\tag{3.20}
\]

then some transposition's fair complete-side distribution has expected gain
at least

\[
\boxed{
\frac{\eta}{n}\mathfrak F_A(F)-\frac{CHB}{n}.
}
\tag{3.21}
\]

If \(F_*\) globally minimizes \(\mathfrak F_A\), every exact child has
nonnegative objective increment. If (3.20) holds at \(F_*\) whenever
\(\mathfrak F_A(F_*)>(C/\eta)HB\), then global minimality and (3.21) give

\[
\boxed{
\mathfrak F_A(F_*)\le\frac C\eta HB=o(W).
}
\tag{3.22}
\]

Thus (3.20), uniformly above the stated residue, composes with the audited
factorial and literal-tail transfer into the sharp constant-one theorem.
Inequality (3.20) is **UNPROVED**.

#### Proof

Equation (2.9) and Theorem 3.1 give

\[
\sum_\tau\mathcal D_\tau^{\rm fac}
=
\sum_{q\le H}\omega_q
\left(2(n-1)\Phi_q-\frac{X_q}{2}\right)
=(n-1)\mathfrak F_A-\frac{X_A^{\rm fac}}2.
\]

There are \(n(n-1)/2\) unordered transpositions, which proves (3.19).
Substitution of (3.20) proves (3.21). At a global minimizer its left side
cannot be positive, so (3.22) follows. \(\square\)

For the standard balanced overload \(O_q\), one has \(O_q\le\Phi_q\).
Since \(c_q\le L_A:=e^{2(A+1)(A+2)}\) on the fixed window,

\[
\sum_{q\le H}\frac{O_q}{c_q}
\le
\frac{L_A+1}{2}\,\mathfrak F_A.
\tag{3.23}
\]

Thus (3.22) gives the explicit weighted-overload bound

\[
\sum_{q\le H}\frac{O_q(F_*)}{c_q}
\le
\frac{(L_A+1)C}{2\eta}HB=o(W),
\tag{3.24}
\]

before diagonalization and literal tail transfer.

---

## 4. The quantitative singleton-fragmentation obstruction

The next theorem is a counting refinement of genuine component data. It
does not claim that singleton owner rows are independently switchable.

Fix one rank \(r=m-q\) with \(2\le r\le m-1\), and put

\[
d=r(n-r).
\tag{4.1}
\]

For a Johnson edge \(\{S,T\}\) and a wreath row \(C\), set

\[
d_C(S,T)
=\mathbf1_{\{S\text{ is a cyclic }r\text{-interval of }C\}}
-\mathbf1_{\{T\text{ is a cyclic }r\text{-interval of }C\}}.
\tag{4.2}
\]

Define the singleton-refined duplicate-minus-mixing sum

\[
D_q^{\rm sing}
=
\sum_{\{S,T\}\in E(J(n,r))}
\sum_{C<D}d_C(S,T)d_D(S,T).
\tag{4.3}
\]

### Theorem 4.1 (exact singleton and legal-coarsening ledgers)

One has

\[
\boxed{
D_q^{\rm sing}
=
\frac12
\sum_{\{S,T\}\in E(J(n,r))}
(\mu_q(S)-\mu_q(T))^2
-\left(\frac d2-1\right)W.
}
\tag{4.4}
\]

For any owner partition \(\mathcal P_\tau\), and in particular for the
genuine ownership-component partition, define

\[
I_q^{\rm dup}
=\sum_{\tau,p,K}
\left[\binom{x_K}{2}+\binom{y_K}{2}\right],
\tag{4.5}
\]

\[
I_q^{\rm opp}
=\sum_{\tau,p,K}(x_Ky_K-h_K),
\tag{4.6}
\]

where \(h_K\) counts rows in \(K\) owning both targets of \(p\). Then

\[
\boxed{
D_q(\mathcal P)
=D_q^{\rm sing}
+I_q^{\rm opp}-I_q^{\rm dup},
}
\tag{4.7}
\]

where

\[
D_q(\mathcal P)
=\sum_{\tau,p}
(\mathsf B_{\tau,p}-\mathsf M_{\tau,p}-\mathsf R_{\tau,p}).
\tag{4.8}
\]

For genuine ownership components, \(D_q(\mathcal P)/2\) is the sum over
transpositions of the fair expected decrease in the undoubled objective
\(\Phi_q\). Thus “nonnegative total fair gap” below is equivalently the
condition \(\sum_qD_q(\mathcal P)/b_q\ge0\).

#### Proof

For an edge \(\{S,T\}\), direct expansion of (4.3) gives

\[
\binom{\mu(S)}2+\binom{\mu(T)}2-\mu(S)\mu(T)+h(S,T),
\tag{4.9}
\]

where \(h(S,T)\) is the number of rows owning both \(S\) and \(T\).

Every row contains exactly the \(n\) Johnson edges between consecutive
cyclic \(r\)-intervals. Since \(2\le r<n/2\), no other two cyclic
\(r\)-intervals of that row are Johnson-adjacent. Therefore

\[
\sum_{\{S,T\}}h(S,T)=n|F|=W.
\tag{4.10}
\]

Every rank-\(r\) target has Johnson degree \(d\). Summing (4.9), using
\(\sum_S\mu(S)=W\), and expanding the Johnson Dirichlet energy proves
(4.4).

Passing from singleton rows to a block \(K\) removes the same-target row
pairs counted by (4.5) from the separated sum. It also removes from
opposite-target mixing exactly the distinct-row pairs counted by (4.6).
Summing over the blocks proves (4.7). \(\square\)

### Theorem 4.2 (quantitative fragmentation penalty)

Let

\[
\theta=\frac WN-c,\qquad
\beta=N\theta(1-\theta).
\]

Then

\[
\boxed{
\frac{\beta}{W}\le3-2\sqrt2,
}
\tag{4.11}
\]

and

\[
\boxed{
D_q^{\rm sing}
\le
-\kappa_{m,q}\,dW+(d+r)\Phi_q(F),
}
\tag{4.12}
\]

where

\[
\boxed{
\kappa_{m,q}
=
\frac12-\frac1d
-\frac{3-2\sqrt2}{2}
\left(1+\frac1{n-r}\right).
}
\tag{4.13}
\]

Uniformly for \(q\le A\sqrt m\),

\[
\boxed{
\kappa_{m,q}=\sqrt2-1-o_A(1).
}
\tag{4.14}
\]

Consequently, if

\[
\sum_{q\le H}\frac{\Phi_q(F)}{b_q}=o(W),
\tag{4.15}
\]

then

\[
\boxed{
\sum_{q\le H}\frac{D_q^{\rm sing}}{b_q}
\le
-(\sqrt2-1-o_A(1))
W\sum_{q\le H}\frac{(m-q)(m+q+1)}{b_q}.
}
\tag{4.16}
\]

Thus any genuine component partition with a nonnegative total fair gap must
satisfy

\[
\boxed{
\sum_{q\le H}\frac{
I_q^{\rm opp}-I_q^{\rm dup}
}{b_q}
\ge
(\sqrt2-1-o_A(1))
W\sum_{q\le H}
\frac{(m-q)(m+q+1)}{b_q}.
}
\tag{4.17}
\]

#### Proof

The function

\[
\frac{\theta(1-\theta)}{c+\theta}
\]

is largest when \(c=1\) and \(\theta=\sqrt2-1\), where its value is
\(3-2\sqrt2\). This proves (4.11).

The largest eigenvalue of the Johnson Laplacian is

\[
r(n-r+1)=d+r.
\]

Equations (3.8) and (4.4) therefore give

\[
\begin{aligned}
D_q^{\rm sing}
&\le\frac{d+r}{2}(\beta+2\Phi_q)
-\left(\frac d2-1\right)W\\
&\le-\kappa_{m,q}dW+(d+r)\Phi_q,
\end{aligned}
\]

which is (4.12). Since \(r=m-q\), \(n-r=m+q+1\), and
\(d=\Theta_A(m^2)\), equation (4.14) follows.

On the fixed window, \(b_q\) is bounded above and below by positive
\(A\)-dependent constants. The positive term obtained by summing
(4.12) is at most

\[
O(m^2)\sum_{q\le H}\frac{\Phi_q}{b_q}=o(Wm^2),
\]

whereas

\[
W\sum_{q\le H}\frac d{b_q}=\Theta_A(Wm^{5/2}).
\]

This proves (4.16). Equation (4.17) follows from (4.7). \(\square\)

The singleton refinement is not a legal switching cube. Its role is exact
and limited: it proves that maximal unsigned fragmentation creates a
macroscopic opposite-target baseline. A legal proof must exploit the
target-sensitive co-location term in (4.7), not component count alone.

---

## 5. An exact high-collision cell with zero best cut

We now prove the decisive genuine-factor no-go.

Let \(F_m^{\rm MSW}\) be the canonical MSW factor and fix

\[
\tau=(2\,3).
\]

Its exact component hierarchy contains the pairwise owner-disjoint
size-two components

\[
J_R=\{1100R,1010R\},
\qquad R\in\mathcal D_{m-2}.
\tag{5.1}
\]

Let \(\mathscr X_m\) be the **full** intrinsic \(\tau\)-component cube,
including all ownership components, not only the packets in (5.1).

### Lemma 5.1 (exactness and intrinsic persistence)

Every vertex of \(\mathscr X_m\) is an integral exact factor. From every
vertex, the freshly recomputed \(\tau\)-overlay has the same component
roots and therefore the same cube \(\mathscr X_m\).

#### Proof

For a component \(K\), its two row sides partition the same middle-root
union \(U_K\). Moreover \(\tau U_K=U_K\). Choosing either side therefore
partitions \(U_K\), and the different \(U_K\)'s are disjoint and cover the
middle layer. This proves exactness.

At any cube vertex, restriction to \(U_K\) is one of the two original
sides. Its \(\tau\)-translate is the other side, and the internal overlay
is the original connected component, possibly read with its shores
reversed. Since \(U_K\) and its complement are both \(\tau\)-invariant, no
overlay edge crosses between roots. Thus the components persist. \(\square\)

### Lemma 5.2 (Catalan private pair-orbit floor)

For every \(1\le q\le m-2\), there are

\[
L_q=C_{m-q-2}
\tag{5.2}
\]

distinct moved \(\tau\)-target pairs \(p_V=\{S_V,\tau S_V\}\) such that
every \(F\in\mathscr X_m\) satisfies

\[
\boxed{
\mu_q^F(S_V)+\mu_q^F(\tau S_V)\ge C_q.
}
\tag{5.3}
\]

#### Proof

Restrict the packet indices in (5.1) to

\[
R=UV,\qquad
U\in\mathcal D_q,\quad
V\in\mathcal D_{m-q-2}.
\]

For fixed \(V\), Lemma 4.1 of
`MATH_ATTACK_AB5_AFR_OVERLAY_FRAGMENTATION_20260725.md` and its audited
four-arm formula make all \(C_q\) choices of \(U\) contribute the same
oriented even-suffix dipole. In the MSW flip-list notation, let
\(\mathsf A(V)\) be the down-step list of \(V\). Its common core and moved
pair are

\[
\mathcal C_V=(4+2q+\mathsf A(V))\cup\{n\},
\qquad
p_V=\{\mathcal C_V\cup\{2\},\mathcal C_V\cup\{3\}\}.
\tag{5.3a}
\]

Every negative arm, for every packet index, omits the private coordinate
\(n\): the opposite even-prefix arm deletes it and the two odd arms never
contain it. Hence there is no cross-packet negative cancellation, and the
coefficient on \(p_V\) has magnitude at least \(C_q\). The map
\(V\mapsto\mathsf A(V)=\operatorname{Down}(V)\) is injective, since the
down-step set determines the Dyck word. Thus the cores and unordered moved
pairs are distinct.

Let \(a\) be the old selected-packet load and \(\tau a\) its translated
load. On a private pair,

\[
|a(S_V)-a(\tau S_V)|\ge C_q.
\]

All load entries are nonnegative, so

\[
a(S_V)+a(\tau S_V)\ge C_q.
\]

The other rows only increase the total. Finally, switching any complete
\(\tau\)-component interchanges its two contributions on a \(\tau\)-pair
and preserves their sum. Thus (5.3) holds on every cube vertex. \(\square\)

### Theorem 5.3 (exact same-overlay factorial no-go)

For every fixed \(A>0\) and all sufficiently large \(m\), there is a vertex
\(G_m\in\mathscr X_m\) such that

\[
\boxed{
\max_I\bigl(
\mathfrak F_A(G_m)-\mathfrak F_A(G_m^I)
\bigr)=0,
}
\tag{5.4}
\]

while

\[
\boxed{
\mathfrak F_A(G_m)
\ge
W\left(
\frac{4^H}{2048K_A\,nH^4}-1
\right).
}
\tag{5.5}
\]

Consequently

\[
\frac{\mathfrak F_A(G_m)}W\to\infty,
\qquad
\frac{\mathfrak F_A(G_m)}{nW}\to\infty.
\tag{5.6}
\]

#### Proof

For nonnegative integers \(x+y=t\),

\[
\min_{x+y=t}
\left[\binom x2+\binom y2\right]
=
\psi(t):=
\left\lfloor\frac{(t-1)^2}{4}\right\rfloor.
\tag{5.7}
\]

Apply Lemma 5.2 at \(q=H\). The \(L_H=C_{m-H-2}\) pairs are distinct,
so every \(F\in\mathscr X_m\) obeys

\[
\Phi_H(F)
\ge
C_{m-H-2}\psi(C_H)-P_H^{\min}.
\tag{5.8}
\]

For \(H\ge3\),

\[
C_H\ge\frac{4^H}{4H^2},
\qquad
\psi(C_H)\ge\frac{C_H^2}{8}.
\tag{5.9}
\]

Every successive Catalan ratio is less than four, hence

\[
C_{m-H-2}>
\frac{C_m}{4^{H+2}}
=\frac{W}{n4^{H+2}}.
\tag{5.10}
\]

Equations (5.9)--(5.10) give

\[
C_{m-H-2}\psi(C_H)
>
\frac{W4^H}{2048\,nH^4}.
\tag{5.11}
\]

Furthermore,

\[
\frac W{N_H}
=\prod_{j=0}^{H-1}
\frac{m+2+j}{m-j}
\le
\exp\left(\frac{2H(H+1)}m\right)
\le
e^{2(A+1)(A+2)}
\tag{5.12}
\]

for sufficiently large \(m\). Thus \(b_H\le K_A\), while

\[
P_H^{\min}\le N_Hb_H\le Wb_H.
\tag{5.13}
\]

Divide (5.8) by \(b_H\), use (5.11)--(5.13), and discard the other
nonnegative depths:

\[
\mathfrak F_A(F)
\ge
\frac{\Phi_H(F)}{b_H}
\ge
W\left(
\frac{4^H}{2048K_A\,nH^4}-1
\right)
\tag{5.14}
\]

for every \(F\in\mathscr X_m\).

Choose \(G_m\) to minimize \(\mathfrak F_A\) on the finite cube
\(\mathscr X_m\). By Lemma 5.1, every component cut stays in that same
cube, so no cut decreases the objective. The empty cut gives gain zero;
equivalently, the full cut gives the relabelled factor \(\tau G_m\), whose
objective is equal. This proves (5.4).

Finally \(H=\lceil A\sqrt m\rceil\), so

\[
\frac{4^H}{n^2H^4}\longrightarrow\infty.
\]

Together with (5.14), this proves (5.5)--(5.6). \(\square\)

### Corollary 5.4 (precise false theorem class)

Fix \(A>0\) and a transposition \(\tau\) in advance. There do not exist
\(\eta_A>0\) and an error \(e_A(m)\) satisfying

\[
\max_I\bigl(
\mathfrak F_A(F)-\mathfrak F_A(F^I)
\bigr)
\ge
\frac{\eta_A}{n}\mathfrak F_A(F)-e_A(m)
\tag{5.15}
\]

for every exact factor \(F\), whenever

\[
e_A(m)
=o\left(\frac{\mathfrak F_A(G_m)}n\right).
\tag{5.16}
\]

In particular, (5.15) is false with the coefficient-one-scale residue

\[
e_A(m)=O_A(HB/n),
\]

and even with \(e_A(m)=O_A(W)\). More generally it remains false if the
capture coefficient is any fixed inverse polynomial in \(m\) and the error
is polynomial times \(W\).

#### Proof

For \(\tau=(2\,3)\), substitute \(F=G_m\) from Theorem 5.3. The left side
is zero, while the right side is positive for all sufficiently large
\(m\). Conjugate the entire exact cell to obtain the same conclusion for
any transposition fixed in advance. \(\square\)

---

## 6. What is closed and what remains

The following statements are now proved.

1. The exact deterministic occurrence ledger is duplicate separation minus
   opposite-target mixing, with no hidden factor or parity loss.
2. The all-transposition aggregate ledger (3.18) has the sharp constants
   \(n-1\), \(1/2\), and \(2/n\).
3. The scale-correct sufficient gate furnished by this fair aggregate ledger
   is (3.20); it must control unit-gradient shielding, opposite mixing, and
   within-component multiplicity simultaneously.
4. Singleton fragmentation has the explicit uniform negative constant
   \(\sqrt2-1\) on every fixed Gaussian window.
5. A prescribed genuine MSW transposition cell can be completely locked at
   factorial collision \(\omega(nW)\). No common signing, correlated cut,
   component expansion, or packet abundance theorem inside that cell can
   prove coefficient one.

This definitively closes the lane with quantifiers

\[
\forall F\ \forall\tau
\quad\text{or}\quad
\text{a bridge prescribed independently of }F,
\]

and it closes the canonical MSW bridge after committing to its intrinsic
cell. It does not close a transposition selected adaptively from \(F\).

The following are not closed.

1. An all-transposition selector theorem

   \[
   \forall F\ \exists\tau
   \]

   controlling \(X_A^{\rm fac}\) at a global minimizer.
2. Adaptive preparation followed by a genuinely new bridge and recomputed
   components.
3. A direct construction of one exact factor satisfying
   \(\mathfrak F_A=o(W)\).
4. A literal contiguous-OR construction bypassing exact-factor collision
   balancing.

The same-cell obstruction is an exact-factor method no-go, not a
counterexample to the sharp constant-one conjecture.

Every load in Theorem 5.3 is the actual cyclic-interval histogram of a set
of literal wreath rows, and every \(G_m^I\) is another squarefree exact
middle factor. Thus the obstruction survives the integrality and literal
middle-block requirements; it is not obtained by averaging factors or by
postulating a signed load profile.

---

## 7. Independent audit checklist

The decisive steps requiring independent audit are:

1. **Normalization.** \(\Phi_q\) is undoubled collision excess,
   \(2\Phi_q\) is the floor energy, and the factorial weight is
   \(1/b_q\). Therefore fair gain uses \(1/(2b_q)\), as in (2.9).
2. **Johnson counting.** Every pair \((\tau,p)\) is one Johnson edge;
   the eigenvalue is \(j(n-j+1)\), and the degree-two baseline is
   \(2(n-1)\).
3. **Singleton row edges.** For \(2\le r<n/2\), one cyclic row has exactly
   \(n\) Johnson-adjacent interval pairs.
4. **Private pairs.** The \(C_{m-H-2}\) Catalan cores are distinct
   \(\tau\)-pairs, and every full-cell switch preserves their pair totals.
5. **Constants.** The factors \(2048\), \(K_A\), and \(nH^4\) in (5.5)
   come respectively from the pair collision floor, two Catalan estimates,
   the bounded Gaussian load, and \(B=W/n\).
6. **Scope.** The singleton refinement is counting-only; Theorem 5.3,
   by contrast, uses only genuine complete component switches inside one
   intrinsic exact-factor cell.

No unproved implication is used in Theorem 5.3 or Corollary 5.4.
