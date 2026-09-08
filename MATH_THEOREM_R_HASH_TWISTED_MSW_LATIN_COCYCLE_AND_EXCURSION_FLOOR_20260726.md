# Hash-twisted MSW rows: the exact Latin cocycle and the excursion-blind root-fibre floor

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Exact outcome

Let \(D=\mathcal D_m\) be the Catalan family of Dyck \(m\)-subsets of
\(J=[2m]\), and write the canonical MSW/Chung--Feller rows as

\[
 X_0(P),X_1(P),\ldots,X_m(P),\qquad P\in D.
\]

Here \(P\mapsto X_t(P)\) bijects \(D\) onto the \(t\)-th Chung--Feller
layer, \(X_m(P)=J\setminus P\), and all adjacent unions

\[
 Y_t(P)=X_t(P)\cup X_{t+1}(P),\qquad 0\le t<m,
\]

exhaust \(\binom J{m+1}\) once.

This note proves six precise statements.

1. A phasewise row interleaving is exact if and only if its hash classes
   form a Latin partition at every phase, its relative matchings are
   Johnson-legal with zero monodromy, and its complete adjacent-union map
   is a bijection. This is a necessary-and-sufficient theorem, not a
   sufficient grammar.
2. In a binary twist, lower-state ownership forces the hash to be constant
   on the orbits of every relative phase permutation. If the two complete
   options are themselves exact factors, the full lower/upper condition is
   exactly constancy on the components of their owner-overlay graph.
3. After normalizing the initial row labels, a twist is merely one global
   coordinate conjugate precisely when its phase permutations equal a
   specified coboundary \(r_t(h)\) for one
   \(h\in H_m=\langle(2\ 3),(4\ 5),\ldots,(2m-2\ 2m-1)\rangle\).
   A common hash permutation at all phases is only a row relabelling and
   changes no physical factor.
4. Nonlocal suffix hashes do produce exponentially many exact and, for
   \(m\ge5\), some genuinely non-coordinate-conjugate factors, by choosing
   reciprocal rectangles independently. Nevertheless every rowwise
   \(H_m\)-conjugate hash factor has a one-sided first-edge fibre of size at
   least

   \[
      R_{m-1},\qquad
      \sum_{n\ge0}R_nz^n={1\over1-z^2C(z)^2}
                        ={C(z)^2\over2C(z)-1},
   \]

   and

   \[
                         {R_{m-1}\over C_m}\longrightarrow {1\over9}.
   \]
5. One may force the complete two-row rectangle layer to the conjugate
   shore and still choose the remaining bounded component bits so that the
   resulting exact factor is at row distance

   \[
                      (1/8-o(1))C_m
   \]

   from every covariant \(H_m\)-conjugate of the canonical factor. On the
   aligned child plateau it reduces the old target from \(C_{m-1}\) to at
   most \(C_{m-1}-C_{m-2}\), an exact asymptotic factor \(3/4\).
6. Even after granting every blind occurrence an arbitrary choice among
   \(p\) cyclic coordinate phases, one fixed-carrier local packet has at
   most \(p\) physical images. At local semilength \(r\), its raw cap-\(p\)
   excess is therefore at least

   \[
                         (R_{r-1}-p^2)_+.
   \]

   At \(r=2\log_4p+O(\log\log p)\), this is
   \((1/9-o(1))C_r\) at depth \(O(\log p)\). Thus a positive-density
   occurrence-disjoint fixed-carrier deployment of this hash class
   remains linearly obstructed after arbitrary row phases.

Thus a nonlocal hash breaks rowwise rigidity but not this root-scale
excursion-blind fibre. To make this particular fibre \(o(C_m)\), a
construction must use row orders outside the complete \(H_m\)-conjugate
row library on \((1/9-o(1))C_m\) roots, while still satisfying the full
Latin cocycle.

The root-scale fibre here is the depth-\((m-1)\) child interval, whose
targets are singletons. It is outside the Gaussian protected band
\(q=O(\sqrt m)\), and singleton margins are universal for every exact
factor. Therefore the \(1/9\) statement alone is not a coefficient-one
obstruction. Section 11 gives a fixed-carrier shallow lift, while the
companion boundary-cocycle theorem treats bounded target maps with
explicit context-overlap accounting. Neither result rules out
filling-dependent or exterior-moving collars.

## 1. The canonical phase coordinates

Put

\[
 \mathcal X=\binom Jm,\qquad \mathcal Y=\binom J{m+1},
 \qquad C_m=|D|.
\]

For \(0\le t\le m\), write

\[
 \xi_t:D\longrightarrow\mathcal D_{2m}^t,
 \qquad \xi_t(P)=X_t(P).
\]

Every \(\xi_t\) is a bijection. The aggregate map

\[
 \eta:\{0,\ldots,m-1\}\times D\longrightarrow\mathcal Y,
 \qquad \eta(t,P)=Y_t(P)
\]

is also a bijection. Notice that the second assertion is an aggregate
upper-shore assertion: a noncanonical factor need not retain the old
upper palette separately at every cut.

Let \(p_0,\ldots,p_m:D\to D\) be arbitrary maps and define

\[
                         Z_t(P)=X_t(p_t(P)).             \tag{1.1}
\]

The word *phase* below always means the Chung--Feller flaw layer.

### Theorem 1.1 (complete phase-interleaving criterion)

The rows \(Z_0(P),\ldots,Z_m(P)\), \(P\in D\), form a phase-respecting
exact rooted MSW-type factor if and only if all four conditions hold:

\[
                         p_t\in\operatorname{Sym}(D)
                         \quad(0\le t\le m),             \tag{1.2}
\]

\[
                         p_m=p_0,                         \tag{1.3}
\]

\[
 |Z_t(P)\mathbin\triangle Z_{t+1}(P)|=2
             \quad(P\in D,\ 0\le t<m),                  \tag{1.4}
\]

and

\[
 (t,P)\longmapsto Z_t(P)\cup Z_{t+1}(P)                 \tag{1.5}
\]

is a bijection from \(\{0,\ldots,m-1\}\times D\) onto
\(\mathcal Y\).

#### Proof

