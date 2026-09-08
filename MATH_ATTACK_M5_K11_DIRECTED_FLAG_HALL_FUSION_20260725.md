# Fifth-wave lane M: directed-flag and external-Hall fusion at \(k=11\)

Date: 2026-07-25

## 1. Verdict

Assume the audited length-\(465\), zero-margin \(k=11\) normal form and
Theorem M3-K11 from
MATH_ATTACK_M3_K11_RANK7_PHYSICAL_LIFT_20260724.md.

No contradiction is obtained, and the certified lower bound for
\(\nu(11)\) is not improved.

There are nevertheless four strict finite advances.

1. The external directed flags obey a new orthogonality Hall system. For
   every nonempty \(Z\subseteq[11]\), externally supported complement rows,
   sources containing \(Z\), and swap pairs meeting \(Z\) are disjoint
   anchor classes. For a singleton, path telescoping changes the physical
   factor-four pair bound into an exact factor-two head-label inequality
   with explicit endpoint restitution.

2. Every external-headed forest arc supplies a second
   external-source/external-target inclusion in addition to the perfect
   matching incidence. More sharply, lifting each such incidence through
   its five rank-seven supersets gives the directed-capacity inequality
   \[
   \boxed{
   \sum_Y
   \mathfrak h_{7-V_Y}(21-U_Y)
   \geq10E-5c+5b_H-5d,
   }
   \]
   where \(\mathfrak h_v(u)\) is the exact maximum number of incidences
   between \(u\) edges and \(v\) vertices of \(K_7\).  Its singleton
   projections retain the directed complement flags and the path endpoint
   restitution.  In particular, if \(K\) is the central
   rank-five/rank-six inclusion count, then
   \[
   \boxed{
   K\geq2772-10E-c+b_H-d.
   }
   \]
   At the smallest external mass \(E=132\), this forces
   \[
   K\geq1446,
   \]
   at least \(152\) central six-targets with at least four central facets,
   and at least \(63\) with at least five.

3. The central joint-zero geometry supplies a second, correlated capacity
   on every external rank-seven row. If \(a_Y\) is the excess of central
   rank-five sources in \(Q=[11]\setminus Y\) over its central six-facets,
   then
   \[
   \boxed{
   x_Y\leq(6-V_Y)_+-(a_Y-15)_+.
   }
   \]
   Hence
   \[
   \boxed{
   \sum_Y(a_Y-15)_+
   \leq4E-330+c+d-b_H+N_7^\star.
   }
   \]
   This is a genuine new global inequality, but the exact moment
   \(\sum_Ya_Y=10q\) permits every positive-part term to vanish.

4. The short rank-eight lift improves sharply. A fixed rank-eight color
   has at most \(23\), not \(26\), nonlazy width-at-most-five occurrences;
   the constant \(23\) is sharp for the abstract linear-forest restriction
   geometry. More importantly, at least \(314\) distinct supported
   rank-seven colors are pivot-active. A four-shadow argument then gives
   \[
   \boxed{
   z_8^{(\leq5)}\geq47.
   }
   \]
   The link open-wedge audit excludes shadow defects one and three.  Thus
   the lower bound is actually \(48\) whenever
   \((c-c_0)+M_7\leq16\).  Any surviving \(47\)-color case is forced to
   the unique parameter corner
   \[
   c=6,\qquad c_0=0,\qquad M_7=11,\qquad D=7,
   \]
   with nonzero pair-codegree defect \(\Phi\), five monochromatic short
   components, and one component carrying at least \(426\) edges.
   This strictly improves the previous lower bound \(13\), but remains far
   below the \(165\) rank-eight targets.

All proofs below are finite, deterministic, and integral. No web lookup,
finite search, solver, random experiment, or computational enumeration is
used.

## 2. Frozen notation

Put
\[
\Omega=[11].
\]
Let
\[
q=m-3,\qquad E=462-q=465-m.
\tag{2.1}
\]
The projected six-set forest has \(c\leq6\) path components and
\[
462-c
\tag{2.2}
\]
edges. Let
\[
b_H\in\{1,2\}
\]
be the number of postcut central six-path pieces, and let
\[
0\leq d\leq b_H
\tag{2.3}
\]
be the number of retained inward interfaces. The external induced forest
has
\[
s_{\rm ext}=c-b_H+d
\tag{2.4}
\]
components and
\[
R_{\rm ext}=E-s_{\rm ext}=E+b_H-c-d
\tag{2.5}
\]
edges.

Let
\[
\mathscr C_5\subseteq\binom{\Omega}{5},
\qquad
\mathscr T_6\subseteq\binom{\Omega}{6}
\tag{2.6}
\]
be the central source and target families. Both have size \(q\), and the
perfect matching maps \(\mathscr C_5\) onto \(\mathscr T_6\). Their
external complements have size \(E\).

For \(Y\in\binom{\Omega}{4}\), put
\[
Q=\Omega\setminus Y.
\tag{2.7}
\]
Retain the exact physical-lift notation
\[
V_Y=\#\{T\in\mathscr T_6:T\subset Q\},
\tag{2.8}
\]
\[
t_Q=c_Y+\rho_Y+x_Y.
\tag{2.9}
\]
Here \(c_Y\) is the central-core multiplicity, \(\rho_Y\) is the interface
multiplicity, and \(x_Y\) is the external-headed multiplicity. Thus
\[
\sum_Yc_Y=q-b_H,\qquad
\sum_Y\rho_Y=d,\qquad
\sum_Yx_Y=R_{\rm ext}.
\tag{2.10}
\]
The frozen bounds are
\[
0\leq t_Q\leq6,
\qquad
M_7:=\#\{Q:t_Q=0\}\leq11,
\tag{2.11}
\]
\[
\Delta_7=\sum_Q(t_Q-1)_+
=132-c+M_7,
\qquad
126\leq\Delta_7\leq137.
\tag{2.12}
\]

For an external-headed anchor \(p\), the exact flag is
\[
\Omega
=Y_p\sqcup S_p\sqcup\{\xi_p,\beta_p\},
\qquad
(|Y_p|,|S_p|)=(4,5).
\tag{2.13}
\]
The external transition gains \(\xi_p\), loses \(\beta_p\), and has
\[
Q_p=\Omega\setminus Y_p.
\tag{2.14}
\]
Let
\[
\omega_x=\#\{p:\xi_p=x\},
\qquad
\omega(Z)=\sum_{x\in Z}\omega_x.
\tag{2.15}
\]

For nonempty \(Z\subseteq\Omega\), define
\[
A_Z^{\rm ext}
=\#\{Y:Z\subseteq Y,\ x_Y>0\},
\tag{2.16}
\]
\[
X_Z=\sum_{Y\supseteq Z}x_Y,
\qquad
\Delta_Z^{\rm ext}
=\sum_{Y\supseteq Z}(x_Y-1)_+,
\tag{2.17}
\]
\[
s_Z^{\rm h}
=\#\{p:Z\subseteq S_p\},
\tag{2.18}
\]
\[
P_Z
=\#\{p:\{\xi_p,\beta_p\}\cap Z\neq\varnothing\}.
\tag{2.19}
\]
All anchors in (2.15)--(2.19) are external-headed.

## 3. Orthogonality Hall and exact path restitution

### Theorem 3.1: the three disjoint anchor classes

For every nonempty \(Z\subseteq\Omega\),
\[
\boxed{
A_Z^{\rm ext}+s_Z^{\rm h}+P_Z
\leq R_{\rm ext}.
}
\tag{3.1}
\]

#### Proof

For every \(Y\supseteq Z\) with \(x_Y>0\), choose one external-headed
representative of that row. Its flag satisfies
\[
S_p\subseteq Q_p=\Omega\setminus Y,
\qquad
\{\xi_p,\beta_p\}\subseteq Q_p.
\]
Thus both \(S_p\) and the swap pair avoid \(Z\). The chosen
representatives are therefore disjoint from the \(s_Z^{\rm h}\) anchors
and from the \(P_Z\) anchors.

The latter two classes are also disjoint. Indeed,
\[
S_p\cap\{\xi_p,\beta_p\}=\varnothing;
\]
if \(Z\subseteq S_p\), the pair cannot meet \(Z\). All three classes lie
among the \(R_{\rm ext}\) external-headed anchors, proving (3.1).
\(\square\)

The empty-set case is deliberately excluded: \(s_\varnothing^{\rm h}\)
already equals \(R_{\rm ext}\).

### Exact slack

For \(|Z|>1\), let \(H_Z\) count the remaining anchors for which the swap
pair avoids \(Z\), while \(Z\) meets both \(Y_p\) and \(S_p\) nontrivially.
The flag partition (2.13) gives
\[
\boxed{
R_{\rm ext}
=X_Z+s_Z^{\rm h}+P_Z+H_Z.
}
\tag{3.2}
\]
Consequently,
\[
\boxed{
R_{\rm ext}
-(A_Z^{\rm ext}+s_Z^{\rm h}+P_Z)
=\Delta_Z^{\rm ext}+H_Z.
}
\tag{3.3}
\]
For \(Z=\{x\}\), no mixed class exists:
\[
\boxed{
X_{\{x\}}+s_{\{x\}}^{\rm h}+P_{\{x\}}
=R_{\rm ext},
}
\tag{3.4}
\]
\[
\boxed{
R_{\rm ext}
-(A_{\{x\}}^{\rm ext}+s_{\{x\}}^{\rm h}+P_{\{x\}})
=\sum_{Y\ni x}(x_Y-1)_+.
}
\tag{3.5}
\]
Thus (3.1) is exact but, by itself, is a support projection: its singleton
slack is precisely the external-headed same-color repetition.

### Corollary 3.2: fusion with pair Hall

