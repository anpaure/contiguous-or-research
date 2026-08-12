# Second-wave T: balanced three-box layer and corridor braids

Date: 2026-07-24

## 0. Verdict

Let

\[
P(p,q,r)=[0,p]\times[0,q]\times[0,r]
\]

with the product order. A range-maximum word is a finite word of nonzero
points of \(P(p,q,r)\) such that every nonzero target is the coordinatewise
maximum of a contiguous interval. Let \(g_3(p,q,r)\) be the minimum length
and \(w_3(p,q,r)\) the width.

For \(p+q+r>0\), the standard lower bound \(g_3\ge w_3\) is literal:
witnesses selected for a target antichain form an antichain under interval
containment, and a containment antichain of intervals on an \(N\)-position
line has at most \(N\) members (their left endpoints are distinct). The
all-zero degenerate box is excluded from this sentence because the zero
target is omitted.

Here “uniform compact” means the inherited statement uniform over
\(\delta R\le p,q,r\le CR\) for arbitrary fixed \(0<\delta<C\); it does
not mean the narrower asymptotically equilateral condition
\(p/R,q/R,r/R\to1\). That uniform compact target is false. The critical
dominant-ray lower bound in
'MATH_ATTACK_F_DRAY_CONSTRUCTION_20260724.md' survives a new independent
audit in every vulnerable place. For fixed integers

\[
0<a<b,\qquad c>2b,
\]

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_3(at,bt,ct)-(at+1)(bt+1)}{t^2}
\ge
\frac{ab(c-2b)}{c+5a+5b}>0.
}
\tag{0.1}
\]

In particular,

\[
g_3(t,2t,5t)
\ge (t+1)(2t+1)+\left(\frac1{10}-o(1)\right)t^2.
\tag{0.2}
\]

Thus a theorem uniform over all fixed comparable aspect ratios cannot be
true. This invalidates the former compact-box/DRAY product route. It does
not refute the Boolean contiguous-OR conjecture, because a global
construction may share witnesses between product boxes rather than solve
each three-box at its own width.

The equilateral and strict-triangle sectors remain open. In particular,

\[
\boxed{
g_3(R,R,R)=w_3(R,R,R)+o(R^2)
}
\tag{EQ}
\]

is neither proved nor disproved here.

The second-wave layer/corridor attack produced these exact results.

1. A literal rectangular priority-shell word covers every target. On the
   cube, for \(R\ge2\), it has length

   \[
   \frac{3R(R+1)}2+R-1
   =2w_3(R,R,R)-\left\lfloor\frac R2\right\rfloor-3,
   \]

   so it remains at asymptotic factor two.

2. There is an explicit width-sized, three-direction, cross-radius middle
   order \(\mathcal B_a\) for \([0,2a]^3\). Its raw middle word misses a
   displayed upper target. More strongly, every near-width physical factor
   inducing this order has excess

   \[
   D\ge\left(\frac1{21}-o(1)\right)a^2
   =\left(\frac1{84}-o(1)\right)R^2.
   \]

3. A common-pivot full-slice recursion costs at least \(R^2+2R\).
   Arbitrarily many local rectangular pivots still force
   \(N\ge\lceil R(2R+1)/2\rceil\) if each physical position serves at most
   two portals. A width-scale word in that model therefore needs quadratic
   excess portal-incidence mass above reuse degree two. If reuse degree is
   capped at three, this means positive-density triple use.

4. In every unrestricted near-width cube word, elementary boundary-arm
   witnesses force at least \((3/4-o(1))R^2\) units of physical corridor
   overlap incidence between different max levels. This mass may be
   concentrated on few high-multiplicity positions; it is a necessary
   ledger, not a contradiction.

No width-plus-\(o(R^2)\) cube braid was constructed. A survivor must realize
quadratic overlap-incidence mass. The present bounds do not decide whether
that mass is spread over degree-three positions or concentrated at
high-degree hubs, nor whether the reuse is local, nonlocal, or
mixed-orientation. Every theorem below states its exact scope.

---

## 1. The dominant-ray obstruction: independent audit

This section is self-contained because the result changes the target of the
lane.

### 1.1 Full rectangular middle layer

Assume

\[
0<p<q,\qquad r>p+q.
\]

Put

\[
M=(p+1)(q+1),\qquad
h=\left\lfloor\frac{p+q+r}{2}\right\rfloor,\qquad
\varepsilon=p+q+r-2h\in\{0,1\}.
\tag{1.1}
\]

Since \(p+q\le h\le r\), the full rank-\(h\) layer is

\[
\mathcal S_h=
\{(x,y,h-x-y):0\le x\le p,\ 0\le y\le q\}.
\tag{1.2}
\]

It has \(M\) points. Projection onto \((x,y)\) is injective on every
antichain, because points in one vertical fibre are comparable. Hence

\[
w_3(p,q,r)=M.
\tag{1.3}
\]

For fixed \(x,y\), the values

\[
z=0,1,\ldots,h-x-y-1
\]

are precisely the points below rank \(h\). Removing the zero target gives

\[
\begin{aligned}
L_{<h}
&=\sum_{x=0}^p\sum_{y=0}^q(h-x-y)-1\\
&=M\left(h-\frac{p+q}{2}\right)-1\\
&=M\frac{r-\varepsilon}{2}-1.
\end{aligned}
\tag{1.4}
\]

