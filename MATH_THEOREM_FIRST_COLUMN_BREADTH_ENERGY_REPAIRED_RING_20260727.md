# First column breadth energy in the repaired-ring catalogue

Date: 2026-07-27

Scope: the first missing aggregate column term in the repaired-ring
slow-greedy hierarchy.

## 0. Result

Fix a current owner \(X\).  Let \(\mathcal F_X\) be the current catalogue
edges containing \(X\), and let \(\mathcal R_X\) be the current catalogue
edges avoiding \(X\).  Put

\[
 d_X=|\mathcal F_X|,
 \qquad
 L=K\Delta_t,
\tag{0.1}
\]

where \(\Delta_t\) is the current maximum resource degree.  For
\(e\in\mathcal R_X\), write

\[
 a(e)=a_X(e)=
 |\{f\in\mathcal F_X:f\cap e\ne\varnothing\}|,
\tag{0.2}
\]

and, for \(e,g\in\mathcal R_X\),

\[
 b(e,g)=b_X(e,g)=
 |\{f\in\mathcal F_X:f\cap e\ne\varnothing,
                         f\cap g\ne\varnothing\}|.
\tag{0.3}
\]

Suppose, up to a stopping time,

\[
                         a(e)\le A
             \qquad(e\in\mathcal R_X).
\tag{0.4}
\]

Then for every \(h,\ell\ge1\),

\[
 Y_h:=\sum_{e\in\mathcal R_X}a(e)^h
 \le d_XLA^{h-1},
\tag{0.5}
\]

and

\[
 \boxed{
 \sum_{g\in\mathcal R_X}
 \left(\sum_{e\in\mathcal R_X}
        a(e)^{h-1}b(e,g)\right)^\ell
 \le d_XL^{\ell+1}A^{h\ell-1}.}
\tag{0.6}
\]

In particular, for the first missing breadth term,

\[
 \boxed{
 \sum_g\left(\sum_e a_X(e)b_X(e,g)\right)^2
 \le d_XL^3A^3.}
\tag{0.7}
\]

With the natural reference

\[
                       y_h=d_XLA^{h-1},
\tag{0.8}
\]

equation (0.6) is exactly

\[
 {1\over L}\sum_g
 \left(
 {\sum_ea(e)^{h-1}b(e,g)\over y_h}
 \right)^\ell
 \le
 \left({A\over d_X}\right)^{\ell-1}.
\tag{0.9}
\]

Thus if

\[
                         {A\over d_X}
 \le {C_z(\log m)^4\over m^2u_t},
\tag{0.10}
\]

the first aggregate column hierarchy has precisely the required
\(m^{-2}\) factor, at every moment order \(\ell\).  No additional
endpoint exposure is needed: (0.6) is a tree count.

The same estimate survives the fact that selection of \(g\) removes
protected indices \(e\) which meet \(g\).  Section 3 gives the exact
bound.

This theorem closes the first *breadth* calculation conditionally on the
stopped relative influence bound (0.4).  It does not regenerate (0.4).
That relative influence regeneration remains the next gate.

## 1. Conflict-incidence graph

Form the bipartite graph \(\mathcal B_X\) with left shore
\(\mathcal F_X\), right shore \(\mathcal R_X\), and

\[
                     f\sim e
       \quad\Longleftrightarrow\quad f\cap e\ne\varnothing.
\tag{1.1}
\]

This is a simple incidence graph; intersections of several resources are
not counted with multiplicity.  Its right degrees and right codegrees are
exactly

\[
             d_{\mathcal B_X}(e)=a(e),
 \qquad
             d_{\mathcal B_X}(e,g)=b(e,g).
\tag{1.2}
\]

Every \(f\in\mathcal F_X\) contains at most \(K\) resources, and every
resource lies in at most \(\Delta_t\) current catalogue edges.  Hence

\[
                     d_{\mathcal B_X}(f)\le K\Delta_t=L.
\tag{1.3}
\]

Assumption (0.4) is the right-degree bound

\[
                     d_{\mathcal B_X}(e)\le A.
\tag{1.4}
\]

No transitivity or product-density approximation is used below.

## 2. Tree-homomorphism proof

### Lemma 2.1

Let \(B=(U,V;E)\) be any finite bipartite graph with

\[
                  |U|=d,qquad
                  \Delta_U(B)\le L,qquad
                  \Delta_V(B)\le A.
\tag{2.1}
\]

For \(v,w\in V\), put

\[
                  a(v)=d_B(v),
 \qquad
                  b(v,w)=|N(v)\cap N(w)|.
\tag{2.2}
\]