At phase \(t\), the canonical map \(\xi_t\) is a bijection. Hence the
states in (1.1) exhaust the \(t\)-th layer once exactly when \(p_t\) is a
permutation. This proves that (1.2) is exactly the lower-state ownership
condition.

Condition (1.4) is exactly Johnson adjacency. The intermediate upper
token on that edge is its union, so (1.5) is exactly upper-token
ownership. Its domain and codomain have the same size

\[
 mC_m=\binom{2m}{m+1},
\]

so either injectivity or surjectivity would suffice, but the bijection
form records the ownership statement without an implicit count.

Finally,

\[
 Z_m(P)=J\setminus p_m(P),\qquad Z_0(P)=p_0(P).
\]

Thus the two endpoints of row \(P\) are complementary exactly when
\(p_m(P)=p_0(P)\). These four statements are precisely the two shore
partitions, edge legality, and odd-cycle closure. There is no further
completion condition. \(\square\)

Equivalently, if \(\pi_P\) denotes the closed odd-graph row obtained from
the rooted path and \(I_{\pi_P}(j,m)\) is its \(j\)-th middle vertex, exact
middle ownership is the single literal bijection

\[
 \Phi_m:D\times\mathbb Z_{2m+1}\longrightarrow
               \binom{[2m+1]}m,\qquad
 \Phi_m(P,j)=I_{\pi_P}(j,m).                           \tag{1.6}
\]

Theorem 1.1 is the cut-open form of this condition: its lower map records
the \(X\)-shore and its aggregate union map records the complementary
\(Y\)-shore. Consequently every factor constructed below is integral and
literal. Each selected row is a genuine complementary Johnson geodesic;
complementing the \(Y\)-states and adjoining the interface coordinate
closes it to an odd-graph cycle, whose coordinate transition order is a
literal contiguous-OR word. No signed or fractional row is used.

## 2. The exact hash-Latin equations

Let \(\mathcal A\) be a finite set of hash values, let

\[
                         \chi:D\longrightarrow\mathcal A,
 \qquad D_a=\chi^{-1}(a),                               \tag{2.1}
\]

and, for every phase and hash value, choose a row permutation

\[
                         g_{t,a}\in\operatorname{Sym}(D).          \tag{2.2}
\]

The natural hash interleaving is

\[
                         p_t(P)=g_{t,\chi(P)}P.           \tag{2.3}
\]

### Theorem 2.1 (phasewise Latin partition)

For a fixed phase \(t\), the map \(p_t\) in (2.3) is a permutation of
\(D\) if and only if

\[
                         D=\mathop{\dot\bigcup}_{a\in\mathcal A}
                              g_{t,a}D_a.                \tag{2.4}
\]

Equivalently, for every \(Q\in D\),

\[
 \boxed{
   \sum_{a\in\mathcal A}
      \mathbf1_{D_a}(g_{t,a}^{-1}Q)=1.}                 \tag{2.5}
\]

Consequently, the hash twist is an exact factor if and only if (2.4) holds
at every phase and conditions (1.3)--(1.5) hold.

#### Proof

The restriction of \(p_t\) to \(D_a\) is the injective map \(g_{t,a}\).
Its image is \(g_{t,a}D_a\). Therefore \(p_t\) is bijective exactly when
these images partition \(D\), which is (2.4), and pointwise membership in
that partition is (2.5). The last assertion is Theorem 1.1. \(\square\)

Equation (2.5) is the required bijection on Dyck rows. Merely balancing
the sizes of the hash classes is not enough.

### Corollary 2.2 (binary orbit obstruction)

Suppose \(\mathcal A=\{0,1\}\). Put

\[
                         \theta_t=g_{t,0}^{-1}g_{t,1}.              \tag{2.6}
\]

Then lower-state ownership at phase \(t\) is equivalent to

\[
                         \theta_t(D_1)=D_1.              \tag{2.7}
\]

Thus a single binary hash used at every phase must be constant on every
orbit of

\[
                         K=\langle\theta_0,\ldots,\theta_m\rangle. \tag{2.8}
\]

In particular, if \(K\) is transitive, only the two constant hashes are
possible before the upper-token equations are even considered.

#### Proof

Apply \(g_{t,0}^{-1}\) to the image partition (2.4). It becomes

\[
                         D=D_0\ \dot\cup\ \theta_tD_1.
\]

Since \(D=D_0\dot\cup D_1\) and \(|\theta_tD_1|=|D_1|\), this is equivalent
to (2.7). Invariance under all generators is invariance under \(K\).
\(\square\)

This orbit criterion concerns only the lower shore. For arbitrary phase
options which are not complete exact factors individually, the upper
condition must still be checked in the literal form (1.5); it need not be
another orbit condition.

## 3. Relative matchings and the hash cocycle

Assume the Latin equations hold, so every \(p_t\) is invertible, and put

\[
                         \sigma_t=p_{t+1}p_t^{-1}
                         \quad(0\le t<m).               \tag{3.1}
\]

After replacing the row variable \(P\) at phase \(t\) by \(Q=p_t(P)\),
edge legality becomes

\[
                         X_t(Q)\sim_JX_{t+1}(\sigma_tQ),            \tag{3.2}
\]

and upper ownership becomes bijectivity of

\[
 (t,Q)\longmapsto X_t(Q)\cup X_{t+1}(\sigma_tQ).        \tag{3.3}
\]

The endpoint condition is exactly

\[
 \boxed{\sigma_{m-1}\sigma_{m-2}\cdots\sigma_0=1.}      \tag{3.4}
\]

Indeed \(p_m=(\sigma_{m-1}\cdots\sigma_0)p_0\).

The hash transported to phase \(t\) is

\[
                         \chi_t(Q)=\chi(p_t^{-1}Q).       \tag{3.5}
\]

It obeys the exact edge cocycle

\[
 \boxed{\chi_{t+1}(\sigma_tQ)=\chi_t(Q).}               \tag{3.6}
\]

#### Proof

Substitute (3.1) into the definitions. For (3.6),

\[
 p_{t+1}^{-1}\sigma_tQ
   =p_{t+1}^{-1}p_{t+1}p_t^{-1}Q=p_t^{-1}Q.
\]

Thus the hash is not independently selectable at successive phases: it is
parallel-transported along the row matching. Equation (3.4) is precisely
zero holonomy around the complementary row. \(\square\)

