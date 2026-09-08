# Order-conjugated cube factors: exact local resolution, cycle trades, and the integral owner gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Audited outcome

Let \(\ell=2^t\ge4\), and let \(1\le H\le\ell/2\). Direction margins,
fibre-tagged affine faces, and physical Boolean targets are three different
balancing levels, and they have different answers.
For the ambient Boolean middle layer write
\[
                             W=\binom{2m}{m}.
\]

1. **Direction sets.** A multiset \(\Omega\) of \(M\) cyclic orders is an
   exact simultaneous interval design through \(H\) if every
   \(q\)-subset occurs equally often as a cyclic \(q\)-interval for every
   \(q\le H\). Its forced multiplicities are
   \[
       \lambda_q=\frac{M\ell}{\binom{\ell}{q}},
       \qquad
       \frac{\binom{\ell}{q}}
            {\gcd(\binom{\ell}{q},\ell)}\mid M.          \tag{0.1}
   \]
   All cyclic orders give an exact all-depth design. At \(H=2\), the
   lower divisibility bound is attained by \(\ell-1\) Walecki orders.
   A \(T\)-wise-uniform permutation family implies such a design through
   \(T\); an ordinary orthogonal array does not.

2. **Literal disjoint cube fibres.** There is an exact positive
   coefficient-one local construction. Let \(\mathcal F_\ell\) be the
   recursive half-depth-rainbow factor of \(Q_\ell\), and place every
   coordinate conjugate \(g\mathcal F_\ell g^{-1}\), \(g\in A_\ell\), on a
   different literal copy of \(Q_\ell\). Then:

   * every physical owner is used exactly once;
   * every component is an isometric \(2\ell\)-cycle;
   * for every \(q\le H\), every direction \(q\)-set has exactly
     \[
                      \frac{|A_\ell|\,2^\ell}
                           {\binom{\ell}{q}}             \tag{0.2}
     \]
     forward occurrences, and the same reverse count;
   * every fibre-tagged affine \(q\)-face has load \(0\) or \(1\), on both
     sides.

   Since
   \[
       \frac{2^q}{\binom{\ell}{q}}\le1
       \qquad(q\le\ell/2),                              \tag{0.3}
   \]
   the \(0/1\) assertion is exact floor/ceiling balance, the strongest
   possible integral balance at this density.

3. **Equal positive load on every tagged face.** This is arithmetically
   impossible for one owner-resolving factor when the average in (0.3) is
   strictly below one. Thus “balanced” must mean floor/ceiling incidence,
   not a common positive integer.

4. **One-order linear factors.** If one Hamming-type vertex factor is
   assigned to each of \(M\) disjoint fibres according to an interval
   design, then the unlabelled direction count is exactly
   \[
                         \frac{M2^\ell}{\binom{\ell}{q}}. \tag{0.4}
   \]
   This does not give deep labelled-face balance: a low-redundancy linear
   class has affine collisions beyond logarithmic depth. Taking all
   \(\ell/2\) classes of an edge-resolution shore repairs affine incidence
   exactly, but repeats every owner \(\ell/2\) times on one cube.

5. **Literal order-changing trade.** Every linear transversal kernel from
   LINEAR_CYCLE_TILING.md has a repeated pair of syndrome columns. If
   \(\tau=(a\,b)\) swaps such a pair and
   \(\delta=e_a+e_b\), then the old and conjugated factors decompose into
   \(2^\ell/(4\ell)\) independent two-for-two packets:
   \[
      \boxed{
      \mathbf1_{P+k}+\mathbf1_{P+k+\delta}
      =
      \mathbf1_{\tau P+k}+\mathbf1_{\tau P+k+\delta}.}  \tag{0.5}
   \]
   Either shore of each packet is a literal owner-disjoint cycle
   selection. This is an actual cycle trade, not histogram cancellation.

6. **Trade limitation.** Same-kernel conjugacies preserve the syndrome
   colour of every coordinate. Hence they preserve the cyclic syndrome
   colour word and every quotient-face total. The switches in (0.5) give
   genuine local order bits but cannot generate an unrestricted
   permutation design or repair a syndrome-cell deficit.

7. **Boolean shadow targets.** Direction balance and even perfect
   fibre-tagged face balance do not balance physical Boolean intersection
   targets. For one fixed coordinate-pair frame, every internal
   orientation-cube order field obeys the exact type cut
   \[
        \sum_{T\in\mathcal O^-_{f,q}}L_q(T)\le V_f,
        \qquad
        V_f=
        \frac{m!}{f!^2(m-2f)!}\,2^{m-2f},               \tag{0.6}
   \]
   whereas the number of demanded targets is
   \[
        T_{f,q}=
        \frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.       \tag{0.7}
   \]
   Thus at least \((T_{f,q}-V_f)_+\) targets are missed. At
   \(q=A\sqrt m+o(\sqrt m)\), this is a positive multiple of \(W\).
   Varying orders across literal fibres does not evade this internal
   fixed-frame obstruction. In the standard block concatenation,
   \(O(W/\ell)\) seams add only \(O(qW/\ell)=o(W)\) crossing windows.

8. **Exact remaining equation.** With mixed pair frames, the local cube
   problem is solved but the fibres overlap in their middle owners. The
   remaining theorem is the integral system
   \[
      \sum_{\beta,c:\,x\in\beta}z_{\beta,c}=1
      \quad(\text{every middle owner }x),               \tag{0.8}
   \]
   together with one labelled lower and upper target equation at every
   depth. Its fractional feasibility has an exact separation/Hall dual.
   Its matrix is not generally totally unimodular: a \(4\times4\)
   determinant-\(2\) phase-coset minor occurs already at depth two.

Therefore the requested order-conjugated local resolution exists, with
exact owner integrality and optimal multidepth affine collision behaviour.
It does not prove coefficient one globally. The precise unsolved gate is
the mixed-frame integral owner-plus-target system, not permutation supply,
orthogonal-array size, phase choice, or local cycle residence.

## 1. Cycles, faces, and the only meaningful local normalization

Write
\[
                         V=\mathbb F_2^\ell.
\]
An isometric \(2\ell\)-cycle has direction word
\[
                         \sigma\sigma                  \tag{1.1}
\]
for a permutation \(\sigma\) of the \(\ell\) coordinates. Indeed every
cyclic block of \(\ell\) directions must be repetition-free; comparing
successive \(\ell\)-blocks gives \(d_{i+\ell}=d_i\). Conversely, a doubled
permutation makes every arc of length at most \(\ell\) a cube geodesic.