Both the parity term and the final subtraction are exact.

### 1.2 Ordered witnesses and rank-capped starts

Let a universal word have length \(N=M+D\). Choose one interval

\[
I_i=[\ell_i,r_i]
\]

witnessing each point of \(\mathcal S_h\), ordered by increasing left
endpoint. Equal starts are impossible: the intervals would be nested and
their distinct equal-rank maxima comparable. The right endpoints are
strictly increasing too. If

\[
\ell_i<\ell_j,\qquad r_i\ge r_j,
\]

then \(I_j\subseteq I_i\), giving the same contradiction.

Thus

\[
\ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,
\tag{1.5}
\]

where

\[
0\le\alpha_1\le\cdots\le\alpha_M\le D,\qquad
0\le\beta_1\le\cdots\le\beta_M\le D.
\tag{1.6}
\]

Write

\[
d_i=r_i-\ell_i=\beta_i-\alpha_i.
\tag{1.7}
\]

### Lemma 1.1 (rank-capped starts)

\[
\boxed{
L_{<h}\le\sum_{i=1}^M d_i+(h-1)D.
}
\tag{1.8}
\]

#### Proof

Select one witness for each nonzero target below rank \(h\), grouping by
left endpoint. At selected start \(\ell_i\), a below-middle witness must end
before \(r_i\); otherwise it contains \(I_i\) and dominates its rank-\(h\)
target. There are \(d_i\) possible earlier endpoints.

Exactly \(D=N-M\) starts are unselected. At one fixed start, maxima obtained
by moving the right endpoint form a chain. A strict chain of nonzero points
below rank \(h\) has at most one point in each rank \(1,\ldots,h-1\), hence
at most \(h-1\) points. Summing proves (1.8). \(\square\)

No shortest or canonical middle witnesses were used.

### 1.3 Valley and short-run lemmas

For a nonnegative integer sequence \(u_1,\ldots,u_m\), an internal positive
threshold run is a component \([s,t]\) of

\[
\{i:u_i\ge k\},\qquad k\ge1,
\]

with \(1<s\le t<m\).

### Lemma 1.2 (valley characterization)

If there is no internal positive threshold run, then for some \(\tau\),

\[
u_1\ge\cdots\ge u_\tau\le\cdots\le u_m.
\tag{1.9}
\]

#### Proof

Choose a global-minimum index \(\tau\). If the prefix through \(\tau\) is
not nonincreasing, some \(i<j<\tau\) satisfy \(u_i<u_j\), while
\(u_\tau\le u_i\). At threshold \(u_j\ge1\), the positive component
containing \(j\) is blocked on the left by \(i\) and on the right by
\(\tau\). The suffix argument is symmetric. \(\square\)

### Lemma 1.3 (constant-sum valley bound)

Let \(T_1,\ldots,T_m\in\mathcal S_h\) be distinct. If all three coordinate
sequences are valleys, then

\[
m\le p+q+1.
\tag{1.10}
\]

#### Proof

Relabel the coordinates as \(X,Y,Z\) so their turns satisfy
\(\tau_X\le\tau_Y\le\tau_Z\). Before \(\tau_X\), all coordinates are
nonincreasing, so constant sum forces every step to be constant. Hence
\(\tau_X=1\). Similarly \(\tau_Z=m\).

Between \(\tau_X\) and \(\tau_Y\), \(X\) is nondecreasing while \(Y,Z\)
are nonincreasing, so \(X\) must increase strictly at every step. Between
\(\tau_Y\) and \(\tau_Z\), \(Z\) must decrease strictly. Therefore

\[
\begin{aligned}
m-1
&\le X_{\tau_Y}-X_{\tau_X}
  +Z_{\tau_Y}-Z_{\tau_Z}\\
&=h-Y_{\tau_Y}-X_{\tau_X}-Z_{\tau_Z}.
\end{aligned}
\tag{1.11}
\]

The three coordinatewise lower bounds on \(\mathcal S_h\), in some order,
are \(0,0,h-p-q\). The last line is at most \(p+q\). \(\square\)

### Lemma 1.4 (short-run mesh)

Every ordering of \(p+q+2\) distinct points of \(\mathcal S_h\) contains an
internal coordinate-threshold run \([u,v]\) satisfying

\[
v-u\le q.
\tag{1.12}
\]

#### Proof

Lemmas 1.2--1.3 first give an internal run in some coordinate. Let \(m_0\)
be the maximum coordinate value attained on it. Choose the maximal
consecutive \(m_0\)-plateau containing an occurrence of \(m_0\) inside the
original run. Both immediate neighbors are below \(m_0\), so this plateau
is itself an internal run at threshold \(m_0\).

An \(x\)-level in \(\mathcal S_h\) has \(q+1\) points, a \(y\)-level has
\(p+1\), and a \(z\)-level has at most \(p+1\). The plateau has at most
\(q+1\) positions. \(\square\)

The phrase “containing an occurrence inside the original run” is the only
wording repair needed in the source proof.

### 1.4 Literal multipin-safe gap

Fix a coordinate threshold \(k\), and let \([u,v]\) be an internal positive
run in its incidence word on the ordered middle targets.

