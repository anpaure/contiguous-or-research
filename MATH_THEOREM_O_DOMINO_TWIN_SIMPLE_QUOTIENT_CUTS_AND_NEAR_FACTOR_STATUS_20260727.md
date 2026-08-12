# Domino-twin annular superpackets: simple quotient, exact cuts, and the near-factor gate

**Date:** 2026-07-27  
**Lane:** O, constant-one annular obstruction  
**Status:** exact local structure, degrees, codegrees, design divisibility, and the principal Hall-type cuts are proved below.  A near-factor is **not** proved, and no positive-density cut obstruction is found.  The unresolved statement is isolated precisely in Theorem 9.3.

---

## 0. Executive verdict

Let
\[
n=2m,\qquad R=m-q_0=2r+1<m,
\qquad g=n-2R=2q_0>0,
\]
where (q_0=a\sqrt m+O(1)), with fixed (a>0), and let
\[
N=N_R:=\binom nR=\Theta(W).
\]
For a cyclic order (P=(x_0,\ldots,x_{n-1})), let (E_R(P)) be its (n) cyclic (R)-intervals.  Put
\[
\tau=(0\ 1)(2\ 3)\cdots(n-2\ n-1),
\qquad
Q(P):=E_R(P)\cup E_R(P^\tau).
\]
Because (R) is odd, the two component packets are disjoint and (|Q(P)|=2n=4m).

The conclusions are as follows.

1.  A simple superpacket is not an anchored permutation.  It is exactly an unoriented cyclic necklace of (m) unordered dominoes.  Its anchored representation multiplicity is
    \[
    \mu=n2^m=2^{m+1}m.
    \]
    Hence the simple catalogue has
    \[
    |\mathcal Q|=\frac{(n-1)!}{2^m},
    \qquad
    D=2^{1-m}R!(n-R)!
    \]
    at every target.  Parallel labelled representations may not be counted as independent choices in a matching argument.

2.  The exact maximum target-pair codegree and the normalized internal collision energy are
    \[
    \frac{\Delta _2}{D}=\frac5{R(n-R)}
      =\frac{5+o(1)}{m^2},
    \qquad
    \eta=\frac{25n}{R(n-R)}+O(m^{-3})
      =\frac{50+o(1)}m.
    \]
    The largest triple codegree is
    \[
    \frac{\Delta _3}{D}
      =\frac6{R(R-1)(n-R)}
      =\frac{6+o(1)}{m^3}.
    \]

3.  The full template-divisibility sequence is
    \[
    g_0=2n,\qquad g_1=2R,\qquad g_2=2,
    \qquad g_j=1\quad(3\le j\le R).
    \]
    Thus a matching leave must be coordinate-regular and have even pair-degrees, but there is no higher parity law.  Proposition 6.4 below realizes the complete inhomogeneous syndrome, including \(N\bmod2n\), by a simple leave of size at most \(2n^2 2^m=o(N)\).  Hence these arithmetic conditions cannot force a positive-density leave.

4.  The uniform edge weighting is an exact fractional perfect matching.  The target 2-section is complete, the column-conflict graph has diameter at most two, balanced half-layer cuts have a factor \(\Theta(\sqrt m)\) of slack, and total or fixed-single-state lower/upper quartet counts give no deficit.  Consequently no ordinary fractional dual cut, invariant-component cut, balanced-half cut, or fixed-single-state quartet count rescues the annular route.  Arbitrary subset cuts in the ordered quartet projection remain among the possible integral obstructions.

5.  A matching covering \(N-o(N)\) targets would force
    \[
    \widetilde E_{q_0+1}\ge
      \left(\frac14-o(1)\right)N=\Theta(W)
    \]
    at the first deeper annular layer.  Therefore such a near-factor would rigorously disprove the sufficiency of uncoloured entrance matching.

6.  The near-factor itself remains an integral global question.  All scalar parameters remain favourable down to \(z=m^{-1/3}\):
    \[
    \log\!\bigl(Dz^{4m-1}\bigr)
       =\frac23m\log m-O(m),
    \qquad
    \eta_z,\alpha_z=O(m^{-2/3}).
    \]
    The remaining gate is not another first-order cut.  It is a trajectory/absorption theorem controlling the highly nonuniform intersections between simple superpackets, including rare pairs sharing an entire \(n\)-target component packet.

In particular, the present calculation neither proves nor refutes existence of a near-factor.  It does prove that every currently visible low-order cut fails to provide the hoped-for rescue.

---

## 1. Definitions

All indices on coordinates are cyclic modulo (n), and all indices on dominoes are cyclic modulo (m).

For a cyclic order (P=(x_0,\ldots,x_{n-1})), write
\[
I_j^\ell(P)=\{x_j,x_{j+1},\ldots,x_{j+\ell-1}\},
\qquad
E_\ell(P)=\{I_j^\ell(P):j\in\mathbb Z_n\}.
\]
The domino twin (P^\tau) is obtained by interchanging positions (2i) and (2i+1) for every (i\in\mathbb Z_m).  The entrance superpacket is
\[
Q(P)=E_R(P)\cup E_R(P^\tau).
\]

Let \(\mathcal Q\) be the set of distinct subsets (Q(P)\subseteq\binom{[n]}R), with repetitions from different anchored orders removed.  The **simple domino-twin hypergraph** is
\[
\mathcal H^\square=(V,\mathcal Q),
\qquad V=\binom{[n]}R.
\]
It has rank
\[
K=|Q|=2n=4m.
\]

For targets (A,B\in V), write (d(A)) for their common vertex degree and (d(A,B)) for their pair codegree in the simple catalogue.  By transitivity (d(A)=D) is constant.  Define
\[
\eta(Q):=
 \sum_{\{A,B\}\in\binom Q2}\frac{d(A,B)}D.
\]
The value is independent of (Q), so it will be denoted simply by (\eta).

