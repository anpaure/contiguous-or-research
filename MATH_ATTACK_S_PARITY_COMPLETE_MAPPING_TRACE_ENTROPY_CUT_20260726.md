# A recursive parity-complete rotor with quarter-depth joint trace recovery

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Let

\[
 E_n=\{p\in Q_n:|p|\equiv0\pmod2\},\qquad
 O_n=\{p\in Q_n:|p|\equiv1\pmod2\}.
\tag{0.1}
\]

For every

\[
                         n=4\cdot2^t\qquad(t\ge0),
\tag{0.2}
\]

there is an explicit family of neighbour permutations

\[
                         (F_{n,p})_{p\in Q_n}
\tag{0.3}
\]

with the following properties.

1. Every component of every \(F_{n,p}\) is an isometric \(C_{2n}\), and
   its direction word is \(\pi\pi\) for a permutation \(\pi\) of
   \([n]\).
2. If \(d_{n,p}(x)\) is the outgoing direction of \(F_{n,p}\), then for
   every \(x\in Q_n\) the full-cube column map

   \[
       \Theta_{n,x}(p)=p\oplus e_{d_{n,p}(x)}
       \quad(p\in Q_n)
   \tag{0.4}
   \]

   is a bijection and reverses parity. In particular its restriction is
   the exact required complete mapping \(E_n\to O_n\).
3. For both forward and reverse trajectories, every joint aligned code

   \[
   \mathcal C^{\pm}_{n,q}(p,x)=
   \bigl(J^{\pm}_{n,p,q}(x),
         p|_{(J^{\pm})^c},x|_{(J^{\pm})^c}\bigr)
   \tag{0.5}
   \]

   is injective on the full domain \(Q_n\times Q_n\), simultaneously for

   \[
                            0\le q\le n/4.
   \tag{0.6}
   \]

4. After fixing one context \(p\), the ordinary forward and reverse row
   trace codes are injective through the larger coarse depth \(n/2\).

Restricting (0.3) to even contexts and applying the exact paired-order
lift therefore gives one integral \(C_{4n}\)-factor of \(Q_{2n}\). Under
the coordinate-disjoint Johnson realization used by that lift,
every literal lower trace and every literal upper trace, from either
physical phase and in either orientation, recovers its start for every
physical length

\[
                         1\le \ell\le n/2-1.
\tag{0.7}
\]

Thus the parity complete-mapping gate and the full half-step trace gate
are positively closed at this range. Given an intended protected physical
depth \(H\), choosing the least \(n=4\cdot2^t\ge2(H+1)\) gives the exact
construction with

\[
                         2n<8(H+1)
\tag{0.8}
\]

physical cube coordinates.

The range is not being inflated. For this particular leafwise recursion,
the forward aligned code already fails at

\[
                         q=n/4+1.
\tag{0.9}
\]

For arbitrary admissible isometric paired-order constructions there is
also a universal support-capacity cut

\[
 \operatorname {Exc}_{n,q}^{\pm}
 \ge
 \left(2^{2n-1}-\binom nq\,2^{2n-2q}\right)_+.
\tag{0.10}
\]

In particular no construction can retain near-injective aligned traces at
coarse half depth \(q=n/2\). The positive quarter-depth theorem and this
half-depth obstruction are compatible; the interval between them remains
open for different, genuinely cross-leaf rotors.

## 1. The audited \(Q_4\) seed

All vector addition below is over \(\mathbb F_2\). Let \(G\) be the
successor permutation on the following two rows:

\[
\begin{aligned}
 A={}&(0000,1000,1100,1110,1111,0111,0011,0001),\\
 B={}&A\oplus0101.
\end{aligned}
\tag{1.1}
\]

Both rows are \(C_8\)'s with direction word

\[
                             1234\,1234.
\tag{1.2}
\]

Write

\[
                         G(y)=y\oplus e_{\delta(y)}.
\tag{1.3}
\]

Put

\[
 K=\langle1111,0101\rangle
   =\{0000,1111,0101,1010\}.
\tag{1.4}
\]

Reading (1.1) gives the four direction classes