For an exact cycle factor \(\mathcal F\) of \(Q_\ell\), orient every
component and let \(\rho_{\mathcal F}(x)\) be the direction used from
owner \(x\) to its successor. Put
\[
 D_q^+(x)=
 \{\rho_{\mathcal F}(x),\rho_{\mathcal F}(Fx),\ldots,
   \rho_{\mathcal F}(F^{q-1}x)\},                       \tag{1.2}
\]
and encode the forward affine face by
\[
 \Sigma_q^+(x)=
 \left(D_q^+(x),
 x\big|_{[\ell]\setminus D_q^+(x)}\right).             \tag{1.3}
\]
Define \(\Sigma_q^-\) from the reverse factor. For \(q\le\ell\), these
are exactly the lower and upper pair-flip face data.

There are
\[
                        2^{\ell-q}\binom{\ell}{q}       \tag{1.4}
\]
affine \(q\)-faces and exactly \(2^\ell\) starting owners. Therefore the
mean occurrence load of a factor on the full affine-face universe is
\[
                        \mu_{\ell,q}
                         =\frac{2^q}{\binom{\ell}{q}}.  \tag{1.5}
\]

### Lemma 1.1 (subunit density through half depth)

For \(q\le\ell/2\),
\[
                          \binom{\ell}{q}\ge2^q.        \tag{1.6}
\]

#### Proof

Choose \(2q\) of the \(\ell\) coordinates and partition them into \(q\)
ordered pairs. Choosing one coordinate from each pair gives \(2^q\)
different \(q\)-subsets. \(\square\)

Consequently, at the depths relevant below, a literal integral face design
cannot give the same positive integer to every face. The exact
floor/ceiling optimum is:
\[
                       \text{every face load lies in }\{0,1\}. \tag{1.7}
\]
This is equivalent to injectivity of \(\Sigma_q^\pm\).

## 2. Exact cyclic interval designs

Let \(\Omega\) be a multiset of \(M\) oriented cyclic orders on
\([\ell]\), modulo cyclic rotation. For \(Q\in\binom{[\ell]}q\), define
\[
 b_q^\Omega(Q)=
 \sum_{\omega\in\Omega}\sum_{j\in\mathbb Z_\ell}
 \mathbf1_{\{
 Q=\{\omega_j,\omega_{j+1},\ldots,\omega_{j+q-1}\}\}}. \tag{2.1}
\]

Call \(\Omega\) a cyclic interval \(H\)-design when
\(b_q^\Omega(Q)\) is independent of \(Q\) for every \(q\le H\).

### Theorem 2.1 (exact counts and divisibility)

If \(\Omega\) is a cyclic interval \(H\)-design, then
\[
               b_q^\Omega(Q)=
               \lambda_q=\frac{M\ell}{\binom{\ell}{q}},
               \qquad q\le H,                          \tag{2.2}
\]
and hence
\[
 d_{\ell,q}:=
 \frac{\binom{\ell}{q}}
      {\gcd(\binom{\ell}{q},\ell)}
 \mid M.                                                \tag{2.3}
\]
Thus
\[
                  D_{\ell,H}:=
                  \operatorname{lcm}_{q\le H}d_{\ell,q}
 \mid M.                                                \tag{2.4}
\]

For \(\ell=2^t\) and \(1\le q<\ell\),
\[
 v_2\binom{\ell}{q}=t-v_2(q),                           \tag{2.5}
\]
so
\[
 d_{\ell,q}
 =\frac{\binom{\ell}{q}}{2^{t-v_2(q)}}                 \tag{2.6}
\]
is odd.

#### Proof

Each order has exactly \(\ell\) cyclic \(q\)-positions, so
\[
 \sum_Qb_q^\Omega(Q)=M\ell.
\]
Uniformity gives (2.2), and integrality gives (2.3)--(2.4).

For (2.5), use
\[
 \binom{\ell}{q}=\frac{\ell}{q}\binom{\ell-1}{q-1}.
\]
Modulo two,
\[
 (1+x)^{2^t-1}=1+x+\cdots+x^{2^t-1},
\]
so every \(\binom{\ell-1}{j}\) is odd. Taking two-adic valuations proves
(2.5)--(2.6). \(\square\)

### Theorem 2.2 (canonical all-depth design)

The multiset of all oriented cyclic orders has
\[
                         M=(\ell-1)!                   \tag{2.7}
\]
and is an interval design at every depth, with
\[
                         \lambda_q=q!(\ell-q)!         \tag{2.8}
\]
for \(q<\ell\).

#### Proof

Contract a prescribed \(q\)-set \(Q\) to one cyclic block. Order its
elements in \(q!\) ways and arrange the block with the other
\(\ell-q\) points in \((\ell-q)!\) cyclic orders. This gives (2.8).
Equation (2.2) gives the same value. \(\square\)

If reversal is identified as well, both (2.7) and (2.8) divide by two.

### Theorem 2.3 (sharp depth-two design)

For even \(\ell=2r\), there are \(\ell-1\) cyclic orders in which every
unordered coordinate pair is adjacent exactly twice. This attains the
divisibility lower bound at \(H=2\).

#### Proof

Put \(n=\ell-1\) and label the points
\(\mathbb Z_n\cup\{\infty\}\). For \(a\in\mathbb Z_n\), take
\[
 \omega_a=
 (\infty,a,a-1,a+1,a-2,a+2,\ldots,
   a-(r-1),a+(r-1)).                                    \tag{2.9}
\]
Every edge incident with \(\infty\) occurs twice as \(a\) varies. Among
finite points, the consecutive differences in one order contain two
representatives of every nonzero undirected difference class in
\(\mathbb Z_n\). Translation by \(a\) therefore covers every finite
unordered pair twice. Hence these Hamilton cycles decompose
\(2K_\ell\). Since
\[
 d_{\ell,2}=\ell-1,
\]
the number of orders is minimum. \(\square\)

## 3. Permutation designs and orthogonal arrays