A **near-factor** means a matching (\mathcal M\subseteq\mathcal Q) whose leave
\[
\mathcal L:=V\setminus\bigcup_{Q\in\mathcal M}Q
\]
satisfies (|\mathcal L|=o(N)).

---

## 2. Twin overlap and the first deeper repeat

### Lemma 2.1 (exact component overlap)

For (2\le\ell\le n-2),
\[
|E_\ell(P)\cap E_\ell(P^\tau)|=
\begin{cases}
n/2,&\ell\text{ is even},\\
0,&\ell\text{ is odd}.
\end{cases}
\]

#### Proof

Partition the positions into the dominoes
\[
B_i=\{x_{2i},x_{2i+1}\}.
\]
If (\ell=2s), an interval whose two endpoints lie on domino boundaries is the union of (s) consecutive dominoes and is unchanged as a set by all internal swaps.  There are (m=n/2) such intervals.  An interval starting in the middle of a domino has one unmatched coordinate at each endpoint; after applying (\tau), both endpoint choices change, so it is not an interval with the same coordinate set in the original order.  Hence the intersection has size (m).

If (\ell=2s+1), every interval has exactly one split domino.  The twin operation changes the chosen member of that split domino.  Since (2\le\ell\le n-2), this change cannot be hidden by taking the complementary cyclic interval.  Thus no target occurs in both component packets. ∎

Since (R) is odd, (Q(P)) is a disjoint union at the entrance.  At depth displacement (d), the interval length is (R-d), so the two components overlap in (n/2) targets whenever (d) is odd.

### Corollary 2.2 (linear first-deeper repeat forced by a near-factor)

Let (\mathcal M\) be a matching of (T) entrance superpackets.  Counting the two ordinary component packets of every selected superpacket at length (R-1), their repeat excess is at least (nT/2).  If (2nT=N-o(N)), then after subtracting the unavoidable scalar rank floor,
\[
\widetilde E_{q_0+1}
 \ge \frac{nT}{2}-o(N)
 =\left(\frac14-o(1)\right)N.
\]

#### Proof

Each selected (Q) contributes (n/2) targets occurring in both of its component packets.  If the same deeper target receives (2s) occurrences from (s) selected twins, its contribution to repeat excess is (2s-1\ge s).  Summing therefore gives at least (nT/2), with no assumption that contributions from different (Q)'s are disjoint.

Moreover
\[
N_{R-1}=\binom n{R-1}
=N\frac{R}{n-R+1}=N-o(N)
\]
in the Gaussian regime, so the scalar mismatch between (2nT) and the next rank is (o(N)).  This proves the claim. ∎

---

## 3. Exact domino-necklace normal form

### Theorem 3.1 (normal form)

Put (R=2r+1).  For every anchored order (P), define
\[
B_i=\{x_{2i},x_{2i+1}\},
\qquad
C_i=B_i\cup B_{i+1}\cup\cdots\cup B_{i+r-1}.
\]
Then
\[
\boxed{
Q(P)=
 \bigl\{C_i\cup\{z\}:
 i\in\mathbb Z_m,
 z\in B_{i-1}\cup B_{i+r}\bigr\}.}
\tag{3.1}
\]
In particular, every (C_i) is an intrinsic lower core supporting all four of its boundary extensions.

#### Proof

An odd interval of length (2r+1) contains (r) whole dominoes and one endpoint coordinate from one of the two adjacent boundary dominoes.  If its starting position is even, the whole dominoes are (B_i,\ldots,B_{i+r-1}) and its split endpoint lies in (B_{i+r}).  If its starting position is odd, the same core is obtained after shifting the core index, and the split endpoint lies in (B_{i-1}).  Applying (\tau) exchanges the two possible members of the split boundary domino.  Thus the union of the two packets consists of all four displayed extensions.

Different displayed extensions are distinct because (R<n/2), and Lemma 2.1 already gives (|Q|=2n=4m). ∎

### Lemma 3.2 (coordinate-pair census inside one superpacket)

For a coordinate (x),
\[
d_Q(x):=|\{A\in Q:x\in A\}|=2R.
\tag{3.2}
\]
For distinct coordinates (x,y), let their domino blocks have cyclic distance (d\le m/2).  Then
\[
d_Q(x,y)=
\begin{cases}
2(R-1),&x,y\text{ are the two members of one }B_i,\\
2(R-2d),&1\le d\le r,\\
0,&d>r.
\end{cases}
\tag{3.3}
\]

#### Proof

Equation (3.2) also follows by adding the (R) occurrences in each component packet.  For (3.3), a mate pair is contained precisely when its domino is wholly internal to the core; summing the four extensions over the (r) possible core positions gives (4r=2(R-1)).

For two different blocks at distance (1\le d\le r), there are (r-d) core positions in which both blocks are internal, contributing four extensions each.  There are two further boundary configurations in which one block is internal and the required coordinate of the other is the split endpoint.  This gives
\[
4(r-d)+2=2(R-2d).
\]
At distance greater than (r), an (R)-interval cannot contain both. ∎

### Corollary 3.3 (recoverability and stabilizer)

For all sufficiently large (m), (Q) determines both:

1. its perfect matching into dominoes, and
2. the unoriented cyclic order of those dominoes.

Consequently
\[
\operatorname{Stab}_{S_n}(Q)=C_2^m\rtimes D_m,
\qquad
|\operatorname{Stab}_{S_n}(Q)|=2^m(2m)=n2^m.
\tag{3.4}
\]

#### Proof

By (3.3), domino mates are exactly the coordinate pairs of maximum internal cooccurrence (2(R-1)).  After contracting these pairs, adjacent blocks are exactly the distinct blocks of maximum positive cooccurrence below the mate value, namely (2(R-2)).  Thus the matching and the unoriented block cycle are recovered from (Q).

