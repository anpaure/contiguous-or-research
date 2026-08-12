# Repaired promotion rings: an EKR theorem and the absence of large nonstar cliques

Date: 2026-07-26

## 0. Statement

Use the packing-side repaired-ring hypergraph \(\mathcal G\) from the
packing-side codegree note. Thus

\[
 M=m+H,\qquad H=(1+o(1))\sqrt{m\log m}.
\]

An edge consists of one rank-\(M\) top (the **root**) and \(M-1\) of
the \(M\) cyclic \(m\)-windows on that top, and formal orientations are
retained. Write

\[
 D_T=M!,\qquad
 D_O=(M-1)\frac{(m!)^2}{(m-H)!},
\]

for the root and owner degrees, and write

\[
 C_1=
 \frac{2(M-2)((m-1)!)^2}{(m-H)!}
\]

for the maximum pair codegree. Recall

\[
 \frac{D_O}{D_T}=1-O(H/m)<1,\qquad
 \frac{C_1}{D_T}=\frac{2+o(1)}{m^2}.
\tag{0.1}
\]

### Theorem (repaired-ring EKR)

For every pairwise-intersecting family \(\mathcal A\) of formal repaired
rings, one of the following holds.

1. All members of \(\mathcal A\) contain a common vertex. Consequently
   \[
   |\mathcal A|\le
   \begin{cases}
   D_T,&\text{if the common vertex is a root},\\
   D_O,&\text{if it is an owner}.
   \end{cases}
   \]
2. The family is nonstar, and
   \[
   \boxed{
   |\mathcal A|
   \le H(M-1)m!H!
      +(M-1)\big((4+o(1))C_1\big)
   =\left(\frac8m+o\!\left(\frac1m\right)\right)D_T.}
   \tag{0.2}
   \]

It follows that, for all sufficiently large \(m\),

\[
\boxed{\omega(L(\mathcal G))=D_T=M!,}
\tag{0.3}
\]

and the only maximum cliques are the full root stars. Full owner stars
have size \(D_O=(1-O(H/m))D_T\). Every clique with no common resource
is smaller by a factor \(\Omega(m)\).

Thus the factor-\(M\) gap in the elementary greedy matching bound is
**not** explained by a clique obstruction in the line graph. Any
statewise obstruction must be a genuinely higher matching-polytope
obstruction (an odd mesh or more complicated fractional-colouring
constraint), not a large intersecting family.

## 1. Two cyclic-window lemmas

### Lemma 1.1 (at most four distance-one windows)

Let \(V\) be an \(M\)-set with a cyclic order, and let \(X\) be any
\(m\)-subset of the ambient \(2m\)-set. Among the \(M\) cyclic
\(m\)-windows \(Y\subseteq V\), at most four satisfy

\[
 d_J(X,Y)=1.
\tag{1.1}
\]

#### Proof

Put \(a=|X\setminus V|\). Since every \(Y\) is contained in \(V\),
\(d_J(X,Y)\ge a\), so only \(a=0,1\) matter.

Mark the elements of \(V\setminus X\) as zeroes in the cyclic order.
There are \(H+a\) zeroes and \(m-a\) ones. A cyclic \(m\)-window has
Johnson distance one from \(X\) exactly when it contains one zero.

List the zeroes cyclically and let \(g_i\) be the number of ones in the
gap after the \(i\)-th zero. A length-\(m\) interval containing only
the \(i\)-th zero must lie in the arc consisting of that zero and its
two adjacent one-gaps. Such an interval can exist only if

\[
 g_{i-1}+g_i+1\ge m.
\tag{1.2}
\]

For \(a=0\), \(\sum_i g_i=m\). Hence at most two indices can satisfy
\(g_{i-1}+g_i\ge m-1\), because
\(\sum_i(g_{i-1}+g_i)=2m\) and \(m\ge4\). For each such index the
available arc has length at most \(m+1\), so it contains at most two
length-\(m\) intervals. This gives at most four.

For \(a=1\), \(\sum_i g_i=m-1\). Again at most two indices satisfy
(1.2), and now each available arc has length at most \(m\), so there is
at most one interval for each. This gives at most two. \(\square\)

