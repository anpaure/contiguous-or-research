# Strict balanced expansion: an exact common-basis certificate that regenerates in the chained lift

Date: 2026-07-31  
Status: complete all-parameter equivalence and common-basis theorem; exact
min-cut separation; independently replayed on the authenticated chained
forests through the produced parameter-seven child.  Preservation by one
further direct lift is open.

## 0. Result

The individual strict pulled-back dual transversal matroids need not have
the uniform rank density used in the unrestricted two-coordinate theorem.
Nevertheless there is an exact, polynomially checkable condition under
which the same constant-vector proof becomes valid again.

For one strict shore, let `G=(O,X)` be its occurrence graph, where

\[
 |O|=P,\qquad |X|=M,
\]

and let `T` be the image of the oriented child endpoints (tails above,
heads below).  Thus

\[
 |T|=N,\qquad Z:=X\setminus T,\qquad |Z|=K=M-N.
\]

Put

\[
 C=M-P,\qquad R=N-C=P-K,
\]

and give the middle vertices the fractional capacities

\[
 y(D)=
 \begin{cases}
 R/N,&D\in T,\\
 1,&D\in Z.
 \end{cases}                                           \tag{0.1}
\]

Their total is exactly

\[
 y(X)=R+K=P.                                           \tag{0.2}
\]

Call the shore **strictly balanced-expanding** (SBE) when

\[
 \boxed{\quad |\mathcal U|\le y(N_G(\mathcal U))
       \quad(\mathcal U\subseteq O).\quad}             \tag{0.3}
\]

The main theorem is:

> **Strict balanced-expansion theorem.**  Condition (0.3) is equivalent
> to the constant vector
> \[
>                  u_q=C/N\qquad(q\in E(F))            \tag{0.4}
> \]
> lying in the base polytope of the strict pulled-back dual transversal
> matroid on the child edges.  Consequently, if both strict shores are
> SBE, the two strict matroids have a common basis.  In fact there is a
> distribution on strict common bases with the exact marginals
> \[
>                  \Pr(q\in Q)=C/N.                    \tag{0.5}
> \]

Thus SBE restores, inside the strict child-edge system, the balanced
common-basis conclusion previously available only for unrestricted
two-step containment.

The condition has one exact min-cut oracle.  On the authenticated chained
forests its scaled maximum violations `(upper,lower)` are

\[
 (11,4),\quad(14,0),\quad(0,0),\quad(0,0),\quad(0,0)   \tag{0.6}
\]

at child parameters `n=3,4,5,6,7`, respectively.  In particular the property
is absent at the original seed, nearly holds at the next stage, and then
**regenerates exactly on both shores at parameters five, six, and seven**.

This is a sufficient invariant, not yet a preservation theorem.  It
narrows the common-basis part of DERF to preserving one explicit weighted
expansion condition after it has appeared.

## 1. The strict matroid and its full-ground extension

Fix one shore.  Let `mathcal T_G` be the transversal matroid on `X`
represented by matching middle vertices into the `P` outer vertices of
`G`.  It has rank `P`.  Its dual has rank `C=M-P`.

The endpoint map

\[
 \tau:E(F)\longrightarrow T\subset X                  \tag{1.1}
\]

is a bijection.  The strict direct matroid is the pullback

\[
 \mathcal A^{\rm dir}_F
   =\tau^*(\mathcal T_G^*|T).                          \tag{1.2}
\]

It has rank `C` exactly when some full dual base is contained in `T`, which
is the strict one-shore puncture condition.

Extend the vector (0.4) to all of `X` by

\[
 \widetilde u(D)=
 \begin{cases}
 C/N,&D\in T,\\
 0,&D\in Z.
 \end{cases}                                           \tag{1.3}
\]

Then

\[
                  \mathbf 1-\widetilde u=y.            \tag{1.4}
\]

The identity (1.4) is the source of the weights in (0.1): a strict dual
base omits all `K` terminal vertices and omits a fraction `C/N` of the
endpoint bank, so its complementary primal base uses every terminal and a
fraction `R/N` of every endpoint.

