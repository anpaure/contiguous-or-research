# Fifth-wave K: Hall--cyclomatic expansion and its sharp Johnson obstruction

## Executive verdict

Put

\[
W=\binom{2m}{m},
\qquad
N_q=\binom{2m}{m-q},
\qquad
K=m+1,
\]

and

\[
t_q=K-q,
\qquad
s_q=\left\lfloor K\frac{N_q}{W}\right\rfloor,
\qquad
d_q=t_q-s_q.
\]

A complementary geodesic has \(t_q\) genuine internal flags in each signed
depth-\(q\) row.  The Hall target asks to retain \(s_q\) distinct flags per
path, so \(d_q\) is the discard allowance.

The fifth-wave attack does not prove the desired near-spanning Hall theorem.
It proves a sharp obstruction to deriving that theorem from Johnson
geodesicity, middle disjointness, depth-one rainbowness, pairwise expansion,
or projected girth alone.

The principal conclusions are these.

1.  The Hall deficiency is exactly a matroid-union nullity and exactly a
    collision-budget excess:

    \[
    \delta_q^\sigma
    =
    \max_{\mathcal X}
    \left(
    \sum_S(\mu_{\mathcal X}(S)-1)_+
    -d_q|\mathcal X|
    \right)_+.
    \]

    Thus flag rounding itself has no integrality gap.  Every obstruction is
    already present in the selected path blocks.

2.  The quota satisfies the exact universal bound

    \[
    d_q\le q(q-1).
    \]

3.  Two admissible complementary paths cannot share lower depth-\(q\) flags
    at row separations \(q-1,q,q+1\).  These are three sharp necessary
    consequences of the physical resource rows: the corresponding unions would be,
    respectively, a common lower first colour, a common middle mask, or a
    common upper first colour.

4.  That three-distance restriction is not enough.  An explicit
    cap-swapped braid of \(R=q+2\) genuine complementary paths has disjoint
    middle rows and separately disjoint physical lower and upper first rows,
    yet has exact lower depth-\(q\) deficiency

    \[
    \delta_q^-=
    \left((R-1)h-Rd_q\right)_+,
    \]

    where \(h\sim m/2\) flags form a common core.

    A completely finite instance exists for every \(q\ge2\):

    \[
    m=q(2q+3),
    \qquad
    R=q+2,
    \qquad
    h=q^2,
    \qquad
    \delta_q^-\ge2q>0.
    \]

    Hence exact Hall can fail at the genuinely growing Gaussian depth

    \[
    q=(1/\sqrt2+o(1))\sqrt m.
    \]

5.  Along the cap-braid parameter sequences with \(q/\sqrt m\to A\), the
    common-core obstruction has the sharp normalized limit

    \[
    \frac{\delta_q^-}{Rm}
    \longrightarrow
    \left(e^{-A^2}-\frac12\right)_+.
    \]

    Its exact phase boundary is

    \[
    A_{\rm core}=\sqrt{\log2}.
    \]

    The sharp two-path boundary is smaller:

    \[
    A_2=\sqrt{\log(4/3)}.
    \]

    In the interval \(A_2<A<A_{\rm core}\), every two-route subfamily of the
    construction passes Hall asymptotically, while the full
    \(\Theta(\sqrt m)\)-route family fails.  Pairwise dispersion is therefore
    rigorously insufficient.

6.  At depth two the exact maximum two-path deficiency is

    \[
    \left(
    \left\lceil\frac{m-1}{4}\right\rceil-4
    \right)_+.
    \]

    There are also depth-two examples whose projected union is a cactus of
    arbitrarily large girth and maximum degree four but whose Hall deficiency
    grows.  Girth is not a substitute for cyclomatic control.

7.  A fixed complementary-path factor with macroscopic internal defect
    cannot be repaired by deleting \(o(B/H)\) paths, where
    \(B=W/(m+1)\).  More precisely, after deleting \(z\) paths,

    \[
    \delta_q^\sigma
    \ge
    \left(
    D_{q,\mathrm{int}}^\sigma-f_q-s_qz
    \right)_+,
    \qquad
    f_q=N_q-Bs_q.
    \]

    At depth one, a defect \(\varepsilon W\) forces
    \(z\ge(\varepsilon+o(1))B\).  Thus the frozen odd-cut factor, global
    coordinate permutations, and every static Catalan-tail rebundling which
    retains its macroscopic first-shadow defect are excluded from this Hall
    route.

The local braid has only polynomially many paths and polynomial deficiency,
so it does not by itself contradict the permitted global condition
\(\sum_{q,\sigma}\delta_q^\sigma=o(W)\).  The surviving task is a genuinely
global selection theorem which avoids a positive density of these
uncrossed deficient cores.

No web search, finite search, or computational experiment is used below.

---

## 1. Exact Hall, collision, and quota normalizations

Fix one sign \(\sigma\) and one depth \(q\ge2\).  Let \(\mathcal P\) be a
family of complementary paths and let

\[
\mathcal I_q^\sigma(P)
\]

be the set of its \(t_q\) genuine internal signed depth-\(q\) flags.  These
flags are distinct on each individual path.  For
\(\mathcal X\subseteq\mathcal P\), write

\[
N_q^\sigma(\mathcal X)
=
\bigcup_{P\in\mathcal X}\mathcal I_q^\sigma(P)
\]

and

\[
\delta_q^\sigma(\mathcal P)
=
\max_{\mathcal X\subseteq\mathcal P}
\left(
s_q|\mathcal X|-|N_q^\sigma(\mathcal X)|
\right)_+.
\tag{1.1}
\]

### Theorem 1.1 (exact collision-hypergraph form)

For a flag \(S\), let

\[
\mu_{\mathcal X}(S)
=
\#\{P\in\mathcal X:S\in\mathcal I_q^\sigma(P)\},
\]

and put

\[
\kappa_q^\sigma(\mathcal X)
=
\sum_S(\mu_{\mathcal X}(S)-1)_+.
\tag{1.2}
\]

Then

\[
\boxed{
\delta_q^\sigma(\mathcal P)
=
\max_{\mathcal X\subseteq\mathcal P}
\left(
\kappa_q^\sigma(\mathcal X)-d_q|\mathcal X|
\right)_+.
}
\tag{1.3}
\]