Independent flips inside the (m) dominoes and every dihedral symmetry of the block cycle preserve (3.1), giving (C_2^m\rtimes D_m).  Recoverability shows there are no further permutations. ∎

### Corollary 3.4 (simple catalogue and component incidence)

The number of simple superpackets and their common vertex degree are
\[
|\mathcal Q|=\frac{n!}{n2^m}=\frac{(n-1)!}{2^m},
\tag{3.5}
\]
\[
\boxed{D=2^{1-m}R!(n-R)!.}
\tag{3.6}
\]
Every simple (Q) has (2^m) distinct ordinary component-packet traces, paired into (2^{m-1}) twin decompositions.  Conversely, every ordinary unoriented cyclic packet trace belongs to exactly two simple (Q)'s.

#### Proof

Equation (3.5) is orbit-stabilizer.  Double-counting incidences ((A,Q)) gives
\[
D=\frac{|\mathcal Q|\,2n}{\binom nR}
=2^{1-m}R!(n-R)!.
\]
Each choice of orientations of all dominoes gives a component cyclic order; global reversal identifies the twin decompositions in pairs, yielding the stated counts.  Alternatively, the final assertion follows by double-counting component traces: there are ((n-1)!/2) ordinary unoriented traces, whereas (|\mathcal Q|2^m=(n-1)!). ∎

The last statement is important dynamically: two distinct simple columns can share an entire (n)-target ordinary packet.  Such large overlaps are rare, but they prohibit replacing the simple catalogue by a fictitious independent labelled catalogue.

---

## 4. Exact target-pair codegrees

Let (A,B\in\binom{[n]}R) be distinct and put
\[
t=|A\cap B|,
\qquad h=R-t.
\]
Define
\[
\lambda_0=R!^2(g+1)!,
\qquad
\lambda_t=2(R-t)!^2t!(g+t)!\quad(t>0),
\tag{4.1}
\]
and
\[
a_t=
\begin{cases}
3,&t=1\text{ or }t=R-1,\\
2,&\text{otherwise}.
\end{cases}
\tag{4.2}
\]

### Theorem 4.1 (exact pair codegrees)

In the anchored labelled presentation,
\[
D_{\rm lab}=2nR!(n-R)!,
\tag{4.3}
\]
and
\[
d^{\rm lab}_0
=2n\frac{2g+1}{g+1}\lambda_0,
\tag{4.4}
\]
\[
d^{\rm lab}_t=n(2+a_t)\lambda_t
\qquad(1\le t\le R-1).
\tag{4.5}
\]
Every expression in (4.3)--(4.5) is divided by the same multiplicity (n2^m) in the simple catalogue.  Equivalently,
\[
\frac{d(A,B)}D=
\begin{cases}
\displaystyle
\frac{2g+1}{\binom{n-R}{R}},&t=0,\\[3mm]
\displaystyle
\frac{2+a_t}{\binom Rh\binom{n-R}h},&1\le t\le R-1.
\end{cases}
\tag{4.6}
\]

#### Proof

First count anchored representations together with a distinguished
occurrence of a target.  There are \(2n\) possible target slots among
the two component packets, followed by \(R!\) orders of the target
coordinates and \((n-R)!\) orders of the complement.  This gives
(4.3).

We next count the unordered target pairs of every intersection type
inside one \(Q\), directly in position space.  Fix
\[
I_s=\{s,s+1,\ldots,s+R-1\},\qquad
J=\tau(I_0)=\{0,1,\ldots,R-2\}\cup\{R\}.
\]
As \(s\) runs once around \(\mathbb Z_n\), the multiplicities of
\(|I_s\cap J|=t\) are
\[
\begin{array}{c|cccc}
t&0&1&2\le t\le R-2&R-1\\ \hline
\text{multiplicity}&g&3&2&3 .
\end{array}
\tag{4.7a}
\]
Indeed, the two ordinary left/right approaches give multiplicity two
at every positive overlap; the displaced singleton of \(J\) gives one
extra position at \(t=1,R-1\), and the remaining \(g\) positions are
disjoint.  Explicitly, the three starts at \(t=R-1\) are
\(-1,0,1\), and those at \(t=1\) are
\(-(R-1),R-1,R\).  The identity
\[
g+3+3+2(R-3)=n
\]
checks that all starts have been exhausted.

The two same-component cyclic packets together contain \(2n\)
unordered pairs of each positive intersection type and \(n(g+1)\)
disjoint pairs.  The cross-component pairs contribute \(3n\) at
\(t=1,R-1\), \(2n\) at every interior positive \(t\), and \(ng\) at
\(t=0\).  Thus, writing \(b_t\) for the internal pair count,
\[
b_0=n(2g+1),\qquad
b_t=n(2+a_t)\quad(1\le t\le R-1).
\tag{4.7b}
\]

There are
\[
\frac N2\binom Rt\binom{n-R}{R-t}
\]
unordered target pairs of intersection \(t\).  Double-counting
\((Q,\{A,B\})\), and using \(DN=|\mathcal Q|\,2n\), gives
\[
\frac{d(A,B)}D
=\frac{b_t}
 {n\binom Rt\binom{n-R}{R-t}}.
\tag{4.7c}
\]
Substitution of (4.7b), together with
\(\binom Rt=\binom Rh\), is exactly (4.6).  Multiplying (4.6) by
\(D_{\rm lab}\) and simplifying the factorials gives (4.4)--(4.5).
Finally, Corollary 3.3 divides all labelled degrees and codegrees by
the same \(n2^m\), as required. ∎

### Corollary 4.2 (maximum codegree)

For Gaussian (R=m-O(\sqrt m)),
\[
\boxed{
\frac{\Delta_2}{D}=\frac5{R(n-R)}
=\frac{5+o(1)}{m^2}.}
\tag{4.7}
\]