If \(p_t=p\) is independent of \(t\), then \(\sigma_t=1\) for every \(t\).
As \(P\) ranges through \(D\), the rows are just the canonical rows indexed
by \(p(P)\). Hence a common nonlocal hash permutation at all phases is
physically vacuous: it is a row relabelling, not a new factor.

## 4. Whole-factor hashes and the full owner-overlay graph

There is a sharper form when every hash value chooses one complete rooted
exact factor rather than unrelated phase options.

Let \(\{F^a:a\in\mathcal A\}\) be exact rooted factors with the same port
set \(D\). For a physical lower or upper token

\[
                         T\in\mathcal X\sqcup\mathcal Y,
\]

let \(\lambda_a(T)\in D\) be its unique owner root in \(F^a\). Form a
candidate by using the complete row of \(F^{\chi(P)}\) at root \(P\).

### Theorem 4.1 (owner-transversal Latin system)

The hash-selected candidate is exact if and only if

\[
 \boxed{
   \sum_{a\in\mathcal A}
      \mathbf1_{\{\chi(\lambda_a(T))=a\}}=1
   \qquad(T\in\mathcal X\sqcup\mathcal Y).}             \tag{4.1}
\]

#### Proof

For a fixed option \(a\), token \(T\) lies in exactly one row, rooted at
\(\lambda_a(T)\). The candidate retains that occurrence exactly when that
root chooses \(a\). Therefore the left side of (4.1) is the literal
multiplicity of \(T\) in the candidate. Requiring it to be one for every
token is exactly the lower- and upper-shore ownership condition. Each
selected row is already a legal complementary path, so nothing further is
required. \(\square\)

For two factors \(F^0,F^1\), put \(A=\chi^{-1}(1)\) and form the multigraph
\(\Gamma(F^0,F^1)\) on \(D\) with one edge

\[
                         \lambda_0(T)--\lambda_1(T)      \tag{4.2}
\]

for every lower or upper token \(T\). Loops and repeated edges are allowed.

### Corollary 4.2 (binary full cocycle)

\[
 \boxed{
   \text{The binary row hash is exact}
   \iff A\text{ is a union of connected components of }
        \Gamma(F^0,F^1).}                              \tag{4.3}
\]

#### Proof

The multiplicity of \(T\) is

\[
 \mathbf1_{\{\lambda_0(T)\notin A\}}
 +\mathbf1_{\{\lambda_1(T)\in A\}}.
\]

It equals one exactly when

\[
                         \mathbf1_A(\lambda_0(T))
                         =\mathbf1_A(\lambda_1(T)).
\]

These are precisely the edge-constancy equations for (4.2). \(\square\)

Unlike a lower-phase orbit test, (4.3) includes every upper-colour
equation. It is the complete binary ownership cocycle.

## 5. Exact coordinate-conjugacy signature

The coordinate stabilizer of the Dyck port family is

\[
 H_m=\langle(2\ 3),(4\ 5),\ldots,(2m-2\ 2m-1)\rangle. \tag{5.1}
\]

For completeness, if \(a_i\) denotes the number of Dyck roots containing
coordinate \(i\), then

\[
 a_{2j}=a_{2j+1},\qquad
 a_{2j}-a_{2j+2}=C_jC_{m-j-1}>0,
\]

with singleton end classes at \(1\) and \(2m\). Thus the coordinate
frequency classes are exactly

\[
 \{1\},\{2,3\},\{4,5\},\ldots,\{2m-2,2m-1\},\{2m\}.
\]

Every coordinate stabilizer must preserve these classes, and every swap
inside one displayed pair preserves Dyckness. Hence

\[
                         \operatorname{Aut}_{S_{2m}}(D)=H_m.       \tag{5.2}
\]

The reverse--complement symmetry of the layer-coloured Johnson graph is
contravariant on the lower/upper inclusion geometry. It does not give an
additional covariant coordinate conjugate.

For \(h\in H_m\), define the phase coboundary

\[
 r_t(h)=\xi_t^{-1}\circ h\circ\xi_t\circ h^{-1}
          \in\operatorname{Sym}(D).                    \tag{5.3}
\]

The globally coordinate-conjugated row rooted at \(P\) is

\[
                         hX_t(h^{-1}P)=X_t(r_t(h)P).     \tag{5.4}
\]

Notice \(r_0(h)=r_m(h)=1\).

### Theorem 5.1 (conjugacy classification)

Given a phase factor \(Z_t(P)=X_t(p_tP)\), normalize its row labels by

\[
                         \bar p_t=p_tp_0^{-1}.           \tag{5.5}
\]

It is one global covariant coordinate conjugate of the canonical MSW
factor if and only if there exists \(h\in H_m\) such that

\[
 \boxed{\bar p_t=r_t(h)\qquad(0\le t\le m).}            \tag{5.6}
\]

#### Proof

After relabelling rows by their physical phase-zero roots, the state at
phase \(t\) is \(X_t(\bar p_tP)\). Formula (5.4) gives (5.6) for a global
conjugate. Conversely, if (5.6) holds, every state in every rooted row is
the corresponding state in (5.4). Adjacent unions are then the same as
well, so the entire rooted factor is that conjugate. Equation (5.2) shows
there is no other covariant coordinate permutation to consider.
\(\square\)

Thus (5.6), rather than nonconstancy of the hash by itself, is the exact
test for whether a proposed twist is genuinely nonconjugate.

The scope here is the fixed \(D\)-port rooting and the covariant
lower/upper inclusion geometry. An unrooted odd-graph factor could in
principle be coordinate-conjugated and then recut at different phases on
different cycles; that operation is not a phase-respecting conjugate in
the present sense and is not classified by (5.6).

## 6. Root-dependent coordinate conjugates

Let \(F\) be the canonical rooted factor. For an arbitrary selector

\[
                         a:D\longrightarrow H_m,         \tag{6.1}
\]

use at root \(P\) the row

\[
                         F_a(P)=a(P)F(a(P)P),            \tag{6.2}
\]

where every element of \(H_m\) is an involution. Each row begins at \(P\)
and ends at \(J\setminus P\).

Let \(\rho(T)\) be the canonical owner root of a lower or upper token
\(T\). In the global \(h\)-conjugate its owner is