Equivalently, for every repeated flag one must choose at most one keeper;
every other occurrence consumes one discard slot, and every path has
capacity \(d_q\).

#### Proof

There are \(t_q|\mathcal X|\) flag occurrences and
\(|N_q^\sigma(\mathcal X)|\) distinct flags.  Therefore

\[
\kappa_q^\sigma(\mathcal X)
=t_q|\mathcal X|-|N_q^\sigma(\mathcal X)|.
\]

Since \(s_q=t_q-d_q\), the expression in (1.1) is exactly

\[
\kappa_q^\sigma(\mathcal X)-d_q|\mathcal X|.
\]

Taking the positive maximum proves (1.3).  The keeper interpretation is the
same identity read occurrence by occurrence.  \(\square\)

### Exact cyclomatic and pseudoarboricity forms

For \(\mathcal X\subseteq\mathcal P\), form the image multigraph
\(\Gamma_q^\sigma(\mathcal X)\) whose vertices are its distinct
depth-\(q\) flags and whose edge occurrences join consecutive flags along
each source row; retain parallel edges.  Let \(g_q^\sigma(\mathcal X)\) be
its component count and \(\beta_q^\sigma(\mathcal X)\) its cyclomatic
number.  Since every source row contributes \(t_q-1\) edges,

\[
\beta_q^\sigma(\mathcal X)
=(t_q-1)|\mathcal X|-|N_q^\sigma(\mathcal X)|
+g_q^\sigma(\mathcal X).
\]

Consequently,

\[
\kappa_q^\sigma(\mathcal X)
=\beta_q^\sigma(\mathcal X)
+|\mathcal X|-g_q^\sigma(\mathcal X),
\]

and Theorem 1.1 is equivalently

\[
\boxed{
\delta_q^\sigma
=
\max_{\mathcal X\subseteq\mathcal P}
\left(
\beta_q^\sigma(\mathcal X)
-(d_q-1)|\mathcal X|
-g_q^\sigma(\mathcal X)
\right)_+.
}
\tag{1.3a}
\]

If every flag has multiplicity at most two, form the collision multigraph
\(C_q^\sigma\) on the paths, with one edge for each shared flag.  Then

\[
\kappa_q^\sigma(\mathcal X)
=|E(C_q^\sigma[\mathcal X])|,
\]

so Hall is equivalent to

\[
|E(C_q^\sigma[\mathcal X])|
\le d_q|\mathcal X|
\quad\text{for every }\mathcal X.
\tag{1.3b}
\]

Equivalently, \(C_q^\sigma\) admits an orientation of maximum indegree at
most \(d_q\); equivalently, its pseudoarboricity is at most \(d_q\), so its
edge set decomposes into \(d_q\) pseudoforests, or is independent in the
union of \(d_q\) bicircular matroids.  To see the orientation directly,
orient each collision toward the path which discards that flag.  Conversely,
the capacitated endpoint-assignment Hall theorem says that (1.3b) is exactly
the condition for such an orientation.

### Theorem 1.2 (exact matroid-union nullity)

Let

\[
\Omega
=
\{(P,S):P\in\mathcal P,\ S\in\mathcal I_q^\sigma(P)\}.
\]

On \(\Omega\), let \(M_D\) be the partition matroid with capacity \(d_q\)
on each path class, and let \(M_K\) be the partition matroid with capacity
one on each flag class.  Then a valid \(s_q\)-per-path decoration exists if
and only if

\[
\Omega\in M_D\vee M_K.
\]

More strongly,

\[
\boxed{
|\Omega|-r_{M_D\vee M_K}(\Omega)
=
\delta_q^\sigma(\mathcal P).
}
\tag{1.4}
\]

#### Proof

A decomposition \(\Omega=D\sqcup K_0\), with \(D\) independent in \(M_D\)
and \(K_0\) independent in \(M_K\), discards at most \(d_q\) occurrences
per path and keeps at most one occurrence of every flag.  It therefore
keeps at least \(s_q\) unique flags per path; excess keepers may be trimmed.
The converse follows by taking the complement of a valid decoration as the
discard set.

For the rank identity, the matroid-union formula gives

\[
|\Omega|-r_{M_D\vee M_K}(\Omega)
=
\max_{A\subseteq\Omega}
\left(
|A|-r_D(A)-r_K(A)
\right).
\tag{1.5}
\]

If \(a_P\) is the number of incidences of \(A\) on path \(P\), then the
quantity in parentheses is

\[
\sum_P(a_P-d_q)_+-|F(A)|,
\tag{1.6}
\]

where \(F(A)\) is the set of flags represented in \(A\).  Remove all
incidences on paths with \(a_P\le d_q\); this cannot decrease (1.6).
Then complete each remaining path to all of its \(t_q\) incidences.  Every
added incidence raises the first term by one and the flag term by at most
one, so (1.6) again cannot decrease.  The result is the complete incidence
set of some path family \(\mathcal X\), where (1.6) becomes

\[
(t_q-d_q)|\mathcal X|-|N_q^\sigma(\mathcal X)|
=
s_q|\mathcal X|-|N_q^\sigma(\mathcal X)|.
\]

This is exactly (1.1).  \(\square\)

Thus arbitrary correlation in the keeper rounding cannot bypass Hall:
the fractional bipartite assignment polytope is integral, and its exact
rank deficit is already \(\delta_q^\sigma\).

### Lemma 1.3 (exact discard bound)

For every \(2\le q\le m\),

\[
\boxed{
d_q
=
\left\lceil
(m+1)\left(1-\frac{N_q}{W}\right)
\right\rceil-q
\le q(q-1).
}
\tag{1.7}
\]

#### Proof

Write

\[
\frac{N_q}{W}
=
\prod_{j=0}^{q-1}(1-u_j),
\qquad
u_j=\frac{2j+1}{m+j+1}.
\]

Since \(K=m+1\) is integral,

\[
\lfloor K(1-x)\rfloor=K-\lceil Kx\rceil,
\]

which gives the equality in (1.7).  Also

\[
1-\prod_{j<q}(1-u_j)\le\sum_{j<q}u_j.
\]

For \(q\ge2\),

\[
K\sum_{j<q}u_j
=
\sum_{j<q}(2j+1)\frac{m+1}{m+j+1}
<\sum_{j<q}(2j+1)
=q^2.
\]