#### Proof

At (t=R-1), (4.6) equals (5/[R(n-R)]).  At (t=1), the denominator is (R\binom{n-R}{R-1}), which is exponentially larger.  For (2\le h\le R-2), both binomial factors are at least their endpoint values needed to make the ratio smaller.  The disjoint value is exponentially small. ∎

---

## 5. Internal collision structure, quartets, and triples

### Lemma 5.1 (pair strata within a fixed edge)

Let (b_t) be the number of unordered pairs ({A,B}\subset Q) with (|A\cap B|=t).  Then
\[
b_0=n(2g+1),
\tag{5.1}
\]
\[
b_1=b_{R-1}=5n,
\tag{5.2}
\]
and
\[
b_t=4n\qquad(2\le t\le R-2).
\tag{5.3}
\]

#### Proof

These are precisely the position-space counts (4.7a)--(4.7b) in the
proof of Theorem 4.1.  As an independent check, they sum to
\[
\binom{2n}{2},
\]
the total number of target pairs in \(Q\). ∎

### Theorem 5.2 (exact collision energy)

The normalized collision energy is
\[
\begin{aligned}
\eta={}&
\frac{n(2g+1)^2}{\binom{n-R}{R}}
+\frac{25n}{R\binom{n-R}{R-1}}\\
&+16n\sum_{h=2}^{R-2}
 \frac1{\binom Rh\binom{n-R}h}
+\frac{25n}{R(n-R)}.
\end{aligned}
\tag{5.4}
\]
Consequently
\[
\boxed{
\eta=\frac{25n}{R(n-R)}+O(m^{-3})
=\frac{50+o(1)}m.}
\tag{5.5}
\]

#### Proof

Insert (4.6) and (5.1)--(5.3) into the definition of (\eta).  This gives (5.4).  The (h=1) term is the displayed last term.  The (h=2) term is (O(m^{-3})), and successive interior terms decay further away from the endpoint.  The (t=1) and disjoint terms are exponentially small in the Gaussian regime. ∎

### Theorem 5.3 (alternating quartet chain)

Every (Q) has:

- (m) lower quartets consisting of the four extensions of (C_i), and
- (m) upper quartets consisting of four selected facets of an ((R+1))-set (U_i).

These form an alternating cyclic chain of lower and upper (K_4)'s in the distance-one Johnson graph.  Consecutive cliques share an edge.  The union contains exactly (10m=5n) Johnson edges and is 5-regular on the (4m) targets of (Q).

For a prescribed lower pair ((S,D_4)), where (|S|=R-1), (D_4\subset[n]\setminus S), and (|D_4|=4), the number of simple superpackets realizing the quartet
\[
\{S\cup\{z\}:z\in D_4\}
\]
as an intrinsic lower quartet is
\[
L_4=\frac{3(R-1)!(n-R-3)!}{2^{m-2}}.
\tag{5.6}
\]
For a prescribed upper pair ((U,D_4)), where (|U|=R+1), (D_4\subset U), the number realizing the four facets (U\setminus\{z\}), (z\in D_4), is
\[
U_4=\frac{3(R-3)!(n-R-1)!}{2^{m-2}}.
\tag{5.7}
\]

#### Proof

The lower quartets are explicit in (3.1).  Put
\[
U_i=C_i\cup B_{i+r}.
\]
The two diamonds on the incidences (C_i\subset U_i) and (C_{i+1}\subset U_i) produce the upper quartet.  Following the block cycle yields
\[
C_0-U_0-C_1-U_1-\cdots-C_{m-1}-U_{m-1}-C_0.
\tag{5.8}
\]
Each incidence contributes the two intermediate (R)-sets.  Counting the clique edges with their consecutive overlaps gives (10m); (5.2) gives the same total independently.

For (5.6), double-count pairs consisting of a simple (Q) and one of its (m) lower quartet positions.  There are
\[
\binom n{R-1}\binom{n-R+1}4
\]
possible prescribed pairs ((S,D_4)), and the symmetric group is transitive on them.  Therefore
\[
L_4=
\frac{|\mathcal Q|m}
 {\binom n{R-1}\binom{n-R+1}4}
=\frac{3(R-1)!(n-R-3)!}{2^{m-2}}.
\]
The upper formula follows identically from
\[
U_4=
\frac{|\mathcal Q|m}
 {\binom n{R+1}\binom{R+1}4}.
\]
∎

### Corollary 5.4 (triple maximum)

For sufficiently large Gaussian parameters,
\[
\boxed{
\frac{\Delta_3}{D}
=\frac6{R(R-1)(n-R)}.}
\tag{5.9}
\]
It is attained by three selected facets of a common upper ((R+1))-set.  Three extensions of a common lower core have relative codegree
\[
\frac6{R(n-R)(n-R-1)},
\tag{5.10}
\]
which is smaller because (R<n-R).

#### Proof

If some pair in the triple has Johnson distance at least two, its triple
codegree is at most that pair's codegree.  By (4.6), this is at most
\[
\frac4{\binom R2\binom{n-R}2}=O(m^{-4}),
\]
which is smaller than either displayed (m^{-3}) value.  It remains to
consider a triangle in the Johnson graph.  The elementary classification
of Johnson triangles says that its three vertices are either three
extensions of one common ((R-1))-set or three facets of one common
((R+1))-set: writing two neighbors of (A) as one-element exchanges
makes this immediate according as their deleted or inserted elements
coincide.

For three facets of a fixed upper top, the fourth omitted coordinate in
the selected quartet has (R-2) choices.  Hence the codegree is
((R-2)U_4), and (5.7), divided by (D), gives
\[
\frac{(R-2)U_4}{D}
=\frac6{R(R-1)(n-R)}.
\]
For three extensions of a fixed lower core, the fourth extension
coordinate has (n-R-2) choices.  Thus
\[
\frac{(n-R-2)L_4}{D}
=\frac6{R(n-R)(n-R-1)}.
\]
Because (R<n-R), the upper value is the larger one. ∎