### Lemma 1.2 (few windows lie inside a second top)

Let \(U\ne V\) be two \(M\)-subsets, and cyclically order \(V\). At
most \(H\) cyclic \(m\)-windows of \(V\) are contained in \(U\).

#### Proof

Choose \(z\in V\setminus U\). If an \(m\)-window is contained in
\(U\), then its complementary cyclic \(H\)-window in \(V\) contains
\(z\). Exactly \(H\) cyclic \(H\)-windows contain a fixed point.
\(\square\)

## 2. Link of one vertex against one avoiding edge

For vertices \(v,w\), write \(d(v,w)\) for their codegree. If \(f\) is
an edge avoiding \(v\), put

\[
 S(v,f):=\sum_{w\in f}d(v,w).
\tag{2.1}
\]

### Lemma 2.1 (root link)

If \(v=U\) is a root and \(f\) avoids \(U\), then

\[
 S(U,f)\le H(M-1)m!H!=o(D_T/m).
\tag{2.2}
\]

#### Proof

The root of \(f\) has zero codegree with \(U\). By Lemma 1.2, at most
\(H\) owner windows of \(f\) are contained in \(U\); every other
root--owner codegree is zero. Each incident root--owner pair has
codegree \((M-1)m!H!\). This proves the first inequality. The second
follows from

\[
 \frac{H(M-1)m!H!}{D_T}
 =\frac{H(M-1)}{\binom MH}
 =\exp[-\Theta(H\log(m/H))].
\]
\(\square\)

### Lemma 2.2 (owner link)

If \(v=X\) is an owner and \(f\) avoids \(X\), then

\[
 S(X,f)\le (4+o(1))C_1.
\tag{2.3}
\]

#### Proof

The root in \(f\) contributes at most the root--owner codegree
\((M-1)m!H!=o(C_1)\). By Lemma 1.1, at most four owner windows of
\(f\) have Johnson distance one from \(X\), and each contributes
\(C_1\).

Every remaining owner has distance at least two. From the exact
pair-codegree sequence,

\[
 \frac{C_2}{C_1}=\frac4{(m-1)^2},
\tag{2.4}
\]

the values \(C_d\) decrease for \(2\le d<H\), and the endpoint
\(C_H=o(C_2)\) because

\[
 \frac{C_H}{C_1}
 =\frac{(m-H)^2(m-H+1)}
        {2\binom{m-1}{H}^{\,2}}
 =\exp[-\Theta(H\log(m/H))].
\tag{2.5}
\]

There are fewer than \(M\) remaining owners, so their total
contribution is at most \(MC_2=o(C_1)\). \(\square\)

## 3. Star peeling

### Lemma 3.1 (general peeling lemma)

Let \(\mathcal H\) be any hypergraph and let \(\mathcal A\) be a
pairwise-intersecting edge family with no common vertex. For any
\(e\in\mathcal A\), choose, for every \(v\in e\), an edge
\(f_v\in\mathcal A\) with \(v\notin f_v\). Then

\[
 |\mathcal A|
 \le\sum_{v\in e}\sum_{w\in f_v}d_{\mathcal H}(v,w).
\tag{3.1}
\]

#### Proof

Put \(\mathcal A(v)=\{g\in\mathcal A:v\in g\}\). Since every member of
\(\mathcal A\) meets \(e\),
\(\mathcal A\subseteq\bigcup_{v\in e}\mathcal A(v)\).
For \(g\in\mathcal A(v)\), pairwise intersection gives
\(g\cap f_v\ne\varnothing\). Therefore

\[
 \mathcal A(v)
 \subseteq
 \bigcup_{w\in f_v}\{g:v,w\in g\},
\]

and the union bound gives (3.1). \(\square\)

The same proof has the following weighted form. For nonnegative edge
weights \(w\), write

\[
 w(v,z):=\sum_{\substack{g\in E(\mathcal H)\\v,z\in g}}w(g).
\]

Then every nonstar intersecting \(\mathcal A\) and every choice of
witnesses as in Lemma 3.1 satisfy

\[
\boxed{
 w(\mathcal A)
 \le \sum_{v\in e}\sum_{z\in f_v} w(v,z).}
\tag{3.2}
\]