## 2. Four equivalent forms

### Theorem 2.1 (weighted Hall, flow, base polytope, and rank density)

For one strict shore, the following are equivalent.

1. The weighted Hall inequalities (0.3) hold.
2. There is a fractional matching on `G` that gives every outer vertex
   load one and every middle vertex `D` load exactly `y(D)`.
3. `y` belongs to the base polytope `B(mathcal T_G)`.
4. `widetilde u` belongs to `B(mathcal T_G^*)`.
5. The constant vector (0.4) belongs to
   `B(mathcal A_F^{dir})`.
6. For every child-edge set `S`,
   \[
        r_{\mathcal A_F^{\rm dir}}(S)
             \ge {C\over N}|S|.                       \tag{2.1}
   \]

In particular any one of these conditions proves that the strict direct
matroid has full rank `C`.

#### Proof

Give an outer vertex demand one and a middle vertex capacity `y(D)`.
Fractional bipartite matching has no integrality restriction on the
capacities.  Max-flow/min-cut says that all outer demands can be met if and
only if every outer family sees capacity at least its order, which is
exactly (0.3).  Since the total capacity is `P` by (0.2), every feasible
flow uses every middle capacity with equality.  This proves `(1)<=> (2)`.

The bipartite matching polytope is integral.  Projecting it to the middle
loads gives the independent-set polytope of the transversal matroid; on
the order-`P` face it gives the base polytope.  Hence `(2)<=> (3)`.

For every matroid, complementation identifies its dual base polytope:

\[
       B(\mathcal T_G^*)=\mathbf1-B(\mathcal T_G).
\]

Together with (1.4), this proves `(3)<=> (4)`.

The vector `widetilde u` has zero coordinates on `Z` and total order `C`.
Therefore it lies in the full dual base polytope exactly when its pullback
to `T` lies in the base polytope of the restriction (1.2).  This proves
`(4)<=> (5)`.

Finally a nonnegative vector of total order `C` lies in a matroid base
polytope exactly when all rank inequalities hold.  For the constant vector
these inequalities are precisely (2.1), proving `(5)<=> (6)`. `square`

### Corollary 2.2 (strict common basis with balanced marginals)

If the upper and lower strict shores of an oriented Catalan linear forest
are both SBE, their two pulled-back direct matroids have a common basis of
order `C`.  More strongly, the constant vector (0.4) is a convex
combination of incidence vectors of strict common bases, so (0.5) holds.

#### Proof

Theorem 2.1 places the same vector `u` in both base polytopes.  The
matroid-intersection polytope is integral.  Its order-`C` face is therefore
the convex hull of common bases, proving both existence and the marginal
statement. `square`

### Corollary 2.3 (additive risk averaging)

For every real edge cost `w`, some strict common basis satisfies

\[
                  w(Q)\le {C\over N}w(E(F)).           \tag{2.2}
\]

Applying the same statement to `-w` also gives (possibly for a different
common basis)

\[
             w(E(F)\setminus Q)\le {R\over N}w(E(F)). \tag{2.3}
\]

Both bounds are expectation identities under the distribution of
Corollary 2.2.  A chosen additive objective can therefore be optimized
without leaving the strict common-basis face.  The two displayed one-sided
bounds are not asserted for the same basis: together they would force
equality with the mean.

This does not by itself impose side degree, acyclicity, or residence.  It
does restore an exact balanced starting distribution for those physical
rows.

## 3. Exact min-cut separation

Scale (0.3) by `N` and define

\[
 w(D)=
 \begin{cases}
 R,&D\in T,\\
 N,&D\in Z.
 \end{cases}                                           \tag{3.1}
\]

Construct a network with:

* an arc of capacity `N` from the source to each outer vertex;
* an infinite-capacity arc from an outer vertex to each of its middle
  neighbours; and
* an arc of capacity `w(D)` from each middle vertex to the sink.

### Proposition 3.1 (closure/min-cut formula)