For \(Q\in\binom{\Omega}{7}\), let
\[
\mathcal E_Q
=\{z\in Q:Q\setminus\{z\}
\text{ is an external six-set}\}.
\tag{3.6}
\]
Then
\[
|\mathcal E_Q|=7-V_{\Omega\setminus Q}.
\tag{3.7}
\]
Define
\[
G_Z=
\sum_Q
\left[
x_{\Omega\setminus Q}
-\bigl(|\mathcal E_Q\setminus Z|-1\bigr)_+
\right]_+.
\tag{3.8}
\]
The external pair-forest bound gives
\[
P_Z\geq G_Z.
\]
Also \(P_Z\geq\omega(Z)\), since the head label is one member of the swap
pair. Hence
\[
\boxed{
A_Z^{\rm ext}+s_Z^{\rm h}
+\max\{\omega(Z),G_Z\}
\leq R_{\rm ext}.
}
\tag{3.9}
\]
This is the strongest eliminable form of the joint representative cut.
It becomes effective only if many external rows saturate their available
facet forests.

### Theorem 3.3: singleton path telescoping

Let \(\sigma_x\) count external induced-path starts whose six-set contains
\(x\), and let \(\nu_x\) count external induced-path terminals whose
six-set contains \(x\). Then
\[
\boxed{
P_{\{x\}}
=2\omega_x+\sigma_x-\nu_x.
}
\tag{3.10}
\]
Consequently,
\[
\boxed{
A_{\{x\}}^{\rm ext}
+s_{\{x\}}^{\rm h}
+2\omega_x+\sigma_x-\nu_x
\leq R_{\rm ext}.
}
\tag{3.11}
\]
Since the external forest has \(s_{\rm ext}\) components,
\[
0\leq\sigma_x,\nu_x\leq s_{\rm ext},
\]
and \(R_{\rm ext}+s_{\rm ext}=E\). Therefore
\[
\boxed{
A_{\{x\}}^{\rm ext}
+s_{\{x\}}^{\rm h}
+2\omega_x
\leq E-(s_{\rm ext}-\nu_x)-\sigma_x
\leq E.
}
\tag{3.12}
\]

#### Proof

Along an external path, an \(x\)-gain is exactly an edge with
\(\xi_p=x\), while an \(x\)-loss is exactly an edge with
\(\beta_p=x\). Telescoping the \(x\)-membership indicator gives
\[
\nu_x-\sigma_x
=\#\{\xi_p=x\}-\#\{\beta_p=x\}.
\]
Thus the loss count is
\[
\omega_x+\sigma_x-\nu_x.
\]
Adding gains and losses proves (3.10). Substitute it into (3.1) and use
\(\nu_x\leq s_{\rm ext}\) to get (3.11)--(3.12).
\(\square\)

Interfaces need no additional \(+2\) loss in (3.12): their external tails
are already terminals of the induced external forest.

### Central-inactive and low-entry form

Let
\[
\mathcal Y_0=\{Y:c_Y=0\},
\]
\[
N_x^0=\#\{Y\in\mathcal Y_0:x\in Y\},
\]
and let \(M_x^\perp\) count the globally missing rows among them. Let
\[
I_x^{\rm only}
=\#\{Y\in\mathcal Y_0:
x\in Y,\ \rho_Y>0,\ x_Y=0\}.
\tag{3.13}
\]
Then
\[
D_x^\sharp:=N_x^0-M_x^\perp-I_x^{\rm only}
\leq A_{\{x\}}^{\rm ext}.
\]
Hence (3.12) gives
\[
\boxed{
N_x^0-M_x^\perp-I_x^{\rm only}
+s_x^{\rm h}+2\omega_x
\leq E-(s_{\rm ext}-\nu_x)-\sigma_x
\leq E.
}
\tag{3.14}
\]

Put
\[
C_x=\sum_{Y\ni x}c_Y,
\qquad
\delta_x^C=\sum_{Y\ni x}(c_Y-1)_+,
\tag{3.15}
\]
and
\[
\gamma_x=(s_{\rm ext}-\nu_x)+\sigma_x\geq0.
\tag{3.16}
\]
Since
\[
N_x^0=120-C_x+\delta_x^C
\tag{3.17}
\]
and
\[
\omega_x
=43-R_x^{(3)}
-\mathbf1_{\{x\in H\}}-\iota_x,
\tag{3.18}
\]
the exact fused coordinate inequality is
\[
\boxed{
C_x+2R_x^{(3)}
+M_x^\perp+I_x^{\rm only}
\geq
206-E+\delta_x^C+s_x^{\rm h}+\gamma_x
-2\mathbf1_{\{x\in H\}}-2\iota_x.
}
\tag{3.19}
\]
Here \(\iota_x\) counts external-start matching labels.

Uniformly summing (3.14) over all coordinates recovers only the support
identity behind (3.3). Thus the live content of (3.19) is necessarily
nonuniform: one must force a specific coordinate with simultaneously high
central inactivity, high head-label demand, and low physical exposure.

## 4. Correlated source-and-facet capacity

Fix \(Y\in\binom{\Omega}{4}\). Let \(r_Y^{(3)}\) be the number of maximal
joint \(Y\)-zero-runs of central entries having length at least three, and
put
\[
\chi_Y=\mathbf1_{\{H\cap Y=\varnothing\}}.
\tag{4.1}
\]
Let
\[
U_Y
=\#\{C\in\mathscr C_5:C\subseteq Q\}.
\tag{4.2}
\]

### Lemma 4.1: exact source surplus

\[
\boxed{
U_Y=V_Y+r_Y^{(3)}-\chi_Y.
}
\tag{4.3}
\]
In particular, define
\[
a_Y:=U_Y-V_Y=r_Y^{(3)}-\chi_Y\geq0.
\tag{4.4}
\]
Then
\[
\boxed{
\sum_Ya_Y=10q.
}
\tag{4.5}
\]

#### Proof

A central triple window is contained in \(Q\) exactly when its three
entries avoid \(Y\). A joint zero-run of length \(\ell\) supplies
\((\ell-2)_+\) such triple windows and \((\ell-3)_+\) four-windows.
Their difference is one precisely for every run of length at least three.
All triple windows except \(H\) belong to \(\mathscr C_5\); if \(H\)
avoids \(Y\), its occurrence must be subtracted. This gives (4.3).

Every central source lies in exactly
\[
\binom{6}{2}=15
\]
rank-seven sets, so
\[
\sum_YU_Y=15q.
\]
Every central target lies in five rank-seven sets, so
\[
\sum_YV_Y=5q.
\]
Subtracting proves (4.5).
\(\square\)

### Theorem 4.2: fused row capacity

Every external-headed \(Q\)-edge uses a distinct external rank-five source
contained in \(Q\). Since \(Q\) has \(21\) rank-five subsets,
\[
x_Y\leq21-U_Y.
\tag{4.6}
\]
Together with the external-facet forest cap,
\[
x_Y\leq(6-V_Y)_+,
\tag{4.7}
\]
this gives
\[
\boxed{
x_Y
\leq
\kappa_Y
:=
(6-V_Y)_+-(a_Y-15)_+.
}
\tag{4.8}
\]

#### Proof

The source used by an external-headed edge is the intersection of its two
external six-facets. It is external, is contained in \(Q\), and is the
matched source of the destination. Distinct destinations have distinct
matched sources, proving (4.6).

For \(V_Y\leq6\),
\[
21-U_Y
=21-V_Y-a_Y
=(6-V_Y)+(15-a_Y).
\]
Taking the minimum with (4.7) subtracts exactly
\((a_Y-15)_+\). If \(V_Y=7\), then \(U_Y\leq21\) forces
\(a_Y\leq14\), so the correction vanishes and (4.8) remains exact.
\(\square\)

### Interface-tail refinement

Every external-headed or interface \(Q\)-arc has an external predecessor.
Its missing-coordinate label belongs to \(\mathcal E_Q\), and distinct
arcs have distinct external predecessors. Therefore
\[
\boxed{
x_Y+\rho_Y\leq7-V_Y.
}
\tag{4.9}
\]
The strongest row cap available here is consequently
\[
\boxed{
x_Y\leq
\widehat\kappa_Y:=
\min\{(6-V_Y)_+,\ 21-U_Y,\ 7-V_Y-\rho_Y\}.
}
\tag{4.10}
\]
Because \(\sum_Y\rho_Y=d\leq2\), the third term can differ from the
first on at most two interface rows; it is strictly smaller than
\((6-V_Y)_+\) only when \(\rho_Y=2\), hence on at most one row.

There is a matching Hall refinement. Let
\(\mathcal I_Q^{\rm tail}\subseteq\mathcal E_Q\) be the interface-tail
labels already used by \(Q\), and put
\[
\mathcal B_Q=\mathcal E_Q\setminus\mathcal I_Q^{\rm tail}.
\tag{4.11}
\]
Then the exact simple-head projection must satisfy
\[
\boxed{
\sum_Q
\left(
x_{\Omega\setminus Q}
-|\mathcal B_Q\setminus X|
\right)_+
\leq\omega(X)
\qquad(X\subseteq\Omega).
}
\tag{4.12}
\]
This restores the external-facet and interface-tail restrictions which
are invisible in a head-label matrix using only \(Q\) as its allowed
column set.

### Theorem 4.3: global source-saturation inequality

Put
\[
L_{\rm src}
=\sum_Y(a_Y-15)_+,
\qquad
N_7^\star=\#\{Y:V_Y=7\}.
\tag{4.13}
\]
Then
\[
\boxed{
L_{\rm src}
\leq
4E-330+c+d-b_H+N_7^\star.
}
\tag{4.14}
\]

#### Proof

Summing (4.8) and using (2.10) gives
\[
R_{\rm ext}
\leq
\sum_Y(6-V_Y)_+-L_{\rm src}.
\]
The exact facet-capacity sum is
\[
\sum_Y(6-V_Y)_+
=5E-330+N_7^\star.
\]
Substitute
\[
R_{\rm ext}=E+b_H-c-d
\]
and rearrange.
\(\square\)

Thus a contradiction would follow from
\[
L_{\rm src}
>
4E-330+c+d-b_H+N_7^\star.
\tag{4.15}
\]
At \(E=132\), the right side is
\[
198+s_{\rm ext}+N_7^\star.
\]
But (4.5) has average
\[
\frac1{330}\sum_Ya_Y=\frac q{33}\leq10.
\]
It is compatible with \(a_Y\leq15\) for every \(Y\), in which case
\(L_{\rm src}=0\). No scalar moment argument can activate (4.15).

### Rowwise duplicate gate