\[
\begin{aligned}
 \delta^{-1}(1)&=K,\\
 \delta^{-1}(2)&=e_1+K,\\
 \delta^{-1}(3)&=e_1+e_2+K,\\
 \delta^{-1}(4)&=e_1+e_2+e_3+K.
\end{aligned}
\tag{1.5}
\]

Let

                         S=(1\ 4\ 3\ 2),
 \qquad Se_i=e_{S(i)}.
\tag{1.6}

The incoming direction at a phase of (1.2) is the predecessor of its
outgoing direction. Hence, pointwise on \(Q_4\),

\[
                         G^{-1}(y)=y\oplus e_{S\delta(y)}.
\tag{1.7}
\]

For every \(p,x\in Q_4\), including odd \(p\), define

\[
\begin{aligned}
 y&=Sp\oplus x,\\
 d_{4,p}(x)&=\delta(y),\\
 F_{4,p}(x)&=x\oplus e_{d_{4,p}(x)},\\
 \Theta_{4,x}(p)&=p\oplus e_{d_{4,p}(x)}.
\end{aligned}
\tag{1.8}
\]

### Lemma 1.1 (simultaneous row and full-column bijectivity)

Every \(F_{4,p}\) is a translated conjugate of \(G\), and every
\(\Theta_{4,x}\) is a parity-reversing permutation of the full \(Q_4\).

#### Proof

Equations (1.3), (1.7), and (1.8) give the exact identities

\[
\begin{aligned}
 Sp\oplus F_{4,p}(x)&=G(Sp\oplus x),\\
 S\Theta_{4,x}(p)\oplus x&=G^{-1}(Sp\oplus x).
\end{aligned}
\tag{1.9}
\]

The first is a row conjugacy. For fixed \(x\), the second is a conjugacy
of \(\Theta_{4,x}\) with \(G^{-1}\) under the affine bijection
\(p\mapsto Sp\oplus x\). Thus both maps are permutations. Every neighbour
map toggles parity, while coordinate permutations and the two appearances
of the translation by \(x\) preserve the net parity change. Hence
\(\Theta_{4,x}\) reverses parity. \(\square\)

The full-cube assertion, rather than only \(E_4\to O_4\), is essential:
after the recursion is split into two children, a child context can have
either parity.

### Lemma 1.2 (forward and reverse depth-one joint transversality)

Let \(J^+_{4,p,1}(x)\) be the outgoing direction of \(F_{4,p}\), and let
\(J^-_{4,p,1}(x)\) be the outgoing direction of \(F_{4,p}^{-1}\). Both
maps

\[
 (p,x)\longmapsto
 \bigl(J^\pm_{4,p,1}(x),p|_{(J^\pm)^c},x|_{(J^\pm)^c}\bigr)
\tag{1.10}
\]

are injective on \(Q_4\times Q_4\).

#### Proof

Fix a displayed direction \(i\) and all outside bits. Varying the two
missing bits \(p_i,x_i\) makes \(y=Sp\oplus x\) run through an affine
two-face parallel to

\[
                         U_i=\langle e_{S(i)},e_i\rangle.
\tag{1.11}
\]

The only weight-two supports in \(K\) are \(\{1,3\}\) and \(\{2,4\}\),
whereas

\[
 \{i,S(i)\}\in
 \bigl\{\{1,4\},\{4,3\},\{3,2\},\{2,1\}\bigr\}.
\tag{1.12}
\]

Therefore

\[
                              K\cap U_i=\{0\}.
\tag{1.13}
\]

Since both spaces have dimension two, every coset of \(K\) meets every
such affine face exactly once. In the forward case, direction \(i\) says
that \(y\) belongs to the corresponding coset in (1.5). In the reverse
case, (1.7) says that direction \(i\) is equivalent to
\(y\in\delta^{-1}(S^{-1}i)\), again a coset of \(K\). Thus the missing
bits are unique in both cases. \(\square\)

## 2. The parity-alternating recursive rotor

Suppose \(n=2h\ge8\). Split

\[
 p=(p_L,p_R),\qquad x=(u,v)\in Q_h\times Q_h,
\tag{2.1}
\]

