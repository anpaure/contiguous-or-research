# Audit of the multidepth suffix dual: the full-cube threshold is (64/11), not (16/3)

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The persistent-suffix mechanism is real.  For every retained scale-(s)
rectangle, (s\in\{r,r+1\}), and every (q\ge s), one isolated suffix
arm has both endpoints in the canonical over-cap set.  The fixed-depth
double-boundary interaction count is also

\[
                         J_q=O(W/r^3).
\]

There is, however, a decisive quantifier error in
`MATH_OBSTRUCTION_MSW_TWO_SCALE_MULTIDEPTH_DRAIN_20260726.md`.  That note
keeps only

\[
                 L\sim {D_r\over4}
\]

of the available bits, where (D_r) is the certified canonical defect.
It then proves that this deliberately tuned subcube is insufficient after
one of the four arms is lost.  The full compatible two-scale cube has
(M_r+\widetilde M_{r+1}>L) variables.  Those extra variables cannot be
discarded in a no-go theorem: adding legal variables can only enlarge the
set of reachable factors.

The correct statewise full-cube inequality is

\[
\boxed{
 (K_{q,p}(F_x)-(W-N_q))_+
 \ge
 \left[D_r-(W-N_q)-3(M_r+\widetilde M_{r+1})
             -O(W/r^3)\right]_+.}
\tag{0.1}
\]

Writing (t=\operatorname {Cat}_r/p), this gives an aggregate obstruction
only for

\[
\boxed{
 t>\tau_{m,r}:=
 \left[{1\over2}-3\rho_{m,r}(1+x_{m,r})\right]^{-1}
 ={64\over11}+O(r^{-1}+r/m),}
\tag{0.2}
\]

not for (t>16/3+o(1)).  In the sector

\[
                 {16\over3}<t\le {64\over11}+o(1)
\]

the tuned subcube is obstructed but the full two-scale cube is not.

The second marked arm at the self-depth does **not** presently propagate:
its destination preload comes from the opposite boundary alignment.  Thus
the valid multidepth bound is three useful arms per bit, not two.

Finally, the suffix dual cannot be extended indiscriminately to more
scales.  If (a) is the least index with

\[
                      \operatorname {Cat}_a>p,
\]

then the persistent dead-arm proof applies only to scales (s\ge a+1).
At scale (a), the certified destination preload
(\operatorname {Cat}_{a-1}) is at most (p).  This first sub-cap scale
escapes the dual.  Here (a\in\{r-2,r-1\}), so adding one or two lower
scales removes the scalar-capacity obstruction, although a compatible
multiscale exact cube is still unproved.

## 1. The one persistent suffix arm is valid

Let a scale-(s) parent context be fixed.  In the omitted-label
normalization, its common tail consists of the local Catalan filling,
followed by the exterior symbols.  Put

\[
 \ell_q=m-q-1,
 \qquad A_{C,q}=\operatorname {suf}_{\ell_q}(\mathsf O_C).
\]

For (q=s), one fixed suffix arm has endpoints

\[
 S_{C,s}=A_{C,s}\cup\{\beta_C\},
 \qquad T_{C,s}=A_{C,s}\cup\{\gamma_C\}.
\]

The (\operatorname {Cat}_s) rows (10v), (v\in\mathcal D_s), give
distinct canonical occurrences at (S_{C,s}).  The
(\operatorname {Cat}_{s-1}) rows (1100R),
(R\in\mathcal D_{s-1}), give distinct canonical occurrences at
(T_{C,s}).  Since (q\ge s), one has
(\ell_q\le m-s-1), so (A_{C,q}) lies wholly in the common exterior
tail.  Keeping the same boundary window and shortening this suffix sends
the preceding row occurrences injectively to (S_{C,q}) and (T_{C,q}).
Therefore