A multiset \(\Pi\subseteq S_\ell\) is \(T\)-wise uniform if for every
\(r\le T\), every choice of distinct positions
\((i_1,\ldots,i_r)\), and every ordered \(r\)-tuple of distinct symbols
\((a_1,\ldots,a_r)\), exactly
\[
                           \frac{|\Pi|}{(\ell)_r}        \tag{3.1}
\]
members satisfy \(\pi(i_j)=a_j\) for all \(j\).

### Proposition 3.1 (permutation design implies interval design)

A \(T\)-wise-uniform permutation multiset is a cyclic interval design
through every \(q\le T\). Its multiplicity is
\[
        \lambda_q=
        \ell q!\frac{|\Pi|}{(\ell)_q}
        =\frac{|\Pi|\ell}{\binom{\ell}{q}}.             \tag{3.2}
\]

If \(|\Pi|=\alpha(\ell)_T\), then
\[
        \lambda_q=
        \ell\alpha q!(\ell-q)_{T-q}.                    \tag{3.3}
\]

#### Proof

For a fixed unordered \(Q\), sum over the \(\ell\) cyclic position blocks
and the \(q!\) orderings of \(Q\). Distinctness makes the events
disjoint. Equation (3.1) gives (3.2)--(3.3). \(\square\)

This hypothesis is stronger than necessary: (2.1) asks only that the sum
over cyclic position blocks be uniform.

An ordinary \(OA(N,\ell,\ell,T)\) is not the relevant object. At strength
two it must realize equal symbols in two different columns, whereas every
permutation row has distinct symbols. The correct analogue is a
permutation orthogonal array, equivalently a \(T\)-wise-uniform family on
injective tuples.

The affine group gives a small fixed-strength example. The group
\[
                         AGL(t,2)                       \tag{3.4}
\]
on the \(\ell=2^t\) points is three-transitive, since every three distinct
binary points are affinely independent. Hence one group-indexed orbit of a
cyclic order is an exact interval design through depth three. Its size is
\[
                 |AGL(t,2)|
                 =\ell\prod_{i=0}^{t-1}(\ell-2^i).      \tag{3.5}
\]

For \(\ell\ge8\), one full group-indexed \(AGL(t,2)\)-orbit cannot balance
four-sets. The
four-sets split into affine planes and nonplanes, and the number of planes
is
\[
       \frac{\ell(\ell-1)(\ell-2)}{24}
       =\frac1{\ell-3}\binom{\ell}{4}.                  \tag{3.6}
\]
Uniformity would force the base cyclic order to contain exactly
\[
                           \frac{\ell}{\ell-3}           \tag{3.7}
\]
planar four-windows, which is not an integer. A union of \(B\) full
group-indexed orbits, each taken with the same multiplicity convention,
must at least satisfy \(\ell-3\mid B\). Quotienting to distinct orbit
elements with different stabilizers requires the corresponding weighted
version.

Thus permutation entropy is plentiful, but a bounded-strength affine or
ordinary-OA construction does not give the growing-\(H\) theorem.

## 4. One-order Hamming factors on disjoint fibres

Fix a cyclic order \(\omega\). One Hamming-type vertex-resolution class
of \(Q_\ell\) contains
\[
                           \frac{2^\ell}{2\ell}          \tag{4.1}
\]
isometric cycles, all with word \(\omega\omega\). For \(q<\ell\), a fixed
direction \(q\)-set \(Q\) occurs
\[
 \frac{2^\ell}{\ell}
 \mathbf1_{\{Q\text{ is a cyclic interval of }\omega\}} \tag{4.2}
\]
times.

### Proposition 4.1 (literal-fibre direction resolution)

Let \(\Omega\) be a cyclic interval \(H\)-design of size \(M\). Take
\(M\) pairwise disjoint literal copies of \(Q_\ell\), and put one
order-conjugated Hamming vertex factor with order \(\omega\) on the copy
indexed by \(\omega\). Then every owner is used once and, for every
\(q\le H\), every direction \(q\)-set has exactly
\[
                           \frac{M2^\ell}{\binom{\ell}{q}} \tag{4.3}
\]
occurrences.

#### Proof

Owner integrality holds separately in each disjoint cube. Multiply the
interval multiplicity (2.2) by the conditional occurrence count
\(2^\ell/\ell\) in (4.2). \(\square\)

This is an exact resolvable direction design. It is not a deep affine-face
design. A single linear class has syndrome rank only
\(\log_2(2\ell)\), so its face multiplicities must collide beyond
logarithmic depth.

There is an exact affine multicover if owner repetition is allowed. In the
parity-resolved construction, all \(\ell/2\) vertex factors in one
edge-resolution shore give every affine interval \(q\)-face multiplicity
\[
                              2^{q-1}.                  \tag{4.4}
\]
Here and throughout this use, \(q<\ell\); the standing
\(H\le\ell/2\) guarantees it.
Combining a size-\(M\) interval design with every shore class gives every
abstract affine \(q\)-face multiplicity
\[
                              2^{q-1}\lambda_q.         \tag{4.5}
\]

For \(M_{\rm fac}\) superposed vertex factors, equal affine load forces
\[
             e_{\ell,q}:=
             \frac{\binom{\ell}{q}}
                  {\gcd(\binom{\ell}{q},2^q)}
             \mid M_{\rm fac}.                          \tag{4.6}
\]
Using (2.5),
\[
 e_{\ell,q}
 =d_{\ell,q}\,
 2^{\max\{t-v_2(q)-q,0\}},                              \tag{4.7}
\]
and therefore
\[
 \operatorname{lcm}_{q\le H}e_{\ell,q}
       =\frac{\ell}{2}D_{\ell,H}.                       \tag{4.8}
\]
Thus an interval design of minimum possible size \(D_{\ell,H}\), if it
exists, combined with a full shore has no extra divisibility loss.

At \(H=2\), Theorem 2.3 gives
\[
                        M_{\rm fac}=\frac{\ell(\ell-1)}2, \tag{4.9}
\]
which is universally minimum. Every affine edge has multiplicity
\(\ell-1\), and every affine square has multiplicity \(4\).

Equations (4.4)--(4.9) describe factors superposed on one abstract face
catalogue. They are not a coefficient-one construction there: every owner
is repeated \(\ell/2\) times for each order. Placing those factors on
different physical fibres restores owner integrality, but the fibre
exterior becomes part of the physical face label. The faces then no longer
receive the common multiplicities in (4.5).

