The compact balanced three-box theorem remains open. The attack produced one explicit reset-free literal braid, plus exact quadratic obstructions eliminating concentric-ring, raster, and ordered shell-factor implementations.

## 1. A literal triangular-shell braid

For \(t\ge1\), put
\[
A_t=(t,0,0),\qquad B_t=(0,t,0),\qquad C_t=(0,0,t)
\]
and define
\[
\begin{aligned}
\mathcal C_t={}&
(t,0,0),(t-1,1,0),\ldots,(0,t,0),\\
& (0,t-1,1),\ldots,(0,0,t),\\
& (1,0,t-1),\ldots,(t,0,0).
\end{aligned}
\]
This block has \(3t+1\) entries. Concatenate the blocks for \(t=1,\ldots,R\).

For \(R\ge2\), replace \(\mathcal C_1\) by
\[
(B_1,C_1,A_1).
\]
The resulting literal word \(W_R\) has exact length
\[
\boxed{|W_R|=\frac{3R(R+1)}2+R-1.}
\]

### Literal coverage

Given \(v=(x,y,z)\ne0\), let \(t=\max(x,y,z)\).

- If \(y=t\), the interval
  \[
  (x,t-x,0)\longrightarrow B_t\longrightarrow(0,t-z,z)
  \]
  has maximum \((x,t,z)\).

- If \(y<t\) and \(z=t\), the interval
  \[
  (0,y,t-y)\longrightarrow C_t\longrightarrow(x,0,t-x)
  \]
  has maximum \((x,y,t)\).

- Otherwise \(x=t\) and \(y,z<t\). For \(t\ge2\), take the suffix of \(\mathcal C_{t-1}\) beginning at
  \[
  (t-1-z,0,z),
  \]
  cross the seam from terminal \(A_{t-1}\) to initial \(A_t\), and stop at
  \[
  (t-y,y,0).
  \]
  Its maximum is exactly \((t,y,z)\).

The shortened first block covers six max-one targets; the remaining target \((1,1,0)\) occurs literally in \(\mathcal C_2\). Thus
\[
\boxed{
g_3(R,R,R)\le \frac{3R(R+1)}2+R-1\qquad(R\ge2).
}
\]

Writing \(w_R=w(R,R,R)\),
\[
w_R=
\begin{cases}
3s^2+3s+1,&R=2s,\\
3(s+1)^2,&R=2s+1,
\end{cases}
\]
and hence
\[
|W_R|=2w_R-\left\lfloor\frac R2\right\rfloor-3.
\]
So this is a genuine reset-free surface braid, but its length is still \((2-o(1))w_R\), not \(w_R+o(R^2)\).

## 2. Concentric rings cannot be repaired by sector offsets

Let the \(M_a=3a^2+3a+1\) middle targets of \([0,2a]^3\) be ordered by consecutive radius rings, allowing arbitrary seams and orientations inside each ring. Let a word of length \(M_a+D\) represent them on proper intervals
\[
I_i=[i+\alpha_i,i+\beta_i],
\]
where both offset sequences are nondecreasing in \([0,D]\), and put \(d_i=\beta_i-\alpha_i\).

For every internal positive threshold run \([u,v]\), factorability forces
\[
\boxed{\beta_{u-1}-\alpha_{v+1}\le v-u.}
\tag{1}
\]
Indeed, a pin for that run must lie strictly after \(I_{u-1}\) and strictly before \(I_{v+1}\).

On every radius-\(r\) ring, at least one of the three extreme arcs
\[
x=r,\qquad y=r,\qquad z=r
\]
survives the chosen cut as an internal run of \(r+1\) vertices. Selecting one such run per ring and charging the monotone offset increments gives
\[
\boxed{
\sum_{i=1}^{M_a}d_i
\le
2a^3+6a^2+4a+1+18aD.
}
\tag{2}
\]

The exact rank-capped-start inequality is
\[
V_a\le\sum_i d_i+(3a-1)D,
\]
where
\[
V_a=4a^3+\frac92a^2+\frac32a-1
\]
counts the nonzero targets strictly below the middle rank. Therefore every universal word with this ring order satisfies
\[
\boxed{
D\ge
\frac{2a^3-\frac32a^2-\frac52a-2}{21a-1}
=
\left(\frac2{21}+o(1)\right)a^2.
}
\]

For the canonical ring cut, the sharper exact charging gives
\[
\sum_i d_i\le2a^3+2a^2+1+7aD
\]
and consequently
\[
D\ge\left(\frac15+o(1)\right)a^2.
\]

Thus arbitrary sector-dependent offsets, rotating seams, and ring orientations cannot rescue any concentric cyclic-ring braid. The audit carefully distinguishes the \(M_a\) distinct selected middle targets from the repeated occurrences in the closed spiral.

## 3. Natural fixed-coordinate rasters also incur quadratic excess

Order the middle layer by increasing \(x\), keeping every fixed-\(x\) row contiguous and monotone in \(y\), with arbitrary row orientations.

For one maximum-\(y\) endpoint \(e\) per row, the relevant \(y\)-superlevel component through \(e\) has at most three ordered targets. Exact pinning and total variation of the offsets imply
\[
\sum_e d_e\le2(2a+1)+6D.
\]
Consecutive selected row endpoints are at distance at most \(4a+2\), so
\[
\sum_i d_i\le(4a+2)(4a+2+8D).
\]
Combining this with the same rank-capped-start inequality yields
\[
\boxed{
D\ge
\frac{V_a-(4a+2)^2}{35a+15}
=
\left(\frac4{35}+o(1)\right)a^2.
}
\]

The argument scales uniformly on \(\delta R\le p,q,r\le CR\), giving \(D=\Omega_{\delta,C}(R^2)\) for every natural fixed-coordinate raster.

## 4. The shell braid has no ordered factor compression

Suppose every virtual occurrence \(T_i\) of the triangular-shell word is represented by an interval
\[
J_i=[a_i,b_i]
\]
in a shorter physical word, with both endpoint sequences nondecreasing.

If \(b_{i+1}=b_i\), then \(a_i\le a_{i+1}\) gives
\[
J_{i+1}\subseteq J_i
\quad\Longrightarrow\quad
T_{i+1}\le T_i.
\]
But inside a shell, adjacent occurrences are distinct equal-rank points and hence incomparable. At a shell seam,
\[
A_t<A_{t+1}.
\]
Thus \(b_{i+1}>b_i\) at every adjacency. Therefore the physical word has at least as many positions as the virtual braid:
\[
\boxed{n\ge |W_R|.}
\]
Singleton certificates attain equality. Hence the globally ordered linked-factor optimum is exactly
\[
\frac{3R(R+1)}2+R-1=(2-o(1))w_R.
\]

This does not rule out a nonmonotone crossing-interval factorization. Existing rank-cap and ring estimates do not currently exclude that relaxation.

## Exact surviving gap

A successful construction must now do all of the following:

- interleave radii on a positive proportion of the surface;
- avoid every \(O(R)\)-spaced net of bounded coordinate-threshold components;
- use long cross-radius coordinate corridors;
- abandon globally monotone factor endpoints, or abandon the shell order;
- prove literal lower-target pin survival, not merely meet-shadow coverage.

No such braid was obtained. In particular, the primitive-ray theorem
\[
g_3(at,bt,ct)=w(at,bt,ct)+o(t^2)
\]
remains unproved even on the cubic ray. The new shell braid is integral and literal throughout, but it stops at asymptotic factor \(2\).

All decisive constants and indexing conventions above were independently audited. No web search, finite search, or workspace edits were used.