Hence the ceiling in (1.7) is at most \(q^2\), proving
\(d_q\le q^2-q\).  \(\square\)

For later use put

\[
B=\frac{W}{m+1},
\qquad
f_q=N_q-Bs_q.
\tag{1.8}
\]

Then

\[
0\le f_q<B.
\tag{1.9}
\]

For each fixed \(q\ge2\), as \(m\to\infty\),

\[
(m+1)\frac{N_q}{W}
=
m+1-q^2
+\frac{q^2(q^2-1)}{2m}
+O_q(m^{-2}).
\tag{1.10}
\]

Consequently, for all sufficiently large \(m\),

\[
s_q=m+1-q^2,
\qquad
d_q=q(q-1),
\tag{1.11}
\]

and

\[
f_q
=
\left(
\frac{q^2(q^2-1)}2+o_q(1)
\right)\frac{W}{m^2}.
\tag{1.12}
\]

At depth two these formulas are exact for \(m\ge5\):

\[
s_2=m-3,
\qquad
d_2=2,
\qquad
f_2=\frac{6W}{(m+1)(m+2)}.
\tag{1.13}
\]

---

## 2. Positive expansion criteria and uncrossed cores

The exact normalization gives useful sufficient criteria, but the Johnson
geometry will not supply them automatically.

### Proposition 2.1 (reciprocal-multiplicity expansion)

Let

\[
\mu(S)=\#\{P\in\mathcal P:S\in\mathcal I_q^\sigma(P)\}.
\]

If every path satisfies

\[
\boxed{
\sum_{S\in\mathcal I_q^\sigma(P)}\frac1{\mu(S)}
\ge s_q,
}
\tag{2.1}
\]

then all-subfamily Hall holds.

Equivalently, it suffices that every path have reciprocal collision load

\[
\sum_{S\in\mathcal I_q^\sigma(P)}
\left(1-\frac1{\mu(S)}\right)
\le d_q.
\tag{2.2}
\]

#### Proof

For every \(\mathcal X\subseteq\mathcal P\),

\[
\begin{aligned}
|N_q^\sigma(\mathcal X)|
&\ge
\sum_S\frac{\mu_{\mathcal X}(S)}{\mu(S)}\\
&=
\sum_{P\in\mathcal X}
\sum_{S\in\mathcal I_q^\sigma(P)}\frac1{\mu(S)}
\ge s_q|\mathcal X|.
\end{aligned}
\]

This is Hall.  \(\square\)

If every flag has multiplicity at most \(M\), then

\[
|N_q^\sigma(\mathcal X)|
\ge\frac{t_q}{M}|\mathcal X|.
\]

Therefore

\[
\boxed{
\max_S\mu(S)\le M
\quad\text{and}\quad
Ms_q\le t_q
\quad\Longrightarrow\quad
\delta_q^\sigma=0.
}
\tag{2.3}
\]

When \(q/\sqrt m\to A\), condition \(Ms_q\le t_q\) holds with a fixed
margin throughout the strict range

\[
A>\sqrt{\log M}.
\tag{2.4}
\]

Equality is a floor-sensitive boundary and is not needed below.

This is a genuine rankwise positive expansion theorem.  It does not solve
the multirank target because the shallow ranks have \(s_q/t_q\to1\), where
even multiplicity two is too large.

### Proposition 2.2 (supermodular deficiency cores)

Define

\[
\phi(\mathcal X)
=
s_q|\mathcal X|-|N_q^\sigma(\mathcal X)|.
\tag{2.5}
\]

Then \(\phi\) is supermodular:

\[
\phi(A\cup C)+\phi(A\cap C)
\ge\phi(A)+\phi(C).
\tag{2.6}
\]

If \(\delta_q^\sigma>0\), the maximum-deficiency path sets are closed under
union and intersection.  Hence there are unique nonempty minimal and maximal
maximum-deficiency cores.

Any switch which changes only paths outside the minimal core cannot reduce
the old deficiency: that core remains a witness of the same value, although
a larger new deficiency may appear.  If \(u_P\) is the number of flags unique to \(P\)
inside that minimal core \(\mathcal C\), then

\[
\phi(\mathcal C)-\phi(\mathcal C\setminus\{P\})
=s_q-u_P\ge1,
\]

so

\[
u_P\le s_q-1.
\tag{2.7}
\]

Every path of a minimal deficient core therefore has at least \(d_q+1\)
internally repeated flag incidences.

#### Proof

Neighborhood cardinality is submodular, so (2.6) follows after subtracting
it from the modular function \(s_q|\mathcal X|\).  If two sets both attain
the positive maximum \(\delta_q^\sigma\), (2.6) and maximality force their
union and intersection to attain the same value; the intersection cannot be
empty because \(\phi(\varnothing)=0\).  Intersecting and unioning all
maximizers gives the unique extremal cores.  Minimality then makes
\(\phi(\mathcal C\setminus\{P\})<\phi(\mathcal C)\), yielding (2.7).
\(\square\)

### Proposition 2.3 (augmentation and replacement)

Suppose \(\mathcal P\) is Hall-feasible and \(Q\) is another path.  Then

\[
\mathcal P\cup\{Q\}\text{ is Hall-feasible}
\]

if and only if, for every \(\mathcal X\subseteq\mathcal P\),

\[
\boxed{
|\mathcal I_q^\sigma(Q)\setminus N_q^\sigma(\mathcal X)|
\ge s_q+\phi(\mathcal X).
}
\tag{2.8}
\]

In particular, the strong greedy rule

\[
|\mathcal I_q^\sigma(Q)\cap N_q^\sigma(\mathcal P)|
\le d_q
\tag{2.9}
\]

preserves Hall.

If two equal-size path families differ by \(z\) path replacements, then