## 5. Exact owner-one, half-depth affine balance

The preceding defect is removed by allowing the cyclic order to vary from
cycle to cycle inside one nonlinear factor.

Define \(F_\ell:Q_\ell\to Q_\ell\) recursively. For \(\ell=1\), let it
toggle the unique bit. If \(\ell=2a\), write \(x=(u,v)\in Q_a\times Q_a\)
and set
\[
 F_{2a}(u,v)=
 \begin{cases}
   (F_a(u),v),&|u|+|v|\equiv0\pmod2,\\
   (u,F_a(v)),&|u|+|v|\equiv1\pmod2.
 \end{cases}                                           \tag{5.1}
\]

### Theorem 5.1 (recursive half-depth-rainbow factor)

For every power of two \(\ell\ge2\):

1. \(F_\ell\) is a permutation whose cycles all have length \(2\ell\);
2. every cycle has a direction word \(\pi\pi\), and hence is isometric;
3. for every \(q\le\ell/2\), both maps
   \(\Sigma_q^+\) and \(\Sigma_q^-\) are injective.

#### Proof

For \(\ell=2\), the assertion is checked directly on the unique square:
its four forward (and four reverse) depth-one starts give the four distinct
cube edges, distinguished by direction label and fixed outside bit.

Now let \(\ell=2a\) with \(a\ge2\), and assume the theorem for \(a\).
The inverse is obtained by moving the left half at odd total parity and
the right half at even total parity. Thus \(F_{2a}\) is a permutation.
Successive moves alternate halves, and
\[
                 F_{2a}^{\,2j}(u,v)
                    =(F_a^j(u),F_a^j(v)).              \tag{5.2}
\]
Inductively each parent cycle has exact length \(2a\), so (5.2) gives
child length \(4a=2(2a)\); odd returns are excluded by parity.

During the first \(2a\) child moves, each half makes \(a\) moves. The
parent direction word uses every coordinate once in any \(a\) consecutive
moves. Hence the first \(2a\) child directions form a permutation of all
coordinates and the next \(2a\) repeat it. This proves isometry.

For forward injectivity, let \(q=2r\). The shadow data split into the two
parent shadows
\[
                         \Sigma_r^+(u),\qquad
                         \Sigma_r^+(v),                 \tag{5.3}
\]
which recover \(u,v\) by induction. If \(q=2r+1\), one half makes
\(r+1\) moves and the other makes \(r\). The cardinalities of the two
deleted direction sets identify which half moved first, and the data split
into depths \(r+1,r\). Since \(a\ge2\) is even and the present \(q\) is
odd, \(q\le a\) implies \(q\le a-1\); hence both parent depths are at most
\(a/2\).
Induction again recovers \(u,v\). The inverse recursion is identical, so
the same proof gives reverse injectivity. \(\square\)

We now symmetrize this already integral factor across **different** literal
fibres, not across overlapping phases.

### Theorem 5.2 (order-conjugated literal-fibre resolution)

Let \(G\le S_\ell\) be transitive on \(q\)-subsets for every \(q\le H\).
For each \(g\in G\), take one disjoint labelled copy \(\beta_g\) of
\(Q_\ell\), and put the conjugated factor
\[
                         gF_\ell g^{-1}                 \tag{5.4}
\]
on \(\beta_g\). Then:

1. every owner in \(\bigsqcup_g\beta_g\) occurs in exactly one cycle;
2. every component is an isometric \(2\ell\)-cycle;
3. for each \(q\le H\) and \(Q\in\binom{[\ell]}q\), the number of forward
   starts with direction set \(Q\) is
   \[
                         \boxed{
                         \frac{|G|2^\ell}{\binom{\ell}{q}};} \tag{5.5}
   \]
   the reverse count is the same;
4. every fibre-tagged affine \(q\)-face has forward load in
   \(\{0,1\}\), and reverse load in \(\{0,1\}\).

#### Proof

Items 1--2 follow from disjointness of the fibres and Theorem 5.1.
For the direction count, let
\[
 w_q(D)=|\{x\in Q_\ell:D_q^+(x)=D\}|                  \tag{5.6}
\]
in the base factor. Then \(\sum_Dw_q(D)=2^\ell\). In the \(g\)-conjugate,
the count at \(Q\) is \(w_q(g^{-1}Q)\). By \(q\)-homogeneity, for every
fixed \(D,Q\),
\[
             |\{g\in G:gD=Q\}|=\frac{|G|}{\binom{\ell}{q}}. \tag{5.7}
\]
Summing first over \(D\) proves (5.5). Apply the same argument to the
reverse factor.

Theorem 5.1 makes each affine face map injective inside its fibre.
Different fibres have different physical tags, so their face images are
disjoint. This proves item 4. \(\square\)

For each fixed direction \(Q\), the tagged union contains
\(|G|2^{\ell-q}\) affine \(Q\)-faces, of which exactly the number in
(5.5) are selected. Hence the selected density is the same
\[
                         \frac{2^q}{\binom{\ell}{q}}    \tag{5.7a}
\]
for every direction class, while every individual load is \(0\) or \(1\).
Thus Theorem 5.2 balances both the direction margin and the finest
fibre-tagged affine incidence.

One may take
\[
                             G=A_\ell,                  \tag{5.8}
\]
which is homogeneous on \(q\)-subsets for every \(q\), and has
\[
                             |G|=\ell!/2.               \tag{5.9}
\]
Indeed, start with any permutation sending one \(q\)-set to another. If
it is odd, compose it with a transposition inside the target set or its
complement; for \(\ell\ge4\), at least one of those two sets has size at
least two. The resulting map is even and has the same set image.
Thus Theorem 5.2 is an explicit simultaneous construction through every
\(H\le\ell/2\).

By Lemma 1.1, item 4 is exact floor/ceiling affine balance. It is stronger
than small discrepancy: the collision excess is identically zero at every
depth in both directions.

### Corollary 5.3 (packing complete conjugacy orbits into a large stratum)

Partition a source \(Q_s\) into
\[
                              B=2^{s-\ell}              \tag{5.10}
\]
literal \(Q_\ell\)-fibres using one common active coordinate set. Group
\(\lfloor B/|A_\ell|\rfloor|A_\ell|\) fibres into complete conjugacy
orbits and leave fewer than \(|A_\ell|\) fibres exceptional.