Then, for all \(h,\ell\ge1\),

\[
 \sum_{v\in V}a(v)^h\le dLA^{h-1},
\tag{2.3}
\]

and

\[
 \sum_{w\in V}
 \left(\sum_{v\in V}a(v)^{h-1}b(v,w)\right)^\ell
 \le dL^{\ell+1}A^{h\ell-1}.
\tag{2.4}
\]

#### Proof

The left side of (2.3) counts homomorphisms into \(B\) from the star
with one centre in \(V\) and \(h\) leaves in \(U\).  Root the star at
one \(U\)-leaf.  There are at most \(d\) choices for the root, at most
\(L\) choices for the centre, and at most \(A\) choices for every one of
the other \(h-1\) leaves.  This proves (2.3).

Expand the left side of (2.4).  One factor

\[
                  a(v)^{h-1}b(v,w)
\tag{2.5}
\]

chooses a right vertex \(v\), \(h-1\) arbitrary left neighbours of
\(v\), and one further left neighbour which is adjacent to both \(v\)
and \(w\).  Taking \(\ell\) copies of (2.5) with the same \(w\) gives
the homomorphism count of a tree \(T_{h,\ell}\): it has

\[
 h\ell\ \text{left vertices},qquad
 \ell+1\ \text{right vertices},qquad
 \ell(h+1)\ \text{edges}.
\tag{2.6}
\]

Indeed the \(\ell\) length-two branches meet only at the common right
vertex \(w\), and every branch has its additional \(h-1\) left leaves.
The count includes noninjective homomorphisms, exactly as does the
expanded power, so no distinctness correction is required.

Root \(T_{h,\ell}\) at one of its left vertices.  Every one of the
\(\ell+1\) right vertices is first reached from a left vertex and costs
at most \(L\).  The remaining \(h\ell-1\) left vertices are first reached
from a right vertex and cost at most \(A\).  Hence

\[
             \operatorname{hom}(T_{h,\ell},B)
             \le dL^{\ell+1}A^{h\ell-1},
\]

which is (2.4). \(\square\)

Applying Lemma 2.1 to \(\mathcal B_X\) proves (0.5)--(0.7).

### Interpretation as a mixed row-column diagram

For \(h=2,\ell=2\), the expanded witness-incidence graph is

\[
 f_1-e-f_2-g-f_4-e'-f_3,
\tag{2.7}
\]

