# Moving-atlas Hall dual compression: the exact symmetry lemma and a paired-\(Q_8\) counterexample

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, web input, or
independent packet sampling is used.

## 0. Verdict

There is one valid positive compression principle for the exact moving-atlas
outer Hall dual:

> Average target weights over a group which genuinely permutes the entire
> legal component-option catalogue.

Such averaging preserves total target weight and cannot increase the
component support function. Hence it cannot decrease the dual deficit.

This reduces arbitrary weights to actual symmetry-orbit weights. It does
not, in general, reduce them to coarse occupancy thresholds.

The stronger reduction fails already in one concrete paired \(Q_8\)
associator component at depth two. All lower depth-two targets in the cell
have the same total local occupancy, but there are two physical face types:

1. the two active directions form one completed physical pair; or
2. they lie in two different physical pairs.

Every paired-order factor has exactly \(128\) literal starts of each type.
There are \(256\) faces of the first type and \(1536\) of the second. Give
weight one to all second-type faces and zero to all first-type faces. Every
legal pair-preserving option has weight \(128\). Compressing this weight to
depend only on total occupancy makes it the constant \(6/7\), under which
every option has weight

\[
                         \frac67\,256=\frac{1536}{7}>128.       \tag{0.1}
\]

Thus occupancy compression lowers the Hall dual objective by exactly

\[
                         \frac{1536}{7}-128=rac{640}{7}.      \tag{0.2}
\]

Equivalently, the occupancy-average of a legal option incidence vector is
not in the convex hull of legal paired-option incidence vectors. No shifting
or rearrangement theorem which forgets the completed-pair type can be valid
for these components.

The maximal justified reduction retains the full orbit data of the physical
pair-preserving group. At depth two this data includes the completed-pair
type \(c\). If the catalogue is enlarged to all coordinate conjugates and
all physical pairings, full group averaging may remove this particular
counterexample; that is the already proved symmetric fractional cover, not
an integral componentwise compression theorem.

## 1. Exact support-function form of the moving-atlas dual

At one sign and depth, write the exact component quotient as

\[
 \mathfrak D(y)=sum_Ty_T-sum_\kappa h_\kappa(y),
 \qquad
 h_\kappa(y)=max_{o\in\Theta_\kappa}
                 \langle a_{\kappa,o},y\rangle,                \tag{1.1}
\]

where \(a_{\kappa,o}\in\{0,1\}^{\mathcal T_q}\) is the literal target
incidence vector of option \(o\). Put

\[
 K_\kappa=\operatorname{conv}
  \{a_{\kappa,o}:o\in\Theta_\kappa\}.                         \tag{1.2}
\]

Then \(h_\kappa\) is the support function of \(K_\kappa\). Since support
functions add under Minkowski sum, define

\[
 K=\sum_\kappa K_\kappa,
 \qquad
 H(y)=\sum_\kappa h_\kappa(y)=h_K(y).                         \tag{1.3}
\]

Thus

\[
                         \mathfrak D(y)=\mathbf1^Ty-h_K(y).    \tag{1.4}
\]

This formulation keeps the per-component maximum exactly. It does not
replace it by a depthwise or ownerwise average.

## 2. Exact criterion for a valid linear compression

Let \(P\) be a nonnegative linear map on target weights satisfying

\[
                         P\mathbf1=\mathbf1,
 \qquad                    \mathbf1^TP=\mathbf1^T.              \tag{2.1}
\]

Thus \(P\) is mass preserving; an averaging or conditional-expectation
projection is the main example.

### Theorem 2.1 (compression criterion)

If \(P\) is self-adjoint, then

\[
 \mathfrak D(Py)\ge\mathfrak D(y)quad\text{for every }y        \tag{2.2}
\]

if and only if

\[
                         PK\subseteq K.                         \tag{2.3}
\]

For a general mass-preserving \(P\), the criterion is

\[
                         P^TK\subseteq K.                       \tag{2.4}
\]

#### Proof

Mass preservation gives \(\mathbf1^TPy=\mathbf1^Ty\). Also

\[
 h_K(Py)=\max_{v\in K}\langle v,Py\rangle
        =h_{P^TK}(y).                                            \tag{2.5}
\]

Hence (2.2) for every \(y\) is equivalent to
\(h_{P^TK}(y)\le h_K(y)\) for every \(y\). By the separating-hyperplane
characterization of closed convex sets, this is equivalent to
\(P^TK\subseteq K\). The self-adjoint case gives (2.3). \(\square\)

This criterion is useful because it tests the component options themselves,
not only target cardinalities or marginal occupancies.

## 3. The valid symmetry compression

Let a finite group \(G\) permute the target layer and suppose it permutes the
whole legal component-option system: it may permute the indices \(\kappa\),
but it carries every option incidence vector to another legal option vector
in the correspondingly permuted component. Then \(K\) is \(G\)-invariant.

Put

\[
                         P_Gy=\frac1{|G|}\sum_{g\in G}gy.       \tag{3.1}
\]

### Corollary 3.1 (Reynolds compression)

For every \(0\le y\le1\),

\[
                         \boxed{\mathfrak D(P_Gy)\ge
                                \mathfrak D(y).}                \tag{3.2}
\]

#### Proof