The exceptional vertex fraction is at most
\[
                  \frac{|A_\ell|}{2^{s-\ell}}
                  \le
                  2^{\,O(\ell\log\ell)-(s-\ell)}.       \tag{5.11}
\]
Hence it is \(o(1)\) whenever
\[
                         \ell\log\ell=o(s).             \tag{5.12}
\]
On every retained fibre, owners are used exactly once; on every complete
orbit block, (5.5) is exact simultaneously for all \(q\le H\).

In the intended regime
\[
 H\asymp\sqrt{m\log m},
 \qquad
 \ell\asymp\sqrt m\,\log m,
 \qquad s=\Theta(m),                                   \tag{5.13}
\]
conditions \(H\le\ell/2\) and (5.12) both hold. The low-\(s\) source
strata have exponentially small middle mass by the standard split-pair
tail estimate. Thus the local orbit remainder costs \(o(W)\).

This is a genuine local theorem with the requested owner quantifier. It
does not identify faces in different fibres with one common Boolean
target.

In fact, within one fixed source stratum
\(\alpha=(F_0,E_0,R)\), the physical lower and upper shadow maps are
injective on all retained starts through \(H\). The lower target records
the free direction set as its newly empty pairs \(D\) in
\(E_0\cup D\), and then records every unflipped split orientation; the
upper target analogously records \(D\) in \(F_0\cup D\). Thus the affine
face data can be reconstructed from the target once \(\alpha\) is fixed.
The unresolved collisions are between different source strata, not within
one literal-fibre orbit block.

## 6. Exact owner-preserving cycle trades

Theorem 5.2 varies whole factors between disjoint fibres. There is also a
literal order-changing switch inside one fixed cube.

Let \(P,Q\subseteq V\) be two \(2\ell\)-cycle transversals for the same
subgroup \(K\le V\). Thus
\[
 \mathcal F_P=\{P+k:k\in K\},
 \qquad
 \mathcal F_Q=\{Q+k:k\in K\}                            \tag{6.1}
\]
are vertex factors. For \(p\in P\), let \(q(p)\in Q\) be the unique point
in the same \(K\)-coset and put
\[
                         d(p)=p+q(p)\in K.              \tag{6.2}
\]

### Theorem 6.1 (same-kernel overlay components)

Fix \(p_0\in P\), and let
\[
                 H_{P,Q}=
                 \langle d(p)+d(p_0):p\in P\rangle
                 \le K.                                \tag{6.3}
\]
The owner overlay of \(\mathcal F_P,\mathcal F_Q\) is the bipartite
Cayley multigraph
\[
                  k_L\longleftrightarrow(k+d(p))_R
                  \qquad(k\in K,\ p\in P).             \tag{6.4}
\]
Its connected components are exactly
\[
       (k+H_{P,Q})_L
       \ \sqcup\
       (k+d(p_0)+H_{P,Q})_R.                            \tag{6.5}
\]
Every component has \(|H_{P,Q}|\) cycles on each shore. A selection of
whole old/new cycles covers every owner exactly once if and only if it
chooses one complete shore independently in every component.

#### Proof

The owner \(p+k\) lies in the old cycle \(P+k\). Since
\[
 p+k=q(p)+(k+d(p)),
\]
it lies in the new cycle \(Q+k+d(p)\), proving (6.4).

