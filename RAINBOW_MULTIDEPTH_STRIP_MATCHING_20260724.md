# Quantitative multidepth-rainbow Johnson paths from strip matchings

## Result

Put

\[
W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\]

Let \(\omega=\omega(m)\) satisfy

\[
\omega\longrightarrow\infty,
\qquad
\omega=o\!\left(\frac{\log m}{\log\log m}\right).
\tag{0.1}
\]

Write \(L=\log m\), \(\lambda=\log L\), and set

\[
H=\left\lfloor
\left(\frac{L}{64\omega\lambda}\right)^{1/3}
\right\rfloor,
\qquad
\ell=\left\lceil\omega H^2\right\rceil.
\tag{0.2}
\]

Then there is a vertex-disjoint family \(\mathcal P_m\) of Johnson paths in
\(J(2m,m)\), with \(p_m\) path components, such that

\[
\rho_H(\mathcal P_m)=0
\tag{0.3}
\]

and

\[
\boxed{
Hp_m+
\sum_{q=1}^H(M_q^-+M_q^+)
+(H^2+2H)\rho_H(\mathcal P_m)=o(W).
}
\tag{0.4}
\]

More quantitatively, if \(U_m\) denotes the number of band vertices missed
by the strip matching constructed below, then

\[
U_m\le W(\log m)^{-10}
\tag{0.5}
\]

for all sufficiently large \(m\) (the exponent 10 is inessential), and

\[
Hp_m+\sum_{q=1}^H(M_q^-+M_q^+)
\le
U_m+\frac{H^2+2H}{2\ell}W
=O\!\left(\frac W\omega\right)+U_m.
\tag{0.6}
\]

Thus the reduced multidepth Johnson-path gate is unconditionally true at the
explicit depth

\[
H=\Theta\!\left(
\left(\frac{\log m}
{\omega(m)\log\log m}\right)^{1/3}
\right).
\tag{0.7}
\]

This does not approach the sprinkled-tail threshold
\(\Theta(\sqrt{m\log\log m})\), and hence does not prove the coefficient-one
conjecture.  It is a quantitative path-family result: unlike the economical
strip **cover**, the selected strip supports form a matching, so their
middle Johnson paths are genuinely vertex-disjoint and their certified
shadows have zero duplicate excess before the cycle cuts.

## 1. What depth-one rainbowness already implies at depth two

Let

\[
T_{i-1}\longrightarrow T_i\longrightarrow T_{i+1}
\]

be two consecutive edges in a two-sided-rainbow Johnson path.  Write the
first transition as removal of \(a_i\) and insertion of \(b_i\), and the
second as removal of \(a_{i+1}\) and insertion of \(b_{i+1}\).  The two
lower edge colours are

\[
T_i\setminus\{b_i\},\qquad T_i\setminus\{a_{i+1}\}.
\]

Their distinctness implies \(b_i\ne a_{i+1}\).  The two upper edge colours
are

\[
T_i\cup\{a_i\},\qquad T_i\cup\{b_{i+1}\},
\]

and their distinctness implies \(a_i\ne b_{i+1}\).  Hence neither changed
coordinate is immediately reversed, and

\[
\left|T_{i-1}\cap T_i\cap T_{i+1}\right|=m-2,
\qquad
\left|T_{i-1}\cup T_i\cup T_{i+1}\right|=m+2.
\tag{1.1}
\]

Thus every two-sided-rainbow depth-one forest is automatically locally
geodesic through depth two.  What it does not control is equality of the
depth-two values at different positions.  This is a real extra condition:
for a fixed \((m-2)\)-set \(S\), a depth-two window has the form

\[
S\cup\{x,y\},\quad S\cup\{y,z\},\quad S\cup\{z,w\}
\tag{1.2}
\]

with four distinct coordinates outside \(S\).  Its two lower edge colours
are the distinct facets \(S\cup\{y\}\), \(S\cup\{z\}\), and its two upper
edge colours are also distinct.  Therefore depth-one rainbowness alone does
not identify the depth-two lower colour.  The construction below enforces
all depths at once by putting the complete strip of shadow values into the
matching hyperedge.

## 2. Even cyclic strips and their Johnson cycles

Assume eventually that

\[
2\le \ell-H,\qquad H<\ell<m.
\tag{2.1}
\]