a seven-vertex tree.  The three right columns \(e,g,e'\) each get one
free incidence; their three second incidences each cost the right-degree
ratio \(A/d_X\).  This is the literal source of the cube
\((A/d_X)^3\) in (0.7).

## 3. Removal of protected indices

When \(g\) is selected, every protected index \(e\) which meets \(g\)
ceases to be active.  Put

\[
 R_h(g)=\sum_{e:e\cap g\ne\varnothing}a(e)^h.
\tag{3.1}
\]

The conflict graph on current catalogue edges has maximum degree at most
\(L=K\Delta_t\).  Therefore

\[
                 R_h(g)\le LA^h
\tag{3.2}
\]

and, after reversing the order of summation,

\[
                 \sum_gR_h(g)\le LY_h\le Ly_h.
\tag{3.3}
\]

Maximum times first moment gives, for every \(\ell\ge1\),

\[
\begin{aligned}
 \sum_gR_h(g)^\ell
 &\le (LA^h)^{\ell-1}Ly_h\\
 &=L y_h^\ell
       \left({A\over d_X}\right)^{\ell-1}.
\end{aligned}
\tag{3.4}
\]

For an index \(e\) disjoint from \(g\), its link count loses exactly
\(b(e,g)\) options.  Hence the total decrement \(D_h(g)\) of \(Y_h\)
satisfies

\[
 D_h(g)
 \le R_h(g)+h\sum_ea(e)^{h-1}b(e,g).
\tag{3.5}
\]

Combining (0.6), (3.4), and
\((x+y)^\ell\le2^{\ell-1}(x^\ell+y^\ell)\) yields

\[
 \boxed{
 {1\over L}\sum_g
       \left({D_h(g)\over y_h}\right)^\ell
 \le (2h)^\ell
       \left({A\over d_X}\right)^{\ell-1}.}
\tag{3.6}

Thus both sources of a jump of the aggregate mesh power have the required
column-energy scale.

## 4. High-influence tail from a higher power

The maximum hypothesis (0.4) can be softened at a fixed checkpoint.
Suppose, for some \(J>2\) and baseline \(A_0\),

\[
              \sum_ea(e)^J\le d_XLA_0^{J-1}.
\tag{4.1}
\]

For \(A=cA_0\), \(c>1\), the high-influence part obeys

\[
 \sum_{e:a(e)>A}a(e)^2
 \le A^{2-J}\sum_ea(e)^J
 \le c^{2-J}d_XLA_0.
\tag{4.2}
\]

Moreover

\[
 |\{e:a(e)>A\}|
 \le {d_XL\over c^JA_0}.
\tag{4.3}
\]

At selection rate \(1/L\), the compensator over time \(T\) of selecting
one of these high-influence edges is at most

\[
                 {T d_X\over c^JA_0}.
\tag{4.4}
\]

When \(A_0/d_X=\Theta(m^{-2})\), choosing
\(J=C_0\log m\) and a fixed \(c>1\) with \(C_0\) large makes (4.2) and
(4.4) superpolynomially small.  Thus a regenerated \(J\)-th influence
moment is enough to replace a literal all-edge maximum at one checkpoint.

This does not by itself prove that (4.1) regenerates over
\(O(m\log m)\) time.  It reduces the next dynamic gate to the high
influence moment rather than the first breadth column.

## 5. Consequence for the trajectory audit

The breadth countermodel in
`MATH_AUDIT_BUFFERED_SLOW_BITE_COLUMN_ENERGY_OBSTRUCTION_20260727.md`
shows that arbitrary row-power data do not imply column control.  The
literal repaired-ring conflict incidence has extra structure: its first
mixed diagrams are trees, and bounded left/right degrees force the exact
column estimate (3.6).

Therefore the updated status is:

\[
\boxed{
 \text{the first ACLE breadth term is proved under the stopped
 influence scale; regeneration of the high influence moment remains.}
}
\tag{5.1}

In particular, there is no literal breadth obstruction at the first
missing term.  The claimed near-perfect owner packing is still not proved,
because the moving-buffer note has not established the dynamic relative
influence/high-moment condition used in (0.4) or (4.1).

## 6. Why high-moment truncation alone does not regenerate itself

It is tempting to combine Section 4 with the column theorem, suppress all
high-influence edges, and track only

\[
                         Y_J=\sum_ea(e)^J.
\tag{6.1}
\]

This does close the quadratic-variation and large-jump sides of the
stopped martingale.  It does **not** close the predictable drift.

Expand \(Y_J\) as the number of star configurations

\[
                         (e;f_1,\ldots,f_J),
 \qquad f_i\in\mathcal F_X,quad f_i\sim e.
\tag{6.2}
\]

Such a configuration is killed when the selected catalogue edge belongs
to

\[
             \operatorname{Conf}(e)
             \cup\bigcup_{i=1}^J\operatorname{Conf}(f_i).
\tag{6.3}
\]

The product-density reference for \(Y_J\) has logarithmic decay
\((J+1+o(1))\) in slow time.  To dominate it one needs the union in
(6.3) to have size \((J+1-o(J))L\) on average.  Bonferroni shows that
this is a common-neighbourhood assertion, not a consequence of
\(a(e)\le A\).

For example, the pair-overlap correction among the \(f_i\)'s contains
the exact term

\[
 \binom J2
 \sum_{e,g}a(e)^{J-2}b(e,g)^2,
\tag{6.4}
\]

apart from the separately countable star of \(X\).  Equation (6.4) is a
weighted \(4\)-cycle count in the conflict-incidence graph.  The overlap
between the centre \(e\) and a leaf \(f_i\) also gives

\[
 J\sum_ea(e)^{J-1}
       \sum_{f\in N(e)}
       |\operatorname{Conf}(e)\cap\operatorname{Conf}(f)|.
\tag{6.5}
\]

Bounded left and right degrees control every *tree* homomorphism, which is
why Sections 2--3 close.  They do not control (6.4), a cycle.  A family
of distinct repaired paths can share a long owner segment, so their
conflict neighbourhoods can be highly coherent even when every
individual right degree is at most \(A\).

The time-zero multiplicity mesh estimates do bound (6.4)--(6.5) at the
required scale.  What has not been proved is their regeneration after
dependent restrictions.  In the compensated-bite version, a compensation
coin at one resource creates the same issue with a resource column in
place of \(g\).

Therefore:

\[
\boxed{
 \text{high-influence truncation closes the first column moments, but
 a dynamic weighted }C_4\text{/common-neighbourhood bound is still
 required for drift.}
}
\tag{6.6}

This is the precise failure of a buffer-free proof based only on \(Y_J\).