and let \(\epsilon(z)=|z|\bmod2\). Define, for every \(p\in Q_n\),

\[
 F_{n,p}(u,v)=
 \begin{cases}
  (F_{h,p_L}(u),v),&\epsilon(u)+\epsilon(v)=0,\\
  (u,F_{h,p_R}(v)),&\epsilon(u)+\epsilon(v)=1.
 \end{cases}
\tag{2.2}
\]

Thus the rotor moves the left child at even total phase parity and the
right child at odd total phase parity.

### Theorem 2.1 (exact recursive row factors)

Every \(F_{n,p}\) is a neighbour permutation whose components are
isometric \(C_{2n}\)'s with doubled-permutation direction words.

#### Proof

Every child move toggles total parity, so the selected halves alternate.
For either starting parity,

\[
 F_{n,p}^{\,2}(u,v)
 =\bigl(F_{h,p_L}(u),F_{h,p_R}(v)\bigr).
\tag{2.3}
\]

Both child points have exact period \(2h\). Hence an even parent return
first occurs after \(2(2h)=4h=2n\) moves; an odd return is impossible by
parity. This also proves bijectivity.

During the first \(n=2h\) parent moves, each child makes \(h\) consecutive
moves. Any \(h\) consecutive letters in a child word \(\pi\pi\) contain
every child coordinate once. Hence the first \(n\) parent directions are
a permutation of all \(n\) coordinates. Each child direction phase then
repeats, as does the left-right alternation, so the next \(n\) directions
repeat the same permutation. This is the doubled-permutation criterion
for an isometric \(C_{2n}\). \(\square\)

### Theorem 2.2 (exact recursive full-column maps)

For every \(x\in Q_n\), the map \(\Theta_{n,x}\) in (0.4) is a
parity-reversing permutation of \(Q_n\).

#### Proof

The branch in (2.2) depends only on \(x\), not on \(p\). Consequently

\[
 \Theta_{n,(u,v)}(p_L,p_R)=
 \begin{cases}
  (\Theta_{h,u}(p_L),p_R),&\epsilon(u)+\epsilon(v)=0,\\
  (p_L,\Theta_{h,v}(p_R)),&\epsilon(u)+\epsilon(v)=1.
 \end{cases}
\tag{2.4}
\]

The active child map is bijective and reverses child parity by induction;
the inactive child is unchanged. Hence the parent map is bijective and
reverses total parity. Lemma 1.1 is the base. \(\square\)

Restricting (2.4) to \(E_n\) proves the exact pointwise complete-mapping
gate with no rounding, discarded owner, or common-owner synchronization
assumption.

## 3. Recursive joint trace recovery

For \(q\ge0\), let \(J^+_{n,p,q}(x)\) be the set of the first \(q\)
directions along the \(F_{n,p}\)-trajectory from \(x\), and define
\(J^-\) analogously for \(F_{n,p}^{-1}\). Isometry makes these honest
\(q\)-sets throughout the range below. For \(q=0\), interpret
\(\mathcal C_{n,0}^{\pm}\) as the complete pair \((p,x)\).

### Theorem 3.1 (quarter-depth aligned trace theorem)

For every \(n=4\cdot2^t\), both maps \(\mathcal C^+_{n,q}\) and
\(\mathcal C^-_{n,q}\) in (0.5) are injective on \(Q_n\times Q_n\) for
every integer \(0\le q\le n/4\).

#### Proof

Lemma 1.2 proves the assertion at \(n=4,q=1\), and \(q=0\) is tautological.
Assume it at \(h\), and put \(n=2h\).

For a forward window of even depth \(q=2s\), alternation in (2.2) gives
child depths

\[
                              (s,s).
\tag{3.1}
\]

The parent support split \(J\cap L,J\cap R\), together with the parent
outside restrictions, is exactly the pair of child codes

\[
 \mathcal C^+_{h,s}(p_L,u),\qquad
 \mathcal C^+_{h,s}(p_R,v).
\tag{3.2}
\]