Choose disjoint sets \(C,D\subset[2m]\) with

\[
|C|=|D|=m-\ell,
\]

and let \(R=[2m]\setminus(C\cup D)\), so \(|R|=2\ell\).  Give \(R\) an
undirected cyclic order \(\gamma\).  After choosing either orientation,
write

\[
I_\gamma(t,s)=\{z_t,z_{t+1},\ldots,z_{t+s-1}\},
\qquad t\in\mathbb Z_{2\ell}.
\]

Define the strip

\[
\mathcal E(C,D,\gamma)=
\left\{
C\cup I_\gamma(t,\ell+d):
-H\le d\le H, t\in\mathbb Z_{2\ell}
\right\}.
\tag{2.2}
\]

Every row contains exactly \(2\ell\) distinct masks, so the strip size is

\[
K=2\ell(2H+1).
\tag{2.3}
\]

Its middle row

\[
T_t=C\cup I_\gamma(t,\ell),
\qquad t\in\mathbb Z_{2\ell},
\tag{2.4}
\]

is a Johnson cycle: advancing \(t\) removes \(z_t\) and inserts
\(z_{t+\ell}\).  For \(1\le q\le H\), direct cyclic-interval geometry gives

\[
\bigcap_{s=0}^qT_{t+s}
=C\cup I_\gamma(t+q,\ell-q),
\tag{2.5}
\]

and

\[
\bigcup_{s=0}^qT_{t+s}
=C\cup I_\gamma(t,\ell+q).
\tag{2.6}
\]

Thus every cyclic depth-\(q\) lower and upper shadow of (2.4) is a distinct
vertex of the corresponding strip row.

The strip parametrization is injective.  Its lowest-rank row recovers
\(C\) by intersection and \(C\cup R\) by union, hence also \(D\).  After
deleting \(C\), the family of length-\((\ell-H)\) intervals recovers the
undirected cycle: two coordinates are adjacent precisely when they occur
together in \(\ell-H-1\) of these intervals, while a nonadjacent pair occurs
together at most \(\ell-H-2\) times.  Therefore the strip hypergraph below
is an ordinary simple hypergraph.

## 3. Exact degrees and codegrees

Let \(\mathcal G=\mathcal G(m,H,\ell)\) be the simple \(K\)-uniform
hypergraph with vertex set

\[
V(\mathcal G)=
\bigsqcup_{d=-H}^H\binom{[2m]}{m+d}
\tag{3.1}
\]

and all strips (2.2) as edges.

There are

\[
|E(\mathcal G)|=
\frac{(2m)!}{4\ell\,(m-\ell)!^2}
\tag{3.2}
\]

edges.  By symmetry and double counting, a rank-\((m+d)\) vertex has degree

\[
D_d=
\frac{(m+d)!(m-d)!}{2(m-\ell)!^2}.
\tag{3.3}
\]

The minimum is \(D_0\), the maximum is \(D=D_H=D_{-H}\), and

\[
\frac D{D_0}
=\frac{(m+H)!(m-H)!}{m!^2}
=\exp\!\left(O\!\left(\frac{H^2}{m}\right)\right).
\tag{3.4}
\]

In particular every degree lies in

\[
\left(1-O(H^2/m)\right)D\le D_d\le D.
\tag{3.5}
\]

Also, uniformly in the parameter range used here,

\[
\log D=(2+o(1))\ell\log m.
\tag{3.6}
\]

Let \(\Gamma\) be the maximum pair-codegree.  Fix distinct band vertices
\(X,Y\).  The stabilizer

\[
\mathfrak S_X\times\mathfrak S_{[2m]\setminus X}
\]

has orbit on \(Y\) of size

\[
\binom{|X|}{|X\cap Y|}
\binom{2m-|X|}{|Y\setminus X|}.
\tag{3.7}
\]

Every strip containing \(X\) has only \(2\ell\) vertices in the rank of
\(Y\), and all members of the orbit have the same codegree with \(X\).
The orbit has size at least \(m-H\).  Indeed, orbit size one is possible only
for \(Y\in\{\varnothing,X,X^c,[2m]\}\); the first and last lie outside the
band, \(Y=X\) is excluded, and \(X^c\) cannot co-occur with \(X\) because
every strip member contains the nonempty core \(C\).  Every other binomial
product in (3.7) is at least \(m-H\).  Hence