\[
                         \lambda_h(T)=h\rho(hT).         \tag{6.3}
\]

Theorem 4.1 becomes the exact system

\[
 \boxed{
   \sum_{h\in H_m}
      \mathbf1_{\{a(\lambda_h(T))=h\}}=1
      \qquad(T\in\mathcal X\sqcup\mathcal Y).}          \tag{6.4}
\]

This is the simultaneous lower/upper Latin section. Checking only that
the phase states are permuted is insufficient.

A selector (6.1) is physically a single global conjugate precisely when
there is \(k\in H_m\) for which its induced phase maps satisfy (5.6), or,
equivalently,

\[
 a(P)X_t(a(P)P)=kX_t(kP)
       \qquad(P\in D,\ 0\le t\le m).                   \tag{6.5}
\]

This criterion allows for the possibility that two different selector
descriptions happen to give the same physical rooted factor.

## 7. A genuine nonlocal hash bank

Let

\[
                         \sigma=(2\ 3)\in H_m.
\]

For every \(R\in D_{m-2}\), define two roots

\[
                         P_R=1100R,\qquad Q_R=1010R.     \tag{7.1}
\]

Suppressing the common shifted suffix \(R\), their first three canonical
states are

\[
\begin{array}{c|ccc}
P_R&12R&14R&34R\\
Q_R&13R&23R&24R.
\end{array}                                             \tag{7.2}
\]

Indeed the MSW flip recursion gives

\[
\begin{aligned}
 \pi(1100R)&=(4,2,3,1,4+\pi(R)),\\
 \pi(1010R)&=(2,1,4,3,4+\pi(R)),
\end{aligned}
\]

and taking the middle states after successive insertion--deletion pairs
gives (7.2).

The corresponding two \(\sigma\)-conjugate rows are

\[
\begin{array}{c|ccc}
P_R&12R&23R&34R\\
Q_R&13R&14R&24R.
\end{array}                                             \tag{7.3}
\]

Both tables use the same six lower states and the same four upper colours

\[
                         123R,124R,134R,234R             \tag{7.4}
\]

once. They rejoin after the displayed slab. Hence

\[
                         K_R=\{P_R,Q_R\}                 \tag{7.5}
\]

is a complete component of the binary owner overlay. The components
\(K_R\) are pairwise root-disjoint.

### Theorem 7.1 (suffix-hashed exact factors)

For every hash

\[
                         \psi:D_{m-2}\longrightarrow\{0,1\},      \tag{7.6}
\]

select the \(\sigma\)-row on both roots of \(K_R\) when \(\psi(R)=1\),
and the canonical row otherwise. The resulting rooted factor is exact.
The \(2^{C_{m-2}}\) choices of \(\psi\) give \(2^{C_{m-2}}\) distinct
rooted factors.

#### Proof

Each selected set is a union of the complete owner-overlay components
(7.5), so Corollary 4.2 proves exactness. If two hashes differ at \(R\),
the rooted path at \(P_R\) has middle state \(14R\) in one factor and
\(23R\) in the other. Thus the rooted factors are distinct. \(\square\)

The bit \(\psi(R)\) may depend on the entire long suffix. Thus exact middle
ownership does permit a genuinely nonlocal Dyck-word hash; locality of the
hash is not forced.

There are at most

\[
                         |H_m|=2^{m-1}                  \tag{7.7}
\]

global covariant coordinate conjugates. Since \(C_{m-2}>m-1\) for
\(m\ge5\), Theorem 7.1 yields:

### Corollary 7.2 (nonconjugate exact existence)

For every \(m\ge5\), the suffix-hash bank contains a genuinely
non-coordinate-conjugate exact factor.

This is an existence assertion inside an explicit Boolean family. A
particular hash is certified nonconjugate by the exact signature (5.6).

## 8. The unavoidable excursion-blind fibre

Write a Dyck root in paired form

\[
                         P=1b_1b_2\cdots b_{m-1}0,
                         \qquad |b_i|=2,                \tag{8.1}
\]

and encode the pairs by a two-coloured Motzkin path:

\[
 11\mapsto U,\qquad00\mapsto D,\qquad
 01\mapsto\alpha,\qquad10\mapsto\beta.                \tag{8.2}
\]

Call a horizontal step ground-level if the Motzkin height before it is
zero. Let \(\mathcal F_{m,m}\) be the Dyck roots whose first return is at
the final position. In this encoding, these are precisely the roots with
no ground \(\alpha\)-step. For \(P\in\mathcal F_{m,m}\), let

\[
 B(P)=\{i:b_i\text{ is a ground }\beta\text{-step}\}.  \tag{8.3}
\]

For \(h\in H_m\), let \(S(h)\) be the set of pair indices swapped by \(h\).
The action of \(h\) fixes the uncoloured Motzkin skeleton and exchanges
\(\alpha,\beta\) at exactly the indices in \(S(h)\).

The canonical first insertion label is

\[
                         b_1^F(Q)=2\operatorname{fr}(Q),            \tag{8.4}
\]

where \(\operatorname{fr}(Q)\) is the first-return semilength. Therefore
the first insertion in the selected row (6.2) is

\[
                         b_1^{F_a}(P)
 =a(P)\bigl(2\operatorname{fr}(a(P)P)\bigr).            \tag{8.5}
\]

To verify (8.4), write the first-return decomposition as \(Q=1u0v\).
Then \(|u|=2(\operatorname{fr}(Q)-1)\), and the MSW recursion starts its
flip word with \(|u|+2\), the closing zero of that first primitive block.
This is an insertion and equals \(2\operatorname{fr}(Q)\).

Every \(h\in H_m\) fixes coordinate \(2m\). Hence, on
\(\mathcal F_{m,m}\), (8.5) equals \(2m\) exactly when no ground
\(\beta\)-step is flipped.

Let

\[
                         \mathcal E_m
 =\{P:\text{the Motzkin encoding has no ground horizontal step}\}. \tag{8.6}
\]

Every selector row, legal or not, has first insertion \(2m\) on every root
of \(\mathcal E_m\).

### Theorem 8.1 (sharp pointwise fibre formula)

For every selector \(a:D\to H_m\),