An even overlay walk changes an old label by a sum of vectors
\(d(p)+d(p')\), so its reachable old labels are contained in a coset of
\(H_{P,Q}\). Conversely the generators in (6.3) are realized by two-edge
walks through the \(p\)- and \(p_0\)-edges. This proves (6.5).

Let \(u_C,v_D\in\{0,1\}\) record selected cycles. Every owner edge \(CD\)
requires
\[
                              u_C+v_D=1.                \tag{6.6}
\]
On a connected component, these equations force all old values equal and
all new values equal to their complement. Thus precisely one full shore is
chosen. Since every selected object is a whole component cycle of one of
the two isometric factors, the resulting owner partition is again a factor
into isometric \(2\ell\)-cycles. \(\square\)

### Theorem 6.2 (explicit two-for-two transposition packet)

Let \(K=\ker\phi\) be a kernel from the linear-cycle construction with
\(\ell=2^t\ge4\). Two of its first \(\ell-1\) syndrome columns coincide:
\[
                        \phi(e_a)=\phi(e_b).            \tag{6.7}
\]
Put
\[
                        \delta=e_a+e_b\in K,
                        \qquad\tau=(a\,b).              \tag{6.8}
\]
Then \(\tau K=K\), \(\tau P\) is a cycle transversal, and the
\(P/\tau P\) overlay has exactly
\[
                            \frac{|K|}{2}
                              =\frac{2^\ell}{4\ell}      \tag{6.9}
\]
components. Each component is the literal trade (0.5).

#### Proof

In the linear construction the first \(\ell-1\) columns are
\[
                         c_i=u_i+u_{i-1}
                         \qquad(1\le i<\ell),           \tag{6.10a}
\]
where \(u_0,\ldots,u_{\ell-1}\) enumerate \(\mathbb F_2^t\).
They are nonzero. If they were all distinct, they would be all nonzero
vectors of \(\mathbb F_2^t\), whose sum is zero for \(t\ge2\). But
telescoping gives
\[
                         \sum_{i=1}^{\ell-1}c_i
                           =u_{\ell-1}\ne0,
\]
a contradiction. Thus (6.7) always has a solution.

The repeated-column identity gives
\[
                             \phi\tau=\phi,             \tag{6.10}
\]
so \(\tau K=K\), and \(\tau P\) is again a transversal. For every
\(p\in P\), the same-coset match is \(q(p)=\tau p\), and
\[
                 d(p)=p+\tau p\in\{0,\delta\}.          \tag{6.11}
\]
Both values occur: while traversing \(P\), the \(a\)- and \(b\)-bits agree
before the first of those coordinates is flipped and differ between their
two flip positions. Therefore
\[
                         H_{P,\tau P}=\langle\delta\rangle. \tag{6.12}
\]
Theorem 6.1 gives two cycles on each shore and \(|K|/2\) components.
Equation (6.6) proves the pointwise owner identity (0.5). \(\square\)

The repeated columns cannot be adjacent in the syndrome enumeration:
equality of adjacent columns would force two enumerated syndrome vertices
to coincide. If their positions in the cyclic direction order have
directed separation \(d\), \(1<d<\ell-1\), then in every packet
\[
\begin{array}{c|cc}
 &\tau P+k&\tau P+k+\delta\\ \hline
 P+k&2\ell-2d&2d\\
 P+k+\delta&2d&2\ell-2d
\end{array}                                             \tag{6.13}
\]
are the owner-intersection multiplicities. Hence the component is a
connected \(K_{2,2}\) with parallel owner edges; no one-for-one subtrade
exists.

For \(q<\ell\) and a direction set \(D\), switching one packet changes the
depth-\(q\) direction count by
\[
 4\left(
 \mathbf1_{\{D\text{ interval in }\tau\sigma\}}
 -
 \mathbf1_{\{D\text{ interval in }\sigma\}}
 \right).                                               \tag{6.14}
\]
For \(\ell\ge8\), this genuinely changes the unoriented cyclic order. At
\(\ell=4\), the forced swap reverses it, so the unoriented interval
catalogue is unchanged even though the affine cycle trade remains
nontrivial.

### Theorem 6.3 (general code-stabilizer packet size)

If a coordinate permutation \(\tau\) satisfies \(\phi\tau=\phi\), then
\[
                    H_{P,\tau P}=\operatorname{im}(I+\tau)\le K. \tag{6.15}
\]
If \(c(\tau)\) is the number of coordinate cycles of \(\tau\), every
overlay component has
\[
                    2^{\ell-c(\tau)}                   \tag{6.16}
\]
cycles on each shore.

#### Proof

Take \(p_0=0\in P\). Then \(d(p)=(I+\tau)p\). The vertices of \(P\)
span \(V\): its successive prefix differences give \(\ell-1\) coordinate
basis vectors and its antipodal vertex supplies the last. Thus the span of
the \(d(p)\)'s is \(\operatorname{im}(I+\tau)\). A vector lies in
\(\ker(I+\tau)\) precisely when it is constant on every coordinate cycle
of \(\tau\), so the kernel dimension is \(c(\tau)\). Rank-nullity gives
(6.16). \(\square\)

This is an exact storage law: a single equal-column transposition is the
minimal nontrivial packet, while \(r\) disjoint transpositions require
\(2^r\) cycles per shore.

## 7. What the trades cannot change

Colour coordinate \(i\) by its syndrome column
\[
                              \kappa(i)=\phi(e_i).       \tag{7.1}
\]
Every code-stabilizing conjugacy \(\tau\) with \(\phi\tau=\phi\) permutes
coordinates only within equal-colour classes. Therefore the cyclic colour
word
\[
       \kappa(\sigma_1),\kappa(\sigma_2),\ldots,
       \kappa(\sigma_\ell)                              \tag{7.2}
\]
is invariant under every sequence of the trades in Section 6.

### Corollary 7.1 (colour-window obstruction)

A \(q\)-set \(D\) can become a cyclic interval under these same-kernel
trades only if the colour multiset of \(D\) equals the colour multiset of
some cyclic \(q\)-window of (7.2). At \(q=2\), only colour pairs adjacent
in (7.2) are reachable.

Moreover, for \(\tau=(a\,b)\) as in Theorem 6.2, applying \(\tau\) to an
old packet gives exactly the new packet. Hence the new labelled affine
face multiset is the \(\tau\)-image of the old one. Since
\(\phi\tau=\phi\), every quotient face
\[
                         \phi(x)+\phi(V_D)              \tag{7.3}
\]
retains its total multiplicity.

Thus the independent packet bits redistribute physical faces only inside
fixed syndrome cells. For one repeated pair, all packet bits also have the
same direction-change vector (6.14). They cannot furnish the independent
coordinates of a growing permutation design.

The trade theorem is nevertheless a genuine advance: local order change
and owner integrality coexist exactly. What is missing is a family of
trades that changes the syndrome-colour word, or a nonlinear recursive
trade such as Theorem 5.1 together with global target synchronization.

## 8. The exact labelled owner-and-target system

We now retain every physical label.

A literal active cube is
\[
 \beta=(\alpha,A,\zeta),                               \tag{8.1}
\]
where:

* \(\alpha=(F_0,E_0,R)\) is a source full/empty/split stratum;
* \(A\subseteq R\), \(|A|=\ell\), is the active pair-direction set;
* \(\zeta\) is the spectator orientation on \(R\setminus A\).

A local option \(c\in\mathcal C_\beta\) contains:

* one exact isometric cycle factor on \(\beta\);
* all its state-dependent direction orders and phases;
* a clipped radius label \(r_c(x)\);
* its literal forward and reverse face maps through \(H\).

Let
\[
 z_{\beta,c}\in\{0,1\}.                                \tag{8.2}
\]
For a lower or upper Boolean target \(T\) at depth \(q\), define the exact
coefficient
\[
 a_{T,q}^{\pm}(\beta,c)=
 \#\{x\in\beta:
 r_c(x)\ge q,\ 
 \partial^\pm\Sigma_{q,c}(x)=T\}.                      \tag{8.3}
\]

### Theorem 8.1 (necessary and sufficient integral system)

An integral selection of the local options uses every middle owner exactly
once and realizes prescribed lower/upper target loads \(b_{T,q}^\pm\) if
and only if
\[
 \boxed{
 \sum_{\beta,c:\,x\in\beta}z_{\beta,c}=1
 \qquad(\text{every middle owner }x),}                 \tag{8.4}
\]
\[
 \boxed{
 \sum_{\beta,c}
 a_{T,q}^{\pm}(\beta,c)z_{\beta,c}
 =b_{T,q}^\pm
 \qquad(T,q,\pm).}                                     \tag{8.5}
\]

If the \(\beta\)'s form one fixed disjoint physical partition, (8.4)
reduces to
\[
                         \sum_{c\in\mathcal C_\beta}
                              z_{\beta,c}=1
                         \qquad(\text{every }\beta).    \tag{8.6}
\]

#### Proof

Every selected local factor covers each owner of its cube once. Therefore
the multiplicity of owner \(x\) is exactly the left side of (8.4).
Likewise (8.3) counts all and only the selected consecutive windows whose
literal shadow is \(T\). This proves necessity and sufficiency. Disjointness
gives (8.6). \(\square\)

For an **unthinned, common-order Hamming option** at \(q<\ell\),
\[
 c=(\sigma,\Psi,K_0,a)
\]
and a physical affine face \(F=x+V_D\subseteq\beta\), its coefficient is
\[
 m_{\beta,c}(F)=
 \begin{cases}
 2^{q-\rho_c(D)},&
 D\text{ is a cyclic interval beginning at }j,\\
 &a\in\Psi(x+p_j)+\Psi(V_D),\\
 0,&\text{otherwise},
 \end{cases}                                           \tag{8.7}
\]
where
\[
                         \rho_c(D)=\dim\Psi(V_D).        \tag{8.8}
\]
Summing over affine offsets gives the exact direction projection
\[
 \sum_{\substack{F:\,\operatorname{dir}F=D}}
 m_{\beta,c}(F)
 =
 \frac{2^\ell}{\ell}
 \mathbf1_{\{D\text{ is an interval of }\sigma\}}.     \tag{8.9}
\]

Equation (8.9) explains the gap: a direction design is only a projection
of (8.5). It discards all affine-offset, exterior, pair-frame, radius, and
upper/lower synchronization data.

If the Hamming option carries a nonconstant radius label, (8.7) must be
replaced by the literal active-start count
\[
 |(p_j+r_a+\ker\Psi)\cap F\cap\{x:r_c(x)\ge q\}|,       \tag{8.10}
\]
and (8.9) becomes the number of active starts with direction set \(D\).
Neither formula is asserted for the recursive state-dependent-order factor;
that factor is covered by the general coefficient (8.3).

Already at \(q=1\), two different phase classes have identical direction
counts but different physical edge supports. At face-simple depths,
different syndrome cosets can have disjoint face supports. Hence no
implication from direction balance to (8.5) is possible.

## 9. Exact fractional Hall dual and the integrality obstruction

First suppose the physical fibres \(\beta\) are disjoint, so the owner
rows are (8.6). Let
\[
                    v_{\beta,c}\in\mathbb R^{\mathcal T} \tag{9.1}
\]
be the vector of all desired target/radius incidences of option \(c\), and
let \(b\) be the demanded vector.

### Theorem 9.1 (weighted Hall/separation criterion)

There is a fractional selection
\[
 x_{\beta,c}\ge0,\qquad
 \sum_cx_{\beta,c}=1,\qquad
 \sum_{\beta,c}x_{\beta,c}v_{\beta,c}=b               \tag{9.2}
\]
if and only if, for every real target weight vector \(y\),
\[
 \boxed{
 \langle y,b\rangle
 \le
 \sum_\beta\max_{c\in\mathcal C_\beta}
              \langle y,v_{\beta,c}\rangle.}           \tag{9.3}
\]

#### Proof

The attainable fractional set is the Minkowski sum
\[
                  \sum_\beta
                  \operatorname{conv}
                  \{v_{\beta,c}:c\in\mathcal C_\beta\}. \tag{9.4}
\]
Its support function is the right side of (9.3). Membership in a compact
convex set is equivalent, by finite-dimensional separation, to domination
by its support function for every \(y\). \(\square\)

Indicator weights \(y=\mathbf1_U\) give ordinary Hall-type cuts, but all
real \(y\)'s are needed in general.

There is one clean integral-flow case. Suppose every option has a profile
\(g\), all options of profile \(g\) have the same incidence vector, and
the demand is genuinely
\[
                           b=\sum_gr_gv_g              \tag{9.5a}
\]
with exactly \(r_g\) fibres required of every profile. This requires
literal target-label alignment across fibres; an abstractly identical
coset label is not enough when the exterior labels differ. Join
\(\beta\) to every allowed \(g\). Then an integral choice exists if and
only if
\[
                         \sum_gr_g=|\mathcal B|         \tag{9.5}
\]
and
\[
       |X|\le\sum_{g\in N(X)}r_g
       \qquad(X\subseteq\mathcal B).                   \tag{9.6}
\]
This is the capacitated bipartite Hall theorem and follows from integral
max flow.

Multiple depths produce tuples of affine-coset profiles rather than one
partition, and total unimodularity already fails in the smallest
three-direction pattern.

### Proposition 9.2 (determinant-two obstruction)

Let the phase-label space be \(A_0=\mathbb F_2^2\), ordered as
\[
                         00,10,01,11.
\]
Take the three lines
\[
 B_1=\langle10\rangle,\quad
 B_2=\langle01\rangle,\quad
 B_3=\langle11\rangle.                                \tag{9.7}
\]

These three rows occur in one literal depth-two parity system. Take
\(\ell=8\), syndrome space \(\mathbb F_2^3\), parity equal to the first
bit, and the alternating prefix-syndrome enumeration
\[
 000,100,010,101,001,110,011,111.                      \tag{9.7a}
\]
Its cyclic coordinate columns are
\[
 100,110,111,100,111,101,100,111.                      \tag{9.7b}
\]
The first three adjacent column sums are
\[
                         010,\quad001,\quad011,
\]
which span precisely \(B_1,B_2,B_3\) after identifying the even shore
with \(\mathbb F_2^2\). Every adjacent pair of columns is distinct, hence
independent, so these intervals are face-simple. Choosing one affine face
whose allowed phase set is the zero coset of each line, together with the
fibre-choice row, realizes the matrix below as an actual configuration
submatrix.

For two replicated choices, require one selected label in the zero coset
of each \(B_i\) and total mass two. The phase counts \(n_a\) obey
\[
 \begin{pmatrix}
 1&1&0&0\\
 1&0&1&0\\
 1&0&0&1\\
 1&1&1&1
 \end{pmatrix}
 \begin{pmatrix}n_{00}\\n_{10}\\n_{01}\\n_{11}\end{pmatrix}
 =
 \begin{pmatrix}1\\1\\1\\2\end{pmatrix}.               \tag{9.8}
\]
The determinant is \(+2\), and the unique solution is
\[
                         n_a=\frac12\quad(a\in A_0).    \tag{9.9}
\]
Thus every fractional marginal passes, but no integral phase selection
exists.

The determinant-\(2\) non-total-unimodularity statement is literal by
(9.7a)--(9.7b). The two-replica infeasibility additionally identifies the
three coset rows across the replicas; for exterior-distinct physical
fibres that target-label alignment is an extra hypothesis. The example is
therefore a rigorous obstruction to generic TU rounding, not by itself a
global Boolean-target counterexample.

This is the phase-coset form of the odd relation
\[
                         10+01+11=0.                   \tag{9.10}
\]
It proves that neither ordinary Hall cuts nor an orthogonal array implies
integral simultaneous-depth selection.

## 10. The fixed-pair cut survives every order field

Fix one perfect matching of the \(2m\) ground coordinates. A lower
rank-\(m-q\) target of type \(f\) has
\[
 f\text{ full pairs},\quad
 f+q\text{ empty pairs},\quad
 m-2f-q\text{ split pairs}.                            \tag{10.1}
\]
Its orbit size is (0.7). The source middle owners with \(f\) full,
\(f\) empty, and \(m-2f\) split pairs number (0.6).

Every **internal** pair-flip \(q\)-window beginning at a source owner of type \(f\)
has a lower target of the same type \(f\). Therefore, for every choice of
cyclic orders, kernels, phases, recursive factors, and local trades,
\[
             \sum_{T\in\mathcal O^-_{f,q}}L_q(T)=V_f  \tag{10.2}
\]
in the unthinned factor. With a radius-\(q\) active subset, the left side
is at most \(V_f\).

Consequently
\[
 \boxed{
 \#\{\text{missed type-}f\text{ targets}\}
 \ge(T_{f,q}-V_f)_+.}                                  \tag{10.3}
\]
The exact average load is
\[
 \lambda_{f,q}
 =\frac{V_f}{T_{f,q}}
 =\frac{2^q\binom{f+q}{q}}
        {\binom{m-2f}{q}}.                             \tag{10.4}
\]

At \(f=0\), whenever \(\binom mq>2^q\), at least
\[
                 2^{m-q}\left(\binom mq-2^q\right)     \tag{10.5}
\]
labelled targets are missed. More sharply, if
\[
                         q=A\sqrt m+o(\sqrt m),
                         \qquad A>0,                    \tag{10.6}
\]
then, with \(N_q=\binom{2m}{m-q}\),
\[
 \frac1{N_q}\sum_f(T_{f,q}-V_f)_+
 \longrightarrow
 \Phi(A/2)-e^{A^2}\Phi(-3A/2)>0.                       \tag{10.7}
\]
Thus the deficit is \(\Theta_A(W)\) at one fixed Gaussian depth.

For the standard block literalization, there are \(O(W/\ell)\) cycle or
block interfaces. At most \(O(q)\) depth-\(q\) windows cross each
interface, so all crossing windows contribute only
\[
                           O(qW/\ell)=o(W)              \tag{10.8}
\]
when \(q=o(\ell)\). They cannot repair the \(\Theta_A(W)\) deficit in
(10.7). Thus Theorem 5.2 resolves the fibre-tagged local
owner/order/affine-collision problem, but it cannot yield coefficient one
inside one fixed-frame orientation-cube block architecture with
\(O(W/\ell)\) interfaces.

This does **not** rule out a no-cut globally fused construction, a dynamic
pair frame inside windows, or \(\Omega(W/q)\) genuinely cross-stratum
interfaces. Those constructions fall outside the internal-window identity
(10.2).

## 11. Precise constant-one boundary

The following are proved.

1. Exact simultaneous cyclic interval designs have the counts and
   divisibilities (2.2)--(2.6). Full permutation symmetry gives an
   all-depth construction, and Walecki attains the minimum through depth
   two.
2. Permutation \(T\)-designs imply interval designs through \(T\);
   ordinary orthogonal arrays and bounded affine-group orbits do not solve
   growing depth.
3. The recursive factor, conjugated across disjoint literal fibres, gives
   an exact owner-one resolution with uniform direction counts and
   collision-free forward and reverse affine faces through half depth.
4. Repeated syndrome columns give the literal two-for-two order trade
   (0.5). The general component size is (6.16).
5. Same-kernel trades preserve syndrome-colour and quotient-face totals.
6. The full labelled selection problem is exactly (8.4)--(8.5), its
   fractional dual is (9.3), and its configuration matrix is not generally
   integral.
7. One fixed-frame orientation-cube block construction fails the type cut
   (10.3) by a positive Gaussian density; its standard
   \(O(W/\ell)\)-interface literalization cannot repair that deficit when
   \(q=o(\ell)\).

The new positive local theorem may be inserted into any mixed-frame
construction: it removes local order entropy, face collision, residence,
and middle-owner defects at once. What remains unproved is:

> Select overlapping mixed-frame literal cubes and one local conjugate in
> each selected cube so that every middle owner satisfies (8.4), every
> lower and upper target satisfies (8.5) with the floor-corrected SCD/MWB
> quota, and the selected cycles admit one literal contiguous-OR
> concatenation with \(o(W)\) boundary toll.

No direction design, phase average, orthogonal array, or pairwise cycle
trade proves that integral statement. Conversely, the local cube geometry
is no longer the missing theorem.

## 12. Independent audit corrections

The decisive positive and negative steps were independently rederived.
The following corrections are already incorporated above.

1. The half-depth induction starts at \(F_2\), checked directly. The
   parent-depth inequality used in the odd case is false for the formal
   \(F_1\) base but correct for every induction step \(a\ge2\).
2. The factor \(4\) in the two-for-two directional change (6.14), the
   intersection counts \(2\ell-2d,2d\), and the general shore size
   \(2^{\ell-c(\tau)}\) were all checked independently.
3. The matrix in (9.8) has determinant \(+2\), not \(-2\).
   Enumeration (9.7a) makes it a literal depth-two configuration minor;
   the separate two-replica infeasibility still requires aligned physical
   target labels.
4. Formulas (8.7)--(8.9) are explicitly restricted to unthinned
   common-order Hamming options and \(q<\ell\). Radius-thinned and recursive
   options use the general literal coefficient (8.3).
5. The fixed-frame type law concerns internal pair-flip windows. Its
   coefficient-one consequence uses the explicit seam bound (10.8) and
   does not exclude a genuinely no-cut or interface-dense construction.

No correction changes Theorem 5.2, the literal trade (0.5), or the exact
integral owner system (8.4)--(8.5).