\[
\boxed{
\frac\Gamma D\le\frac{2\ell}{m-H}.
}
\tag{3.8}
\]

## 4. The quantitative matching theorem applies

We use the near-regular matching form of the
[Alon--Bollobas--Kim--Vu theorem](https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf),
Theorem 3.9.  For an ordinary (no parallel edges)
\(K\)-uniform hypergraph of maximum degree \(D\), maximum pair-codegree at
most \(C\), and all degrees
at least

\[
D-f(D),\qquad
f(D)=20(D^2C\log D)^{1/3},
\]

if \(K>4\), \(K\le\tfrac12\log D\), \(f(D)\le D/10\), and

\[
e^{2K}C\log D=o(D),
\tag{4.1}
\]

then there is a matching leaving at most

\[
O\!\left(
K\left(\frac{C\log(1+C)}D\right)^{1/(K-1)}
|V(\mathcal G)|
\right)
\tag{4.2}
\]

vertices uncovered.  This is the \(B=\varnothing\) case of their
Theorem 3.9.

Take

\[
C_*:=\left\lceil\frac{2\ell D}{m-H}\right\rceil.
\tag{4.3}
\]

Equation (3.8) gives \(\Gamma\le C_*\).  In the theorem's functions
\(f(D)\) and residual bound we use this upper codegree parameter \(C_*\)
(enlarging an upper bound on the actual codegree is harmless).  From (0.2),

\[
\ell=(1+o(1))\omega H^2,
\qquad
K=(4+o(1))\omega H^3
\le(1+o(1))\frac{L}{16\lambda}.
\tag{4.4}
\]

In view of (3.6), this also gives \(K=o(\log D)\), and hence the auxiliary
condition \(K\le\tfrac12\log D\).

The relative degree defect in (3.5) satisfies

\[
\frac{H^2}{m}
=o\!\left[
\left(\frac{C_*\log D}{D}\right)^{1/3}
\right],
\tag{4.5}
\]

because the expression in brackets is at least a constant multiple of
\((\ell\log D/m)^{1/3}\), while all \(H,\ell\) here are polylogarithmic.
Alternatively one may use the upper parameter \(C_*\) itself in \(f(D)\),
which only enlarges the permitted defect.  Also

\[
\frac{f(D)}D
=O\!\left[
\left(\frac{\ell^2L}{m}\right)^{1/3}
\right]=o(1).
\tag{4.6}
\]

Moreover, by (3.6), (4.3), and (4.4),

\[
\log\left(
e^{2K}\frac{C_*\log D}{D}
\right)
\le
-L+2K+O(\log(\ell^2L))
=-L+o(L),
\tag{4.7}
\]

so (4.1) holds.

Finally put

\[
\eta=\frac{C_*\log(1+C_*)}{D}.
\]

Since \(\log(1+C_*)=O(\log D)=O(\ell L)\),

\[
\eta=O\!\left(\frac{\ell^2L}{m}\right),
\qquad
\log\eta=-L+O(\lambda).
\tag{4.8}
\]

The upper bound on \(K\) in (4.4) gives

\[
\eta^{1/(K-1)}\le L^{-16+o(1)}.
\tag{4.9}
\]

Also

\[
|V(\mathcal G)|\le(2H+1)W.
\]

Substitution into (4.2) yields an uncovered count

\[
U_m
\le
O\!\left(K(2H+1)L^{-16+o(1)}W\right)
\le W L^{-10}
\tag{4.10}
\]

for all sufficiently large \(m\).  This proves (0.5).

## 5. Cut the matched cycles into paths

Let the matching contain \(p_m\) strip edges.  Their middle rows are
pairwise vertex-disjoint Johnson cycles, and every selected depth-\(q\)
shadow is globally distinct, because the matching is disjoint in every rank
class.

Cut one edge of each cycle and retain the path

\[
T_0,T_1,\ldots,T_{2\ell-1}.
\tag{5.1}
\]

For every \(q\le H\), this path keeps exactly \(2\ell-q\) of the
\(2\ell\) cyclic lower windows and exactly \(2\ell-q\) of the cyclic upper
windows.  Therefore the missing counts are exactly

\[
M_q^-=N_q-p_m(2\ell-q),
\qquad
M_q^+=N_q-p_m(2\ell-q).
\tag{5.2}
\]