For odd depth \(q=2s+1\), the depths are \((s+1,s)\) or \((s,s+1)\).
The two support cardinalities identify which half moved first, after which
the parent data again split into the two child codes.

If \(q\le n/4=h/2\), then in the even case \(s\le h/4\). Since
\(h/2\) is even, an odd \(q\le h/2\) actually satisfies
\(q\le h/2-1\), and hence \(s+1\le h/4\). The inductive hypothesis
recovers both child starts and contexts, proving forward injectivity.

For the inverse map, a state of odd total phase parity moves backward in
the left child, while a state of even total phase parity moves backward in
the right child. The halves again alternate; their projections are
consecutive inverse child windows with exactly the same depth split.
Lemma 1.2 supplies the reverse base, so the identical induction proves
reverse injectivity. \(\square\)

The construction is not the diagonal translation family
\(F_p(x)=p\oplus F(p\oplus x)\). That family makes every column bijective
but makes its support depend only on \(p\oplus x\), leaving an exact
\(2^{q-1}\)-element same-phase erased-context subfibre at depth \(q\)
(and possibly larger total fibres). In (2.2), the two
child contexts independently alter the recursive support; Theorem 3.1
shows that this support carries all erased phase and context bits through
quarter depth.

The underlying rows retain the larger ordinary rotor range.

### Proposition 3.2 (fixed-context half-depth rainbowness)

Fix \(p\in Q_n\). For either orientation, the ordinary row code

\[
 x\longmapsto
 \bigl(J^\pm_{n,p,q}(x),x|_{(J^\pm)^c}\bigr)
\tag{3.3}
\]

is injective for every \(0\le q\le n/2\).

#### Proof

At \(n=4,q=1\), two putative starts differ only in coordinate \(i\),
while their phase variables lie in one \(K\)-coset; this would put
\(e_i\) in \(K\), impossible. At \(q=2\), the four possible forward
supports are

\[
                         12,23,34,41,
\tag{3.4}
\]

and each support identifies its initial direction. Two starts with the
same outside phase would differ by a vector in both \(K\) and the
coordinate plane of that adjacent pair. The only weight-two supports in
\(K\) are \(13,24\), so the intersection is zero. Reverse order gives
the same four adjacent pairs. This proves the base through \(q=2=n/2\).

Under (2.2), a parent row code splits into two child row codes of depths
\((s,s)\) or \((s+1,s)\), exactly as in Theorem 3.1. If \(q\le n/2=h\),
both child depths are at most \(h/2\). The child induction therefore
recovers \(u,v\), for both orientations. \(\square\)

## 4. Literal physical half-step recovery

Restrict now to \(p\in E_n\) and apply the paired-order lift. A coarse
direction \(i\) becomes the adjacent forward physical block

\[
                              (b_i,a_i),
\tag{4.1}
\]

and the reverse block is \((a_i,b_i)\). The lift theorem and Theorems
2.1--2.2 give one exact \(C_{4n}\)-factor of \(Q_{2n}\).

The following statement uses the intended literal coordinate-disjoint
Johnson interface, not a raw unlabelled two-bit surrogate. Every physical
cube direction is represented by its own ground-coordinate swap pair. A
varied direction contributes no endpoint of that pair to a lower
intersection and both endpoints to an upper union; an untouched direction
contributes exactly one endpoint to either sign. Thus either signed target
identifies the varied physical directions, and an untouched endpoint
records its orientation bit.

### Lemma 4.1 (exact half-step reduction)

Let a physical interval have length \(\ell\), and complete it to the
smallest aligned whole-pair superinterval by adjoining at most one move at
each end. Its literal signed target determines the aligned code of that
superinterval. If \(\ell=2d\) or \(2d+1\), the required aligned depth is

\[
\begin{array}{c|c|c}
\text{physical start}&\text{physical length}&\text{aligned depth}\\ \hline
\text{block boundary}&2d&d\\
\text{block boundary}&2d+1&d+1\\
\text{block midpoint}&2d&d+1\\
\text{block midpoint}&2d+1&d+1.
\end{array}
\tag{4.2}
\]

The assertion holds for both signs and both orientations.

#### Proof