Let
\[
\varepsilon_Y
=\mathbf1_{\{\text{internal seam},\ \eta=0,\ Y=Y_*\}},
\tag{4.16}
\]
so that
\[
c_Y=W_Y-\varepsilon_Y.
\]
Write \(b_Y\) for the number of long joint \(Y\)-zero blocks and
\(u_{4,Y}\) for the number of exact length-four blocks. Since
\[
V_Y=W_Y+b_Y+u_{4,Y},
\]
(4.8) gives
\[
\boxed{
c_Y+\rho_Y+\kappa_Y
=
6-b_Y-u_{4,Y}-\varepsilon_Y+\rho_Y
+\mathbf1_{\{V_Y=7\}}-(a_Y-15)_+.
}
\tag{4.17}
\]
The long-run length \(W_Y\) cancels exactly.

Put
\[
\Gamma_Y
=c_Y+\rho_Y+\widehat\kappa_Y.
\tag{4.18}
\]
Every survivor must satisfy
\[
\boxed{
\#\{Y:\Gamma_Y=0\}\leq11,
}
\tag{4.19}
\]
\[
\boxed{
126
\leq
\sum_Y
\left(\min\{6,\Gamma_Y\}-1\right)_+.
}
\tag{4.20}
\]
Moreover, colors with \(c_Y=0\) and
\(\widehat\kappa_Y\leq1\) contribute at most \(d\) duplicate units in
total. Therefore at least
\[
\boxed{126-d\geq124}
\tag{4.21}
\]
duplicate units lie on colors satisfying
\[
c_Y>0
\quad\text{or}\quad
\widehat\kappa_Y\geq2.
\]
This strictly refines the former alternative
\(c_Y>0\) or \(V_Y\leq4\).

### Theorem 4.4: five-row directed-incidence capacity

For integers \(0\leq u\leq21\) and \(0\leq v\leq7\), define
\[
\mathfrak h_v(u)
=2\min\left\{u,\binom v2\right\}
+\min\left\{
\left(u-\binom v2\right)_+,\ v(7-v)
\right\}.
\tag{4.22}
\]
This is the exact maximum number of vertex-edge incidences between a
family of \(u\) edges and a family of \(v\) vertices in \(K_7\).

For \(Q=\Omega\setminus Y\), let \(K_Y\) be the number of central
rank-five/rank-six inclusions wholly contained in \(Q\), and let
\(J_Y^{EE}\) be the corresponding external-source/external-target
inclusion count.  Let \(m_Y\) count external matching incidences contained
in \(Q\).

For an external-headed flag \(p\), write its predecessor as
\[
U_p^-=S_p\cup\{\beta_p\}.
\]
Its nonmatching incidence is
\[
S_p\subset U_p^-.
\]
The five rank-seven supersets of this incidence have complement rows
\[
Y_p,
\qquad
(Y_p\setminus\{z\})\cup\{\xi_p\}
\quad(z\in Y_p).
\tag{4.23}
\]
Let \(h_Y\) count the occurrences of row \(Y\) in this five-row lift,
over all external-headed flags.  Then, row by row,
\[
\boxed{
m_Y+h_Y
\leq J_Y^{EE}
=42-2U_Y-6V_Y+K_Y
\leq H_Y^{EE},
}
\tag{4.24}
\]
where
\[
H_Y^{EE}
:=\mathfrak h_{7-V_Y}(21-U_Y).
\tag{4.25}
\]
Consequently,
\[
\boxed{
\sum_YH_Y^{EE}
\geq5(E+R_{\rm ext})
=10E-5s_{\rm ext}
=10E-5c+5b_H-5d.
}
\tag{4.26}
\]

There is an exact subset hierarchy behind (4.26).  For
\(Z\subseteq\Omega\), \(|Z|=r\leq4\), put
\[
e_Z^-
=\#\{T\text{ external six-target}:T\cap Z=\varnothing\},
\tag{4.27}
\]
\[
\lambda_Z
=\#\{p:Z\subseteq Y_p\cup\{\xi_p\}\}.
\tag{4.28}
\]
Then
\[
\boxed{
(5-r)(e_Z^-+\lambda_Z)
\leq
\sum_{Y\supseteq Z}H_Y^{EE}.
}
\tag{4.29}
\]
For a singleton this reads
\[
\boxed{
4(e_x^-+X_{\{x\}}+\omega_x)
\leq
\sum_{Y\ni x}H_Y^{EE}.
}
\tag{4.30}
\]
Using (3.4) and (3.10), its completely path-restored form is
\[
\boxed{
4\bigl(
e_x^-+R_{\rm ext}-s_x^{\rm h}-\omega_x-\sigma_x+\nu_x
\bigr)
\leq
\sum_{Y\ni x}H_Y^{EE}.
}
\tag{4.31}
\]

#### Proof

Inside a fixed seven-set \(Q\), identify its rank-five subsets with the
edges of \(K_7\) and its rank-six subsets with the vertices of \(K_7\).
An inclusion is precisely an edge-vertex incidence.  For fixed families
of \(u\) edges and \(v\) vertices, an edge internal to the vertex family
contributes two, a crossing edge contributes one, and every other edge
contributes zero.  Taking all \(\binom v2\) internal edges first and then
the \(v(7-v)\) crossing edges proves (4.22).

There are \(42\) incidences inside \(Q\).  The \(U_Y\) central edges meet
\(2U_Y\) incidences, the \(V_Y\) central vertices meet \(6V_Y\), and
their intersection has size \(K_Y\).  Inclusion-exclusion gives the
middle equality in (4.24).  The external families have sizes
\(21-U_Y\) and \(7-V_Y\), so (4.22) gives the upper bound.

The \(E\) external matching pairs are distinct external-external
incidences.  Every external-headed arc \(U_p^-\to U_p\) contributes the
second incidence \(S_p\subset U_p^-\).  It is nonmatching because
\(S_p\) is matched to \(U_p\neq U_p^-\).  Different arcs have different
destinations and hence different matched sources \(S_p\), so all these
second incidences are distinct from one another and from all matching
incidences.  Lifting distinct incidences through rank-seven supersets
preserves their distinction in each row.  The flag partition (2.13)
gives exactly the five rows in (4.23), proving the lower bound in (4.24).

Every rank-five/rank-six incidence lies in exactly five seven-sets.
Therefore
\[
\sum_Ym_Y=5E,
\qquad
\sum_Yh_Y=5R_{\rm ext}.
\]
Summing (4.24) proves (4.26), including the exact inward-interface defect
through \(s_{\rm ext}=c-b_H+d\).

The five complement rows lifted from any one incidence are precisely the
five four-facets of a five-set.  Exactly \(5-r\) of those facets contain
an \(r\)-set \(Z\) when \(Z\) lies in that five-set, and none do
otherwise.  For a matching incidence the five-set is the complement of
its external target; for a directed incidence it is
\(Y_p\cup\{\xi_p\}\).  This proves (4.29).  When \(Z=\{x\}\), the two
disjoint possibilities for the directed flag are \(x\in Y_p\) and
\(x=\xi_p\), counted by \(X_{\{x\}}\) and \(\omega_x\), respectively.
This proves (4.30).  Finally,
\[
X_{\{x\}}+2\omega_x+\sigma_x-\nu_x+s_x^{\rm h}
=R_{\rm ext}
\]
by (3.4) and (3.10), which gives (4.31).
\(\square\)

The scalar inequality (4.26) is feasible.  At
\(E=132,s_{\rm ext}=6\), it asks for a total capacity of at least
\(1290\).  The moment-relaxation profile \(U_Y=15,V_Y=5\) for all
\(Y\) has \(H_Y^{EE}=7\) and total \(2310\).  Thus any contradiction
from (4.24) or (4.29) must again be nonuniform; the displayed profile is
only an arithmetic capacity witness, not a physical word.

The full rowwise inequality (4.24), before eliminating \(J_Y^{EE}\) and
\(K_Y\), retains more distributional information than its
scalar sum.  Since every global inclusion lies in five seven-sets,
summing its lower half gives exactly five copies of Theorem 5.1 below.
Thus (5.2)--(5.3) are scalar consequences of the five-row system, whereas
(4.26) is the further capacity relaxation obtained after eliminating the
actual local incidence counts.

## 5. The second external incidence and central congestion

Let
\[
K
=\#\{(C,T)\in\mathscr C_5\times\mathscr T_6:C\subset T\}.
\tag{5.1}
\]
Let \(I_{EE}\) be the corresponding inclusion count between the external
rank-five sources and external rank-six targets.

### Theorem 5.1: two-incidence inequality

\[
\boxed{
I_{EE}\geq E+R_{\rm ext}=2E-s_{\rm ext}.
}
\tag{5.2}
\]
Consequently,
\[
\boxed{
K
\geq
10q-1848-s_{\rm ext}
=2772-10E-c+b_H-d.
}
\tag{5.3}
\]
Equivalently,
\[
\boxed{
6q-K\leq4E+s_{\rm ext}.
}
\tag{5.4}
\]

#### Proof

The full rank-five/rank-six inclusion graph is \(6\)-regular and has
\[
6\binom{11}{5}=2772
\]
edges. Block inclusion-exclusion gives
\[
I_{EE}=2772-12q+K.
\tag{5.5}
\]

The external perfect matching supplies \(E\) distinct \(EE\) incidences.
For every external-headed arc
\[
U^-\longrightarrow U,
\]
the destination source is
\[
P(U)=M^{-1}(U)=U^-\cap U.
\]
It is external, and
\[
P(U)\subset U^-
\]
is a second, nonmatching \(EE\) incidence. Different destinations have
different matched sources, so these \(R_{\rm ext}\) incidences are
distinct. None is a matching incidence, since that would match the same
source to both \(U\) and \(U^-\).

Interfaces are correctly excluded: every interface points from an
external target into a central target, and its intervening destination
source is central. This proves (5.2). Substitute (5.5) and
\(q=462-E\) to obtain (5.3)--(5.4).
\(\square\)

The improvement over the old matching-only residual-facet bound is exactly
\[
R_{\rm ext}\geq E-c\geq126.
\tag{5.6}
\]

### Corollary 5.2: many high-central-facet targets