\[
 \boxed{
 \mu_q^{\rm MSW}(S_{C,q})\ge\operatorname {Cat}_s,
 \qquad
 \mu_q^{\rm MSW}(T_{C,q})\ge\operatorname {Cat}_{s-1}.}
\tag{1.1}
\]

If (r) is minimal with (\operatorname {Cat}_r\ge4p), then, for
(s=r,r+1), both numbers in (1.1) exceed (p).  Hence for

\[
 \alpha_q=\mathbf1_{\{S:\mu_q^{\rm MSW}(S)>p\}},
\]

this arm has zero (\alpha_q)-action.  The other three unit arms have
action at most one each, and consequently every isolated retained column
satisfies

\[
             \alpha_q(N_{q,e})-\alpha_q(P_{q,e})\le3.
\tag{1.2}
\]

This is an occurrence injection, not an average-load assertion.

## 2. Why the second self-depth arm does not propagate

At (q=s), the two occurrence-level marked moves are

\[
                    2\longrightarrow4,
 \qquad             4\longrightarrow3.
\]

All three canonical targets have loads

\[
 \operatorname {Cat}_s,
 \quad \operatorname {Cat}_{s-1},
 \quad \operatorname {Cat}_{s-1},
\]

so both marked moves are cap-neutral at the self-depth.  Their preload
certificates have different geometry, however.

* The preload at (4) used by the (2\to4) move comes from the
  (1100R) rows on the **same** boundary alignment.  It survives suffix
  shortening, as in Section 1.
* The preload at (3) used by the (4\to3) move comes from the rows
  (D_R=101R0) on the **opposite** boundary alignment: in Lemma 15.2A it
  is the odd window on phases (0,\ldots,s-1), whereas the moved (A_R)
  window is the even window on phases (1,\ldots,s).

For (q>s), these one-phase-shifted windows peel different exterior
parity flags.  Thus the (D_R) occurrences do not inject into the new
(A_R) endpoint.  A second persistent arm would require a new identity
equating those shifted exterior flags.  None of the current prefix/suffix
formulas supplies it.  Hence the self-depth two-arm theorem cannot be
used to replace (1.2) by a bound of two.

## 3. A bivariate fixed-displacement proof of (J_q=O(W/r^3))

Put

\[
 C(z)=1+zC(z)^2,
 \qquad A(z)=zC(z),
 \qquad U(z)={1\over1-2A(z)}=A'(z).
\]

For one LCA-to-marked-node branch, mark by (x) the root nodes and sibling
subtrees on the complementary cyclic arc, and by (y) those on the phase
arc between the two marked blocks.  One context frame contributes either
(A(x)) or (A(y)), so the exact branch series is

\[
                         V(x,y)={1\over1-A(x)-A(y)}.
\tag{3.1}
\]

For two incomparable marked recursion blocks, the root-to-LCA context
contributes (U(x)) and the two LCA branches contribute (V(x,y)^2).
The LCA itself, the boundary orientations, and the fixed offsets inside
the local switch blocks change this by only finitely many monomials.  It
therefore suffices to bound

\[
                         [x^a y^j]U(x)V(x,y)^2,
\tag{3.2}
\]

where the prescribed phase displacement fixes (j) up to (O(1)), and

\[
                         a=m-s-t-j+O(1).
\]

For (q\le m/2), one has (a=\Omega(m)).  Expanding gives

\[
 V(x,y)^2
 =\sum_{b\ge0}(b+1)A(y)^b C(x)^{b+2}.
\tag{3.3}
\]

There are exact coefficient formulas

\[
\begin{aligned}
 X_{a,b}:=[x^a]U(x)C(x)^{b+2}
 &= {a+1\over2a+b+3}
       \binom{2a+b+3}{a+1},\\
 Y_{j,b}:=[y^j]A(y)^b
 &= {b\over j}\binom{2j-b-1}{j-b}
 \qquad(b\ge1).
\end{aligned}
\tag{3.4}
\]