\[
\begin{aligned}
 Q_a(m,2m)
  &:=\#\{P\in\mathcal F_{m,m}:b_1^{F_a}(P)=2m\}\\
  &=R_{m-1}
    +\#\{P\in\mathcal F_{m,m}:B(P)\ne\varnothing,
                    S(a(P))\cap B(P)=\varnothing\}.      \tag{8.7}
\end{aligned}
\]

In particular,

\[
 \boxed{Q_a(m,2m)\ge R_{m-1}}                           \tag{8.8}
\]

without any exactness hypothesis.

#### Proof

For a root in \(\mathcal F_{m,m}\), flipping pair \(i\) changes failure of
the final first-return condition exactly when it changes a ground
\(\beta\) into a ground \(\alpha\). Thus (8.5) equals \(2m\) exactly when
\(S(a(P))\cap B(P)=\varnothing\). If \(B(P)=\varnothing\), this is
automatic for every selector. Splitting according as \(B(P)\) is empty or
nonempty gives (8.7), once \(|\mathcal E_m|=R_{m-1}\) is established.
\(\square\)

It remains to count \(\mathcal E_m\). Two-coloured Motzkin excursions have
generating function \(C(z)^2\). A path with no ground horizontal step is a
sequence of elevated blocks \(UMD\), where \(M\) is an arbitrary
two-coloured Motzkin excursion. Therefore

\[
 R(z)=\sum_{n\ge0}R_nz^n
     ={1\over1-z^2C(z)^2}
     ={C(z)^2\over2C(z)-1}.                            \tag{8.9}
\]

The paired Motzkin path has length \(m-1\), so
\(|\mathcal E_m|=R_{m-1}\).

At the Catalan singularity,

\[
 C(z)=2-2\sqrt{1-4z}+O(1-4z).
\]