For \(2\leq r\leq6\), let
\[
N_{\geq r}
=\#\{T\in\mathscr T_6:
\#\{C\in\mathscr C_5:C\subset T\}\geq r\}.
\tag{5.7}
\]
Then
\[
\boxed{
N_{\geq r}
\geq
\left\lceil
\frac{
\bigl(10q-1848-s_{\rm ext}-(r-1)q\bigr)_+
}{7-r}
\right\rceil.
}
\tag{5.8}
\]
In particular,
\[
\boxed{
N_{\geq4}
\geq
\max\left\{
0,\
q-\left\lfloor\frac{4E+s_{\rm ext}}3\right\rfloor
\right\},
}
\tag{5.9}
\]
\[
\boxed{
N_{\geq5}
\geq
\max\left\{
0,\
q-\left\lfloor\frac{4E+s_{\rm ext}}2\right\rfloor
\right\}.
}
\tag{5.10}
\]

#### Proof

Put
\[
k_T=\#\{C\in\mathscr C_5:C\subset T\}.
\]
Then
\[
\sum_Tk_T=K,\qquad0\leq k_T\leq6.
\]
If \(N_{\geq r}=n\), then
\[
K
\leq(r-1)(q-n)+6n
=(r-1)q+(7-r)n.
\]
Combine this with (5.3).
\(\square\)

At \(E=132\), the worst endpoint defect is \(s_{\rm ext}=6\), and
\[
\boxed{
K\geq1446,\qquad
N_{\geq4}\geq152,\qquad
N_{\geq5}\geq63.
}
\tag{5.11}
\]
At \(E=133,s_{\rm ext}=6\), the corresponding constants are
\[
\boxed{
K\geq1436,\qquad
N_{\geq4}\geq150,\qquad
N_{\geq5}\geq60.
}
\tag{5.12}
\]

The number of locally forced central incidences is \(2q-b_H\). Thus the
nonlocal central incidence count obeys
\[
\boxed{
K_{\rm nonlocal}
\geq
8q-1848-c+2b_H-d.
}
\tag{5.13}
\]
At \(E=132\), this is at least \(787\). These are genuine physical
joint-zero obligations, but no proved upper bound on their simultaneous
realization is below (5.13).

## 6. The sharp local rank-eight pivot cap

Let \(c_0\) be the number of isolated six-set components. Put
\[
\mathcal A_7
=\#\{\text{lazy adjacent hull pairs}\},
\qquad
\mathcal S_7
=\text{separated-return excess}.
\]
The exact duplicate identity is
\[
\Delta_7=\mathcal A_7+\mathcal S_7.
\tag{6.1}
\]
The number of adjacent pairs of forest edges is
\[
462-2c+c_0.
\]
Therefore the exact number of nonlazy, width-at-most-five rank-eight
occurrences is
\[
\boxed{
N_8^{(\leq5)}
=330-c-M_7+c_0+\mathcal S_7.
}
\tag{6.2}
\]
In particular,
\[
N_8^{(\leq5)}\geq313.
\tag{6.3}
\]

### Theorem 6.1: fixed rank-eight multiplicity is at most \(23\)

For every \(R\in\binom{\Omega}{8}\), at most \(23\) occurrences counted
by (6.2) have union color \(R\):
\[
\boxed{p_R\leq23.}
\tag{6.4}
\]
The constant is sharp for the abstract linear-forest restriction geometry.

#### Proof

Identify a six-subset \(D\subset R\) with the edge
\[
e_D=R\setminus D
\]
of \(K_8\). Two sixsets are Johnson-adjacent exactly when their
corresponding \(K_8\)-edges meet. Thus the restriction of the global
forest to the \(28\) six-subsets of \(R\) is a simple linear-forest
subgraph of the line graph \(L(K_8)\). Here “restriction” does not mean
the graph-theoretically induced subgraph of \(L(K_8)\).

Along one induced path
\[
e_0,e_1,\ldots,e_\ell,
\]
put
\[
a_i=e_{i-1}\cap e_i.
\]
The internal vertex \(e_i\) is nonlazy precisely when
\[
a_i\neq a_{i+1}.
\]
Then
\[
e_i=\{a_i,a_{i+1}\},
\]
so the nonlazy internal vertices, in order, form a trail in \(K_8\).
Lazy centers can be deleted and the neighboring trail pieces spliced at
their common color.

Suppose that \(24\) nonlazy centers exist. Complete the induced forest by
isolated unused vertices. Let
\[
r=\#\{\text{nontrivial induced paths}\},\qquad
t=\#\{\text{isolates}\},\qquad
L=\#\{\text{lazy internal centers}\}.
\]
Since a path with \(v\) vertices has \(v-2\) internal centers,
\[
2r+t+L=4.
\tag{6.5}
\]
There are only two cases.

#### One trail

Here \(r=1\) and \(t+L=2\). Let \(J\) be the four \(K_8\)-edges which are
not nonlazy pivots: the two physical endpoint edges, together with the
isolates and lazy centers. Then
\[
H=K_8\setminus J
\]
has an Euler trail containing all \(24\) of its edges.

Because every \(K_8\)-degree is \(7\),
\[
\deg_H(v)\equiv1+\deg_J(v)\pmod2.
\tag{6.6}
\]
If \(H\) has no odd vertices, all eight \(J\)-degrees are odd. Their sum
is \(8\), so \(J\) is a perfect matching. But the Euler circuit's common
endpoint lies on both distinct physical endpoint edges in \(J\), impossible
for a matching.

If \(H\) has two odd endpoints, those two vertices have positive even
\(J\)-degree, hence degree at least two; the other six have positive odd
\(J\)-degree, hence degree at least one. This would give
\[
\sum_v\deg_J(v)\geq2+2+6=10,
\]
contrary to \(|J|=4\).

#### Two trails

Here \(r=2,t=L=0\), and the four edges of \(J\) are the four physical
path endpoints. For each trail-end occurrence, choose the endpoint vertex
where its physical endpoint edge meets the adjacent retained edge. Let
\(m_v\) be the resulting endpoint multiplicity at \(v\).

If one induced component has two vertices, its retained pivot trail is
empty.  In that case assign both of its trail-end occurrences to the
unique vertex where its two physical endpoint edges meet.  Both assigned
occurrences are incident to their respective edges of \(J\), and their
total parity contribution is zero, so the same two relations below still
hold.

Parity gives
\[
m_v\equiv\deg_H(v)\equiv1+\deg_J(v)\pmod2,
\tag{6.7}
\]
and the endpoint assignment gives
\[
m_v\leq\deg_J(v).
\tag{6.8}
\]
If \(\deg_J(v)=0\), equations (6.7)--(6.8) are impossible. Thus \(J\)
spans all eight vertices and is a perfect matching. Then every
\(\deg_J(v)=1\), so every \(m_v\) must be even and at most one, hence zero.
This contradicts the four trail-end occurrences. The same parity argument
covers every case.

Both cases are impossible, proving \(p_R\leq23\).

For sharpness, take
\[
J=\{12,13,14,56,78\}\subset E(K_8).
\tag{6.9}
\]
Then \(K_8\setminus J\) is connected and Eulerian, with degree four at
vertex \(1\) and degree six elsewhere. Take an Euler circuit based at
\(1\), place \(12\) and \(13\) at its physical ends, and leave
\(14,56,78\) isolated. This is a spanning linear forest in \(L(K_8)\)
with exactly the \(23\) circuit edges as nonlazy centers.
\(\square\)

The local cap alone gives
\[
z_8^{(\leq5)}
\geq
\left\lceil
\frac{330-c-M_7+c_0+\mathcal S_7}{23}
\right\rceil
\geq14.
\tag{6.10}
\]
The next section is substantially stronger.

## 7. Global active-color shadow theorem

Compress each six-path's rank-seven hull-color word into its maximal
constant blocks. A supported rank-seven color is **pivot-active** if one
of its blocks is adjacent to a block of another color.

Let
\[
p=c-c_0
\tag{7.1}
\]
be the number of nonisolated six-path components.

### Lemma 7.1: at least \(314\) distinct pivot-active colors