This is the appropriate weighted star-peeling statement. It does not
collapse to (0.2) for arbitrary weights: weights can be concentrated on
a small nonstar configuration, destroying the unweighted codegree
comparison. It does collapse whenever the weighted pair links obey the
same \(O(C_1/D_T)\) spread as the full catalogue.

### Proof of the theorem

If \(\mathcal A\) has a common vertex, it is contained in that vertex's
star, giving the first alternative.

Otherwise apply Lemma 3.1 to a fixed repaired ring \(e\). Its unique
root contributes the bound in Lemma 2.1, and each of its \(M-1\) owners
contributes the bound in Lemma 2.2. Hence

\[
 |\mathcal A|
 \le H(M-1)m!H!+(M-1)(4+o(1))C_1.
\]

Using \(C_1/D_T=(2+o(1))/m^2\), \(M=(1+o(1))m\), and Lemma 2.1 gives
(0.2).

Finally \(D_O<D_T\), while (0.2) is \(o(D_T)\). Therefore a largest
intersecting family is a root star; equality forces the full root star.
\(\square\)

## 4. What this does and does not rule out

The theorem completely classifies clique-scale obstructions:

| family type | maximum size |
|---|---:|
| root star | \(D_T\) |
| owner star | \(D_O=(1-O(H/m))D_T\) |
| no common resource | at most \((8+o(1))D_T/m\) |

In particular, there is no triangle-gadget analogue whose replicated
positive-weight edges form a clique larger than the design degree.

This is not yet a fractional edge-colouring theorem. A collection
\(\mathcal B\) with matching number \(r>1\) could still satisfy
\(|\mathcal B|>D_T r\) without containing a large clique. Ruling that
out requires a weighted star-peeling or odd-mesh theorem controlling
all matching-polytope constraints, not only cliques. The present result
shows exactly where the next obstruction search must look.

## 5. Small odd meshes cannot be made from full stars

The next elementary obstruction after a clique would be an odd mesh
made by gluing several large stars while preventing a transversal
matching. The root stars remain matchable far beyond every polynomial
scale.

### Proposition 5.1 (root-star transversal)

Let \(U_1,\ldots,U_r\) be distinct roots. If

\[
 r-1<\frac{\binom MH}{(M-1)^2},
\tag{5.1}
\]

then there are pairwise-disjoint repaired rings
\(e_i\in\mathcal S(U_i)\), one from every root star. Consequently the
union of these \(r\) full root stars has matching number exactly \(r\)
and edge-to-matching ratio exactly \(D_T\).

#### Proof

Choose the rings sequentially. After choosing \(t-1\) rings, fewer than
\((t-1)(M-1)\) owners have been used. Inside a fixed new root star, a
given owner lies in at most

\[
 C_{T,O}=(M-1)m!H!
\]

formal edges. Thus fewer than
\((t-1)(M-1)C_{T,O}\) of its \(D_T\) edges are forbidden. Condition
(5.1) and

\[
 \frac{D_T}{C_{T,O}}=\frac{\binom MH}{M-1}
\]

leave an available edge. Distinct roots already guarantee disjoint
tags. The upper bound \(r\) on the matching number comes from the \(r\)
root vertices. \(\square\)

The threshold in (5.1) is

\[
 \exp\!\big((1+o(1))H\log(m/H)\big),
\]

so no bounded, polylogarithmic, or polynomial number of complete root
stars can form an odd-mesh obstruction.

There is a weaker analogous owner-star statement. Any \(r\) distinct
owner stars have a transversal matching whenever

\[
 r(M+1)\Delta_2<D_O,
\]

and hence whenever \(r<(1/2-o(1))m\). Indeed, at the \(t\)-th greedy
step forbid both the vertices used previously and all other
distinguished owners.  This is fewer than \(r(M+1)\) vertices, each of
which forbids at most \(\Delta_2\) edges of the new owner star.  The
chosen edge then contains no future distinguished owner, so the
induction continues. Thus even an owner-star odd mesh must involve
\(\Omega(m)\) resources; the familiar three-star triangle obstruction
is quantitatively impossible here.