At a boundary start, a length \(2d\) interval contains \(d\) complete
blocks. A length \(2d+1\) interval contains those blocks and the first
edge of the next block. At a midpoint start, a length \(2d\) interval
contains the second edge of the initial block, \(d-1\) complete blocks,
and the first edge of the final block. A length \(2d+1\) interval contains
the second initial edge and \(d\) subsequent complete blocks. This proves
the depth table.

By the physical direction decoder, the signed target identifies all
complete and partial coarse pairs. On \(J^c\), neither physical direction
moved, so the unchanged local endpoints give both orientation bits and
hence

\[
                         x|_{J^c},\qquad p|_{J^c}.
\tag{4.3}
\]

For a missing boundary move, the aligned target is a deterministic
function of the unaligned target: on the lower side delete the currently
recorded endpoint of the newly completed swap pair, and on the upper side
adjoin its mate. Applying this operation at one or both ends produces the
aligned code at the depth in (4.2). Aligned injectivity recovers the
extended start and therefore the original start.

There is no cross-class ambiguity. A boundary-aligned even interval has
only zero-or-two direction counts in every coarse pair; a midpoint even
interval has two count-one boundary pairs. For odd length there is one
count-one pair, but a boundary start leaves an unpaired \(b\)-direction
whereas a midpoint start leaves an unpaired \(a\)-direction. The physical
direction decoder distinguishes them. Reversal interchanges \(a\) and
\(b\) throughout and gives the same conclusion. \(\square\)

### Corollary 4.2 (literal physical trace-rainbow range)

Every lower and upper physical trace map is injective, for every start
phase and in both orientations, whenever

\[
                 1\le\ell\le2\lfloor n/4\rfloor-1=n/2-1.
\tag{4.4}
\]

At \(\ell=n/2\), boundary-aligned starts still use
\(\mathcal C_{n,n/4}\), but midpoint starts require the presently
noninjective/unavailable depth \(n/4+1\). No endpoint claim at
\(\ell=n/2\) is made.

If one discards coordinate-disjoint swap-pair labels and interprets
\(Q_{2n}\) as raw unlabelled bits, a literal one-sided target need not
reveal the varied directions. Under that different interface, Lemma 4.1
proves only injectivity of the augmented half-step codes. This caveat is
structural, not asymptotic.

## 5. The exact endpoint of this recursion

The quarter-depth limit in Theorem 3.1 is sharp for the particular binary
leafwise recursion (2.2).

Let \(R=(1\ 2\ 3\ 4)\), the successor permutation in the seed word
(1.2). If a seed trajectory begins with direction \(i\), its first two
directions have support

\[
                         J_i=\{i,R(i)\}.
\tag{5.1}
\]

Put \(v_i=e_i\oplus e_{R(i)}\). Then \(v_i\) has even weight and

\[
 (I+S)v_i=e_{S(i)}\oplus e_{R(i)}\in K.
\tag{5.2}
\]

### Proposition 5.1 (parity-preserving seed collision at depth two)

For every seed start \((p,x)\) whose first direction is \(i\), the distinct
start

\[
                         (p\oplus v_i,x\oplus v_i)
\tag{5.3}
\]

has the same forward depth-two code, and has the same individual
\(p\)-parity and \(x\)-parity.

#### Proof

The phase variable changes by

\[
 S(p\oplus v_i)\oplus(x\oplus v_i)
 =(Sp\oplus x)\oplus(I+S)v_i.
\tag{5.4}
\]

By (5.2) this is a translation by \(K\). Every direction class in (1.5)
is a \(K\)-coset, so \(\delta\), and hence the entire translated direction
trajectory, is unchanged. The vector \(v_i\) is supported on the first
two directions, so all outside data in the depth-two code are unchanged.
Its even weight preserves both displayed parities. \(\square\)

### Proposition 5.2 (global failure at \(n/4+1\))

For every \(n=4\cdot2^t\), the forward code
\(\mathcal C^+_{n,n/4+1}\), even after restriction to \(E_n\times Q_n\),
is not injective.

#### Proof