---

## 6. Exact design divisibility and leave constraints

For (0\le j\le R), define the template gcd
\[
g_j:=\gcd\{d_Q(S):S\in\tbinom{[n]}j\},
\qquad
d_Q(S)=|\{A\in Q:S\subseteq A\}|.
\]

### Theorem 6.1 (complete template-gcd sequence)

For the domino-twin template,
\[
\boxed{
g_0=2n,\quad g_1=2R,\quad g_2=2,
\quad g_j=1\ (3\le j\le R).}
\tag{6.1}
\]

#### Proof

The first two values are (|Q|=2n) and (3.2).  Formula (3.3) shows every coordinate-pair degree is even, while a pair in blocks at distance (r) has degree exactly two.  Hence (g_2=2).

For (j\ge3), use anchored positions and take
\[
S_j=\{0,1,R-1\}\cup T,
\qquad
T\in\binom{\{2,\ldots,R-2\}}{j-3}.
\]
Exactly the original interval (I_0^R(P)) contains these positions.  The twin image of the initial triple contains positions (0,1,R), which fit in no common cyclic (R)-interval because (n>2R).  Thus (d_Q(S_j)=1), proving (g_j=1). ∎

### Theorem 6.2 (necessary leave equations)

If (T) pairwise disjoint superpackets are selected and their leave is (\mathcal L), then
\[
|\mathcal L|=N-2nT,
\tag{6.2}
\]
\[
d_{\mathcal L}(x)
=\binom{n-1}{R-1}-2RT
=\frac{R|\mathcal L|}{n}
\quad\text{for every }x,
\tag{6.3}
\]
and
\[
d_{\mathcal L}(x,y)
\equiv\binom{n-2}{R-2}\equiv0\pmod2
\quad\text{for every }x\ne y.
\tag{6.4}
\]
There is no universal congruence at orders (j\ge3).

#### Proof

Equations (6.2) and (6.3) follow by subtracting (T) copies of the template 0- and 1-degrees from the complete layer.  Every selected template has even pair degrees, proving the first congruence in (6.4).  Since (n-2) is even and (R-2) is odd,
\[
(1+x)^{n-2}=(1+x^2)^{(n-2)/2}\quad\text{over }\mathbb F_2
\]
has zero coefficient at (x^{R-2}), proving the second congruence.  Theorem 6.1 removes all higher universal congruences. ∎

For an exact factor, the apparent coordinate divisibility is not independent: if (2n\mid N), then
\[
\binom{n-1}{R-1}=\frac RnN
\]
is automatically divisible by (2R).  Thus the only independent exact arithmetic requirement is the edge-count divisibility (2n\mid N).

### Proposition 6.3 (polynomial witness against a macroscopic parity cut)

Let (b=q_0-1), and assume (b\ge3) and (4b<m).  There is a simple family (\mathcal L_0\subseteq\binom{[n]}R) such that
\[
|\mathcal L_0|=n(R+1)=O(m^2),
\tag{6.5}
\]
every coordinate has the same degree in (\mathcal L_0), and every pair-degree is even.

#### Proof

Identify the even coordinates with (\mathbb Z_m).  Put
\[
B=\{0,1,\ldots,b-2\}\cup\{2b\}
\subset\mathbb Z_m
\]
and let (S) be the set of even coordinates whose block indices are outside (B).  Then
\[
|S|=m-b=R+1.
\]
For every nonzero (d\in\mathbb Z_m), the assumption (4b<m) and the explicit interval-plus-outlier form of (B) give
\[
|B\cap(B+d)|\le b-2.
\]
Indeed, choose the signed representative of (d).  By symmetry it is
enough to take (1\le d\le m/2).  If (d>2b), the two copies are
disjoint because (B\subset[0,2b]) and (4b<m).  For
(1\le d\le2b), there is no wraparound.  The two interval parts meet
in (b-1-d\le b-2) points when (d\le b-2), and do not meet
otherwise.  The outlier (2b) can lie in the translated interval only
when (b+2\le d\le2b), in which range the interval parts are already
disjoint; it then contributes just one point.  The translated outlier
lies beyond (2b).  This proves the displayed bound.

Hence two distinct even translates of (S) intersect in at most (R-1) coordinates; an even and an odd translate are disjoint.  It follows that the families
\[
\binom{S+u}R,\qquad u\in\mathbb Z_n,
\]
are pairwise disjoint.  Define their union to be (\mathcal L_0).

It has (n(R+1)) members and is coordinate-regular by translation symmetry.  Inside each ((R+1))-set (S+u), a fixed coordinate pair belongs to exactly
\[
\binom{R-1}{R-2}=R-1
\]
of its (R)-facets.  Since (R-1) is even, every pair-degree in the union is even. ∎

This witness has residue zero modulo \(2n\), so it does not by itself
realize the actual inhomogeneous leave syndrome.  The next proposition
supplies that missing residue by a different, global construction.

### Proposition 6.4 (exact syndrome compression)

For every \(n=2m\) and odd \(R\) in the stated Gaussian regime, there
is a simple family \(\mathcal L_{\rm syn}\subseteq\binom{[n]}R\) such
that
\[
|\mathcal L_{\rm syn}|\equiv N\pmod{2n},
\tag{6.6}
\]
\[
d_{\mathcal L_{\rm syn}}(x)
=\frac{R|\mathcal L_{\rm syn}|}{n}
\quad\text{for every }x,
\tag{6.7}
\]
\[
d_{\mathcal L_{\rm syn}}(x,y)\equiv0\pmod2
\quad\text{for every }x\ne y,
\tag{6.8}
\]
and
\[
|\mathcal L_{\rm syn}|<2n^2 2^m=o(N).
\tag{6.9}
\]
Thus every displayed pointwise template-gcd condition in Theorem 6.2
has a sublinear simple leave witness with the actual complete-layer
syndrome.