The first uses (U=A') and

\[
 U C^{b+2}=A'C^{b+2}
 ={1\over b+1}(C^{b+1})',
\]

while the second is Lagrange inversion for (A=z/(1-A)).  Uniform
binomial estimates give, for (1\le b\le j\le a),

\[
\begin{aligned}
 X_{a,b}
 &\le C\,{4^a2^b\over\sqrt a}e^{-c b^2/a},\\
 Y_{j,b}
 &\le C\,{4^j2^{-b}b\over j^{3/2}}e^{-c b^2/j}.
\end{aligned}
\tag{3.5}
\]

Consequently

\[
\begin{aligned}
 [x^a y^j]UV^2
 &=\sum_{b=0}^j(b+1)X_{a,b}Y_{j,b}\\
 &\le C{4^{a+j}\over\sqrt a\,j^{3/2}}
       \sum_{b\ge1}b^2e^{-cb^2/j}\\
 &\le C{4^{a+j}\over\sqrt a}.
\end{aligned}
\tag{3.6}
\]

The case (j=0) is absorbed into the same bound.  Multiplying by the two
local filling counts gives

\[
 J_q^{s,t}
 \le C{4^{m-s-t}\over\sqrt m}
       \operatorname {Cat}_{s-1}\operatorname {Cat}_{t-1}
 \le {C'W\over(st)^{3/2}}.
\tag{3.7}
\]

Adjacent-scale pruning removes the only nested pair, and equal-scale
nodes cannot be nested.  Summing the four ordered scale pairs gives

\[
                         \boxed{J_q\le CW/r^3.}
\tag{3.8}
\]

For one double-boundary window, the mixed difference has two positive and
two negative unit terms, so its pairing with any (0\le\alpha\le1) has
absolute value at most two.  Therefore

\[
             |\langle\alpha_q,\mathcal R_q(x)\rangle|
                       \le2J_q.
\tag{3.9}
\]

Fixing (q) fixes the (y)-degree.  Summing all displacements would remove
that restriction and restore an extra factor of order (m).

## 4. The correct full-cube theorem

Put

\[
 d=\operatorname {Cat}_r,
 \qquad D_r=H_{m,r}(d/2-p),
 \qquad c_q=W-N_q.
\]

Let (x) be any state of the full compatible pruned cube

\[
                   \mathcal E_r\dot\cup
                   \widetilde{\mathcal E}_{r+1}.
\]

The canonical plateau theorem gives (K_{q,p}(F_{\rm MSW})\ge D_r).
Equations (1.2) and (3.9) give

\[
\begin{aligned}
 K_{q,p}(F_x)
 &\ge \langle\alpha_q,\mu_q^x-p\mathbf1\rangle\\
 &\ge D_r-3|x|-2J_q\\
 &\ge D_r-3(M_r+\widetilde M_{r+1})-CW/r^3.
\end{aligned}
\tag{4.1}
\]

Subtracting (c_q) proves (0.1).

Let

\[
 \rho_{m,r}={M_r\over H_{m,r}d}
 ={(k+1)(r+1)\over4(2k+1)(2r-1)},
 \quad k=m-r-1,
\]

and

\[
 x_{m,r}={\widetilde M_{r+1}\over M_r}
 ={3k(r-1)\over2(2k-1)(r+1)}.
\]

After division by (H_{m,r}d), the main part of (4.1) is

\[
 \boxed{
 {1\over2}-{1\over t}
       -3\rho_{m,r}(1+x_{m,r}).}
\tag{4.2}

Since

\[
 3\rho_{m,r}(1+x_{m,r})
 ={21\over64}+O(r^{-1}+r/m),
\]

the threshold is (0.2).  If (t\ge64/11+\varepsilon),
(q\in[r+1,H]), (H=\Theta(p^{1/4})), then (c_H=o(D_r)) and

\[
 (K_{q,p}(F_x)-c_q)_+
       \ge c_\varepsilon {W\over r^{3/2}}.
\]

Summing (\Theta(p^{1/4})) depths gives

\[
 \operatorname {PCap}_{[r+1,H]}(F_x)
 \ge
 \Omega_\varepsilon\left(
     {Wp^{1/4}\over(\log p)^{3/2}}
                         \right)\gg W.
\tag{4.3}

This is a valid full-cube no-go in the upper Catalan-overshoot sector.

## 5. Exact comparison with the tuned subcube

If one first retains only

\[
                         L=\lfloor(D_r-c_H)/4\rfloor
\]

variables, then (4.1) yields

\[
       (K_{q,p}-c_q)_+\ge L-O(W/r^3).
\]

That statement is correct for that subcube.  It cannot be promoted to the
full cube because

\[
 M_r+\widetilde M_{r+1}>L
\]

through a substantial part of the overshoot interval.  Retuning the
catalogue after discovering a three-arm rather than four-arm capacity
means retaining about (D_r/3) variables, when available.  This is exactly
what changes (16/3) to (64/11).

## 6. Lower scales and why a many-scale extension is not automatic

Let

\[
 R_j={\operatorname {Cat}_j\over\operatorname {Cat}_{j-1}}
     ={2(2j-1)\over j+1}.
\]

The persistent-arm proof at scale (s) requires

\[
                    \operatorname {Cat}_{s-1}>p.
\tag{6.1}

Let (a) be least with (\operatorname {Cat}_a>p).  Since
(\operatorname {Cat}_{r-1}>p) and
(\operatorname {Cat}_{r-3}<p), one has

\[
                         a\in\{r-2,r-1\}.
\tag{6.2}

More explicitly,

\[
 a=r-1
 \quad\Longleftrightarrow\quad
 t\le R_rR_{r-1};
\]

otherwise (a=r-2).  At scale (a), the positive endpoint certificate
is only (\operatorname {Cat}_{a-1}\le p), so the fixed-cut argument no
longer loses one arm.

For reference, the pruned pair of scales (r-1,r), granting four arms to
scale (r-1) and three to scale (r), has normalized oriented capacity

\[
 {\rho_{m,r}\over\sigma_{m,r-1}}
        (4+3x_{m,r-1})
 ={25\over64}+O(r^{-1}+r/m),
\]

where (\sigma_{m,r-1}=M_r/M_{r-1}).  Its corresponding obstruction
threshold is

\[
                         {64\over7}+O(r^{-1}+r/m).
\tag{6.3}

Thus merely shifting the two-scale window down improves, but does not
cover, the entire interval (4\le t<16).

On the other hand, if the first sub-cap scale (a) could be added
compatibly to the (r,r+1) cube without a constant loss, its possible
four-arm contribution together with the two three-arm catalogues exceeds
the maximal normalized demand (7/16).  Likewise an additional full
scale (r+2) would erase the present scalar dual once enough of its
catalogue survives.  These are capacity statements only: adjacent and
nonadjacent three-scale physical compatibility has not been proved.

Consequently an assertion that the obstruction persists for
(k=o(r^{3/4})) scales is false without an additional hypothesis fixing
the *total number of retained variables* near (D_r/4).  The interaction
error remains small for several scales, but the isolated three- or
four-arm supply grows linearly with the number of retained catalogues and
eventually dominates the fixed canonical defect.

## 7. Correct scope

What is proved:

1. one suffix arm is coherently dead at every (q\ge s);
2. fixed-depth nonlinear rescues are (O(W/r^3));
3. the full pruned (r,r+1) cube has an aggregate PCap obstruction for
   (t>64/11+o(1)).

What is not proved:

1. a second persistent dead arm;
2. a no-go for the full two-scale cube down to (t>16/3);
3. a no-go after adding the first sub-cap scale;
4. a no-go for an arbitrary growing collection of scales.

The remaining middle overshoot sector is therefore a genuine open
interlacing/orientation problem, not a consequence of the present dual.