The scaled maximum SBE violation is

\[
 \Delta(G,T)
   =\max_{\mathcal U\subseteq O}
      \left[N|\mathcal U|-\sum_{D\in N_G(\mathcal U)}w(D)\right]
   =NP-\operatorname{mincut}.                          \tag{3.2}
\]

Hence the shore is SBE exactly when `Delta(G,T)=0`.

#### Proof

This is the standard maximum-weight closure reduction.  Putting an outer
vertex on the source side earns `N`; the infinite arcs force all its
neighbours to the source side, where their sink arcs pay exactly their
weights.  The empty closure has value zero, so `Delta>=0`, and (3.2)
follows by subtracting the cut from the total outer profit `NP`. `square`

Thus the strengthened invariant has a single polynomial separation oracle;
it does not require enumerating matroid subsets or common bases.

## 4. Exact finite regeneration

The independent audit

```text
scratch/audit_catalan_strict_balanced_expansion_n3_n7_20260731.py
scratch/catalan_strict_balanced_expansion_n3_n7_20260731.audit.json
```

loads the authenticated chained witness from

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n6_20260731.witness.json
```

and reconstructs, without trusting its palette claims:

* every child atom and both exact child palettes;
* both strict occurrence graphs;
* the oriented endpoint images and terminal banks; and
* the exact integer min-cut (3.2).

The result is

\[
\begin{array}{c|rr|c}
n&N\Delta^-&N\Delta^+&\text{SBE shores}\\ \hline
3&11&4&\text{neither}\\
4&14&0&\text{lower only}\\
5&0&0&\text{both}\\
6&0&0&\text{both}\\
7&0&0&\text{both}.
\end{array}                                            \tag{4.1}
\]

Here `n=7` is not a separate searched fixture: it is the literal ambient
forest produced by the authenticated `n=6` strict lift.  Thus balanced
strict expansion is observed on three consecutive recursively related
structural parents.

The script and JSON hashes at freeze time are

```text
01b2675f00e386993fd96b1652bdcbc0e5c15fb5d1ec8052fa6bb1d292b21e1e
5b11055a39e6dc33e1a53fbb553bb7f8e32c1795b2c29a51a5a0076eddaf7cd2
```

respectively.  The JSON canonical payload hash is

```text
9acf4f4b11ed5f87d0ca3ffb653cc8d2294e225b705df94e6250b8a4291b7ba0
```

## 5. Correct induction target after the independent filler theorem

The independent-`c`-rail theorem shows that the structural parent used for
`Q` and the strict side systems need not also supply the copied Catalan
rail.  Consequently SBE belongs only to the **structural-parent state**;
residence safety on the untouched rail may be supplied by a different
guarded filler.

The sharpened recursive target is therefore:

> **Balanced DERF preservation.**  Starting from an SBE structural parent
> `F_n`, choose a balanced strict common basis and physical side
> representatives, together with an independently guarded filler `G_n`,
> so that the resulting parameter-`n+1` structural output is again SBE and
> the full output obeys the physical/guard rows.

Corollary 2.2 removes the common-basis existence part of this target.  The
remaining selection is on the integral common-basis face with exact uniform
marginals, plus the physical and guard constraints.  The finite regeneration
in (4.1) makes this a materially smaller induction hypothesis than
arbitrary DERF, but no all-parameter preservation proof is claimed.

## 6. Scope and obstruction

SBE is sufficient, not necessary.  The authenticated `n=3` and `n=4`
steps have strict common bases and valid physical extensions even though
one or both SBE inequalities fail.  Conversely, the exact degree laws
alone do not imply SBE: the positive violations in (4.1) are literal
counterexamples.

The theorem therefore identifies the narrow missing invariant between the
false uniform-density claim and the full two-matroid search:

\[
 \boxed{\text{weighted expansion of the endpoint/terminal bank, separable
 by one min-cut}.}
\]

Proving its preservation from parameter five onward—or finding a
recursively produced counterexample—is the next exact common-basis test.