#### Proof

Identify the ground set with \(\mathbb Z_n\), and partition the complete
\(R\)-layer into its orbits under cyclic translation.  Every such orbit
\(\mathcal O\) is itself a simple translation-invariant family.  Hence
its coordinate degrees are all equal, necessarily to
\[
\frac{R|\mathcal O|}{n}.
\tag{6.10}
\]

There are exactly \(m\) translation orbits of unordered coordinate
pairs, indexed by their cyclic distance \(d=1,\ldots,m\).  For a layer
orbit \(\mathcal O\), define its finite syndrome
\[
\sigma(\mathcal O)=
\left(
 |\mathcal O|\bmod 2n,\,
 \bigl(d_{\mathcal O}(\{0,d\})\bmod2\bigr)_{d=1}^{m}
\right)
\in G,
\tag{6.11}
\]
where
\[
G:=\mathbb Z/(2n)\mathbb Z\times\mathbb F_2^m,
\qquad |G|=2n2^m.
\]
Translation invariance ensures that the \(m\) parity bits encode the
pair degree of every unordered coordinate pair, including the
antipodal distance \(m\).

The sum of the syndromes of all layer orbits is the syndrome of the
complete \(R\)-layer.  Its first coordinate is \(N\bmod2n\).  Every
pair has complete-layer degree
\[
\binom{n-2}{R-2}\equiv0\pmod2
\]
by Theorem 6.2.  Therefore
\[
\sum_{\mathcal O}\sigma(\mathcal O)
=(N\bmod2n,0,\ldots,0).
\tag{6.12}
\]

We use the elementary finite-group compression lemma: from any finite
sequence in a group \(G\), one may retain a subsequence of at most
\(|G|-1\) terms having the same sum.  Indeed, whenever at least
\(|G|\) terms remain, the initial zero and the successive partial sums
contain two equal elements of \(G\); the intervening nonempty block has
sum zero and may be deleted.  Iterate.

Apply this lemma to the list of layer-orbit syndromes.  Let
\(\mathscr O_*\) be the retained collection and set
\[
\mathcal L_{\rm syn}:=\bigcup_{\mathcal O\in\mathscr O_*}\mathcal O.
\]
The union is simple because the translation orbits partition the
layer.  Its syndrome is (6.12), proving (6.6) and (6.8), while the sum
of (6.10) proves exact coordinate regularity (6.7).  Each orbit has at
most \(n\) members, so
\[
|\mathcal L_{\rm syn}|
\le n(|G|-1)<2n^2 2^m.
\]
Finally, uniformly for \(q_0=O(\sqrt m)\),
\[
\log N=2m\log2-O(\log m),
\]
whereas
\[
\log(2n^2 2^m)=m\log2+O(\log m).
\]
Their ratio tends to zero exponentially, proving (6.9).

Finally, (6.6) makes
\[
T:=\frac{N-|\mathcal L_{\rm syn}|}{2n}
\]
an integer, and (6.7) is exactly
\[
d_{\mathcal L_{\rm syn}}(x)
=\binom{n-1}{R-1}-2RT.
\]
Thus all equations in Theorem 6.2 hold with the same \(T\).  This does
not assert that the complement of \(\mathcal L_{\rm syn}\) factors into
superpackets.  In particular it does not exclude a mixed Smith-normal-
form congruence of the full incidence matrix, an odd-set inequality, or
an ordered-quartet cut; those belong to the integral incidence-semigroup
problem left in Theorem 9.3. ∎

---

## 7. Hall-type and geometric cuts

### Theorem 7.1 (fractional neutrality)

The simple hypergraph has an exact fractional perfect matching.  Namely,
\[
x_Q=\frac1D\qquad(Q\in\mathcal Q)
\tag{7.1}
\]
satisfies
\[
\sum_{Q\ni A}x_Q=1\qquad(A\in V)
\]
and has total mass (N/(2n)).  The constant dual cover
\[
y_A=\frac1{2n}\qquad(A\in V)
\tag{7.2}
\]
has the same value.

Consequently no ordinary nonnegative vertex-weight Hall dual can certify a deficit below (N/(2n)).

#### Proof

Regularity gives the vertex equations in (7.1), and double counting gives
\[
\sum_Qx_Q=\frac{|\mathcal Q|}{D}=\frac N{2n}.
\]
Every edge contains (2n) vertices, so (7.2) is feasible with equal value.  Linear-programming duality proves the assertion. ∎

### Proposition 7.2 (no component cut)

The target 2-section is complete: every two distinct (R)-sets lie together in at least one simple superpacket.  The column-conflict graph therefore has diameter at most two.

#### Proof

Every possible intersection size (0\le t\le R-1) has positive codegree in (4.6).  Thus every target pair is adjacent in the 2-section.  Given two columns (Q,Q'), choose (A\in Q) and (B\in Q').  A third column containing (A,B) intersects both, so the column-conflict distance is at most two. ∎

### Proposition 7.3 (balanced half-layer cuts have large slack)

Fix a balanced coordinate half (H_0\subset[n]), (|H_0|=m), and define
\[
\mathcal B_\pm=
\left\{A\in\binom{[n]}R:
 |A\cap H_0|=\frac{R\pm1}{2}\right\}.
\]
Every ordinary cyclic packet meets both (\mathcal B_-) and (\mathcal B_+), hence every (Q) meets each in at least two targets.  Moreover
\[
|\mathcal B_\pm|
=\left(\frac2{\sqrt{\pi m}}+o(m^{-1/2})\right)N.
\tag{7.3}
\]
The resulting matching upper bound is (\Theta(N/\sqrt m)), whereas a near-factor needs only
\[
T\sim\frac N{4m}.
\]
Thus these cuts have a factor (\Theta(\sqrt m)) of slack.