### Lemma 1.5 (literal pin gap)

\[
\boxed{
r_{u-1}+2\le\ell_{v+1},\qquad
\beta_{u-1}-\alpha_{v+1}\le v-u.
}
\tag{1.13}
\]

#### Proof

The positive witness \(I_u\) contains a physical position \(s\) whose
chosen coordinate is at least \(k\). The negative interval \(I_{u-1}\)
contains no such position. Since \(s\ge\ell_u>\ell_{u-1}\), one has
\(s>r_{u-1}\). Likewise \(I_{v+1}\) is negative and
\(s\le r_u<r_{v+1}\), so \(s<\ell_{v+1}\). Thus

\[
r_{u-1}+1\le s\le\ell_{v+1}-1,
\]

which gives (1.13). \(\square\)

Only one occurrence in one positive witness is used. The threshold may
occur at arbitrarily many physical positions, and different witnesses may
use different pins.

If \(v-u\le q\), monotonicity gives

\[
d_i\le q+\alpha_{v+1}-\alpha_i\qquad(i<u),
\tag{1.14}
\]

and

\[
d_i\le q+\beta_i-\beta_{u-1}\qquad(i>v).
\tag{1.15}
\]

### 1.5 Balanced block pairing

Put

\[
s_0=p+q+2,\qquad
K=2\left\lfloor\frac{M}{2s_0}\right\rfloor.
\tag{1.16}
\]

Assume \(K\ge2\), let \(R_0=M-Ks_0\), and set

\[
B=s_0+\left\lceil\frac{R_0}{K}\right\rceil.
\tag{1.17}
\]

Then \(K\) is even and \(0\le R_0<2s_0\). Partition the middle order into
\(K\) consecutive blocks, each of size in \([s_0,B]\). Apply Lemma 1.4 to
the first \(s_0\) points of every block, so the run and both negative
neighbors stay inside the block.