\[
\boxed{
\left|
\delta_q^\sigma(\mathcal P)
-\delta_q^\sigma(\mathcal P')
\right|
\le s_qz.
}
\tag{2.10}
\]

#### Proof

The only new Hall sets contain \(Q\).  For
\(\mathcal X\subseteq\mathcal P\), their inequality is

\[
s_q(|\mathcal X|+1)
\le
|N_q^\sigma(\mathcal X)|
+|\mathcal I_q^\sigma(Q)\setminus N_q^\sigma(\mathcal X)|,
\]

which rearranges to (2.8).  Since \(\phi(\mathcal X)\le0\) and
\(N_q^\sigma(\mathcal X)\subseteq N_q^\sigma(\mathcal P)\), (2.9) is
sufficient.

Let \(\mathcal P_0=\mathcal P\cap\mathcal P'\).  Adding one path cannot
destroy an old deficient subfamily and can increase the maximum by at most
\(s_q\).  Hence both \(\delta_q^\sigma(\mathcal P)\) and
\(\delta_q^\sigma(\mathcal P')\) lie in the interval

\[
\left[
\delta_q^\sigma(\mathcal P_0),
\delta_q^\sigma(\mathcal P_0)+s_qz
\right].
\]

Their difference is therefore at most \(s_qz\), proving (2.10).
\(\square\)

The maximum-flow proof also gives a purification fact: after a maximum clone
matching leaves \(\delta_q^\sigma\) unsaturated clones, delete every path
containing one.  At most \(\delta_q^\sigma\) paths are deleted, and the
remaining family has exact Hall at that rank and sign.

### Proposition 2.4 (whole-path selection is not a matroid)

Although incidence assignment is a matroid union, the feasible complete
path blocks do not form a matroid in general.  Let \(t=s+d\) with
\(t\ge4d+2\).  Take three abstract \(t\)-flag blocks \(A,B,C\) such that

- \(A\cap B=X\) and \(A\cap C=Y\), where \(X,Y\) are disjoint and each has
  size \(2d+1\);
- \(B\cap C=\varnothing\);
- every remaining flag is private.

Then \(\{A\}\) and \(\{B,C\}\) are Hall-feasible, but

\[
|A\cup B|=|A\cup C|
=2t-(2d+1)=2s-1,
\]

so neither \(\{A,B\}\) nor \(\{A,C\}\) is feasible.  The block-exchange
axiom fails.  For the depth-two parameters \(d=2,t=m-1\), the numerical
condition holds from \(m=11\).  This is an abstract incidence example, not
claimed to be Johnson-realizable; Theorem 4.1 supplies the genuine Johnson
failure needed below.

---

## 3. The three-distance Johnson lemma

Write an oriented complementary geodesic as

\[
T_i
=
A\setminus\{p_0,\ldots,p_{i-1}\}
\cup
\{b_0,\ldots,b_{i-1}\},
\qquad
0\le i\le m.
\tag{3.1}
\]

Its lower depth-\(q\) flag at position \(i\) is

\[
F_{i,q}
=
A\setminus\{p_0,\ldots,p_{i+q-1}\}
\cup
\{b_0,\ldots,b_{i-1}\},
\qquad
0\le i\le m-q.
\tag{3.2}
\]

The row \(F_{0,q},\ldots,F_{m-q,q}\) is an isometric Johnson geodesic:

\[
d_J(F_{i,q},F_{i+r,q})=r.
\tag{3.3}
\]

### Lemma 3.1 (three forbidden distances)

Let \(P,Q\) be two complementary geodesics whose middle rows are disjoint
and whose physical lower and upper depth-one rows are separately disjoint.
If the two lower depth-\(q\) rows share two flags, then their row distance
cannot be any of

\[
\boxed{q-1,\ q,\ q+1.}
\tag{3.4}
\]

#### Proof

On one path,

\[
F_{i,q}\cup F_{i+r,q}
=
A\setminus\{p_0,\ldots,p_{i+q-1}\}
\cup
\{b_0,\ldots,b_{i+r-1}\}.
\tag{3.5}
\]

For \(r=q-1\), this is the physical lower first colour at the intervening
edge.  For \(r=q\), it is \(T_{i+q}\).  For \(r=q+1\), it is the physical
upper first colour at the intervening edge.

If two flags are common to \(P\) and \(Q\), their distance along either
projected row equals their Johnson distance by (3.3), even if their orders
are reversed.  Their union is the same set on both paths.  At the three
distances in (3.4), this contradicts, respectively, lower-first,
middle-row, or upper-first disjointness.  \(\square\)

### Lemma 3.2 (sharp three-distance density)

If \(E\) is a set of integer positions containing no pair at distance
\(q-1,q\), or \(q+1\), then every interval of \(2q\) consecutive positions
contains at most \(q-1\) points of \(E\).

#### Proof

Pair the first and second halves of a \(2q\)-interval at distance \(q\).
At most one point from each pair may be selected, so \(q\) is the only
possible larger value.  If exactly \(q\) points were selected, choose one
point from every pair and record whether it came from the lower or upper
half.  Adjacent choices cannot differ: a lower choice followed by an upper
choice has distance \(q+1\), while an upper choice followed by a lower one
has distance \(q-1\).  Hence all choices lie in one half.  They then form
\(q\) consecutive points, whose two endpoints have distance \(q-1\), again
forbidden.  \(\square\)

It follows that for two admissible paths

\[
|\mathcal I_q^-(P)\cap\mathcal I_q^-(Q)|
\le
\frac{q-1}{2q}\,t_q+O(q).
\tag{3.6}
\]

If

\[
m=q(2M+1),
\tag{3.7}
\]

then \(t_q=2qM+1\), and the exact bound is

\[
\boxed{
|\mathcal I_q^-(P)\cap\mathcal I_q^-(Q)|
\le M(q-1)+1.
}
\tag{3.8}
\]

The construction in the next section attains (3.8).

For arbitrary \(n=m-q>q+1\), define

\[
E_0
=
\bigcup_{j\ge0}
\bigl([2qj,2qj+q-2]\cap[0,n]\bigr).
\tag{3.9}
\]

Delete from \(E_0\) any points at distance \(q-1,q\), or \(q+1\) from
\(n\), and then adjoin \(n\).  The resulting set \(E\) contains \(0,n\),
avoids the three forbidden distances, and satisfies

\[
|E|
\ge
(q-1)\left\lfloor\frac{n+1}{2q}\right\rfloor-3.
\tag{3.10}
\]

Two cap-swapped paths realize exactly this common-position set: use the
identity active order on the first path and, on the second, reverse each
block between consecutive points of \(E\).  Proper prefix sets disagree
inside every nontrivial block and agree at its endpoints.  The same
prefix-signature proof as in Theorem 4.1 excludes all middle and physical
depth-one collisions.  Thus (3.6) is asymptotically attained for every
sequence \(q\to\infty\), \(q=o(m)\), not merely on the divisible family
(3.7).

For \(q=2\), the forbidden distances are \(1,2,3\), so shared positions are
four-separated.  For every \(m\),

\[
\boxed{
|\mathcal I_2^-(P)\cap\mathcal I_2^-(Q)|
\le
\left\lceil\frac{m-1}{4}\right\rceil.
}
\tag{3.11}
\]

This bound is also attained.

---

## 4. Exact cap-braid construction

We now construct a genuine Johnson family which attains the common-position
density and violates all-subfamily Hall.

### Theorem 4.1 (the \(R\)-route cap braid)

Fix integers

\[
q\ge2,
\qquad
M\ge1,
\qquad
2\le R\le q+2,
\]

and put

\[
m=q(2M+1),
\qquad
n=m-q=2qM.
\tag{4.1}
\]

There exist \(R\) complementary geodesics with all of the following
properties.

1. Their middle rows are pairwise disjoint.
2. Their physical lower depth-one rows are pairwise disjoint.
3. Their physical upper depth-one rows are pairwise disjoint.
4. Their lower depth-\(q\) rows share exactly

   \[
   h=M(q-1)+1
   \tag{4.2}
   \]

   common flags, and every other lower depth-\(q\) flag belongs to exactly
   one route.

Consequently, for an \(a\)-route subfamily,

\[
\left|\bigcup\mathcal I_q^-\right|
=a t_q-(a-1)h,
\tag{4.3}
\]

and its raw Hall excess is

\[
\phi_a=(a-1)h-a d_q.
\tag{4.4}
\]

If the full family is deficient, its exact deficiency is

\[
\boxed{
\delta_q^-=(R-1)h-Rd_q.
}
\tag{4.5}
\]

#### Construction

Partition the \(2m\) coordinates into

\[
X=\{x_1,\ldots,x_n\},
\qquad
Y=\{y_1,\ldots,y_n\},
\qquad
Z=\{z_0,\ldots,z_{2q-1}\}.
\]

The set \(Z\) is cyclically ordered.  Define the common prefix-index set

\[
E
=
\bigcup_{j=0}^{M-1}
\{2qj,2qj+1,\ldots,2qj+q-2\}
\cup\{n\}.
\tag{4.6}
\]

Thus \(|E|=h\).  Consecutive elements of \(E\) have gap one or \(q+2\), and
no two elements of \(E\) differ by \(q-1,q\), or \(q+1\).

For \(0\le a<R\), define a permutation \(\pi_a\) of \([n]\) as a direct sum
over the blocks between consecutive elements of \(E\).  On a unit block use
its unique order.  On every block of length \(q+2\), use the \(a\)-th cyclic
rotation.  The \(R\le q+2\) rotations have pairwise distinct proper prefix
sets.  Therefore, for \(a\ne b\),

\[
\boxed{
\pi_a([i])=\pi_b([i])
\quad\Longleftrightarrow\quad
i\in E.
}
\tag{4.7}
\]

For \(0\le a<R\), let

\[
A_a=\{z_a,z_{a+1},\ldots,z_{a+q-1}\},
\qquad
C_a=Z\setminus A_a,
\tag{4.8}
\]

with indices modulo \(2q\).  Route \(P_a\) starts at

\[
T_0^{(a)}=X\cup A_a.
\]

Its departure word is

\[
z_a,z_{a+1},\ldots,z_{a+q-1},
x_{\pi_a(1)},\ldots,x_{\pi_a(n)},
\tag{4.9}
\]

and its entry word is

\[
y_{\pi_a(1)},\ldots,y_{\pi_a(n)},
z_{a+q},\ldots,z_{a+2q-1}.
\tag{4.10}
\]

The terminal set is \(Y\cup C_a=(T_0^{(a)})^c\), so these are genuine
complementary geodesics.

#### Proof of resource disjointness

The pair

\[
\left(|S\cap X|,|S\cap Y|\right)
\]

determines the row index of any middle, physical lower-first, or physical
upper-first resource.  Thus a cross-route equality must compare equal
indices.

In the cap-free range, equality between routes \(a\ne b\) requires equality
of the following two active prefix sets:

\[
\begin{array}{c|c}
\text{resource}&\text{prefix indices}\\ \hline
T_i&i-q,\ i\\
T_i\cap T_{i+1}&i-q+1,\ i\\
T_i\cup T_{i+1}&i-q,\ i+1.
\end{array}
\tag{4.11}
\]

By (4.7), both indices would have to lie in \(E\).  Their differences are
\(q,q-1,q+1\), all forbidden by (4.6).

At the initial boundary, every nonempty surviving cap suffix is a cyclic
interval with route-dependent start.  At the terminal boundary, every
nonempty entered cap prefix has the same property.  These intervals are
distinct for \(0\le a<R\le q+2\), and the \(X,Y\)-cardinality pair excludes
an early resource from equalling a late one.  This proves properties
1--3.

#### Proof of the common depth-\(q\) core

For \(0\le i\le n\), the lower depth-\(q\) flag of route \(a\) is

\[
F_{i,q}^{(a)}
=
X\setminus\{x_{\pi_a(1)},\ldots,x_{\pi_a(i)}\}
\cup
\{y_{\pi_a(1)},\ldots,y_{\pi_a(i)}\}.
\tag{4.12}
\]

Its \(Y\)-cardinality is \(i\), so a cross-route equality again forces equal
indices.  Equation (4.7) shows that all \(R\) flags coincide exactly when
\(i\in E\); outside \(E\), no two routes coincide.  Hence the support size
is (4.3).

Equation (4.4) is \(a s_q\) minus that support.  If the full value is
positive, then \(h>d_q\), so (4.4) increases with \(a\); the full family is
the maximizing subfamily and (4.5) follows.  \(\square\)

### Corollary 4.2 (fully finite growing-depth obstruction)

For every \(q\ge2\), take

\[
M=q+1,
\qquad
R=q+2.
\]

Then

\[
m=q(2q+3),
\qquad
h=q^2.
\]

Using Lemma 1.3,

\[
\begin{aligned}
(R-1)h-Rd_q
&\ge
(q+1)q^2-(q+2)q(q-1)\\
&=2q.
\end{aligned}
\]

Therefore

\[
\boxed{\delta_q^-\ge2q>0.}
\tag{4.13}
\]

This is a literal Hall violation at

\[
q=(1/\sqrt2+o(1))\sqrt m
\]

inside an otherwise admissible Johnson path family.

---

## 5. Sharp Gaussian and fixed-depth constants

Suppose \(q\to\infty\) and

\[
\frac q{\sqrt m}\longrightarrow A>0.
\tag{5.1}
\]

The exact product gives

\[
\frac{N_q}{W}\longrightarrow e^{-A^2},
\tag{5.2}
\]

and therefore

\[
\frac{d_q}{m}\longrightarrow1-e^{-A^2}.
\tag{5.3}
\]

For the construction in Theorem 4.1, choose \(M\to\infty\) so that (5.1)
holds.  Then

\[
\frac hm\longrightarrow\frac12.
\tag{5.4}
\]

For fixed \(R\),

\[
\frac{\delta_q^-}{Rm}
\longrightarrow
\left(
\frac{R-1}{2R}-(1-e^{-A^2})
\right)_+.
\tag{5.5}
\]

Thus the \(R\)-route common-core obstruction is positive precisely when

\[
\boxed{
A<\sqrt{\log\frac{2R}{R+1}}.
}
\tag{5.6}
\]

### 5.1 The sharp pair boundary

For \(R=2\), (5.6) becomes

\[
\boxed{
A_2=\sqrt{\log(4/3)}.
}
\tag{5.7}
\]

Lemma 3.2 proves that the common support of any admissible pair has
asymptotic density at most \(1/2\), and Theorem 4.1 attains it.  Therefore

\[
\boxed{
\frac1m
\max_{\text{admissible pairs}}
\delta_q^-
\longrightarrow
\left(
2e^{-A^2}-\frac32
\right)_+.
}
\tag{5.8}
\]

This is an exact asymptotic pairwise phase transition.

At depth two, \(d_2=2\) for \(m\ge5\), and (3.11) is attainable by blocks of length four,
with any final remainder merged into one block of length \(4,5,6\), or
\(7\).  Hence

\[
\boxed{
\max_{\text{admissible pairs}}\delta_2^-
=
\left(
\left\lceil\frac{m-1}{4}\right\rceil-4
\right)_+.
}
\tag{5.9}
\]

The right side is positive exactly from \(m=18\).

### 5.2 The sharp common-core boundary

Take \(R=q+2\to\infty\).  Equations (5.3)--(5.4) give

\[
\boxed{
\frac{\delta_q^-}{Rm}
\longrightarrow
\left(e^{-A^2}-\frac12\right)_+.
}
\tag{5.10}
\]

Thus

\[
\boxed{
A_{\rm core}=\sqrt{\log2}.
}
\tag{5.11}
\]

The density bound in Lemma 3.2 shows that no mechanism in which all routes
share one common flag core and are otherwise disjoint can have asymptotic
core density above \(1/2\).  Hence (5.11) is sharp for that architecture.
It is not asserted to be a global threshold for arbitrary distributed
collision hypergraphs.

The interval

\[
\sqrt{\log(4/3)}<A<\sqrt{\log2}
\tag{5.12}
\]

separates pairwise from all-subfamily control.  Every two-route subfamily of
the braid has negative Hall excess with a linear margin, while the full
\(R=q+2\) family has positive deficiency of order \(Rm\).  Actual Johnson
geometry therefore admits genuinely multiway Hall obstructions invisible to
every pair test.

Complementing all states gives identical upper-sign constructions and
constants.

---

## 6. Projected girth does not repair Hall

The depth-two obstruction can have arbitrarily large projected girth.

### Proposition 6.1 (cactus obstruction)

Let

\[
m=bk+2,
\qquad
b\ge4.
\]

Use two cap-swapped routes.  Partition their \(m-2=bk\) active coordinates
into \(k\) blocks of length \(b\).  In every block use the two orders

\[
(1,2,\ldots,b)
\qquad\text{and}\qquad
(3,4,\ldots,b,1,2).
\tag{6.1}
\]

The paths are middle-disjoint and separately lower- and upper-first
rainbow.  Their lower depth-two rows share exactly the \(k+1\) block-boundary
flags.  The union of the two projected rows is a cactus chain of \(k\)
cycles, each of length \(2b\).  If \(g\) is its component count and
\(\beta\) its cyclomatic number, then

\[
g=1,
\qquad
\beta=k,
\qquad
\boxed{\delta_2^-=(k-3)_+.}
\tag{6.2}
\]

#### Proof

Inside one block, the two proper prefix sets are distinct and agree again at
the block endpoint.  Since consecutive common endpoints are \(b\ge4\)
positions apart, the three forbidden depth-two gaps \(1,2,3\) do not occur;
the cap argument from Theorem 4.1 proves all three physical resource rows
disjoint.  Between two consecutive common flags, the projected routes are
internally disjoint paths of length \(b\), so their union is a \(2b\)-cycle.
Successive cycles share only their boundary flag, proving the cactus claim.
Finally, the two-path formula gives raw excess \(k-3\), and hence

\[
\delta_2^-=\left((k+1)-2d_2\right)_+=(k-3)_+.
\]

\(\square\)

Taking \(b\to\infty\) and \(k\ge4\) fixed gives linear projected girth,
maximum projected degree four, and positive Hall deficiency.  Taking both
\(b,k\to\infty\) makes both girth and deficiency grow.  High girth controls
short cycles in the projected graph; it does not control the total
cyclomatic budget of the path-collision quotient.

---

## 7. Amplification, switching, and pair dispersion

The local obstruction becomes global if it occurs on many disjoint path
cores.

### Proposition 7.1 (exact amplification)

Let \(\mathcal C_1,\ldots,\mathcal C_r\) be pairwise path-disjoint subfamilies
at one rank and sign.  Then

\[
\boxed{
\phi\left(\bigcup_{j=1}^r\mathcal C_j\right)
\ge
\sum_{j=1}^r\phi(\mathcal C_j).
}
\tag{7.1}
\]

Consequently, a path family containing \(\Theta(B/R)\) disjoint copies of an
\(R\)-route Gaussian braid with deficiency \(\Theta(Rm)\) has

\[
\delta_q^\sigma=\Omega(Bm)=\Omega(W).
\tag{7.2}
\]

#### Proof

Apply supermodularity (2.6) repeatedly.  Since the path sets are disjoint,
their intersections are empty and \(\phi(\varnothing)=0\).  Flag overlap
between different cores only increases collision excess, so no
flag-disjointness assumption is required.  \(\square\)

No packing of \(\Theta(B/R)\) cap braids into an exact or near-exact factor
is proved here.  Equation (7.2) is a precise conditional amplification
criterion, not a global counterexample.

For two paths define the positive pair weight

\[
w_q^\sigma(P,Q)
=
\left(
|\mathcal I_q^\sigma(P)\cap\mathcal I_q^\sigma(Q)|
-2d_q
\right)_+.
\tag{7.3}
\]

For any matching \(\mathcal M\) of disjoint path pairs,

\[
\boxed{
\delta_q^\sigma(\mathcal P)
\ge
\sum_{PQ\in\mathcal M}w_q^\sigma(P,Q).
}
\tag{7.4}
\]

Indeed, collision excess is superadditive over disjoint path subfamilies,
and each positive pair contributes its intersection minus the two discard
budgets.

Thus, if \(\delta_q^\sigma=o(W)\), then for every fixed \(\lambda>0\), the
graph joining pairs with

\[
|\mathcal I_q^\sigma(P)\cap\mathcal I_q^\sigma(Q)|
>2d_q+\lambda m
\tag{7.5}
\]

has matching number \(o(B)\).  The endpoints of a maximal matching form a
vertex cover, so deleting \(o(B)\) paths removes all such linearly bad pairs.
This is a necessary pair-dispersion law, although the interval (5.12) shows
that it is not sufficient.

The replacement bound (2.10) quantifies local repair.  For fixed
\(A<\sqrt{\log2}\), the \(R=q+2\) braid has

\[
\delta_q^-
=
\left(e^{-A^2}-\frac12+o(1)\right)Rm,
\qquad
s_q=(e^{-A^2}+o(1))m.
\]

Any repair by path replacements therefore needs at least

\[
\boxed{
\left(
1-\frac{e^{A^2}}2-o(1)
\right)R
}
\tag{7.6}
\]

routes: a positive fraction of the entire deficient core.

---

## 8. Fixed-factor persistence and architectural ceilings

Let \(\mathcal F\) be an exact middle-layer factor into

\[
B=\frac{W}{m+1}
\]

complementary paths.  At signed depth \(q\), put

\[
D_{q,\mathrm{int}}^\sigma
=
N_q-
\left|
\bigcup_{P\in\mathcal F}\mathcal I_q^\sigma(P)
\right|.
\tag{8.1}
\]

Recall \(f_q=N_q-Bs_q\).

### Theorem 8.1 (Hall persistence under near-full subselection)

If \(\mathcal P=\mathcal F\setminus\mathcal Z\) and
\(|\mathcal Z|=z\), then

\[
\boxed{
\delta_q^\sigma(\mathcal P)
\ge
\left(
D_{q,\mathrm{int}}^\sigma-f_q-s_qz
\right)_+.
}
\tag{8.2}
\]

Consequently, for \(H=O(\sqrt m)\),

\[
\begin{aligned}
\sum_{q=2}^H
(\delta_q^-+\delta_q^+)
\ge{}&
D_H^{\mathrm{int}}
-2(H-1)B\\
&-2z\sum_{q=2}^H s_q,
\end{aligned}
\tag{8.3}
\]

where

\[
D_H^{\mathrm{int}}
=
\sum_{q=2}^H
(D_{q,\mathrm{int}}^-+D_{q,\mathrm{int}}^+).
\]

If \(z=o(B/H)\), then the two error terms in (8.3) are \(o(W)\).  Therefore

\[
\boxed{
D_H^{\mathrm{int}}=\Omega(W)
\quad\Longrightarrow\quad
\sum_{q=2}^H(\delta_q^-+\delta_q^+)=\Omega(W)
}
\tag{8.4}
\]

after every allowed near-full subselection.

#### Proof

Use the whole remaining family \(\mathcal P\) as a test set in (1.1).  Its
support is contained in the full-factor support, so

\[
\begin{aligned}
\delta_q^\sigma(\mathcal P)
&\ge
\left(
s_q(B-z)
-
\left|
\bigcup_{P\in\mathcal P}\mathcal I_q^\sigma(P)
\right|
\right)_+\\
&\ge
\left(
s_qB-s_qz-N_q+D_{q,\mathrm{int}}^\sigma
\right)_+,
\end{aligned}
\]

which is (8.2).  Summing the untruncated lower bounds is legitimate because
each nonnegative deficiency is at least its possibly negative raw lower
bound.  By (1.9),

\[
\sum_{q=2}^H2f_q<2(H-1)B,
\]

giving (8.3).  Finally,

\[
HB=O(W/\sqrt m)=o(W)
\]

and

\[
z\sum_{q=2}^Hs_q
\le zH(m+1)=o(Bm)=o(W).
\]

\(\square\)

For the full factor itself, the all-family Hall test is exact:

\[
s_qB-
\left|
\bigcup_{P\in\mathcal F}\mathcal I_q^\sigma(P)
\right|
=
D_{q,\mathrm{int}}^\sigma-f_q.
\tag{8.5}
\]

Thus exact Hall at one fixed depth requires

\[
D_{q,\mathrm{int}}^\sigma\le f_q.
\tag{8.6}
\]

For fixed \(q\), (1.12) makes this the extremely rigid requirement

\[
D_{q,\mathrm{int}}^\sigma
=O_q(W/m^2).
\tag{8.7}
\]

At depth two the exact floor is only

\[
f_2=\frac{6W}{(m+1)(m+2)}.
\]

This is far stronger than merely asking for an \(o(W)\) deep defect.

### Corollary 8.2 (depth-one and static-tail ceiling)

At depth one,

\[
s_1=t_1=m,
\qquad
f_1=0.
\]

If one signed physical first-shadow support of \(\mathcal F\) has defect
\(D_{1,\mathrm{int}}^\sigma\), every subfamily with that row rainbow must
delete at least

\[
\boxed{
z\ge\frac{D_{1,\mathrm{int}}^\sigma}{m}.
}
\tag{8.8}
\]

In particular, a defect \(\varepsilon W\) forces

\[
z\ge(\varepsilon+o(1))B.
\tag{8.9}
\]

One global coordinate permutation preserves every support cardinality and
cannot change this conclusion.

Under the frozen premise that the canonical odd-cut/MSW factor has
macroscopic first-shadow defect, every static long-suffix Catalan-tail
rebundling from the audited tail cube still has such a defect: its entire
first-shadow action is \(o(W)\), so it can fill only \(o(W)\) old holes.
Equation (8.9) then excludes the whole static seam-sparse tail architecture
from the near-full Hall target.  A dynamically recomputed or genuinely
nonlocal rebundling is mandatory.

The scope of this corollary is exact: it uses the frozen macroscopic-defect
premise and the audited \(o(W)\) static-tail action.  It does not assert that
every exact path factor is first-shadow defective.

---

## 9. A deterministic collision-potential target

Although ordinary pair tests are insufficient for exact Hall, a small total
pair-collision potential is a useful stronger sufficient condition.

Let the path-selection law be supported on middle-disjoint complementary
path families whose two physical depth-one rows are separately disjoint, and
define their uncovered middle leave by

\[
L=W-(m+1)|\mathcal P|.
\tag{9.1}
\]

Also define

\[
\mathcal C_q^\sigma(\mathcal P)
=
\sum_S\binom{\mu(S)}2
=
\sum_{P<Q}
|\mathcal I_q^\sigma(P)\cap\mathcal I_q^\sigma(Q)|.
\tag{9.2}
\]

Since

\[
(\mu-1)_+\le\binom{\mu}{2},
\]

Theorem 1.1 gives

\[
\boxed{
\delta_q^\sigma(\mathcal P)
\le
\mathcal C_q^\sigma(\mathcal P).
}
\tag{9.3}
\]

Therefore any random admissible path-selection law satisfying

\[
\mathbb E\left[
HL+
\sum_{q=2}^H
(\mathcal C_q^-+\mathcal C_q^+)
\right]
=o(W)
\tag{9.4}
\]

has a deterministic realization with

\[
HL+
\sum_{q=2}^H
(\delta_q^-+\delta_q^+)
=o(W).
\tag{9.5}
\]

For \(H=o(m)\), the component baseline \(HB=o(W)\) is automatic; the stated
middle and depth-one admissibility then combines (9.5) with the exact
adaptive-MTF reduction to prove \(\mathrm{AD}(H)\).  Thus (9.4) is a concrete
randomized-to-deterministic sufficient target.  It does not move the
correlation problem into the final rounding: the path-selection law itself
must already suppress the cap-braid cores.

---

## 10. Final ceiling and exact remaining theorem

### What is proved

1. Hall deficiency is exactly collision excess over discard budget and
   exactly the nullity of a partition-matroid union.
2. The discard allowance obeys \(d_q\le q(q-1)\), with exact fixed-depth
   floors.
3. Reciprocal multiplicity, bounded multiplicity, and backward-collision
   bounds give explicit positive expansion criteria.
4. Deficient Hall sets uncross into canonical minimal and maximal cores.
5. Complementary geodesicity plus middle and two-sided depth-one
   rainbowness imposes the three forbidden common-flag distances used here.
6. The three-distance density bound is sharp.
7. The \(R=q+2\) cap braid gives a literal growing Gaussian Hall violation
   and the sharp common-core threshold \(\sqrt{\log2}\).
8. The sharp two-path threshold is \(\sqrt{\log(4/3)}\); pair tests fail to
   detect the multiway obstruction between these constants.
9. At depth two the exact pair deficiency is (5.9), and projected girth can
   grow while Hall still fails.
10. Disjoint deficient cores amplify, and repairing one cap braid requires a
    positive fraction of its paths.
11. Macroscopically defective fixed factors, global permutations, and static
    Catalan-tail rebundlings cannot enter the near-full Hall target.

### What is not proved

- The cap braid is not packed into a near-spanning complementary-path
  factor.
- Its polynomial deficiency is \(o(W)\), so one isolated braid does not
  contradict the aggregate target \(\sum_{q,\sigma}\delta_q^\sigma=o(W)\).
- The constant \(\sqrt{\log2}\) is sharp only for the one-common-core
  architecture, not for arbitrary distributed collision hypergraphs.
- No global path switch scheme avoiding every deficient core is constructed.
- No unconditional adaptive-MTF theorem beyond the previously audited scale
  is obtained.

The exact remaining theorem is therefore:

> **Global Hall-core dispersion theorem — unproved.**  For the desired
> growing \(H\), choose
> \[
> B-o(B/H)
> \]
> middle-disjoint complementary geodesics whose physical lower and upper
> first rows are separately disjoint, and whose direct-sum incidence-matroid
> nullity satisfies
> \[
> \sum_{q=2}^H(\delta_q^-+\delta_q^+)=o(W).
> \]

The fifth-wave obstruction proves that this theorem cannot follow from
the three-distance Johnson condition, pairwise Hall tests, growing projected
girth, or correlated flag rounding alone.  It requires a global
selection or rebundling theorem which hits every uncrossed deficient core.

---

## 11. Audit record and caveats

The collision normalization, matroid-union rank formula, quota bound,
three-distance lemma, sharp position density, cap boundaries, all three
physical resource rows, Gaussian constants, depth-two cactus, replacement
bound, amplification inequality, and fixed-factor persistence estimate were
independently rederived and cross-audited.

The following scopes are essential.

- A local Hall violation disproves an automatic all-subfamily expansion
  theorem but does not by itself produce an \(\Omega(W)\) global loss.
- The \(\sqrt{\log(4/3)}\) constant is the sharp pairwise threshold.
- The \(\sqrt{\log2}\) constant is the sharp one-common-core threshold.
  More general multi-core collision patterns remain open.
- Bounded multiplicity is only a rankwise positive criterion; the shallow
  ranks remain the dominant obstacle.
- Pair-dispersion cleanup is necessary but not sufficient.
- The cactus theorem excludes girth-only proofs, not expansion hypotheses
  which already imply the full cyclomatic inequality.
- Fixed-factor persistence does not obstruct starting from a different
  globally rebundled factor with small internal defects.
- The Catalan-tail corollary inherits both the frozen macroscopic-defect
  premise and the static-tail \(o(W)\)-action theorem.
- The random collision-potential criterion is sufficient, not necessary.

Within these scopes, every theorem, identity, constant, and finite
construction above is unconditional.  The sole remaining existence theorem
is explicitly labelled unproved.