#### Proof

Along a cyclic packet, the quantity (|I_j^R(P)\cap H_0|) changes by at most one at every shift and has average (R/2), a half-integer.  It must therefore attain both adjacent integer values.  Applying this to both twin components gives the incidence lower bound.  Equation (7.3) is the central local estimate for the hypergeometric distribution with variance (m/8+o(m)). ∎

### Proposition 7.4 (total and fixed-single-state quartet counts)

Every (Q) uses (m) distinct lower cores and (m) distinct upper tops.  In a putative near-factor,
\[
mT=\left(\frac14+o(1)\right)N.
\]
Since both adjacent layers have \((1+o(1))N\) states and every prescribed four-boundary choice occurs with the exact positive multiplicities (5.6)--(5.7), neither the total shore count nor any fixed single lower-core or upper-top count yields a scalar capacity deficit.  This statement does **not** verify Hall inequalities for arbitrary subsets of cores, tops, or boundary-labelled states.

There is nevertheless a genuine necessary ordered condition.  Pair the
two intermediate \(R\)-sets on every incidence \(C_i\subset U_i\) in
(5.8).  The resulting \(2m\) Johnson edges partition the \(4m\) targets
of \(Q\).  Color each such edge below by the intersection of its two
targets and above by their union.  Every lower color (C_i) and every
upper color (U_i) occurs exactly twice around (5.8).  Therefore a
superpacket near-factor induces an almost perfect Johnson matching in
which both color multiplicities are even and the colored incidence
graph decomposes into the special alternating block-geodesic \(2m\)-cycles.
Even color multiplicity alone permits arbitrary alternating cycles and
does not encode the domino chronology.  No Hall deficit is presently
known in this ordered projection; arbitrary subset cuts there remain
open.

---

## 8. Entropy and thinning scales in the simple catalogue

This section corrects a potentially serious normalization mistake: the \(n2^m\) parallel anchored representations cannot be retained when estimating residual choice counts.

Let a formal product thinning retain every target with density \(z\).  The reference degree at a surviving target is
\[
D_z=Dz^{K-1}=Dz^{4m-1}.
\]
Stirling's formula gives, uniformly for \(q_0=O(\sqrt m)\),
\[
\log D
=2m\log m-(2+\log2)m+O(\log m).
\tag{8.1}
\]
Hence
\[
\log D_z
=2m\log m-(2+\log2)m+(4m-1)\log z+O(\log m).
\tag{8.2}
\]

At \(z=c/\sqrt m\),
\[
\log D_z
=\bigl(4\log c-2-\log2\bigr)m+O(\log m).
\tag{8.3}
\]
Thus a typical surviving vertex has exponentially many reference options only when
\[
c>c_{\mathrm{vert}}
:=\exp\!\left(\frac{2+\log2}{4}\right).
\tag{8.4}
\]
At \(c=1\), the reference degree is exponentially small.  The weaker threshold for the expected existence of any residual simple edge is
\[
c_{\mathrm{edge}}
:=\exp\!\left(\frac{2-\log2}{4}\right).
\tag{8.5}
\]

These square-root thresholds are not needed for the present obstruction.  It is enough to reach any \(z=o(m^{-1/4})\).  For the concrete choice
\[
z=m^{-1/3},
\tag{8.6}
\]
equation (8.2) gives
\[
\log D_z=\frac23m\log m-O(m).
\tag{8.7}
\]
The formally thinned collision and maximum-influence parameters are
\[
\eta_z=O\!\left(\frac1{mz}\right)=O(m^{-2/3}),
\tag{8.8}
\]
\[
\alpha_z
:=\frac{K\Delta_2}{Dz}
=O\!\left(\frac1{mz}\right)=O(m^{-2/3}).
\tag{8.9}
\]
For completeness, if the entrance leave is \(L=zN\), define its scalar
annular floor through a fixed Gaussian window \(q_0\le q\le b\sqrt m\) by
\[
B(L):=\sum_{q=q_0}^{b\sqrt m}(N_q-N+L)_+.
\]
The exact adjacent-rank product gives, uniformly for
\(d=o(\sqrt m)\),
\[
\frac{N_{q_0+d}}N
=\exp\!\left(-\frac{2q_0d+d^2}{m}
+O_a(m^{-1/2}+d/m)\right).
\]
Therefore positive summands occur at only
\(O_a(1+z\sqrt m)\) depths and each is at most \(L\).  Hence
\[
B(L)=O_a\!\left(L+\frac{L^2\sqrt m}{N}\right)
=O_a\!\left(Nz+Nz^2\sqrt m\right).
\tag{8.10}
\]
At \(z=m^{-1/3}\), the second term dominates and
\[
B(L)=O_a(Nm^{-1/6})=o(W).
\tag{8.11}
\]

Thus neither entropy exhaustion, pair codegree, energy, nor the scalar annular floor blocks a near-factor trajectory to the density required for the uncoloured counterexample.

There is nevertheless a real unproved issue.  Corollary 3.4 shows that distinct simple columns may share an entire \(n\)-target component packet.  Pair codegrees average this phenomenon away, but a multiround proof must control all overlap strata after conditioning on earlier selected columns.  Equations (8.7)--(8.9) are reference calculations, not a proof that the residual catalogue regenerates them.