For \(\Phi(u)=u^2/(2u-1)\), one has \(\Phi'(2)=4/9\). Hence

\[
                         R_n\sim{4\over9}C_n.           \tag{8.10}
\]

Since

\[
                         {C_{m-1}\over C_m}
                         ={m+1\over4m-2}\longrightarrow{1\over4}, \tag{8.11}
\]

we obtain

\[
 \boxed{{R_{m-1}\over C_m}\longrightarrow{1\over9}.}   \tag{8.12}
\]

## 9. Exact scope and the constant-one boundary

Theorems 7.1 and 8.1 together give the exact answer for the root-scale
first-insertion statistic in the natural rowwise coordinate-conjugate hash
route.

* Exact middle ownership does not force the hash to be local or constant.
  There are exponentially many exact suffix-hashed patchworks, and some
  are genuinely nonconjugate.
* Nevertheless every permitted row option is blind on the same set
  \(\mathcal E_m\) for this statistic. No correlation among the hash bits
  can split the common root-scale fibre.
* Reducing the \(2m\) first-insertion fibre itself to \(o(C_m)\) therefore
  requires
  changing the first edge outside the rowwise \(H_m\)-conjugate library on
  at least

  \[
                         R_{m-1}-o(C_m)
                         =(1/9-o(1))C_m                 \tag{9.1}
  \]

  roots.

This does **not** yet rule out coefficient one. The interval defining
\(Q_a(m,2m)\) has depth \(m-1\), not \(O(\sqrt m)\), and exact singleton
margins force a common global census at that depth independently of the
hash. To turn the same mechanism into a shallow hereditary obstruction,
one must suspend a local size-\(r\) blind set inside the ambient
size-\(m\) factor with \(r=O(\sqrt m)\), keep the relevant collars common
or explicitly bounded, and control how often the resulting occurrences
overlap. None of those three quantitative steps follows from (8.8).

The general phasewise hash class of Sections 1--3 is also not ruled out.
A successful recursive twist outside the complete-row library must prove,
simultaneously:

1. the phasewise image partitions (2.4);
2. literal Johnson adjacency (3.2);
3. the complete upper-token bijection (3.3);
4. zero monodromy (3.4); and
5. first-edge escape on the positive-density blind set (8.6).

The reciprocal rectangle proves that the cocycle is not universally
rigid. The \(1/9\) floor proves only that nonlocal hashing of complete
coordinate-conjugate rows cannot disperse this root-scale fibre. It is not,
without the context-and-collar lift just described, a failure theorem for
CPCR or for coefficient one.

## 10. A forced-drain hash far from every covariant conjugate

The two-row bank proves nonconjugacy by counting. A stronger construction
can be forced to move a definite part of one Catalan plateau while remaining
far from every covariant coordinate conjugate.

We use the audited complete component hierarchy for the comparison of
\(F_m\) with its \(\sigma=(2\ 3)\)-conjugate. For \(0\le j\le m-2\), put

\[
 \mathcal A_j=
 \{1u0:u\in D_{j+1}\}\ \dot\cup\
 \{10\,1v0:v\in D_j\}.                                \tag{10.1}
\]

For \(R\in D_{m-j-2}\), the full lower/upper owner-overlay component is

\[
                         \mathcal C_{j,R}=\mathcal A_jR,           \tag{10.2}
\]

and each shore has

\[
                         k_j=C_j+C_{j+1}                           \tag{10.3}
\]

rows. Suffix locality prevents an owner edge from changing \(R\), and
the MSW first-return recursion is transitive on \(\mathcal A_j\). These
facts give (10.2). On every such nontrivial component, the canonical and
\(\sigma\)-conjugate rooted rows are distinct at every root. The Catalan
convolution

\[
 \sum_{j=0}^{m-2} C_{m-j-2}(C_j+C_{j+1})=C_m            \tag{10.4}
\]

checks that the components exhaust every root. The case \(j=0\) is the
directly verified rectangle \(K_R\) of Section 7.

Inside \(F_m\), consider the aligned right-child roots

\[
                         \mathcal P_m=\{10v:v\in D_{m-1}\}.        \tag{10.5}
\]

Their distinguished child intervals all have the same canonical local
target, denoted \(S_2\); in general \(S_x\) denotes the same exterior
target with its local singleton changed to coordinate \(x\). The roots
of \(\mathcal P_m\) in component
\((j,R)\) are precisely

\[
                         10\,1v0R,\qquad v\in D_j.                 \tag{10.6}
\]

For a root \(10\,1v0R\) in this intersection, the switched row has first
insertion \(2j+4\): after applying \(\sigma\), its first primitive has
semilength \(j+2\), and \(\sigma\) fixes the even coordinate \(2j+4\).
Thus switching this component replaces its target \(S_2\) by
\(S_{2j+4}\). There are exactly \(C_j\) such roots, so the literal
distinguished component vector is

\[
                   C_j(e_{S_{2j+4}}-e_{S_2}).                     \tag{10.7}
\]

### Theorem 10.1 (nonlocal exact drain and covariant-orbit escape)

For every \(0<\varepsilon<1/8\), for all sufficiently large \(m\), there
is a Boolean component hash \(b_{j,R}\) such that:

1. \(b_{0,R}=1\) for every \(R\in D_{m-2}\);
2. \(b_{j,R}=0\) for every \(j>J(\varepsilon)\), where
   \(J(\varepsilon)\) is independent of \(m\);
3. the corresponding component hybrid \(G_m\) is an integral exact
   anchored factor;
4. for every \(h\in H_m\), where \(d_{\rm row}\) counts roots at which
   the complete rooted paths differ,

   \[
       d_{\rm row}\bigl(G_m,hF_m(h\,\cdot)\bigr)>
                         (1/8-\varepsilon)C_m;          \tag{10.8}
   \]

5. the contribution of the aligned fibre \(\mathcal P_m\) to the old
   target satisfies

   \[
      \mu^{\mathcal P_m}_{G_m}(S_2)\le C_{m-1}-C_{m-2}
       =C_{m-1}{3(m-2)\over2(2m-3)}.                   \tag{10.9}
   \]

In particular, \(G_m\) is not a covariant coordinate conjugate of the
canonical factor, and the old child fibre is reduced by an asymptotic
factor at most \(3/4\).

#### Proof

Every whole component shore is a zero-defect owner trade, so any choice
of the bits gives an exact integral factor. Force every \(j=0\) bit to
one. By (10.6)--(10.7), this removes one \(S_2\)-occurrence for every
\(R\in D_{m-2}\); all other switched components can only remove more.
Thus

\[
              \mu^{\mathcal P_m}_{G_m}(S_2)\le C_{m-1}-C_{m-2}.
\]

The exact Catalan ratio

\[
                         {C_{m-2}\over C_{m-1}}
                         ={m\over4m-6}                 \tag{10.10}
\]

gives (10.9).

For a fixed \(J\), let

\[
 S_{m,J}^*=
   \sum_{j=1}^{J}C_{m-j-2}k_j.                         \tag{10.11}
\]

Since \(C_{m-j-2}/C_m\to4^{-j-2}\) for fixed \(j\),

\[
 \lim_{J\to\infty}\lim_{m\to\infty}{S_{m,J}^*\over C_m}
   =\sum_{j\ge1}{C_j+C_{j+1}\over4^{j+2}}
   ={1\over4}.                                         \tag{10.12}
\]

Indeed the same sum beginning at \(j=0\) is \(3/8\), while its \(j=0\)
term is \(2/16=1/8\). Choose \(J=J(\varepsilon)\) so that, for all large
\(m\),

\[
                         S_{m,J}^*>(1/4-\varepsilon/2)C_m.        \tag{10.13}
\]

Choose the bits on components \(1\le j\le J\) independently and fairly.
Fix \(h\in H_m\) and compare rooted rows with the covariant conjugate
\(H=hF_m(h\,\cdot)\). On one component of \(k_i\) roots, let \(D_i^0\)
and \(D_i^1\) be the row distances from \(H\) of its canonical and
\(\sigma\)-conjugate shores. At each root the two candidate rows are
distinct, so the fixed comparison row can agree with at most one of them.
Therefore

\[
                         D_i^0+D_i^1\ge k_i.            \tag{10.14}
\]

The expected contribution is at least \(k_i/2\), and its range has length
at most \(k_i\le k_J\). Contributions from the forced \(j=0\) layer and
from \(j>J\) are nonnegative and may be ignored. Consequently

\[
 \mathbb E\,d_{\rm row}(G_m,H)
       \ge{1\over2}S_{m,J}^*>
                         (1/8-\varepsilon/4)C_m.        \tag{10.15}
\]

Moreover

\[
 \sum_i k_i^2\le k_J\sum_i k_i
                 =k_JS_{m,J}^*\le k_JC_m.              \tag{10.16}
\]

Hoeffding's inequality gives

\[
 \Pr\{d_{\rm row}(G_m,H)\le(1/8-\varepsilon)C_m\}
 \le \exp\{-c_\varepsilon C_m/k_J\}                    \tag{10.17}
\]

for some \(c_\varepsilon>0\). There are
\(|H_m|=2^{m-1}=\exp(o(C_m))\) covariant conjugates. The union bound is
therefore less than one for all sufficiently large \(m\). Some
deterministic component hash satisfies (10.8) for every \(h\)
simultaneously. \(\square\)

Theorem 10.1 is a genuine positive construction: the hash may depend on
the complete suffix \(R\), exactness is integral on both shores, and the
result is globally far from the complete covariant conjugate orbit. It is
only a one-sided improvement. Section 8 still forces a different
root-scale fibre of size \((1/9-o(1))C_m\).

## 11. The phase-robust fixed-carrier lift

We now add the context hypothesis missing from the root-scale statement.
Install a local \(D_r\)-port rowwise \(H_r\)-hash factor on a coordinate
block \(J\) of size \(2r\). Suppose the serviced ambient window has the
same exterior intersection \(K\) for every filling of this local packet.
In deletion--insertion notation,

\[
                         X_t=(P\setminus A_t)\cup B_t.
\]

For every interval \(i\le j\),

\[
             \bigcap_{t=i}^{j}X_t=(P\setminus A_j)\cup B_i.       \tag{11.1}
\]

Hence the child window \(X_1,\ldots,X_r\), of transition depth \(r-1\),
has local intersection

\[
                         \bigcap_{t=1}^{r}X_t=\{b_1\}.             \tag{11.2}
\]

Every root in \(\mathcal E_r\) therefore gives the same ambient target

\[
                         K\cup\{2r\}.                              \tag{11.3}
\]

### Theorem 11.1 (arbitrary \(p\)-phase cap floor)

Let \(N\) fixed-carrier packets satisfying the preceding hypothesis have
pairwise disjoint distinguished occurrence sets, and install them in an
ambient system with per-target cap \(p\). Grant every
blind occurrence an arbitrary cyclic coordinate phase from a group of
order at most \(p\), independently of all ownership and chronology
constraints. If \(\mu\) is the resulting target histogram at depth
\(r-1\), including any nonnegative background contribution from the
remaining ambient occurrences, then

\[
 \boxed{
   \sum_S(\mu(S)-p)_+\ge
                         N(R_{r-1}-p^2)_+.}             \tag{11.4}
\]

Without the extra cyclic phases, the stronger bound is

\[
                         \sum_S(\mu(S)-p)_+
                         \ge N(R_{r-1}-p)_+.            \tag{11.5}
\]

#### Proof

By Theorem 8.1 and (11.2), every packet contributes \(R_{r-1}\) blind
occurrences before phasing. Without phases they share one target in that
packet. A nonnegative integral histogram of mass \(M\) on support \(U\)
satisfies

\[
                         \sum_S(\mu(S)-p)_+
                         \ge (M-p|U|)_+.               \tag{11.6}
\]

This proves (11.5), packet by packet; the functional on the left is
superadditive under addition of histograms.

After arbitrary cyclic phasing, the blind occurrences of one packet can
occupy at most \(p\) physical images of (11.3). Applying (11.6) to that
packet gives \((R_{r-1}-p^2)_+\). Superadditivity then permits summing the
\(N\) packet bounds even when their phase orbits overlap. This argument
grants independent phases, so it applies a fortiori to every common legal
phase assignment. \(\square\)

### Corollary 11.2 (fixed-carrier obstruction inside the Gaussian range)

Let \(p=2M+1\) tend to infinity, and write

\[
 W_M=\binom{2M+1}{M},
 \qquad
 N_{M,q}=\binom{2M+1}{M-q}.
\]

Put

\[
 r(p)=\left\lceil
       2\log_4p+2\log_4\log p
      \right\rceil.                                    \tag{11.7}
\]

Then

\[
 r(p)=O(\log p)=o(\sqrt M),
 \qquad {C_{r(p)}\over p^2}\longrightarrow\infty,
 \qquad {R_{r(p)-1}\over p^2}\longrightarrow\infty.    \tag{11.8}
\]

Indeed \(4^{r(p)}\ge p^2(\log p)^2\), while
\(C_r\sim4^r/(\sqrt\pi r^{3/2})\), so
\(C_{r(p)}/p^2=\Omega(\sqrt{\log p})\). Equation (8.12) gives the last
limit.

Assume the ambient depth-\(q\) histogram has total mass \(W_M\), as it
does for an exact seed factor. If an occurrence-disjoint bank of these
packets contains total distinguished mass

\[
                         NC_{r(p)}\ge\beta W_M          \tag{11.9}
\]

for some fixed \(\beta>0\), Theorem 11.1 yields

\[
 \sum_S(\mu(S)-p)_+
       \ge(1/9-o(1))NC_{r(p)}
       \ge(\beta/9-o(1))W_M.                           \tag{11.10}
\]

At \(q=r(p)-1=o(\sqrt M)\), the unavoidable duplicate baseline is

\[
                 W_M-N_{M,q}=O(q^2W_M/M)=o(W_M).        \tag{11.11}
\]

If \(\mathsf H_q\) is the number of missing depth-\(q\) targets, then the
exact load identity gives

\[
 \mathsf H_q\ge
 \sum_S(\mu(S)-p)_+-(W_M-N_{M,q}).
\tag{11.12}
\]

Equations (11.10)--(11.12) therefore leave a linear missing-target defect
after the baseline is subtracted. Positive-density occurrence-disjoint
fixed-carrier use of the rowwise \(H_r\)-hash class cannot compose into
coefficient one, even after arbitrary cyclic row phases.

The fixed-carrier hypothesis in this section is essential. A
filling-dependent stationary collar, a parent-crossing outside collar, or
a nonidentity local endpoint pairing with matching exterior displacement
can enlarge the image of (11.3). Those mechanisms are treated by the
boundary-cocycle theorem summarized next.

## 12. Boundary cocycle and the complete escape condition

The following theorem applies beyond coordinate-conjugate MSW rows. Let
\(J\) and \(E\) be disjoint coordinate sets, \(|J|=2r\), and let
\(u\mapsto P_u\in\binom Jr\) be injective. Suppose a contiguous
length-\(r\) Johnson geodesic in row \(u\) has endpoints

\[
 Z_0(u)=O_L(u)\mathbin{\dot\cup}P_u,\qquad
 Z_r(u)=O_R(u)\mathbin{\dot\cup}(J\setminus P_{\tau u}),           \tag{12.1}
\]

where \(\tau\) permutes the row labels and
\(|O_L(u)|=|O_R(u)|\).

### Theorem 12.1 (geodesic boundary-cocycle identity)

For every \(u\),

\[
 \boxed{|O_L(u)\setminus O_R(u)|
              =|P_u\setminus P_{\tau u}|}                         \tag{12.2}
\]

and

\[
 \boxed{\bigcap_{t=0}^{r} Z_t(u)=
   \bigl(O_L(u)\cap O_R(u)\bigr)\mathbin{\dot\cup}
   \bigl(P_u\setminus P_{\tau u}\bigr).}                           \tag{12.3}
\]

#### Proof

Johnson distance between the endpoints in (12.1) is

\[
\begin{aligned}
 d_J(Z_0(u),Z_r(u))
 &=|O_L(u)\setminus O_R(u)|
   +|P_u\cap P_{\tau u}|\\
 &=|O_L(u)\setminus O_R(u)|
   +r-|P_u\setminus P_{\tau u}|.
\end{aligned}                                                       \tag{12.4}
\]

It equals the geodesic length \(r\), proving (12.2). Every coordinate
common to the endpoints of a Johnson geodesic remains present throughout:
deleting and reinserting it would spend two moves without reducing the
endpoint distance. Conversely, every coordinate in the full intersection
belongs to both endpoints. Thus the full intersection equals
\(Z_0(u)\cap Z_r(u)\), which is (12.3). \(\square\)

In particular, a common exterior \(O_L(u)=O_R(u)\) forces
\(P_{\tau u}=P_u\), hence \(\tau u=u\). A nonidentity local endpoint braid
is possible only with the exactly matching exterior displacement in
(12.2).

If \(B_{C,q}(u)\) is the intersection supplied by the remainder of a
serviced window in context \(C\), with the coordinate blocks in the
following union disjoint, its literal target is

\[
 \Phi_{C,q}(u)=B_{C,q}(u)
   \cup\bigl(O_L(u)\cap O_R(u)\bigr)
   \cup\bigl(P_u\setminus P_{\tau_Cu}\bigr).                       \tag{12.5}
\]

Thus a closed fixed-port recursive hash is blind regardless of how
nonlocally it chooses the internal chronology. It can escape only through
one of the three displayed data: a filling-dependent outside collar, a
filling-dependent stationary exterior, or nonzero local monodromy with
the displacement required by (12.2).

There is an aggregate version which explicitly accounts for context
overlap. Let \(d=C_r\), and let

\[
 n_{C,T}=|\{u\in D_r:\Phi_{C,q}(u)=T\}|.
\]

Assume the full aligned family has
\(H_{M,r}=\frac12\binom{2(M-r)}{M-r}\) contexts and each physical rooted
occurrence is boundary-served by at most two of them. This degree-two
claim is automatic only when the contiguous size-\(r\) block remains
identifiable and service is through its canonical left or right boundary.
For cap \(b\), put

\[
                         K_{q,b}=\sum_T(\mu_q(T)-b)_+.
\]

### Theorem 12.2 (compressed-target cap lower bound)

\[
 \boxed{
 K_{q,b}\ge {1\over2}\sum_C\sum_T(n_{C,T}-2b)_+.}                  \tag{12.6}
\]

If every \(\Phi_{C,q}\) has at most \(L\) images, then

\[
 \boxed{
 K_{q,b}\ge {H_{M,r}\over2}(C_r-2bL)_+,\qquad
 H_{M,r}={1\over2}\binom{2(M-r)}{M-r}.}                            \tag{12.7}
\]

#### Proof

Put \(I_T=\sum_Cn_{C,T}\). The incidence-degree hypothesis gives
\(\mu_q(T)\ge I_T/2\). Hence

\[
 K_{q,b}\ge{1\over2}\sum_T(I_T-2b)_+.
\]

For nonnegative \(x,y,a\),

\[
                         (x+y-a)_+\ge(x-a)_++(y-a)_+.
\]

Iterating over contexts proves (12.6). If one context has at most \(L\)
nonzero values \(n_{C,T}\), then

\[
 \sum_T(n_{C,T}-2b)_+\ge C_r-2bL.
\]

There are \(H_{M,r}\) aligned contexts, giving (12.7). \(\square\)

For the ambient odd factor, take \(p=2M+1\), \(b=p\), and choose \(r\)
minimally with

\[
                         C_r\ge4pL.                                \tag{12.8}
\]

Then \(C_r<16pL\), \(r=\Theta(\log(pL+2))\), and

\[
 K_{q,p}\ge{H_{M,r}C_r\over4},\qquad
 {K_{q,p}\over W}\ge
              {1-o(1)\over16\sqrt\pi\,r^{3/2}}                    \tag{12.9}
\]

uniformly for \(r=o(M)\) and \(r\le q\le M/2\) under the canonical
left/right boundary service, or at any other depth for which every
context is serviced and the stated degree-two hypothesis holds. Here
\(W=\binom{2M+1}{M}\). The constant follows from

\[
 {H_{M,r}C_r\over W}
       ={1+o(1)\over4\sqrt\pi\,r^{3/2}}.                           \tag{12.10}
\]

Since, with

\[
                         N_q=\binom{2M+1}{M-q},
\]

a missing-target count \(M_q\) obeys

\[
                         M_q\ge K_{q,p}-(W-N_q),\qquad
 {W-N_q\over W}=O(q^2/M),                                         \tag{12.11}
\]

if \(r\to\infty\), \(r=o(M^{1/5})\), and the hypotheses above hold for
every depth in the interval, summing over
\(2r\le q\le\lfloor\sqrt M/r\rfloor\) gives

\[
 {1\over W}\sum_qM_q
 \ge {1-o(1)\over16\sqrt\pi}{\sqrt M\over r^{5/2}}.                \tag{12.12}
\]

Consequently, if the actual target alphabet \(L\), including every
allowed phase image, satisfies

\[
                         \log(pL)=o(M^{1/5}),                       \tag{12.13}
\]

then a hash-pure collar construction with boundary-service incidence at
most two has a non-\(o(W)\) aggregate Gaussian-band defect. This is a
coefficient-one obstruction for that class, not for arbitrary
exterior-moving factors.

## 13. Exact proved boundary

The algebraic seed route has both a positive and a negative conclusion.

* **Positive:** the simultaneous owner cocycle admits arbitrary nonlocal
  suffix data on complete components. Theorem 10.1 gives an integral,
  literal, nonconjugate exact factor with bounded component support, a
  quantitative \((1/8-o(1))C_m\) covariant-orbit escape, and an exact
  one-sided \(3/4\) child-fibre bound.
* **Negative:** every complete coordinate-conjugate row option has the
  same root-scale excursion-blind core of sharp mass
  \(R_{m-1}=(1/9+o(1))C_m\). Under occurrence-disjoint fixed carriers,
  Theorem 11.1 lifts it to shallow depth even after arbitrary
  \(p\)-phase choices. More generally, Theorem 12.2 rules out every
  hash-pure collar satisfying the degree-two overlap hypothesis and
  \(\log(pL)=o(M^{1/5})\).

No theorem here rules out a phasewise non-\(H_m\) interleaving satisfying
the full conditions (2.4), (3.2), (3.3), and (3.4), nor a
filling-dependent or exterior-moving cross-parent packet. Such an escape
must disperse the literal target map (12.5) while preserving both
ownership ledgers and zero root monodromy. A larger or more correlated
hash inside the closed-row fixed-collar class cannot do so.