Let \(z_7=330-M_7\). Then the number \(B_\#\) of distinct pivot-active
rank-seven colors satisfies
\[
\boxed{
B_\#
\geq z_7-p+1
=331-c-M_7+c_0
\geq314.
}
\tag{7.2}
\]

#### Proof

An inactive color can occur only as the sole block of every path word in
which it occurs. Choosing one such word injects inactive colors into the
monochromatic nonisolated path components.

There is at least one nonlazy transition, since (6.3) gives at least
\(313\). Hence at least one nonisolated path word has two or more blocks,
leaving at most \(p-1\) monochromatic path words. Thus at most \(p-1\)
supported colors are inactive, which proves (7.2).
\(\square\)

Every active rank-seven color is a facet of a literal width-at-most-five
rank-eight color arising at an adjacent nonlazy transition.

### Lemma 7.2: upper four-shadow bound for triples

Let
\[
\mathcal F\subseteq\binom{\Omega}{3},
\qquad
|\mathcal F|=s,
\]
and let
\[
\partial^+\mathcal F
=\{Y\in\binom{\Omega}{4}:
\exists T\in\mathcal F,\ T\subset Y\}.
\]
Then
\[
\boxed{
|\partial^+\mathcal F|\leq5s+82.
}
\tag{7.3}
\]

More exactly, let
\[
d_e=\#\{T\in\mathcal F:e\subset T\}
\qquad(e\in\binom{\Omega}{2}),
\]
\[
\Phi
=\sum_e\frac{(d_e-2)(d_e-3)}2\geq0,
\tag{7.4}
\]
and let
\[
n_j
=\#\{Y\in\binom{\Omega}{4}:
\#\{T\in\mathcal F:T\subset Y\}=j\}.
\tag{7.5}
\]
Then
\[
\boxed{
2|\partial^+\mathcal F|
=10s+165-\Phi-n_2-n_3.
}
\tag{7.6}
\]

#### Proof

Put
\[
r_Y=\#\{T\in\mathcal F:T\subset Y\}.
\]
Every triple lies in eight four-sets, so
\[
\sum_Yr_Y=8s.
\tag{7.7}
\]
The overlap loss is
\[
O=\sum_Y(r_Y-1)_+
=8s-|\partial^+\mathcal F|.
\tag{7.8}
\]

Pairs of selected triples whose intersection has size two are counted both
by pair codegrees and by their unique four-set union:
\[
P
:=\sum_e\binom{d_e}{2}
=\sum_Y\binom{r_Y}{2}.
\tag{7.9}
\]
The pointwise identity
\[
\binom d2
=2d-3+\frac{(d-2)(d-3)}2
\]
and
\[
\sum_ed_e=3s
\]
give
\[
P=6s-165+\Phi.
\tag{7.10}
\]
Since \(0\leq r_Y\leq4\),
\[
2O-P=n_2+n_3.
\tag{7.11}
\]
Substitute (7.8) and (7.10) into (7.11) to obtain (7.6). The right side of
(7.6) is at most \(10s+165\), and the left side is even, proving (7.3).
\(\square\)

### Theorem 7.3: forty-seven short rank-eight colors

Let \(\mathcal R_8^{(\leq5)}\) be the set of distinct rank-eight union
colors produced by nonlazy adjacent forest-edge pairs. Then
\[
\boxed{
|\mathcal R_8^{(\leq5)}|
\geq
\left\lceil
\frac{249-c-M_7+c_0}{5}
\right\rceil
\geq47.
}
\tag{7.12}
\]

#### Proof

Complement every \(R\in\mathcal R_8^{(\leq5)}\) to the triple
\[
T=\Omega\setminus R.
\]
Let \(\mathcal F\) be the resulting triple family and put
\[
s=|\mathcal F|.
\]
A rank-seven facet \(Q\subset R\) complements to a four-set
\[
Y=\Omega\setminus Q
\]
containing \(T\). Thus the complements of all pivot-active rank-seven
colors lie in \(\partial^+\mathcal F\). By Lemmas 7.1 and 7.2,
\[
331-c-M_7+c_0
\leq|\partial^+\mathcal F|
\leq5s+82.
\]
Rearrange and use \(c\leq6,M_7\leq11,c_0\geq0\).
\(\square\)

This is the strict quantitative improvement in the present attack:
\[
13\longrightarrow47
\]
for distinct literal rank-eight colors of width at most five.

Put
\[
\tau=(c-c_0)+M_7.
\]
Then (7.12) is
\[
|\mathcal R_8^{(\leq5)}|
\geq\left\lceil\frac{249-\tau}{5}\right\rceil.
\tag{7.12a}
\]
Consequently the lower bound is at least
\[
\begin{array}{c|c}
\tau\text{ range}&|\mathcal R_8^{(\leq5)}|\text{ lower bound}\\ \hline
1\leq\tau\leq3&50\\
4\leq\tau\leq8&49\\
9\leq\tau\leq13&48\\
14\leq\tau\leq17&47.
\end{array}
\tag{7.12b}
\]
In particular, an equality-range \(47\)-color case forces
\[
\tau\geq14
\quad\text{and hence}\quad
M_7\geq8.
\tag{7.12c}
\]

### Near-equality profile at \(s=47\)

If \(s=47\), (7.6) becomes
\[
2|\partial^+\mathcal F|
=635-(\Phi+n_2+n_3).
\tag{7.13}
\]
Since the shadow has size at least \(314\),
\[
\boxed{
\Phi+n_2+n_3\leq7,
\qquad
\Phi+n_2+n_3\ \text{is odd}.
}
\tag{7.14}
\]
Therefore
\[
314\leq|\partial^+\mathcal F|\leq317,
\tag{7.15}
\]
so between \(13\) and \(16\) four-sets are uncovered.

Also, from (7.11),
\[
O=\frac{117+\Phi+n_2+n_3}{2}.
\]
Since \(n_2+2n_3\leq2(\Phi+n_2+n_3)\),
\[
3n_4
=O-n_2-2n_3
\geq
\frac{117-3(\Phi+n_2+n_3)}2
\geq48.
\]
Hence
\[
\boxed{n_4\geq16.}
\tag{7.16}
\]
Any equality-range survivor must therefore produce a highly saturated
upper-four-shadow profile.

More precisely, (7.2) and (7.13) give
\[
\Phi+n_2+n_3\leq2\tau-27.
\tag{7.17}
\]
If \(\tau=14\), parity forces equality
\[
\Phi+n_2+n_3=1.
\]
Here \(|\partial^+\mathcal F|=317\), so the overlap loss is
\(O=8\cdot47-317=59\).  The three possible locations of the single
defect unit are \(\Phi=1\), \(n_2=1\), or \(n_3=1\).  Since
\[
O=n_2+2n_3+3n_4,
\]
the first two possibilities would give respectively
\(3n_4=59\) or \(3n_4=58\), both impossible.  Thus the incidence
equations have the unique solution
\[
\boxed{
\Phi=0,\quad n_0=13,\quad n_1=297,\quad
n_2=0,\quad n_3=1,\quad n_4=19,
\quad |\partial^+\mathcal F|=317.
}
\tag{7.18}
\]
Moreover, \(\Phi=0\) forces every pair codegree to be two or three.
Since their sum is \(3s=141\), exactly \(24\) pair codegrees are two and
\(31\) are three.  The active-color lower bound is also \(317\), so every
member of this upper shadow must be active.  These are necessary
near-equality conditions only; no realization of the profile is asserted.

### Lemma 7.4: the link open-wedge ledger

For a vertex \(i\in\Omega\), let \(L_i\) be the link graph of
\(\mathcal F\) on \(\Omega\setminus\{i\}\):
\[
jk\in E(L_i)
\quad\Longleftrightarrow\quad
\{i,j,k\}\in\mathcal F.
\]
Thus
\[
\deg_{L_i}(j)=d_{ij}.
\]
Let \(t_i\) be the number of triangles of \(L_i\), and define
\[
\delta_i
=\sum_{j\neq i}\binom{d_{ij}}2-3t_i.
\tag{7.19}
\]
Then \(\delta_i\) is exactly the number of induced two-edge paths, or
open wedges, in \(L_i\), and
\[
\boxed{
\sum_i\delta_i=2n_2+3n_3.
}
\tag{7.20}
\]

If a graph has minimum degree at least two, its open-wedge count cannot
equal one.  More generally, a graph with exactly one open wedge is the
disjoint union of one three-vertex path and any number of cliques.  If
the minimum degree is at least two and the open-wedge count is exactly
two, it is the disjoint union of one diamond \(K_4-e\) and any number of
cliques.  If its open-wedge count is zero, it is a disjoint union of cliques.  In
particular, a ten-vertex graph all of whose degrees are two
or three and whose open-wedge count is zero is
\[
K_4\sqcup K_3\sqcup K_3.
\tag{7.21}
\]

#### Proof

At a link vertex \(j\), \(\binom{d_{ij}}2\) counts all pairs of incident
link edges.  A link triangle closes three such wedges, proving the first
claim.  Every four-set of multiplicity three gives one link triangle,
at the vertex opposite its missing triple, and every four-set of
multiplicity four gives four.  Hence
\[
\sum_it_i=n_3+4n_4.
\]
Also
\[
\sum_i\sum_{j\neq i}\binom{d_{ij}}2
=2\sum_e\binom{d_e}2
=2(n_2+3n_3+6n_4).
\]
Subtracting proves (7.20).

For the one-wedge assertion, suppose \(a-v-b\) is the unique induced
two-edge path.  If \(a\) had a neighbor \(z\neq v\), uniqueness would
force \(z\sim v\), then \(z\sim b\), making \(a-z-b\) a second open
wedge.  Thus \(a\), and symmetrically \(b\), has degree one.  The center
\(v\) has no further neighbor, since that neighbor together with \(a\)
would make another wedge.  Hence this component is exactly a
three-vertex path, and every other component has no open wedge and is a
clique.  The minimum-degree-two assertion follows immediately.

For the two-wedge assertion, take an induced path \(a-v-b\) in the
unique noncomplete component and choose \(z\sim a\), \(z\neq v\).  If
\(z\not\sim v\), then \(z-a-v\) is the second wedge.  Choosing a second
neighbor of \(b\) and successively avoiding a third wedge forces it to
be adjacent to \(v,a,z\), whereupon the nonedge \(ab\) creates a third
wedge at that neighbor.  If \(z\sim v\) but \(z\not\sim b\), the two
wedges are \(a-v-b\) and \(z-v-b\); a second neighbor of \(b\) similarly
forces a third.  Hence \(z\) is adjacent to both \(v\) and \(b\), and
\(\{a,v,b,z\}\) induces the diamond with missing edge \(ab\).  Any
further neighbor of a diamond vertex must be adjacent to all of the
other diamond vertices to avoid a new wedge, but then it is a third
common neighbor of the nonadjacent pair \(a,b\).  Thus the component is
exactly the diamond, and every other component is a clique.

Finally, a graph with no induced two-edge path has every connected
component complete.  Components in a degree-two/degree-three graph have
orders three and four, and the unique partition of ten into threes and
fours is \(10=4+3+3\).
\(\square\)

### Theorem 7.5: shadow defects one and three are impossible

Assume \(|\mathcal F|=47\), and put
\[
D=\Phi+n_2+n_3.
\tag{7.22}
\]
Then
\[
\boxed{D\notin\{1,3\}.}
\tag{7.23}
\]

#### Proof: defect one

The case \(D=1\) is exactly (7.18): all pair codegrees are two or three,
there are \(31\) codegree-three pairs, and
\[
n_2=0,\qquad n_3=1.
\]
Let
\[
g_i=\#\{j:d_{ij}=3\}.
\]
Then
\[
\sum_i g_i=2\cdot31=62,
\tag{7.24}
\]
whereas (7.20) gives \(\sum_i\delta_i=3\).  Every link has minimum
degree two, so Lemma 7.4 implies that exactly ten links have defect zero
and the remaining link has defect three.  Each zero-defect link has
\(g_i=4\) by (7.21), while always \(g_i\leq10\).  Therefore
\[
\sum_i g_i\leq10\cdot4+10=50,
\]
contradicting (7.24).

#### Proof: defect three

Now \(D=3\).  Since (7.13) gives
\(|\partial^+\mathcal F|=316\), the overlap loss is \(60\).  The
nonnegative integer solutions of
\[
\Phi+n_2+n_3=3,
\qquad
60=n_2+2n_3+3n_4
\]
are exactly
\[
\begin{array}{c|c|c|c|c}
&\Phi&n_2&n_3&n_4\\ \hline
A&3&0&0&20\\
B&1&1&1&19\\
C&0&3&0&19\\
D&0&0&3&18.
\end{array}
\tag{7.25}
\]

In case A, (7.20) says that every link has zero open-wedge defect.  Thus
every link is a union of cliques.  Equivalently, if two selected triples
share a pair, their four-set is complete; iterating this closure
decomposes \(\mathcal F\) into complete three-graphs on maximal blocks,
any two blocks meeting in at most one vertex.  If the block orders are
\(k\), then
\[
\sum\binom k3=47,
\qquad
\sum\binom k4=20,
\qquad
\sum\binom k2\leq55.
\tag{7.26}
\]
No block has order at least seven.  Solving the first two equations for
orders three through six gives only the following.  Indeed, if \(a_j\)
is the number of order-\(j\) blocks, then
\[
a_4+5a_5+15a_6=20,
\quad
a_3=10a_5+40a_6-33,
\]
whose nonnegative solutions give
\[
4K_5+7K_3,
\qquad
K_6+5K_4+7K_3,
\qquad
K_6+K_5+17K_3.
\tag{7.27}
\]
Their pair totals are respectively \(61,66,76\), contradicting the last
inequality in (7.26).

For later use, whenever all degrees of \(L_i\) are two or three,
handshaking makes \(g_i\) even and
\[
\delta_i=10+2g_i-3t_i.
\tag{7.25a}
\]

In case B, \(\Phi=1\) means that there is a unique exceptional pair,
of codegree one or four; every other pair has codegree two or three.
The nine links away from its endpoints have minimum degree two.  If the
exceptional codegree is one, there are \(32\) codegree-three pairs, so
\[
\sum_i g_i=64.
\]
By (7.20), the total link defect is five.  A positive regular-link defect
is at least two.  At most two regular links can therefore be positive,
while fewer than two would give
\[
\sum_i g_i\leq8\cdot4+10+2\cdot9=60.
\]
With two positive regular links, the only degree-sum possibility not
already below \(64\) has defects two and three, with respectively
\(g_i=8,10\), and both exceptional-endpoint links must have defect zero
and \(g_i=9\).  But such an endpoint link has exactly one degree-one
vertex.  A zero-defect graph is a union of cliques, in which degree-one
vertices occur in pairs as \(K_2\)-components.  This is impossible.

If the exceptional codegree is four, there are \(29\)
codegree-three pairs, so \(\sum_i g_i=58\).  Each exceptional-endpoint
link has one degree-four vertex and all other degrees two or three.  It
cannot have defect zero, since a degree-four vertex in a clique component
would require four other degree-four vertices; it cannot have defect one
by Lemma 7.4.  The two endpoint links therefore consume at least four of
the five defect units, leaving every regular link at defect zero.  Hence
\[
\sum_i g_i\leq9\cdot4+2\cdot9=54<58,
\]
a contradiction.

In cases C and D, \(\Phi=0\), so again all pair codegrees are two or
three and \(\sum_i g_i=62\).  In case C the total link defect is six.
If \(k\) links have positive defect, then \(k\leq3\), while
\[
62=\sum_i g_i
\leq4(11-k)+10k
\]
forces \(k\geq3\).  Thus exactly three links have defect two and
\(g_i=10\).  But for \(g_i=10\),
\[
\delta_i=30-3t_i
\]
is divisible by three, contradiction.

In case D the total link defect is nine, so the number \(k\) of positive
links is three or four.  If \(k=3\), the same degree sum forces all three
to have \(g_i=10\), and divisibility forces each defect to be three.  A
cubic graph on ten vertices cannot have defect three: that would mean
nine triangles.  Without a \(K_4\)-component every vertex lies in at most
two triangles, giving at most six; with a \(K_4\)-component the remaining
cubic graph on six vertices has no \(K_4\)-component and has at most four
triangles, giving at most eight in total.

If \(k=4\), the four positive defects are \(2,2,2,3\).  From
\[
\delta_i\equiv10+2g_i\pmod3
\]
and the evenness of \(g_i\), a defect-two link has \(g_i\leq8\), while a
defect-three link has \(g_i\leq10\).  The degree sum can reach \(62\)
only at \(g_i=8,8,8,10\), so the defect-three link is cubic, again
contradicting the preceding cubic argument.  All four cases in (7.25)
are impossible.
\(\square\)

### Lemma 7.6: a codegree-two/three family has at least \(23\) open wedges

If \(|\mathcal F|=47\) and \(\Phi=0\), then
\[
\boxed{
2n_2+3n_3=\sum_i\delta_i\geq23.
}
\tag{7.27a}
\]

#### Proof

All pair codegrees are two or three.  For any ten-vertex graph whose
degrees are two or three, let \(g\) be the number of degree-three
vertices and \(\delta\) its open-wedge count.  Then
\[
\delta\geq\frac54(g-4).
\tag{7.27b}
\]
For \(g\leq4\) this is immediate.  The handshake lemma makes \(g\) even.
For \(g=6\), (7.25a) gives \(\delta\equiv1\pmod3\), and Lemma 7.4
excludes \(\delta=1\), so \(\delta\geq4\).

For \(g=8\), a violation of (7.27b) would force
\(\delta=2\), hence eight triangles.  If there is no
\(K_4\)-component, a degree-three vertex lies in at most two triangles
and a degree-two vertex in at most one, giving at most six triangles.  If
there is a \(K_4\)-component, the remaining graph has four degree-three
and two degree-two vertices.  A \(K_4\) in a maximum-degree-three graph
is an entire component; a second one would strand two degree-two
vertices, so the remainder has none.  Triangle incidence gives at most
three further triangles, for at most seven total.

For \(g=10\), the graph is cubic.  Without a \(K_4\)-component it has at
most six triangles.  With one \(K_4\)-component, the remaining graph is
cubic on six vertices.  Its complement is two-regular, hence either a
six-cycle or two triangles; the cubic graph has respectively two or zero
triangles.  Thus the original graph has at most six triangles and
\(\delta\geq12\).  This proves (7.27b) in every case.

When \(\Phi=0\), exactly \(31\) of the \(55\) pair codegrees are three,
so \(\sum_i g_i=62\).  Summing (7.27b) over the eleven links gives
\[
\sum_i\delta_i
\geq\frac54(62-44)=\frac{45}{2}.
\]
The left side is integral, proving (7.27a).
\(\square\)

In particular, every physical \(47\)-color survivor has
\[
\boxed{\Phi\geq1.}
\tag{7.27c}
\]
Indeed, otherwise (7.14) would give
\(n_2+n_3=D\leq7\), whence
\(2n_2+3n_3\leq21\), contrary to (7.27a).

### Lemma 7.7: defect five cannot have \(\Phi=1\)

If \(|\mathcal F|=47\) and \(D=5\), then
\[
\boxed{\Phi\neq1.}
\tag{7.27d}
\]

#### Proof

If \(D=5\) and \(\Phi=1\), then
\(n_2+n_3=4\).  The overlap loss is \(61\), so divisibility of
\[
61-n_2-2n_3=3n_4
\]
leaves exactly
\[
(n_2,n_3)=(4,0)
\quad\text{or}\quad
(1,3).
\tag{7.27e}
\]
By (7.20), the corresponding total open-wedge budgets are
\[
W:=\sum_i\delta_i=8
\quad\text{or}\quad11.
\tag{7.27f}
\]

The condition \(\Phi=1\) means that exactly one pair is exceptional, of
codegree one or four; all other pairs have codegree two or three.  Let
its endpoints be \(a,b\).  The other nine links have all degrees two or
three, so (7.27b) gives
\[
\sum_{i\notin\{a,b\}}g_i
\leq36+\frac45
\sum_{i\notin\{a,b\}}\delta_i.
\tag{7.27g}
\]

If the exceptional codegree is one, there are \(32\) codegree-three
pairs, hence \(\sum_i g_i=64\).  Since \(g_a,g_b\leq9\), (7.27g) gives
\[
\sum_i g_i
\leq54+\frac45W.
\]
For \(W=8\) or \(11\), the right side is respectively \(60.4\) or
\(62.8\), both below \(64\).

If the exceptional codegree is four, there are \(29\)
codegree-three pairs, so \(\sum_i g_i=58\).  Each endpoint link has
exactly one degree-four vertex and all other degrees two or three.  It
has neither defect zero nor defect one, by the same clique-component and
minimum-degree arguments used in case B of Theorem 7.5.  Thus
\(\delta_a+\delta_b\geq4\).  Handshaking in either endpoint link also
makes \(g_a,g_b\) even, so each is at most eight.  Equation (7.27g)
therefore gives
\[
\sum_i g_i
\leq36+\frac45(W-4)+16
=48.8+\frac45W.
\]
This is \(55.2\) for \(W=8\) and \(57.6\) for \(W=11\), both below
\(58\).  The two possibilities are impossible.
\(\square\)

### Lemma 7.8: defect five cannot have \(\Phi=4\)

If \(|\mathcal F|=47\) and \(D=5\), then
\[
\boxed{\Phi\neq4.}
\tag{7.27h}
\]

#### Proof

Here \(n_2+n_3=1\), and the overlap congruence forces
\[
n_2=1,
\qquad
n_3=0,
\qquad
n_4=20.
\]
Thus (7.20) gives a total of only
\[
W=\sum_i\delta_i=2
\tag{7.27i}
\]
open wedges.

The nonzero summands in \(\Phi\) are one at pair codegree one or four,
and three at pair codegree zero or five.  Consequently \(\Phi=4\) is
obtained either from four exceptional pairs of the first kind, or from
one pair of each kind.

Call codegrees four and five high.  At an endpoint of a high pair, the
link contains fewer than five degree-four vertices and fewer than six
degree-five vertices.  It therefore cannot be a union of cliques, and it
cannot be a three-vertex path plus cliques.  Lemma 7.4 gives link defect
at least two.  Since a high pair has two endpoints, (7.27i) excludes all
high pairs.

The one-plus-three decomposition would now consist of one codegree-zero
pair and one codegree-one pair.  Each endpoint of the latter has exactly
one degree-one vertex in its link.  Both a zero-defect union of cliques
and a one-defect three-vertex-path-plus-cliques graph have an even number
of degree-one vertices.  Each endpoint would have defect at least two,
again contradicting (7.27i).

It remains that all four exceptional pairs have codegree one.  If a
vertex is incident with an odd number of these pairs, its link has an odd
number of degree-one vertices and hence defect at least two.  The number
of odd-degree vertices in the four-edge exceptional graph is even, so
(7.27i) forces all its degrees to be even.  The exceptional graph is
therefore a four-cycle.

The other \(51\) pair codegrees are two or three.  Their total forces
exactly \(35\) codegree-three pairs, so
\[
\sum_i g_i=70.
\]
At each of the four cycle vertices, \(g_i\leq8\).  The remaining seven
links have all degrees two or three, so (7.27b) gives
\[
\sum_i g_i
\leq4\cdot8+7\cdot4+\frac45W
=61.6<70,
\]
the final contradiction.
\(\square\)

### Lemma 7.9: defect five cannot have \(\Phi=3\)

If \(|\mathcal F|=47\) and \(D=5\), then
\[
\boxed{\Phi\neq3.}
\tag{7.27j}
\]

#### Proof

The profile is
\[
n_2=0,
\qquad
n_3=2,
\qquad
n_4=19,
\qquad
W:=\sum_i\delta_i=6.
\tag{7.27k}
\]
The defect \(\Phi=3\) is supplied either by one exceptional pair of
codegree zero or five, or by three exceptional pairs of codegree one or
four.

For one codegree-zero pair, the other pair codegrees force \(33\)
codegree-three pairs and \(\sum_i g_i=66\).  The nine regular links and
the two endpoint bounds give
\[
\sum_i g_i
\leq9\cdot4+\frac45W+2\cdot9
=58.8<66.
\]
For one codegree-five pair, there are \(28\) codegree-three pairs and
\(\sum_i g_i=56\).  Each endpoint link has a unique degree-five vertex,
so it has defect at least two; hence the regular links receive at most
two defect units.  Therefore
\[
\sum_i g_i
\leq36+\frac45\cdot2+18
=55.6<56.
\]

It remains to consider three codegree-one/codegree-four pairs.  Let \(h\)
be the number having codegree four.  Then the number of codegree-three
pairs is \(34-3h\), so
\[
\sum_i g_i=68-6h.
\tag{7.27l}
\]

If \(h=0\), a vertex incident with an odd number of exceptional pairs has
link defect at least two, because both zero- and one-wedge graphs have an
even number of degree-one vertices.  The three-edge exceptional graph
therefore has at most two odd-degree vertices.  It is either a triangle
or a four-vertex path.  In the triangle case, the three exceptional
vertices contribute at most \(3\cdot8\), and the eight regular links give
at most \(8\cdot4+\frac45W\), for a total at most \(60.8<68\).  In the
path case the four exceptional vertices contribute at most
\(9+8+8+9=34\), and the seven regular links give at most
\(28+\frac45W\), for a total at most \(66.8<68\).

Suppose \(h=1\).  The two endpoints of the codegree-four pair each have
defect at least two.  The two codegree-one pairs cannot be disjoint,
because their four odd endpoints would force total defect at least eight.
They form a two-edge path.  If both odd endpoints are the two high-pair
endpoints, the three exceptional vertices contribute at most \(24\),
while the eight regular links receive at most two further defect units;
the total is at most
\[
24+32+\frac85=57.6<62.
\]
If neither odd endpoint is high, the two high endpoints and two distinct
odd low endpoints are four forced-positive links and already cost at
least eight defect units, impossible.
If exactly one odd endpoint is high, the path center is distinct from
both high endpoints, since no pair can have two codegrees.  The four
exceptional vertices contribute at most
\[
8+8+9+8=33;
\]
the three forced positive links consume all six defect units, so the
seven regular links contribute \(28\).  The total is at most
\(61<62\).

If \(h=2\), the two high pairs must meet, since four high endpoints would
already use eight defect units.  Their three endpoints consume all six
units.  The low pair must join the two outer endpoints, or it would force
a new positive link.  At an outer endpoint the anomalous degrees one and
four make \(g_i\) odd and at most seven; at the common endpoint the two
degree-four anomalies give \(g_i\leq8\).  Thus
\[
\sum_i g_i\leq7+8+7+8\cdot4=54<56.
\]

Finally let \(h=3\).  The three high pairs must form a triangle, every
exceptional link has defect two, and all eight regular links have defect
zero.  At an exceptional link,
\[
2=20+2g_i-3t_i.
\]
Thus \(g_i\equiv0\pmod3\); handshaking makes \(g_i\) even, and
\(g_i\leq8\), so \(g_i\in\{0,6\}\).  Equation (7.27l) requires their
sum to be \(18\), hence every exceptional link has \(g_i=6\).  Such a
link has degree multiset
\[
4,4,3,3,3,3,3,3,2,2
\]
and exactly two open wedges.  By Lemma 7.4 it is a diamond plus clique
components.  Its two degree-four vertices would have to lie in
\(K_5\)-components, in which degree-four vertices occur in multiples of
five, a contradiction.
\(\square\)

### Lemma 7.10: defect five cannot have \(\Phi=2\)

If \(|\mathcal F|=47\) and \(D=5\), then
\[
\boxed{\Phi\neq2.}
\tag{7.27m}
\]

#### Proof

The unique profile is
\[
n_2=2,
\qquad
n_3=1,
\qquad
n_4=19,
\qquad
W=2n_2+3n_3=7.
\tag{7.27n}
\]
There are exactly two exceptional pairs, each of codegree one or four.
Let \(h\in\{0,1,2\}\) count those of codegree four.  The numbers of
codegree-three pairs are respectively \(33,30,27\), so
\[
\sum_i g_i=66,60,54.
\tag{7.27o}
\]

If \(h=0\), disjoint exceptional pairs have four odd endpoints and force
at least eight open wedges.  The pairs must therefore meet.  Their three
vertices contribute at most \(9+8+9=26\), while the eight regular links
give at most \(32+\frac45W\).  Hence
\[
\sum_i g_i\leq63.6<66.
\]

If \(h=1\), disjoint exceptional pairs again force at least eight defect
units: two from each high endpoint and two from each odd low endpoint.
When they meet, the common endpoint has one degree-one and one
degree-four anomaly, the other high endpoint has one degree-four anomaly,
and the other low endpoint has one degree-one anomaly.  Their \(g_i\)'s
are at most \(7,8,9\), respectively.  These three links consume at least
six units, leaving no positive regular link because a regular positive
defect is at least two.  Thus
\[
\sum_i g_i\leq7+8+9+8\cdot4=56<60.
\]

If \(h=2\), the high pairs must meet.  Their three endpoint links have
positive defects summing to seven, hence the multiset \(2,2,3\), and all
eight regular links have defect zero.  At the common endpoint
\[
\delta_i=20+2g_i-3t_i,
\]
while at either outer endpoint
\[
\delta_i=15+2g_i-3t_i.
\]
All three \(g_i\) are even.  If the defect-three link is common, the
three \(g_i\)'s are at most \(8,4,4\); if it is outer, they are at most
\(6,6,4\).  In either case their sum is at most \(16\).  Consequently
\[
\sum_i g_i\leq16+8\cdot4=48<54.
\]
All cases are impossible.
\(\square\)

### Corollary 7.11: strengthened forty-seven-color gate

If the short rank-eight support has size \(47\), then
\[
\boxed{
D=7,
\qquad
\Phi\geq1,
\qquad
\tau=(c-c_0)+M_7=17,
\qquad
M_7=11,
\qquad
c=6,
\qquad
c_0=0.
}
\tag{7.28}
\]
Indeed, \(D\) is odd and at most seven.  Theorem 7.5 excludes one and
three; Lemmas 7.6--7.10 exclude all defect-five profiles.  Thus \(D=7\).
Equation (7.17) gives \(\tau\geq17\), while
\(c-c_0\leq6\) and \(M_7\leq11\) give the reverse inequality.  Equality
forces \(M_7=11\), \(c-c_0=6\), and hence \(c=6,c_0=0\).

Thus (7.12b) sharpens to
\[
\boxed{
\begin{array}{c|c}
\tau\text{ range}&|\mathcal R_8^{(\leq5)}|\text{ lower bound}\\ \hline
1\leq\tau\leq3&50\\
4\leq\tau\leq8&49\\
9\leq\tau\leq16&48\\
\tau=17&47.
\end{array}
}
\tag{7.29}
\]
In the \(47\)-color case the upper shadow has size \(314\), exactly the
active-color lower bound, so every shadow member is active.

There is also an equality structure on the six-path forest.  Here
\(z_7=319\), while exactly \(314\) supported colors are active.  Equality
in Lemma 7.1 forces five of the six nonisolated components to have
monochromatic hull-color words, in five distinct inactive colors, and the
remaining component to contain all \(314\) active colors.  Since a
rank-seven color has multiplicity at most six, the five monochromatic
components contain at most \(30\) forest edges in total.  The remaining
component therefore contains at least
\[
456-30=426
\tag{7.30}
\]
edges, and hence at least \(427\) six-set vertices.  Every nonlazy
rank-eight transition lies on this single component.

## 8. Duplicate and interface supplements

### 8.1 Exact interface gluing

Split the hull-color occurrences into central-core and outer
(interface plus external-headed) category words. Let
\[
\mathcal A_C,\mathcal S_C,
\qquad
\mathcal A_O,\mathcal S_O
\]
be their lazy and separated-return excesses, and put
\[
o_{CO}
=|\operatorname{supp}C\cap\operatorname{supp}O|.
\]
Let \(N_O\) be the number of outer occurrences,
\(z_O=|\operatorname{supp}O|\), and
\[
D_O=N_O-z_O=\mathcal A_O+\mathcal S_O.
\]
Let
\[
a=|\operatorname{supp}O\setminus\operatorname{supp}C|,
\]
the number of colors first introduced outside the central core.  If
\(m_{\rm glue}\) of the at most \(d\) actual category boundaries have
equal adjacent colors, then
\[
\boxed{
\mathcal A_7
=\mathcal A_C+\mathcal A_O+m_{\rm glue},
}
\tag{8.1}
\]
\[
\boxed{
\mathcal S_7
=\mathcal S_C+\mathcal S_O+o_{CO}-m_{\rm glue},
\qquad
0\leq m_{\rm glue}\leq d.
}
\tag{8.2}
\]
One overlap color can glue both interfaces, so the false inequality
\(m_{\rm glue}\leq o_{CO}\) must not be used. The safe consequence is
\[
\boxed{
\mathcal S_7
\geq
\max\{0,\mathcal S_C+\mathcal S_O+o_{CO}-d\}.
}
\tag{8.3}
\]

If
\[
\Lambda=\sum_Y(5-V_Y)_+,
\]
then the internal outer duplicate excess obeys
\[
D_O\leq\Lambda+d.
\tag{8.4}
\]
Indeed, the outer multiplicity of row \(Y\) is \(x_Y+\rho_Y\), and
\[
(x_Y+\rho_Y-1)_+
\leq(x_Y-1)_++\rho_Y
\leq(5-V_Y)_++\rho_Y.
\]
Sum over \(Y\) and use \(\sum_Y\rho_Y=d\).
Since
\[
N_O-a=D_O+o_{CO},
\]
equations (8.3)--(8.4) give
\[
\boxed{
\mathcal S_7
\geq
\max\{0,N_O-a-\Lambda-2d\}.
}
\tag{8.5}
\]
Here the last implication uses
\(\mathcal A_O\leq D_O\leq\Lambda+d\) in (8.3).
Substituting (8.5) into (6.2) gives a conditional strengthening of the
rank-eight occurrence count, but no uniform improvement beyond (7.12).

### 8.2 Duplicate concentration

For a coordinate \(x\), put
\[
D_x^{(1)}
=\sum_{Q\ni x}(t_Q-1)_+.
\]
Since every rank-seven color contains seven coordinates,
\[
\sum_xD_x^{(1)}=7\Delta_7.
\]
Therefore some coordinate satisfies
\[
\boxed{
D_x^{(1)}
\geq
\left\lceil\frac{7\Delta_7}{11}\right\rceil
\geq81.
}
\tag{8.6}
\]
A repeated color contributes at most five, so this coordinate belongs to
at least
\[
\boxed{17}
\tag{8.7}
\]
distinct repeated rank-seven colors.

Similarly, for coordinate pairs,
\[
\sum_{\{x,y\}}
\sum_{Q\supseteq\{x,y\}}(t_Q-1)_+
=21\Delta_7.
\]
Some pair has duplicate incidence at least
\[
\boxed{
\left\lceil\frac{21\Delta_7}{55}\right\rceil
\geq49,
}
\tag{8.8}
\]
and hence lies in at least
\[
\boxed{10}
\tag{8.9}
\]
distinct repeated rank-seven colors.

These improve the previous existence statements, but they do not identify
the same coordinate or pair as a bottleneck in (3.19).

## 9. Exact slack barriers

The new inequalities do not contradict one another.

1. **Orthogonality Hall is support-exact.**  
   Equation (3.3) displays all its slack. For a singleton it is precisely
   the external-headed duplicate excess. Uniform coordinate summation
   reduces to the tautology that the number of externally used colors is
   at most \(R_{\rm ext}\).

2. **Source saturation has zero scalar forcing.**  
   The exact moment is
   \[
   \sum_Ya_Y=10q\leq3300.
   \]
   Assigning \(a_Y=10\) at \(q=330\), or distributing the smaller total
   below \(15\) for \(q<330\), makes every term in \(L_{\rm src}\) vanish.
   A contradiction needs a nonuniform joint-run theorem forcing many
   \(a_Y\)'s above \(15\).

3. **The incidence profile is arithmetically feasible.**  
   At \(E=132,s_{\rm ext}=6,q=330\), the degree profile
   \[
   178\text{ targets of degree }3,
   \qquad
   152\text{ targets of degree }6
   \]
   has total
   \[
   178\cdot3+152\cdot6=1446.
   \]
   It attains (5.11) at the scalar level. This is not a common-word
   construction, but it prevents a degree-sum contradiction.

4. **The rank-eight shadow remains feasible.**  
   The bound \(47\) is far below
   \(\binom{11}{8}=165\). At equality it now forces the unique parameter
   corner \(D=7,\tau=17,M_7=11,c=6,c_0=0\), the one-long/five-short
   forest structure (7.30), and a \(314\)-element upper shadow all of
   whose members are active.  That corner has not been excluded.

Thus the exact remaining gate is a correlation theorem:

> prove that the same physical central word and external directed forest
> cannot simultaneously keep every source surplus \(a_Y\leq15\), realize
> the five-row directed capacities (4.24)--(4.31) and the high
> central-incidence load (5.3), absorb the singleton inequality (3.19),
> and realize the extremal upper-four-shadow and one-long-component
> structure in (7.28)--(7.30).

No such theorem is proved here.

## 10. Strongest fifth-wave theorem

### Theorem M5-K11

Every hypothetical length-\(465\) zero-margin survivor induces an integral
system satisfying all of the following.

1. For every nonempty \(Z\subseteq\Omega\), the orthogonality Hall cut
   \[
   A_Z^{\rm ext}+s_Z^{\rm h}+P_Z\leq R_{\rm ext},
   \]
   its pair-saturated form (3.9), and its exact slack identity (3.3).

2. For every coordinate \(x\), the path-restored inequality
   \[
   A_x^{\rm ext}+s_x^{\rm h}+2\omega_x
   \leq E-(s_{\rm ext}-\nu_x)-\sigma_x
   \leq E,
   \]
   and the low-entry form (3.19).

3. The five-row lift of the directed complement flags satisfies the
   rowwise incidence-capacity system (4.24), its global consequence
   \[
   \sum_Y\mathfrak h_{7-V_Y}(21-U_Y)
   \geq10E-5c+5b_H-5d,
   \]
   and every subset projection (4.29), including the singleton fusion
   (4.30)--(4.31).

4. For every four-set \(Y\), the correlated source/facet/interface cap
   \[
   x_Y\leq
   \min\{(6-V_Y)_+,\ 21-U_Y,\ 7-V_Y-\rho_Y\},
   \]
   with
   \[
   U_Y=V_Y+a_Y,\qquad
   \sum_Ya_Y=10q,
   \]
   and the global inequality
   \[
   \sum_Y(a_Y-15)_+
   \leq4E-330+c+d-b_H+N_7^\star.
   \]

5. The strengthened central incidence bound
   \[
   K\geq2772-10E-c+b_H-d,
   \]
   including the numerical consequences (5.11)--(5.13).

6. The exact local short-rank-eight multiplicity cap
   \[
   p_R\leq23,
   \]
   and the global support theorem
   \[
   \boxed{
   z_8^{(\leq5)}\geq47.
   }
   \]
   Moreover, (7.28)--(7.29) hold: if the support is \(47\), then its
   shadow defect is seven, \(\Phi\geq1\), and necessarily
   \(c=6,c_0=0,M_7=11\); the forest equality structure (7.30) also
   holds.

7. A coordinate in at least \(17\), and a coordinate pair in at least
   \(10\), distinct repeated rank-seven colors.

Items 1--5 are new necessary conditions on a length-\(465\) survivor.
Item 6 is the strict finite lower-bound improvement. None excludes the
survivor, so the interval for \(\nu(11)\) is unchanged.

## 11. Audit

The decisive steps were independently rederived.

1. **External-incidence audit.**  
   The \(E\) matching incidences and \(R_{\rm ext}\) nonmatching
   path incidences have distinct sources. Interfaces are cross-block
   incidences and are not silently counted in \(I_{EE}\). This gives the
   exact constant \(2772-10E-c+b_H-d\).

2. **Source-capacity audit.**  
   The identity
   \[
   U_Y=V_Y+r_Y^{(3)}-\chi_Y
   \]
   and the cap
   \[
   \min\{(6-V_Y)_+,21-U_Y\}
   =(6-V_Y)_+-(a_Y-15)_+
   \]
   hold also at \(V_Y=7\), where \(U_Y\leq21\) forces the correction to
   vanish.

3. **Five-row flag-lift audit.**  
   A nonmatching incidence from an external-headed flag lifts to the
   complement rows
   \[
   Y_p,\qquad (Y_p\setminus\{z\})\cup\{\xi_p\}\quad(z\in Y_p).
   \]
   The exact \(K_7\) extremum is (4.22), and the matching and directed
   incidences are pairwise distinct.  This independently reproduces
   (4.24), the constant \(10E-5s_{\rm ext}\), and the factor four in the
   singleton projection (4.30).

4. **Path-sign audit.**  
   With \(\sigma_x\) at starts and \(\nu_x\) at terminals,
   \[
   \nu_x-\sigma_x=\text{gains}-\text{losses},
   \]
   so
   \[
   P_x=2\omega_x+\sigma_x-\nu_x.
   \]
   The sign and the absence of an extra interface term were checked
   independently.

5. **Rank-eight local audit.**  
   The equation
   \[
   2r+t+L=4
   \]
   exhausts every possible linear-forest restriction shape with \(24\)
   nonlazy centers. The one-trail and two-trail parity arguments both
   fail. The five-edge example (6.9) realizes \(23\), proving sharpness at
   the abstract local level.

6. **Shadow audit.**  
   The exact identity
   \[
   2|\partial^+\mathcal F|
   =10|\mathcal F|+165-\Phi-n_2-n_3
   \]
   follows independently from pair codegrees and four-set multiplicities.
   Together with at least \(314\) active colors, it gives \(47\), with no
   rounding ambiguity.  The link identity
   \[
   \sum_i\delta_i=2n_2+3n_3
   \]
   was then audited case by case.  It excludes defects one and three,
   proves the \(23\)-open-wedge bound when \(\Phi=0\), and excludes all
   defect-five profiles.  Thus every \(47\)-color survivor obeys the
   exact extremal restrictions (7.28)--(7.30).

The only unproved step is the final correlation gate in Section 9.