Pair adjacent blocks \(C=[a,b]\) and \(C'=[b+1,c]\). Assign every index of
\(C\) to the short run in \(C'\), and every index of \(C'\) to the short
run in \(C\). Equations (1.14)--(1.15) give

\[
\sum_{i\in C}d_i
\le q|C|+B(\alpha_c-\alpha_a),
\tag{1.18}
\]

\[
\sum_{i\in C'}d_i
\le q|C'|+B(\beta_c-\beta_a).
\tag{1.19}
\]

Distinct pair spans are disjoint, so the total \(\alpha\)-variation and
the total \(\beta\)-variation charged are separately at most \(D\). Hence

\[
\boxed{
\sum_{i=1}^M d_i\le qM+2BD.
}
\tag{1.20}
\]

No increment is charged across a boundary between block pairs.

### 1.6 Finite and asymptotic conclusions

Combining (1.4), (1.8), and (1.20) gives

\[
\boxed{
D\ge
\frac{M((r-\varepsilon)/2-q)-1}{h-1+2B}
}
\tag{1.21}
\]

whenever the numerator is positive.

Now set \(p=at,q=bt,r=ct\), with fixed \(0<a<b\), \(c>2b\). Then

\[
\frac{M}{t^2}\to ab,\qquad
\frac ht\to\frac{a+b+c}{2},\qquad
\frac Bt\to a+b.
\]

Dividing (1.21) by \(t^2\) gives (0.1). The finite condition \(K\ge2\) is
automatic eventually.

The proof is architecture-free and disproves DRAY. It says nothing
directly about the cube because it requires \(r>p+q\). The strict-triangle
sector \(r<p+q\), including the cube, survives and is still unproved. The
same argument also leaves moderate plateau rays
\(p+q\le r\le2q\) unresolved; strict-triangle is the revised focus of this
lane, not the exhaustive complement of the obstruction.

The smallest retained target in this lane is (EQ). If (EQ) holds, the
standard face-extension inequality extends it at \(o(R^2)\) cost to every
asymptotically equilateral family

\[
p=R+o(R),\qquad q=R+o(R),\qquad r=R+o(R).
\]

It does not extend it to arbitrary fixed unequal ratios.

---

## 2. Best explicit literal word: the rectangular priority shell

### Theorem 2.1 (priority-shell word)

For \(1\le p\le q\le r\),

\[
\boxed{
g_3(p,q,r)
\le
pq+pr+qr-p^2-\binom q2+p+r-\mathbf1_{\{q\ge2\}}.
}
\tag{2.1}
\]

#### Construction

For \(1\le t\le p\), use

\[
\begin{aligned}
\mathcal C_t={}&
(t,0,0),(t-1,1,0),\ldots,(0,t,0),\\
&(0,t-1,1),\ldots,(0,0,t),\\
&(1,0,t-1),\ldots,(t,0,0).
\end{aligned}
\tag{2.2}
\]

For \(p<t\le q\), use

\[
\begin{aligned}
\mathcal D_t={}&
(p,t-p,0),(p-1,t-p+1,0),\ldots,(0,t,0),\\
&(0,t-1,1),\ldots,(0,0,t),\\
&(1,0,t-1),\ldots,(p,0,t-p).
\end{aligned}
\tag{2.3}
\]

For \(q<t\le r\), use

\[
\begin{aligned}
\mathcal E_t={}&
(0,q,t-q),(0,q-1,t-q+1),\ldots,(0,0,t),\\
&(1,0,t-1),\ldots,(p,0,t-p).
\end{aligned}
\tag{2.4}
\]

Concatenate the blocks in increasing \(t\).

#### Literal certificates

Take a nonzero target \((x,y,z)\) and put \(t=\max\{x,y,z\}\), resolving
ties in this order.

1. If \(y=t\), the interval

   \[
   (x,t-x,0)\longrightarrow(0,t,0)\longrightarrow(0,t-z,z)
   \tag{2.5}
   \]

   has maximum \((x,t,z)\).

2. If \(y<t\) and \(z=t\), the interval

   \[
   (0,y,t-y)\longrightarrow(0,0,t)\longrightarrow(x,0,t-x)
   \tag{2.6}
   \]

   has maximum \((x,y,t)\).

3. Otherwise \(x=t\) and \(y,z<t\), so \(t\le p\). For \(t\ge2\), begin
   in the suffix of \(\mathcal C_{t-1}\) at
   \((t-1-z,0,z)\), cross the seam from \((t-1,0,0)\) to \((t,0,0)\),
   and end at \((t-y,y,0)\). The maximum is \((t,y,z)\). At \(t=1\), the
   remaining target \((1,0,0)\) occurs literally.

The unshortened length is

\[
\sum_{t=1}^{p}(3t+1)
+\sum_{t=p+1}^{q}(t+2p+1)
+\sum_{t=q+1}^{r}(p+q+1)
=pq+pr+qr-p^2-\binom q2+p+r.
\tag{2.7}
\]

If \(q\ge2\), replace \(\mathcal C_1\) by

\[
(0,1,0),(0,0,1),(1,0,0).
\tag{2.8}
\]

It misses only \((1,1,0)\), supplied at level two by \(\mathcal C_2\) if
\(p\ge2\), or by the first point of \(\mathcal D_2\) if \(p=1\). This
proves (2.1). \(\square\)

For the cube,

\[
w_3(R,R,R)=
\begin{cases}
3s^2+3s+1,&R=2s,\\[1mm]
3(s+1)^2,&R=2s+1,
\end{cases}
\tag{2.9}
\]

whereas, for \(R\ge2\), the word length is

\[
N_R=\frac{3R(R+1)}2+R-1
=2w_3(R,R,R)-\left\lfloor\frac R2\right\rfloor-3.
\tag{2.10}
\]

It is a literal reset-free baseline, not a proof of (EQ).

---

## 3. Explicit width-sized rotating corridor order

Work in the translated middle layer of \([0,2a]^3\):

\[
H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,\ |x|,|y|,|z|\le a\},
\qquad
M_a=3a^2+3a+1.
\tag{3.1}
\]

All literal maxima below are interpreted after translating every displayed
triple by \((a,a,a)\); coordinatewise translation commutes with interval
maximum.

For \(1\le t\le a\), put

\[
L_t=\max(-a,-2t),\qquad U_t=\min(a-t,t-1),
\tag{3.2}
\]

and define

\[
X_t=\bigl((t,j,-t-j):j=L_t,\ldots,U_t\bigr),
\tag{3.3}
\]

\[
Y_t=\bigl((j,t,-t-j):
j=\min(t,a-t),\ldots,\max(-a,-2t+1)\bigr),
\tag{3.4}
\]

with the \(Y_t\)-parameter traversed downward, and

\[
Z_t=\bigl((j,-t-j,t):j=L_t,\ldots,U_t\bigr).
\tag{3.5}
\]

The cyclic tie convention is:

- \(X_t\) owns \(x=t\) with \(y<t\);
- \(Y_t\) owns \(y=t\) with \(z<t\);
- \(Z_t\) owns \(z=t\) with \(x<t\).

These blocks partition the shell \(\max\{x,y,z\}=t\). All three have length

\[
h_t=
\begin{cases}
3t,&2t\le a,\\[1mm]
2a-t+1,&2t>a.
\end{cases}
\tag{3.6}
\]

Indeed, the \(X_t\)-parameter interval is \([-2t,t-1]\) in the first case
and \([-a,a-t]\) in the second; the other counts are identical. Moreover,

\[
\sum_{t=1}^a h_t=a(a+1).
\tag{3.7}
\]

Define

\[
\boxed{
\mathcal B_a=
X_aY_aZ_a\,X_{a-1}Y_{a-1}Z_{a-1}\cdots
X_1Y_1Z_1\,(0,0,0).
}
\tag{3.8}
\]

It enumerates \(H_a\) once and has the exact width length

\[
|\mathcal B_a|=1+3\sum_{t=1}^a h_t=M_a.
\tag{3.9}
\]

### 3.1 Seam geometry and partial certificate

At \(X_t|Y_t\), either \(x=t\) continues for one position or \(z=-a\)
is a two-position valley. At \(Y_t|Z_t\), either \(y=t\) continues or
\(x=-a\) is a valley. At \(Z_t|X_{t-1}\), the varying coordinates
continue monotonically, with either \(x=t-1\) or \(y=-a\) constant at the
seam. Thus \(\mathcal B_a\) is a genuine three-direction cross-radius
braid, not a complete-ring enumeration.

If

\[
L_t\le -t-c\le b\le U_t,
\tag{3.10}
\]

then the interval in \(X_t\) from parameter \(-t-c\) to parameter \(b\)
has literal maximum

\[
\max\{(t,j,-t-j):-t-c\le j\le b\}=(t,b,c).
\tag{3.11}
\]

The cyclic analogues hold in \(Y_t,Z_t\). Hence each corridor covers an
explicit triangular wedge.

### 3.2 Exact upper-shadow failure

For \(a\ge2\), consider

\[
U=(a,a-1,-a+1),
\tag{3.12}
\]

or \((2a,2a-1,1)\) in unshifted box coordinates. Every provider of
first-coordinate value \(a\) lies in the initial block \(X_a\), where
\(y\le0\). Every provider of \(y=a-1\) occurs later. Any interval joining
the two crosses \(Y_a\), whose second coordinate is \(a\), exceeding the
target. Therefore \(U\) is not the maximum of any contiguous interval of
the raw middle word.

### 3.3 Multipin-safe heterogeneous run cover

Suppose a physical universal word of length \(M_a+D\) has selected middle
witnesses whose increasing-left-end order is \(\mathcal B_a\). Write

\[
I_i=[i+\alpha_i,i+\beta_i],\qquad
d_i=\beta_i-\alpha_i,
\tag{3.13}
\]

with \(\alpha,\beta\) nondecreasing in \([0,D]\).

For every index \(i\), choose an internal threshold run
\(R_i=[u_i,v_i]\) not containing \(i\), and put
\(\lambda_i=v_i-u_i\). The pin-gap lemma gives

\[
d_i\le\lambda_i+\alpha_{v_i+1}-\alpha_i
\qquad(i<u_i),
\tag{3.14}
\]

\[
d_i\le\lambda_i+\beta_i-\beta_{u_i-1}
\qquad(i>v_i).
\tag{3.15}
\]

If all forward charge spans are at most \(H_\alpha\) and all backward
spans at most \(H_\beta\), expansion into adjacent increments gives

\[
\boxed{
\sum_i d_i
\le\sum_i\lambda_i+(H_\alpha+H_\beta)D.
}
\tag{3.16}
\]

Each \(\alpha\)-increment is charged by at most the number of possible
source indices in the forward span; similarly for \(\beta\). This is the
entire congestion proof.

### 3.4 Exact run assignment

Assign:

- every source index of \(X_t\) to the internal run \(y\ge t\);
- every source index of \(Y_t\) to the internal run \(z\ge t\);
- every source index of \(Z_t\), for \(t<a\), to the internal run \(x\ge t\);
- \(Z_a\) to the internal run \(y\ge a\);
- the final center to the internal run \(z\ge1\).

No source lies in its assigned run.

The run \(y\ge t\) is \(Y_t\), plus the first point of \(Z_t\) exactly
when \(2t\le a\), so its edge cost is at most \(h_t\). The run \(z\ge t\)
is exactly \(Z_t\), of cost \(h_t-1\). For \(t<a\), the run \(x\ge t\)
is \(X_t\), together with at most the last point of \(Z_{t+1}\) and the
first point of \(Y_t\), so its cost is at most \(h_t+1\). Each run is
bracketed by negative neighbors.

The total base cost is therefore at most

\[
\begin{aligned}
S_a
&=\sum_{t=1}^a
\bigl(h_t^2+h_t(h_t-1)+h_t(h_t+1)\bigr)+2\\
&=3\sum_{t=1}^a h_t^2+2.
\end{aligned}
\tag{3.17}
\]

The \(t=a\) term is overcounted, so this is safe. A forward charge crosses
at most \(2h_{\max}+1\) adjacent index increments; a backward charge
crosses at most \(3h_{\max}+1\). Consequently

\[
\boxed{
\sum_i d_i
\le3\sum_{t=1}^a h_t^2+2+(5h_{\max}+2)D.
}
\tag{3.18}
\]

The exact sums are

\[
\sum_{t=1}^a h_t^2
=\frac76a^3+\frac74a^2+\frac56a
+\begin{cases}
0,&a\text{ even},\\[1mm]
\frac14,&a\text{ odd},
\end{cases}
\tag{3.19}
\]

\[
h_{\max}=
\begin{cases}
\frac32a,&a\text{ even},\\[1mm]
\frac{3a+1}{2},&a\text{ odd}.
\end{cases}
\tag{3.20}
\]

### 3.5 Exact quadratic factor obstruction

The number of nonzero targets strictly below the middle layer is

\[
V_a=4a^3+\frac92a^2+\frac32a-1.
\tag{3.21}
\]

The rank-capped start lemma gives

\[
V_a\le\sum_i d_i+(3a-1)D.
\tag{3.22}
\]

Combining (3.18)--(3.22), for even \(a\),

\[
\boxed{
D\ge
\frac{2a^3-3a^2-4a-12}{2(21a+2)}.
}
\tag{3.23}
\]

For odd \(a\ge3\),

\[
\boxed{
D\ge
\frac{2a^3-3a^2-4a-15}{2(21a+7)}.
}
\tag{3.24}
\]

Hence

\[
\boxed{
D\ge\left(\frac1{21}-o(1)\right)a^2
=\left(\frac1{84}-o(1)\right)R^2,\qquad R=2a.
}
\tag{3.25}
\]

This is architecture-local. It rules out physical factors inducing
\(\mathcal B_a\), not unrestricted \(g_3(2a,2a,2a)\).

---

## 4. Universal boundary-corridor overlap

### Theorem 4.1 (boundary-arm corridor ledger)

Let \(W=(v_1,\ldots,v_n)\) be universal for \([0,R]^3\). For each
\(1\le t\le R\), select witnesses for

\[
\begin{aligned}
A_{t,i}&=(i,t,0),&1\le i\le t,\\
B_{t,j}&=(0,j,t),&1\le j\le t,\\
C_{t,k}&=(t,0,k),&1\le k\le t.
\end{aligned}
\tag{4.1}
\]

Let \(J_t\) be any physical interval containing all these selected
witnesses. Then

\[
\boxed{|J_t|\ge3t.}
\tag{4.2}
\]

If \(d(s)=|\{t:s\in J_t\}|\), then

\[
\boxed{
\sum_{s=1}^n d(s)=\sum_{t=1}^R|J_t|
\ge\frac{3R(R+1)}2.
}
\tag{4.3}
\]

#### Proof

An \(A_{t,i}\)-witness contains a position with first coordinate \(i\);
because its target has third coordinate zero, that position has third
coordinate zero. Choose one such pin \(u_{t,i}\). A \(B_{t,j}\)-witness
gives a pin \(v_{t,j}\) with second coordinate \(j\) and first coordinate
zero. A \(C_{t,k}\)-witness gives a pin \(w_{t,k}\) with third coordinate
\(k\) and second coordinate zero.

Pins in one family are distinct because their positive levels differ. The
three families are pairwise disjoint: \(u\ne v\) by the first coordinate,
\(v\ne w\) by the second, and \(w\ne u\) by the third. All \(3t\) pins lie
in \(J_t\). Double-count incidences to get (4.3). \(\square\)

If the \(J_t\) were disjoint, this would force the factor-two shell length.
For a hypothetical word with \(n=w_3(R,R,R)+o(R^2)\), it instead forces

\[
\frac1n\sum_s d(s)\ge2-o(1),
\tag{4.4}
\]

\[
\sum_s(d(s)-1)_+
\ge\frac{3R(R+1)}2-n
=\left(\frac34-o(1)\right)R^2.
\tag{4.5}
\]

The total cross-level overlap-incidence toll is quadratic. Equation (4.5)
does not force quadratic support: high multiplicity could concentrate it
on a sparse set of positions. It is a requirement, not an impossibility
theorem.

---

## 5. Dyadic layer portals

The most direct deterministic recursion joins an \(x\)-record arm and a
\(y\)-record arm through one or more height-\(t\) pivots.

### 5.1 One-pivot portal

Put

\[
X_i=(i,0,0),\qquad Y_j=(0,j,0),\qquad Z_t=(0,0,t).
\]

The word

\[
X_p,X_{p-1},\ldots,X_1,Z_t,Y_1,\ldots,Y_q
\tag{5.1}
\]

is a literal portal for the full height-\(t\) slice: its appropriate
suffix-pivot-prefix interval has maximum \((x,y,t)\).

### Theorem 5.1 (one-pivot tree bound)

Let \(A_1,\ldots,A_N\in P(p,q,r)\). Suppose that for every \(t\) in a set
\(T\subseteq\{1,\ldots,r\}\), one distinguished occurrence

\[
A_{k_t}=(0,0,t)
\]

belongs to a selected witness for every target

\[
(x,y,t),\qquad0\le x\le p,\quad0\le y\le q.
\]

Put \(s=\min(p,q)\), \(K=|T|\). Then

\[
\boxed{N\ge(s+1)K+s.}
\tag{5.2}
\]

#### Proof

Fix \(t\). Let \(C_t\) be the maximal contiguous component of positions
whose third coordinate is at most \(t\) and which contains \(k_t\). Every
selected witness containing \(k_t\) lies in \(C_t\).

The \(xy\)-maxima of suffixes ending at \(k_t\) form a product-order chain
\(L_t\); prefix maxima beginning at \(k_t\) form a chain \(R_t\). Every
point of the \(xy\)-rectangle is the join of one state from each chain.

For target \((x,0)\), both states lie on the \(x\)-axis and one has first
coordinate exactly \(x\). Thus \(L_t\cup R_t\) contains every positive
\(x\)-axis state. Likewise it contains every positive \(y\)-axis state. A
product-order chain cannot contain a positive point from both axes. Hence
one arm supplies all \(p\) positive \(x\)-states and the other all \(q\)
positive \(y\)-states. Each side of \(k_t\) in \(C_t\) has at least \(s\)
positions.

Tie-break equal third-coordinate values so that \(k_t\) is higher than all
other occurrences at level \(t\). This is simultaneous across distinct
heights. In the max-Cartesian tree of the third-coordinate word, the
subtree rooted at \(k_t\) is exactly \(C_t\), and both child subtrees have
at least \(s\) nodes.

Each marked tree node has two child-side slots. A slot is occupied if its
child subtree contains a marked descendant. Occupied slots inject into the
non-root marked nodes by choosing a first marked descendant, so at most
\(K-1\) slots are occupied. At least \(K+1\) slots are mark-free; their
child subtrees are pairwise disjoint and each has at least \(s\) nodes.
Adding the \(K\) marked nodes gives (5.2). \(\square\)

For the cube, using one common pivot at every positive height forces

\[
N\ge R^2+2R,
\tag{5.3}
\]

and

\[
N-w_3(R,R,R)\ge
\begin{cases}
\frac14R^2+\frac12R-1,&R\text{ even},\\[1mm]
\frac14R^2+\frac12R-\frac34,&R\text{ odd}.
\end{cases}
\tag{5.4}
\]

Thus a near-width word can use such a common full-slice pivot on at most
\((3/4+o(1))R\) positive heights.

### 5.2 Arbitrarily many local rectangle pivots

A portal rectangle with lower corner \((u,v)\) and dimensions \(A\times B\)
has the literal word

\[
\begin{aligned}
&(u+A-1,v,0),\ldots,(u+1,v,0),\\
&(u,v,t),\\
&(u,v+1,0),\ldots,(u,v+B-1,0).
\end{aligned}
\tag{5.5}
\]

It has \(A+B-1\) positions, and every point of the rectangle is the
maximum of an appropriate suffix-pivot-prefix interval.

Conversely, a common-pivot suffix-prefix portal with \(A\) distinct
left-arm states and \(B\) distinct right-arm states needs at least
\(A+B-1\) physical state positions. The two-axis argument forces one arm
to provide the first-coordinate states and the other the second-coordinate
states; only the pivot can be shared.

### Lemma 5.2 (rectangle-cover incidence)

Suppose rectangles of dimensions \(A_e\times B_e\) cover a \(P\times Q\)
slice, where \(1\le A_e\le P\), \(1\le B_e\le Q\). Then

\[
\boxed{
\sum_e(A_e+B_e-1)\ge P+Q-1.
}
\tag{5.6}
\]

#### Proof

The ratio

\[
\frac{AB}{A+B-1}
\]

is nondecreasing in both variables, so

\[
\frac{A_eB_e}{A_e+B_e-1}
\le\frac{PQ}{P+Q-1}.
\tag{5.7}
\]

Coverage gives \(PQ\le\sum_eA_eB_e\). Apply (5.7) termwise and cancel
\(PQ\). \(\square\)

For an \((R+1)\times(R+1)\) slice, the portal-state demand is \(2R+1\),
regardless of the number or sizes of local rectangles.

Assume that for every \(t=1,\ldots,R\), a family of these rectangles covers
the entire \((R+1)\times(R+1)\) height-\(t\) slice. Impose the explicit
global local-seam hypothesis that every physical position supplies endpoint
states to at most two portals over all those heights. Then

\[
2N\ge R(2R+1),
\]

so

\[
\boxed{
N\ge\left\lceil\frac{R(2R+1)}2\right\rceil.
}
\tag{5.8}
\]

The corresponding cubic width comparison is

\[
N-w_3(R,R,R)\ge
\begin{cases}
\frac14R^2-R-1,&R\text{ even},\\[1mm]
\frac14R^2-R-\frac14,&R\text{ odd}.
\end{cases}
\tag{5.9}
\]

The lower-order expressions can be negative for small \(R\); the leading
quadratic obstruction is the content.

### 5.3 Positive-density triple reuse

Let \(c_i\) be the number of portal-state incidences using position \(i\).
The slice demands imply

\[
\sum_i c_i\ge R(2R+1).
\tag{5.10}
\]

Since \(c_i\le2+(c_i-2)_+\), a width-plus-\(o(R^2)\) word in this model
must satisfy

\[
\boxed{
\sum_i(c_i-2)_+
\ge\left(\frac12-o(1)\right)R^2.
}
\tag{5.11}
\]

If \(c_i\le3\), at least \((1/2-o(1))R^2\) positions—two thirds of a
near-width word—must be triple-used. Sparse exceptional nesting cannot
repair degree-two corridor recursion.

These portal theorems are architecture-local. In an unrestricted word, one
physical position may serve many nonlocal portals, and mixed-orientation
partial rectangles need not fit the common-pivot product model.

---

## 6. A concrete surviving recursive gate

For \(R\ge1\), define

\[
\phi_R(j)=
\begin{cases}
0,&j=0,\\
j+1,&1\le j\le R-1.
\end{cases}
\tag{6.1}
\]

Apply it coordinatewise to a word in \([0,R-1]^3\). Since \(\phi_R\) is
monotone,

\[
\phi_R\left(\max_{i\in I}a_i\right)
=\max_{i\in I}\phi_R(a_i)
\tag{6.2}
\]

in every coordinate. The lifted word therefore covers every target in
\([0,R]^3\) whose coordinates avoid the value \(1\). The missing family is
the union of the three coordinate-\(1\) planes.

The exact cubic width increment is

\[
w_3(R,R,R)-w_3(R-1,R-1,R-1)
=\left\lfloor\frac{3R}{2}\right\rfloor+1.
\tag{6.3}
\]

This isolates a sharp open statement.

> **Selective zero-preserving lift lemma — UNPROVED.** There is one
> deterministic sequence \(e_R=o(R)\) such that, for every \(R\ge1\) and
> every universal \((R-1)\)-cube word, starting from its coordinatewise
> image under \(\phi_R\), one can insert at most
>
> \[
> \left\lfloor\frac{3R}{2}\right\rfloor+1+e_R
> \]
>
> new positions so that every target with at least one coordinate equal to
> \(1\) has a literal contiguous witness, while every previously covered
> target retains one selected mapped literal witness.

If this held uniformly, iteration and Cesàro summation would prove (EQ).
In the tested triangular-shell implementation, the three zero-face
families split into \(R\) components each and use about \(3R\) fresh pins;
this is not an unrestricted lower bound. No \(3R/2+o(R)\) insertion was
found.

---

## 7. Exact obstruction inventory

The table separates architecture-local statements from the one
architecture-free ray theorem.

| Architecture | Proved excess or defect | Exact scope |
|---|---:|---|
| Complete contiguous concentric rings | \(D\ge(2/15-o(1))a^2\) | Complete-ring block orders covered by the audited ring assignment |
| Explicit outward six-block ring order | \(D\ge(1/4-o(1))a^2\) | That displayed outward enumeration |
| Fixed-coordinate contiguous monotone raster | \(D\ge(4/19-o(1))a^2\) | Induced raster witness order with monotone rows |
| Rotating cross-radius order \(\mathcal B_a\) | \(D\ge(1/21-o(1))a^2\) | Physical factors inducing \(\mathcal B_a\) |
| One common full-slice pivot | \(N\ge R^2+2R\) | Distinguished pivot lies in every slice witness for every \(t=1,\ldots,R\) |
| Local rectangle portals, reuse degree at most two | \(N\ge\lceil R(2R+1)/2\rceil\) | Common-pivot suffix-prefix portal model |
| Dominant ray \(0<a<b,\ c>2b\) | coefficient (0.1) | Unrestricted literal words |

The first six rows do not lower-bound unrestricted cubic \(g_3\). The final
row is a genuine lower bound, but only in the dominant plateau cone.

A successful cube construction must:

1. accumulate quadratic excess overlap incidence among max-level boundary
   corridors, by (4.5), although this may concentrate on sparse support;
2. if organized by rectangle portals, accumulate quadratic portal-incidence
   mass above degree two, by (5.11); under a degree-three cap this becomes
   quadratic support of triple-used positions;
3. realize that excess through local degree-three reuse, sparse
   high-degree hubs, nonlocal reuse, mixed orientations, or some combination;
4. avoid complete rings, intact rasters, and the order \(\mathcal B_a\);
5. give literal interval maxima rather than only shadow identities or a
   fractional assignment of corridor roles.

These are requirements inside the stated models, not an existence or
impossibility theorem.

The cleanest surviving positive target is the selective lift of Section 6.
Another sufficient, but not necessary, target is a direct construction of
the following kind.

> **Mixed distributed braid lemma — UNPROVED.** Construct a literal word
> for \([0,R]^3\) of length \(w_3(R,R,R)+o(R^2)\) whose selected layer
> portals have positive-density cross-level triple reuse, with every
> coordinate threshold protected from contamination on every claimed
> interval.

A shadow walk, endpoint matching, or family of separately valid factors is
insufficient.

---

## 8. Independent audit and implication scope

1. **DRAY finite bound.** Two new independent audits rechecked ordered
   witnesses, valley turns, plateau extraction, the literal multipin gap,
   block pairing, congestion, parity, and the limiting constant. Both
   passed. The only repair is the explicit choice of the top plateau
   containing a point of the original run.

2. **Rotating corridor.** An independent audit reconstructed the shell
   partition, every run and negative neighbor, the one-sided spans, the
   square sum, both parity cases, and the \(1/21\) coefficient. All
   constants in (3.23)--(3.25) passed.

3. **Portal ledgers.** An independent audit checked the two-arm axis
   argument, Cartesian-tree count, \(A+B-1\) cost, monotonic ratio (5.7),
   and even/odd width comparisons. The reuse-degree hypothesis remains
   explicit.

4. **Literal logic.** Every positive claim here constructs or analyzes
   literal contiguous range maxima. Nothing is inferred from labelled
   common-owner synchronization, separate exact factors, or fractional
   corridor packings.

5. **Global scope.** Failure of DRAY and of the uniform compact three-box
   theorem invalidates that sufficient product-box route only. It does not
   imply failure of the Boolean contiguous-OR conjecture.

6. **Cubic status.** No result here proves
   \(g_3(R,R,R)\ge w_3(R,R,R)+\Omega(R^2)\), and no result proves the
   matching \(w_3+o(R^2)\) upper bound.

No web search, finite search, computational search, or probabilistic
experiment was used.

## Final status

The requested uniform width-plus-\(o(R^2)\) balanced-box braid cannot exist
as originally quantified, because the comparable ray \((1,2,5)\) has
positive quadratic excess. After revising the target to the
equilateral/strict-triangle sector, the attack yields an explicit literal
factor-two priority-shell word, a width-sized rotating corridor candidate
with an audited quadratic factor obstruction, and exact portal-reuse
requirements. The unrestricted equilateral braid (EQ) remains open.