The recursion has \(n/4\) leaves of dimension four. Over \(n/4\)
consecutive parent moves, repeated binary alternation sends exactly one
move to every leaf. The next move is sent to one distinguished leaf.
Thus at depth \(n/4+1\), one leaf has local depth two and all other leaves
have local depth one.

Hold every other leaf start fixed. In the exceptional leaf apply the
replacement (5.3), using its actual first two directions. The exceptional
leaf's \(x\)-parity is unchanged, so every ancestor parity test and hence
the entire leaf-interleaving schedule is unchanged. Its \(p\)-parity is
also unchanged, so the global context remains even. Proposition 5.1 gives
the same local code in the exceptional leaf; all other local codes are
identical by construction. The two distinct global starts therefore have
the same global code. \(\square\)

This is an invariant of the present leafwise rotor, not a universal
quarter-depth impossibility theorem. A different recursion with genuine
cross-leaf coding could conceivably pass \(n/4+1\).

## 6. Universal support-capacity obstruction

For aligned physical length \(2q\), there are

\[
                         |E_n|\,|Q_n|=2^{2n-1}
\tag{6.1}
\]

even-context starts. The enriched trace code has at most

\[
                         \binom nq4^{n-q}
\tag{6.2}
\]

values: choose its \(q\)-set support, then choose the two outside bits on
each of the remaining \(n-q\) cells. A literal lower or upper target has
no larger image.

### Theorem 6.1 (universal aligned Hall cut)

For every parity-indexed family whose protected aligned \(q\)-windows use
\(q\) distinct coarse directions—in particular every admissible
isometric doubled-permutation row family—independently of its column maps
or recursive structure, the cap-one collision excess at aligned depth
\(q\) is at least

\[
 \boxed{
 \left(2^{2n-1}-\binom nq\,2^{2n-2q}\right)_+}.
\tag{6.3}
\]

Therefore injectivity requires

\[
                              \binom nq\ge2^{2q-1}.
\tag{6.4}
\]

At \(q=n/2\),

\[
 \operatorname {Exc}_{n,n/2}^{\pm}
 \ge
 2^{2n-1}\left(1-\frac{2\binom n{n/2}}{2^n}\right)
 =\left(1-O(n^{-1/2})\right)2^{2n-1}.
\tag{6.5}
\]

#### Proof

Equation (6.2) is the cardinality of the full enriched-code alphabet.
Subtract it from the domain size (6.1), taking the positive part. The
central-binomial estimate gives (6.5). \(\square\)

The obstruction explains why the original half-depth request cannot be
true, but it does not touch the present quarter-depth theorem. At
\(q=n/4\), the support alphabet has enough information; Sections 1--3
give an integral rotor which actually uses it.

## 7. Audited implication boundary

The following statements are proved without omitted finite cases.

* The row factors, full-cube column bijections, and parity restrictions are
  exact for every \(n=4\cdot2^t\).
* The forward and reverse joint codes are injective on all
  \(Q_n\times Q_n\) through aligned coarse depth \(n/4\).
* Every fixed-context row separately retains ordinary two-sided trace
  rainbowness through coarse depth \(n/2\).
* Under the paired theorem's coordinate-disjoint Johnson realization, the
  result is literal, not merely an augmented-code statement, through
  physical length \(n/2-1\).
* The aligned range \(n/4\) is sharp for recursion (2.2).
* No construction can be near-injective at aligned coarse half depth.

The following are not claimed.

* No trace assertion is made at physical length \(n/2\) for midpoint
  starts.
* Proposition 5.2 does not rule out another cross-leaf construction beyond
  quarter depth.
* The theorem closes the finite parity-complete local compiler. It does
  not by itself prove the outer packet coupling, the global
  coefficient-one OR theorem, or an owner-disjoint embedding of all local
  factors into one prescribed external decomposition.
* Without the coordinate-disjoint physical-direction decoder, the
  half-step conclusion is only an augmented-code theorem.

The decisive mechanism is the combination of a \(Q_4\) transversal
complete mapping with a parity-alternating product. The former supplies
two erased bits per selected seed direction; the latter distributes a
short window recursively among independent context children while keeping
every column map a literal bijection.