If \(U_m\) is the total number of band vertices uncovered by the matching,
then

\[
U_m=
\bigl(W-2\ell p_m\bigr)
+2\sum_{q=1}^H\bigl(N_q-2\ell p_m\bigr).
\tag{5.3}
\]

Consequently

\[
\sum_{q=1}^H(M_q^-+M_q^+)
=U_m-\bigl(W-2\ell p_m\bigr)
+p_mH(H+1)
\le U_m+p_mH(H+1).
\tag{5.4}
\]

Every coordinate in \(C\) is present throughout (5.1), every coordinate in
\(D\) is absent throughout, and every coordinate in \(R\) has one cyclic
one-run of length \(\ell\).  After the cut, that run is either one internal
run of length \(\ell\), or it is split into two boundary runs.  Since
\(\ell>H\),

\[
\rho_H(\mathcal P_m)=0.
\tag{5.5}
\]

Finally, middle disjointness gives

\[
p_m\le\frac W{2\ell}.
\]

Using (5.4)--(5.5),

\[
\begin{aligned}
Hp_m+\sum_{q=1}^H(M_q^-+M_q^+)
&\le U_m+p_m(H^2+2H)\\
&\le U_m+\frac{H^2+2H}{2\ell}W\\
&=U_m+\left(\frac1{2\omega}+o(1)\right)W\\
&=o(W).
\end{aligned}
\tag{5.6}
\]

This proves (0.3)--(0.7).

## 6. A sharp ceiling for independently cut strip matchings

The cube-root scale is not merely an arbitrary choice of parameters for this
specific architecture.

Suppose a strip matching covers all but \(o(W)\) middle vertices.  Then

\[
p_m=(1-o(1))\frac{W}{2\ell}.
\tag{6.1}
\]

If every selected cycle is cut independently and no crossing window between
different cycles is credited, (5.2) shows that the cut creates exactly

\[
p_mH(H+1)
\tag{6.2}
\]

missing signed shadow slots in total.  Since the retained values are globally
distinct, this is also the exact additional missing-mask count.  Therefore
an \(o(W)\) gate charge forces

\[
\frac{H^2}{\ell}=o(1).
\tag{6.3}
\]

There is also a lower codegree bound.  Fix a middle set \(X\).  In every
strip containing \(X\), exactly two rank-\((m+1)\) strip members are immediate
supersets of \(X\).  The stabilizer of \(X\) is transitive on its \(m\)
immediate supersets, so each such pair has codegree \(2D_0/m\).  Hence

\[
\Gamma\ge\frac{2D_0}{m}
=\frac{2D}{m}(1-o(1)).
\tag{6.4}
\]

If the same full-strip hypergraph is certified by the displayed ABKV
hypothesis

\[
e^{2K}\Gamma\log D=o(D),
\]

then (3.6), (6.4), and \(K=(4+o(1))\ell H\) imply

\[
8\ell H\le(1+o(1))\log m.
\tag{6.5}
\]

Combining (6.3) and (6.5),

\[
H^3=\frac{H^2}{\ell}(\ell H)=o(\log m),
\qquad
H=o((\log m)^{1/3}).
\tag{6.6}
\]

This is a ceiling only for the architecture consisting of one full-strip
ABKV matching followed by independent cycle cuts.  A safe splice can recover
the crossing windows lost in (6.2), so (6.6) is not an obstruction to the
reduced Johnson-path gate itself.  It pinpoints the required new operation:
the cycles must be joined while preserving new multidepth colours and long
coordinate runs.

## 7. Exact scope

The theorem gives a quantitative, zero-short-run solution of the reduced
Johnson-path gate through a cube-root polylogarithmic depth.  It improves the
previous rate-free diagonal implication of the fixed-depth cyclic-block
packing and makes explicit that depth-two/three compatibility itself is not
the obstruction.

It does not improve the already deeper queue-rounding band.  Its value is
structural: it stays entirely within a vertex-disjoint Johnson path family,
has globally unique certified shadows before the unavoidable cycle cuts, and
enters the endpoint-capped erosion theorem with \(\rho_H=0\).  Reaching
\(H\asymp\sqrt{m\log\log m}\) requires replacing the independent cycle cuts
by a multidepth-safe splice or absorber; the generic strip matching pays
\(H(H+1)\) lost shadow windows per component.