The exact tilted observable makes this distinction explicit.  Fix a
target \(X\in F\) and, for \(0\le j\le K-2\), put
\[
a_j(F,X):=
\#\{G\in\mathcal Q:G\ne F,\ X\in G,\ |F\cap G|-1=j\}.
\tag{8.12}
\]
Condition on every target of \(F\) surviving an independent
vertex-thinning of density \(z\).  The expected number of other surviving
competitors through \(X\) is exactly
\[
\overline d_F(z)
=z^{K-1}\sum_{j=0}^{K-2}a_j(F,X)z^{-j}.
\tag{8.13}
\]
Indeed, a competitor in stratum \(j\) has \(K-1-j\) targets outside
\(F\), and precisely those targets still have to survive.  Likewise its
tilted factorial-overlap numerator is
\[
S_{p,F}(z)
=z^{K-1}\sum_{j=0}^{K-2}(j)_p\,a_j(F,X)z^{-j}.
\tag{8.14}
\]
Thus the natural conditional overlap statistic is
\[
b_{p,F}(z)=\frac{S_{p,F}(z)}{\overline d_F(z)},
\tag{8.15}
\]
not its time-zero value at \(z=1\).  The factors \(z^{-j}\) amplify
macroscopic intersection strata and show rigorously why the pair table,
the energy, and even any fixed or logarithmic collection of un-tilted
moments do not by themselves prove hereditary regeneration.  A
near-factor proof must control (8.13)--(8.15), or an equivalent stopped
hazard hierarchy, along the actual matching residual.

---

## 9. Exact proved/open boundary

### Theorem 9.1 (audited failures of the elementary cuts)

In the Gaussian regime above, the following exact statements hold:

1. there is no pointwise template gcd above order two, and the complete inhomogeneous coordinate/pair-parity leave syndrome from Theorem 6.2 has an \(o(N)\)-size simple witness;
2. no nonnegative fractional vertex-weight Hall cut has a deficit;
3. no connected-component or 2-section cut has a deficit;
4. every balanced-half one-level cut has \(\Theta(\sqrt m)\) slack;
5. total-shore and fixed-single-state lower-core/upper-top counts have no deficit.

#### Proof

Items 1--5 are respectively Theorems 6.1--6.2 and Proposition 6.4, Theorem 7.1, Proposition 7.2, Proposition 7.3, and Proposition 7.4.  This theorem deliberately does not include arbitrary subset cuts in the ordered quartet projection. ∎

### Theorem 9.2 (what a near-factor would prove)

If \(\mathcal H^\square\) has a matching with leave \(o(N)\), then there is an entrance-disjoint family of ordinary annular packets covering \(N-o(N)\) entrance targets but having repeat excess at least
\[
\left(\frac14-o(1)\right)N=\Theta(W)
\]
at the first deeper layer.  Hence uncoloured annular entrance matching, by itself, cannot imply simultaneous growing-depth control.

#### Proof

Split every selected superpacket into either of its twin component pairs and apply Corollary 2.2. ∎

### Theorem 9.3 (remaining near-factor gate; unproved)

The following is the exact missing assertion:

> **Domino-twin near-factor assertion.**  For \(R=m-q_0\) odd and \(q_0=a\sqrt m+O(1)\), the simple hypergraph \(\mathcal H^\square\) has a matching covering \(N-o(N)\) targets.

For the stronger annular contradiction with all scalar hole terms already negligible, it is enough to prove a matching leaving
\[
O(Nm^{-1/3})+o(N)
\]
targets, or more generally to regenerate a slow matching trajectory to any \(z=o(m^{-1/4})\).

This assertion is **not proved in this report**.  The exact unresolved alternatives are:

- prove a catalogue-specific slow-nibble or absorption theorem controlling the complete overlap hierarchy, including whole-component overlaps; or
- exhibit an integral ordered/blossom obstruction in the alternating diamond-cycle projection that is invisible to all vertex-weight Hall duals and to the template gcds.

The degree, codegree, energy, entropy, and cut calculations above do not decide between these alternatives.

---

## 10. Independent audit notes and caveats

1.  The domino normal form, stabilizer, simple quotient, pair-codegree maximum, collision energy, template-gcd sequence, exact syndrome-compression argument, and entropy normalization were independently rederived in separate audits.

2.  The largest correction to the earlier labelled calculation is conceptual rather than algebraic: all anchored degree and codegree formulas are correct, but every one must be divided by \(n2^m\) before applying a simple-hypergraph matching argument.

3.  It is false that the simple residual degree remains factorially large at \(z=m^{-1/2}\).  Equation (8.3) is the corrected threshold.  The safer obstruction target \(z=m^{-1/3}\) lies well above the entropy collapse and already makes the scalar annular floor \(o(W)\).

4.  Proposition 6.3 alone has residue zero.  Proposition 6.4 is the separate global argument that realizes the actual inhomogeneous pointwise syndrome; it is only a necessary-leave construction and supplies no superpacket matching or classification of the full incidence lattice.

5.  Uniform fractional matching rules out ordinary nonnegative vertex-weight Hall cuts, not integral blossom inequalities or chronology-sensitive cuts on the diamond-cycle projection.

6.  No claim of the constant-one theorem is made here.  The only implication to the main programme is the conditional negative statement in Theorem 9.2.

---

## Final verdict

The domino-twin catalogue is substantially more regular than its physical definition suggests: after quotienting representations, it is a transitive \(4m\)-uniform hypergraph with normalized pair codegree \((5+o(1))/m^2\), collision energy \((50+o(1))/m\), and an exact fractional factor.  Its audited elementary cuts show no macroscopic obstruction.

This does **not** yet prove a near-factor.  The surviving possibilities include a mixed incidence-lattice congruence, an odd-set or arbitrary-subset cut in the ordered quartet projection, or a genuinely trajectory-sensitive obstruction invisible to fractional Hall duality, the displayed pointwise template-gcd syndrome, central slices, components, and fixed-state counts.  Conversely, a trajectory theorem down to \(z=o(m^{-1/4})\) would immediately produce the desired linear deeper-repeat counterexample to uncoloured annulus matching.