The convex set \(K\) is invariant under every \(g\), so the average of
\(gv\), \(g\in G\), belongs to \(K\) for every \(v\in K\). Thus
\(P_GK\subseteq K\), and Theorem 2.1 applies. Equivalently, convexity and
invariance of \(h_K\) give

\[
 h_K(P_Gy)le\frac1{|G|}\sum_gh_K(gy)=h_K(y).         \tag{3.3}
\]

\(\square\)

For the complete \(S_{2m}\)-conjugacy catalogue, (3.2) reduces weights at a
fixed rank to constants. This recovers the symmetric fractional cover and
explains why the full moving-frame catalogue has no fractional Hall cut.

For a concrete paired \(Q_8\) component, however, the physical option group
is only

\[
 \Gamma_{\rm pair}
 =\mathbb F_2^8\rtimes(S_2\wr S_4).                           \tag{3.4}
\]

Its target orbits remember how many logical physical pairs are completed.
Reynolds compression therefore retains that statistic; it does not reduce
to total occupancy alone.

## 4. Concrete paired-\(Q_8\) counterexample

Work in one \(Q_8\) owner cell with four fixed logical direction pairs

\[
                         \Pi=\{\{a_i,b_i\}:1\le i\le4\}.        \tag{4.1}
\]

At depth two, a coordinate face has one of two types:

\[
\begin{array}{c|c|c}
 c&\text{active directions}&\text{number of faces}\\ \hline
 1&\text{both directions of one pair}&
  2^{8-2}\binom41=256,\\
 0&\text{one direction in each of two pairs}&
  2^{8-2}\binom42 2^2=1536.
\end{array}                                                     \tag{4.2}
\]

Both types are literal lower targets of the same total local rank: every
depth-two trace deletes two middle coordinates. Thus a weight depending only
on total local occupancy cannot distinguish them.

Every paired direction word consists of adjacent blocks

\[
 (b_{\pi_1},a_{\pi_1}),\ldots,(b_{\pi_4},a_{\pi_4})
\]

repeated once. Among its \(4^8=256\) directed phase starts, exactly half
begin at a pair boundary and span one completed pair, while the other half
straddle two adjacent pair blocks. Under the granted trace-code gate these
are distinct literal targets. Therefore every legal pair-preserving option
incidence vector \(a_o\) satisfies

\[
 \sum_{T:c(T)=1}a_o(T)=128,
 \qquad
 \sum_{T:c(T)=0}a_o(T)=128.                         \tag{4.3}
\]

The same equations hold throughout the convex hull \(K_{Q_8}\).

Let \(P_{\rm occ}\) average a target weight over all \(1792\) depth-two
faces in the cell, which is precisely the projection to total-local-occupancy
weights. Apply it to

\[
                         y(T)=\mathbf1_{\{c(T)=0\}}.             \tag{4.4}
\]

Then

\[
 \sum_Ty(T)=1536,
 \qquad
 h_{K_{Q_8}}(y)=128,                                  \tag{4.5}
\]

whereas

\[
 P_{\rm occ}y=\frac67\mathbf1,
 \qquad
 h_{K_{Q_8}}(P_{\rm occ}y)
 =\frac67\cdot256=rac{1536}{7}.                   \tag{4.6}
\]

Consequently the local dual contribution changes by

\[
\begin{aligned}
 \bigl[\mathbf1^TP_{\rm occ}y
       -h_{K_{Q_8}}(P_{\rm occ}y)\bigr]
 -\bigl[\mathbf1^Ty-h_{K_{Q_8}}(y)\bigr]
 &=-\frac{640}{7}<0.                                 \tag{4.7}
\end{aligned}

Equivalently, for any legal option vector \(a_o\),
\(P_{\rm occ}a_o=(1/7)\mathbf1\). Its masses on the two face types are

\[
                         \frac{256}{7},qquad
                         \frac{1536}{7},                         \tag{4.8}
\]

not \((128,128)\). Hence

\[
                         P_{\rm occ}a_o\notin K_{Q_8},          \tag{4.9}
\]

which violates the exact criterion (2.3).

This is a literal occurrence-capacity counterexample. It does not use
independent packet choices, collision heuristics, or an abstract relaxation.

## 5. Consequences for the moving-atlas route

1. **No total-occupancy threshold reduction.** Arbitrary target weights
   cannot be compressed to total-occupancy thresholds inside concrete
   pair-preserving \(Q_8\) components without potentially decreasing the
   exact Hall dual.
2. **The completed-pair statistic is indispensable.** The maximal automatic
   compression is to actual \(\Gamma_{\rm pair}\)-orbits. At depth two these
   orbits include \(c=0,1\). Any proposed rearrangement must retain at least
   this datum, as well as any finer wire invariant of the chosen associator
   library.
3. **Full conjugacy is different.** If the option catalogue on a component
   is enlarged to every coordinate conjugate and every physical pairing, the
   full group average is a convex combination of legal option vectors and
   (3.2) applies. This is the known symmetric fractional cover. Exact
   componentwise selection and integral all-depth rounding remain separate.
4. **No global Hall obstruction is claimed.** The example disproves the
   proposed compression lemma; it does not produce a positive dual for the
   complete all-conjugacy moving atlas, whose fractional Hall problem is
   already solved.

Thus the positive compression route stops at true option symmetries. To go
further one needs either a component option polytope closed under the desired
occupancy averaging, or a new inequality which keeps the physical
completed-pair/wire statistics instead of discarding them.
